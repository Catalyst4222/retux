from .abc import Snowflake, Object, Timestamp
from .user import User
from .guild import Member

from attrs import define
from enum import IntEnum

__all__ = (
    "GuildScheduledEvent",
    "GuildScheduledEventEntityType",
    "GuildScheduledEventStatus",
    "GuildScheduledEventEntityMetadata",
    "GuildScheduledEventPrivacyLevel",
    "GuildScheduledEventUser",
)


class GuildScheduledEventPrivacyLevel(IntEnum):
    """
    Represents the privacy levels of a guild scheduled event from Discord.

    Constants
    ---------
    GUILD_ONLY
        The scheduled event is only accessible to guild members.
    """

    GUILD_ONLY = 2
    """The scheduled event is only accessible to guild members."""


class GuildScheduledEventEntityType(IntEnum):
    """
    Represents the different types of guild scheduled events from Discord.

    Constants
    ---------
    STAGE_INSTANCE
        The event will happen in a stage instance.
    VOICE
        The event will happen in a voice channel.
    EXTERNAL
        The event will happen in an external location.

        This requires `GuildScheduledEventEntityMetadata`.
    """

    STAGE_INSTANCE = 1
    """The event will happen in a stage instance."""
    VOICE = 2
    """The event will happen in a voice channel."""
    EXTERNAL = 3
    """The event will happen in an external location."""


class GuildScheduledEventStatus(IntEnum):
    """
    Represents the different status a guild scheduled event can have.

    Once the status is set to `Completed` or `Canceled`, it can't be updated again.

    Constants
    ----------
    SCHEDULED
        The event is currently scheduled and not active.
    ACTIVE
        The event is happening right now.
    COMPLETED
        The event was completed successfully.
    CANCELED
        The event was canceled before it could begin.
    """

    SCHEDULED = 1
    """The event is currently scheduled and not active."""
    ACTIVE = 2
    """The event is happening right now."""
    COMPLETED = 3
    """The event was completed successfully."""
    CANCELED = 4
    """The event was canceled before it could begin."""


@define(kw_only=True)
class GuildScheduledEventEntityMetadata:
    """
    Represents the additional metadata of guild scheduled events from Discord.

    Attributes
    ----------
    location : `str`, optional
        The location of the event in-between 1-100 characters.

        This is required for events with the `EXTERNAL` entity type.
    """

    location: str = None
    """The location of the event in-between 1-100 characters."""


@define(kw_only=True)
class GuildScheduledEvent(Object):
    """
    Represents a scheduled event of a guild from Discord.

    Attributes
    ----------
    id : `Snowflake`
        The ID belonging to the scheduled event.
    guild_id : `Snowflake`
        The ID of the guild the event belongs to.
    channel_id : `Snowflake`, optional
        The ID of the channel the event will be hosted in, if any.

        This is not available for Events with the `entity_type` `EXTERNAL`.
    creator_id : `Snowflake`, optional
        The ID of the user who created the event, if any.

        This is only available for events created after October 25th, 2021.
    namer : `str`
        The name of the scheduled event (1-100 characters).
    description : `str`, optional
        The description of the scheduled event, if any (1-1000 characters).
    scheduled_start_time : `datetime`
        The time the scheduled event will start.
    scheduled_end_time : `datetime`, optional
        The time the scheduled event will end, if any.

        This is only required if the `entity_type` is `EXTERNAL`
    privacy_level : `GuildScheduledEventPrivacyLevel`
        The privacy level of the scheduled event.
    status : `GuildScheduledEventStatus`
        The status of the scheduled event.
    entity_type : `GuildScheduledEventEntityType`
        The type of the scheduled event.
    entity_id : `Snowflake`, optional
        The ID of an entity associated with a guild scheduled event, if any.
    entity_metadata : `GuildScheduledEventEntityMetadata`, optional
        Additional metadata for the guild scheduled event, if any.

        This must not present for scheduled events with the type `VOICE` or `STAGE_INSTANCE` but must be set for
        scheduled events with the type `EXTERNAL`.
    creator : `User`, optional
        The user that created the scheduled event.
    user_count : `int`, optional
        The number of users subscribed to the scheduled event.
    image : `str`, optional
        The cover image hash of the scheduled event.
    """

    id: Snowflake
    """The ID belonging to the scheduled event."""
    guild_id: Snowflake
    """The ID of the guild the event belongs to."""
    channel_id: Snowflake
    """The ID of the channel the event will be hosted in."""
    creator_id: Snowflake = None
    """The ID of the user who created the event."""
    name: str
    """The name of the scheduled event (1-100 characters)."""
    description: str = None
    """The description of the scheduled event (1-1000 characters)."""
    scheduled_start_time: Timestamp
    """The time the scheduled event will start."""
    scheduled_end_time: Timestamp = None
    """The time the scheduled event will end."""
    privacy_level: GuildScheduledEventPrivacyLevel
    """The privacy level of the scheduled event."""
    status: GuildScheduledEventStatus
    """The status of the scheduled event."""
    entity_type: GuildScheduledEventEntityType
    """The type of the scheduled event."""
    entity_id: Snowflake = None
    """The ID of an entity associated with a guild scheduled event."""
    entity_metadata: GuildScheduledEventEntityMetadata = None
    """Additional metadata for the guild scheduled event."""
    creator: User = None
    """The user that created the scheduled event."""
    user_count: int = None
    """The number of users subscribed to the scheduled event."""
    image: str = None
    """The cover image hash of the scheduled event."""


class GuildScheduledEventUser:
    """
    Represents a user in a guild scheduled event from Discord.

    Attributes
    ----------
    guild_scheduled_event_id : `Snowflake`
        The scheduled event ID which the user subscribed to.
    user : `User`
        The user which subscribed to an event.
    member : `Member`, optional
        Guild member data for this user for the guild which this event belongs to, if any.
    """

    guild_scheduled_event_id: Snowflake
    """The scheduled event id which the user subscribed to."""
    user: User = None
    """The user which subscribed to an event."""
    member: Member = None
    """Guild member data for this user for the guild which this event belongs to, if any."""
