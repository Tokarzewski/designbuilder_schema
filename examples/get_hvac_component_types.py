from designbuilder_schema.utils import load_and_validate


dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.json"
db_json = load_and_validate(dbjson_filepath)

site = db_json.Site
building = site.Buildings.Building
hvac_network = building.HVACNetwork
hvac_loops = hvac_network.HVACLoops.HVACLoop

for loop in hvac_loops:
    for subloop in [loop.SupplySubLoop, loop.DemandSubLoop]:
        for hvac_component in subloop.HVACComponents.HVACComponent:
            print(
                hvac_component.__class__.__name__,
                hvac_component.type,
                hvac_component.ComponentType,
            )
