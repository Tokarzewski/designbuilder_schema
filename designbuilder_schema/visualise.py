"""
visualise.py
====================================
Extension module that adds visualization capabilities
"""

from designbuilder_schema.core import Building, BuildingBlock, Zone

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def vis_building(building: Building):
    """Show matplotlib plot for all zones in building."""
    building_blocks = building.BuildingBlocks.BuildingBlock
    _zones = []

    building_blocks = (
        building_blocks if isinstance(building_blocks, list) else [building_blocks]
    )

    for block in building_blocks:
        zones = block.Zones.Zone
        _zones.extend(zones if isinstance(zones, list) else [zones])

    display_zones([zone_vis_data(zone) for zone in _zones])


def display_zones(zones):
    """Display all zone faces and openings with random colours."""
    # Create 3D figure
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection="3d")

    # Generate distinct colors for each zone
    base_colors = ["lightgray", "lightgreen", "lightpink", "lightyellow", "lightblue"]
    colors = base_colors * (len(zones) // len(base_colors) + 1)

    # Track bounds for axis scaling
    x_coords, y_coords, z_coords = [], [], []

    # Plot each zone
    for zone_idx, zone in enumerate(zones):

        faces = zone["faces"]
        if faces:
            face_collection = Poly3DCollection(faces, alpha=0.3)
            face_collection.set_facecolor(colors[zone_idx])
            face_collection.set_edgecolor("black")
            ax.add_collection3d(face_collection)

            # Collect coordinates for bounds
            for face in faces:
                x, y, z = zip(*face)
                x_coords.extend(x)
                y_coords.extend(y)
                z_coords.extend(z)

        openings = zone["openings"]
        if openings:
            opening_collection = Poly3DCollection(openings, alpha=0.5)
            opening_collection.set_facecolor("lightblue")
            opening_collection.set_edgecolor("blue")
            ax.add_collection3d(opening_collection)

    # Set axis labels
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    max_range = max([max(x_coords), max(y_coords), max(z_coords)])
    min_range = min([min(x_coords), min(y_coords), min(z_coords)])

    # Set the limits with equal scaling
    ax.set_xlim(min_range, max_range)
    ax.set_ylim(min_range, max_range)
    ax.set_zlim(min_range, max_range)

    # Add title
    plt.title(f"Visualization of {len(zones)} Zones")

    plt.show()


def vis_building_block(self: BuildingBlock):
    # attributes = {a.key: a.text for a in self.Attributes.Attribute}
    # attributes["Title"]
    return self.ProfileBody.Body.faces


def zone_vis_data(zone: Zone):
    # attributes = {a.key: a.text for a in self.Attributes.Attribute}
    # attributes["Title"]
    faces = zone.Body.faces
    openings = zone.Body.openings
    dict = {"faces": faces, "openings": openings}
    return dict


def add_visualisation_extention():
    """Extend classes with the visualise methods"""
    Building.visualise = vis_building
    BuildingBlock.visualise = vis_building_block
