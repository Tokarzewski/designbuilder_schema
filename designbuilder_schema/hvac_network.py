"""
hvac_network.py
====================================
The hvac network module of the designbuilder_schema
"""

from pydantic import field_validator
from typing import Union, Optional
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import *
from designbuilder_schema.id import ObjectIDs
from designbuilder_schema.hvac_components import *
from designbuilder_schema.hvac_zone_components import *
from designbuilder_schema.attributes import *


class HVACNetwork(BaseModel):
    ObjectHandle: int
    ObjectIDs: "ObjectIDs"
    HVACLoops: "HVACLoops"
    HVACZoneGroups: "HVACZoneGroups"


class HVACLoops(BaseModel):
    HVACLoop: Union["HVACLoop", list["HVACLoop"]]


class HVACZoneGroups(BaseModel):
    HVACZoneGroup: Union["HVACZoneGroup", list["HVACZoneGroup"]]


class HVACLoop(BaseModel):
    currentSubLoopIndex: int
    loopType: int
    plantLoopType: int
    numberOfFlowNodes: int
    ObjectIDs: "ObjectIDs"
    Origin: "Point3D"
    PlantOperationSchemes: Optional["PlantOperationSchemes"]
    DemandSubLoop: "DemandSubLoop"
    SupplySubLoop: "SupplySubLoop"
    Attributes: "NameAttributes"


class ZoneElementList(BaseModel):
    HVACZoneComponent: list

    @field_validator("HVACZoneComponent", mode="before")
    def map_to_specific_class(cls, components):
        mapped_components = []
        for component in components:
            match component.get("@type"):
                case "Zone extract":
                    mapped_components.append(ZoneExtract(**component))
                # case "Zone mixer":
                #    mapped_components.append(ZoneMixer(**component))
                case _:
                    mapped_components.append(HVACZoneComponent(**component))
        return mapped_components


class BuildingZoneHandle(BaseModel):
    BuildingZoneHandle: Union[str, list[str]]


class PlantOperationSchemes(BaseModel):
    PlantOperationScheme: Union["PlantOperationScheme", list["PlantOperationScheme"]]


class PlantOperationScheme(BaseModel):
    PlantOperationRanges: Union["PlantOperationRanges", list["PlantOperationRanges"]]
    Attributes: "NameAttributes"


class PlantOperationRanges(BaseModel):
    PlantOperationRange: "PlantOperationRange"


class PlantOperationRange(BaseModel):
    Attributes: "NameAttributes"


class DemandSubLoop(BaseModel):
    LoopType: int
    PlantLoopType: int
    SubLoopType: int
    ObjectIDs: "ObjectIDs"
    HVACComponents: "HVACComponents"
    HVACConnections: "HVACConnections"
    Attributes: "NameAttributes"


class SupplySubLoop(BaseModel):
    LoopType: int
    PlantLoopType: int
    SubLoopType: int
    ObjectIDs: "ObjectIDs"
    HVACComponents: "HVACComponents"
    HVACConnections: "HVACConnections"
    Attributes: "NameAttributes"


class HVACComponents(BaseModel):
    HVACComponent: list

    @field_validator("HVACComponent", mode="before")
    def map_to_specific_class(cls, components):
        mapped_components = []
        for component in components:
            match component.get("@type"):
                case "Sub-loop node":
                    mapped_components.append(SubLoopNode(**component))
                case "Zone mixer":
                    mapped_components.append(ZoneMixer(**component))
                case "Zone splitter":
                    mapped_components.append(ZoneSplitter(**component))
                case "Splitter":
                    mapped_components.append(Splitter(**component))
                case "Mixer":
                    mapped_components.append(Mixer(**component))
                case "Setpoint manager":
                    mapped_components.append(SetpointManager(**component))
                case "Air handling unit":
                    mapped_components.append(AirHandlingUnit(**component))
                case "Pump":
                    mapped_components.append(Pump(**component))
                case "Boiler":
                    mapped_components.append(Boiler(**component))
                case "Cooling tower":
                    mapped_components.append(CoolingTower(**component))
                case "Chiller":
                    mapped_components.append(Chiller(**component))
                case _:
                    mapped_components.append(HVACComponent(**component))
        return mapped_components


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
    Attributes: "NameAttributes"
    ZoneComponentAttributeList: Optional["ZoneComponentAttributeList"]
    ValidZoneGroup: str
    Width: float
    Height: float
    Origin: "Point3D"
    BuildingZoneHandleList: Optional["BuildingZoneHandle"]
    ZoneElementList: "ZoneElementList"
    ZoneGroupAttributes: "NameAttribute"


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
