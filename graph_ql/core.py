from strawberry.experimental.pydantic import type as strawberry_type
from designbuilder_schema.attributes import *
from designbuilder_schema.core import DSB, Site
from typing import Optional
from strawberry import auto

from .attributes import NameAttributesType
from .tables import TablesType


@strawberry_type(model=Site)
class SiteType:
    count: auto
    handle: auto
    Attributes: NameAttributesType
    Tables: Optional[TablesType]
    # AssemblyLibrary: Optional["AssemblyLibrary"]
    # Buildings: Optional["Buildings"]


@strawberry_type(model=DSB)
class DSBType:
    name: auto
    date: auto
    version: auto
    objects: auto
    Site: Optional[SiteType]


"""@strawberry_type(model=Buildings, all_fields=True)
class BuildingsType:
    pass"""
