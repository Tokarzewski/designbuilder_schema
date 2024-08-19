from designbuilder_schema.utils import load_and_validate


dbjson_filepath = r".\samples\models\DetailedHVAC.json"
db_json = load_and_validate(dbjson_filepath)

site = db_json.Site
building = site.Buildings.Building
hvac_network = building.HVACNetwork
hvac_loops = hvac_network.HVACLoops.HVACLoop

hvac_components_set = set()

for loop in hvac_loops:
    for subloop in [loop.SupplySubLoop, loop.DemandSubLoop]:
        for hc in subloop.HVACComponents.HVACComponent:

            hvac_components_set.add(
                "{0} | {1} | {2}".format(hc.__class__.__name__, hc.type, hc.ComponentType)
            )

for item in hvac_components_set:
    print(item)
