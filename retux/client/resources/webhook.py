from .abc import Snowflake, Object
from .user import User
from .guild import Guild
from .channel import Channel
from ..mixins import Serializable
from ...utils.converters import optional_c

from attrs import define, field
from enum import IntEnum


class WebhookType(IntEnum):
    """
    Represents the types of webhooks from Discord.

    Constants
    ---------
    INCOMING
        Incoming webhooks can post messages to channels with a generated token.
    CHANNEL_FOLLOWER
        Channel-Follower webhooks are internal webhooks used with channel following to post new messages into channels.
    APPLICATION
        Application webhooks are webhooks used with interactions.
    """

    INCOMING = 1
    """Incoming webhooks can post messages to channels with a generated token."""
    CHANNEL_FOLLOWER = 2
    """Channel-Follower webhooks are internal webhooks used with channel following to post new messages into channels."""
    APPLICATION = 3
    """Application webhooks are webhooks used with interactions."""


@define()
class Webhook(Object, Serializable):
    """
    Represents a webhook from Discord.

    Attributes
    ----------
    id : `Snowflake`
        The ID of the webhook.
    type : `WebhookType`
        The type of the webhook.
    guild_id : `Snowflake`, optional
        The guild ID this webhook is for, if any.
    channel_id : `Snowflake`, optional
        The channel ID this webhook is for, if any.
    user : `User`, optional
        The user this webhook was created by.

        Not included when getting a webhook by its token.
    name : `str`, optional
        The default name of the webhook, if any.
    avatar : `str`, optional
        The default user avatar hash of the webhook, if any.
    token : `str`, optional
        The secure token of the webhook, if any. This is returned for `INCOMING` webhooks.
    application_id : `Snowflake`, optional
        The bot/OAuth2 application that created this webhook, if any.
    source_guild : `Guild`, optional
        The guild of the channel that this webhook is following, if any. Returned for `CHANNEL_FOLLOWER` webhooks.
    soruce_channel : `Channel`, optional
        The channel that this webhook is following, if any. Returned for `CHANNEL_FOLLOWER` webhooks.
    url : `str`, optional
        The url used for executing the webhook, if any. This is returned by the webhooks OAuth2 flow.
    """

    id: Snowflake | str = field(converter=Snowflake)
    """The ID of the webhook."""
    type: int | WebhookType = field(converter=WebhookType)
    """The type of the webhook."""
    guild_id: str | Snowflake | None = field(converter=optional_c(Snowflake), default=None)
    """The guild ID this webhook is for, if any."""
    channel_id: str | Snowflake | None = field(converter=optional_c(Snowflake), default=None)
    """The channel ID this webhook is for, if any."""
    user: dict | User | None = field(converter=optional_c(User._c), default=None)
    """The user this webhook was created by, if any."""
    name: str | None = field(default=None)
    """The default name of the webhook, if any."""
    avatar: str | None = field(default=None)
    """The default user avatar hash of the webhook, if any."""
    token: str | None = field(default=None)
    """The secure token of the webhook, if any. This is returned for `INCOMING` webhooks."""
    application_id: str | Snowflake | None = field(converter=optional_c(Snowflake), default=None)
    """The bot/OAuth2 application that created this webhook, if any."""
    source_guild: dict | Guild | None = field(converter=optional_c(Guild), default=None)
    """The guild of the channel that this webhook is following, if any. Returned for `CHANNEL_FOLLOWER` webhooks."""
    source_channel: dict | Channel | None = field(converter=optional_c(Channel._c), default=None)
    """The channel that this webhook is following, if any. Returned for `CHANNEL_FOLLOWER` webhooks."""
    url: str | None = field(default=None)
    """The url used for executing the webhook, if any. This is returned by the webhooks OAuth2 flow."""
