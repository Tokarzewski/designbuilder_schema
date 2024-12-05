from typing import Optional
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import *
from designbuilder_schema.attributes import NameAttribute, ZoneComponentAttributeList


class NoTypeHVACZoneComponent(BaseModel):
    ImageRectangle: "ImageRectangle"
    ConnectingPlantLoopHandle: int
    ConnectingAirLoopHandle: int
    LoopType: int
    SubLoopType: int
    PlantLoopType: int
    AirLoopDuctType: int
    ComponentType: int
    Location: int
    ConnectionOffset: float
    Editable: int
    ZoneBranchFlag: int
    Orientation: int
    WaterInConnectionOrientation: int
    WaterOutConnectionOrientation: int
    AirInConnectionOrientation: int
    AirOutConnectionOrientation: int
    WaterInConnection: int
    WaterOutConnection: int
    AirInConnection: int
    AirOutConnection: int
    WaterInConnected: int
    WaterOutConnected: int
    AirInConnected: int
    AirOutConnected: int
    FanPlacement: int
    WaterInConnectionCoordinate: "Point3D"
    WaterOutConnectionCoordinate: "Point3D"
    AirInConnectionCoordinate: "Point3D"
    AirOutConnectionCoordinate: "Point3D"
    Attributes: Optional["NameAttribute"]
    ZoneComponentAttributeList: Optional["ZoneComponentAttributeList"]


class HVACZoneComponent(NoTypeHVACZoneComponent):
    type: str


class ZoneExtract(HVACZoneComponent):
    Width: float
    Height: float
    Origin: "Point3D"
    ExtractGrille: "ExtractGrille"


class ExtractGrille(NoTypeHVACZoneComponent):
    pass


class ZoneADUSingleDuctCAVNoReheat(HVACZoneComponent):
    Width: float
    Height: float
    MixingBoxWidth: float
    SupplyDiffuser: "SupplyDiffuser"
    # UnitElementList


class SupplyDiffuser(NoTypeHVACZoneComponent):
    pass


class ZoneConvectiveElectricBaseboard(HVACZoneComponent):
    pass
