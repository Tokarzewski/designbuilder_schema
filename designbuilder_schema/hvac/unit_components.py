from pydantic import field_validator
from typing import List, Literal
from designbuilder_schema.base import BaseModel
from designbuilder_schema.hvac.components import (
    NoTypeHVACComponent,
    HVACComponent,
    GenericHeatingCoil,
    WaterCoolingCoil,
)


class UnitElementList(BaseModel):
    HVACComponent: List

    @field_validator("HVACComponent", mode="before")
    def recast_components(cls, components):
        mapping = {
            "Supply fan": SupplyFan,
            "Zone ADU louvre": ZoneADULouvre,
            "Zone ADU PIU intake louvre": ZoneADUPIUIntakeLouvre,
            "Water cooling coil": WaterCoolingCoil,
            "Generic heating coil": GenericHeatingCoil,
            "DX cooling coil": DXCoolingCoil,
            "DX heating coil": DXHeatingCoil,
            "Variable refrigerant flow cooling DX coil": VariableRefrigerantFlowCoolingDXCoil,
            "Variable refrigerant flow heating DX coil": VariableRefrigerantFlowHeatingDXCoil,
            "Water-to-air heat pump cooling coil": WaterToAirHeatPumpCoolingCoil,
            "Water-to-air heat pump heating coil": WaterToAirHeatPumpHeatingCoil,
        }
        if not isinstance(components, list):
            components = [components]
        return [
            mapping.get(component["type"], HVACComponent)(**component)
            for component in components
        ]


class SupplyFan(NoTypeHVACComponent):
    type: Literal["Supply fan"]


class ZoneADULouvre(NoTypeHVACComponent):
    type: Literal["Zone ADU louvre"]


class ZoneADUPIUIntakeLouvre(NoTypeHVACComponent):
    type: Literal["Zone ADU PIU intake louvre"]


class VariableRefrigerantFlowCoolingDXCoil(NoTypeHVACComponent):
    type: Literal["Variable refrigerant flow cooling DX coil"]


class VariableRefrigerantFlowHeatingDXCoil(NoTypeHVACComponent):
    type: Literal["Variable refrigerant flow heating DX coil"]


class DXCoolingCoil(NoTypeHVACComponent):
    type: Literal["DX cooling coil"]


class DXHeatingCoil(NoTypeHVACComponent):
    type: Literal["DX heating coil"]


class WaterToAirHeatPumpCoolingCoil(NoTypeHVACComponent):
    type: Literal["Water-to-air heat pump cooling coil"]


class WaterToAirHeatPumpHeatingCoil(NoTypeHVACComponent):
    type: Literal["Water-to-air heat pump heating coil"]
