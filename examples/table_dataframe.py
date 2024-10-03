from designbuilder_schema.utils import load_and_validate

dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\Shoebox10x10-All.xml"
#dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"

db_json = load_and_validate(dbjson_filepath)

site = db_json.Site
tables = site.Tables
table = tables.Table[1]

print(table.Row[0])

dataframe = table.to_dataframe()
dataframe.loc[0, "Id"] = "9"
table.read_dataframe(dataframe)

print(table.Row[0])