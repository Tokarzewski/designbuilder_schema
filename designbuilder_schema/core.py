"""
core.py
====================================
The core module of the designbuilder_schema
"""

from typing import Union, Optional, List, Any
from designbuilder_schema.hvac_network import HVACNetwork
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import *
from designbuilder_schema.tables import Tables
from designbuilder_schema.attributes import NameAttributes, KeyAttributes, KeyAttribute
import datetime


class DSBJSON(BaseModel):
    name: str
    date: datetime.date
    version: str
    objects: str
    Site: Optional["Site"]


class Site(BaseModel):
    handle: int
    count: int
    Attributes: "NameAttributes"
    Tables: Optional["Tables"]
    AssemblyLibrary: Optional["AssemblyLibrary"]
    Buildings: Optional["Buildings"]


class AssemblyLibrary(BaseModel):
    assemblyHandle: int
    Assembly: Union["Assembly", List["Assembly"]]


class Assembly(BaseModel):
    assemblyHandle: int
    componentBlockHandle: int
    reference: str
    HandlePoint: "Point3D"
    ComponentBlocks: "ComponentBlocks"
    Attributes: "KeyAttributes"


class ComponentBlocks(BaseModel):
    ComponentBlock: Union["ComponentBlock", List["ComponentBlock"]]


class ComponentBlock(BaseModel):
    type: str
    Body: "Body"


class Body(BaseModel):
    volume: float
    extrusionHeight: float
    ObjectIDs: "ObjectIDs"
    Vertices: "Vertices"
    Surfaces: "Surfaces"
    VoidPerimeterList: Optional["VoidPerimeterList"]
    Attributes: Union["KeyAttributes", "KeyAttribute", None]


class Surfaces(BaseModel):
    Surface: List["Surface"]


class Surface(BaseModel):
    type: str
    area: float
    alpha: float
    phi: float
    defaultOpenings: str
    adjacentPartitionHandle: int
    thickness: float
    ObjectIDs: "ObjectIDs"
    VertexIndices: str  # vertex indexes of parent body
    HoleIndices: Optional[str]
    Openings: Optional["Openings"]
    Adjacencies: Optional["Adjacencies"]
    Attributes: Union["KeyAttributes", "KeyAttribute", None]


class Openings(BaseModel):
    Opening: Union[List["Opening"], "Opening"]


class Opening(BaseModel):
    type: str
    Polygon: "Polygon"
    Attributes: Optional["KeyAttributes"]
    # SegmentList: Any


class Adjacencies(BaseModel):
    Adjacency: Union["Adjacency", List["Adjacency"]]


class Adjacency(BaseModel):
    type: str
    adjacencyDistance: float
    ObjectIDs: "ObjectIDs"
    AdjacencyPolygonList: "AdjacencyPolygonList"


class AdjacencyPolygonList(BaseModel):
    Polygon: Union["Polygon", List["Polygon"]]


class Buildings(BaseModel):
    numberOfBuildings: int
    Building: Union["Building", List["Building"]]


class Building(BaseModel):
    currentComponentBlockHandle: int
    currentAssemblyInstanceHandle: int
    currentPlaneHandle: int
    ObjectIDs: "ObjectIDs"
    BuildingBlocks: Optional["BuildingBlocks"]
    ComponentBlocks: Optional["ComponentBlocks"]
    AssemblyInstances: Optional["AssemblyInstances"]
    ProfileOutlines: Optional["ProfileOutlines"]  # OutlineBlocks
    ConstructionLines: Optional["ConstructionLines"]
    Planes: Optional["Planes"]
    HVACNetwork: Optional["HVACNetwork"]
    BookmarkBuildings: Optional["BookmarkBuildings"]
    Attributes: "KeyAttributes"


class BuildingBlocks(BaseModel):
    BuildingBlock: Union["BuildingBlock", List["BuildingBlock"]]


class BuildingBlock(BaseModel):
    type: str
    height: float
    roofSlope: float
    roofOverlap: float
    roofType: str
    wallSlope: float
    ObjectIDs: "ObjectIDs"
    ComponentBlocks: Optional["ComponentBlocks"]
    CFDFans: Optional["CFDFans"]
    AssemblyInstances: Optional["AssemblyInstances"]
    ProfileOutlines: Optional["ProfileOutlines"]
    InternalPartitions: Optional["InternalPartitions"]
    VoidBodies: Optional["VoidBodies"]
    Zones: "Zones"
    ProfileBody: Optional["ProfileBody"]
    Perimeter: Optional["Perimeter"]
    BaseProfileBody: Optional["BaseProfileBody"]
    Attributes: "KeyAttributes"


class InternalPartitions(BaseModel):
    InternalPartition: Union["InternalPartition", List["InternalPartition"]]


class InternalPartition(BaseModel):
    type: str
    height: float
    area: float
    floatingPartition: bool
    ObjectIDs: "ObjectIDs"
    StartPoint: "Point3D"
    EndPoint: "Point3D"


class Zones(BaseModel):
    Zone: Union["Zone", List["Zone"]]


class Zone(BaseModel):
    parentZoneHandle: str
    inheritedZoneHandle: str
    planExtrusion: str
    innerSurfaceMode: str
    Body: "Body"
    LightSensorOne: "LightSensorOne"
    LightSensorTwo: "LightSensorTwo"
    LabelPosition: "Point3D"
    Polygon: Optional["Polygon"]
    InnerSurfaceBody: Optional["InnerSurfaceBody"]


class ProfileBody(BaseModel):
    elementSlope: float
    roofOverlap: float
    Body: "Body"


class Perimeter(BaseModel):
    Polygon: "Polygon"


class BaseProfileBody(BaseModel):
    ProfileBody: "ProfileBody"


class Polygon(BaseModel):
    auxiliaryType: str
    ObjectIDs: "ObjectIDs"
    Vertices: Optional["Vertices"]
    PolygonHoles: Optional["PolygonHoles"]


class PolygonHoles(BaseModel):
    PolygonHole: Union["PolygonHole", List["PolygonHole"]]


class PolygonHole(BaseModel):
    ObjectIDs: "ObjectIDs"
    Vertices: "Vertices"


class LightSensorOne(BaseModel):
    index: int
    Point3D: str


class LightSensorTwo(BaseModel):
    index: int
    Point3D: str


class InnerSurfaceBody(BaseModel):
    Body: "Body"


class BookmarkBuildings(BaseModel):
    numberOfBuildings: int


class ConstructionLines(BaseModel):
    ConstructionLine: Union["ConstructionLine", List["ConstructionLine"], None]


class ConstructionLine(BaseModel):
    Line: "Line"
    Planes: "CPlanes"


class CPlanes(BaseModel):
    Polygon: Union["Polygon", List["Polygon"]]


class Planes(BaseModel):
    Plane: Union["Plane", List["Plane"]]


class Plane(BaseModel):
    type: int
    Polygon: "Polygon"
    # Attributes: "KeyAttributes"


class AssemblyInstances(BaseModel):
    AssemblyInstance: Union["AssemblyInstance", List["AssemblyInstance"], None]


class AssemblyInstance(BaseModel):
    assemblyHandle: int
    reflected: int
    active: int
    ObjectIDs: "ObjectIDs"
    AssemblyInstanceTransformationMatrix: "AssemblyInstanceTransformationMatrix"
    Attributes: Optional["KeyAttributes"]


class AssemblyInstanceTransformationMatrix(BaseModel):
    Matrix: "Matrix"


class Matrix(BaseModel):
    MatrixRow: List[str]


class ProfileOutlines(BaseModel):
    ProfileOutline: Union["ProfileOutline", List["ProfileOutline"], None]


class ProfileOutline(BaseModel):
    Body: "Body"


class VoidBodies(BaseModel):
    VoidBody: Union["VoidBody", List["VoidBody"]]


class VoidBody(BaseModel):
    ProfileBody: "ProfileBody"


class VoidPerimeterList(BaseModel):
    Polygon: Union["Polygon", List["Polygon"]]


class CFDFans(BaseModel):
    CFDFan: Union["CFDFan", List["CFDFan"]]


class CFDFan(BaseModel):
    ComponentBlock: "ComponentBlock"
