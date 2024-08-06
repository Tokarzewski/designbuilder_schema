from designbuilder_schema.utils import load

filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"
db_json = load(filepath)
print(db_json.version)
