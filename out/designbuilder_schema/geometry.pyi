from designbuilder_schema.base import BaseModel as BaseModel
from designbuilder_schema.id import ObjectIDs as ObjectIDs

class Point3D(BaseModel):
    Point3D: str

class Vertices(BaseModel):
    Point3D: list[str]

class Range(BaseModel):
    Org: Point3D
    End: Point3D

class Line(BaseModel):
    ObjectIDs: ObjectIDs
    Begin: Point3D
    End: Point3D
