from attrs import define

from .abc import Event
from ...client.resources.guild_scheduled_event import GuildScheduledEvent
from ...client.resources.abc import Timestamp
from ...client.resources.channel import Channel, ThreadChannel
from ...client.resources.guild import Guild, Member
from ...client.resources.stage_instance import StageInstance


@define(kw_only=True, repr=False)
class GuildCreate(Guild, Event):
    """
    Represents a `GUILD_CREATE` Gateway event from Discord.

    Attributes
    ----------
    joined_at : `Timestamp`
        The time the bot joined the guild.
    large : `bool`
        Whether the guild is large or not.
    unavailable : `bool`
        Whether the guild is unavailable or not.
        Defaults to `False`.
    member_count : `int`
        The total amount of members in the guild.
    members : `list[Member]`
        The members of the guild.
    channels : `list[Channel]`
        The channels of the guild.
    threads : `list[ThreadChannel]`
        The thread channels of the guild.
    stage_instances : `list[StageInstance]`
        The stage instances of the guild.
    guild_scheduled_events : `list[GuildScheduledEvent]`
        The scheduled events of the guild.
    """

    joined_at: Timestamp
    """The time the bot joined the guild."""
    large: bool
    """Whether the guild is large or not."""
    unavailable: bool = False
    """Whether the guild is unavailable or not. Defaults to `False`."""
    member_count: int
    """The total amount of members in the guild."""
    # TODO: Implement PartialVoiceState object.
    # voice_states: list[PartialVoiceState]
    # """The voice states of members in the guild."""
    members: list[Member]
    """The members of the guild."""
    channels: list[Channel]
    """The channels of the guild."""
    threads: list[ThreadChannel]
    """The thread channels of the guild."""
    # TODO: Implement PartialPresenceUpdate object.
    # presences: list[PartialPresenceUpdate]
    # """The presences of members in the guild."""
    stage_instances: list[StageInstance]
    """The stage instances of the guild."""
    guild_scheduled_events: list[GuildScheduledEvent]
    """The scheduled events of the guild."""
