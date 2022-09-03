from .abc import Snowflake, Timestamp
from .guild import Member

from attrs import define

__all__ = ("Voice", "VoiceState")


@define(kw_only=True)
class VoiceState:
    """
    Represents the state of a user's VOIP from Discord.

    Attributes
    ----------
    guild_id : `Snowflake`, optional
        The guild ID this voice state is for.
    channel_id : `Snowflake`, optional
        The channel ID this user is connected to.
    user_id : `Snowflake`
        The user ID this voice state is for.
    member : `Member`, optional
        The guild member this voice state is for.
    session_id : `str`
        The session ID for this voice state.
    deaf : `bool`
        Whether this user is deafened by the server or not.
    mute : `bool`
        Whether this user is muted by the server or not.
    self_deaf : `bool`
        Whether this user is locally deafened or not.
    self_mute : `bool`
        Whether this user is muted by the server or not.
    self_stream : `bool`
        Whether this user is streaming using 'Go Live' or not.
    self_video : `bool`
        Whether this user's camera is enabled or not.
    suppress : `bool`
        Whether this user is muted by the current user or not.
    request_to_speak_timestamp : `datetime`, optional
        The time at which the user requested to speak, if present.
    """

    guild_id: Snowflake = None
    """The guild ID this voice state is for."""
    channel_id: Snowflake = None
    """The channel ID this user is connected to."""
    user_id: Snowflake
    """The user ID this voice state is for."""
    member: Member = None
    """The guild member this voice state is for."""
    session_id: str
    """The session ID for this voice state."""
    deaf: bool
    """Whether this user is deafened by the server."""
    mute: bool
    """Whether this user is muted by the server."""
    self_deaf: bool
    """Whether this user is locally deafened."""
    self_mute: bool
    """Whether this user is locally muted."""
    self_stream: bool = False
    """Whether this user is streaming using 'Go Live'."""
    self_video: bool
    """Whether this user's camera is enabled."""
    suppress: bool
    """Whether this user is muted by the current user."""
    request_to_speak_timestamp: Timestamp = None
    """The time at which the user requested to speak."""


Voice = VoiceState
