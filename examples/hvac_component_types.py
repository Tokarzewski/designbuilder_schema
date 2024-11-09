from designbuilder_schema.utils import load_model


dbjson_filepath = r".\samples\models\DetailedHVAC.json"
db_json = load_model(dbjson_filepath)

site = db_json.Site
building = site.Buildings.Building
hvac_network = building.HVACNetwork
hvac_loops = hvac_network.HVACLoops.HVACLoop

hc_set = set()
for loop in hvac_loops:
    for subloop in [loop.SupplySubLoop, loop.DemandSubLoop]:
        for hc in subloop.HVACComponents.HVACComponent:
            hc_set.add(f"{hc.__class__.__name__} | {hc.type} | {hc.ComponentType}")

for item in hc_set:
    print(item)
