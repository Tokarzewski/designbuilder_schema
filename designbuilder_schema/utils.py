import json, xmltodict
from designbuilder_schema.core import DSB
from designbuilder_schema.id import set_site_counter


def remove_prefixes(_, key, value):
    if key[0] in "@#":
        return key[1:], value
    else:
        return key, value


def add_prefixes(data_dict):
    if isinstance(data_dict, list):
        return [add_prefixes(l) for l in data_dict]
    elif isinstance(data_dict, dict):
        return {
            ("#text" if key == "text" else "@" + key if key[0].islower() else key): (
                add_prefixes(val) if isinstance(val, (dict, list)) else val
            )
            for key, val in data_dict.items()
        }
    else:
        return data_dict


def load_file_to_dict(filepath: str) -> dict:
    """Load a file as a dictionary"""
    with open(filepath, "r") as f:
        file_content = f.read()
        if filepath.endswith(".json"):
            return json.loads(file_content)
        elif filepath.endswith(".xml"):
            return xmltodict.parse(file_content, postprocessor=remove_prefixes)
        else:
            raise ValueError("Unsupported file format")


def load_model(filepath: str) -> DSB:
    """Loads DBJSON model from file and validates at the same time."""
    dict = load_file_to_dict(filepath)
    key = "dsbXML" if filepath.endswith(".xml") else "dsbJSON"
    site_handle = int(dict[key]["Site"]["handle"])
    set_site_counter(site_handle)
    return DSB.model_validate(dict[key])


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


def save_model(model: DSB, filepath: str) -> None:
    model = model.model_dump(mode="json", by_alias=True)
    save_dict({"dsbJSON": model}, filepath)
