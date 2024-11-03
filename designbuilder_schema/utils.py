import json, xmltodict
from designbuilder_schema.core import DBJSON


def load_file_to_dict(filepath: str) -> dict:
    """Load a file as a dictionary"""
    with open(filepath, "r") as f:
        file_content = f.read()
        if filepath.endswith(".json"):
            return json.loads(file_content)
        elif filepath.endswith(".xml"):
            return xmltodict.parse(xml_input=file_content)
        else:
            raise ValueError("Unsupported file format")


def load_and_validate(filepath: str) -> DBJSON:
    dictionary = load_file_to_dict(filepath)
    if filepath.endswith(".json"):
        return DBJSON.model_validate(dictionary["dbJSON"])
    elif filepath.endswith(".xml"):
        return DBJSON.model_validate(dictionary["dbXML"])


def save_data_to_file(data: str, filename: str):
    with open(filename, "w") as f:
        f.write(data)
    print(f"Text saved to {filename}")
