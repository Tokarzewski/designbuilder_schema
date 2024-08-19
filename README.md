# designbuilder_schema
Python library built on top of pydantic for reading DBXML files from DesignBuilder software.

# requirements

- pydantic
- xmltodict
- fire

# todo

1. map more HVAC classes
2. generate more examples
3. autogenerate docs using https://pypi.org/project/autodoc_pydantic/
4. add more enumerations (enums)
5. Add example on - How to find all objects of class Point3D?
6. store tables in pandas, store attributes in dicts

# DesignBuilder bugs

1. dbXML schema has incorrect class names HVACNetwork and DetailedHVACNetwork 