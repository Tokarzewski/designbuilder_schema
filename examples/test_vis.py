from designbuilder_schema.visualise import add_visualisation_extention
from designbuilder_schema.utils import load_and_validate

add_visualisation_extention()

db_json = load_and_validate(r"samples\models\ThreeBlocks_SixZones.xml")
building = db_json.Site.Buildings.Building

building.visualise()