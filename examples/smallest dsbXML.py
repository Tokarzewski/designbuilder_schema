from designbuilder_schema.core import DSBJSON, Site, SiteAttributes, SiteAttribute
from designbuilder_schema.utils import save_model
import datetime

version = "8.0.0.057"

version_site_attribute = SiteAttribute(name="Version", text=version)

site_attributes = SiteAttributes(Attribute=[version_site_attribute])

site = Site(
    handle=1,
    count=1,
    Attributes=site_attributes,
    Tables=None,
    AssemblyLibrary=None,
    Buildings=None,
)

db_json = DSBJSON(
    name="MadeByPydantic",
    date=datetime.date.today().isoformat(),
    version=version,
    objects="all",
    Site=site,
)

save_model(db_json, "examples/MadeByPydantic.xml")
save_model(db_json, "examples/MadeByPydantic.json")