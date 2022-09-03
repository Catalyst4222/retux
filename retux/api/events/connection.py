from attrs import define

from ...client.resources.guild import UnavailableGuild
from ...client.resources.user import User
from ...client.resources.application import PartialApplication

__all__ = ("Ready", "HeartbeatAck", "Resumed", "Reconnect", "InvalidSession")


@define(kw_only=True)
class Ready:
    """
    Represents when the client has successfully connected.

    ---

    The `READY` event can be the largest and most complex one
    the Gateway will send, as it contains all the state required
    for a client to begin interacting with the rest of the platform.

    ---

    Attributes
    ----------
    v : `int`
        The used version of the Discord API.
    user_settings : `dict`, optional
        The settings of the bot application, if present.
    guilds : `list[UnavailableGuild]`
        The guilds unavailable to the bot.
    geo_ordered_rtc_regions : `list[str]`
        The RTC voice regions accessible to the bot application.
    session_type : `str`
        The type of session that the bot has established with the Gateway.
    session_id : `str`
        The ID of the bot's Gateway connection session, used for reconnection.
    resume_gateway_url : `str`
        The URL of the Gateway upon resuming an existing connection.
    shard : `list[int]`, optional
        The shards of the Gateway connection, if present.
    application : `PartialApplication`
        The application form of the bot. Contains only `id` and `flags`.

    Methods
    -------
    version : `int`
        The used version of the Discord API.
    """

    v: int
    """The used version of the Discord API."""
    user_settings: dict = None
    """The settings of the bot application, if present."""
    user: User
    """The user form of the bot application."""
    guilds: list[UnavailableGuild]
    """The guilds unavailable to the bot."""
    # TODO: Investigate the guild_join_requests field.
    guild_join_requests: list = None
    """
    The pending approval requests for guilds the bot cannot access.

    Some data is conferred here supplied from `guilds`.
    """
    # geo_ordered_rtc_regions: list[str]
    geo_ordered_rtc_regions: list
    """The RTC voice regions accessible to the bot application."""
    session_type: str
    """The type of session that the bot has established with the Gateway."""
    session_id: str
    """The ID of the bot's Gateway connection session, used for reconnection."""
    resume_gateway_url: str
    """The URL of the Gateway upon resuming an existing connection."""
    # TODO: Investigate the relationships field.
    relationships: list = None
    """The relationships associated to the bot application, if present."""
    # TODO: Investigate the private_channels field.
    private_channels: list = None
    """The private channels of the bot application, if present."""
    # TODO: Investigate the presences field.
    presences: list = None
    """The presences of the bot application, if present."""
    # shard: list[int] = None
    shard: list = None
    """The shards of the Gateway connection, if present."""
    application: PartialApplication
    """The application form of the bot. Contains only `id` and `flags`."""

    @property
    def version(self) -> int:
        """The used version of the Discord API."""
        return self.v


@define
class HeartbeatAck:
    """
    Represents when the client's Gateway connection has validated a heartbeat.

    Attributes
    ----------
    latency : `float`
        The latency or difference in milliseconds between heartbeats.
    """

    latency: float
    """The latency or difference in milliseconds between heartbeats."""


@define(kw_only=True)
class Resumed:
    """
    Represents when the client has successfully resumed a connection.

    Attributes
    ----------
    token : `str`
        The token of the bot used.
    session_id : `str`
        The ID of the Gateway connection session.
    seq : `int`
        The last sequence number given for the session.
    """

    token: str
    """The token of the bot used."""
    session_id: str
    """The ID of the Gateway connection session."""
    seq: int
    """The last sequence number given for the session."""


@define()
class Reconnect:
    """
    Represents when the client has been told to reconnect.

    ---

    It should be noted that reconnection is automatically handled for you
    in retux already. This event should never be used outside of logging down
    when reconnections were made. Do not use this event to force a reconnection
    unless you know what you're doing!
    """


@define(repr=False)
class InvalidSession:
    """
    Represents when the client has an invalidated Gateway connection.

    ---

    Invalid sessions are determined by one of three factors:

    - The Gateway could not resume the connection.
    - The client could not identify itself correctly.
    - The Gateway has invalidated the session for you, and requires a new connection.

    ---

    Attributes
    ----------
    _invalid_session : `bool`
        Whether the session can be reconnected to or not.
        This should never need to be called upon directly.
        Please use the representation of the class itself.

        This defaults to `False` and determined on good faith
        of ensuring a stable connection over potential client
        conflict.

    Methods
    -------
    can_reconnect() : `bool`
        Checks the session to see if a reconnection is possible.
    """

    _invalid_session: bool = False
    """
    Whether the session can be reconnected to or not.
    This should never need to be called upon directly.
    Please use the representation of the class itself.

    This defaults to `False` and determined on good faith
    of ensuring a stable connection over potential client
    conflict.
    """

    def __repr__(self) -> bool:
        return self._invalid_session

    def can_reconnect(self) -> bool:
        """
        Checks the session to see if a reconnection is possible.

        Returns
        -------
        `bool`
            Whether the session can be reconnected to or not.
        """
        return self._invalid_session
