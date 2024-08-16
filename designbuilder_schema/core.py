"""
core.py
====================================
The core schema module of the designbuilder_schema
"""

from pydantic import Field
from typing import Union, Optional
from designbuilder_schema.hvac_network import HVACNetwork
from designbuilder_schema.base import BaseModel


class DesignBuilderSchema(BaseModel):
    dbJSON: "DBJSON"


class DBJSON(BaseModel):
    name: str = Field(alias="@name")
    date: str = Field(alias="@date")
    version: str = Field(alias="@version")
    objects: str = Field(alias="@objects")
    Site: Union[None, "Site"]


class Site(BaseModel):
    handle: int = Field(alias="@handle")
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
    numberOfFields: int = Field(alias="@numberOfFields")
    Category: Union[str, list, None] = Field(default=None)
    FieldName: list[str]


class AssemblyLibrary(BaseModel):
    assemblyHandle: int = Field(alias="@assemblyHandle")
    Assembly: Union["Assembly", list["Assembly"]]


class Assembly(BaseModel):
    assemblyHandle: int = Field(alias="@assemblyHandle")
    componentBlockHandle: int = Field(alias="@componentBlockHandle")
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
    volume: float = Field(alias="@volume")
    extrusionHeight: float = Field(alias="@extrusionHeight")
    ObjectIDs: "ObjectIDs"
    Vertices: "Vertices"
    Surfaces: "Surfaces"
    # VoidPerimeterList: Union["VoidPerimeterList", None]
    Attributes: Union["Attributes", "Attribute", None]


class ObjectIDs(BaseModel):
    handle: int = Field(alias="@handle")
    buildingHandle: int = Field(alias="@buildingHandle")
    buildingBlockHandle: int = Field(alias="@buildingBlockHandle")
    zoneHandle: int = Field(alias="@zoneHandle")
    surfaceIndex: int = Field(alias="@surfaceIndex")
    openingIndex: int = Field(alias="@openingIndex")


class Surfaces(BaseModel):
    Surface: list["Surface"]


class Surface(BaseModel):
    type: str = Field(alias="@type")
    area: float = Field(alias="@area")
    alpha: float = Field(alias="@alpha")
    phi: float = Field(alias="@phi")
    defaultOpenings: str = Field(alias="@defaultOpenings")
    adjacentPartitionHandle: int = Field(alias="@adjacentPartitionHandle")
    thickness: float = Field(alias="@thickness")
    ObjectIDs: "ObjectIDs"
    VertexIndices: str
    HoleIndices: Union[str, None]
    Openings: Union["Openings", None]
    Adjacencies: Union["Adjacencies", None]
    Attributes: Union["Attributes", "Attribute", None]


class Openings(BaseModel):
    Opening: Union["Opening", list["Opening"], None]


class Opening(BaseModel):
    type: str = Field(alias="@type")
    Polygon: "Polygon"
    Attributes: Union["Attributes", None]
    SegmentList: None


class Adjacencies(BaseModel):
    Adjacency: Union["Adjacency", list["Adjacency"]]


class Adjacency(BaseModel):
    type: str = Field(alias="@type")
    adjacencyDistance: float = Field(alias="@adjacencyDistance")
    ObjectIDs: "ObjectIDs"
    AdjacencyPolygonList: "AdjacencyPolygonList"


class AdjacencyPolygonList(BaseModel):
    Polygon: Union["Polygon"]


class Buildings(BaseModel):
    numberOfBuildings: int = Field(alias="@numberOfBuildings")
    Building: Union["Building", list["Building"]]


class Building(BaseModel):
    currentComponentBlockHandle: int = Field(alias="@currentComponentBlockHandle")
    currentAssemblyInstanceHandle: int = Field(alias="@currentAssemblyInstanceHandle")
    currentPlaneHandle: int = Field(alias="@currentPlaneHandle")
    ObjectIDs: "ObjectIDs"
    BuildingBlocks: Union["BuildingBlocks", None]
    ComponentBlocks: Union["ComponentBlocks", None]
    AssemblyInstances: Union["AssemblyInstances", None]
    ProfileOutlines: Union["ProfileOutlines", None]  # OutlineBlocks
    ConstructionLines: Union["ConstructionLines", None]
    Planes: Union["Planes", None]
    HVACNetwork: Optional["HVACNetwork"]  # DetailedHVACNetwork...
    BookmarkBuildings: "BookmarkBuildings"
    Attributes: "Attributes"


class BuildingBlocks(BaseModel):
    BuildingBlock: "BuildingBlock"


class BuildingBlock(BaseModel):
    type: str = Field(alias="@type")
    height: float = Field(alias="@height")
    roofSlope: float = Field(alias="@roofSlope")
    roofOverlap: float = Field(alias="@roofOverlap")
    roofType: str = Field(alias="@roofType")
    wallSlope: float = Field(alias="@wallSlope")
    ObjectIDs: "ObjectIDs"
    ComponentBlocks: Union["ComponentBlocks", None]
    # CFDFans: Union["CFDFans", None]
    AssemblyInstances: Union["AssemblyInstances", None]
    ProfileOutlines: Union["ProfileOutlines", None]
    InternalPartitions: Union["InternalPartitions", None]
    # VoidBodies: Union["VoidBodies", None]
    Zones: "Zones"
    ProfileBody: "ProfileBody"
    Perimeter: "Perimeter"
    BaseProfileBody: "BaseProfileBody"
    Attributes: "Attributes"


class InternalPartitions(BaseModel):
    InternalPartition: Union["InternalPartition", list["InternalPartition"]]


class InternalPartition(BaseModel):
    type: str = Field(alias="@type")
    height: float = Field(alias="@height")
    area: float = Field(alias="@area")
    floatingPartition: bool = Field(alias="@floatingPartition")
    ObjectIDs: "ObjectIDs"
    StartPoint: "Point3D"
    EndPoint: "Point3D"


class Zones(BaseModel):
    Zone: Union["Zone", list["Zone"]]


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
    numberOfBuildings: int = Field(alias="@numberOfBuildings")


class ConstructionLines(BaseModel):
    ConstructionLine: Union["ConstructionLine", list["ConstructionLine"], None]


class ConstructionLine(BaseModel):
    Line: "Line3D"
    Planes: "CPlanes"


class Line3D(BaseModel):
    ObjectIDs: "ObjectIDs"
    Begin: "Point3D"
    End: "Point3D"


class CPlanes(BaseModel):
    Polygon: Union["Polygon", list["Polygon"]]


class Planes(BaseModel):
    Plane: Union["Plane", list["Plane"]]


class Plane(BaseModel):
    type: int = Field(alias="@type")
    Polygon: "Polygon"
    Attributes: "Attributes"


class AssemblyInstances(BaseModel):
    AssemblyInstance: Union["AssemblyInstance", list["AssemblyInstance"], None]


class AssemblyInstance(BaseModel):
    assemblyHandle: int = Field(alias="@assemblyHandle")
    reflected: int = Field(alias="@reflected")
    active: int = Field(alias="@active")
    ObjectIDs: "ObjectIDs"
    AssemblyInstanceTransformationMatrix: "AssemblyInstanceTransformationMatrix"
    Attributes: Union["Attributes", None]


class AssemblyInstanceTransformationMatrix(BaseModel):
    Matrix: "Matrix"


class Matrix(BaseModel):
    MatrixRow: list[str]


class ProfileOutlines(BaseModel):
    ProfileOutline: Union["ProfileOutline", list["ProfileOutline"], None]


class ProfileOutline(BaseModel):
    Body: "Body"
