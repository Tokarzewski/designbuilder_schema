from designbuilder_schema.base import BaseModel
from typing import List, Union, Optional


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

    Attribute: Union["NameAttribute", List["NameAttribute"]]


class KeyAttributes(BaseModel):
    """Non-Site and Non-HVAC Attibute"""

    Attribute: Union["KeyAttribute", List["KeyAttribute"]]


class HVACAttributeList(BaseModel):
    buildingZoneHandle: str
    Attributes: "NameAttributes"


class ZoneComponentAttributeList(BaseModel):
    HVACAttributeList: Union["HVACAttributeList", list["HVACAttributeList"]]
