from designbuilder_schema.utils import load_and_validate

dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.json"
db_json = load_and_validate(dbjson_filepath)

site = db_json.Site
building = site.Buildings.Building
building_blocks = building.BuildingBlocks
vertices = building_blocks.BuildingBlock.Zones.Zone.Body.Vertices

first_point = vertices[0]

print(first_point.x)
print(first_point.coordinates())