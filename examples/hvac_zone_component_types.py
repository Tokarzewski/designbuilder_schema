from designbuilder_schema.utils import load_model


dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\debug\hvac_network.xml"
db_json = load_model(dbjson_filepath)

site = db_json.Site
building = site.Buildings.Building
hvac_network = building.HVACNetwork
zone_groups = hvac_network.HVACZoneGroups.HVACZoneGroup

hzc_set = set()
for zone_group in zone_groups:
    zone_components = zone_group.ZoneElementList.HVACZoneComponent
    for hc in zone_components:
        hzc_set.add(f"{hc.__class__.__name__} | {hc.type} | {hc.ComponentType}")

for item in hzc_set:
    print(item)
