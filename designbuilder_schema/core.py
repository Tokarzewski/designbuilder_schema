"""
core.py
====================================
The core module of the designbuilder_schema
"""

from pydantic import Field
from typing import Union, Optional, List
from designbuilder_schema.hvac_network import HVACNetwork
from designbuilder_schema.base import BaseModel
from designbuilder_schema.geometry import *
from designbuilder_schema.tables import Tables
import datetime

class DBJSON(BaseModel):
    name: str
    date: datetime.date
    version: str
    objects: str
    Site: Optional["Site"]


class Site(BaseModel):
    handle: int
    count: int
    Attributes: "SiteAttributes"
    Tables: Optional["Tables"]
    AssemblyLibrary: Optional["AssemblyLibrary"]
    Buildings: Optional["Buildings"]


class SiteAttributes(BaseModel):
    """Site Attibutes Only"""

    Attribute: List["SiteAttribute"]


class Attributes(BaseModel):
    """Non-Site Attibutes"""

    Attribute: List["Attribute"]


class SiteAttribute(BaseModel):
    """Site Attibute Only"""

    name: str = None
    text: str = Field(alias="#text", default=None)


class Attribute(BaseModel):
    """Non-Site Attibute"""

    key: str = None
    text: str = Field(alias="#text", default=None)


class AssemblyLibrary(BaseModel):
    assemblyHandle: int
    Assembly: Union["Assembly", List["Assembly"]]


class Assembly(BaseModel):
    assemblyHandle: int
    componentBlockHandle: int
    reference: str
    HandlePoint: "Point3D"
    ComponentBlocks: "ComponentBlocks"
    Attributes: "Attributes"


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
    Attributes: Union["Attributes", "Attribute", None]

    @property
    def faces(self) -> List[List[float]]:
        """List of faces where, where each face is a list of x,y,z coordiantes."""
        vertices = [vertex.coords for vertex in self.Vertices]
        faces = []
        for surface in self.Surfaces.Surface:
            vertex_indices = surface.VertexIndices
            if (
                vertex_indices[-1] == ";"
            ):  # fix - if semicolon is last char then remove it
                vertex_indices = surface.VertexIndices[0:-1]

            indices = [int(x) for x in vertex_indices.split("; ")]
            face = [vertices[i] for i in indices]
            faces.append(face)

        return faces

    @property
    def openings(self) -> List[List[float]]:
        """List of openings where, where each opening is a list of x,y,z coordiantes."""
        opening_List = []

        for surface in self.Surfaces.Surface:
            if surface.Openings:
                openings = surface.Openings.Opening
                if isinstance(openings, List):
                    opening_List.extend(openings)
                else:
                    opening_List.append(openings)

        return [[vertex.coords for vertex in o.Polygon.Vertices] for o in opening_List]


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
    Attributes: Union["Attributes", "Attribute", None]


class Openings(BaseModel):
    Opening: Union[List["Opening"], "Opening"]


class Opening(BaseModel):
    type: str
    Polygon: "Polygon"
    Attributes: Optional["Attributes"]
    SegmentList: None


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
    BookmarkBuildings: "BookmarkBuildings"
    Attributes: "Attributes"

    def visualise():
        pass


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
    ProfileBody: "ProfileBody"
    Perimeter: "Perimeter"
    BaseProfileBody: "BaseProfileBody"
    Attributes: "Attributes"


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
    Polygon: "Polygon"
    InnerSurfaceBody: "InnerSurfaceBody"


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
    index: str
    Point3D: str


class LightSensorTwo(BaseModel):
    index: str
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
    # Attributes: "Attributes"


class AssemblyInstances(BaseModel):
    AssemblyInstance: Union["AssemblyInstance", List["AssemblyInstance"], None]


class AssemblyInstance(BaseModel):
    assemblyHandle: int
    reflected: int
    active: int
    ObjectIDs: "ObjectIDs"
    AssemblyInstanceTransformationMatrix: "AssemblyInstanceTransformationMatrix"
    Attributes: Optional["Attributes"]


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
