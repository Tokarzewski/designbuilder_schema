"""Tests for the geometry module"""

import pytest
from designbuilder_schema.geometry import Point3D, Vertices, Line, Range
from designbuilder_schema.id import ObjectIDs


class TestPoint3D:
    """Test Point3D class functionality"""

    def test_point3d_creation(self):
        """Test creating a Point3D from a string"""
        point = Point3D(Point3D="1.0;2.0;3.0")
        assert point.Point3D == "1.0;2.0;3.0"

    def test_point3d_x_property(self):
        """Test accessing x coordinate"""
        point = Point3D(Point3D="1.5;2.0;3.0")
        assert point.x == 1.5

    def test_point3d_y_property(self):
        """Test accessing y coordinate"""
        point = Point3D(Point3D="1.0;2.5;3.0")
        assert point.y == 2.5

    def test_point3d_z_property(self):
        """Test accessing z coordinate"""
        point = Point3D(Point3D="1.0;2.0;3.5")
        assert point.z == 3.5

    def test_point3d_coords_property(self):
        """Test accessing all coordinates as a list"""
        point = Point3D(Point3D="1.0;2.0;3.0")
        assert point.coords == [1.0, 2.0, 3.0]

    def test_point3d_set_x(self):
        """Test setting x coordinate"""
        point = Point3D(Point3D="1.0;2.0;3.0")
        point.x = 5.0
        assert point.x == 5.0
        assert point.Point3D == "5.0;2.0;3.0"

    def test_point3d_set_y(self):
        """Test setting y coordinate"""
        point = Point3D(Point3D="1.0;2.0;3.0")
        point.y = 5.0
        assert point.y == 5.0
        assert point.Point3D == "1.0;5.0;3.0"

    def test_point3d_set_z(self):
        """Test setting z coordinate"""
        point = Point3D(Point3D="1.0;2.0;3.0")
        point.z = 5.0
        assert point.z == 5.0
        assert point.Point3D == "1.0;2.0;5.0"

    def test_point3d_set_coords(self):
        """Test setting all coordinates at once"""
        point = Point3D(Point3D="1.0;2.0;3.0")
        point.coords = [4.0, 5.0, 6.0]
        assert point.coords == [4.0, 5.0, 6.0]
        assert point.Point3D == "4.0;5.0;6.0"

    def test_point3d_set_coords_invalid_length(self):
        """Test that setting coords with wrong length raises ValueError"""
        point = Point3D(Point3D="1.0;2.0;3.0")
        with pytest.raises(ValueError, match="Coordinates must be a list of 3 numbers"):
            point.coords = [1.0, 2.0]


class TestVertices:
    """Test Vertices class functionality"""

    def test_vertices_creation(self):
        """Test creating Vertices from list of strings"""
        vertices = Vertices(Point3D=["1.0;2.0;3.0", "4.0;5.0;6.0"])
        assert len(vertices.Point3D) == 2

    def test_vertices_getitem(self):
        """Test accessing individual vertex by index"""
        vertices = Vertices(Point3D=["1.0;2.0;3.0", "4.0;5.0;6.0"])
        point = vertices[0]
        assert isinstance(point, Point3D)
        assert point.x == 1.0
        assert point.y == 2.0
        assert point.z == 3.0

    def test_vertices_setitem_with_point3d(self):
        """Test setting a vertex with Point3D object"""
        vertices = Vertices(Point3D=["1.0;2.0;3.0", "4.0;5.0;6.0"])
        new_point = Point3D(Point3D="7.0;8.0;9.0")
        vertices[0] = new_point
        assert vertices.Point3D[0] == "7.0;8.0;9.0"

    def test_vertices_setitem_with_string(self):
        """Test setting a vertex with string"""
        vertices = Vertices(Point3D=["1.0;2.0;3.0", "4.0;5.0;6.0"])
        vertices[1] = "7.0;8.0;9.0"
        assert vertices.Point3D[1] == "7.0;8.0;9.0"

    def test_vertices_iter(self):
        """Test iterating over vertices"""
        vertices = Vertices(Point3D=["1.0;2.0;3.0", "4.0;5.0;6.0"])
        coords_list = list(vertices)
        assert len(coords_list) == 2
        assert coords_list[0] == "1.0;2.0;3.0"
        assert coords_list[1] == "4.0;5.0;6.0"


class TestLine:
    """Test Line class functionality"""

    def test_line_creation(self):
        """Test creating a Line with Begin and End points"""
        begin = Point3D(Point3D="0.0;0.0;0.0")
        end = Point3D(Point3D="10.0;10.0;10.0")
        line = Line(Begin=begin, End=end)
        assert line.Begin.Point3D == "0.0;0.0;0.0"
        assert line.End.Point3D == "10.0;10.0;10.0"

    def test_line_has_object_ids(self):
        """Test that Line has ObjectIDs"""
        begin = Point3D(Point3D="0.0;0.0;0.0")
        end = Point3D(Point3D="10.0;10.0;10.0")
        line = Line(Begin=begin, End=end)
        assert isinstance(line.ObjectIDs, ObjectIDs)
        assert line.ObjectIDs.handle >= 0


class TestRange:
    """Test Range class functionality"""

    def test_range_creation(self):
        """Test creating a Range with Org and End points"""
        org = Point3D(Point3D="0.0;0.0;0.0")
        end = Point3D(Point3D="100.0;100.0;0.0")
        range_obj = Range(Org=org, End=end)
        assert range_obj.Org.Point3D == "0.0;0.0;0.0"
        assert range_obj.End.Point3D == "100.0;100.0;0.0"
