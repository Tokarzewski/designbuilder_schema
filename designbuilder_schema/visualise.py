"""
visualise.py
====================================
Extension module that adds visualization capabilities
"""

from designbuilder_schema.core import Building, BuildingBlock, Zone
from designbuilder_schema.hvac_network import HVACNetwork, HVACComponent
from designbuilder_schema.utils import load_and_validate


def building_vis(self: Building):
    #attributes = {a.key: a.text for a in self.Attributes.Attribute}
    building_blocks = self.BuildingBlocks.BuildingBlock
    zones = []

    if isinstance(building_blocks, list):
        for bb in building_blocks:
            zones.extend(bb.Zones.Zone)
    else:
        zones.extend(bb.Zones.Zone)

    return {"zones": [zone_vis(zone) for zone in zones]}


def building_block_vis(self: BuildingBlock):
    #attributes = {a.key: a.text for a in self.Attributes.Attribute}
    #attributes["Title"]
    return self.ProfileBody.Body.faces 


def zone_vis(self: Zone):
    #attributes = {a.key: a.text for a in self.Attributes.Attribute}
    #attributes["Title"]
    faces = self.Body.faces
    openings = self.Body.openings
    dict = {
        "faces": faces,
        "openings": openings
    }
    return dict


def hvac_network_vis(self: HVACNetwork):
    fig = 0
    return fig


def hvac_component_vis(self: HVACComponent):
    attributes = {a.name: a.text for a in self.Attributes.Attribute}
    attributes["Title"]
    fig = 0
    return fig


def add_visualisation_extention():
    """Extend classes with the visualisation methods"""
    Building.visualise = building_vis
    BuildingBlock.visualise = building_block_vis
    Zone.visualise = zone_vis
    
    HVACNetwork.visualise = hvac_network_vis
    HVACComponent.visualise = hvac_component_vis


if __name__ == "__main__":
    add_visualisation_extention()

    filepath = r"samples\models\ThreeBlocks_SixZones.xml"
    db_json = load_and_validate(filepath)
    
    building = db_json.Site.Buildings.Building
    #building_blocks = building.BuildingBlocks.BuildingBlock
    #zone = building_blocks.Zones.Zone
    
    """print(building.visualise())
    print(building_blocks.visualise())
    """
    from pprint import pprint
    pprint(building.visualise())