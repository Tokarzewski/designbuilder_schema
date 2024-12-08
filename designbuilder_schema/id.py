from designbuilder_schema.base import BaseModel
#from pydantic import field_serializer

class ObjectIDs(BaseModel):
    handle: int
    buildingHandle: int
    buildingBlockHandle: int
    zoneHandle: int
    surfaceIndex: int
    openingIndex: int

#    @field_serializer
#    def ...