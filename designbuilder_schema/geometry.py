"""
geometry.py
====================================
The geometry module of the designbuilder_schema
"""

from designbuilder_schema.base import BaseModel
from designbuilder_schema.id import ObjectIDs
from typing import List, Union
from pydantic import field_validator, field_serializer


class Vertices(BaseModel):
    Point3D: List["Point3D"]

    @field_validator("Point3D", mode="before")
    def parse_vertices(cls, vertices: List[str]) -> List["Point3D"]:
        if not isinstance(vertices, list):
            raise ValueError("Expected a list of Point3D values")

        result = []
        for vertex in vertices:
            if isinstance(vertex, str):
                result.append(Point3D(Point3D=vertex))
            else:
                raise ValueError(f"Unexpected type for Point3D: {type(vertex)}")
        return result

    @field_serializer("Point3D")
    def serialize_vertices(self, vertices: List["Point3D"]) -> List[str]:
        return [vertex.Point3D for vertex in vertices]

    def __getitem__(self, index: int) -> "Point3D":
        return self.Point3D[index]

    def __setitem__(self, index: int, value: str) -> None:
        try:
            self.Point3D[index] = value
        except IndexError as e:
            raise ValueError(f"Invalid index {index} for Vertices.Point3D") from e

    def __iter__(self):
        return iter(self.Point3D)


class Point3D(BaseModel):
    Point3D: str

    @field_validator("Point3D")
    def parse_point3d(cls, point: str) -> str:
        coordinates = point.split(";")
        if len(coordinates) != 3:
            raise ValueError("Point3D str must have 3 floats separated by ;")
        return point

    @property
    def x(self) -> float:
        return float(self.Point3D.split(";")[0])

    @property
    def y(self) -> float:
        return float(self.Point3D.split(";")[1])

    @property
    def z(self) -> float:
        return float(self.Point3D.split(";")[2])

    @property
    def coords(self) -> List[float]:
        return [float(coord) for coord in self.Point3D.split(";")]

    def __setattr__(self, name: str, value: Union[float, List[float]]) -> None:
        if name == "coords":
            if isinstance(value, list) and len(value) == 3:
                self.Point3D = ";".join(map(str, value))
            else:
                raise ValueError("Coordinates must be a list of 3 numbers")
        elif name in ["x", "y", "z"]:
            index = {"x": 0, "y": 1, "z": 2}[name]
            coords = self.Point3D.split(";")
            coords[index] = str(value)
            self.Point3D = ";".join(coords)
        else:
            super().__setattr__(name, value)


class Range(BaseModel):
    """Used only in ImageRectangle to represent rectangle relative position.
    Org - top left corner.
    End -  bottom right corner."""

    Org: "Point3D"
    End: "Point3D"


class Line(BaseModel):
    ObjectIDs: "ObjectIDs"
    Begin: "Point3D"
    End: "Point3D"
