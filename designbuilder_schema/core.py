"""
core.py
====================================
The core schema module of the designbuilder_schema
"""

from pydantic import BaseModel, Field, StringConstraints
from typing import Union, List, Optional
from designbuilder_schema.hvac_network import HVACNetwork
from typing_extensions import Annotated


class DesignBuilderSchema(BaseModel):
    dbJSON: "DBJSON"


class DBJSON(BaseModel):
    name: str = Field(alias="@name")
    date: str = Field(alias="@date")
    version: str = Field(alias="@version")
    objects: str = Field(alias="@objects")
    Site: Union[None, "Site"]


class Site(BaseModel):
    handle: str = Field(alias="@handle")
    count: int = Field(alias="@count")
    Attributes: "SiteAttributes"
    Tables: "Tables"
    AssemblyLibrary: "AssemblyLibrary"
    Buildings: Union[None, "Buildings"]


class SiteAttributes(BaseModel):
    """Site Attibutes Only"""

    Attribute: list["SiteAttribute"]


class Attributes(BaseModel):
    """Non-Site Attibutes"""

    Attribute: list["Attribute"]


class SiteAttribute(BaseModel):
    """Site Attibute Only"""

    name: str = Field(alias="@name", default=None)
    text: str = Field(alias="#text", default=None)


class Attribute(BaseModel):
    """Non-Site Attibute"""

    key: str = Field(alias="@key", default=None)
    text: str = Field(alias="#text", default=None)


class Tables(BaseModel):
    Table: list["Table"]


class Table(BaseModel):
    name: str = Field(alias="@name")
    numberOfFields: str = Field(alias="@numberOfFields")
    Category: Union[str, list] = Field(default=None)
    FieldName: list


class AssemblyLibrary(BaseModel):
    assemblyHandle: str = Field(alias="@assemblyHandle")
    Assembly: list["Assembly"]


class Assembly(BaseModel):
    assemblyHandle: str = Field(alias="@assemblyHandle")
    componentBlockHandle: str = Field(alias="@componentBlockHandle")
    reference: str = Field(alias="@reference")
    HandlePoint: "Point3D"
    ComponentBlocks: "ComponentBlocks"
    Attributes: "Attributes"


class Point3D(BaseModel):
    Point3D: str


class Vertices(BaseModel):
    Point3D: list[str]


class ComponentBlocks(BaseModel):
    ComponentBlock: Union[list["ComponentBlock"], "ComponentBlock"]


class ComponentBlock(BaseModel):
    type: str = Field(alias="@type")
    Body: "Body"


class Body(BaseModel):
    volume: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(alias="@volume")
    extrusionHeight: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(alias="@extrusionHeight")
    ObjectIDs: "ObjectIDs"
    Vertices: "Vertices"
    Surfaces: "Surfaces"
    # VoidPerimeterList: "VoidPerimeterList"
    Attributes: Union["Attributes", "Attribute", None]


class ObjectIDs(BaseModel):
    handle: str = Field(alias="@handle")
    buildingHandle: str = Field(alias="@buildingHandle")
    buildingBlockHandle: str = Field(alias="@buildingBlockHandle")
    zoneHandle: str = Field(alias="@zoneHandle")
    surfaceIndex: str = Field(alias="@surfaceIndex")
    openingIndex: str = Field(alias="@openingIndex")


class Surfaces(BaseModel):
    Surface: list["Surface"]


class Surface(BaseModel):
    type: str = Field(alias="@type")
    area: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(alias="@area")
    alpha: str = Field(alias="@alpha")
    phi: str = Field(alias="@phi")
    defaultOpenings: str = Field(alias="@defaultOpenings")
    adjacentPartitionHandle: str = Field(alias="@adjacentPartitionHandle")
    thickness: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(alias="@thickness")
    ObjectIDs: "ObjectIDs"
    VertexIndices: str
    HoleIndices: Union[str, None]
    # Openings: Union["Openings", None]
    # Adjacencies: Union["Adjacencies", None]
    Attributes: Union["Attributes", "Attribute", None]


class Openings(BaseModel):
    Opening: Union["Opening", list["Opening"]]


class Opening(BaseModel):
    type: str = Field(alias="@type")
    Polygon: "Polygon"
    Attributes: "Attributes"
    SegmentList: None


class Buildings(BaseModel):
    numberOfBuildings: str = Field(alias="@numberOfBuildings")
    Building: Union["Building", List["Building"]]


class Building(BaseModel):
    currentComponentBlockHandle: str = Field(alias="@currentComponentBlockHandle")
    currentAssemblyInstanceHandle: str = Field(alias="@currentAssemblyInstanceHandle")
    currentPlaneHandle: str = Field(alias="@currentPlaneHandle")
    ObjectIDs: "ObjectIDs"
    BuildingBlocks: Union["BuildingBlocks", None]
    # ComponentBlocks: Union["ComponentBlocks", None]
    # AssemblyInstances: Union["AssemblyInstances", None]
    # ProfileOutlines: Union["ProfileOutlines", None] #OutlineBlocks
    # ConstructionLines: Union["ConstructionLines", None]
    # Planes: Union["Planes", None]
    HVACNetwork: Optional["HVACNetwork"]  # DetailedHVACNetwork...
    BookmarkBuildings: "BookmarkBuildings"
    Attributes: "Attributes"


class BuildingBlocks(BaseModel):
    BuildingBlock: "BuildingBlock"


class BuildingBlock(BaseModel):
    type: str = Field(alias="@type")
    height: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(alias="@height")
    roofSlope: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(alias="@roofSlope")
    roofOverlap: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(alias="@roofOverlap")
    roofType: str = Field(alias="@roofType")
    wallSlope: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(alias="@wallSlope")
    ObjectIDs: "ObjectIDs"
    ComponentBlocks: Union["ComponentBlocks", None]
    # CFDFans: Union["CFDFans", None]
    # AssemblyInstances: Union["AssemblyInstances", None]
    # ProfileOutlines: Union["ProfileOutlines", None]
    # InternalPartitions: Union["InternalPartitions", None]
    # VoidBodies: Union["VoidBodies", None]
    Zones: "Zones"
    ProfileBody: "ProfileBody"
    Perimeter: "Perimeter"
    BaseProfileBody: "BaseProfileBody"
    Attributes: "Attributes"


class Zones(BaseModel):
    Zone: "Zone"


class Zone(BaseModel):
    parentZoneHandle: str = Field(alias="@parentZoneHandle")
    inheritedZoneHandle: str = Field(alias="@inheritedZoneHandle")
    planExtrusion: str = Field(alias="@planExtrusion")
    innerSurfaceMode: str = Field(alias="@innerSurfaceMode")
    Body: "Body"
    LightSensorOne: "LightSensorOne"
    LightSensorTwo: "LightSensorTwo"
    LabelPosition: "Point3D"
    Polygon: "Polygon"
    InnerSurfaceBody: "InnerSurfaceBody"


class ProfileBody(BaseModel):
    elementSlope: str = Field(alias="@elementSlope")
    roofOverlap: str = Field(alias="@roofOverlap")
    Body: "Body"


class Perimeter(BaseModel):
    Polygon: "Polygon"


class BaseProfileBody(BaseModel):
    ProfileBody: "ProfileBody"


class Polygon(BaseModel):
    auxiliaryType: str = Field(alias="@auxiliaryType")
    ObjectIDs: "ObjectIDs"
    Vertices: Union["Vertices", None]
    # PolygonHoles: Union["PolygonHoles", None]


# class PolygonHoles(BaseModel):
#    X


class LightSensorOne(BaseModel):
    index: str = Field(alias="@index")
    Point3D: str


class LightSensorTwo(BaseModel):
    index: str = Field(alias="@index")
    Point3D: str


class InnerSurfaceBody(BaseModel):
    Body: "Body"


class BookmarkBuildings(BaseModel):
    numberOfBuildings: str = Field(alias="@numberOfBuildings")
