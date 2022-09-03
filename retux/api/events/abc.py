from .channel import (
    ChannelCreate,
    ChannelUpdate,
    ChannelDelete,
    ChannelPinsUpdate,
    ThreadListSync,
    ThreadDelete,
    ThreadUpdate,
    ThreadCreate,
)
from .connection import HeartbeatAck, Ready, InvalidSession, Reconnect, Resumed
from .misc import TypingStart
from .guild import (
    GuildCreate,
    GuildDelete,
    GuildUpdate,
    GuildStickersUpdate,
    GuildEmojisUpdate,
    GuildBanRemove,
    GuildBanAdd,
    GuildMembersChunk,
    GuildMemberUpdate,
    GuildMemberRemove,
    GuildMemberAdd,
    GuildIntegrationsUpdate,
    GuildRoleAdd,
    GuildRoleDelete,
    GuildRoleUpdate,
    GuildScheduledEventCreate,
    GuildScheduledEventUpdate,
    GuildScheduledEventDelete,
    GuildScheduledEventUserAdd,
    GuildScheduledEventUserRemove,
)


class _EventTable:
    """
    Stores events from the Gateway for potential use dispatching.
    """

    connection: dict[str, type] = {
        "READY": Ready,
        "HEARTBEAT_ACK": HeartbeatAck,
        "INVALID_SESSION": InvalidSession,
        "RECONNECT": Reconnect,
        "RESUMED": Resumed,
    }

    guild: dict[str, type] = {
        "GUILD_CREATE": GuildCreate,
        "GUILD_UPDATE": GuildUpdate,
        "GUILD_DELETE": GuildDelete,
        "GUILD_BAN_ADD": GuildBanAdd,
        "GUILD_BAN_REMOVE": GuildBanRemove,
        "GUILD_EMOJIS_UPDATE": GuildEmojisUpdate,
        "GUILD_STICKERS_UPDATE": GuildStickersUpdate,
        "GUILD_INTEGRATIONS_UPDATE": GuildIntegrationsUpdate,
        "GUILD_MEMBER_ADD": GuildMemberAdd,
        "GUILD_MEMBER_REMOVE": GuildMemberRemove,
        "GUILD_MEMBER_UPDATE": GuildMemberUpdate,
        "GUILD_MEMBERS_CHUNK": GuildMembersChunk,
        "GUILD_ROLE_CREATE": GuildRoleAdd,
        "GUILD_ROLE_UPDATE": GuildRoleUpdate,
        "GUILD_ROLE_DELETE": GuildRoleDelete,
        "GUILD_SCHEDULED_EVENT_CREATE": GuildScheduledEventCreate,
        "GUILD_SCHEDULED_EVENT_UPDATE": GuildScheduledEventUpdate,
        "GUILD_SCHEDULED_EVENT_DELETE": GuildScheduledEventDelete,
        "GUILD_SCHEDULED_EVENT_USER_ADD": GuildScheduledEventUserAdd,
        "GUILD_SCHEDULED_EVENT_USER_REMOVE": GuildScheduledEventUserRemove,
    }
    channel: dict[str, type] = {
        "CHANNEL_CREATE": ChannelCreate,
        "CHANNEL_UPDATE": ChannelUpdate,
        "CHANNEL_DELETE": ChannelDelete,
        "CHANNEL_PINS_UPDATE": ChannelPinsUpdate,
        "THREAD_CREATE": ThreadCreate,
        "THREAD_UPDATE": ThreadUpdate,
        "THREAD_DELETE": ThreadDelete,
        "THREAD_LIST_SYNC": ThreadListSync,
    }

    @classmethod
    def lookup(cls, name: str) -> type:
        if cls.guild.get(name):
            return cls.guild[name]
        if cls.channel.get(name):
            return cls.channel[name]
        if name == "TYPING_START":
            return TypingStart
