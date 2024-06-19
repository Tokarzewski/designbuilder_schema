from pydantic import BaseModel

class SmallHVACNetwork(BaseModel):
    SHVACComponents: list["SHVACComponent"]
    Lines: list["Line"]
    Nodes: list["Node"]


class SHVACComponent(BaseModel):
    Image: "Image"
    name: str
    type: str
    attributes: dict = {}


class Image(BaseModel):
    Rectangle: "Rectangle"
    texture: str
    mask: str


class Rectangle(BaseModel):
    Point1: "Point2D"
    Point2: "Point2D"


class Line(BaseModel):
    Point1: "Point2D"
    Point2: "Point2D"
    colour: str
    attributes: dict


class Point2D(BaseModel):
    x: float
    y: float


class Node(BaseModel):
    Point: "Point2D"
    name: str
    attributes: dict
