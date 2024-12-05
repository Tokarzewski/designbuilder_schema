"""
cli.py
====================================
The command line interface of the designbuilder_schema
"""

import json
from pathlib import Path
from fire import Fire
from designbuilder_schema.utils import load_file_to_dict, load_model
from xmltodict import unparse


def get_version(filepath: str) -> str:
    """Return the schema version."""
    dictionary = load_file_to_dict(filepath)
    if "dsbJSON" in str(dictionary.keys()):
        return dictionary["dsbJSON"]["@version"]
    elif "dsbXML" in str(dictionary.keys()):
        return dictionary["dsbXML"]["@version"]
    else:
        print("Can't find dsbJSON or dsbXML in: ", dictionary.keys())


def xml_to_json(xml_filepath: str):
    """Convert XML file to JSON file."""
    dictionary = load_file_to_dict(xml_filepath)
    dictionary["dsbJSON"] = dictionary.pop("dsbXML")
    json_filepath = Path(xml_filepath).with_suffix(".json")

    with open(json_filepath, "w") as f:
        json.dump(dictionary, f, indent=4)


def json_to_xml(json_filepath: str):
    """Convert JSON file to XML file."""
    dictionary = load_file_to_dict(json_filepath)
    dictionary["dsbXML"] = dictionary.pop("dsbJSON")
    xml_filepath = Path(json_filepath).with_suffix(".xml")

    with open(xml_filepath, "w") as f:
        xml_data = unparse(dictionary, full_document=True, pretty=True)
        f.write(xml_data)


def validate_file(filepath: str) -> str:
    """Check if file follows the schema."""
    model = load_model(filepath)
    return f"Validation successful, file saved in version {model.version}."


if __name__ == "__main__":
    Fire(
        {
            "version": get_version,
            "validate": validate_file,
            "xml2json": xml_to_json,
            "json2xml": json_to_xml,
        }
    )
