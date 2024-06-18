import os
import json
from core import DBJSON
import pytest
import xml.etree.ElementTree as ET
import xmltodict


def get_filepaths(directory, extension=".json"):
    filepaths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                filepaths.append(os.path.join(root, file))
    return filepaths


# Get model filepaths from models folder
models_folder = r"C:\GitHub\designbuilder_schema\samples\models"
json_filepaths = get_filepaths(models_folder, extension=".json")


def load_file_to_dict(file_path: str):
    """Load a file and return its content as a dictionary"""
    with open(file_path, "r") as f:
        file_content = f.read()
        if file_path.endswith(".json"):
            return json.loads(file_content)
        elif file_path.endswith(".xml"):
            return xmltodict.parse(xml_input=file_content)
        else:
            raise ValueError("Unsupported file format")


@pytest.mark.parametrize("filepath", json_filepaths)
def test_validate_dbjson(filepath):
    dictionary = load_file_to_dict(filepath)

    # Check if the "dbJSON" key exists
    assert "dbJSON" in dictionary, f"Key 'dbJSON' not found in {filepath}"

    db_json = DBJSON.model_validate(dictionary["dbJSON"])

    # Check if the validation result is not None
    assert db_json is not None, f"DBJSON validation failed for {filepath}"


# collision in schema HVACNetwork vs DetailedHVACNetwork
"""
xml_filepaths = get_filepaths(models_folder, extension=".xml")
@pytest.mark.parametrize("filepath", xml_filepaths)
def test_validate_dbxml(filepath):
    dictionary = load_file_to_dict(filepath)

    ## Check if the "dbJSON" key exists
    # assert "dbXML" in dictionary, f"Key 'dbXML' not found in {filepath}"

    db_xml = DBJSON.model_validate(dictionary["dbXML"])

    # Check if the validation result is not None
    assert db_xml is not None, f"DBJSON validation failed for {filepath}"
"""
