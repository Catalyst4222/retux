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
)


class _EventTable:
    """
    Stores events from the Gateway for potential use dispatching.
    """

    guild: dict[str, object] = {
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
    }

    @classmethod
    def lookup(cls, name: str):
        if cls.guild.get(name):
            return cls.guild[name]
        if name == "TYPING_START":
            return TypingStart
