from ..api.http import _Route, _RouteMethod

from attrs import asdict

__all__ = ("Respondable", "Controllable", "Editable")


class Editable:
    """
    A mixin for objects with edit/delete methods.

    Methods
    -------
    `edit()` : `dict`
        Edits an object with the given path and kwargs.
    `modify()` : `dict`
        An alias of the `edit()` method.
    `delete()` : `dict | None`
        Delete an object from discord.
    """

    async def edit(self, bot: "Bot", path: str, **kwargs) -> dict:  # noqa
        """
        Edits an object with the given path and kwargs.

        Parameters
        -----------
        bot : `retux.Bot`
            The instance of the bot.
        path : `str`
            The path to the endpoint of the Discord API.
        **kwargs : `dict`
            The data to edit.

        Returns
        -------
        `dict`
            The data returned from Discord.
        """

        route = _Route(method=_RouteMethod.PATCH, path=path)
        payload = {}
        for key, value in kwargs.items():
            if hasattr(value, "__slots__"):
                payload[key] = asdict(
                    value, filter=lambda _name, _value: _name.name not in {"_bot", "bot"}
                )
            else:
                payload[key] = value

        return await bot.http.request(route, payload)

    async def modify(self, bot: "Bot", path: str, **kwargs) -> dict:  # noqa
        """An alias of the `edit()` method."""
        return await self.edit(bot, path, **kwargs)

    async def delete(self, bot: "Bot", path: str) -> None | dict:  # noqa
        """
        Delete an object from discord.

        Parameters
        ----------
        bot : `retux.Bot`
            The instance of the bot.
        path : `str`
            The path to the endpoint of the Discord API.

        Returns
        -------
        `dict | None`
            The data given from Discord, if any.
        """
        route = _Route(method=_RouteMethod.DELETE, path=path)
        return await bot.http.request(route)


class Respondable(Editable):
    """
    A mixin for objects with send/edit/delete methods.

    Methods
    -------
    respond() : `dict`
        Executes a `respond` action to Discord with the given path and keyword arguments.
    send() : `dict`
        An alias of the `respond()` method.
    """

    async def respond(self, bot: "Bot", path: str, **kwargs) -> dict:  # noqa
        """
        Executes a `respond` action to Discord with the given path and keyword arguments.

        Parameters
        ----------
        bot : `retux.Bot`
            The instance of the bot.
        path : `str`
            The path to the endpoint of the Discord API.
        **kwargs : `dict`
            The data to include in the request.

        Returns
        -------
        `dict`
            The data of the interaction response returned by Discord.
        """

        route = _Route(method=_RouteMethod.POST, path=path)

        payload = {}
        for key, value in kwargs.items():
            if hasattr(value, "__slots__"):
                payload[key] = asdict(
                    value, filter=lambda _name, _value: _name.name not in {"_bot", "bot"}
                )
            else:
                payload[key] = value

        return await bot.http.request(route, payload)

    async def send(self, bot: "Bot", path: str, **kwargs) -> dict:  # noqa
        """An alias of the `respond()` method."""
        return await self.respond(bot, path, **kwargs)


class Controllable:
    """
    A mixin for objects with create/get methods.

    Methods
    -------
    `create()` : `dict`
        Creates an object with the given path and kwargs.
    `get()` : `dict`
        Gets an object from the Discord API.
    """

    @classmethod
    async def create(cls, bot: "Bot", path: str, **kwargs) -> dict:  # noqa
        """
        Creates an object with the given path and kwargs.

        Parameters
        ----------
        bot : `retux.Bot`
            The instance of the bot.
        path : `str`
            The path to the endpoint of the Discord API.
        **kwargs : `dict`
            The data for the object creation.

        Returns
        -------
        `dict`
            The data of the object returned by Discord.
        """
        route = _Route(method=_RouteMethod.POST, path=path)

        payload = {}
        for key, value in kwargs.items():
            if hasattr(value, "__slots__"):
                payload[key] = asdict(
                    value, filter=lambda _name, _value: _name.name not in {"_bot", "bot"}
                )
            else:
                payload[key] = value

        return await bot.http.request(route, payload)

    @classmethod
    async def get(cls, bot: "Bot", path: str, **query_params: dict | None) -> dict:  # noqa
        """
        Gets an object from the Discord API.

        Parameters
        ----------
        bot : `retux.Bot`
            The instance of the bot.
        path : `str`
            The path to the endpoint of the Discord API.
        **query_params : `dict`, optional
            The data to query for when getting. For example `with_counts=True` for guilds.

        Returns
        -------
        `dict`
            The data of the object returned by Discord.
        """
        route = _Route(method=_RouteMethod.GET, path=path)
        return await bot.http.request(route, payload=query_params)
