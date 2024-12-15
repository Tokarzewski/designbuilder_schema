from designbuilder_schema.utils import load_model

filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"
model = load_model(filepath)
print(model.Site.handle)
