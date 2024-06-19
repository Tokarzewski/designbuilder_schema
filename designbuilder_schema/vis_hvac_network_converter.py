import os, json
from core import DBJSON
from hvac_network import *
from cli import xml_to_json, change_fileformat
from vis_small_hvac_network import *
from functools import reduce


def load_dbjson(json_filepath):
    with open(json_filepath, "r") as f:
        json_data = json.load(f)
        db_json = DBJSON.model_validate(json_data["dbJSON"])
    return db_json


def get_hvac_components_and_connections(sub_loops: list):
    component_list = []
    connection_list = []
    for sub_loop in sub_loops:
        for components in sub_loop.HVACComponents:
            for component in components[1]:
                component_list.append(component)
        for connections in sub_loop.HVACConnections:
            for connection in connections[1]:
                connection_list.append(connection)
    return component_list, connection_list


def convert_hvac_network(source: HVACNetwork) -> SmallHVACNetwork:
    """Main conversion function that combines all the steps"""
    small_hvac_components = []
    lines = []
    nodes = []

    # GETTING DETAILED HVAC OBJECTS
    hvac_loops = source.HVACLoops.HVACLoop
    sdl_origins, demand_sub_loops, supply_sub_loops = zip(
        *[
            [hvac_loop.Origin, hvac_loop.DemandSubLoop, hvac_loop.SupplySubLoop]
            for hvac_loop in hvac_loops
        ]
    )

    demand_hvac_components, demand_hvac_connections = (
        get_hvac_components_and_connections(demand_sub_loops)
    )
    supply_hvac_components, supply_hvac_connections = (
        get_hvac_components_and_connections(supply_sub_loops)
    )
    hvac_connections = demand_hvac_connections + supply_hvac_connections

    # CONVERTING OBJECTS

    small_hvac_components.extend(
        [convert_supply_demand_link(x.Point3D) for x in sdl_origins]
    )

    # hvac_connections = [convert_hvac_connections(x.) for x in hvac_connections]
    # Lines.append(hvac_connections)

    return SmallHVACNetwork(
        SHVACComponents=small_hvac_components, Lines=lines, Nodes=nodes
    )


def convert_Point3D_to_Point2D(Point3D: str, ndigits=4) -> Point2D:
    def bugfix_infinite_value(value, treshold=100000):
        if abs(value) < treshold:
            return value
        else:
            return 0
        
    x, y, _ = [float(x.strip()) for x in Point3D.split(";")]
    x, y = bugfix_infinite_value(x), bugfix_infinite_value(y)
    x, y = round(x, ndigits), round(y, ndigits)

    return Point2D(x=x, y=y)


def convert_supply_demand_link(source: Point3D) -> SHVACComponent:

    origin2D = convert_Point3D_to_Point2D(source)
    point1 = Point2D(x=origin2D.x - 24, y=origin2D.y + 44)
    point2 = Point2D(x=origin2D.x + 24, y=origin2D.y - 44)

    rectangle = Rectangle(Point1=point1, Point2=point2)

    image = Image(
        Rectangle=rectangle,
        texture="SupplyDemandLink_image.bmp",
        mask="SupplyDemandLink_mask.bmp",
    )
    name = "supply_demand_link"
    type = "supply_demand_link"

    return SHVACComponent(Image=image, name=name, type=type)


def save_small_hvac(filepath: str, small_hvac_network: SmallHVACNetwork):

    simple_dict = small_hvac_network.model_dump()

    with open(filepath, "w") as file:
        json.dump(simple_dict, file, indent=4)

    print(f"Data saved to {filepath}")


if __name__ == "__main__":
    xml_filepath = r"C:\Users\thinkpad\OneDrive - Designbuilder Software Ltd\scripting & plugins\HVAC Outputs Visualisation\dbXML examples\WAHP_withExhaustFan.xml"
    xml_to_json(xml_filepath)

    json_filepath = change_fileformat(xml_filepath, "json")
    db_json = load_dbjson(json_filepath)

    detailed_hvac_network = db_json.Site.Buildings.Building.HVACNetwork
    small_hvac_network = convert_hvac_network(detailed_hvac_network)

    save_small_hvac(filepath="simple_data.json", small_hvac_network=small_hvac_network)
