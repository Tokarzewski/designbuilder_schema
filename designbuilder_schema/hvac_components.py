from typing import Union, Optional
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import *
from designbuilder_schema.attributes import NameAttributes, ZoneComponentAttributeList


class NoTypeHVACComponent(BaseModel):
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


class HVACComponent(NoTypeHVACComponent):
    type: str


class SubLoopNode(HVACComponent):
    NumberOfFlowConnections: int
    FlowConnections: "FlowConnections"
    HVACSubLoopNodeConnection: "HVACSubLoopNodeConnection"
    Origin: "Point3D"


class ZoneMixer(HVACComponent):
    LoopFlowDirection: int
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class ZoneSplitter(HVACComponent):
    LoopFlowDirection: int
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class Mixer(HVACComponent):
    LoopFlowDirection: int
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class Splitter(HVACComponent):
    LoopFlowDirection: int
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
    ExhaustUnitComponentList: Optional["ExhaustUnitComponentList"]
    IntakeUnitComponentList: "IntakeUnitComponentList"
    LineArray: "LineArray"


class Pump(HVACComponent): ...


class Boiler(HVACComponent): ...


class CoolingTower(HVACComponent): ...


class Chiller(HVACComponent):
    WaterCooledCondenser: "WaterCooledCondenser"
    ChillerHRHeatExchanger: "ChillerHRHeatExchanger"
    AbsorptionChillerUnit: "AbsorptionChillerUnit"


class WaterCooledCondenser(NoTypeHVACComponent):
    pass


class ChillerHRHeatExchanger(NoTypeHVACComponent):
    pass


class AbsorptionChillerUnit(NoTypeHVACComponent):
    AbsorptionChillerGeneratorHeatExchanger: "AbsorptionChillerGeneratorHeatExchanger"


class AbsorptionChillerGeneratorHeatExchanger(NoTypeHVACComponent):
    pass


class FlowConnections(BaseModel):
    HVACSubLoopNodeConnection: Union[
        "HVACSubLoopNodeConnection", list["HVACSubLoopNodeConnection"]
    ]


class ExhaustUnitComponentList(BaseModel):
    AirHandlingUnitHVACComponent: Union[
        "AirHandlingUnitHVACComponent", list["AirHandlingUnitHVACComponent"]
    ]


class IntakeUnitComponentList(BaseModel):
    AirHandlingUnitHVACComponent: Union[
        "AirHandlingUnitHVACComponent", list["AirHandlingUnitHVACComponent"]
    ]


class HVACConnectorNode(BaseModel):
    ObjectIDs: "ObjectIDs"
    Name: str
    Active: int


class BranchConnectionList(BaseModel):
    HVACConnectorNode: list["HVACConnectorNode"]


class HVACSubLoopNodeConnection(BaseModel):
    ObjectIDs: "ObjectIDs"
    Connected: int
    Coordinate: "Point3D"
    Attributes: "NameAttributes"


class OutdoorAirSystem(NoTypeHVACComponent):
    HeatRecovery: int
    Recirculation: int
    HeatRecoveryDevice: "HeatRecoveryDevice"
    # OutdoorAirSystemComponentList:


class IntakeDamper(NoTypeHVACComponent):
    pass


class ExhaustDamper(NoTypeHVACComponent):
    pass


class DOASIntakeDamper(NoTypeHVACComponent):
    pass


class DOASExhaustDamper(NoTypeHVACComponent):
    pass


class MixingDamper(NoTypeHVACComponent):
    pass


class HeatRecoveryDevice(NoTypeHVACComponent):
    pass


class AirHandlingUnitHVACComponent(HVACComponent):
    pass
