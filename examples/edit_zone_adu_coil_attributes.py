from designbuilder_schema.utils import load_model, save_model
from designbuilder_schema.hvac_components import GenericHeatingCoil

filepath = r".\samples\models\Large10x10x10x8.xml"
model = load_model(filepath)

building = model.Site.Buildings.Building
hvac_zone_group = building.HVACNetwork.HVACZoneGroups.HVACZoneGroup
hvac_zone_components = hvac_zone_group.ZoneElementList.HVACZoneComponent

adu = hvac_zone_components[1]
heating_coil = adu.UnitElementList.HVACComponent[1] # type: GenericHeatingCoil
hvac_attribute_list = heating_coil.ZoneComponentAttributeList.HVACAttributeList

#print(len(hvac_attribute_list)) #1280
# update all 1280 items
for list in hvac_attribute_list:
    #print(len(first_hvac_attribute_list)) #101
    list.Attributes.Attribute[16].text = "1234"

# check one 
print(hvac_attribute_list[123].Attributes.Attribute[16])

save_model(model, r".\samples\models\Large10x10x10x8_edited.xml")


"""
1. dsbXML
2. Site
3. Buildings
4. Building
5. HVACNetwork 
6. HVACZoneGroups
7. HVACZoneGroup
8. ZoneElementList 
9. ZoneADUSingleDuctVAVReheat(HVACZoneComponent)
10. UnitElementList 
11. GenericHeatingCoil(HVACComponent)
12. ZoneComponentAttributeList
13. HVACAttributeList
14. Attributes
15. Attribute
"""