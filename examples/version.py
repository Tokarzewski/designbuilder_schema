from designbuilder_schema.utils import load_model

filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.json"
db_json = load_model(filepath)
print(db_json.version)

filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"
db_xml = load_model(filepath)
print(db_xml.version)
