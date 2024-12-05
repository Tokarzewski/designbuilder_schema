from designbuilder_schema.utils import load_model

filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.json"
dsb_json = load_model(filepath)
print(dsb_json.version)

filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"
dsb_xml = load_model(filepath)
print(dsb_xml.version)
