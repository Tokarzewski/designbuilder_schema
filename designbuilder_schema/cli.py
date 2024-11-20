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
    if "dbJSON" in str(dictionary.keys()):
        return dictionary["dbJSON"]["@version"]
    elif "dbXML" in str(dictionary.keys()):
        return dictionary["dbXML"]["@version"]
    else:
        print("Can't find dbJSON or dbXML in: ", dictionary.keys())


def change_fileformat(filepath: str, new_ext: str) -> Path:
    return Path(filepath).with_suffix(new_ext)


def xml_to_json(xml_filepath: str):
    """Convert XML file to JSON file."""
    dictionary = load_file_to_dict(xml_filepath)
    dictionary["dbJSON"] = dictionary.pop("dbXML")
    json_filepath = change_fileformat(xml_filepath, ".json")

    with open(json_filepath, "w") as f:
        json.dump(dictionary, f, indent=4)


def json_to_xml(json_filepath: str):
    """Convert JSON file to XML file."""
    dictionary = load_file_to_dict(json_filepath)
    dictionary["dbXML"] = dictionary.pop("dbJSON")
    xml_filepath = change_fileformat(json_filepath, ".xml")

    with open(xml_filepath, "w") as f:
        xml_data = unparse(dictionary, full_document=True, pretty=True)
        f.write(xml_data)


def validate(filepath: str) -> str:
    """Check if file follows the schema."""
    DBJSON = load_model(filepath)
    return f"Validation successful, file saved in version {DBJSON.version}."


if __name__ == "__main__":
    Fire(
        {
            "version": get_version,
            "validate": validate,
            "xml2json": xml_to_json,
            "json2xml": json_to_xml,
        }
    )
