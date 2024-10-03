from designbuilder_schema.utils import load_and_validate
from designbuilder_schema.tables import *

dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\Shoebox10x10-All.xml"
#dbjson_filepath = r"C:\GitHub\designbuilder_schema\samples\models\DetailedHVAC.xml"

db_json = load_and_validate(dbjson_filepath)

site = db_json.Site
tables = site.Tables 
glazing_table = Tables.get_table_by_name(tables, "Glazing") # type: Glazing

print(glazing_table.Layers)