from designbuilder_schema.utils import load_model
from designbuilder_schema.tables import *

dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\Shoebox10x10-All.xml"

db_json = load_model(dbjson_filepath)

site = db_json.Site
tables = site.Tables
glazing_table = Tables.get_table_by_name(tables, "Glazing") # type: Glazing

print(glazing_table.Id[0])

dataframe = glazing_table.to_dataframe()
dataframe.loc[0, "Id"] = "9"
glazing_table.from_dataframe(dataframe)

print(glazing_table[0].Id)