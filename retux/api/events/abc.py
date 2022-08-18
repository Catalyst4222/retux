from .misc import TypingStart
from .guild import GuildCreate


class _EventTable:
    """
    Stores events from the Gateway for potential use dispatching.
    """

    guild: dict[str, object] = {
        "GUILD_CREATE": GuildCreate,
    }

    @classmethod
    def lookup(cls, name: str):
        if cls.guild.get(name):
            return cls.guild[name]
        if name == "TYPING_START":
            return TypingStart
