"""
cli.py
====================================
The command line interface of the designbuilder_schema project
"""

import os, json, fire, xmltodict


def load_file(file_path):
    """Load a file and return its content as a dictionary"""
    with open(file_path, "r") as f:
        file_content = f.read()
        if file_path.endswith(".json"):
            return json.loads(file_content)
        elif file_path.endswith(".xml"):
            return xmltodict.parse(xml_input=file_content)
        else:
            raise ValueError("Unsupported file format")


def get_version(file_path):
    """Return the schema version"""

    db_dictionary = load_file(file_path)

    if "JSON" in str(db_dictionary.keys()):
        return db_dictionary["dbJSON"]["@version"]
    elif "XML" in str(db_dictionary.keys()):
        return db_dictionary["dbXML"]["@version"]
    else:
        print("Unsupported key", str(db_dictionary.keys()))


def convert_dict_to_json(file_path):
    """Convert XML file to JSON file"""
    data = load_file(file_path)
    data['dbJSON'] = data.pop('dbXML')
    file_name, _ = os.path.splitext(os.path.basename(file_path))
    output_filepath = os.path.join(os.path.dirname(file_path), f"{file_name}.json")
    with open(output_filepath, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    fire.Fire({"version": get_version, 
               "xml2json": convert_dict_to_json})
