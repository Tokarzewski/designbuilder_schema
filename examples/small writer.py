from designbuilder_schema.core import DBJSON, DesignBuilderSchema
from designbuilder_schema.utils import save_data_to_file
import datetime

db_json = DBJSON(
    name="MadeByPydantic",
    date=datetime.date.today().isoformat(),
    version="8.0.0.052",
    objects="all",
    Site=None,
)

db_schema = DesignBuilderSchema(dbJSON=db_json)
db_schema_dict = db_schema.model_dump(by_alias=True)
save_data_to_file(db_schema_dict, "examples/new_file_using_pydantic.json")
