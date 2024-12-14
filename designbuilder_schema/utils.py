import json, xmltodict
from designbuilder_schema.core import DSBJSON
from designbuilder_schema.id import set_counter


def load_file_to_dict(filepath: str) -> dict:
    """Load a file as a dictionary"""
    with open(filepath, "r") as f:
        file_content = f.read()
        if filepath.endswith(".json"):
            return json.loads(file_content)
        elif filepath.endswith(".xml"):
            return xmltodict.parse(file_content)
        else:
            raise ValueError("Unsupported file format")


def load_model(filepath: str) -> DSBJSON:
    """Loads DBJSON model from file and validates at the same time."""
    dict = load_file_to_dict(filepath)
    key = "dsbXML" if filepath.endswith(".xml") else "dsbJSON"
    site_handle = int(dict[key]["Site"]["@handle"])
    set_counter(site_handle)
    return DSBJSON.model_validate(dict[key])


def save_dict(dictionary: dict, filepath: str) -> None:
    """Save dictionary to either JSON or XML file format."""
    if filepath.endswith(".json"):
        data = json.dumps(dictionary, indent=4)
    elif filepath.endswith(".xml"):
        dictionary = {"dsbXML": dictionary["dsbJSON"]}
        data = xmltodict.unparse(dictionary, full_document=True, pretty=True)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")

    with open(filepath, "w") as f:
        f.write(data)


def save_model(dsb_json: DSBJSON, filepath: str) -> None:
    dsb_json = dsb_json.model_dump(mode="json", by_alias=True)
    save_dict({"dsbJSON": dsb_json}, filepath)
