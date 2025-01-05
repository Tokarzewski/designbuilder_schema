from designbuilder_schema.base import BaseModel, AlwaysList
from typing import Optional


class NameAttribute(BaseModel):
    """Site and HVAC Attibute"""

    name: str
    text: Optional[str] = None


class KeyAttribute(BaseModel):
    """Non-Site and Non-HVAC Attibute"""

    key: str
    text: str = None


class NameAttributes(BaseModel):
    """Site and HVAC Attibutes"""

    Attribute: AlwaysList["NameAttribute"]


class KeyAttributes(BaseModel):
    """Non-Site and Non-HVAC Attibute"""

    Attribute: AlwaysList["KeyAttribute"]


class HVACAttributeList(BaseModel):
    buildingZoneHandle: str
    Attributes: "NameAttributes"


class ZoneComponentAttributeList(BaseModel):
    HVACAttributeList: AlwaysList["HVACAttributeList"]
