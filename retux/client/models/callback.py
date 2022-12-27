from typing import Callable, Any

from attr import define, field


@define(kw_only=True)
class Callback:
    callback: Callable
    _obj: Any = field(default=None, init=False)  # set later as needed

    def __call__(self, *args, **kwargs):
        if self._obj is not None:
            return self.callback(self._obj, *args, **kwargs)
        return self.callback(*args, **kwargs)
