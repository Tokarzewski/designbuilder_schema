from pydantic import field_validator
from typing import List
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import Point3D
from designbuilder_schema.hvac_components import (
    NoTypeHVACComponent,
    HVACComponent,
    GenericHeatingCoil,
)


class ZoneExtract(HVACComponent):
    Width: float
    Height: float
    Origin: "Point3D"
    ExtractGrille: "ExtractGrille"


class ZoneADUSingleDuctCAVNoReheat(HVACComponent):
    Width: float
    Height: float
    MixingBoxWidth: float
    SupplyDiffuser: "SupplyDiffuser"
    UnitElementList: None


class ZoneADUSingleDuctVAVReheat(HVACComponent):
    Width: float
    Height: float
    MixingBoxWidth: float
    SupplyDiffuser: "SupplyDiffuser"
    UnitElementList: "UnitElementList"


class ExtractGrille(NoTypeHVACComponent):
    pass


class SupplyDiffuser(NoTypeHVACComponent):
    pass


class ZoneConvectiveElectricBaseboard(HVACComponent):
    pass


class ZoneADULouvre(HVACComponent):
    pass


class UnitElementList(BaseModel):
    HVACComponent: List

    @field_validator("HVACComponent", mode="before")
    def recast_components(cls, components):
        recasted = []
        for component in components:
            match component.get("@type"):
                case "Zone ADU louvre":
                    recasted.append(ZoneADULouvre(**component))
                case "Generic heating coil":
                    recasted.append(GenericHeatingCoil(**component))
                case _:
                    recasted.append(HVACComponent(**component))
        return recasted
