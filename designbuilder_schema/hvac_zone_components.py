from pydantic import field_validator
from typing import List, Literal
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import Point3D
from designbuilder_schema.hvac_components import (
    NoTypeHVACComponent,
    HVACComponent,
    GenericHeatingCoil,
)


class ZoneElementList(BaseModel):
    HVACZoneComponent: List

    @field_validator("HVACZoneComponent", mode="before")
    def recast_components(cls, components):
        mapping = {
            "Zone extract": ZoneExtract,
            "Zone convective electric baseboard": ZoneConvectiveElectricBaseboard,
            "Zone ADU single duct CAV no reheat": ZoneADUSingleDuctCAVNoReheat,
            "Zone ADU single duct VAV reheat": ZoneADUSingleDuctVAVReheat,
        }
        return [
            mapping.get(component["@type"], HVACComponent)(**component)
            for component in components
        ]


class UnitElementList(BaseModel):
    HVACComponent: List

    @field_validator("HVACComponent", mode="before")
    def recast_components(cls, components):
        mapping = {
            "Zone ADU louvre": ZoneADULouvre,
            "Generic heating coil": GenericHeatingCoil,
        }
        return [
            mapping.get(component["@type"], HVACComponent)(**component)
            for component in components
        ]


class ZoneExtract(NoTypeHVACComponent):
    type: Literal["Zone extract"]
    Width: float
    Height: float
    Origin: "Point3D"
    ExtractGrille: "ExtractGrille"


class ZoneADUSingleDuctCAVNoReheat(NoTypeHVACComponent):
    type: Literal["Zone ADU single duct CAV no reheat"]
    Width: float
    Height: float
    MixingBoxWidth: float
    SupplyDiffuser: "SupplyDiffuser"
    UnitElementList: None


class ZoneADUSingleDuctVAVReheat(NoTypeHVACComponent):
    type: Literal["Zone ADU single duct VAV reheat"]
    Width: float
    Height: float
    MixingBoxWidth: float
    SupplyDiffuser: "SupplyDiffuser"
    UnitElementList: "UnitElementList"


class ZoneConvectiveElectricBaseboard(NoTypeHVACComponent):
    type: Literal["Zone convective electric baseboard"]


class ZoneADULouvre(NoTypeHVACComponent):
    type: Literal["Zone ADU louvre"]


class ExtractGrille(NoTypeHVACComponent):
    pass


class SupplyDiffuser(NoTypeHVACComponent):
    pass
