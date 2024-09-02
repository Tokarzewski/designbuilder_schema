# designbuilder_schema
Python library built on top of Pydantic for reading DBXML files from DesignBuilder software.

# requirements

- pydantic
- xmltodict
- fire

# todo

1. map more HVAC classes
2. generate more examples
3. autogenerate docs using https://pypi.org/project/autodoc_pydantic/
4. Verify if it is worth adding enumerations (enums). Doesn't Pydantic already have efficient hashmaps?
5. Add an example of - How to find all objects of class (Point3D, Surface...)?
6. Optionally include variable type, default, min and max values based on .fmt files

# DesignBuilder bugs

1. dbXML schema has incorrect class names HVACNetwork and DetailedHVACNetwork
