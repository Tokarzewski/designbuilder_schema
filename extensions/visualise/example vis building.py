from building import add_extention
from designbuilder_schema.utils import load_model


model = load_model(r"samples\models\Tutorial Model.xml")
building = model.Site.Buildings.Building

add_extention()
building.visualise()
