import os, pytest
from designbuilder_schema.utils import load_model


def get_filepaths(directory, extension=".xml"):
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
def test_validate_dsbjson(filepath):
    assert load_model(filepath)


@pytest.mark.parametrize("filepath", xml_filepaths)
def test_validate_dsbxml(filepath):
    assert load_model(filepath)
