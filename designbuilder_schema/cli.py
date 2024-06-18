"""
cli.py
====================================
The command line interface of the designbuilder_schema project
"""

import os, json, fire, xmltodict


def load_file_to_dict(filepath: str):
    """Load a file and return its content as a dictionary"""
    with open(filepath, "r") as f:
        file_content = f.read()
        if filepath.endswith(".json"):
            return json.loads(file_content)
        elif filepath.endswith(".xml"):
            return xmltodict.parse(xml_input=file_content)
        else:
            raise ValueError("Unsupported file format")


def get_version(filepath: str):
    """Return the schema version"""

    db_dictionary = load_file_to_dict(filepath)

    if "JSON" in str(db_dictionary.keys()):
        return db_dictionary["dbJSON"]["@version"]
    elif "XML" in str(db_dictionary.keys()):
        return db_dictionary["dbXML"]["@version"]
    else:
        print("Unsupported key", str(db_dictionary.keys()))


def change_fileformat(filepath: str, new_file_extension: str):
    return os.path.splitext(filepath)[0] + f".{new_file_extension}"


def xml_to_json(xml_filepath: str):
    """Convert XML file to JSON file"""
    dictionary = load_file_to_dict(xml_filepath)
    dictionary["dbJSON"] = dictionary.pop("dbXML")

    output_filepath = change_fileformat(xml_filepath, "json")

    with open(output_filepath, "w") as f:
        json.dump(dictionary, f, indent=4)


def json_to_xml(json_filepath: str):
    """Convert JSON file to XML file"""
    dictionary = load_file_to_dict(json_filepath)
    dictionary["dbXML"] = dictionary.pop("dbJSON")

    output_filepath = change_fileformat(json_filepath, "xml")

    with open(output_filepath, "w") as f:
        xml_data = xmltodict.unparse(dictionary, full_document=True, pretty=True)
        f.write(xml_data)


if __name__ == "__main__":
    fire.Fire(
        {"version": get_version, "xml2json": xml_to_json, "json2xml": json_to_xml}
    )
