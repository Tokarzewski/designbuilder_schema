"""
test_debug.py - created specifically for continous schema improvement
models from debug folder that pass the tests can be moved to examples folder
"""

import os, pytest
from designbuilder_schema.utils import load_model


def get_filepaths(directory, extension=".json"):
    filepaths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                filepaths.append(os.path.join(root, file))
    return filepaths


# Get model filepaths from models folder
debug_folder = r".\samples\debug"
json_filepaths = get_filepaths(debug_folder, extension=".json")
xml_filepaths = get_filepaths(debug_folder, extension=".xml")


@pytest.mark.parametrize("filepath", json_filepaths)
def test_validate_dbjson(filepath):
    dsb_json = load_model(filepath)

    # Check if the validation result is not None
    assert dsb_json is not None, f"dsbJSON validation failed for {filepath}"


@pytest.mark.parametrize("filepath", xml_filepaths)
def test_validate_dbxml(filepath):
    dsb_xml = load_model(filepath)

    # Check if the validation result is not None
    assert dsb_xml is not None, f"dsbXML validation failed for {filepath}"
