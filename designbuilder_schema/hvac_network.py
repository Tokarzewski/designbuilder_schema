"""
hvac_network.py
====================================
The hvac network module of the designbuilder_schema
"""

from pydantic import Field, field_validator
from typing import Union, List, Optional
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import *
from designbuilder_schema.id import ObjectIDs


class HVACNetwork(BaseModel):
    handle: int = Field(alias="ObjectHandle")
    ObjectIDs: "ObjectIDs"
    HVACLoops: "HVACLoops"
    HVACZoneGroups: "HVACZoneGroups"


class HVACLoops(BaseModel):
    HVACLoop: Union["HVACLoop", list["HVACLoop"]]


class HVACZoneGroups(BaseModel):
    HVACZoneGroup: Union["HVACZoneGroup", list["HVACZoneGroup"]]


class HVACLoop(BaseModel):
    currentSubLoopIndex: int = Field(alias="@currentSubLoopIndex")
    loopType: int = Field(alias="@loopType")
    plantLoopType: int = Field(alias="@plantLoopType")
    numberOfFlowNodes: int = Field(alias="@numberOfFlowNodes")
    ObjectIDs: "ObjectIDs"
    Origin: "Point3D"
    # PlantOperationSchemes: Union["PlantOperationSchemes", None]
    DemandSubLoop: "DemandSubLoop"
    SupplySubLoop: "SupplySubLoop"
    Attributes: "Attributes"


class Attributes(BaseModel):
    Attribute: Union["Attribute", list["Attribute"]]


class Attribute(BaseModel):
    name: str = Field(alias="@name", default=None)
    text: str = Field(alias="#text", default=None)


class ImageRectangle(BaseModel):
    ObjectIDs: "ObjectIDs"
    ImageTextureIndex: str
    MaskTextureIndex: str
    SelectedImageTextureIndex: str
    InactiveImageTextureIndex: str
    Textured: str
    Masked: str
    SelectedImage: str
    InactiveImage: str
    Color: str
    Active: str
    Vertices: "Vertices"
    Range: "Range"


class ZoneComponentAttributeList(BaseModel):
    HVACAttributeList: "HVACAttributeList"


class ZoneElementList(BaseModel):
    HVACZoneComponent: Union["HVACZoneComponent", list["HVACZoneComponent"]]


class BuildingZoneHandle(BaseModel):
    BuildingZoneHandle: str


class HVACAttributeList(BaseModel):
    buildingZoneHandle: str = Field(alias="@buildingZoneHandle")
    Attributes: "Attributes"


class PlantOperationSchemes(BaseModel):
    PlantOperationScheme: "PlantOperationScheme"


class PlantOperationScheme(BaseModel):
    PlantOperationRanges: "PlantOperationRanges"
    Attributes: "Attributes"


class PlantOperationRanges(BaseModel):
    PlantOperationRange: "PlantOperationRange"


class PlantOperationRange(BaseModel):
    Attributes: "Attributes"


class DemandSubLoop(BaseModel):
    LoopType: int
    PlantLoopType: int
    SubLoopType: int
    ObjectIDs: "ObjectIDs"
    HVACComponents: "HVACComponents"
    HVACConnections: "HVACConnections"
    Attributes: "Attributes"


class SupplySubLoop(BaseModel):
    LoopType: int
    PlantLoopType: int
    SubLoopType: int
    ObjectIDs: "ObjectIDs"
    HVACComponents: "HVACComponents"
    HVACConnections: "HVACConnections"
    Attributes: "Attributes"


HVACComponentEnum = Union[
    "HVACComponent",
    "SubLoopNode",
    "ZoneMixer",
    "SetpointManager",
    "AirHandlingUnit",
]


class HVACComponents(BaseModel):
    HVACComponent: List[HVACComponentEnum]

    @field_validator("HVACComponent", mode="before")
    def map_to_specific_class(cls, components):
        mapped_components = []
        for component in components:
            match component.get("@type"):
                case "Sub-loop node":
                    mapped_components.append(SubLoopNode(**component))
                case "Zone mixer":
                    mapped_components.append(ZoneSplitter(**component))
                case "Zone splitter":
                    mapped_components.append(ZoneMixer(**component))
                case "Splitter":
                    mapped_components.append(Splitter(**component))
                case "Mixer":
                    mapped_components.append(Mixer(**component))
                case "Setpoint manager":
                    mapped_components.append(SetpointManager(**component))
                case "Air handling unit":
                    mapped_components.append(AirHandlingUnit(**component))
                case _:
                    mapped_components.append(HVACComponent(**component))
        return mapped_components


class HVACComponent(BaseModel):
    type: str = Field(alias="@type")
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
    Attributes: "Attributes"
    ZoneComponentAttributeList: Union[None, "ZoneComponentAttributeList"]
    NumberOfFlowConnections: Optional[str] = None
    # Origin: "Point3D"


class HVACZoneComponent(HVACComponent):
    Width: float
    Height: float
    # ExtractGrille: "ExtractGrille"


class HVACZoneGroup(BaseModel):
    ImageRectangle: "ImageRectangle"
    ConnectingPlantLoopHandle: str
    ConnectingAirLoopHandle: str
    LoopType: str
    SubLoopType: str
    PlantLoopType: str
    AirLoopDuctType: str
    ComponentType: str
    Location: str
    ConnectionOffset: str
    Editable: str
    ZoneBranchFlag: str
    Orientation: str
    WaterInConnectionOrientation: str
    WaterOutConnectionOrientation: str
    AirInConnectionOrientation: str
    AirOutConnectionOrientation: str
    WaterInConnection: str
    WaterOutConnection: str
    AirInConnection: str
    AirOutConnection: str
    WaterInConnected: str
    WaterOutConnected: str
    AirInConnected: str
    AirOutConnected: str
    FanPlacement: str
    WaterInConnectionCoordinate: "Point3D"
    WaterOutConnectionCoordinate: "Point3D"
    AirInConnectionCoordinate: "Point3D"
    AirOutConnectionCoordinate: "Point3D"
    Attributes: "Attributes"
    ZoneComponentAttributeList: Union[None, "ZoneComponentAttributeList"]
    ValidZoneGroup: str
    Width: float
    Height: float
    Origin: "Point3D"
    BuildingZoneHandleList: "BuildingZoneHandle"
    ZoneElementList: "ZoneElementList"
    ZoneGroupAttributes: "Attribute"


class SubLoopNode(HVACComponent):
    NumberOfFlowConnections: str
    FlowConnections: "FlowConnections"
    HVACSubLoopNodeConnection: "HVACSubLoopNodeConnection"
    Origin: "Point3D"


class ZoneMixer(HVACComponent):
    LoopFlowDirection: str
    # HVACConnectorNode: "HVACConnectorNode"
    # BranchConnectionList


class ZoneSplitter(HVACComponent):
    LoopFlowDirection: str
    # HVACConnectorNode: "HVACConnectorNode"
    # BranchConnectionList


class Mixer(HVACComponent):
    LoopFlowDirection: str
    Origin: "Point3D"
    # HVACConnectorNode: "HVACConnectorNode"
    # BranchConnectionList


class Splitter(HVACComponent):
    LoopFlowDirection: str
    Origin: "Point3D"
    # HVACConnectorNode: "HVACConnectorNode"
    # BranchConnectionList


class SetpointManager(HVACComponent):
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
    """
    OutdoorAirSystem: "OutdoorAirSystem"
    IntakeDamper: "IntakeDamper"
    ExhaustDamper: "ExhaustDamper"
    DOASIntakeDamper: "DOASIntakeDamper"
    DOASExhaustDamper: "DOASExhaustDamper"
    MixingDamper: "MixingDamper"
    ExhaustUnitComponentList: "ExhaustUnitComponentList"
    IntakeUnitComponentList: "IntakeUnitComponentList"
    """
    LineArray: "LineArray"


class HVACConnections(BaseModel):
    HVACConnection: Union["HVACConnection", list["HVACConnection"]]


class HVACConnection(BaseModel):
    ObjectIDs: "ObjectIDs"
    LoopHandle: int
    SubLoopType: int
    LoopType: int
    PlantLoopType: int
    LoopFlowDirection: int
    ElementList: "ElementList"


class ElementList(BaseModel):
    HVACConnectionElement: Union["HVACConnectionElement", list["HVACConnectionElement"]]


class HVACConnectionElement(BaseModel):
    Line: "Line"
    SegmentList: "SegmentList"


class SegmentList(BaseModel):
    LineArray: "LineArray"


class LineArray(BaseModel):
    Line: Union["Line", list["Line"]]


class FlowConnections(BaseModel):
    HVACSubLoopNodeConnection: Union[
        "HVACSubLoopNodeConnection", list["HVACSubLoopNodeConnection"]
    ]


class HVACSubLoopNodeConnection(BaseModel):
    ObjectIDs: "ObjectIDs"
    Connected: str
    Coordinate: "Point3D"
    Attributes: "Attributes"
