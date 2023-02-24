import inspect
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ..bot import Bot


class EventMeta(type):
    def __new__(cls, name: str, bases, dct, event_type=None):
        if event_type is None:
            event_type = dct.pop("event_type") if "event_type" in dct else name.lower()
        res = super(EventMeta, cls).__new__(cls, name, bases, dct)

        res.event_type = event_type

        return res


class Event(metaclass=EventMeta):
    @classmethod
    def _register_events(cls, bot: "Bot"):
        """Registers listeners from the event"""
        self = cls()
        event_types = ("create", "add", "update", "delete", "remove", "remove_all", "delete_bulk")

        for _, func in inspect.getmembers(self, predicate=inspect.ismethod):
            func: Callable

            if func.__name__ in event_types:
                # override the name
                name = f"{self.event_type}_{func.__name__}"
                bot._register(coro=func, name=name)

        return cls

    @classmethod
    def _remove_events(cls, bot: "Bot"):
        """Removes all listeners made from this event"""
        for listeners in bot._calls.values():
            for listener in listeners.copy():
                if owner := getattr(listener.callback, "__self__", None):
                    if isinstance(owner, cls):
                        listeners.remove(listener)
