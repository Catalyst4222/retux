from attrs import define

from ...client.resources.channel import Channel, ThreadChannel
from ...client.resources.emoji import Emoji
from ...client.resources.guild import Guild, Member, UnavailableGuild
from ...client.resources.guild_scheduled_event import GuildScheduledEvent
from ...client.resources.misc import CDNEndpoint, Image, Timestamp
from ...client.resources.role import Role
from ...client.resources.stage_instance import StageInstance
from ...client.resources.sticker import Sticker
from ...client.resources.user import User


@define(kw_only=True)
class GuildCreate(Guild):
    """
    Represents a `GUILD_CREATE` Gateway event from Discord.

    Attributes
    ----------
    joined_at : `Timestamp`
        The time the bot joined the guild.
    large : `bool`
        Whether the guild is large or not.
    unavailable : `bool`
        Whether the guild is unavailable or not.
        Defaults to `False`.
    member_count : `int`
        The total amount of members in the guild.
    members : `list[Member]`
        The members of the guild.
    channels : `list[Channel]`
        The channels of the guild.
    threads : `list[ThreadChannel]`
        The thread channels of the guild.
    stage_instances : `list[StageInstance]`
        The stage instances of the guild.
    guild_scheduled_events : `list[GuildScheduledEvent]`
        The scheduled events of the guild.
    """

    joined_at: Timestamp
    """The time the bot joined the guild."""
    large: bool
    """Whether the guild is large or not."""
    unavailable: bool = False
    """Whether the guild is unavailable or not. Defaults to `False`."""
    member_count: int
    """The total amount of members in the guild."""
    # # TODO: Implement PartialVoiceState object.
    # # voice_states: list[PartialVoiceState]
    # # """The voice states of members in the guild."""
    members: list[Member]
    """The members of the guild."""
    channels: list[Channel]
    """The channels of the guild."""
    threads: list[ThreadChannel]
    """The thread channels of the guild."""
    # TODO: Implement PartialPresenceUpdate object.
    # presences: list[PartialPresenceUpdate]
    # """The presences of members in the guild."""
    stage_instances: list[StageInstance]
    """The stage instances of the guild."""
    guild_scheduled_events: list[GuildScheduledEvent]
    """The scheduled events of the guild."""


class GuildUpdate(Guild):
    """Represents a `GUILD_UPDATE` Gateway event from Discord."""


class GuildDelete(UnavailableGuild):
    """
    Represents a `GUILD_DELETE` Gateway event from Discord.

    ---

    If `unavailable` is set to `False`, this represents the bot
    being removed from the guild.
    """


@define(kw_only=True)
class GuildBanAdd:
    """
    Represents a `GUILD_BAN_ADD` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where the ban occurred.
    user : `User`
        The user who was banned from the guild.
    """

    guild_id: int
    """The ID of the guild where the ban occurred."""
    user: User
    """The user who was banned from the guild."""


@define(kw_only=True)
class GuildBanRemove:
    """
    Represents a `GUILD_BAN_REMOVE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where the unban occurred.
    user : `User`
        The user who was unbanned from the guild.
    """

    guild_id: int
    """The ID of the guild where the unban occurred."""
    user: User
    """The user who was unbanned from the guild."""


@define(kw_only=True)
class GuildEmojisUpdate:
    """
    Represents a `GUILD_EMOJIS_UPDATE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where emojis were updated.
    emojis : `list[Emoji]`
        The emojis updated in the guild.
    """

    guild_id: int
    """The ID of the guild where emojis were updated."""
    emojis: list[Emoji]
    """The emojis updated in the guild."""


@define(kw_only=True)
class GuildStickersUpdate:
    """
    Represents a `GUILD_STICKERS_UPDATE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where stickers were updated.
    stickers : `list[Sticker]`
        The stickers updated in the guild.
    """

    guild_id: int
    """The ID of the guild where emojis were updated."""
    stickers: list[Sticker]
    """The stickers updated in the guild."""


@define(kw_only=True)
class GuildIntegrationsUpdate:
    """
    Represents a `GUILD_INTEGRATIONS_UPDATE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where integrations were updated.
    """

    guild_id: int
    """The ID of the guild where integrations were updated."""


@define(kw_only=True)
class GuildMemberAdd(Member):
    """
    Represents a `GUILD_MEMBER_ADD` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where a user was added.
    """

    guild_id: int
    """The ID of the guild where a user was added."""


@define(kw_only=True)
class GuildMemberRemove:
    """
    Represents a `GUILD_MEMBER_REMOVE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where the user was removed.
    user : `User`
        The user who was removed from the guild.
    """

    guild_id: int
    """The ID of the guild where the user was removed."""
    user: User
    """The user who was removed from the guild."""


@define(kw_only=True)
class GuildMemberUpdate:
    """
    Represents a `GUILD_MEMBER_UPDATE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where the user was removed.
    roles : `list[int]`
        The roles belonging to the guild member.
    user : `User`
        The user who was removed from the guild.
    nick : `str`, optional
        The nickname of the guild member, if present.
    avatar : `Image`, optional
        The avatar of the guild member, if present.
    joined_at : `Timestamp`
        The time at which the user joined the guild.
    premium_since : `Timestamp`, optional
        The time at which the member boosted the guild,
        if present.
    deaf : `bool`
        Whether the guild member is globally deafened or not.
        Defaults to `False`.
    mute : `bool`
        Whether the guild member is globally muted or not.
        Defaults to `False`.
    pending : `bool`
        Whether the user is still gated by Membership Screening
        or not. Defaults to `False`.
    communication_disabled_until : `Timestamp`, optional
        The time remaining before the member is no longer
        timed out, if present.
    """

    guild_id: int
    """The ID of the guild where the user was removed."""
    roles: list[int]
    """The roles belonging to the guild member."""
    user: User
    """The user who was removed from the guild."""
    nick: str = None
    """The nickname of the guild member, if present."""
    avatar: str | Image = None
    """The avatar of the guild member, if present."""
    joined_at: Timestamp = None
    """The time at which the user joined the guild."""
    premium_since: Timestamp = None
    """
    The time at which the member boosted the guild,
    if present.
    """
    deaf: bool = False
    """
    Whether the guild member is globally deafened or not.
    Defaults to `False`.
    """
    mute: bool = False
    """
    Whether the guild member is globally muted or not.
    Defaults to `False`.
    """
    pending: bool = False
    """
    Whether the user is still gated by Membership Screening or not.
    Defaults to `False`.
    """
    communication_disabled_until: Timestamp = None
    """
    The time remaining before the member is no longer timed out,
    if present.
    """

    def __attrs_post_init__(self):
        # FIXME: This needs a more proper method of being built. Some design limitations
        # are easy to see when put into practice.
        if self.avatar is not None:
            hash = self.avatar
            self.avatar = Image._c(CDNEndpoint.GUILD_MEMBER_AVATAR)
            self.avatar._vars = [self.guild_id, self.user.id, hash]


@define(kw_only=True)
class GuildMembersChunk:
    """
    Represents a `GUILD_MEMBERS_CHUNK` Gateway event from Discord.

    ---

    This dataclass is sent in response to a `Request Guild Members`
    Gateway command.

    ---

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where the request was performed.
    members : `list[Member]`
        The returned members of the guild.
    chunk_index : `int`
        The current chunk index of the guild.
    chunk_count : `int`
        The amount of chunks sent to the guild.
    not_found : `list`, optional
        IDs that were not found in the request, if present.
    nonce : `str`, optional
        The nonce of the requested guild.
    """

    guild_id: int
    """The ID of the guild where the request was performed."""
    members: list[Member]
    """The returned members of the guild."""
    chunk_index: int
    """The current chunk index of the guild."""
    chunk_count: int
    """The amount of chunks sent to the guild."""
    not_found: list = None
    """IDs that were not found in the request, if present."""
    # TODO: Implement Presence object.
    # presences: list[Presence] = None
    nonce: str = None
    """The nonce of the requested guild."""


@define(kw_only=True)
class GuildRoleCreate:
    """
    Represents a `GUILD_ROLE_CREATE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where the role was created.
    role : `Role`
        The role that was added to the guild.
    """

    guild_id: int
    """The ID of the guild where the role was added."""
    role: Role
    """The role that was added to the guild."""


@define(kw_only=True)
class GuildRoleUpdate:
    """
    Represents a `GUILD_ROLE_UPDATE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where the role was updated.
    role : `Role`
        The role that was updated in the guild.
    """

    guild_id: int
    """The ID of the guild where the role was added."""
    role: Role
    """The role that was added to the guild."""


@define(kw_only=True)
class GuildRoleDelete:
    """
    Represents a `GUILD_ROLE_DELETE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `int`
        The ID of the guild where the role was deleted.
    role_id : `int`
        The ID of the role that was deleted from the guild.
    """

    guild_id: int
    """The ID of the guild where the role was deleted."""
    role_id: int
    """The ID of the role that was deleted from the guild."""


class GuildScheduledEventCreate(GuildScheduledEvent):
    """Represents a `GUILD_SCHEDULED_EVENT_CREATE` Gateway event from Discord."""


class GuildScheduledEventUpdate(GuildScheduledEvent):
    """Represents a `GUILD_SCHEDULED_EVENT_UPDATE` Gateway event from Discord."""


class GuildScheduledEventDelete(GuildScheduledEvent):
    """Represents a `GUILD_SCHEDULED_EVENT_DELETE` Gateway event from Discord."""


@define(kw_only=True)
class GuildScheduledEventUserAdd:
    """
    Represents a `GUILD_SCHEDULED_EVENT_USER_ADD` Gateway event from Discord.

    Attributes
    ----------
    guild_scheduled_event_id : `int`
        The ID of the guild's scheduled event.
    user_id : `int`
        The ID of the user in the guild scheduled event.
    guild_id : `int`
        The ID of the guild associated to the scheduled event.
    """

    guild_scheduled_event_id: int
    """The ID of the guild's scheduled event."""
    user_id: int
    """The ID of the user in the guild scheduled event."""
    guild_id: int
    """The ID of the guild associated to the scheduled event."""


@define(kw_only=True)
class GuildScheduledEventUserRemove:
    """
    Represents a `GUILD_SCHEDULED_EVENT_USER_REMOVE` Gateway event from Discord.

    Attributes
    ----------
    guild_scheduled_event_id : `int`
        The ID of the guild's scheduled event.
    user_id : `int`
        The ID of the user in the guild scheduled event.
    guild_id : `int`
        The ID of the guild associated to the scheduled event.
    """

    guild_scheduled_event_id: int
    """The ID of the guild's scheduled event."""
    user_id: int
    """The ID of the user in the guild scheduled event."""
    guild_id: int
    """The ID of the guild associated to the scheduled event."""
