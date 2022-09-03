from attrs import define

from ...client.resources.abc import Snowflake, Timestamp
from ...client.resources.channel import Channel, ThreadChannel, ThreadMember


class ChannelCreate(Channel):
    """Represents a `CHANNEL_CREATE` Gateway event from Discord."""


class ChannelUpdate(Channel):
    """Represents a `CHANNEL_UPDATE` Gateway event from Discord."""


class ChannelDelete(Channel):
    """Represents a `CHANNEL_DELETE` Gateway event from Discord."""


class ThreadCreate(ThreadChannel):
    """Represents a `THREAD_CREATE` Gateway event from Discord."""


class ThreadUpdate(ThreadChannel):
    """Represents a `THREAD_UPDATE` Gateway event from Discord."""


class ThreadDelete(ThreadChannel):
    """Represents a `THREAD_DELETE` Gateway event from Discord."""


@define(kw_only=True)
class ThreadListSync:
    """
    Represents a `THREAD_LIST_SYNC` Gateway event from Discord.

    ---

    This should not be confused with `THREAD_CREATE`, for when a thread
    is created. This event in particular is sent when access is *gained*
    to the thread.

    ---

    Attributes
    ----------
    guild_id : `Snowflake`
        The members inside of the threads given.
    channel_ids : `list[Snowflake]`, optional
        The members inside of the threads given.
    threads : `list[ThreadChannel]`
        The members inside of the threads given.
    members : `list[ThreadMember]`
        The members inside of the threads given.
    """

    guild_id: Snowflake
    """the id of the guild a thread was gained access to."""
    channel_ids: list[Snowflake] = None
    """the thread channel ids associated to the syncing call."""
    threads: list[ThreadChannel]
    """the thread channels associated to the syncing call."""
    members: list[ThreadMember]
    """The members inside of the threads given."""


@define(kw_only=True)
class ChannelPinsUpdate:
    """
    Represents a `CHANNEL_PINS_UPDATE` Gateway event from Discord.

    Attributes
    ----------
    guild_id : `Snowflake`
        The ID of the guild associated to a channel's pins update.
    channel_id : `Snowflake`
        The ID of the channel where pins were updated.
    last_pin_timestamp : `Timestamp`
        The timestamp of the last known pinned message in the channel.
    """

    guild_id: Snowflake
    """The ID of the guild associated to a channel's pins update."""
    channel_id: Snowflake
    """The ID of the channel where pins were updated."""
    last_pin_timestamp: Timestamp
    """The timestamp of the last known pinned message in the channel."""
