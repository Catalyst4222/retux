from enum import IntEnum
from json import dumps, loads
from logging import getLogger
from random import random
from sys import platform
from time import perf_counter
from typing import Any

from attrs import asdict, define, field
from cattrs import structure
from trio import Nursery, open_nursery, sleep
from trio_websocket import ConnectionClosed, WebSocketConnection, open_websocket_url

from ..client.flags import Intents
from ..const import MISSING, NotNeeded, __gateway_url__
from .error import (
    DisallowedIntents,
    InvalidIntents,
    InvalidShard,
    InvalidToken,
    RandomClose,
    RateLimited,
    RequiresSharding,
)
from .events.lookup import EventType

logger = getLogger(__name__)


@define()
class _GatewayMeta:
    """Represents metadata for a Gateway connection."""

    version: int = field()
    """The version of the Gateway."""
    encoding: str = field()
    """The encoding type on Gateway payloads."""
    compress: str | None = field(default=None)
    """The compression type on Gateway payloads."""
    heartbeat_interval: float | None = field(default=None)
    """The heartbeat used to keep a Gateway connection alive."""
    resume_gateway_url: str | None = field(default=None)
    """The URL for resuming Gateway connections."""
    session_id: str | None = field(default=None)
    """The ID of an existent session, used for when resuming a lost connection."""
    seq: int | None = field(default=None)
    """The sequence number on an existent session."""


class _GatewayOpCode(IntEnum):
    """Represents a Gateway event's operation code."""

    DISPATCH = 0
    """An event has been received."""
    HEARTBEAT = 1
    """A handshake sent periodically to ensure an alive connection."""
    IDENTIFY = 2
    """An identification event to start a session with the initial handshake."""
    PRESENCE_UPDATE = 3
    """An event sent to update the client's presence."""
    VOICE_STATE_UPDATE = 4
    """An event sent to update the client's voice state."""
    RESUME = 6
    """An event sent to resume a previous connection prior to disconnect."""
    RECONNECT = 7
    """An event received informing the client to reconnect."""
    REQUEST_GUILD_MEMBERS = 8
    """An event sent to receive information on offline guild members."""
    INVALID_SESSION = 9
    """
    An event received informing the client the connection has been invalidated.
    `RECONNECT` ultimately follows this.
    """
    HELLO = 10
    """An event received on a successfully initiated connection."""
    HEARTBEAT_ACK = 11
    """An event received to acknowledge a `HEARTBEAT` sent."""


@define(slots=False)
class _GatewayPayload:
    """
    Represents a Gateway payload, signifying data for events.

    The `s` (`sequence`) and `t` (`name`) attributes will only have
    a value when:

    - `op` (`opcode`) is `DISPATCH`.
    - A `RESUME` call has been made. (specific to the former)
    """

    op: int | _GatewayOpCode = field(converter=int)
    """The opcode of the payload."""
    d: Any | None = None
    """The payload's event data."""
    s: int | None = None
    """The sequence number, used for resuming sessions and heartbeats."""
    t: str | None = None
    """The name of the payload's event."""

    @property
    def opcode(self) -> int:
        """The opcode of the payload."""
        return self.op

    @property
    def data(self) -> Any | None:
        """The payload's event data"""
        return self.d

    @property
    def sequence(self) -> int | None:
        """The sequence number, used for resuming sessions and heartbeats."""
        return self.s

    @property
    def name(self) -> str | None:
        """The name of the payload's event."""
        return self.t


class GatewayClient:
    """
    Represents a connection to Discord's Gateway. Gateways are Discord's
    form of real-time communication over secure WebSockets. Clients will
    receive events and data over the Gateway they are connected to and
    send data over the REST API.

    Upon instantiation, the class will attempt to assign encoding
    and compression values. Please see the documentation when instantiating
    for more details.

    ---

    Attributes
    ----------
    token : `str`
        The bots token.
    intents : `Intents`
        The intents to connect with.
    _conn : `trio_websocket.WebSocketConnection`
        An instance of a connection to the Gateway.
    _meta : `_GatewayMeta`
        Metadata representing connection parameters for the Gateway.
    _tasks : `trio.Nursery`
        The tasks associated with the Gateway, for reconnection and heart-beating.
    _closed : `bool`
        Whether the Gateway connection is closed or not.
    _stopped : `bool`
        Whether the Gateway connection was forcefully stopped or not.
    _heartbeat_ack : `bool`
        Whether we've received the first heartbeat acknowledgement or not.
    _last_ack : `list[float]`
        The before/after time of the last Gateway event tracked. See `latency` for Gateway connection timing.
    _bots : `list[retux.Bot]`
        The bot instances used for dispatching events.
    """

    # TODO: Add sharding and presence changing.

    __slots__ = (
        "token",
        "intents",
        "_meta",
        "_tasks",
        "_closed",
        "_stopped",
        "_heartbeat_ack",
        "_last_ack",
        "_bots",
        "_conn",
    )
    token: str
    """The bots token."""
    intents: Intents
    """The intents to connect with."""
    _meta: _GatewayMeta
    """Metadata representing connection parameters for the Gateway."""
    _conn: WebSocketConnection | None
    """An instance of a connection to the Gateway."""
    _tasks: Nursery | None
    """The tasks associated with the Gateway, for reconnection and heart-beating."""
    _closed: bool
    """Whether the Gateway connection is closed or not."""
    _stopped: bool
    """Whether the Gateway connection was forcefully stopped or not."""
    _heartbeat_ack: bool
    """Whether we've received the first heartbeat acknowledgement or not."""
    _last_ack: list[float]
    """The before/after time of the last Gateway event tracked. See `latency` for Gateway connection timing."""
    _bots: list["Bot"]  # noqa
    """The bot instances used for dispatching events."""

    def __init__(
        self,
        token: str,
        intents: Intents,
        *,
        version: int = 10,
        encoding: str = "json",
        compress: NotNeeded[str] = MISSING,
    ):
        """
        Creates a new connection to the Gateway.

        Parameters
        ----------
        token : `str`
            The bots token to connect with.
        intents : `Intents`
            The intents to connect with.
        version : `int`, optional
            The version of the Gateway to use. Defaults to version `10`.
        encoding : `str`, optional
            The type of encoding to use on payloads. Defaults to `json`.
        compress : `str`, optional
            The type of data compression to use on payloads. Defaults to none.
        """
        self.token = token
        self.intents = intents
        self._meta = _GatewayMeta(
            version=version, encoding=encoding, compress=None if compress is MISSING else compress
        )

        self._conn = None
        self._tasks = None
        self._closed = True
        self._stopped = False
        self._heartbeat_ack = False
        self._last_ack = []
        self._bots = []

    async def __aenter__(self):
        self._tasks = open_nursery()
        nursery = await self._tasks.__aenter__()  # noqa
        nursery.start_soon(self.reconnect)
        nursery.start_soon(self._heartbeat)
        return self

    async def __aexit__(self, *exc):
        return await self._tasks.__aexit__(*exc)  # noqa

    async def _receive(self) -> _GatewayPayload:
        """
        Receives the next incoming payload from the Gateway.

        Returns
        -------
        `_GatewayPayload`
            A class of the payload data.
        """

        # FIXME: our exception handling neglects other rejection
        # reasons. A more thorough analysis of trio_websocket
        # is necessary to have an extensible exception of our
        # own for clarifying connection loss.

        try:
            resp = await self._conn.get_message()
            json = loads(resp)
            return structure(json, _GatewayPayload)
        except ConnectionClosed:
            logger.error("The connection to Discord's Gateway has closed.")
            await self._error()

    async def _send(self, payload: _GatewayPayload):
        """
        Sends a payload to the Gateway.

        Parameters
        ----------
        payload : `_GatewayPayload`
            The payload to send.
        """

        # TODO: implement the gateway rate limiting logic here.
        # the theory of this is to "queue" dispatched information
        # from the Gateway when we enter a rate limit.

        try:
            json = dumps(asdict(payload))
            resp = await self._conn.send_message(json)  # noqa
        except ConnectionClosed:
            logger.error("The connection to Discord's Gateway has closed.")
            await self._error()

    async def connect(self):
        """Connects to the Gateway and initiates a WebSocket state."""
        self._stopped = False
        self._last_ack = [perf_counter(), perf_counter()]

        # FIXME: this connection type will only work with JSON in mind.
        # if other compression or encoding types are supplied, they
        # will not be properly digested. This is only added so others
        # may modify their GatewayClient to their liking.

        async with open_websocket_url(
            f"{self._meta.resume_gateway_url or __gateway_url__}?v={self._meta.version}&encoding={self._meta.encoding}"
            f"{'' if self._meta.compress is None else f'&compress={self._meta.compress}'}"
        ) as self._conn:
            self._closed = bool(self._conn.closed)

            if self._stopped:
                await self._conn.aclose()
                await self.__aexit__(*self._conn.closed)
            if self._closed:
                await self._error()

            while not self._closed:
                data = await self._receive()

                if data:
                    await self._track(data)

    async def reconnect(self):
        """Reconnects to the Gateway and re-initiates a WebSocket state."""
        self._heartbeat_ack = False
        self._closed = True

        if self._conn is not None:
            await self._conn.aclose()

        await self.connect()

    async def _error(self):
        """Handles error responses from closing codes."""
        code = self._conn.closed.code if self._conn.closed is not None else 4999
        reason = self._conn.closed.reason if self._conn.closed is not None else "N/A"
        await self._conn.aclose()

        match code:
            case 1000:
                # This is a normal closure. We should never try reconnecting it, but random edge cases
                # happen when our connection is terminated with this but a RECONNECT/RESUME event is missing.
                if not self._stopped:
                    await self.reconnect()
            case 1006:
                # 1006 closing codes occur when the server mishandled data or commit a malformed action.
                logger.warning("Closing ABNORMAL state.")
                await self.reconnect()
            case 1011:
                # 1011 closing codes typically occur when the Gateway commits suicide to the
                # client connection. There is nothing wrong with the client, it's just Discord
                # being Discord.
                logger.error("Gateway has committed suicide.")
                await self.reconnect()
            case 4000:
                logger.exception(
                    RandomClose,
                    "Something went wrong with the Gateway. We'll reconnect.",
                )
                await self.reconnect()
            case 4004:
                raise InvalidToken(
                    "Your bots token is invalid. (Make sure there's a value, or reset if needed.)"
                )
            case 4008:
                # Theory-wise, the user won't need to know about the rate limit if we're handling it already.
                # We only throw non-resumable exceptions for things that cannot resume the connection.
                # FIXME: probably move away from exception logging and use a traceback formatter.
                logger.exception(
                    RateLimited,
                    "Your bot is being Gateway rate limited. You will be reconnected.",
                )
                await self.reconnect()
            case 4010:
                raise InvalidShard(
                    "You provided an invalid shard. Make sure the shard is correct! (https://discord.dev/topics/gateway#sharding)"
                )
            case 4011:
                raise RequiresSharding("Your bot requires sharding, please use autoshard=True.")
            case 4013:
                raise InvalidIntents(
                    "You provided an invalid intent. Make sure your intent is a value! (Did you also miss a | for adding more than one?)"
                )
            case 4014:
                raise DisallowedIntents(
                    "You provided an intent that your bot is not approved for. Make sure your bot is verified and/or has it enabled in the Developer Portal."
                )
            case 4999:
                logger.exception(
                    RandomClose,
                    "The Gateway client declared a closure. We'll reconnect.",
                )
                await self.reconnect()
            case _:
                raise RandomClose(f"The Gateway randomly closed. {reason}#{code}")

    async def _track(self, payload: _GatewayPayload):
        """
        Tracks data sent from the Gateway and interprets it.

        Parameters
        ----------
        payload : `_GatewayPayload`
            The payload being sent from the Gateway.
        """
        logger.debug(f"Tracking {_GatewayOpCode(payload.opcode).name}.")
        # Discord recommends to always use the last given sequence for reconnects.
        # This helps with resending payloads that were lost on a disconnect.
        self._meta.seq = payload.sequence
        self._last_ack[1] = perf_counter()

        match _GatewayOpCode(payload.opcode):
            case _GatewayOpCode.HELLO:
                if self._meta.session_id and self._meta.resume_gateway_url:
                    await self._resume()
                else:
                    await self._identify()
                    self._meta.heartbeat_interval = payload.data["heartbeat_interval"] / 1000
                    logger.debug(f"❤ -> {self._meta.heartbeat_interval}ms.")
                    self._heartbeat_ack = True
            case _GatewayOpCode.HEARTBEAT_ACK:
                logger.debug(f"❤️ ({self.latency}ms.)")
            case _GatewayOpCode.INVALID_SESSION:
                logger.info("Our Gateway connection has suddenly invalidated.")

                if bool(payload.data):
                    self._heartbeat_ack = False
                    await self._resume()
                else:
                    self._meta.session_id = None
                    await self._conn.aclose()
                    await self.reconnect()
            case _GatewayOpCode.RECONNECT:
                self._heartbeat_ack = False
                await self._resume()
            case _GatewayOpCode.DISPATCH:
                if payload.name not in ["RESUMED", "READY"]:
                    resource = EventType.__dict__.get(payload.name, MISSING)
                    if resource is not MISSING:
                        await self._dispatch(payload.name, resource.value, **payload.data)
                    else:
                        await self._dispatch(payload.name, payload.data)
                    await self._dispatch(
                        "RAW_RECEIVE",
                        {
                            **payload.data,
                            "_event_type": resource,
                            "_event_name": payload.name,
                        },
                    )
        match payload.name:
            case "RESUMED":
                logger.info(
                    f"Resumed connection. (session: {self._meta.session_id}, sequence: {self._meta.seq})"
                )
                self._heartbeat_ack = True
            case "READY":
                self._meta.session_id = payload.data["session_id"]
                self._meta.seq = payload.sequence
                self._meta.resume_gateway_url = payload.data["resume_gateway_url"]
                logger.info(
                    f"Connection is now ready. (session: {self._meta.session_id}, sequence: {self._meta.seq})"
                )
        self._last_ack[0] = perf_counter()

    async def _hook(self, bot: "Bot") -> object:  # noqa
        """
        Hooks the Gateway to a bot for event dispatching.

        ---

        The `bot` field allows for numerous bots in theory
        to be hooked onto with one `GatewayClient` process
        being ran, allowing for IPC pipes and more intuitive
        sharding.

        ---

        Parameters
        ----------
        bot : `retux.Bot`
            The bot instance to hook onto. This instance
            can be any bot instance for interchangeable
            handling of 1 main Gateway.
        """
        self._bots.append(bot)

    async def _dispatch(
        self, _name: str, data: list[dict] | dict | type | MISSING, *args, **kwargs
    ):
        """
        Dispatches an event from the Gateway.

        ---

        "Dispatching" is when the Gateway sends the client
        information regarding an event non-relevant to
        the connection.

        The `*args` and `**kwargs` signature is for data sent
        in the form of an `_Event`. These are only to be used
        to fill in the actual data of the Gateway event, whereas
        `data` is purely the dataclass.

        ---

        Parameters
        ----------
        _name : `str`
            The name of the event.
        data : `dict`, `Serializable`, `MISSING`
            The supplied payload data from the event.
        """
        logger.debug(f"{_name}: {data if isinstance(data, dict) else kwargs}")

        # TODO: move the underlying dispatch logic to the ._track() method.
        # We probably don't need to segregate the callback designator flow here,
        # and may prove more beneficial if we handle it directly right next to the
        # event table lookup call, to avoid O(n) + 1 time complexity.

        for bot in self._bots:
            if isinstance(data, (dict, MISSING)):
                await bot._trigger(_name.lower(), data)
            elif data is None:
                await bot._trigger(_name.lower(), kwargs)
            else:
                if kwargs.get("id"):
                    kwargs["bot_inst"] = bot.__class__
                await bot._trigger(
                    _name.lower(),
                    structure(kwargs, data),
                )

    async def _identify(self):
        """Sends an identification payload to the Gateway."""
        payload = _GatewayPayload(
            op=_GatewayOpCode.IDENTIFY.value,
            d={
                "token": self.token,
                "intents": self.intents.value,
                "properties": {"os": platform, "browser": "retux", "device": "retux"},
            },
        )
        logger.debug("Sending identification.")
        await self._send(payload)

    async def _resume(self):
        """Sends a resuming payload to the Gateway."""
        payload = _GatewayPayload(
            op=_GatewayOpCode.RESUME,
            d={
                "token": self.token,
                "session_id": self._meta.session_id,
                "seq": self._meta.seq,
            },
        )
        logger.debug("Resuming connection call.")
        await self._send(payload)

    async def _heartbeat(self):
        """Sends a heartbeat payload to the Gateway."""
        payload = _GatewayPayload(op=_GatewayOpCode.HEARTBEAT, d=self._meta.seq)

        await sleep(random())

        while self._heartbeat_ack:
            logger.debug("❤")
            await self._send(payload)
            await sleep(self._meta.heartbeat_interval)

    async def request_guild_members(
        self,
        guild_id: int,
        *,
        query: NotNeeded[str] = MISSING,
        limit: NotNeeded[int] = MISSING,
        presences: NotNeeded[bool] = MISSING,
        user_ids: NotNeeded[int | list[int]] = MISSING,
        nonce: NotNeeded[str] = MISSING,
    ):
        """
        Sends a request for all guild members to the Gateway.

        Parameters
        ----------
        guild_id : `int`
            The ID of the guild to request from.
        query : `str`, optional
            The name of the guild member(s). If you're looking to
            receive all members of a guild, this is left untouched.
        limit : `int`, optional
            How many guild members you wish to return. When `query`
            is specified, only a maximum of `100` are returned.
            This should be left untouched with `query` for all
            members of a guild.
        presences : `bool`, optional
            Whether you only want to receive guild members with
            a presence. The `GUILD_PRESENCES` intent must be
            enabled in order to use.
        user_ids : `int`, `list[int]`, optional
            The IDs of members in the guild to return. This
            may be used in conjunction to `query`, and poses the
            same maximum as `limit` regardless of declaration.
        nonce : `str`, optional
            A nonce used for identification when receiving a
            `Guild Members Chunk` event.
        """
        payload = _GatewayPayload(
            op=_GatewayOpCode.REQUEST_GUILD_MEMBERS,
            d={
                "guild_id": guild_id,
                "query": "" if query is MISSING else query,
                "limit": 0 if limit is MISSING else limit,
            },
        )

        if presences is not MISSING:
            payload.data["presences"] = presences
        if user_ids is not MISSING:
            payload.data["user_ids"] = user_ids
        if nonce is not MISSING:
            payload.data["nonce"] = nonce

        logger.debug("Requesting for guild members.")
        await self._send(payload)

    async def update_voice_state(
        self,
        guild_id: int,
        channel_id: NotNeeded[int] = MISSING,
        self_mute: NotNeeded[bool] = MISSING,
        self_deaf: NotNeeded[bool] = MISSING,
    ):
        """
        Sends a request updating the bots voice state to the Gateway.

        Parameters
        ----------
        guild_id : `int`
            The ID of the guild to request from.
        channel_id : `int`, optional
            The channel ID of the guild to update in.
            If the bot is trying to disconnect, this should
            be left untouched.
        self_mute : `bool`, optional
            Whether the bot is muting itself or not.
            Defaults to `False`.
        self_deaf : `bool`, optional
            Whether the bot is deafening itself or not.
            Defaults to `False`.
        """
        payload = _GatewayPayload(
            op=_GatewayOpCode.VOICE_STATE_UPDATE,
            d={
                "guild_id": guild_id,
                "channel_id": None if channel_id is MISSING else channel_id,
                "self_mute": False if self_mute is MISSING else self_mute,
                "self_deaf": False if self_deaf is MISSING else self_deaf,
            },
        )
        logger.debug("Requesting for a voice state update.")
        await self._send(payload)

    async def update_presence(
        self,
        # TODO: Implement Activity object.
        # activities: list[Activity],
        status: NotNeeded[str] = MISSING,
        afk: NotNeeded[bool] = MISSING,
    ):
        """
        Sends a request updating the bots presence to the Gateway.

        Parameters
        ----------
        status : `str`, optional
            The activity status of the bot while connected
            to Discord.
            e.g. "online", "dnd"
        afk : `bool`, optional
            Whether the bot is AFK or not. This is used in favour of
            allowing `since`, a client-determined variable. You may
            use this instead of writing "idle" to `status`.
        """
        payload = _GatewayPayload(
            op=_GatewayOpCode.PRESENCE_UPDATE,
            d={
                "since": 0,
                # "activities": asdict(activities),
                "status": "online" if status is MISSING else status,
                "afk": False if afk is MISSING and status != "idle" else afk,
            },
        )
        logger.debug("Requesting for a presence update.")
        await self._send(payload)

    @property
    def latency(self) -> float:
        """
        The calculated difference between the last known set
        of acknowledgements for a Gateway event.
        """
        return self._last_ack[1] - self._last_ack[0]
