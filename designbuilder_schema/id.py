from designbuilder_schema.base import BaseModel
from pydantic import Field


_counter = 0


def current_handle() -> int:
    return _counter


def generate_handle() -> int:
    global _counter
    _counter += 1
    return _counter - 1


def set_counter(value: int) -> None:
    global _counter
    _counter = value


class ObjectIDs(BaseModel):
    """
    RULES:
    1. All defined handles must be unique integers
    2. undefined handle is -1
    3. Site handle is always the max current handle
    4. each ObjectID is given new handle on creation
    """

    handle: int = Field(default_factory=generate_handle)
    buildingHandle: int = -1
    buildingBlockHandle: int = -1
    zoneHandle: int = -1
    surfaceIndex: int = -1
    openingIndex: int = -1

    # make sure that all ObjectIDs instances have:
    # 1. update parent handles with @field_serialize
