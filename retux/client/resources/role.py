from attrs import define

from .misc import Object

__all__ = (
    "Role",
    "RoleTags",
)


@define(kw_only=True)
class RoleTags:
    """
    Represents the tags of a role from Discord.

    Attributes
    ----------
    bot_id : `int`, optional
        The ID of the bot this role belongs to.
    integration_id : `int`, optional
        The ID of the integration this role belongs to.
    premium_subscriber : `bool`
        Whether this is the guild's premium subscriber role.
    """

    bot_id: int | None = None
    """The id of the bot this role belongs to."""
    integration_id: int | None = None
    """The id of the integration this role belongs to."""
    premium_subscriber: bool = False
    """Whether this is the guild's premium subscriber role."""


@define(kw_only=True)
class Role(Object):
    """
    Represents a role from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the role.
    name : `str`
        The name of the role.
    color : `int`
        The integer representation of hexadecimal color code of the role.
    hoist : `bool`
        If this role is pinned in the user listing.
    icon : `str`, optional
        The hash of the roles icon, if present.
    unicode_emoji : `str`, optional
        The emoji unicode of the role, if present.
    position : `int`
        The position of the role.
    permissions : `str`
        The role's permission bit set.
    managed : `bool`
        Whether this role is managed by an integration.
    tags : `RoleTags`, optional
        The tags this role has, if present.
    """

    id: int
    """The ID of the role."""
    name: str
    """The name of the role."""
    color: int
    """The integer representation of hexadecimal color code of the role."""
    hoist: bool
    """If this role is pinned in the user listing."""
    icon: str = None
    """The role icon hash, if present."""
    unicode_emoji: str = None
    """The emoji unicode of the role, if present."""
    position: int
    """The position of the role."""
    permissions: str
    """The role's permission bit set."""
    managed: bool
    """Whether this role is managed by an integration."""
    mentionable: bool
    """Whether this role is mentionable."""
    tags: RoleTags = None
    """The tags this role has, if present."""
