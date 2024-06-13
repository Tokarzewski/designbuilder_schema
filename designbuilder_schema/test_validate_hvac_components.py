import json
from hvac_network import HVACComponents

def test_validate_component(cls, filepath):
    with open(filepath, "r") as f:
        json_data = json.load(f)
        db_json = cls.model_validate(json_data[cls.__name__])
    return db_json

if __name__ == "__main__":
    json_filepaths = [r"C:\GitHub\designbuilder_schema\samples\fragments\DemandSubLoop_HVACComponents.json",
                      r"C:\GitHub\designbuilder_schema\samples\fragments\SupplySubLoop_HVACComponents.json"]

    for filepath in json_filepaths:
        print("START ", filepath)
        hvac_components = test_validate_component(HVACComponents, filepath).HVACComponent
        for hvac_component in hvac_components:
            print(hvac_component.type, " - ", hvac_component.__class__.__name__)
        print("END ", filepath)