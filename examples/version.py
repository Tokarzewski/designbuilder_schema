from designbuilder_schema.utils import load_and_validate

filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.json"
db_json = load_and_validate(filepath)
print(db_json.version)

filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"
db_xml = load_and_validate(filepath)
print(db_xml.version)
