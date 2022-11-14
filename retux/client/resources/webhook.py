from enum import IntEnum

from attrs import define

from .channel import Channel
from .guild import Guild
from .misc import Object
from .user import User


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


@define(kw_only=True)
class Webhook(Object):
    """
    Represents a webhook from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the webhook.
    type : `WebhookType`
        The type of the webhook.
    guild_id : `int`, optional
        The guild ID this webhook is for, if any.
    channel_id : `int`, optional
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
    application_id : `int`, optional
        The bot/OAuth2 application that created this webhook, if any.
    source_guild : `Guild`, optional
        The guild of the channel that this webhook is following, if any. Returned for `CHANNEL_FOLLOWER` webhooks.
    soruce_channel : `Channel`, optional
        The channel that this webhook is following, if any. Returned for `CHANNEL_FOLLOWER` webhooks.
    url : `str`, optional
        The url used for executing the webhook, if any. This is returned by the webhooks OAuth2 flow.
    """

    id: int
    """The ID of the webhook."""
    type: WebhookType
    """The type of the webhook."""
    guild_id: int | None = None
    """The guild ID this webhook is for, if any."""
    channel_id: int | None = None
    """The channel ID this webhook is for, if any."""
    user: User = None
    """The user this webhook was created by, if any."""
    name: str = None
    """The default name of the webhook, if any."""
    avatar: str = None
    """The default user avatar hash of the webhook, if any."""
    token: str = None
    """The secure token of the webhook, if any. This is returned for `INCOMING` webhooks."""
    application_id: int | None = None
    """The bot/OAuth2 application that created this webhook, if any."""
    source_guild: Guild = None
    """The guild of the channel that this webhook is following, if any. Returned for `CHANNEL_FOLLOWER` webhooks."""
    source_channel: Channel = None
    """The channel that this webhook is following, if any. Returned for `CHANNEL_FOLLOWER` webhooks."""
    url: str = None
    """The url used for executing the webhook, if any. This is returned by the webhooks OAuth2 flow."""
