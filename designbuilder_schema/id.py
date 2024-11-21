from designbuilder_schema.base import BaseModel
from pydantic import Field


class ObjectIDs(BaseModel):
    handle: int
    buildingHandle: int
    buildingBlockHandle: int
    zoneHandle: int
    surfaceIndex: int
    openingIndex: int
