import json
from designbuilder_schema.hvac_network import HVACComponents
import pytest

filepaths = [
    r"C:\GitHub\designbuilder_schema\samples\fragments\DemandSubLoop_HVACComponents.json",
    r"C:\GitHub\designbuilder_schema\samples\fragments\SupplySubLoop_HVACComponents.json",
]


@pytest.fixture(params=filepaths)
def json_filepath(request):
    return request.param


def test_validate_component(json_filepath):
    with open(json_filepath, "r") as f:
        json_data = json.load(f)
        hvac_components = HVACComponents.model_validate(json_data["HVACComponents"])

    for hvac_component in hvac_components.HVACComponent:
        assert hvac_component is not None, f"Invalid HVAC component: {hvac_component}"
        print(hvac_component.type, " - ", hvac_component.__class__.__name__)
