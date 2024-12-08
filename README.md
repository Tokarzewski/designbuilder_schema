# designbuilder_schema
Python library built on top of Pydantic for reading DBXML files from DesignBuilder software.

# requirements

- pandas
- pydantic
- fire
- xmltodict

# todo

1. map more HVAC classes
2. generate more examples
3. autogenerate docs using https://pypi.org/project/autodoc_pydantic/
4. Add enums (use enum.Enum with typing.Literal)
5. New example - How to find all objects of class (Point3D, Surface...)?
6. Include variable type, default, min and max values based on .fmt files
