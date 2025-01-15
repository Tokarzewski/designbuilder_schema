"""
test_debug.py - created specifically for continous schema improvement
models from debug folder that pass the tests can be moved to examples folder
"""

import os, pytest
from designbuilder_schema.utils import load_model


def get_filepaths(directory, extension=".xml"):
    filepaths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                filepaths.append(os.path.join(root, file))
    return filepaths


# Get model filepaths from folder
debug_folder = r".\samples\debug"
xml_filepaths = get_filepaths(debug_folder, extension=".xml")


@pytest.mark.parametrize("filepath", xml_filepaths)
def test_validate_dbxml(filepath):
    assert load_model(filepath)
