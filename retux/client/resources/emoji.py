from attrs import define

from .abc import Object, Snowflake
from .user import User
from .role import Role


@define()
class Emoji(Object):
    """
    Represents an Emoji from Discord.

    Attributes
    ----------
    id : `Snowflake`, optional
        The ID of the Emoji.

        Only available on guild created emojis.
    name : `str`, optional
        The name of the emoji.

        This is a unicode emoji if the emoji
        is standard, otherwise it is the name
        of the emoji.
    user : `User`, optional
        The user that created the emoji.
    require_colons : `bool`, optional
        Whether or not the emoji needs to be wrapped in colons.
    managed : `bool`, optional
        Whether or not the emoji is managed.
    animated : `bool`, optional
        Whether or not the emoji is animated.
    available : `bool`
        Whether or not the emoji is available.

        Defaults to `False` if the server that owns
        the emoji lost a level of boosting.
    """

    id: Snowflake = None
    """
    The ID of the Emoji.

    Only available on guild created emojis.
    """
    name: str = None
    """
    The name of the emoji.

    This is a unicode emoji if the emoji
    is standard, otherwise it is the name
    of the emoji.
    """
    roles: list[Role] = None
    """A list of roles allowed to use this emoji."""
    user: User = None
    """The user that created the emoji."""
    require_colons: bool = None
    """Whether or not the emoji needs to be wrapped in colons."""
    managed: bool = None
    """Whether or not the emoji is managed."""
    animated: bool = None
    """Whether or not the emoji is animated."""
    available: bool = None
    """
    Whether or not the emoji is available.

    Defaults to `False` if the server that owns
    the emoji lost a level of boosting.
    """
