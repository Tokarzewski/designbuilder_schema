from designbuilder_schema.utils import load


dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.json"
db_json = load(dbjson_filepath)

site = db_json.Site
building = site.Buildings.Building
building_blocks = building.BuildingBlocks
body = building_blocks.BuildingBlock.ProfileBody.Body

print(db_json.version)
print(body)