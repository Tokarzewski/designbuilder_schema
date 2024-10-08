"""
geometry.py
====================================
The geometry module of the designbuilder_schema
"""

from designbuilder_schema.base import BaseModel
from designbuilder_schema.id import ObjectIDs
from typing import List, Union
from pydantic import field_validator


class Vertices(BaseModel):
    Point3D: List["Point3D"]

    @field_validator('Point3D', mode='before')
    def parse(cls, v: Union[List[str], List["Point3D"], List[dict]]) -> List["Point3D"]:
        if not isinstance(v, list):
            raise ValueError("Expected a list of Point3D values")

        result = []
        for item in v:
            if isinstance(item, str):
                result.append(Point3D(Point3D=item))
            elif isinstance(item, Point3D):
                result.append(item)
            else:
                raise ValueError(f"Unexpected type for Point3D: {type(item)}")
        
        return result

    def __getitem__(self, index: int) -> "Point3D":
            return self.Point3D[index]

    def __iter__(self):
        return iter(self.Point3D)

    
class Point3D(BaseModel):
    Point3D: str
    
    @field_validator('Point3D')
    def parse_point3d(cls, v: str) -> str:
        parts = v.split(';')
        if len(parts) != 3:
            raise ValueError("Point3D string must have exactly 3 components separated by ';'")
        return v

    @property
    def x(self) -> float:
        return float(self.Point3D.split(';')[0].strip())

    @property
    def y(self) -> float:
        return float(self.Point3D.split(';')[1].strip())

    @property
    def z(self) -> float:
        return float(self.Point3D.split(';')[2].strip())
    
    def coordinates(self) -> List[float]:
        return [float(coord.strip()) for coord in self.Point3D.split(';')]


class Range(BaseModel):
    """Used only in ImageRectangle to represent rectangle.
    Org - top left corner.
    End -  bottom right corner."""

    Org: "Point3D"
    End: "Point3D"


class Line(BaseModel):
    ObjectIDs: "ObjectIDs"
    Begin: "Point3D"
    End: "Point3D"
