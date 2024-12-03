from designbuilder_schema.utils import load_model


dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"
db_json = load_model(dbjson_filepath)

site = db_json.Site
building = site.Buildings.Building
building_blocks = building.BuildingBlocks
body = building_blocks.BuildingBlock.Zones.Zone.Body

print(body.volume)
