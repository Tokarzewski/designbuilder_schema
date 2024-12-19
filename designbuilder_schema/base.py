from pydantic import BaseModel, ConfigDict


def custom_alias_generator(attr: str) -> str:
    """
    Generate alias based on first letter size:
    1. Adds '@' prefix to lowercase attribute (type -> @type)
    2. Keeps uppercase element as-is (Name -> Name)
    3. For exceptions, use Field(alias='...')
    """
    return f"@{attr}" if attr[0].islower() else attr


class BaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=custom_alias_generator,
        populate_by_name=True,
        validate_assignment=True,
        str_strip_whitespace=True,
    )
