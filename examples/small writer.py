from designbuilder_schema.core import *
import datetime, json
from designbuilder_schema.utils import save_data_to_file
from designbuilder_schema.cli import json_to_xml

db_json = DBJSON(
    name="MadeByPydantic",
    date=datetime.date.today().isoformat(),
    version="8.0.0.042",
    objects="all",
    Site=None,
)

db_schema = DesignBuilderSchema(dbJSON=db_json)
db_schema_json = db_schema.model_dump(by_alias=True)

save_data_to_file(json.dumps(db_schema_json, indent=4), "examples/new_file_using_pydantic.json")

json_to_xml("examples/new_file_using_pydantic.json")
