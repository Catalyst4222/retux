from datetime import datetime
from enum import IntEnum, IntFlag

from attrs import define

from .application import Application
from .misc import Object, Partial, Timestamp
from .role import Role
from .sticker import Sticker, StickerItem
from .user import User

__all__ = (
    "Channel",
    "TextChannel",
    "GuildChannel",
    "GuildText",
    "AnnouncementChannel",
    "ForumChannel",
    "DMChannel",
    "ThreadChannel",
    "GuildVoice",
    "VoiceChannel",
    "StageChannel",
    "FollowedChannel",
    "MessageActivity",
    "ChannelType",
    "ChannelFlags",
    "MessageType",
    "MessageActivityType",
    "MessageFlags",
    "VideoQualityMode",
    "Reaction",
    "Overwrite",
    "MessageActivity",
    "MessageReference",
    "ChannelMention",
    "ThreadMetadata",
    "ThreadMember",
    "_EmbedMedia",
    "_EmbedProvider",
    "_EmbedAuthor",
    "_EmbedFooter",
    "_EmbedField",
    "Embed",
    "Attachment",
    "Message",
)


class ChannelType(IntEnum):
    """
    Represents the types of channels from Discord

    Constants
    ---------
    GUILD_TEXT
        A text channel within a server.
    DM
        A direct message between users.
    GUILD_VOICE
        A voice channel within a server.
    GROUP_DM
        A direct message between multiple users.
    GUILD_CATEGORY
        An organizational category that contains up to 50 channels.
    GUILD_NEWS
        A channel that users can follow and crosspost into their own server.
    GUILD_NEWS_THREAD
        A temporary sub-channel within a GUILD_NEWS channel.
    GUILD_PUBLIC_THREAD
        A temporary sub-channel within a GUILD_TEXT channel.
    GUILD_PRIVATE_THREAD
        A temporary sub-channel within a GUILD_TEXT channel.

        Only viewable by those invited and those with the MANAGE_THREADS permission
    GUILD_STAGE_VOICE
        A voice channel for hosting events with an audience.
    GUILD_DIRECTORY
        The channel in a hub containing the listed servers.
    GUILD_FORUM
        A channel that can only contain threads.
    """

    GUILD_TEXT = 0
    """A text channel within a server."""
    DM = 1
    """A direct message between users."""
    GUILD_VOICE = 2
    """A voice channel within a server."""
    GROUP_DM = 3
    """A direct message between multiple users."""
    GUILD_CATEGORY = 4
    """An organizational category that contains up to 50 channels."""
    GUILD_NEWS = 5
    """A channel that users can follow and crosspost into their own server."""
    GUILD_NEWS_THREAD = 10
    """A temporary sub-channel within a GUILD_NEWS channel."""
    GUILD_PUBLIC_THREAD = 11
    """A temporary sub-channel within a GUILD_TEXT channel."""
    GUILD_PRIVATE_THREAD = 12
    """
    A temporary sub-channel within a GUILD_TEXT channel.

    Only viewable by those invited and those with the MANAGE_THREADS permission
    """
    GUILD_STAGE_VOICE = 13
    """A voice channel for hosting events with an audience."""
    GUILD_DIRECTORY = 14
    """The channel in a hub containing the listed servers."""
    GUILD_FORUM = 15
    """A channel that can only contain threads."""


class VideoQualityMode(IntEnum):
    """
    Represents video quality modes from Discord

    Constants
    ---------
    AUTO
        Discord chooses the quality for optimal performance.
    FULL
        720p video resolution (1280x720).
    """

    AUTO = 1
    """Discord chooses the quality for optimal performance."""
    FULL = 2
    """720p video resolution (1280x720)."""


class ChannelFlags(IntFlag):
    """The bitwise values that represent channel flags from Discord"""

    PINNED = 1 << 1
    """
    This thread is pinned to the top of its parent channel.

    Only available on forum channels.
    """


class MessageType(IntEnum):
    """
    Represnts message types from Discord

    Constants
    ---------
    DEFAULT
        A normal message.
    RECIPIENT_ADD
        Unknown
    RECIPIENT_REMOVE
        Unknown
    CALL
        An indicator for a new voice call in a DM.
    CHANNEL_NAME_CHANGE
        A notification message for name of a channel changing.
    CHANNEL_ICON_CHANGE
        A notification message for the icon of a DM changing.
    CHANNEL_PINNED_MESSAGE
        A notification message for a new pinned message.
    USER_JOIN
        A notification message about the name of a channel changing.
    GUILD_BOOST
        A notification message about a new server boost(s).
    GUILD_BOOST_TIER_1
        A notification message about a guild reaching level 1 boost perks.
    GUILD_BOOST_TIER_2
        A notification message about a guild reaching level 2 boost perks.
    GUILD_BOOST_TIER_3
        A notification message about a guild reaching level 3 boost perks.
    CHANNEL_FOLLOW_ADD
        A notification message about a new follower of a news channel.
    GUILD_DISCOVERY_DISQUALIFIED
        A notification message about a guild being disqualified for discovery.
    GUILD_DISCOVERY_REQUALIFIED
        A notification message about a guild being requalified for discovery.
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING
        An intial warning for a discovery grace period.
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING
        A final warning for a discovery grace period.
    THREAD_CREATED
        A notification message for a new thread in a channel.
    REPLY
        A reply to a message.
    CHAT_INPUT_COMMAND
        A resulting message from a slash command being used.
    THREAD_STARTER_MESSAGE
        A starter message for a thread.
    GUILD_INVITE_REMINDER
        A reminder about a guild invite.
    CONTEXT_MENU_COMMAND
        A resulting message from a context menu command being used.
    AUTO_MODERATION_ACTION
        A message from AutoMod describing an action it took.
    """

    DEFAULT = 0
    """A normal message."""
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    """An indicator for a new voice call in a DM."""
    CHANNEL_NAME_CHANGE = 4
    """A notification message for name of a channel changing."""
    CHANNEL_ICON_CHANGE = 5
    """A notification message for the icon of a DM changing."""
    CHANNEL_PINNED_MESSAGE = 6
    """A notification message for a new pinned message."""
    USER_JOIN = 7
    """A notification message about the name of a channel changing."""
    GUILD_BOOST = 8
    """A notification message about a new server boost(s)."""
    GUILD_BOOST_TIER_1 = 9
    """A notification message about a guild reaching level 1 boost perks."""
    GUILD_BOOST_TIER_2 = 10
    """A notification message about a guild reaching level 2 boost perks."""
    GUILD_BOOST_TIER_3 = 11
    """A notification message about a guild reaching level 3 boost perks."""
    CHANNEL_FOLLOW_ADD = 12
    """A notification message about a new follower of a news channel."""
    GUILD_DISCOVERY_DISQUALIFIED = 14
    """A notification message about a guild being disqualified for discovery."""
    GUILD_DISCOVERY_REQUALIFIED = 15
    """A notification message about a guild being requalified for discovery."""
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    """An intial warning for a discovery grace period."""
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    """A final warning for a discovery grace period."""
    THREAD_CREATED = 18
    """A notification message for a new thread in a channel."""
    REPLY = 19
    """A reply to a message."""
    CHAT_INPUT_COMMAND = 20
    """A resulting message from a slash command being used."""
    THREAD_STARTER_MESSAGE = 21
    """A starter message for a thread."""
    GUILD_INVITE_REMINDER = 22
    """A reminder about a guild invite."""
    CONTEXT_MENU_COMMAND = 23
    """A resulting message from a context menu command being used."""
    AUTO_MODERATION_ACTION = 24
    """A message from AutoMod describing an action it took."""


class MessageActivityType(IntEnum):
    """
    Represents a message activity type from Discord.

    Constants
    ---------
    JOIN
        A join message activity.
    SPECTATE
        A spectate message activity.
    LISTEN
        A listen message activity.
    JOIN_REQUEST
        A join request message activity.
    """

    JOIN = 1
    """A join message activity."""
    SPECTATE = 2
    """A spectate message activity."""
    LISTEN = 3
    """A listen message activity."""
    JOIN_REQUEST = 5
    """A join request message activity."""


class MessageFlags(IntFlag):
    """The bitwise values that represent message flags from Discord"""

    CROSSPOSTED = 1 << 0
    """This message has been published to subscribed channels."""
    IS_CROSSPOST = 1 << 1
    """This message originated from a message in another channel."""
    SUPPRESS_EMBEDS = 1 << 2
    """Do not include any embeds when serializing this message."""
    SOURCE_MESSAGE_DELETED = 1 << 3
    """The source message for this crosspost has been deleted."""
    URGENT = 1 << 4
    """This message came from the urgent message system."""
    HAS_THREAD = 1 << 5
    """This message has an associated thread, with the same ID as the message."""
    EPHEMERAL = 1 << 6
    """This message is only visible to the user who invoked the interaction."""
    LOADING = 1 << 7
    """This message is an interaction response showing that the bot is "thinking"."""
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8
    """This message failed to mention some roles and add their members to the thread."""


@define(kw_only=True)
class Reaction:
    """
    Represents a reaction to a message from Discord.

    Attributes
    ----------
    count : `int`
        Number of reactions using the emoji.
    me : `bool`
        Whether or not the current user has reacted using this emoji.
    emoji : `EmojiPartial`
        Information about the emoji of the reaction.
    """

    count: int
    """Number of reactions using the emoji."""
    me: bool
    """Whether or not the current user has reacted using this emoji."""
    # TODO: Implement Partial Emoji object.
    # emoji: PartialEmoji = field(converter=PartialEmoji._c)
    """Information about the emoji of the reaction."""


@define(kw_only=True)
class Overwrite(Object):
    """
    Represents a permission overwrite from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the role or user.
    type : `int`
        The type of overwrite.

        Use `0` for to overwrite a role's permission and `1` to overwrite a guild member's permission.
    allow : `str`
        The bit set representing the overwrite's allowed permissions.
    deny : `str`
        The bit set representing the overwrite's denied permissions.
    """

    id: int
    """The ID of the role or user."""
    type: int
    """
    The type of overwrite.

    Use `0` for to overwrite a role's permission and `1` to overwrite a guild member's permission.
    """
    allow: str
    """The bit set representing the overwrite's allowed permissions."""
    deny: str
    """The bit set representing the overwrite's denied permissions."""


@define(kw_only=True)
class MessageActivity:
    """
    Represents a message activity structure from Discord.

    Attributes
    ----------
    type : `int`
        The type of message activity.
    party_id : `int`, optional
        The ID of a party from a rich presence event.
    """

    type: MessageActivityType
    """The type of message activity."""
    party_id: int | None = None
    """The ID of a party from a rich presence event."""


@define(kw_only=True)
class MessageReference:
    """
    Represents a reference to a message from Discord.

    Attributes
    ----------
    message_id : `int`, optional
        The ID of the originating message.
    channel_id : `int`, optional
        The ID of the originating message's channel.
    guild_id : `int`, optional
        The ID of the originating message's guild.
    fail_if_not_exists : `bool`
        Whether or not to error if the referenced doesn't exist.

        If `False`, sends as a normal, non-reply message.
    """

    message_id: int | None = None
    """The ID of the originating message."""
    channel_id: int | None = None
    """The ID of the originating message's channel."""
    guild_id: int | None = None
    """The ID of the originating message's guild."""
    fail_if_not_exists: bool = True
    """
    Whether or not to error if the referenced doesn't exist.

    If `False`, sends as a normal, non-reply message.
    """


@define(kw_only=True)
class FollowedChannel:
    """
    Represents a followed channel from Discord.

    Attributes
    ----------
    channel_id : `int`
        The ID of the source channel.
    webhook_id : `int`
        The ID of the created target webhook.
    """

    channel_id: int
    """The ID of the source channel."""
    webhook_id: int
    """The ID of the created target webhook."""


@define(kw_only=True)
class ChannelMention(Object):
    """
    Represents a channel mentioned in a message from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the channel being mentioned.
    guild_id : `int`
        The ID of the guild containing the channel being mentioned.
    type : `ChannelType`
        The type of the channel being mentioned.
    name : `str`
        The name of the channel being mentioned.
    """

    id: int
    """The ID of the channel being mentioned."""
    guild_id: int
    """The ID of the guild containing the channel being mentioned."""
    type: ChannelType
    """The type of the channel being mentioned."""
    name: str
    """The name of the channel being mentioned."""


@define(kw_only=True)
class ThreadMetadata:
    """
    Represents a thread metadata structure from Discord.

    Attributes
    ----------
    archived : `bool`
        Whether or not the thread is currently archived.
    auto_archive_duration : `int`
        The amount of minutes after the last message was sent before
        Discord automatically archives the thread.
    archive_timestamp : `datetime`
        When the thread's archive status last changed, used for
        calculating recent activity.
    locked : `bool`
        Whether or not the thread is locked.

        If a thread is locked, only users with MANAGE_THREADS permissions
        can unarchive it.
    invitable : `bool`
        Whether or not non-moderators can add other non-moderators to a thread.

        Only availible an private threads.
    create_timestamp: `datetime`, optional
        When the thread was created.

        Always populated unless the thread was created.
    """

    archived: bool
    """Whether or not the thread is currently archived."""
    auto_archive_duration: int
    """
    The amount of minutes after the last message was sent before
    Discord automatically archives the thread.
    """
    archive_timestamp: Timestamp
    """When the thread's archive status last changed, used for calculating recent activity."""
    locked: bool
    """
    Whether or not the thread is locked.

    If a thread is locked, only users with MANAGE_THREADS permissions can unarchive it.
    """
    invitable: bool
    """
    Whether or not non-moderators can add other non-moderators to a thread.

    Only availible an private threads.
    """
    create_timestamp: Timestamp = None
    """
    When the thread was created.

    Always populated unless the thread was created.
    """


@define(kw_only=True)
class ThreadMember(Object):
    """
    Represents a thread member structure from Discord.

    Attributes
    ----------
    id : `int`, optional
        The ID of the thread.

        This field is omitted on the member sent within each thread in GUILD_CREATE.
    user_id : `int`
        The ID of the user.

        This field is omitted on the member sent within each thread in GUILD_CREATE.
    join_timestamp : `datetime`
        When the user joined the thread.
    flags : `int`
        The flags for any user-thread settings.

        This is not needed by the bot; it is only used for client notifications.
    """

    id: int | None = None
    """
    The ID of the thread.

    This field is omitted on the member sent within each thread in GUILD_CREATE.
    """
    user_id: int
    """
    The ID of the user.

    This field is omitted on the member sent within each thread in GUILD_CREATE.
    """
    join_timestamp: Timestamp
    """When the user joined the thread."""
    flags: int
    """
    The flags for any user-thread settings.

    This is not needed by the bot; it is only used for client notifications.
    """


# todo: fix the docstrings
@define(kw_only=True)
class Channel(Partial, Object):
    """
    Represents a channel from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the channel.
    type : `ChannelType`
        The type of the channel.
    guild_id : `int`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `int`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    bitrate : `int`, optional
        The bitrate of the voice channel.
    user_limit : `int`, optional
        The user limit of the voice channel.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    recipients : `list[User]`, optional
        The recipients of the dm.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `int`, optional
        The ID of the creator of the group dm or thread.
    application_id : `int`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `int`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    rtc_region : `str`, optional
        The channel's voice region ID if present, set to automatic when left as `None`..
    video_quality_mode : `VideoQualityMode`, optional
        The video quality mode of the voice channel.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    def __new__(cls, *args, **kwargs):
        if cls is not Channel:
            return object.__new__(cls)

        # some fun magic to get the right type if a plain Channel is created
        match kwargs.get("type"):
            case ChannelType.DM:
                return object.__new__(DMChannel)
            case ChannelType.GUILD_TEXT:
                return object.__new__(GuildText)
            case ChannelType.GUILD_VOICE:
                return object.__new__(GuildVoice)
            case ChannelType.GUILD_FORUM:
                return object.__new__(ForumChannel)
            case ChannelType.GUILD_NEWS:
                return object.__new__(AnnouncementChannel)
            case ChannelType.GUILD_STAGE_VOICE:
                return object.__new__(StageChannel)
            case ChannelType.GUILD_NEWS_THREAD | ChannelType.GUILD_PUBLIC_THREAD | ChannelType.GUILD_PRIVATE_THREAD:
                return object.__new__(ThreadChannel)
            case ChannelType.GUILD_CATEGORY:
                return object.__new__(GuildChannel)
            case _:
                return object.__new__(Channel)

    id: int
    """The ID of the channel."""
    type: ChannelType
    """The type of the channel."""
    guild_id: int | None = None
    """
    The ID of the guild.

    This is nullable due to some Gateway events
    lacking the data for the ID.
    """
    position: int | None = None
    """Sorted position of the channel."""
    permission_overwrites: list[Overwrite] = None
    """Explicit permission overwrites for members and roles."""
    name: str = None
    """
    The name of the channel.

    A channel name is in-between 1-100 characters.
    """
    topic: str = None
    """
    The topic of the channel.

    A channel topic is in-between 1-1024 characters.
    """
    nsfw: bool = False
    """Whether or not the channel is NSFW. Defaults to `False`."""
    last_message_id: int | None = None
    """
    The ID of the last message sent in this channel.

    Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    """
    bitrate: int | None = None
    """The bitrate of the voice channel."""
    user_limit: int | None = None
    """The user limit of the voice channel."""
    rate_limit_per_user: int | None = None
    """
    Amount of seconds a user has to wait before sending another message

    Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    """
    recipients: list[User] = None
    """The recipients of the dm."""
    icon: str = None
    """The hash for the channel's icon."""
    owner_id: int | None = None
    """The ID of the creator of the group dm or thread."""
    application_id: int | None = None
    """The ID of the application that created the dm if it is bot-created."""
    parent_id: int | None = None
    """
    The ID of the parent of the channel

    Represents the parent category for regular channels and the parent channel for threads.
    """
    last_pin_timestamp: str = None
    """The time when the last message was pinned."""
    rtc_region: str = None
    """The channel's voice region ID if present, set to automatic when left as `None`."""
    video_quality_mode: VideoQualityMode = None
    """The video quality mode of the voice channel."""
    message_count: int | None = None
    """"
    The approximated amount of messages in a thread.

    Stops counting at `50`.
    """
    member_count: int | None = None
    """
    The approximated amount of users in a thread.

    Stops counting at `50`.
    """
    thread_metadata: ThreadMetadata = None
    """Thread-specific fields not needed by other channels."""
    member: ThreadMember = None
    """
    The thread member representation of the user if they have joined the thread.

    This is only included on certain api endpoints.
    """
    default_auto_archive_duration: int | None = None
    """
    The default archive duration for threads in minutes.

    Can be set to `60`, `1440`, `4320`, `10080`.
    """
    permissions: str = None
    """
    The computed permissions for the invoking user in the channel, including any overwrites.

    Only included when part of the resolved data received on a slash command interaction.
    """
    flags: ChannelFlags = None
    """Channel flags combined as a bitfield."""


@define(kw_only=True)
class TextChannel(Channel):  # todo add sendable abc
    """
    Represents a text channel from Discord.

    ---

    This is an event-specific dataclass that is not passed by
    Discord's Gateway. This will only contain the data relevant
    to a text channel -- and just the `id` of it.

    ---

    Attributes
    ----------
    id : `int`
        The ID of the channel.
    guild_id : `int`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `int`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `int`, optional
        The ID of the creator of the group dm or thread.
    application_id : `int`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `int`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    id: int
    """The ID of the channel."""
    name: str = None
    """
    The name of the channel.

    A channel name is in-between 1-100 characters.
    """
    topic: str = None
    """
    The topic of the channel.

    A channel topic is in-between 1-1024 characters.
    """
    last_message_id: int | None = None
    """
    The ID of the last message sent in this channel.

    Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    """
    last_pin_timestamp: str = None
    """The time when the last message was pinned."""
    permissions: str = None
    """
    The computed permissions for the invoking user in the channel, including any overwrites.

    Only included when part of the resolved data received on a slash command interaction.
    """


class GuildChannel(Channel):
    """ """

    name: str = None
    """
    The name of the channel.

    A channel name is in-between 1-100 characters.
    """
    guild_id: int | None = None
    """
    The ID of the guild.

    This is nullable due to some Gateway events
    lacking the data for the ID.
    """
    parent_id: int | None = None
    """
    The ID of the parent of the channel

    Represents the parent category for regular channels and the parent channel for threads.
    """
    position: int | None = None
    """Sorted position of the channel."""
    nsfw: bool = False
    """Whether or not the channel is NSFW. Defaults to `False`."""
    permission_overwrites: list[Overwrite] = None
    """Explicit permission overwrites for members and roles."""


class GuildText(GuildChannel, TextChannel):
    """ """

    topic: str = None
    """
    The topic of the channel.

    A channel topic is in-between 1-1024 characters.
    """
    default_auto_archive_duration: int | None = None
    """
    The default archive duration for threads in minutes.

    Can be set to `60`, `1440`, `4320`, `10080`.
    """
    rate_limit_per_user: int | None = None
    """
    Amount of seconds a user has to wait before sending another message

    Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    """


@define(kw_only=True)
class AnnouncementChannel(GuildChannel):
    """
    Represents an announcement channel on Discord.

    ---

    This information is essentially in vogue the same as a
    text channel, presented with the `TextChannel` object.

    ---

    Attributes
    ----------
    id : `int`
        The ID of the channel.
    guild_id : `int`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `int`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `int`, optional
        The ID of the creator of the group dm or thread.
    application_id : `int`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `int`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """


@define(kw_only=True)
class ForumChannel(GuildChannel):
    """
    Represents a forum channel on Discord.

    ---

    This information is essentially in vogue the same as a
    text channel, presented with the `TextChannel` object.

    ---

    Attributes
    ----------
    id : `int`
        The ID of the channel.
    guild_id : `int`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `int`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `int`, optional
        The ID of the creator of the group dm or thread.
    application_id : `int`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `int`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    flags: ChannelFlags = None
    """Channel flags combined as a bitfield."""

    # todo fix these up (https://discord.com/developers/docs/resources/channel#modify-channel-json-params-guild-channel)
    available_tags: list["Tag"]  # noqa
    default_reaction_emoji: "DefaultReaction"  # noqa
    default_thread_rate_limit_per_user: int
    default_sort_order: int


@define(kw_only=True)
class DMChannel(TextChannel):
    """
    Represents a DM channel on Discord.

    ---

    This information is essentially in vogue the same as a
    text channel, presented with the `TextChannel` object.

    ---

    Attributes
    ----------
    id : `int`
        The ID of the channel.
    guild_id : `int`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    topic : `str`, optional
        The topic of the channel.

        A channel topic is in-between 1-1024 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `int`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `int`, optional
        The ID of the creator of the group dm or thread.
    application_id : `int`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `int`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    recipients: list[User] = None
    """The recipients of the dm."""
    icon: str = None
    """The hash for the dm channel's icon."""
    owner_id: int | None = None
    """The ID of the creator of the group dm."""
    application_id: int | None = None
    """The ID of the application that created the dm if it is bot-created."""


@define(kw_only=True)
class ThreadChannel(GuildText):
    """
    Represents a thread channel from Discord.

    ---

    This is an event-specific dataclass that is not passed by
    Discord's Gateway. This will only contain the data relevant
    to a thread channel -- and just the `id` of it. `type` is
    dropped as this is already given for the event handler via.
    specification in the typehinting.

    ---

    Attributes
    ----------
    id : `int`
        The ID of the channel.
    guild_id : `int`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    last_message_id : `int`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `int`, optional
        The ID of the creator of the group dm or thread.
    parent_id : `int`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    owner_id: int | None = None
    """The ID of the creator of the thread."""
    message_count: int | None = None
    """"
    The approximated amount of messages in a thread.

    Stops counting at `50`.
    """
    member_count: int | None = None
    """
    The approximated amount of users in a thread.

    Stops counting at `50`.
    """
    thread_metadata: ThreadMetadata = None
    """Thread-specific fields not needed by other channels."""
    member: ThreadMember = None
    """
    The thread member representation of the user if they have joined the thread.

    This is only included on certain api endpoints.
    """
    default_auto_archive_duration: int | None = None
    """
    The default archive duration for threads in minutes.

    Can be set to `60`, `1440`, `4320`, `10080`.
    """
    permissions: str = None
    """
    The computed permissions for the invoking user in the channel, including any overwrites.

    Only included when part of the resolved data received on a slash command interaction.
    """


class GuildVoice(Channel):  # All voice things have to be in a guild, right?
    """ """

    bitrate: int | None = None
    """The bitrate of the voice channel."""
    rtc_region: str = None
    """The channel's voice region ID if present, set to automatic when left as `None`."""
    video_quality_mode: VideoQualityMode = None
    """The video quality mode of the voice channel."""


@define(kw_only=True)
class VoiceChannel(GuildVoice):  # todo add sendable abc
    """
    Represents a voice channel from Discord.

    ---

    This is an event-specific dataclass that is not passed by
    Discord's Gateway. This will only contain the data relevant
    to a voice channel -- and just the `id` of it. `type` is
    dropped as this is already given for the event handler via.
    specification in the typehinting.

    ---

    Attributes
    ----------
    id : `int`
        The ID of the channel.
    guild_id : `int`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    nsfw : `bool`, optional
        Whether or not the channel is NSFW. Defaults to `False`.
    last_message_id : `int`, optional
        The ID of the last message sent in this channel

        Can also be a thread if the channel is a forum. May not be an existing or valid message or thread.
    bitrate : `int`, optional
        The bitrate of the voice channel.
    user_limit : `int`, optional
        The user limit of the voice channel.
    rate_limit_per_user : `int`, optional
        Amount of seconds a user has to wait before sending another message

        Can be a number up to 21600. Bots, as well as users with the permission manage_messages or manage_channel, are unaffected.
    icon : `str`, optional
        The hash for the channel's icon.
    owner_id : `int`, optional
        The ID of the creator of the group dm or thread.
    application_id : `int`, optional
        The ID of the application that created the dm if it is bot-created.
    parent_id : `int`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    last_pin_timestamp : `str`, optional
        The time when the last message was pinned.
    rtc_region : `str`, optional
        The channel's voice region ID if present, set to automatic when left as `None`..
    video_quality_mode : `VideoQualityMode`, optional
        The video quality mode of the voice channel.
    message_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    member_count : `int`, optional
        An approximate count of messages in a thread.

        Stops counting at `50`.
    thread_metadata : `ThreadMetadata`, optional
        Thread-specific fields not needed by other channels.
    member : `ThreadMember`, optional
        Thread member object for the current user if they have joined the thread

        This is only included on certain api endpoints.
    default_auto_archive_duration : `int`, optional
        The default archive duration for threads in minutes.

        Can be set to `60`, `1440`, `4320`, `10080`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """

    user_limit: int | None = None
    """The user limit of the voice channel."""


@define(kw_only=True)
class StageChannel(Partial, Object):
    """
    Represents a stage channel from Discord.

    ---

    This is an event-specific dataclass that is not passed by
    Discord's Gateway. This will only contain the data relevant
    to a stage channel -- and just the `id` of it. `type` is
    dropped as this is already given for the event handler via.
    specification in the typehinting.

    ---

    Attributes
    ----------
    id : `int`
        The ID of the channel.
    guild_id : `int`, optional
        The ID of the guild.
        This is nullable due to some Gateway events
        lacking the data for the ID.
    position : `int`, optional
        Sorted position of the channel.
    permission_overwrites : `list[Overwrite]`, optional
        Explicit permission overwrites for members and roles.
    name : `str`, optional
        The name of the channel.

        A channel name is in-between 1-100 characters.
    bitrate : `int`, optional
        The bitrate of the voice channel.
    icon : `str`, optional
        The hash for the channel's icon.
    parent_id : `int`, optional
        The ID of the parent of the channel

        Represents the parent category for regular channels and the parent channel for threads.
    rtc_region : `str`, optional
        The channel's voice region ID if present, set to automatic when left as `None`.
    permissions : `str`, optional
        Computed permissions for the invoking user in the channel, including overwrites.

        Only included when part of the resolved data received on a slash command interaction.
    flags : `ChannelFlags`, optional
        Channel flags combined as a bitfield.
    """


@define(kw_only=True)
class _EmbedMedia:
    """
    Represents an embed thumbnail, video or image from Discord.

    Attributes
    ----------
    url : `str`, optional
        The url to the source of the media.

        The url is only needed for non-video contents.
    proxied_url : `str`, optional
        A proxied url of the media.
    height : `int`, optional
        The height of the media.
    width : `int`, optional
        The width of the media.
    """

    url: str = None
    """
    The url to the source of the media.

    The url is only needed for non-video contents.
    """
    proxy_url: str = None
    """A proxied url of the media."""
    height: int | None = None
    """The height of the media."""
    width: int | None = None
    """The width of the media."""


@define(kw_only=True)
class _EmbedProvider:
    """
    Represents the provider of an embed from Discord.

    Attributes
    ----------
    name : `str`, optional
        The of the provider.
    url : `str`, optional
        The url of the provider.
    """

    name: str = None
    """The of the provider."""
    url: str = None
    """The url of the provider."""


@define(kw_only=True)
class _EmbedAuthor:
    """
    Represents the author of an embed from Discord.

    Attributes
    ----------
    name : `str`, optional
        The name of the author.
    url : `str`, optional
        The URL of the author.
    icon_url : `str`, optional
        The URL of author's icon.
    proxy_icon_url : `str`, optional
        The proxied URL of the author's icon.
    """

    name: str = None
    """The name of the author."""
    url: str = None
    """The URL of the author."""
    icon_url: str = None
    """The URL of author's icon."""
    proxy_icon_url: str = None
    """The proxied URL of the author's icon."""


@define(kw_only=True)
class _EmbedFooter:
    """
    Represents the footer of an embed from Discord.

    Attributes
    ----------
    text : `str`, optional
        The footer text of an embed.
    icon_url : `str`, optional
        The URL of the footer icon.

        Only supports http(s) and attachments.
    proxy_icon_url : `str`, optional
        A proxied URL of the footer icon.
    """

    text: str = None
    """The footer text of an embed."""
    icon_url: str = None
    """
    The URL of the footer icon.

    Only supports http(s) and attachments.
    """
    proxy_icon_url: str = None
    """A proxied URL of the footer icon."""


@define(kw_only=True)
class _EmbedField:
    """
    Represents a field of an embed from Discord.

    Attributes
    ----------
    name : `str`
        The name of the embed field.
    value : `str`
        The value of the embed field.
    inline : `bool`
        Whether or not the embed field is placed inline with other embed fields.
    """

    name: str
    """The name of the embed field."""
    value: str
    """The value of the embed field."""
    inline: bool = None
    """Whether or not the embed field is placed inline with other embed fields."""


@define(kw_only=True, frozen=True)
class Embed:
    """
    Represnts a message embed from Discord.

    Attributes
    ----------
    title : `str`, optional
        The title of the embed.
    type : `str`, optional
        The type of the embed.

        This will always be `"rich"` for webhook embeds.
    description : `str`, optional
        The description of the embed.
    url : `str`, optional
        The url of the embed. This makes the title of the event a hyperlink.
    timestamp : `str`, optional
        The timestamp of the embed. This appears at the bottom.
    color : `Color`, optional
        The color of the embed.
    footer : `_EmbedFooter`, optional
        The footer of the embed.
    image : `_EmbedMedia`, optional
        The image of the embed. This is a large image displayed under the title.
    thumbnail : `_EmbedMedia`, optional
        The thumbnail of the embed. This is displayed as a small image on the embed.
    video : `_EmbedMedia`, optional
        The video of the embed.

        This cannot be used for embeds from bots.
    provider : `_EmbedMedia`, optional
        The provider of the embed.

        This cannot be used for embeds from bots.
    author : `_EmbedAuthor`, optional
        The author of the embed.
    fields : `list[_EmbedField]`, optional
        The fields of the embed.
    """

    title: str = None
    """The title of the embed."""
    type: str = None
    """
    The type of the embed.

    This will always be `"rich"` for webhook embeds.
    """
    description: str = None
    """The description of the embed."""
    url: str = None
    """The url of the embed. This makes the title of the event a hyperlink."""
    timestamp: Timestamp = None
    """The timestamp of the embed. This appears at the bottom."""
    # TODO: implement Color abc
    # color: int | Color | None = field(converter=optional_c(Color), default=None)
    """The color of the embed."""
    footer: _EmbedFooter = None
    """The footer of the embed."""
    image: _EmbedMedia = None
    """The image of the embed. This is a large image displayed under the title."""
    thumbnail: _EmbedMedia = None
    """The thumbnail of the embed. This is displayed as a small image on the embed."""
    video: _EmbedMedia = None
    """
    The video of the embed.

    This cannot be used for embeds from bots.
    """
    provider: _EmbedProvider = None
    """
    The provider of the embed.

    This cannot be used for embeds from bots.
    """
    author: _EmbedAuthor = None
    """The author of the embed."""
    fields: list[_EmbedField] = None
    """The fields of the embed."""


@define(kw_only=True)
class Attachment(Object):
    """
    Represents an attachment from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the attachment.
    filename : `str`, optional
        The name of the attached file.

        Always provided by Discord. Optional for bot use.
    description : `str`, optional
        The description of the attached file.
    content_type : `str`, optional
        The type of media attached.
    size : `int`, optional
        The size of the attached file in bytes.

        Always provided by Discord. Optional for bot use.
    url : `str`, optional
        The source URL of the file.

        Always provided by Discord. Optional for bot use.
    proxy_url : `str`, optional
        A proxied URL of the file.

        Always provided by Discord. Optional for bot use.
    height : `int`, optional
        The height of the file.

        This is only used for images.
    width : `int`, optional
        The height of the file.

        This is only used for images.
    ephemeral : `bool`, optional
        Whether or not the attachment is ephemeral.
    """

    id: int
    """The ID of the attachment."""
    filename: str = None
    """
    The name of the attached file.

    Always provided by Discord. Optional for bot use.
    """
    description: str = None
    """The description of the attached file."""
    content_type: str = None
    """The type of media attached."""
    size: int | None = None
    """
    The size of the attached file in bytes.

    Always provided by Discord. Optional for bot use.
    """
    url: str = None
    """
    The source URL of the file.

    Always provided by Discord. Optional for bot use.
    """
    proxy_url: str = None
    """
    A proxied URL of the file.

    Always provided by Discord. Optional for bot use.
    """
    height: int | None = None
    """
    The height of the file.

    This is only used for images.
    """
    width: int | None = None
    """
    The height of the file.

    This is only used for images.
    """
    ephemeral: bool = None
    """Whether or not the attachment is ephemeral."""


@define(kw_only=True)
class Message(Object):
    """
    Represents a message from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the message.
    channel_id : `int`
        The ID of the channel containing the message.
    author : `User`
        The author of the message.
    content : `str`
        The content of the message.
    timestamp : `datetime`
        When the message was sent.
    edited_timestamp : `datetime`, optional
        When the message was last edited.
    tts : `bool`
        Whether or not this was a Text to Speech message.
    mention_everyone : `bool`
        Whether or not this message mentions everyone.
    mentions : `list[User]`
        Users specifically mentioned in this message.
    mention_roles : `list[Role]`
        Roles specifically mentioned in this message.
    mention_channels : `list[ChannelMention]`, optional
        Channels specifically mentioned in this message.
    attachments : `list[Attachment]`, optional
        The attachments of the message.
    embeds : `list[Embed]`
        The embeds of the message.
    reactions : `list[Reaction]`, optional
        The reactions to the message.
    nonce : `int | str`, optional
        Used for validating whether a message has been sent.
    pinned : `bool`
        Whether or not a message is pinned.
    webhook_id : `int`, optional
        The ID of the message's webhook, if the message was generated by a webhook.
    type : `MessageType`
        The type of the message.
    activity : `MessageActivity`, optional
        The activity of the message.

        Sent with Rich Presence related chat embeds.
    application : `Application`, optional
        The application of the message's activity.

        Sent with Rich Presence related chat embeds.
    application_id : `int`, optional
        The ID of the application.

        Sent if the message is an interactions or an application-owned webhook.
    message_reference : `MessageReference`, optional
        The source of a crosspost or the source of activity related to channel follows.
    flags : `MessageFlags`, optional
        Bitwise values representing a channel's flags.
    referenced_message : `Message`, optional
        The message associated with a message_reference.
    interaction : `Interaction`, optional
        The message's interaction if it is a response to an interaction.
    thread : `ThreadChannel`, optional
        The thread of the message, if it is the message that started a thread.
    components : `list[Component]`, optional
        The components on a message.
    sticker_items : `list[StickerItem]`, optional
        The items used to begin rendering the message's stickers.
    stickers : `list[Sticker]`, optional
        The stickers of a message.
    """

    id: int
    """The ID of the message."""
    channel_id: int
    """The ID of the channel containing the message."""
    author: User
    """The author of the message."""
    content: str
    """The content of the message."""
    timestamp: Timestamp
    """When the message was sent."""
    edited_timestamp: datetime
    """When the message was last edited."""
    tts: bool
    """Whether or not this was a Text to Speech message."""
    mention_everyone: bool
    """Whether or not this message mentions everyone."""
    mentions: list[User]
    """Users specifically mentioned in this message."""
    mention_roles: list[Role]
    """Roles specifically mentioned in this message."""
    mention_channels: list[ChannelMention] = None
    """Channels specifically mentioned in this message."""
    attachments: list[Attachment]
    """The attachments of the message."""
    embeds: list[Embed]
    """The embeds of the message."""
    reactions: list[Reaction] = None
    """The reactions to the message."""
    nonce: int | str = None
    """Used for validating whether a message has been sent."""
    pinned: bool
    """Whether or not a message is pinned."""
    webhook_id: int | None = None
    """The ID of the message's webhook, if the message was generated by a webhook."""
    type: MessageType
    """The type of the message."""
    activity: MessageActivity = None
    """
    The activity of the message.

    Sent with Rich Presence related chat embeds.
    """
    application: Application = None
    """
    The application of the message's activity.

    Sent with Rich Presence related chat embeds.
    """
    application_id: int | None = None
    """
    The ID of the application.

    Sent if the message is an interactions or an application-owned webhook.
    """
    message_reference: MessageReference = None
    """The source of a crosspost or the source of activity related to channel follows."""
    flags: MessageFlags = None
    """Bitwise values representing a channel's flags."""
    referenced_message: dict = None
    # TODO: Implement recursive converters (its a Message object)
    """The message associated with a message_reference."""
    # TODO: Implement Interaction object.
    # interaction: dict | Interaction | None = field(converter=optional_c(Interaction), default=None)
    """# The message's interaction if it is a response to an interaction."""
    thread: ThreadChannel = None
    """The thread of the message, if it is the message that started a thread."""
    # TODO: Implement Component object.
    # components: list[dict] | list[Component] | None = field(converter=optional_c(list_c(Component)), default=None)
    # """The components on a message."""
    sticker_items: list[StickerItem] = None
    """The items used to begin rendering the message's stickers."""
    stickers: list[Sticker] = None
    """The stickers of a message."""
