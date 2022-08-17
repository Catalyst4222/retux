from attrs import define

from .misc import TypingStart
from .guild import GuildCreate


@define(repr=False)
class Event:
    """
    Represents the base object form of a Gateway event from Discord.

    ---

    A Gateway event will contain information relevant to the resource
    in particular. Dataclasses that use the Event object will contain
    its fields, including a direct representation of the resource
    dataclass.

    In order to access the abstracted state, please use the representation
    of the class itself.
    """

    _name: str
    """The name of the Gateway event, used for pattern checking during client dispatch."""


class _EventTable:
    """
    Stores events from the Gateway for potential use dispatching.
    """

    guild: dict[str, Event] = {
        "GUILD_CREATE": GuildCreate,
    }

    @classmethod
    def lookup(cls, name: str, data: dict):
        if cls.guild.get(name):
            return cls.guild[name]
        if name == "TYPING_START":
            return TypingStart
