from designbuilder_schema.base import BaseModel
from typing import List, Union, Any, Optional

class NameAttributes(BaseModel):
    """Site and HVAC Attibutes"""

    Attribute: Union["NameAttribute", List["NameAttribute"]]


class KeyAttributes(BaseModel):
    """Non-Site and Non-HVAC Attibute"""

    Attribute: Union["KeyAttribute", List["KeyAttribute"]]


class NameAttribute(BaseModel):
    """Site and HVAC Attibute"""

    name: str = None
    text: Any = None


class KeyAttribute(BaseModel):
    """Non-Site and Non-HVAC Attibute"""

    key: str = None
    text: Any = None


class HVACAttributeList(BaseModel):
    buildingZoneHandle: str
    Attributes: "NameAttributes"


class ZoneComponentAttributeList(BaseModel):
    HVACAttributeList: Union["HVACAttributeList", list["HVACAttributeList"]]
