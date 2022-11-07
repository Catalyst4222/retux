import abc

__all__ = ("Sendable",)


class Sendable(abc.ABC):
    @abc.abstractmethod
    async def send(self, *everything, **else_):
        ...
