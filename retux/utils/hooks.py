from attr import fields
from cattrs import Converter, global_converter
from cattrs.gen import make_dict_structure_fn

from ..client.resources.misc import Object, Timestamp

__all__ = "cattrs_structure_hooks"


def _pos_arg(data, type):
    return type(data)


def store_extras(converter: Converter = global_converter):
    r"""
    A function that creates a structure factory when called with an optional converter
    The factory adds any extra attributes not present in the original fields into the class's `_extras` field.
    """

    def make_structer(cls):
        default_structure = make_dict_structure_fn(cls, converter)
        names: set[str] = {field.name for field in fields(cls)}

        def structure(data: dict[str, ...], _):
            _extras = {key: data[key] for key in (data.keys() - names)}
            # data["extras"] = _extras
            res = default_structure(data, _)
            res._extras = _extras
            return res

        return structure

    return make_structer


def cattrs_structure_hooks(converter: Converter = global_converter):
    """
    Hooks retux objects into the cattrs converter.
    Can be used to hook objects into a user made
    converter as well.

    Parameters
    ----------
    converter : `Converter`, optional
        The converter to hook into, defaults to the
        global cattrs converter.
    """
    # reg(Snowflake, _pos_arg)
    converter.register_structure_hook(Timestamp, _pos_arg)

    converter.register_structure_hook_factory(
        lambda cls: issubclass(cls, Object), store_extras(converter)
    )
