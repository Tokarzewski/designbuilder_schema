from pydantic import Field, field_validator
from typing import Union, Optional
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import *
from designbuilder_schema.attributes import NameAttributes, ZoneComponentAttributeList


class HVACComponent(BaseModel):
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
    ZoneComponentAttributeList: Optional["ZoneComponentAttributeList"]


class SubLoopNode(HVACComponent):
    NumberOfFlowConnections: int
    FlowConnections: "FlowConnections"
    HVACSubLoopNodeConnection: "HVACSubLoopNodeConnection"
    Origin: "Point3D"


class ZoneMixer(HVACComponent):
    LoopFlowDirection: str
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class ZoneSplitter(HVACComponent):
    LoopFlowDirection: str
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class Mixer(HVACComponent):
    LoopFlowDirection: str
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class Splitter(HVACComponent):
    LoopFlowDirection: str
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class SetpointManager(HVACComponent):
    Origin: "Point3D"
    ControlPoint: "Point3D"
    UpStreamNode: "Point3D"
    DownStreamNode: "Point3D"
    SegmentList: "SegmentList"


class AirHandlingUnit(HVACComponent):
    Width: float
    Height: float
    FanType: int
    DOASAirInConnected: int
    DOASAirOutConnected: int
    Origin: "Point3D"
    OutdoorAirSystem: "OutdoorAirSystem"
    IntakeDamper: "IntakeDamper"
    ExhaustDamper: "ExhaustDamper"
    DOASIntakeDamper: "DOASIntakeDamper"
    DOASExhaustDamper: "DOASExhaustDamper"
    MixingDamper: "MixingDamper"
    # ExhaustUnitComponentList: "ExhaustUnitComponentList"
    # IntakeUnitComponentList: "IntakeUnitComponentList"
    LineArray: "LineArray"


class Pump(HVACComponent):
    pass


class Boiler(HVACComponent):
    pass


class CoolingTower(HVACComponent):
    pass


class Chiller(HVACComponent):
    WaterCooledCondenser: "WaterCooledCondenser"
    ChillerHRHeatExchanger: "ChillerHRHeatExchanger"
    AbsorptionChillerUnit: "AbsorptionChillerUnit"


class WaterCooledCondenser(BaseModel):
    ImageRectangle: "ImageRectangle"
    ComponentType: int
    ConnectingPlantLoopHandle: int
    WaterInConnectionOrientation: int
    WaterOutConnectionOrientation: int
    WaterInConnectionCoordinate: "Point3D"
    WaterOutConnectionCoordinate: "Point3D"
    Attributes: "NameAttributes"


class ChillerHRHeatExchanger(BaseModel):
    ImageRectangle: "ImageRectangle"
    ComponentType: int
    WaterInConnectionOrientation: int
    WaterOutConnectionOrientation: int
    WaterInConnectionCoordinate: "Point3D"
    WaterOutConnectionCoordinate: "Point3D"


class AbsorptionChillerUnit(BaseModel):
    ImageRectangle: "ImageRectangle"
    ComponentType: int
    # AbsorptionChillerGeneratorHeatExchanger: "AbsorptionChillerGeneratorHeatExchanger"


class FlowConnections(BaseModel):
    HVACSubLoopNodeConnection: Union[
        "HVACSubLoopNodeConnection", list["HVACSubLoopNodeConnection"]
    ]


class HVACSubLoopNodeConnection(BaseModel):
    ObjectIDs: "ObjectIDs"
    Connected: int
    Coordinate: "Point3D"
    Attributes: "NameAttributes"


class OutdoorAirSystem(BaseModel):
    HeatRecovery: int
    Recirculation: int
    ImageRectangle: "ImageRectangle"
    Attributes: "NameAttributes"
    HeatRecoveryDevice: "HeatRecoveryDevice"
    # OutdoorAirSystemComponentList:


class IntakeDamper(BaseModel):
    ImageRectangle: "ImageRectangle"


class ExhaustDamper(BaseModel):
    ImageRectangle: "ImageRectangle"


class DOASIntakeDamper(BaseModel):
    ImageRectangle: "ImageRectangle"


class DOASExhaustDamper(BaseModel):
    ImageRectangle: "ImageRectangle"


class MixingDamper(BaseModel):
    ImageRectangle: "ImageRectangle"


class ExhaustUnitComponentList(BaseModel):
    AirHandlingUnitHVACComponent: Union[
        "AirHandlingUnitHVACComponent", list["AirHandlingUnitHVACComponent"]
    ]


class IntakeUnitComponentList(BaseModel):
    AirHandlingUnitHVACComponent: Union[
        "AirHandlingUnitHVACComponent", list["AirHandlingUnitHVACComponent"]
    ]


class HeatRecoveryDevice(BaseModel):
    ImageRectangle: "ImageRectangle"


class AirHandlingUnitHVACComponent(BaseModel):
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
    ZoneComponentAttributeList: Optional["ZoneComponentAttributeList"]


class HVACConnectorNode(BaseModel):
    ObjectIDs: "ObjectIDs"
    Name: str
    Active: int


class BranchConnectionList(BaseModel):
    HVACConnectorNode: list["HVACConnectorNode"]
