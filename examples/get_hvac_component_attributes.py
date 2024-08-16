from designbuilder_schema.utils import load_and_validate


dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.json"
db_json = load_and_validate(dbjson_filepath)

site = db_json.Site
building = site.Buildings.Building
hvac_network = building.HVACNetwork
hvac_loops = hvac_network.HVACLoops.HVACLoop
first_loop = hvac_loops[0]

hvac_components = first_loop.SupplySubLoop.HVACComponents.HVACComponent
second_hvac_component = hvac_components[1]
hvac_component_type = second_hvac_component.ComponentType
hvac_component_title = second_hvac_component.Attributes.Attribute[2].text

print(db_json.version)
print(hvac_component_type, "-", hvac_component_title)

for attribute in second_hvac_component.Attributes.Attribute:
    print(attribute)
