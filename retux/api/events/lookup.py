from enum import Enum

from .channel import (
    ChannelCreate,
    ChannelDelete,
    ChannelPinsUpdate,
    ChannelUpdate,
    ThreadCreate,
    ThreadDelete,
    ThreadListSync,
    ThreadUpdate,
)
from .connection import HeartbeatAck, InvalidSession, Ready, Reconnect, Resumed
from .guild import (
    GuildBanAdd,
    GuildBanRemove,
    GuildCreate,
    GuildDelete,
    GuildEmojisUpdate,
    GuildIntegrationsUpdate,
    GuildMemberAdd,
    GuildMemberRemove,
    GuildMembersChunk,
    GuildMemberUpdate,
    GuildRoleCreate,
    GuildRoleDelete,
    GuildRoleUpdate,
    GuildScheduledEventCreate,
    GuildScheduledEventDelete,
    GuildScheduledEventUpdate,
    GuildScheduledEventUserAdd,
    GuildScheduledEventUserRemove,
    GuildStickersUpdate,
    GuildUpdate,
)
from .misc import TypingStart


class EventType(Enum):
    """
    Represents the type of Gateway events from Discord.

    ---

    This class works similar to a lookup table, where the value
    is the event dataclass' type, and the "constant" is
    the attribute equivalent.
    """

    READY = Ready
    HEARTBEAT_ACK = HeartbeatAck
    INVALID_SESSION = InvalidSession
    RECONNECT = Reconnect
    RESUMED = Resumed

    TYPING_START = TypingStart

    GUILD_CREATE = GuildCreate
    GUILD_UPDATE = GuildUpdate
    GUILD_DELETE = GuildDelete
    GUILD_BAN_ADD = GuildBanAdd
    GUILD_BAN_REMOVE = GuildBanRemove
    GUILD_EMOJIS_UPDATE = GuildEmojisUpdate
    GUILD_STICKERS_UPDATE = GuildStickersUpdate
    GUILD_INTEGRATIONS_UPDATE = GuildIntegrationsUpdate
    GUILD_MEMBER_ADD = GuildMemberAdd
    GUILD_MEMBER_UPDATE = GuildMemberUpdate
    GUILD_MEMBER_REMOVE = GuildMemberRemove
    GUILD_MEMBERS_CHUNK = GuildMembersChunk
    GUILD_ROLE_CREATE = GuildRoleCreate
    GUILD_ROLE_UPDATE = GuildRoleUpdate
    GUILD_ROLE_DELETE = GuildRoleDelete
    GUILD_SCHEDULED_EVENT_CREATE = GuildScheduledEventCreate
    GUILD_SCHEDULED_EVENT_UPDATE = GuildScheduledEventUpdate
    GUILD_SCHEDULED_EVENT_DELETE = GuildScheduledEventDelete
    GUILD_SCHEDULED_EVENT_USER_ADD = GuildScheduledEventUserAdd
    GUILD_SCHEDULED_EVENT_USER_REMOVE = GuildScheduledEventUserRemove

    CHANNEL_CREATE = ChannelCreate
    CHANNEL_UPDATE = ChannelUpdate
    CHANNEL_DELETE = ChannelDelete
    CHANNEL_PINS_UPDATE = ChannelPinsUpdate
    THREAD_CREATE = ThreadCreate
    THREAD_UPDATE = ThreadUpdate
    THREAD_DELETE = ThreadDelete
    THREAD_LIST_SYNC = ThreadListSync
