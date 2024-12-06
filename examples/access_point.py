from designbuilder_schema.utils import load_model

filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"
model = load_model(filepath)

site = model.Site
building = site.Buildings.Building
building_blocks = building.BuildingBlocks
vertices = building_blocks.BuildingBlock.Zones.Zone.Body.Vertices

first_point = vertices[0]
print(first_point)

first_point.coords = [10,0,0]
print(first_point)

first_point.z = 20
print(first_point)