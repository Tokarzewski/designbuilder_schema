"""
hvac_network.py
====================================
The hvac network module of the designbuilder_schema
"""

from pydantic import field_validator
from typing import Union, Optional, List
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import Line, SegmentList
from designbuilder_schema.id import ObjectIDs
from designbuilder_schema.hvac_components import *
from designbuilder_schema.hvac_zone_components import *
from designbuilder_schema.attributes import NameAttribute, NameAttributes


class HVACNetwork(BaseModel):
    ObjectHandle: int
    ObjectIDs: "ObjectIDs"
    HVACLoops: "HVACLoops"
    HVACZoneGroups: "HVACZoneGroups"


class HVACLoops(BaseModel):
    HVACLoop: Union["HVACLoop", List["HVACLoop"]]


class HVACZoneGroups(BaseModel):
    HVACZoneGroup: Union["HVACZoneGroup", List["HVACZoneGroup"]]


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


class HVACZoneGroup(NoTypeHVACComponent):
    ValidZoneGroup: str
    Width: float
    Height: float
    Origin: "Point3D"
    BuildingZoneHandleList: Optional["BuildingZoneHandle"]
    ZoneElementList: "ZoneElementList"
    ZoneGroupAttributes: "NameAttribute"


class BuildingZoneHandle(BaseModel):
    BuildingZoneHandle: Union[str, list[str]]


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


class HVACComponents(BaseModel):
    HVACComponent: List

    @field_validator("HVACComponent", mode="before")
    def recast_components(cls, components):
        recasted = []
        for component in components:
            match component.get("@type"):
                case "Sub-loop node":
                    recasted.append(SubLoopNode(**component))
                case "Zone mixer":
                    recasted.append(ZoneMixer(**component))
                case "Zone splitter":
                    recasted.append(ZoneSplitter(**component))
                case "Splitter":
                    recasted.append(Splitter(**component))
                case "Mixer":
                    recasted.append(Mixer(**component))
                case "Setpoint manager":
                    recasted.append(SetpointManager(**component))
                case "Air handling unit":
                    recasted.append(AirHandlingUnit(**component))
                case "Pump":
                    recasted.append(Pump(**component))
                case "Boiler":
                    recasted.append(Boiler(**component))
                case "Cooling tower":
                    recasted.append(CoolingTower(**component))
                case "Chiller":
                    recasted.append(Chiller(**component))
                case "Generic heating coil":
                    recasted.append(GenericHeatingCoil(**component))
                case _:
                    recasted.append(HVACComponent(**component))
        return recasted


class ZoneElementList(BaseModel):
    HVACZoneComponent: List

    @field_validator("HVACZoneComponent", mode="before")
    def recast_components(cls, components):
        recasted = []
        for component in components:
            match component.get("@type"):
                case "Zone extract":
                    recasted.append(ZoneExtract(**component))
                case "Zone convective electric baseboard":
                    recasted.append(ZoneConvectiveElectricBaseboard(**component))
                case "Zone ADU single duct CAV no reheat":
                    recasted.append(ZoneADUSingleDuctCAVNoReheat(**component))
                case "Zone ADU single duct VAV reheat":
                    recasted.append(ZoneADUSingleDuctVAVReheat(**component))
                case _:
                    recasted.append(HVACComponent(**component))
        return recasted
