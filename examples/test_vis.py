from designbuilder_schema.visualise import add_visualisation_extention
from designbuilder_schema.utils import load_and_validate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def visualize_building(data):
    # Create 3D figure
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate distinct colors for each zone
    base_colors = ['lightgray', 'lightgreen', 'lightpink', 'lightyellow', 'lightblue']
    colors = base_colors * (len(data['zones']) // len(base_colors) + 1)
    
    # Track bounds for axis scaling
    x_coords, y_coords, z_coords = [], [], []
    
    # Plot each zone
    for zone_idx, zone in enumerate(data['zones']):
        # Plot faces (walls, floor, ceiling)
        faces = zone.get('faces', [])
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
    
    # Set equal scaling for all axes
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)
    z_min, z_max = min(z_coords), max(z_coords)
    
    # Calculate the range for each axis
    x_range = x_max - x_min
    y_range = y_max - y_min
    z_range = z_max - z_min
    
    # Find the largest range to ensure proper scaling
    max_range = max(x_range, y_range, z_range)
    
    # Calculate the mid points
    x_mid = (x_max + x_min) / 2
    y_mid = (y_max + y_min) / 2
    z_mid = (z_max + z_min) / 2
    
    # Set the limits with equal scaling and some padding

    ax.set_xlim(x_mid - max_range/2, x_mid + max_range/2)
    ax.set_ylim(y_mid - max_range/2, y_mid + max_range/2)
    ax.set_zlim(z_mid - max_range/2, z_mid + max_range/2)
    
    # Force equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    
    # Add title
    plt.title(f'Visualization of {len(data["zones"])} Zones')
    
    # Add legend for zones
    legend_elements = []
    for zone_idx, color in enumerate(colors[:len(data['zones'])]):
        legend_elements.append(plt.Rectangle((0,0), 1, 1, fc=color, alpha=0.25, label=f'Zone {zone_idx+1}'))
    legend_elements.append(plt.Rectangle((0,0), 1, 1, fc='lightblue', alpha=0.5, label='Openings'))
    ax.legend(handles=legend_elements, loc='upper right')
    
    # Adjust view angle for better visualization
    ax.view_init(elev=20, azim=45)
    
    plt.show()

add_visualisation_extention()

filepath = r"C:\Users\thinkpad\Downloads\CustomerModel.xml"
db_json = load_and_validate(filepath)

building = db_json.Site.Buildings.Building

visualize_building(building.visualise())