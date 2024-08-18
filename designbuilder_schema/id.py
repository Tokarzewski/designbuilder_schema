from designbuilder_schema.base import BaseModel
from pydantic import Field


class ObjectIDs(BaseModel):
    handle: int = Field(alias="@handle")
    buildingHandle: int = Field(alias="@buildingHandle")
    buildingBlockHandle: int = Field(alias="@buildingBlockHandle")
    zoneHandle: int = Field(alias="@zoneHandle")
    surfaceIndex: int = Field(alias="@surfaceIndex")
    openingIndex: int = Field(alias="@openingIndex")
