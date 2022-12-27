from typing import Callable

from attr import define

from .callback import Callback


@define(kw_only=True)
class Listener(Callback):
    name: str

    @classmethod
    def new(cls, name: str = None) -> Callable[[Callable], "Listener"]:
        def wrapper(func: Callable) -> "Listener":
            return cls(name=name if name is not None else func.__name__, callback=func)

        return wrapper
