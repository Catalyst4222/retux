from .abc import Snowflake, Timestamp
from .user import User
from .guild import Guild

from attrs import define

__all__ = ("GuildTemplate",)


@define(kw_only=True)
class GuildTemplate:
    """
    Represents the template of a guild from Discord.

    Attributes
    ----------
    code : `str`
        The template code as unique ID.
    name : `str`
        The name of the template.
    description : `str`, optional
        The description of the template, if any.
    usage_count : `int`
        The amount of times this template has been used.
    creator_id : `Snowflake`
        The ID of the user who created the template.
    creator : `User`
        The user who created the template.
    created_at : `datetime`
        When this template was created.
    updated_at : `datetime`
        When this template was last synced to the source guild.
    source_guild_id : `Snowflake`
        The ID of the guild this template is based on.
    serialized_source_guild : `Guild`
        The guild snapshot this template contains.
    is_dirty : `bool`
        Whether the template has unsynced changes or not.
    """

    code: str
    """The template code as unique ID."""
    name: str
    """The name of the template."""
    description: str = None
    """The description of the template, if any."""
    usage_count: int
    """The amount of times this template has been used."""
    creator_id: Snowflake
    """The ID of the user who created the template."""
    creator: User
    """The user who created the template."""
    created_at: Timestamp
    """When this template was created."""
    updated_at: Timestamp
    """When this template was last synced to the source guild."""
    source_guild_id: Snowflake
    """The ID of the guild this template is based on."""
    serialized_source_guild: Guild
    """The guild snapshot this template contains."""
    is_dirty: bool = False
    """Whether the template has unsynced changes or not."""
