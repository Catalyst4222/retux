from .abc import Snowflake

from attrs import define
from enum import IntEnum

__all__ = (
    "StageInstance",
    "StagePrivacyLevel",
)


class StagePrivacyLevel(IntEnum):
    """
    An enumeration representing the privacy levels of a stage in Discord.

    Constants
    ---------
    PUBLIC
        The Stage instance is visible publicly. (deprecated)
    GUILD_ONLY
        The Stage instance is visible to only guild members.
    """

    PUBLIC = 1
    """The stage instance is visible publicly. (deprecated)"""
    GUILD_ONLY = 2
    """The stage instance is visible to only guild members."""


@define(kw_only=True)
class StageInstance:
    """
    A class object representing a stage instance from Discord.

    Attributes
    ----------
    id : `Snowflake`
        The ID of this stage instance.
    guild_id : `Snowflake`
        The guild ID of the associated stage channel.
    channel_id : `Snowflake`
        The ID of the associated stage channel.
    topic : `str`
        The topic of the stage instance (1-120 characters).
    privacy_level : `StagePrivacyLevel`
        The privacy level of the Stage instance.
    discoverable_disabled : `bool`
        Whether or not Stage Discovery is disabled (deprecated).
    guild_scheduled_event_id : `Snowflake`, optional
        The ID of the scheduled event for this Stage instance.
    """

    id: Snowflake
    """The ID of this stage instance."""
    guild_id: Snowflake
    """The guild ID of the associated stage channel."""
    channel_id: Snowflake
    """The ID of the associated stage channel."""
    topic: str
    """The topic of the stage instance (1-120 characters)."""
    privacy_level: StagePrivacyLevel
    """The privacy level of the stage instance."""
    discoverable_disabled: bool = False
    """Whether or not Stage Discovery is disabled (deprecated)."""
    guild_scheduled_event_id: Snowflake
    """The ID of the scheduled event for this stage instance."""


Stage = StageInstance
