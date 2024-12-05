from pydantic import Field, field_validator
from typing import Union, Optional
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import *
from designbuilder_schema.attributes import NameAttributes, ZoneComponentAttributeList


class HVACZoneComponent(BaseModel):
    type: str
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
    Attributes: "NameAttributes"
    ZoneComponentAttributeList: "ZoneComponentAttributeList"
    # Width: float
    # Height: float
    # ExtractGrille: "ExtractGrille"
    # Origin: "Origin"
    # MixingBoxWidth: float
    # SupplyDiffuser: "SupplyDiffuser"
    # UnitElementList: "UnitElementList"
    # OutdoorAirSupply: int
    # IntakeLouvre: "IntakeLouvre"
    # MixingBox: "MixingBox"
    # RefrigerantConnected: int


class ZoneExtract(BaseModel):
    pass
