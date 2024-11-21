import json, xmltodict
from designbuilder_schema.core import DBJSON


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


def load_model(filepath: str) -> DBJSON:
    """Loads DBJSON model from file and validates at the same time."""
    dictionary = load_file_to_dict(filepath)
    if filepath.endswith(".json"):
        return DBJSON.model_validate(dictionary["dbJSON"])
    elif filepath.endswith(".xml"):
        return DBJSON.model_validate(dictionary["dbXML"])


def save_dict(dictionary: dict, filepath: str) -> None:
    """Save dictionary to either JSON or XML file format."""
    if filepath.endswith(".json"):
        data = json.dumps(dictionary, indent=4)
    elif filepath.endswith(".xml"):
        dictionary = {"dbXML": dictionary["dbJSON"]}
        data = xmltodict.unparse(dictionary, full_document=True, pretty=True)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")

    with open(filepath, "w") as f:
        f.write(data)


def save_model(db_json: DBJSON, filepath: str) -> None:
    db_json = db_json.model_dump(mode="json", by_alias=True)
    save_dict({"dbJSON": db_json}, filepath)
