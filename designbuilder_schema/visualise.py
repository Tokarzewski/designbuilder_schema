"""
visualise.py
====================================
Extension module that adds visualization capabilities
"""

from designbuilder_schema.core import Building, BuildingBlock, Zone
from designbuilder_schema.hvac_network import HVACNetwork, HVACComponent

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def building_data(building: Building):
    """Show matplotlib plot for all zones in building."""
    building_blocks = building.BuildingBlocks.BuildingBlock
    
    zones = []
    if isinstance(building_blocks, list):
        for bb in building_blocks:
            zones.extend(bb.Zones.Zone)
    else:
        zones.extend(building_blocks.Zones.Zone)
    
    # list of simplified zones for visualizations
    zones = [zone_vis_data(zone) for zone in zones]

    display_zones(zones)


def display_zones(zones):
    """Display all zone faces and openings with random colours."""
    # Create 3D figure
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate distinct colors for each zone
    base_colors = ['lightgray', 'lightgreen', 'lightpink', 'lightyellow', 'lightblue']
    colors = base_colors * (len(zones) // len(base_colors) + 1)
    
    # Track bounds for axis scaling
    x_coords, y_coords, z_coords = [], [], []
    
    # Plot each zone
    for zone_idx, zone in enumerate(zones):  # Changed from zones to zone_data
        # Plot faces (walls, floor, ceiling)
        faces = zone.get('faces', [])  # Now this will work as zone is a dict
        openings = zone.get('openings', [])
        
        if faces:
            face_collection = Poly3DCollection(faces, alpha=0.3)
            face_collection.set_facecolor(colors[zone_idx])
            face_collection.set_edgecolor('black')
            ax.add_collection3d(face_collection)
            
            # Collect coordinates for bounds
            for face in faces:
                x_coords.extend([v[0] for v in face])
                y_coords.extend([v[1] for v in face])
                z_coords.extend([v[2] for v in face])
                
        # Plot openings (windows, doors) if they exist
        openings = zone.get('openings', [])
        if openings:
            opening_collection = Poly3DCollection(openings, alpha=0.5)
            opening_collection.set_facecolor('lightblue')
            opening_collection.set_edgecolor('blue')
            ax.add_collection3d(opening_collection)
    
    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    max_range = max([max(x_coords), max(y_coords), max(z_coords)])
    min_range = min([min(x_coords), min(y_coords), min(z_coords)])
    
    # Set the limits with equal scaling
    ax.set_xlim(min_range, max_range)
    ax.set_ylim(min_range, max_range)
    ax.set_zlim(min_range, max_range)
    
    # Add title
    plt.title(f'Visualization of {len(zones)} Zones')
    
    plt.show()


def building_block_vis(self: BuildingBlock):
    #attributes = {a.key: a.text for a in self.Attributes.Attribute}
    #attributes["Title"]
    return self.ProfileBody.Body.faces 


def zone_vis_data(zone: Zone):
    #attributes = {a.key: a.text for a in self.Attributes.Attribute}
    #attributes["Title"]
    faces = zone.Body.faces
    openings = zone.Body.openings
    dict = {
        "faces": faces,
        "openings": openings
    }
    return dict


def zone_vis(zone: Zone):
    return


def hvac_network_vis(self: HVACNetwork):
    fig = 0
    return fig


def hvac_component_vis(self: HVACComponent):
    attributes = {a.name: a.text for a in self.Attributes.Attribute}
    attributes["Title"]
    fig = 0
    return fig


def add_visualisation_extention():
    """Extend classes with the visualise methods"""
    Building.visualise = building_data
    BuildingBlock.visualise = building_block_vis
    Zone.visualise = zone_vis
    
    HVACNetwork.visualise = hvac_network_vis
    HVACComponent.visualise = hvac_component_vis
