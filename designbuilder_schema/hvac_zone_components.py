from designbuilder_schema.geometry import Point3D
from designbuilder_schema.hvac_components import NoTypeHVACComponent, HVACComponent


class ZoneExtract(HVACComponent):
    Width: float
    Height: float
    Origin: "Point3D"
    ExtractGrille: "ExtractGrille"


class ExtractGrille(NoTypeHVACComponent):
    pass


class ZoneADUSingleDuctCAVNoReheat(HVACComponent):
    Width: float
    Height: float
    MixingBoxWidth: float
    SupplyDiffuser: "SupplyDiffuser"
    # UnitElementList


class SupplyDiffuser(NoTypeHVACComponent):
    pass


class ZoneConvectiveElectricBaseboard(HVACComponent):
    pass
