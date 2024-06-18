import os, json
from core import DBJSON


def get_json_filepaths(directory):
    json_filepaths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_filepaths.append(os.path.join(root, file))
    return json_filepaths


def test_validate_dbjson(filepath):
    with open(filepath, "r") as f:
        json_data = json.load(f)
        db_json = DBJSON.model_validate(json_data["dbJSON"])
    return db_json


json_filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.json"
db_json = test_validate_dbjson(json_filepath)

# check hvac component type for HVAC visualisation app
# hvac_component = db_json.Site.Buildings.Building.HVACNetwork.HVACLoops.HVACLoop[0].SupplySubLoop.HVACComponents.HVACComponent[1].ComponentType
# hvac_component.Attributes.Attribute[2].text
hvac_components = db_json.Site.Buildings.Building.HVACNetwork.HVACLoops.HVACLoop[
    0
].SupplySubLoop.HVACComponents.HVACComponent
hvac_component = hvac_components[0]
hvac_component_type = hvac_component.ComponentType
hvac_component_title = hvac_component.Attributes.Attribute[2].text

print(db_json.version)
print(hvac_component_type, "-", hvac_component_title)
print(hvac_component.Attributes)
