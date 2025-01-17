from base64 import b64encode
from datetime import datetime
from enum import Enum
from io import IOBase
from typing import Any

from attr import field
from attrs import define

from ...const import MISSING, NotNeeded

__all__ = (
    "ImageData",
    "Component",
    "CDNEndpoint",
    "Image",
    "TimestampStyle",
    "Timestamp",
    "Partial",
    "Object",
)


@define(repr=False)
class ImageData:
    """
    Represents an image object from Discord.

    This is not supposed for uploading files to messages, because those have to be uploaded to Discord's CDN, what uses
    a different method. Images are directly stored on Discord's backend and used in, for example, guild icons or
    banners.

    Attributes
    ----------
    file : `str`
        The name of the file, or path to the file if no `fp` is specified.
    fp : `io.IoBase`, optional
        The data of the file to be uploaded, either as bytes or io-object.

    Methods
    -------
    data : `str`
        The URI of the image.
    name : `str`
        The name of the image.
    type : `str`
        The type of the image.
    """

    def __repr__(self) -> str:
        return self.data

    file: str
    """The name of the file, or path to the file if no `fp` is specified."""
    fp: IOBase | bytes = MISSING
    """The data of the file to be uploaded, either as bytes or io-object."""
    _data: str = None
    """The finalised and encrypted data that is sent to discord. Do not utilise as user."""

    def __attrs_post_init__(self):

        if self.type not in {
            "jpeg",
            "png",
            "gif",
        }:
            raise ValueError("File type must be one of jpeg, png or gif!")

        if self.fp is not MISSING:
            self.__data = (
                b64encode(self.fp).decode("utf-8")
                if isinstance(self.fp, bytes)
                else b64encode(self.fp.read()).decode("utf-8")
            )
        else:
            with open(self.file, "rb") as file:
                self.__data = b64encode(file.read()).decode("utf-8")

    @property
    def data(self) -> str:
        """
        Returns the base64-encoded data-URI of the Image object.
        """
        return f"data:image/{self.type};base64,{self._data}"

    @property
    def name(self) -> str:
        """
        Returns the name of the image.
        """
        return self._name.split("/")[-1].split(".")[0]

    @property
    def type(self) -> str:
        return self.file.split(".")[-1]


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

    @staticmethod
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
    id : `int`
        The ID associated to the object.
    """

    id: int
    """The ID associated to the object."""
    _bot_inst: NotNeeded["Bot"] = MISSING  # noqa F821
    """An instance of `Bot` used for helper methods."""
    _extras: dict[str, Any] = field(init=False, factory=dict)
    """A dictionary of extra data sent from discord"""

    def __getattr__(self, item):
        try:
            return self._extras[item]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{item}'") from None


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
