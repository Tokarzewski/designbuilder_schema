from pydantic import BaseModel

class SimplifiedHVACNetwork(BaseModel):
    HVACComponent: list["HVACComponent"]
    Lines: list["Line"]
    Nodes: list["Node"]

class HVACComponent(BaseModel):
    Image: "Image"
    name: str
    type: str
    attributes: dict

class Image(BaseModel):
    Rectangle: "Rectangle"
    Texture: str
    Mask: str

class Rectangle(BaseModel):
    point1: "Point2D"
    point2: "Point2D"

class Line(BaseModel):
    point1: "Point2D"
    point2: "Point2D"
    colour: str
    attributes: dict

class Point2D(BaseModel):
    X: float
    Y: float

class Node(BaseModel):
    point: "Point2D"
    name: str
    attributes: dict