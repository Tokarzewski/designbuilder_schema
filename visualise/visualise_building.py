from .visualise import add_visualisation_extention
from designbuilder_schema.utils import load_model


add_visualisation_extention()

model = load_model(r"samples\models\Tutorial Model.xml")
building = model.Site.Buildings.Building
building.visualise()
