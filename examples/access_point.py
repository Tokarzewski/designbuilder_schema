from designbuilder_schema.utils import load_model

dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"
db_json = load_model(dbjson_filepath)

site = db_json.Site
building = site.Buildings.Building
building_blocks = building.BuildingBlocks
vertices = building_blocks.BuildingBlock.Zones.Zone.Body.Vertices

first_point = vertices[0]
print(first_point)

first_point.coords = [10,0,0]
print(first_point)