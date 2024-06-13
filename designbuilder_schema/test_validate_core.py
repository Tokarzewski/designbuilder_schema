import os, json
from core import DBJSON


def get_json_filepaths(directory):
    json_filepaths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_filepaths.append(os.path.join(root, file))
    return json_filepaths


def test_validate_dbjson(filepath):
    with open(filepath, "r") as f:
        json_data = json.load(f)
        db_json = DBJSON.model_validate(json_data["dbJSON"])
    return db_json


if __name__ == "__main__":
    json_filepaths = get_json_filepaths("samples\\models")

    for filepath in json_filepaths:
        print("START ", filepath)
        test_validate_dbjson(filepath)
        print("END ", filepath)
