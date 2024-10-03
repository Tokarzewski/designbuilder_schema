from designbuilder_schema.geometry import *
from designbuilder_schema.base import BaseModel as BaseModel
from designbuilder_schema.hvac_network import HVACNetwork as HVACNetwork
from designbuilder_schema.tables import Tables as Tables

class DesignBuilderSchema(BaseModel):
    dbJSON: DBJSON

class DBJSON(BaseModel):
    name: str
    date: str
    version: str
    objects: str
    Site: Site | None

class Site(BaseModel):
    handle: int
    count: int
    Attributes: SiteAttributes
    Tables: Tables
    AssemblyLibrary: AssemblyLibrary
    Buildings: Buildings | None

class SiteAttributes(BaseModel):
    Attribute: list['SiteAttribute']

class Attributes(BaseModel):
    Attribute: list['Attribute']

class SiteAttribute(BaseModel):
    name: str
    text: str

class Attribute(BaseModel):
    key: str
    text: str

class AssemblyLibrary(BaseModel):
    assemblyHandle: int
    Assembly: Assembly | list['Assembly']

class Assembly(BaseModel):
    assemblyHandle: int
    componentBlockHandle: int
    reference: str
    HandlePoint: Point3D
    ComponentBlocks: ComponentBlocks
    Attributes: Attributes

class ComponentBlocks(BaseModel):
    ComponentBlock: ComponentBlock | list['ComponentBlock']

class ComponentBlock(BaseModel):
    type: str
    Body: Body

class Body(BaseModel):
    volume: float
    extrusionHeight: float
    ObjectIDs: ObjectIDs
    Vertices: Vertices
    Surfaces: Surfaces
    VoidPerimeterList: VoidPerimeterList | None
    Attributes: Attributes | Attribute | None

class Surfaces(BaseModel):
    Surface: list['Surface']

class Surface(BaseModel):
    type: str
    area: float
    alpha: float
    phi: float
    defaultOpenings: str
    adjacentPartitionHandle: int
    thickness: float
    ObjectIDs: ObjectIDs
    VertexIndices: str
    HoleIndices: str | None
    Openings: Openings | None
    Adjacencies: Adjacencies | None
    Attributes: Attributes | Attribute | None

class Openings(BaseModel):
    Opening: Opening | list['Opening'] | None

class Opening(BaseModel):
    type: str
    Polygon: Polygon
    Attributes: Attributes | None
    SegmentList: None

class Adjacencies(BaseModel):
    Adjacency: Adjacency | list['Adjacency']

class Adjacency(BaseModel):
    type: str
    adjacencyDistance: float
    ObjectIDs: ObjectIDs
    AdjacencyPolygonList: AdjacencyPolygonList

class AdjacencyPolygonList(BaseModel):
    Polygon: Polygon

class Buildings(BaseModel):
    numberOfBuildings: int
    Building: Building | list['Building']

class Building(BaseModel):
    currentComponentBlockHandle: int
    currentAssemblyInstanceHandle: int
    currentPlaneHandle: int
    ObjectIDs: ObjectIDs
    BuildingBlocks: BuildingBlocks | None
    ComponentBlocks: ComponentBlocks | None
    AssemblyInstances: AssemblyInstances | None
    ProfileOutlines: ProfileOutlines | None
    ConstructionLines: ConstructionLines | None
    Planes: Planes | None
    HVACNetwork: HVACNetwork | None
    BookmarkBuildings: BookmarkBuildings
    Attributes: Attributes

class BuildingBlocks(BaseModel):
    BuildingBlock: BuildingBlock | list['BuildingBlock']

class BuildingBlock(BaseModel):
    type: str
    height: float
    roofSlope: float
    roofOverlap: float
    roofType: str
    wallSlope: float
    ObjectIDs: ObjectIDs
    ComponentBlocks: ComponentBlocks | None
    CFDFans: CFDFans | None
    AssemblyInstances: AssemblyInstances | None
    ProfileOutlines: ProfileOutlines | None
    InternalPartitions: InternalPartitions | None
    VoidBodies: VoidBodies | None
    Zones: Zones
    ProfileBody: ProfileBody
    Perimeter: Perimeter
    BaseProfileBody: BaseProfileBody
    Attributes: Attributes

class InternalPartitions(BaseModel):
    InternalPartition: InternalPartition | list['InternalPartition']

class InternalPartition(BaseModel):
    type: str
    height: float
    area: float
    floatingPartition: bool
    ObjectIDs: ObjectIDs
    StartPoint: Point3D
    EndPoint: Point3D

class Zones(BaseModel):
    Zone: Zone | list['Zone']

class Zone(BaseModel):
    parentZoneHandle: str
    inheritedZoneHandle: str
    planExtrusion: str
    innerSurfaceMode: str
    Body: Body
    LightSensorOne: LightSensorOne
    LightSensorTwo: LightSensorTwo
    LabelPosition: Point3D
    Polygon: Polygon
    InnerSurfaceBody: InnerSurfaceBody

class ProfileBody(BaseModel):
    elementSlope: float
    roofOverlap: float
    Body: Body

class Perimeter(BaseModel):
    Polygon: Polygon

class BaseProfileBody(BaseModel):
    ProfileBody: ProfileBody

class Polygon(BaseModel):
    auxiliaryType: str
    ObjectIDs: ObjectIDs
    Vertices: Vertices | None
    PolygonHoles: PolygonHoles | None

class PolygonHoles(BaseModel):
    PolygonHole: PolygonHole | list['PolygonHole']

class PolygonHole(BaseModel):
    ObjectIDs: ObjectIDs
    Vertices: Vertices

class LightSensorOne(BaseModel):
    index: str
    Point3D: str

class LightSensorTwo(BaseModel):
    index: str
    Point3D: str

class InnerSurfaceBody(BaseModel):
    Body: Body

class BookmarkBuildings(BaseModel):
    numberOfBuildings: int

class ConstructionLines(BaseModel):
    ConstructionLine: ConstructionLine | list['ConstructionLine'] | None

class ConstructionLine(BaseModel):
    Line: Line
    Planes: CPlanes

class CPlanes(BaseModel):
    Polygon: Polygon | list['Polygon']

class Planes(BaseModel):
    Plane: Plane | list['Plane']

class Plane(BaseModel):
    type: int
    Polygon: Polygon
    Attributes: Attributes

class AssemblyInstances(BaseModel):
    AssemblyInstance: AssemblyInstance | list['AssemblyInstance'] | None

class AssemblyInstance(BaseModel):
    assemblyHandle: int
    reflected: int
    active: int
    ObjectIDs: ObjectIDs
    AssemblyInstanceTransformationMatrix: AssemblyInstanceTransformationMatrix
    Attributes: Attributes | None

class AssemblyInstanceTransformationMatrix(BaseModel):
    Matrix: Matrix

class Matrix(BaseModel):
    MatrixRow: list[str]

class ProfileOutlines(BaseModel):
    ProfileOutline: ProfileOutline | list['ProfileOutline'] | None

class ProfileOutline(BaseModel):
    Body: Body

class VoidBodies(BaseModel):
    VoidBody: VoidBody | list['VoidBody']

class VoidBody(BaseModel):
    ProfileBody: ProfileBody

class VoidPerimeterList(BaseModel):
    Polygon: Polygon | list['Polygon']

class CFDFans(BaseModel):
    CFDFan: CFDFan | list['CFDFan']

class CFDFan(BaseModel):
    ComponentBlock: ComponentBlock
