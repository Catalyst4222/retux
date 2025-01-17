from enum import IntEnum

from attrs import define

from .misc import Object
from .user import User


class StickerType(IntEnum):
    """
    Represents the types of stickers from Discord.

    Constants
    ---------
    STANDARD
        An official sticker of a pack.

        Only availible with Nitro unless
        part of a removed purchaseable pack.
    GUILD
        A sticker uploaded by a guild.
    """

    STANDARD = 1
    """
    An official sticker of a pack.

    Only availible with Nitro unless
    part of a removed purchaseable pack.
    """
    GUILD = 2
    """A sticker uploaded by a guild."""


class StickerFormatType(IntEnum):
    """
    Represents the types of sticker formats from Discord.

    Constants
    ---------
    PNG
        A sticker formatted with the `.png` format.
    APNG
        A sticker formatted with the `.apng` format.
    LOTTIE
        A sticker formatted with the `.lottie` format.
    """

    PNG = 1
    """A sticker formatted with the `.png` format."""
    APNG = 2
    """A sticker formatted with the `.apng` format."""
    LOTTIE = 3
    """A sticker formatted with the `.lottie` format."""


@define(kw_only=True)
class Sticker(Object):
    """
    Represents a sticker from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the sticker.
    pack_id : `int`, optional
        The ID of the pack containing the sticker.

        Only standard stickers owned by Discord
        can be part of a sticker pack.
    name : `str`
        The name of the sticker.
    description : `str`, optional
        The description of the sticker.
    tags : `str`
        The tags or emoji equivelent of a sticker.

        If the sticker is a standard sticker, this
        field will be a comma seperated list of
        keywords. If the sticker is guild owned, it
        will be the name of an emoji.
    asset : `str`
        An empty string previously for the sticker asset hash.
    type : `StickerType`
        The type of the sticker.
    format_type : `StickerFormatType`
        The formatting type that the sticker uses.
    available : `bool`, optinal
        Whether or not the sticker is availible.

        May be false if the guild that owns it
        has lost a level of boosting.
    guild_id : `int`, optional
        The ID of the guild that owns the sticker.

        Will only be set to None if the sticker is
        owned by Discord.
    user : `User`, optional
        The user that uploaded the sticker.

        Will only be set to None if the sticker is
        owned by Discord.
    sort_value : `int`, optional
        The sticker's order within its sticker pack.

        Will only be availible if the sticker is
        part of a pack and owned by Discord.
    """

    id: int
    """The ID of the sticker."""
    pack_id: int | None = None
    """
    The ID of the pack containing the sticker.

    Only standard stickers owned by Discord
    can be part of a sticker pack.
    """
    name: str
    """The name of the sticker."""
    description: str = None
    """The description of the sticker."""
    tags: str
    """
    The tags or emoji equivelent of a sticker.

    If the sticker is a standard sticker, this
    field will be a comma seperated list of
    keywords. If the sticker is guild owned, it
    will be the name of an emoji.
    """
    asset: str = ""
    """An empty string previously for the sticker asset hash."""
    type: StickerType
    """The type of the sticker."""
    format_type: StickerFormatType
    """The formatting type that the sticker uses."""
    available: bool = True
    """
    Whether or not the sticker is availible.

    May be false if the guild that owns it
    has lost a level of boosting.
    """
    guild_id: int | None = None
    """
    The ID of the guild that owns the sticker.

    Will only be set to None if the sticker is
    owned by Discord.
    """
    user: User = None
    """
    The user that uploaded the sticker.

    Will only be set to None if the sticker is
    owned by Discord.
    """
    sort_value: int | None = None
    """
    The sticker's order within its sticker pack.

    Will only be availible if the sticker is
    part of a pack and owned by Discord.
    """

    @property
    async def clean_tags(self):
        """
        A clean list of tags, formatted from the `tags` attribute.

        Only availible on standard stickers.
        """
        if self.type == StickerType.STANDARD:
            return self.tags.split(", ")


@define(kw_only=True)
class StickerItem(Object):
    """
    Represents the bare information needed
    to begin loading a sticker from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the sticker being represented.
    name : `str`
        The name of the sticker being represented.
    format_type : `StickerFormatType`
        The type of formatting of the sticker being represented.
    """

    id: int
    """The ID of the sticker being represented."""
    name: str
    """The name of the sticker being represented."""
    format_type: StickerFormatType
    """The type of formatting of the sticker being represented."""


@define(kw_only=True)
class StickerPack(Object):
    """
    Represents a sticker pack from Discord.

    Attributes
    ----------
    id : `int`
        The ID of the sticker pack.
    stickers : `list[Sticker]`
        The stickers within the sticker pack.
    name : `str
        The name of the sticker pack.
    sku_id : `int`
        The ID of the pack's SKU.
    cover_sticker_id : `int`, optional
        The ID of the sticker featured as the pack's icon.
    description : `str`
        The description of the sticker pack.
    banner_asset_id : `int`, optional
        The ID of the sticker packs's banner image.
    """

    id: int
    """The ID of the sticker pack."""
    stickers: list[Sticker]
    """The stickers within the sticker pack."""
    name: str
    """The name of the sticker pack."""
    sku_id: int
    """The ID of the pack's SKU."""
    cover_sticker_id: int | None = None
    """The ID of the sticker featured as the pack's icon."""
    description: str
    """The description of the sticker pack."""
    banner_asset_id: int | None = None
    """The ID of the sticker packs's banner image."""
