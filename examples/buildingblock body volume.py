from designbuilder_schema.utils import load_model


filepath = r"C:\GitHub\designbuilder_schema\samples\models\Shoebox10x10.xml"
model = load_model(filepath)

site = model.Site
building = site.Buildings.Building
building_blocks = building.BuildingBlocks
body = building_blocks.BuildingBlock.Zones.Zone.Body

print(body.volume)
