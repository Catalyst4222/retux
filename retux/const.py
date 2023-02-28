from typing import TypeVar, Union, Awaitable, Callable

__all__ = (
    "__version__",
    "__api_version__",
    "__api_url__",
    "__gateway_url__",
    "__repo_url__",
    "MISSING",
    "NotNeeded",
    "Coro",
)


__version__ = "0.0.3"
__api_version__ = "v10"
__api_url__ = f"https://discord.com/api/{__api_version__}"
__gateway_url__ = "wss://gateway.discord.gg/"
__repo_url__ = "https://github.com/i0bs/retux"


class MISSING:
    """
    A sentinel that represents an argument with a "missing" value.
    This is used deliberately to avoid `None` space confusion.
    """

    pass


_T = TypeVar("_T")
NotNeeded = Union[_T, MISSING]
"""
A type variable to work alongside `MISSING`. This should only
be used to help further indicate an optional argument where it
already points to said type.
"""

Coro = Callable[..., Awaitable[_T]]
"""
A type variable to replace long typehint definitions.
`Coroutine` is not what people usually call coroutines, it's what's returned by calling an `async def` function
"""
