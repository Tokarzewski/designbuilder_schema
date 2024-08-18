"""
geometry.py
====================================
The geometry module of the designbuilder_schema
"""

from designbuilder_schema.base import BaseModel
from designbuilder_schema.id import ObjectIDs


class Point3D(BaseModel):
    Point3D: str


class Vertices(BaseModel):
    Point3D: list[str]


class Range(BaseModel):
    Org: "Point3D"
    End: "Point3D"


class Line(BaseModel):
    ObjectIDs: "ObjectIDs"
    Begin: "Point3D"
    End: "Point3D"
