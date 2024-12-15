from pydantic import field_validator, Field
from typing import Union, Optional, Literal, List, Annotated
from designbuilder_schema.base import BaseModel
from designbuilder_schema.id import ObjectIDs
from designbuilder_schema.attributes import NameAttributes, ZoneComponentAttributeList
from designbuilder_schema.geometry import (
    Point3D,
    ImageRectangle,
    LineArray,
    SegmentList,
)


class HVACComponents(BaseModel):
    HVACComponent: List

    @field_validator("HVACComponent", mode="before")
    def recast_components(cls, components):
        mapping = {
            "Sub-loop node": SubLoopNode,
            "Zone mixer": ZoneMixer,
            "Zone splitter": ZoneSplitter,
            "Splitter": Splitter,
            "Mixer": Mixer,
            "Setpoint manager": SetpointManager,
            "Air handling unit": AirHandlingUnit,
            "Pump": Pump,
            "Boiler": Boiler,
            "Cooling tower": CoolingTower,
            "Chiller": Chiller,
            "Generic heating coil": GenericHeatingCoil,
        }
        return [
            mapping.get(component["@type"], HVACComponent)(**component)
            for component in components
        ]


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
    Attributes: Optional["NameAttributes"]
    ZoneComponentAttributeList: Optional["ZoneComponentAttributeList"]


class HVACComponent(NoTypeHVACComponent):
    type: str


class SubLoopNode(NoTypeHVACComponent):
    type: Literal["Sub-loop node"]
    NumberOfFlowConnections: int
    FlowConnections: "FlowConnections"
    HVACSubLoopNodeConnection: "HVACSubLoopNodeConnection"
    Origin: "Point3D"


class ZoneMixer(NoTypeHVACComponent):
    type: Literal["Zone mixer"]
    LoopFlowDirection: int
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class ZoneSplitter(NoTypeHVACComponent):
    type: Literal["Zone splitter"]
    LoopFlowDirection: int
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class Splitter(NoTypeHVACComponent):
    type: Literal["Splitter"]
    LoopFlowDirection: int
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class Mixer(NoTypeHVACComponent):
    type: Literal["Mixer"]
    LoopFlowDirection: int
    Origin: "Point3D"
    HVACConnectorNode: "HVACConnectorNode"
    BranchConnectionList: "BranchConnectionList"


class SetpointManager(NoTypeHVACComponent):
    type: Literal["Setpoint manager"]
    Origin: "Point3D"
    ControlPoint: "Point3D"
    UpStreamNode: "Point3D"
    DownStreamNode: "Point3D"
    SegmentList: "SegmentList"


class AirHandlingUnit(NoTypeHVACComponent):
    type: Literal["Air handling unit"]
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


class Pump(NoTypeHVACComponent):
    type: Literal["Pump"]
    ...


class Boiler(NoTypeHVACComponent):
    type: Literal["Boiler"]
    ...


class CoolingTower(NoTypeHVACComponent):
    type: Literal["Cooling tower"]
    ...


class Chiller(NoTypeHVACComponent):
    type: Literal["Chiller"]
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
    ObjectIDs: Annotated["ObjectIDs", Field(default_factory=ObjectIDs)]
    Name: str
    Active: int


class BranchConnectionList(BaseModel):
    HVACConnectorNode: list["HVACConnectorNode"]


class HVACSubLoopNodeConnection(BaseModel):
    ObjectIDs: Annotated["ObjectIDs", Field(default_factory=ObjectIDs)]
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


class GenericHeatingCoil(NoTypeHVACComponent):
    type: Literal["Generic heating coil"]
