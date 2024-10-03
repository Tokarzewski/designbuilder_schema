from designbuilder_schema.base import BaseModel as BaseModel

class ObjectIDs(BaseModel):
    handle: int
    buildingHandle: int
    buildingBlockHandle: int
    zoneHandle: int
    surfaceIndex: int
    openingIndex: int
