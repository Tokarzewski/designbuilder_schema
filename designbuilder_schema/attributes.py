from designbuilder_schema.base import BaseModel

from typing import List, Union
from pydantic import Field



"""
from pydantic import AliasChoices
class Attributes(BaseModel):
    Attribute: Union["Attribute", List["Attribute"]]


class Attribute(BaseModel):
    name: str = Field(default=None, validation_alias=AliasChoices('key', 'name'))
    text: str = Field(alias="#text", default=None)
"""


class NameAttributes(BaseModel):
    """Site and HVAC Attibutes"""

    Attribute: Union["NameAttribute", List["NameAttribute"]]


class KeyAttributes(BaseModel):
    """Non-Site and Non-HVAC Attibute"""

    Attribute: Union["KeyAttribute", List["KeyAttribute"]]


class NameAttribute(BaseModel):
    """Site and HVAC Attibute"""

    name: str = None
    text: str = Field(alias="#text", default=None)


class KeyAttribute(BaseModel):
    """Non-Site and Non-HVAC Attibute"""

    key: str = None
    text: str = Field(alias="#text", default=None)


class HVACAttributeList(BaseModel):
    buildingZoneHandle: str
    Attributes: "NameAttributes"


class ZoneComponentAttributeList(BaseModel):
    HVACAttributeList: Union["HVACAttributeList", list["HVACAttributeList"]]
