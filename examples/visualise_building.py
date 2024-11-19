from designbuilder_schema.visualise import add_visualisation_extention
from designbuilder_schema.utils import load_model


add_visualisation_extention()

db_json = load_model(r"samples\models\Tutorial Model.xml")
building = db_json.Site.Buildings.Building

building.visualise()