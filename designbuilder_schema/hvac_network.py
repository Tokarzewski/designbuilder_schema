"""
hvac_network.py
====================================
The hvac network schema module of the designbuilder_schema project
"""

from pydantic import Field, field_validator
from typing import Union, List, Optional
from designbuilder_schema.base import BaseModel


class HVACNetwork(BaseModel):
    handle: str = Field(alias="ObjectHandle")
    ObjectIDs: "ObjectIDs"
    HVACLoops: "HVACLoops"
    HVACZoneGroups: "HVACZoneGroups"


class ObjectIDs(BaseModel):
    handle: str = Field(alias="@handle")
    buildingHandle: str = Field(alias="@buildingHandle")
    buildingBlockHandle: str = Field(alias="@buildingBlockHandle")
    zoneHandle: str = Field(alias="@zoneHandle")
    surfaceIndex: str = Field(alias="@surfaceIndex")
    openingIndex: str = Field(alias="@openingIndex")


class HVACLoops(BaseModel):
    HVACLoop: Union["HVACLoop", list["HVACLoop"]]


class HVACZoneGroups(BaseModel):
    HVACZoneGroup: Union["HVACZoneGroup", list["HVACZoneGroup"]]


class HVACLoop(BaseModel):
    currentSubLoopIndex: str = Field(alias="@currentSubLoopIndex")
    loopType: str = Field(alias="@loopType")
    plantLoopType: str = Field(alias="@plantLoopType")
    numberOfFlowNodes: str = Field(alias="@numberOfFlowNodes")
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


class Vertices(BaseModel):
    Point3D: list[str]


class Range(BaseModel):
    Org: "Point3D"
    End: "Point3D"


class Point3D(BaseModel):
    Point3D: str


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
    LoopType: str
    PlantLoopType: str
    SubLoopType: str
    ObjectIDs: "ObjectIDs"
    HVACComponents: "HVACComponents"
    HVACConnections: "HVACConnections"
    Attributes: "Attributes"


class SupplySubLoop(BaseModel):
    LoopType: str
    PlantLoopType: str
    SubLoopType: str
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
    NumberOfFlowConnections: Optional[str] = None
    # Origin: "Point3D"


class HVACZoneComponent(HVACComponent):
    Width: str
    Height: str
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
    Width: str
    Height: str
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
    Width: str
    Height: str
    FanType: str
    DOASAirInConnected: str
    DOASAirOutConnected: str
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
    LoopHandle: str
    SubLoopType: str
    LoopType: str
    PlantLoopType: str
    LoopFlowDirection: str
    ElementList: "ElementList"


class ElementList(BaseModel):
    HVACConnectionElement: Union["HVACConnectionElement", list["HVACConnectionElement"]]


class HVACConnectionElement(BaseModel):
    Line: "Line"
    SegmentList: "SegmentList"


class Line(BaseModel):
    ObjectIDs: "ObjectIDs"
    Begin: "Point3D"
    End: "Point3D"


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
