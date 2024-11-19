"""
honeybee_to_designbuilder.py
====================================
Convert Honeybee models to DesignBuilder format
"""

import pathlib
import json
from typing import Dict
import datetime

from honeybee.model import Model
from honeybee.room import Room
from honeybee.face import Face
from honeybee.aperture import Aperture
from honeybee.door import Door
from honeybee.shade import Shade
from ladybug_geometry.geometry3d import Point3D, Face3D

from designbuilder_schema.core import DesignBuilder, DBJSON, Site, Building, Buildings, BuildingBlock, Body
from designbuilder_schema.geometry import Point3D as DBPoint3D
from designbuilder_schema.tables import Tables

def convert_point3d(point: Point3D) -> DBPoint3D:
    """Convert a Ladybug Point3D to a DesignBuilder Point3D."""
    return DBPoint3D(Point3D=f"{point.x};{point.y};{point.z}")

def convert_aperture_to_opening(aperture: Aperture, face: Face) -> Dict:
    """Convert a Honeybee Aperture to a DesignBuilder Opening."""
    vertices = [convert_point3d(v) for v in aperture.geometry.vertices]
    
    return {
        "type": "Window", #if aperture.is_window else "Door",
        "area": aperture.geometry.area,
        "Vertices": {"Point3D": vertices},
        "Attributes": {
            "Attribute": [
                {"key": "Name", "text": aperture.display_name},
                #{"key": "Construction", "text": aperture.properties.energy.construction.display_name}
            ]
        }
    }

def convert_door_to_opening(door: Door, face: Face) -> Dict:
    """Convert a Honeybee Door to a DesignBuilder Opening."""
    vertices = [convert_point3d(v) for v in door.geometry.vertices]
    
    return {
        "type": "Door",
        "area": door.geometry.area,
        "Vertices": {"Point3D": vertices},
        "Attributes": {
            "Attribute": [
                {"key": "Name", "text": door.display_name},
            #    {"key": "Construction", "text": door.properties.energy.construction.display_name}
            ]
        }
    }

def convert_face_to_surface(face: Face) -> Dict:
    """Convert a Honeybee Face to a DesignBuilder Surface."""
    vertices = [convert_point3d(v) for v in face.geometry.vertices]
    
    # Map Honeybee face types to DesignBuilder surface types
    surface_type_map = {
        'Wall': 'Wall',
        'RoofCeiling': 'Roof',
        'Floor': 'Floor',
        'AirBoundary': 'Air'
    }
    
    surface = {
        "type": surface_type_map.get(face.type.name, 'Wall'),
        "area": face.area,
        "Vertices": {"Point3D": vertices},
        "Attributes": {
            "Attribute": [
                {"key": "Name", "text": face.display_name},
                #{"key": "Construction", "text": face.properties.energy.construction.display_name}
            ]
        }
    }
    
    # Add openings if any exist
    openings = []
    if face.apertures:
        openings.extend(convert_aperture_to_opening(ap, face) for ap in face.apertures)
    if face.doors:
        openings.extend(convert_door_to_opening(door, face) for door in face.doors)
    
    if openings:
        surface["Openings"] = {"Opening": openings}
    
    return surface

def convert_room_to_building_block(room: Room) -> BuildingBlock:
    """Convert a Honeybee Room to a DesignBuilder BuildingBlock."""
    surfaces = [convert_face_to_surface(face) for face in room.faces]
    
    return BuildingBlock(
        type="BuildingBlock",
        height=room.geometry.max.z - room.geometry.min.z,
        ObjectIDs={"ID": room.identifier},
        Zones={
            "Zone": {
                "Body": {
                    "Surfaces": {"Surface": surfaces},
                    "Vertices": {
                        "Point3D": [convert_point3d(v) for v in room.geometry.vertices]
                    }
                },
                "Attributes": {
                    "Attribute": []
                        #{"key": "Name", "text": room.display_name},
                        #{"key": "Type", "text": "Zone"}
                    #]
                }
            }
        }
    )

def convert_shade_to_context(shade: Shade) -> Dict:
    """Convert a Honeybee Shade to a DesignBuilder context object."""
    return {
        "type": "Shade",
        "Body": {
            "Vertices": {
                "Point3D": [convert_point3d(v) for v in shade.geometry.vertices]
            }
        },
        "Attributes": {
            "Attribute": [
                {"key": "Name", "text": shade.display_name}
            ]
        }
    }

def model_to_designbuilder(hb_model: Model) -> DesignBuilder:
    """Convert a Honeybee Model to a DesignBuilder Schema."""

    # Convert to metric units if necessary
    if hb_model.units != 'Meters':
        hb_model = hb_model.duplicate()
        hb_model.convert_to_units('Meters')
    
    # Create building
    building = Building(
        currentComponentBlockHandle=1,
        currentAssemblyInstanceHandle=1,
        currentPlaneHandle=1,
        ObjectIDs={"ID": "1"},
        BuildingBlocks={
            "BuildingBlock": [
                convert_room_to_building_block(room) for room in hb_model.rooms
            ]
        }
    )
    
    # Add context shades if any exist
    if hb_model.shades:
        building.ComponentBlocks = {
            "ComponentBlock": [
                convert_shade_to_context(shade) for shade in hb_model.shades
            ]
        }
    
    # Add building to site
    db_model.dbJSON.Site.Buildings.Building = building
    buildings = Buildings(numberOfBuildings=1, Building=[building])
    site = Site(handle=1, count=1, Buildings=buildings)

    db_model = DesignBuilder(
    dbJSON=DBJSON(
        name="UKNOWN",
        date=datetime.date.today().isoformat(),
        version="8.0.0.052",
        objects="all",
        Site=site,
    )
)
    return db_model

def write_model_to_dbjson(
    model: Model, 
    folder: str = '.', 
    name: str = None
) -> pathlib.Path:
    """Write a Honeybee Model to a DesignBuilder JSON file.
    
    Args:
        model: A Honeybee model to be converted
        folder: Target folder for the output file. Defaults to current directory.
        name: Optional name for the output file. Defaults to model display name.
        
    Returns:
        Path to the exported file
    """
    # Convert the model
    db_model = model_to_designbuilder(model)
    
    # Setup output path
    name = name
    if not name.lower().endswith('.dbjson'):
        name = f'{name}.dbjson'
    
    out_folder = pathlib.Path(folder)
    out_folder.mkdir(parents=True, exist_ok=True)
    out_file = out_folder.joinpath(name)
    
    # Write the file
    with out_file.open('w') as f:
        json.dump(db_model.model_dump(by_alias=True), f, indent=2)
    
    return out_file

if __name__ == "__main__":
    model = Model.from_file('examples/revit_sample_model.hbjson')
    output_path = write_model_to_dbjson(model, folder='output')