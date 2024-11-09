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
models_folder = r".\samples\models"
json_filepaths = get_filepaths(models_folder, extension=".json")
xml_filepaths = get_filepaths(models_folder, extension=".xml")


@pytest.mark.parametrize("filepath", json_filepaths)
def test_validate_dbjson(filepath):
    db_json = load_model(filepath)

    # Check if the validation result is not None
    assert db_json is not None, f"dbJSON validation failed for {filepath}"


@pytest.mark.parametrize("filepath", xml_filepaths)
def test_validate_dbxml(filepath):
    db_xml = load_model(filepath)

    # Check if the validation result is not None
    assert db_xml is not None, f"dbXML validation failed for {filepath}"
