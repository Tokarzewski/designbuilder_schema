from designbuilder_schema.geometry import *
from designbuilder_schema.base import BaseModel as BaseModel
from designbuilder_schema.id import ObjectIDs as ObjectIDs

class HVACNetwork(BaseModel):
    handle: int
    ObjectIDs: ObjectIDs
    HVACLoops: HVACLoops
    HVACZoneGroups: HVACZoneGroups

class HVACLoops(BaseModel):
    HVACLoop: HVACLoop | list['HVACLoop']

class HVACZoneGroups(BaseModel):
    HVACZoneGroup: HVACZoneGroup | list['HVACZoneGroup']

class HVACLoop(BaseModel):
    currentSubLoopIndex: int
    loopType: int
    plantLoopType: int
    numberOfFlowNodes: int
    ObjectIDs: ObjectIDs
    Origin: Point3D
    PlantOperationSchemes: PlantOperationSchemes | None
    DemandSubLoop: DemandSubLoop
    SupplySubLoop: SupplySubLoop
    Attributes: Attributes

class Attributes(BaseModel):
    Attribute: Attribute | list['Attribute']

class Attribute(BaseModel):
    name: str
    text: str

class ImageRectangle(BaseModel):
    ObjectIDs: ObjectIDs
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
    Vertices: Vertices
    Range: Range

class ZoneComponentAttributeList(BaseModel):
    HVACAttributeList: HVACAttributeList

class ZoneElementList(BaseModel):
    HVACZoneComponent: HVACZoneComponent | list['HVACZoneComponent']

class BuildingZoneHandle(BaseModel):
    BuildingZoneHandle: str

class HVACAttributeList(BaseModel):
    buildingZoneHandle: str
    Attributes: Attributes

class PlantOperationSchemes(BaseModel):
    PlantOperationScheme: PlantOperationScheme | list['PlantOperationScheme']

class PlantOperationScheme(BaseModel):
    PlantOperationRanges: PlantOperationRanges | list['PlantOperationRanges']
    Attributes: Attributes

class PlantOperationRanges(BaseModel):
    PlantOperationRange: PlantOperationRange

class PlantOperationRange(BaseModel):
    Attributes: Attributes

class DemandSubLoop(BaseModel):
    LoopType: int
    PlantLoopType: int
    SubLoopType: int
    ObjectIDs: ObjectIDs
    HVACComponents: HVACComponents
    HVACConnections: HVACConnections
    Attributes: Attributes

class SupplySubLoop(BaseModel):
    LoopType: int
    PlantLoopType: int
    SubLoopType: int
    ObjectIDs: ObjectIDs
    HVACComponents: HVACComponents
    HVACConnections: HVACConnections
    Attributes: Attributes

class HVACComponents(BaseModel):
    HVACComponent: list
    def map_to_specific_class(cls, components): ...

class HVACComponent(BaseModel):
    type: str
    ImageRectangle: ImageRectangle
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
    WaterInConnectionCoordinate: Point3D
    WaterOutConnectionCoordinate: Point3D
    AirInConnectionCoordinate: Point3D
    AirOutConnectionCoordinate: Point3D
    Attributes: Attributes
    ZoneComponentAttributeList: None | ZoneComponentAttributeList

class HVACZoneComponent(HVACComponent):
    Width: float
    Height: float

class HVACZoneGroup(BaseModel):
    ImageRectangle: ImageRectangle
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
    WaterInConnectionCoordinate: Point3D
    WaterOutConnectionCoordinate: Point3D
    AirInConnectionCoordinate: Point3D
    AirOutConnectionCoordinate: Point3D
    Attributes: Attributes
    ZoneComponentAttributeList: None | ZoneComponentAttributeList
    ValidZoneGroup: str
    Width: float
    Height: float
    Origin: Point3D
    BuildingZoneHandleList: None | BuildingZoneHandle
    ZoneElementList: ZoneElementList
    ZoneGroupAttributes: Attribute

class SubLoopNode(HVACComponent):
    NumberOfFlowConnections: int
    FlowConnections: FlowConnections
    HVACSubLoopNodeConnection: HVACSubLoopNodeConnection
    Origin: Point3D

class ZoneMixer(HVACComponent):
    LoopFlowDirection: str
    Origin: Point3D
    HVACConnectorNode: HVACConnectorNode
    BranchConnectionList: BranchConnectionList

class ZoneSplitter(HVACComponent):
    LoopFlowDirection: str
    Origin: Point3D
    HVACConnectorNode: HVACConnectorNode
    BranchConnectionList: BranchConnectionList

class Mixer(HVACComponent):
    LoopFlowDirection: str
    Origin: Point3D
    HVACConnectorNode: HVACConnectorNode
    BranchConnectionList: BranchConnectionList

class Splitter(HVACComponent):
    LoopFlowDirection: str
    Origin: Point3D
    HVACConnectorNode: HVACConnectorNode
    BranchConnectionList: BranchConnectionList

class SetpointManager(HVACComponent):
    Origin: Point3D
    ControlPoint: Point3D
    UpStreamNode: Point3D
    DownStreamNode: Point3D
    SegmentList: SegmentList

class AirHandlingUnit(HVACComponent):
    Width: float
    Height: float
    FanType: int
    DOASAirInConnected: int
    DOASAirOutConnected: int
    Origin: Point3D
    OutdoorAirSystem: OutdoorAirSystem
    IntakeDamper: IntakeDamper
    ExhaustDamper: ExhaustDamper
    DOASIntakeDamper: DOASIntakeDamper
    DOASExhaustDamper: DOASExhaustDamper
    MixingDamper: MixingDamper
    ExhaustUnitComponentList: ExhaustUnitComponentList
    IntakeUnitComponentList: IntakeUnitComponentList
    LineArray: LineArray

class Pump(HVACComponent): ...
class Boiler(HVACComponent): ...
class CoolingTower(HVACComponent): ...

class Chiller(HVACComponent):
    WaterCooledCondenser: WaterCooledCondenser
    ChillerHRHeatExchanger: ChillerHRHeatExchanger
    AbsorptionChillerUnit: AbsorptionChillerUnit

class WaterCooledCondenser(BaseModel):
    ImageRectangle: ImageRectangle
    ComponentType: int
    ConnectingPlantLoopHandle: int
    WaterInConnectionOrientation: int
    WaterOutConnectionOrientation: int
    WaterInConnectionCoordinate: Point3D
    WaterOutConnectionCoordinate: Point3D

class ChillerHRHeatExchanger(BaseModel):
    ImageRectangle: ImageRectangle
    ComponentType: int
    WaterInConnectionOrientation: int
    WaterOutConnectionOrientation: int
    WaterInConnectionCoordinate: Point3D
    WaterOutConnectionCoordinate: Point3D

class AbsorptionChillerUnit(BaseModel):
    ImageRectangle: ImageRectangle
    ComponentType: int

class HVACConnections(BaseModel):
    HVACConnection: HVACConnection | list['HVACConnection']

class HVACConnection(BaseModel):
    ObjectIDs: ObjectIDs
    LoopHandle: int
    SubLoopType: int
    LoopType: int
    PlantLoopType: int
    LoopFlowDirection: int
    ElementList: ElementList

class ElementList(BaseModel):
    HVACConnectionElement: HVACConnectionElement | list['HVACConnectionElement']

class HVACConnectionElement(BaseModel):
    Line: Line
    SegmentList: SegmentList

class SegmentList(BaseModel):
    LineArray: LineArray

class LineArray(BaseModel):
    Line: Line | list['Line']

class FlowConnections(BaseModel):
    HVACSubLoopNodeConnection: HVACSubLoopNodeConnection | list['HVACSubLoopNodeConnection']

class HVACSubLoopNodeConnection(BaseModel):
    ObjectIDs: ObjectIDs
    Connected: int
    Coordinate: Point3D
    Attributes: Attributes

class OutdoorAirSystem(BaseModel):
    HeatRecovery: int
    Recirculation: int
    ImageRectangle: ImageRectangle
    Attributes: Attributes
    HeatRecoveryDevice: HeatRecoveryDevice

class IntakeDamper(BaseModel):
    ImageRectangle: ImageRectangle

class ExhaustDamper(BaseModel):
    ImageRectangle: ImageRectangle

class DOASIntakeDamper(BaseModel):
    ImageRectangle: ImageRectangle

class DOASExhaustDamper(BaseModel):
    ImageRectangle: ImageRectangle

class MixingDamper(BaseModel):
    ImageRectangle: ImageRectangle

class ExhaustUnitComponentList(BaseModel):
    AirHandlingUnitHVACComponent: AirHandlingUnitHVACComponent | list['AirHandlingUnitHVACComponent']

class IntakeUnitComponentList(BaseModel):
    AirHandlingUnitHVACComponent: AirHandlingUnitHVACComponent | list['AirHandlingUnitHVACComponent']

class HeatRecoveryDevice(BaseModel):
    ImageRectangle: ImageRectangle

class AirHandlingUnitHVACComponent(BaseModel):
    type: str
    ImageRectangle: ImageRectangle
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
    WaterInConnectionCoordinate: Point3D
    WaterOutConnectionCoordinate: Point3D
    AirInConnectionCoordinate: Point3D
    AirOutConnectionCoordinate: Point3D
    Attributes: Attributes
    ZoneComponentAttributeList: None | ZoneComponentAttributeList

class HVACConnectorNode(BaseModel):
    ObjectIDs: ObjectIDs
    Name: str
    Active: int

class BranchConnectionList(BaseModel):
    HVACConnectorNode: list['HVACConnectorNode']
