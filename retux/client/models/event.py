import inspect
from typing import Callable


class EventMeta(type):
    def __new__(cls, name: str, bases, dct, event_type=None):
        if event_type is None:
            event_type = dct.pop("event_type") if "event_type" in dct else name.lower()
        res = super(EventMeta, cls).__new__(cls, name, bases, dct)

        res.event_type = event_type

        return res


class Event(metaclass=EventMeta):
    def __init__(self):
        ...

    @classmethod
    def _register_events(cls, bot):
        self = cls()
        event_types = ("create", "add", "update", "delete", "remove", "remove_all", "delete_bulk")
        print(self.event_type)

        for _, func in inspect.getmembers(self, predicate=inspect.ismethod):
            func: Callable

            if func.__name__ in event_types:
                # override the name
                name = f"{self.event_type}_{func.__name__}"
                print(func)
                bot._register(coro=func, name=name)

        return self
