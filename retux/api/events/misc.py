from datetime import datetime
from attrs import define, field

from ...client.resources.abc import Snowflake
from ...client.resources.guild import Member


@define(kw_only=True)
class TypingStart:
    """
    Represents a `TYPING_START` Gateway event from Discord.

    Attributes
    ----------
    channel_id : `Snowflake`
        The ID of the channel when typing occured.
    user_id : `Snowflake`
        The ID of the user who started typing.
    timestamp : `datetime.datetime`
        The timestamp of when the typing occured.
    guild_id : `Snowflake`, optional
        The ID of the guild when typing occured.

        This will only appear when a user is typing
        outside of a DM.
    member : `Member`, optional
        The member who started typing.

        This will only appear when a user is typing
        outside of a DM.
    """

    channel_id: Snowflake
    """The ID of the channel when typing occured."""
    user_id: Snowflake
    """The ID of the user who started typing."""
    timestamp: datetime = field(converter=datetime.fromtimestamp)
    """The timestamp of when the typing occured."""
    guild_id: Snowflake = None
    """
    The ID of the guild when typing occured.

    This will only appear when a user is typing
    outside of a DM.
    """
    member: Member = None
    """
    The member who started typing.

    This will only appear when a user is typing
    outside of a DM.
    """
