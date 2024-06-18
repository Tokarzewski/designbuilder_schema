import os, json
from core import DBJSON
from cli import xml_to_json, change_fileformat
from vis_small_hvac_network import *


def load_dbjson(json_filepath):
    with open(json_filepath, "r") as f:
        json_data = json.load(f)
        db_json = DBJSON.model_validate(json_data["dbJSON"])
    return db_json


xml_filepath = r"C:\Users\thinkpad\OneDrive - Designbuilder Software Ltd\scripting & plugins\HVAC Outputs Visualisation\dbXML examples\WAHP_withExhaustFan.xml"
xml_to_json(xml_filepath)

json_filepath = change_fileformat(xml_filepath, "json")
db_json = load_dbjson(json_filepath)

### 

detailed_hvac_network = db_json.Site.Buildings.Building.HVACNetwork
hvac_loops = detailed_hvac_network.HVACLoops.HVACLoop

x = [x.Origin for x in hvac_loops]

print(x)
