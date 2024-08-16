from pydantic import BaseModel, ConfigDict


class BaseModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True, validate_assignment=True, str_strip_whitespace=True
    )
