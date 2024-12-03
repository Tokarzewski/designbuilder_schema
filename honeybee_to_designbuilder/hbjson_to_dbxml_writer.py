"""
honeybee_to_designbuilder.py
====================================
Convert Honeybee model to DesignBuilder model
"""

import datetime

from designbuilder_schema.core import (
    DSBJSON, Site, Building, Buildings, BuildingBlock, Body, ProfileBody, BaseProfileBody,
    Zones, Zone, Surface, Opening, Attributes, Attribute, LightSensorOne, LightSensorTwo,
    SiteAttribute, SiteAttributes, Polygon
)
from designbuilder_schema.geometry import Point3D as DBPoint3D, Vertices
from designbuilder_schema.utils import save_model
from designbuilder_schema.id import ObjectIDs

from small_honeybee import load_and_validate, Model, Room, Face, Aperture, Door, Point3D as HBPoint3D


empty_object_id = ObjectIDs(
    handle = 0,
    buildingHandle = 0,
    buildingBlockHandle = 1,
    zoneHandle = -1,
    surfaceIndex = -1,
    openingIndex = -1)

db_point0 = DBPoint3D(Point3D="0.0; 0.0; 0.0")

def convert_point3d(point: HBPoint3D) -> DBPoint3D:
    """Convert a Ladybug Point3D to a DesignBuilder Point3D."""
    return DBPoint3D(Point3D=f"{point.x}; {point.y}; {point.z}")

def convert_aperture_to_opening(aperture: Aperture) -> Opening:
    """Convert a Honeybee Aperture to a DesignBuilder Opening."""
    vertices = [convert_point3d(v).Point3D for v in aperture.geometry.boundary]
    
    polygon = Polygon(
        auxiliaryType="", 
        ObjectIDs=empty_object_id, 
        Vertices=Vertices(Point3D=vertices),
        PolygonHoles=None)

    return Opening(
        type="Window",
        Polygon=polygon,
        Attributes=None,
        SegmentList=None
    )

def convert_door_to_opening(door: Door) -> Opening:
    """Convert a Honeybee Door to a DesignBuilder Opening."""
    vertices = [convert_point3d(v) for v in door.geometry.boundary]
    
    return Opening(
        type="Door",
        area=door.geometry.area if hasattr(door.geometry, 'area') else 0,
        Polygon={"Vertices": {"Point3D": vertices}},
        Attributes=Attributes(
            Attribute=[
                Attribute(key="Name", text=door.identifier)
            ]
        )
    )

def convert_face_to_surface(face: Face, vertices: list[str]) -> Surface:
    """Convert a Honeybee Face to a DesignBuilder Surface."""

    # Map Honeybee face types to DesignBuilder surface types
    surface_type_map = {
        'Wall': 'Wall',
        'RoofCeiling': 'Flat roof',
        'Floor': 'Floor',
        'AirBoundary': 'Air'
    }

    boundary_indices = [vertices.index(convert_point3d(p).Point3D) for p in face.geometry.boundary]
    vertex_indices = "; ".join(str(i) for i in boundary_indices)
    
    surface = Surface(
        type=surface_type_map.get(face.face_type, 'Wall'),
        area= 0,
        alpha=0,
        phi=0,
        defaultOpenings="",
        adjacentPartitionHandle=0,
        thickness=0.3,
        ObjectIDs=empty_object_id,
        VertexIndices=vertex_indices,
        HoleIndices=None,
        Openings=None,
        Adjacencies=None,
        Attributes=None
    )
    
    # Add openings if any exist
    openings = []
    if hasattr(face, 'apertures') and face.apertures:
        openings.extend(convert_aperture_to_opening(ap) for ap in face.apertures)
    
    """if hasattr(face, 'doors') and face.doors:
        openings.extend(convert_door_to_opening(door) for door in face.doors)
    """
    if openings:
        surface.Openings = {"Opening": openings}
    
    return surface

def convert_room_to_building_block(room: Room) -> BuildingBlock:
    """Convert a Honeybee Room to a DesignBuilder BuildingBlock."""
    import itertools
    all_points = {}
    for face in room.faces:
        for point in face.geometry.boundary:
            point_str = str(point)
            if point_str not in all_points:
                all_points[point_str] = convert_point3d(point).Point3D

    vertices = list(all_points.values())

    surfaces = []
    for face in room.faces:
        surface = convert_face_to_surface(face, vertices)
        surfaces.append(surface)

    body = Body(
            volume=0,
            extrusionHeight=3.0,
            ObjectIDs=empty_object_id,
            Vertices=Vertices(Point3D=vertices),
            Surfaces={"Surface": surfaces},
            VoidPerimeterList=None,
            Attributes=Attributes(
                Attribute=[
                    Attribute(key="Title", text="Zone 1")
                ]
            )
        )
    
    profile_body = ProfileBody(elementSlope=30.0, roofOverlap=0.0, Body=body)

    zone = Zone(
                parentZoneHandle="",
                inheritedZoneHandle="",
                planExtrusion="",
                innerSurfaceMode="",
                Body = body,
                LightSensorOne = LightSensorOne(index=0, Point3D=db_point0.Point3D),
                LightSensorTwo = LightSensorTwo(index=1, Point3D=db_point0.Point3D),
                LabelPosition = db_point0,
                Polygon = None,
                InnerSurfaceBody = None
            )
    
    return BuildingBlock(
        type="Plan extruusion",
        height=3.0,
        roofSlope=0,
        roofOverlap=0,
        roofType="Flat",
        wallSlope=0,
        ObjectIDs=empty_object_id,
        ComponentBlocks = None,
        CFDFans = None,
        AssemblyInstances = None,
        ProfileOutlines = None,
        InternalPartitions = None,
        VoidBodies = None,
        Zones=Zones(Zone=zone),
        ProfileBody = profile_body,
        Perimeter = None,
        BaseProfileBody = BaseProfileBody(ProfileBody=profile_body),
        Attributes=Attributes(
            Attribute=[
                Attribute(key="Title", text="Block 1")
            ]
        )
    )

def hb_to_dsb(hb_model: Model) -> DSBJSON:
    """Convert a Honeybee Model to a DesignBuilder Schema."""
    # Convert to metric units if necessary
    """if hb_model.units != 'Meters':
        hb_model = hb_model.duplicate()
        hb_model.convert_to_units('Meters')"""
    
    # Create building blocks from rooms
    building_blocks = [convert_room_to_building_block(room) for room in hb_model.rooms]
    
    # Create building
    building = Building(
        currentComponentBlockHandle=1,
        currentAssemblyInstanceHandle=1,
        currentPlaneHandle=1,
        ObjectIDs=empty_object_id,
        BuildingBlocks={"BuildingBlock": building_blocks},
        ComponentBlocks = None,
        AssemblyInstances = None,
        ProfileOutlines = None,
        ConstructionLines = None, 
        Planes = None, 
        HVACNetwork = None,
        BookmarkBuildings = None,
        Attributes=Attributes(
            Attribute=[
                Attribute(key="Title", text=hb_model.display_name),
                Attribute(key="GeometryDataLevel", text="3")
            ]
        )
    )
    version = "8.0.0.057"
    version_site_attribute = SiteAttribute(name="Version", text=version)
    site_attributes = SiteAttributes(Attribute=[version_site_attribute])

    # Create site with building
    site = Site(
        handle=1,
        count=1,
        Attributes=site_attributes,
        Tables=None,
        AssemblyLibrary=None,
        Buildings=Buildings(numberOfBuildings=1, Building=building),
    )
    
    # Create final DesignBuilder model
    db_json = DSBJSON(
            name=hb_model.display_name,
            date=datetime.date.today().isoformat(),
            version=version,
            objects="all",
            Site=site
        )
    
    return db_json

if __name__ == "__main__":
    hb_filepath = r"honeybee_to_designbuilder\HB Shoebox.json"
    hb_model = load_and_validate(hb_filepath)
    
    db_model = hb_to_dsb(hb_model)
    
    db_filepath = r"honeybee_to_designbuilder\HB Shoebox.xml"
    save_model(db_model, db_filepath)


# define proper handles to building, buildingblock, zone, surface. 
# all handles should be unique
# <Zone parentZoneHandle="10" inheritedZoneHandle="10" planExtrusion="True" innerSurfaceMode="Deflation">
# changed area, volume, slop floats to be different than 0
# ProfileBody is the BuildingBlock shape, make sure to use different handles  