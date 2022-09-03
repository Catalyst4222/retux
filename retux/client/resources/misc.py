from ...const import MISSING
from io import IOBase
from base64 import b64encode
from attrs import define


__all__ = ("ImageData",)


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
                b64encode(self.fp.read()).decode("utf-8")
                if not isinstance(self.fp, bytes)
                else b64encode(self.fp).decode("utf-8")
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
