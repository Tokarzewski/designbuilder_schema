from pydantic import BaseModel, ConfigDict


def custom_alias_generator(attr: str) -> str:
    """Generate alias based on field name and content type:
    - If field starts with lowercase -> add @ prefix
    - If field starts with uppercase -> use as is
    - Exceptions should be handled with Field(alias=#XYZ)
    """
    return f"@{attr}" if attr[0].islower() else attr


class BaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=custom_alias_generator,
        populate_by_name=True,
        validate_assignment=True, 
        str_strip_whitespace=True
    )