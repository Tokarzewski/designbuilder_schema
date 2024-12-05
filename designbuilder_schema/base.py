from pydantic import BaseModel, ConfigDict


def custom_alias_generator(attr: str) -> str:
    """Generate alias based on attribute name:
    1. Adds '@' prefix to lowercase attr (type -> @type)
    2. Keeps uppercase attr as-is (Name -> Name)
    X. For exceptions, use Field(alias='...')
    """
    return f"@{attr}" if attr[0].islower() else attr


class BaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=custom_alias_generator,
        populate_by_name=True,
        validate_assignment=True,
        str_strip_whitespace=True,
    )
