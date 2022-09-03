from datetime import datetime
from enum import Enum
from typing import Union

from attrs import define, field

__all__ = ("Snowflake", "Image", "Partial", "Object", "Component")

from ...const import MISSING, NotNeeded


@define(repr=False, eq=False)
class Snowflake:
    """
    Represents an unique identifier for a Discord resource.

    ---

    Discord utilizes Twitter's snowflake format for uniquely identifiable descriptors
    (IDs). These IDs are guaranteed to be unique across all of Discord, except in some
    unique scenarios in which child objects share their parent's ID.

    ---

    Attributes
    ----------
    _snowflake : `str`
        The internally stored snowflake. Snowflakes are always in string-form.

        This value should never need to be directly checked. Please use the
        representation of the class itself to do this for identity comparisons.

    Methods
    -------
    timestamp : `datetime.datetime`
        The timestamp of the snowflake as a UTC-native datetime.

        Timestamps are denoted as milliseconds since the Discord Epoch:
        the first second of 2015, or or `1420070400000`.
    worker_id : `int`
        The internal worker ID of the snowflake.
    process_id : `int`
        The internal process ID of the snowflake.
    increment : `int`
        The internal incrementation number of the snowflake.

        This value will only increment when a process has been
        generated on this snowflake, e.g. a resource.
    """

    _snowflake: str | int = field(converter=str)
    """
    The internally stored snowflake. Snowflakes are always in string-form.

    The snowflake may only be `None` in the event that a given
    field in a resource does not supply it. This should not be always
    taken for granted as having a value. Please use the representation
    of the class itself.
    """

    def __repr__(self) -> str | None:
        return self._snowflake

    def __eq__(self, other: Union[str, int, "Snowflake"]) -> bool:
        if type(other) == int:
            return int(self._snowflake) == other
        else:
            return self._snowflake == str(other)

    @property
    def timestamp(self) -> datetime:
        """
        The timestamp of the snowflake as a UTC-native datetime.

        Timestamps are denoted as milliseconds since the Discord Epoch:
        the first second of 2015, or `1420070400000`.
        """
        retrieval: int | float = (int(self._snowflake) >> 22) + 1420070400000
        return datetime.utcfromtimestamp(retrieval)

    @property
    def worker_id(self) -> int:
        """The internal worker ID of the snowflake."""
        return (int(self._snowflake) & 0x3E0000) >> 17

    @property
    def process_id(self) -> int:
        """The internal process ID of the snowflake."""
        return (int(self._snowflake) & 0x1F000) >> 12

    @property
    def increment(self) -> int:
        """
        The internal incrementation number of the snowflake.

        This value will only increment when a process has been
        generated on this snowflake, e.g. a resource.
        """
        return int(self._snowflake) & 0xFFF


class CDNEndpoint(Enum):
    """
    Represents all of the different Discord
    CDN endpoints.

    Constants
    ---------
    CUSTOM_EMOJI
        The endpoint for custom emojis.

        The extra id is the emoji's ID.
    GUILD_ICON
        The endpoint for guild icons.

        The extra id is the guild's ID.
        Guild icons can be animated.
    GUILD_SPLASH
        The endpoint for guild splashes.

        The extra id is the guild's ID.
    GUILD_DISCOVERY_SPLASH
        The endpoint for guild discovery splashes.

        The extra id is the guild's ID.
    GUILD_BANNER
        The endpoint for guild banners.

        The extra id is the guild's ID.
    Guild banners can be animated.
    USER_BANNER
        The endpoint for user banners.

        The extra id is the user's ID.
    User banners can be animated.
    DEFAULT_USER_AVATAR
        The endpoint for the default avatars of users.

        The  extra id is the modulo 5 of
        the user's discriminator. The size param is
        ignored for this endpoint.
    USER_AVATAR
        The endpoint for user avatars.

        The extra id is the user's ID.
        User avatars can be animated
    GUILD_MEMBER_AVATAR
        The endpoint for guild-specific member avatars.

        The extra ids are the guild's ID
        and the user's ID. These can be animated.
    APPLICATION_ICON
        The endpoint for application icons.

        The extra id is the application's ID.
    APPLICATION_COVER
        The endpoint for application covers.

        The extra id is the application's ID.
    APPLICATION_ASSET
        The endpoint for application assets.

        The extra id is the applciation's ID.
    ACHIEVEMENT_ICON
        The endpoint for application icons.

        The extra id is the application's ID.
    STICKER_PACK_BANNER
        The endpoint for sticker pack banners.

        The extra id is the sticker pack
        banner asset's ID.
    TEAM_ICON
        The endpoint for team icons.

        The extra id is the team's ID.
    STICKER
        The endpoint for stickers.

        The extra id is the sticker's ID.
        The size parameter is ignored. Stickers can
        be animated.
    ROLE_ICON
        The endpoint for role icons.

        The extra id is the role's ID.
    GUILD_SCHEDULED_EVENT_COVER
        The endpoint for guild scheduled event covers.

        The extra id is the guild's ID.
    GUILD_MEMBER_BANNER
        The endpoint for guild member banners.

        The extra ids are the guild's ID
        and the user's ID.
    """

    CUSTOM_EMOJI = "emojis/{}"
    """
    The endpoint for custom emojis.

    The extra id is the emoji's ID.
    """
    GUILD_ICON = "icons/{}/{hash}"
    """
    The endpoint for guild icons.

    The extra id is the guild's ID.
    Guild icons can be animated.
    """
    GUILD_SPLASH = "splashes/{}/{hash}"
    """
    The endpoint for guild splashes.

    The extra id is the guild's ID.
    """
    GUILD_DISCOVERY_SPLASH = "discovery-splashes/{}/{hash}"
    """
    The endpoint for guild discovery splashes.

    The extra id is the guild's ID.
    """
    GUILD_BANNER = "banners/{}/{hash}"
    """
    The endpoint for guild banners.

    The extra id is the guild's ID.
    Guild banners can be animated.
    """
    USER_BANNER = "banners/{}/{hash}"
    """
    The endpoint for user banners.

    The extra id is the user's ID.
    User banners can be animated.
    """
    DEFAULT_USER_AVATAR = "embed/avatars/{}"
    """
    The endpoint for the default avatars of users.

    The  extra id is the modulo 5 of
    the user's discriminator. The size param is
    ignored for this endpoint.
    """
    USER_AVATAR = "avatars/{}/{hash}"
    """
    The endpoint for user avatars.

    The extra id is the user's ID.
    User avatars can be animated
    """
    GUILD_MEMBER_AVATAR = "guilds/{}/users/{}/avatars/{hash}"
    """
    The endpoint for guild-specific member avatars.

    The extra ids are the guild's ID
    and the user's ID. These can be animated.
    """
    APPLICATION_ICON = "app-icons/{}/{hash}"
    """
    The endpoint for application icons.

    The extra id is the application's ID.
    """
    APPLICATION_COVER = "app-icons/{}/{hash}"
    """
    The endpoint for application covers.

    The extra id is the application's ID.
    """
    APPLICATION_ASSET = "app-assets/{}/{hash}"
    """
    The endpoint for application assets.

    The extra id is the applciation's ID.
    """
    ACHIEVEMENT_ICON = "app-assests/{}/{hash}"
    """
    The endpoint for application icons.

    The extra id is the application's ID.
    """
    STICKER_PACK_BANNER = "app-assets/710982414301790216/store/{}"
    """
    The endpoint for sticker pack banners.

    The extra id is the sticker pack
    banner asset's ID.
    """
    TEAM_ICON = "team-icons/{}/{hash}"
    """
    The endpoint for team icons.

    The extra id is the team's ID.
    """
    STICKER = "stickers/{hash}"
    """
    The endpoint for stickers.

    The extra id is the sticker's ID.
    The size parameter is ignored. Stickers can
    be animated.
    """
    ROLE_ICON = "role-icons/{}/{hash}"
    """
    The endpoint for role icons.

    The extra id is the role's ID.
    """
    GUILD_SCHEDULED_EVENT_COVER = "guild-events/{}/{hash}"
    """
    The endpoint for guild scheduled event covers.

    The extra id is the guild's ID.
    """
    GUILD_MEMBER_BANNER = "guilds/{}/users/{}/banners/{hash}"
    """
    The endpoint for guild member banners.

    The extra ids are the guild's ID
    and the user's ID.
    """


@define(kw_only=True)
class Image:
    """
    Represents an image from Discord.

    Attributes
    ----------
    hash : `str`, optional
        The hash of the image.

    Methods
    -------
    animated : `bool`
        Whether or not the image is animated.
    path : `str`
        The path to the image in CDN.
    url : `str`
        The url to the image.
    """

    hash: str | None = field(default=None)
    """The hash of the image."""
    _endpoint: CDNEndpoint = field()
    """The endpoint of the image."""
    _ids: list | None = field(default=None)
    """
    The needed variables aside
    from the hash for the endpoint.
    """

    def _c(endpoint: CDNEndpoint):
        """
        For internal use only.

        Builds an attrs converter for Images.
        A `__post_attrs_init__` must be used
        to add extra variables needed in the
        endpoint such as ids. This is only
        meant for endpoints that need a hash.

        Please note that the naming of this method, `_c`
        does not reflect the same serialisation methods
        or strategies as `Serialisable._c()`.

        Parameters
        ----------
        endpoint : CDNEndpoint
            The endpoint of the image.

        Returns
        -------
        `function`
            A function that takes one argument
            (the hash). Compatible with attrs.
        """

        def inner(hash: str):
            return Image(hash=hash, endpoint=endpoint)

        return inner

    @property
    def animated(self) -> bool:
        """Whether or not the image is animated."""
        return self.hash and self.hash.startswith("a_")

    @property
    def path(self) -> str:
        """The path to the image in CDN."""
        if not self._ids:
            raise RuntimeError("Tried to access image endpoint without needed ids.")
        if "{hash}" in self._endpoint.value:
            return self._endpoint.value.format(*self._ids, hash=self.hash)
        else:
            return self._endpoint.value.format(*self._ids)

    @property
    def url(self) -> str:
        """The url to the image."""
        return f"https://cdn.discordapp.com/{self.path}"


class TimestampStyle(Enum):
    """
    The styles of a timestamp from Discord.

    Constants
    ---------
    SHORT_TIME
        Formats the timestamp as HH:mm.
    LONG_TIME
        Formats the timestamp as HH:mm:ss.
    SHORT_DATE
        Formats the timestamp as DD/MM/YYYY.
    LONG_DATE
        Formats the timestamp as DD Jj YYYY.
    SHORT_DATE_TIME
        Formats the timestamp as DD Jj YYYY HH:mm.
    LONG_DATE_TIME
        Formats the timestamp as J, DD Jj YYYY HH:mm.
    RELATIVE:
        Formats the timestamp as `x` (DD/MM/YY).
    """

    SHORT_TIME = "t"
    """Formats the timestamp as HH:mm."""
    LONG_TIME = "T"
    """Formats the timestamp as HH:mm:ss."""
    SHORT_DATE = "d"
    """Formats the timestamp as DD/MM/YYYY."""
    LONG_DATE = "D"
    """Formats the timestamp as DD Jj YYYY."""
    SHORT_DATE_TIME = "f"
    """Formats the timestamp as DD Jj YYYY HH:mm."""
    LONG_DATE_TIME = "F"
    """Formats the timestamp as J, DD Jj YYYY HH:mm."""
    RELATIVE = "R"
    """Formats the timestamp as `x` (DD/MM/YY)."""


@define(repr=False, eq=False)
class Timestamp:
    """
    Represents a formatted timestamp from Discord.

    ---

    This is an abstract base class used to help consistently
    control any `datetime` associated attributes. Because it's
    a bad practice to monkeypatch a solution into existing core
    modules, this helps serve as a further layer of abstraction.

    ---

    Attributes
    ----------
    _timestamp : `datetime`
        The Python formatted date and time of the timestamp. This
        is only used for internal reference. Please use the representation
        of the class instead.

    Methods
    -------
    mention(TimestampStyle.SHORT_DATE_TIME) : `str`
        Creates a mentionable format for the timestamp.
    """

    _timestamp: str | datetime = field(converter=datetime.fromisoformat)
    """
    The Python formatted date and time of the timestamp. This is only used for internal
    reference. Please use the representation of the class instead.
    """

    def __repr__(self) -> datetime:
        return self._timestamp

    def __eq__(self, other: str | datetime) -> bool:
        if type(other) == str:
            return str(self._timestamp) == other
        else:
            return self._timestamp == other

    def mention(self, style: NotNeeded[str | TimestampStyle] = MISSING) -> str:
        """
        Creates a mentionable format for the timestamp.

        Parameters
        ----------
        style : `str`, `TimestampStyle`, optional
            The style of the timestamp to use.
            Defaults to `TimestampStyle.SHORT_DATE_TIME`.

        Returns
        -------
        `str`
            The formatted timestamp as a string.
        """
        if style is MISSING:
            _style = TimestampStyle.SHORT_DATE_TIME.value
        else:
            _style = style if isinstance(style, str) else style.value

        return f"<t:{self._timestamp}:{_style}>"


@define()
class Partial:
    """
    Represents partial information to a resource from Discord.

    ---

    Sometimes, Discord will provide back to the client what is
    known as a "partial object." These objects are semantically
    categorised by their resource, but in cases do not carry
    the full set of information required for them. The `Partial`
    class lives to serve as a way to better typehint this incomplete
    data.
    """


@define(kw_only=True)
class Object:
    """
    Represents the base object form of a resource from Discord.

    Attributes
    ----------
    id : `Snowflake`
        The ID associated to the object.
    """

    id: str | Snowflake = field(converter=Snowflake)
    """The ID associated to the object."""
    _bot_inst: NotNeeded["Bot"] = field(default=MISSING)  # noqa F821
    """An instance of `Bot` used for helper methods."""


@define()
class Component:
    """
    Represents the base information of a component from Discord.

    ---

    `custom_id` is an attribute shared in every component,
    however, only `Button` makes them optional. A custom ID is
    a developer-defined ID in-between 1-100 characters.
    """

    custom_id: str = None
