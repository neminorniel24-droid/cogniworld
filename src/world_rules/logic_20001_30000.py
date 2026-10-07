import torch

def rule_20001(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20002(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20003(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20004(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20005(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20006(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20007(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20008(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20009(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20010(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20011(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20012(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20013(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20014(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20015(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20016(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20017(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20018(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20019(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20020(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20021(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20022(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20023(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20024(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20025(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20026(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20027(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20028(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20029(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20030(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20031(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20032(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20033(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20034(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20035(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20036(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20037(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20038(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20039(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20040(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20041(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20042(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20043(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20044(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20045(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20046(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20047(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20048(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20049(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20050(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20051(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20052(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20053(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20054(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20055(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20056(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20057(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20058(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20059(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20060(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20061(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20062(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20063(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20064(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20065(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20066(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20067(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20068(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20069(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20070(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20071(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20072(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20073(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20074(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20075(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20076(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20077(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20078(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20079(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20080(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20081(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20082(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20083(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20084(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20085(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20086(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20087(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20088(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20089(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20090(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20091(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20092(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20093(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20094(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20095(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20096(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20097(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20098(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20099(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20100(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20101(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20102(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20103(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20104(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20105(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20106(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20107(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20108(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20109(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20110(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20111(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20112(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20113(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20114(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20115(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20116(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20117(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20118(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20119(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20120(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20121(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20122(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20123(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20124(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20125(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20126(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20127(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20128(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20129(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20130(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20131(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20132(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20133(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20134(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20135(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20136(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20137(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20138(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20139(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20140(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20141(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20142(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20143(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20144(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20145(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20146(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20147(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20148(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20149(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20150(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20151(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20152(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20153(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20154(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20155(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20156(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20157(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20158(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20159(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20160(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20161(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20162(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20163(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20164(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20165(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20166(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20167(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20168(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20169(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20170(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20171(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20172(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20173(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20174(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20175(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20176(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20177(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20178(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20179(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20180(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20181(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20182(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20183(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20184(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20185(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20186(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20187(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20188(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20189(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20190(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20191(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20192(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20193(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20194(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20195(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20196(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20197(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20198(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20199(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20200(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20201(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20202(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20203(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20204(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20205(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20206(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20207(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20208(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20209(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20210(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20211(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20212(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20213(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20214(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20215(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20216(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20217(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20218(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20219(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20220(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20221(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20222(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20223(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20224(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20225(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20226(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20227(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20228(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20229(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20230(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20231(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20232(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20233(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20234(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20235(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20236(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20237(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20238(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20239(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20240(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20241(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20242(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20243(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20244(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20245(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20246(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20247(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20248(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20249(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20250(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20251(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20252(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20253(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20254(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20255(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20256(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20257(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20258(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20259(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20260(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20261(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20262(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20263(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20264(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20265(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20266(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20267(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20268(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20269(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20270(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20271(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20272(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20273(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20274(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20275(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20276(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20277(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20278(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20279(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20280(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20281(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20282(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20283(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20284(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20285(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20286(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20287(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20288(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20289(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20290(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20291(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20292(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20293(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20294(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20295(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20296(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20297(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20298(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20299(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20300(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20301(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20302(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20303(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20304(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20305(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20306(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20307(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20308(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20309(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20310(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20311(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20312(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20313(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20314(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20315(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20316(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20317(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20318(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20319(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20320(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20321(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20322(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20323(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20324(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20325(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20326(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20327(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20328(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20329(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20330(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20331(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20332(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20333(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20334(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20335(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20336(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20337(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20338(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20339(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20340(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20341(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20342(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20343(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20344(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20345(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20346(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20347(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20348(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20349(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20350(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20351(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20352(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20353(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20354(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20355(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20356(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20357(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20358(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20359(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20360(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20361(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20362(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20363(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20364(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20365(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20366(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20367(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20368(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20369(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20370(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20371(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20372(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20373(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20374(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20375(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20376(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20377(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20378(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20379(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20380(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20381(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20382(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20383(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20384(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20385(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20386(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20387(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20388(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20389(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20390(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20391(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20392(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20393(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20394(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20395(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20396(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20397(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20398(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20399(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20400(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20401(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20402(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20403(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20404(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20405(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20406(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20407(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20408(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20409(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20410(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20411(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20412(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20413(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20414(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20415(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20416(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20417(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20418(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20419(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20420(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20421(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20422(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20423(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20424(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20425(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20426(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20427(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20428(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20429(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20430(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20431(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20432(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20433(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20434(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20435(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20436(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20437(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20438(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20439(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20440(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20441(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20442(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20443(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20444(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20445(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20446(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20447(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20448(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20449(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20450(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20451(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20452(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20453(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20454(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20455(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20456(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20457(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20458(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20459(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20460(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20461(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20462(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20463(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20464(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20465(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20466(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20467(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20468(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20469(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20470(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20471(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20472(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20473(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20474(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20475(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20476(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20477(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20478(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20479(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20480(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20481(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20482(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20483(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20484(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20485(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20486(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20487(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20488(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20489(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20490(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20491(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20492(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20493(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20494(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20495(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20496(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20497(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20498(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20499(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20500(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20501(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20502(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20503(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20504(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20505(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20506(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20507(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20508(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20509(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20510(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20511(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20512(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20513(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20514(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20515(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20516(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20517(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20518(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20519(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20520(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20521(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20522(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20523(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20524(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20525(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20526(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20527(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20528(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20529(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20530(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20531(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20532(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20533(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20534(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20535(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20536(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20537(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20538(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20539(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20540(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20541(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20542(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20543(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20544(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20545(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20546(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20547(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20548(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20549(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20550(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20551(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20552(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20553(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20554(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20555(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20556(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20557(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20558(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20559(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20560(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20561(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20562(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20563(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20564(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20565(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20566(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20567(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20568(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20569(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20570(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20571(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20572(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20573(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20574(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20575(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20576(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20577(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20578(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20579(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20580(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20581(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20582(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20583(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20584(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20585(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20586(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20587(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20588(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20589(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20590(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20591(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20592(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20593(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20594(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20595(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20596(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20597(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20598(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20599(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20600(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20601(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20602(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20603(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20604(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20605(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20606(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20607(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20608(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20609(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20610(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20611(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20612(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20613(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20614(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20615(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20616(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20617(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20618(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20619(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20620(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20621(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20622(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20623(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20624(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20625(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20626(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20627(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20628(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20629(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20630(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20631(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20632(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20633(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20634(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20635(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20636(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20637(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20638(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20639(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20640(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20641(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20642(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20643(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20644(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20645(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20646(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20647(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20648(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20649(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20650(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20651(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20652(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20653(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20654(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20655(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20656(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20657(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20658(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20659(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20660(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20661(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20662(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20663(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20664(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20665(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20666(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20667(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20668(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20669(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20670(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20671(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20672(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20673(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20674(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20675(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20676(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20677(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20678(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20679(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20680(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20681(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20682(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20683(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20684(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20685(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20686(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20687(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20688(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20689(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20690(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20691(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20692(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20693(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20694(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20695(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20696(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20697(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20698(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20699(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20700(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20701(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20702(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20703(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20704(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20705(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20706(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20707(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20708(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20709(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20710(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20711(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20712(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20713(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20714(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20715(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20716(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20717(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20718(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20719(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20720(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20721(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20722(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20723(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20724(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20725(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20726(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20727(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20728(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20729(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20730(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20731(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20732(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20733(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20734(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20735(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20736(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20737(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20738(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20739(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20740(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20741(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20742(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20743(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20744(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20745(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20746(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20747(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20748(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20749(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20750(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20751(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20752(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20753(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20754(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20755(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20756(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20757(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20758(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20759(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20760(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20761(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20762(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20763(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20764(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20765(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20766(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20767(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20768(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20769(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20770(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20771(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20772(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20773(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20774(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20775(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20776(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20777(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20778(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20779(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20780(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20781(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20782(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20783(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20784(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20785(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20786(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20787(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20788(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20789(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20790(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20791(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20792(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20793(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20794(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20795(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20796(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20797(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20798(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20799(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20800(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20801(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20802(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20803(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20804(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20805(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20806(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20807(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20808(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20809(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20810(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20811(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20812(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20813(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20814(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20815(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20816(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20817(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20818(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20819(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20820(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20821(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20822(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20823(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20824(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20825(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20826(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20827(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20828(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20829(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20830(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20831(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20832(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20833(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20834(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20835(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20836(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20837(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20838(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20839(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20840(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20841(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20842(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20843(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20844(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20845(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20846(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20847(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20848(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20849(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20850(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20851(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20852(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20853(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20854(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20855(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20856(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20857(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20858(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20859(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20860(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20861(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20862(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20863(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20864(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20865(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20866(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20867(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20868(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20869(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20870(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20871(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20872(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20873(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20874(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20875(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20876(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20877(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20878(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20879(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20880(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20881(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20882(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20883(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20884(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20885(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20886(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20887(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20888(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20889(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20890(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20891(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20892(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20893(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20894(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20895(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20896(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20897(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20898(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20899(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20900(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20901(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20902(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20903(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20904(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20905(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20906(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20907(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20908(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20909(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20910(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20911(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20912(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20913(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20914(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20915(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20916(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20917(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20918(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20919(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20920(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20921(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20922(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20923(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20924(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20925(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20926(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20927(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20928(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20929(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20930(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20931(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20932(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20933(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20934(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20935(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20936(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20937(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20938(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20939(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20940(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20941(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20942(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20943(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20944(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20945(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20946(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20947(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20948(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20949(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20950(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20951(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20952(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20953(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20954(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_20955(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_20956(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_20957(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_20958(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_20959(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_20960(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_20961(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_20962(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_20963(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_20964(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_20965(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_20966(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_20967(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_20968(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_20969(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_20970(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_20971(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_20972(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_20973(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_20974(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_20975(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_20976(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_20977(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_20978(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_20979(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_20980(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_20981(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_20982(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_20983(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_20984(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_20985(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_20986(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_20987(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_20988(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_20989(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_20990(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_20991(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_20992(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_20993(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_20994(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_20995(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_20996(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_20997(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_20998(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_20999(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21000(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21001(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21002(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21003(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21004(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21005(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21006(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21007(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21008(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21009(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21010(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21011(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21012(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21013(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21014(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21015(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21016(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21017(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21018(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21019(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21020(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21021(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21022(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21023(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21024(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21025(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21026(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21027(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21028(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21029(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21030(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21031(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21032(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21033(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21034(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21035(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21036(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21037(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21038(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21039(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21040(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21041(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21042(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21043(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21044(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21045(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21046(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21047(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21048(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21049(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21050(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21051(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21052(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21053(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21054(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21055(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21056(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21057(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21058(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21059(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21060(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21061(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21062(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21063(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21064(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21065(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21066(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21067(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21068(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21069(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21070(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21071(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21072(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21073(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21074(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21075(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21076(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21077(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21078(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21079(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21080(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21081(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21082(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21083(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21084(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21085(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21086(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21087(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21088(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21089(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21090(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21091(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21092(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21093(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21094(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21095(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21096(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21097(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21098(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21099(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21100(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21101(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21102(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21103(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21104(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21105(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21106(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21107(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21108(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21109(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21110(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21111(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21112(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21113(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21114(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21115(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21116(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21117(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21118(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21119(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21120(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21121(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21122(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21123(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21124(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21125(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21126(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21127(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21128(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21129(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21130(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21131(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21132(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21133(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21134(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21135(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21136(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21137(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21138(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21139(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21140(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21141(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21142(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21143(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21144(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21145(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21146(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21147(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21148(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21149(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21150(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21151(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21152(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21153(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21154(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21155(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21156(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21157(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21158(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21159(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21160(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21161(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21162(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21163(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21164(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21165(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21166(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21167(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21168(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21169(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21170(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21171(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21172(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21173(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21174(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21175(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21176(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21177(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21178(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21179(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21180(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21181(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21182(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21183(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21184(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21185(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21186(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21187(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21188(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21189(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21190(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21191(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21192(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21193(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21194(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21195(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21196(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21197(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21198(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21199(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21200(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21201(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21202(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21203(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21204(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21205(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21206(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21207(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21208(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21209(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21210(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21211(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21212(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21213(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21214(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21215(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21216(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21217(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21218(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21219(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21220(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21221(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21222(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21223(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21224(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21225(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21226(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21227(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21228(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21229(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21230(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21231(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21232(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21233(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21234(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21235(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21236(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21237(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21238(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21239(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21240(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21241(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21242(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21243(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21244(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21245(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21246(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21247(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21248(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21249(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21250(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21251(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21252(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21253(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21254(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21255(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21256(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21257(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21258(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21259(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21260(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21261(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21262(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21263(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21264(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21265(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21266(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21267(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21268(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21269(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21270(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21271(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21272(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21273(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21274(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21275(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21276(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21277(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21278(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21279(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21280(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21281(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21282(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21283(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21284(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21285(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21286(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21287(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21288(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21289(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21290(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21291(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21292(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21293(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21294(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21295(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21296(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21297(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21298(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21299(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21300(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21301(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21302(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21303(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21304(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21305(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21306(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21307(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21308(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21309(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21310(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21311(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21312(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21313(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21314(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21315(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21316(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21317(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21318(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21319(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21320(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21321(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21322(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21323(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21324(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21325(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21326(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21327(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21328(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21329(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21330(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21331(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21332(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21333(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21334(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21335(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21336(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21337(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21338(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21339(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21340(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21341(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21342(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21343(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21344(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21345(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21346(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21347(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21348(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21349(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21350(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21351(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21352(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21353(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21354(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21355(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21356(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21357(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21358(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21359(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21360(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21361(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21362(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21363(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21364(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21365(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21366(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21367(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21368(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21369(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21370(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21371(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21372(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21373(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21374(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21375(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21376(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21377(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21378(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21379(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21380(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21381(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21382(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21383(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21384(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21385(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21386(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21387(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21388(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21389(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21390(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21391(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21392(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21393(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21394(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21395(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21396(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21397(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21398(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21399(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21400(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21401(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21402(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21403(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21404(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21405(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21406(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21407(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21408(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21409(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21410(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21411(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21412(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21413(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21414(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21415(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21416(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21417(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21418(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21419(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21420(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21421(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21422(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21423(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21424(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21425(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21426(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21427(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21428(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21429(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21430(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21431(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21432(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21433(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21434(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21435(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21436(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21437(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21438(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21439(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21440(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21441(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21442(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21443(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21444(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21445(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21446(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21447(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21448(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21449(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21450(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21451(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21452(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21453(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21454(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21455(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21456(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21457(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21458(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21459(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21460(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21461(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21462(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21463(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21464(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21465(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21466(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21467(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21468(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21469(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21470(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21471(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21472(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21473(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21474(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21475(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21476(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21477(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21478(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21479(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21480(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21481(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21482(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21483(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21484(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21485(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21486(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21487(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21488(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21489(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21490(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21491(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21492(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21493(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21494(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21495(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21496(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21497(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21498(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21499(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21500(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21501(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21502(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21503(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21504(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21505(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21506(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21507(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21508(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21509(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21510(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21511(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21512(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21513(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21514(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21515(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21516(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21517(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21518(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21519(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21520(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21521(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21522(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21523(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21524(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21525(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21526(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21527(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21528(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21529(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21530(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21531(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21532(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21533(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21534(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21535(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21536(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21537(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21538(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21539(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21540(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21541(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21542(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21543(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21544(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21545(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21546(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21547(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21548(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21549(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21550(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21551(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21552(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21553(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21554(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21555(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21556(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21557(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21558(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21559(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21560(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21561(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21562(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21563(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21564(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21565(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21566(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21567(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21568(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21569(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21570(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21571(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21572(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21573(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21574(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21575(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21576(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21577(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21578(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21579(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21580(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21581(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21582(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21583(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21584(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21585(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21586(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21587(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21588(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21589(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21590(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21591(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21592(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21593(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21594(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21595(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21596(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21597(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21598(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21599(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21600(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21601(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21602(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21603(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21604(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21605(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21606(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21607(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21608(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21609(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21610(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21611(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21612(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21613(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21614(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21615(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21616(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21617(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21618(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21619(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21620(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21621(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21622(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21623(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21624(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21625(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21626(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21627(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21628(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21629(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21630(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21631(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21632(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21633(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21634(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21635(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21636(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21637(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21638(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21639(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21640(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21641(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21642(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21643(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21644(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21645(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21646(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21647(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21648(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21649(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21650(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21651(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21652(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21653(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21654(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21655(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21656(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21657(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21658(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21659(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21660(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21661(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21662(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21663(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21664(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21665(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21666(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21667(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21668(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21669(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21670(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21671(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21672(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21673(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21674(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21675(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21676(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21677(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21678(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21679(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21680(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21681(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21682(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21683(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21684(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21685(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21686(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21687(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21688(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21689(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21690(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21691(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21692(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21693(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21694(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21695(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21696(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21697(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21698(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21699(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21700(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21701(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21702(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21703(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21704(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21705(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21706(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21707(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21708(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21709(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21710(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21711(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21712(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21713(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21714(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21715(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21716(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21717(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21718(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21719(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21720(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21721(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21722(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21723(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21724(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21725(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21726(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21727(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21728(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21729(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21730(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21731(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21732(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21733(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21734(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21735(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21736(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21737(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21738(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21739(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21740(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21741(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21742(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21743(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21744(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21745(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21746(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21747(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21748(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21749(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21750(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21751(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21752(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21753(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21754(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21755(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21756(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21757(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21758(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21759(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21760(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21761(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21762(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21763(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21764(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21765(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21766(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21767(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21768(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21769(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21770(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21771(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21772(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21773(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21774(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21775(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21776(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21777(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21778(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21779(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21780(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21781(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21782(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21783(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21784(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21785(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21786(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21787(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21788(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21789(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21790(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21791(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21792(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21793(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21794(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21795(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21796(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21797(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21798(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21799(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21800(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21801(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21802(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21803(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21804(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21805(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21806(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21807(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21808(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21809(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21810(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21811(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21812(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21813(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21814(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21815(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21816(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21817(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21818(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21819(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21820(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21821(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21822(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21823(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21824(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21825(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21826(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21827(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21828(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21829(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21830(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21831(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21832(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21833(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21834(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21835(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21836(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21837(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21838(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21839(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21840(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21841(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21842(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21843(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21844(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21845(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21846(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21847(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21848(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21849(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21850(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21851(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21852(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21853(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21854(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21855(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21856(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21857(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21858(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21859(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21860(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21861(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21862(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21863(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21864(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21865(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21866(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21867(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21868(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21869(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21870(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21871(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21872(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21873(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21874(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21875(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21876(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21877(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21878(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21879(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21880(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21881(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21882(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21883(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21884(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21885(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21886(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21887(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21888(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21889(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21890(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21891(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21892(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21893(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21894(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21895(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21896(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21897(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21898(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21899(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21900(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21901(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21902(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21903(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21904(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21905(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21906(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21907(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21908(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21909(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21910(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21911(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21912(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21913(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21914(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21915(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21916(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21917(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21918(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21919(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21920(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21921(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21922(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21923(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21924(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21925(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21926(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21927(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21928(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21929(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21930(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21931(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21932(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21933(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21934(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21935(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21936(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21937(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21938(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21939(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21940(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21941(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21942(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21943(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21944(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21945(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21946(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21947(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21948(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21949(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21950(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21951(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21952(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21953(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21954(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_21955(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_21956(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_21957(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_21958(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_21959(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_21960(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_21961(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_21962(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_21963(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_21964(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_21965(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_21966(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_21967(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_21968(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_21969(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_21970(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_21971(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_21972(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_21973(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_21974(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_21975(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_21976(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_21977(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_21978(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_21979(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_21980(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_21981(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_21982(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_21983(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_21984(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_21985(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_21986(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_21987(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_21988(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_21989(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_21990(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_21991(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_21992(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_21993(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_21994(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_21995(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_21996(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_21997(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_21998(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_21999(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22000(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22001(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22002(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22003(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22004(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22005(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22006(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22007(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22008(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22009(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22010(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22011(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22012(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22013(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22014(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22015(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22016(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22017(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22018(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22019(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22020(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22021(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22022(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22023(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22024(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22025(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22026(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22027(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22028(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22029(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22030(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22031(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22032(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22033(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22034(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22035(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22036(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22037(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22038(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22039(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22040(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22041(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22042(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22043(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22044(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22045(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22046(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22047(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22048(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22049(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22050(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22051(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22052(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22053(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22054(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22055(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22056(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22057(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22058(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22059(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22060(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22061(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22062(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22063(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22064(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22065(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22066(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22067(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22068(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22069(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22070(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22071(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22072(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22073(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22074(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22075(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22076(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22077(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22078(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22079(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22080(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22081(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22082(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22083(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22084(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22085(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22086(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22087(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22088(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22089(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22090(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22091(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22092(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22093(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22094(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22095(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22096(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22097(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22098(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22099(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22100(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22101(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22102(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22103(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22104(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22105(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22106(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22107(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22108(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22109(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22110(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22111(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22112(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22113(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22114(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22115(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22116(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22117(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22118(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22119(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22120(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22121(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22122(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22123(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22124(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22125(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22126(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22127(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22128(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22129(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22130(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22131(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22132(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22133(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22134(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22135(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22136(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22137(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22138(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22139(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22140(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22141(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22142(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22143(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22144(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22145(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22146(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22147(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22148(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22149(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22150(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22151(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22152(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22153(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22154(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22155(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22156(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22157(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22158(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22159(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22160(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22161(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22162(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22163(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22164(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22165(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22166(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22167(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22168(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22169(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22170(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22171(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22172(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22173(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22174(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22175(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22176(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22177(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22178(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22179(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22180(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22181(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22182(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22183(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22184(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22185(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22186(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22187(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22188(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22189(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22190(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22191(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22192(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22193(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22194(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22195(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22196(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22197(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22198(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22199(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22200(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22201(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22202(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22203(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22204(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22205(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22206(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22207(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22208(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22209(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22210(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22211(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22212(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22213(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22214(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22215(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22216(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22217(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22218(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22219(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22220(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22221(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22222(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22223(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22224(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22225(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22226(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22227(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22228(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22229(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22230(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22231(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22232(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22233(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22234(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22235(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22236(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22237(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22238(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22239(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22240(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22241(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22242(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22243(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22244(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22245(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22246(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22247(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22248(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22249(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22250(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22251(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22252(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22253(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22254(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22255(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22256(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22257(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22258(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22259(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22260(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22261(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22262(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22263(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22264(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22265(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22266(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22267(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22268(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22269(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22270(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22271(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22272(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22273(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22274(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22275(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22276(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22277(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22278(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22279(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22280(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22281(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22282(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22283(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22284(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22285(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22286(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22287(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22288(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22289(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22290(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22291(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22292(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22293(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22294(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22295(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22296(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22297(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22298(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22299(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22300(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22301(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22302(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22303(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22304(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22305(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22306(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22307(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22308(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22309(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22310(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22311(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22312(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22313(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22314(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22315(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22316(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22317(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22318(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22319(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22320(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22321(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22322(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22323(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22324(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22325(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22326(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22327(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22328(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22329(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22330(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22331(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22332(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22333(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22334(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22335(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22336(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22337(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22338(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22339(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22340(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22341(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22342(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22343(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22344(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22345(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22346(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22347(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22348(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22349(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22350(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22351(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22352(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22353(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22354(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22355(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22356(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22357(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22358(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22359(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22360(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22361(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22362(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22363(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22364(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22365(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22366(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22367(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22368(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22369(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22370(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22371(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22372(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22373(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22374(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22375(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22376(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22377(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22378(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22379(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22380(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22381(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22382(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22383(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22384(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22385(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22386(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22387(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22388(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22389(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22390(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22391(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22392(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22393(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22394(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22395(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22396(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22397(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22398(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22399(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22400(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22401(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22402(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22403(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22404(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22405(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22406(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22407(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22408(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22409(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22410(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22411(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22412(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22413(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22414(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22415(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22416(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22417(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22418(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22419(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22420(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22421(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22422(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22423(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22424(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22425(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22426(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22427(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22428(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22429(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22430(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22431(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22432(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22433(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22434(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22435(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22436(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22437(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22438(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22439(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22440(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22441(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22442(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22443(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22444(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22445(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22446(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22447(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22448(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22449(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22450(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22451(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22452(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22453(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22454(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22455(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22456(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22457(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22458(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22459(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22460(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22461(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22462(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22463(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22464(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22465(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22466(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22467(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22468(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22469(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22470(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22471(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22472(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22473(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22474(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22475(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22476(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22477(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22478(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22479(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22480(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22481(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22482(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22483(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22484(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22485(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22486(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22487(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22488(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22489(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22490(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22491(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22492(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22493(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22494(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22495(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22496(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22497(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22498(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22499(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22500(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22501(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22502(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22503(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22504(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22505(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22506(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22507(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22508(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22509(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22510(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22511(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22512(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22513(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22514(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22515(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22516(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22517(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22518(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22519(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22520(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22521(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22522(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22523(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22524(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22525(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22526(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22527(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22528(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22529(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22530(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22531(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22532(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22533(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22534(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22535(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22536(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22537(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22538(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22539(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22540(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22541(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22542(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22543(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22544(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22545(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22546(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22547(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22548(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22549(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22550(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22551(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22552(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22553(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22554(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22555(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22556(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22557(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22558(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22559(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22560(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22561(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22562(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22563(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22564(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22565(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22566(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22567(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22568(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22569(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22570(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22571(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22572(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22573(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22574(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22575(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22576(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22577(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22578(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22579(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22580(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22581(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22582(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22583(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22584(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22585(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22586(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22587(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22588(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22589(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22590(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22591(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22592(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22593(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22594(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22595(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22596(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22597(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22598(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22599(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22600(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22601(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22602(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22603(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22604(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22605(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22606(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22607(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22608(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22609(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22610(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22611(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22612(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22613(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22614(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22615(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22616(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22617(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22618(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22619(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22620(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22621(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22622(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22623(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22624(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22625(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22626(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22627(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22628(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22629(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22630(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22631(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22632(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22633(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22634(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22635(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22636(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22637(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22638(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22639(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22640(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22641(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22642(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22643(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22644(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22645(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22646(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22647(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22648(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22649(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22650(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22651(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22652(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22653(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22654(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22655(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22656(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22657(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22658(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22659(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22660(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22661(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22662(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22663(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22664(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22665(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22666(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22667(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22668(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22669(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22670(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22671(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22672(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22673(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22674(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22675(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22676(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22677(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22678(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22679(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22680(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22681(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22682(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22683(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22684(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22685(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22686(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22687(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22688(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22689(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22690(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22691(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22692(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22693(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22694(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22695(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22696(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22697(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22698(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22699(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22700(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22701(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22702(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22703(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22704(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22705(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22706(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22707(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22708(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22709(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22710(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22711(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22712(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22713(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22714(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22715(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22716(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22717(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22718(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22719(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22720(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22721(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22722(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22723(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22724(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22725(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22726(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22727(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22728(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22729(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22730(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22731(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22732(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22733(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22734(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22735(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22736(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22737(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22738(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22739(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22740(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22741(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22742(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22743(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22744(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22745(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22746(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22747(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22748(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22749(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22750(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22751(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22752(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22753(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22754(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22755(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22756(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22757(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22758(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22759(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22760(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22761(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22762(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22763(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22764(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22765(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22766(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22767(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22768(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22769(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22770(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22771(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22772(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22773(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22774(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22775(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22776(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22777(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22778(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22779(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22780(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22781(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22782(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22783(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22784(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22785(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22786(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22787(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22788(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22789(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22790(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22791(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22792(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22793(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22794(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22795(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22796(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22797(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22798(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22799(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22800(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22801(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22802(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22803(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22804(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22805(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22806(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22807(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22808(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22809(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22810(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22811(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22812(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22813(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22814(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22815(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22816(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22817(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22818(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22819(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22820(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22821(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22822(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22823(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22824(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22825(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22826(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22827(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22828(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22829(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22830(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22831(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22832(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22833(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22834(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22835(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22836(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22837(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22838(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22839(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22840(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22841(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22842(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22843(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22844(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22845(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22846(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22847(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22848(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22849(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22850(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22851(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22852(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22853(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22854(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22855(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22856(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22857(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22858(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22859(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22860(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22861(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22862(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22863(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22864(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22865(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22866(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22867(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22868(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22869(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22870(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22871(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22872(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22873(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22874(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22875(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22876(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22877(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22878(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22879(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22880(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22881(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22882(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22883(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22884(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22885(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22886(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22887(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22888(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22889(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22890(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22891(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22892(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22893(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22894(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22895(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22896(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22897(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22898(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22899(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22900(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22901(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22902(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22903(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22904(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22905(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22906(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22907(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22908(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22909(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22910(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22911(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22912(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22913(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22914(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22915(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22916(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22917(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22918(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22919(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22920(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22921(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22922(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22923(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22924(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22925(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22926(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22927(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22928(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22929(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22930(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22931(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22932(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22933(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22934(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22935(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22936(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22937(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22938(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22939(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22940(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22941(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22942(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22943(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22944(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22945(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22946(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22947(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22948(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22949(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22950(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22951(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22952(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22953(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22954(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_22955(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_22956(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_22957(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_22958(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_22959(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_22960(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_22961(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_22962(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_22963(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_22964(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_22965(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_22966(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_22967(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_22968(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_22969(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_22970(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_22971(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_22972(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_22973(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_22974(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_22975(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_22976(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_22977(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_22978(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_22979(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_22980(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_22981(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_22982(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_22983(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_22984(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_22985(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_22986(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_22987(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_22988(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_22989(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_22990(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_22991(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_22992(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_22993(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_22994(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_22995(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_22996(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_22997(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_22998(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_22999(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23000(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23001(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23002(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23003(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23004(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23005(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23006(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23007(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23008(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23009(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23010(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23011(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23012(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23013(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23014(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23015(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23016(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23017(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23018(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23019(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23020(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23021(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23022(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23023(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23024(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23025(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23026(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23027(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23028(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23029(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23030(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23031(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23032(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23033(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23034(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23035(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23036(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23037(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23038(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23039(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23040(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23041(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23042(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23043(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23044(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23045(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23046(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23047(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23048(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23049(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23050(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23051(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23052(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23053(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23054(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23055(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23056(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23057(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23058(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23059(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23060(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23061(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23062(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23063(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23064(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23065(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23066(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23067(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23068(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23069(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23070(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23071(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23072(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23073(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23074(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23075(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23076(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23077(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23078(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23079(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23080(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23081(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23082(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23083(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23084(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23085(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23086(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23087(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23088(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23089(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23090(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23091(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23092(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23093(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23094(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23095(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23096(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23097(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23098(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23099(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23100(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23101(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23102(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23103(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23104(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23105(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23106(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23107(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23108(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23109(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23110(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23111(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23112(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23113(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23114(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23115(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23116(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23117(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23118(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23119(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23120(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23121(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23122(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23123(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23124(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23125(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23126(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23127(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23128(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23129(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23130(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23131(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23132(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23133(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23134(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23135(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23136(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23137(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23138(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23139(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23140(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23141(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23142(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23143(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23144(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23145(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23146(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23147(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23148(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23149(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23150(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23151(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23152(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23153(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23154(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23155(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23156(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23157(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23158(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23159(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23160(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23161(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23162(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23163(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23164(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23165(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23166(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23167(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23168(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23169(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23170(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23171(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23172(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23173(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23174(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23175(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23176(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23177(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23178(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23179(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23180(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23181(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23182(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23183(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23184(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23185(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23186(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23187(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23188(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23189(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23190(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23191(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23192(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23193(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23194(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23195(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23196(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23197(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23198(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23199(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23200(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23201(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23202(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23203(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23204(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23205(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23206(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23207(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23208(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23209(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23210(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23211(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23212(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23213(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23214(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23215(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23216(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23217(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23218(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23219(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23220(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23221(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23222(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23223(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23224(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23225(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23226(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23227(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23228(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23229(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23230(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23231(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23232(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23233(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23234(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23235(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23236(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23237(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23238(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23239(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23240(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23241(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23242(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23243(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23244(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23245(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23246(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23247(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23248(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23249(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23250(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23251(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23252(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23253(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23254(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23255(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23256(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23257(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23258(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23259(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23260(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23261(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23262(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23263(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23264(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23265(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23266(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23267(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23268(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23269(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23270(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23271(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23272(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23273(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23274(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23275(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23276(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23277(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23278(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23279(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23280(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23281(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23282(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23283(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23284(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23285(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23286(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23287(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23288(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23289(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23290(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23291(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23292(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23293(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23294(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23295(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23296(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23297(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23298(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23299(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23300(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23301(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23302(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23303(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23304(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23305(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23306(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23307(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23308(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23309(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23310(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23311(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23312(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23313(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23314(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23315(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23316(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23317(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23318(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23319(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23320(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23321(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23322(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23323(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23324(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23325(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23326(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23327(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23328(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23329(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23330(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23331(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23332(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23333(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23334(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23335(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23336(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23337(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23338(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23339(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23340(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23341(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23342(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23343(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23344(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23345(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23346(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23347(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23348(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23349(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23350(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23351(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23352(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23353(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23354(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23355(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23356(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23357(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23358(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23359(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23360(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23361(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23362(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23363(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23364(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23365(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23366(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23367(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23368(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23369(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23370(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23371(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23372(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23373(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23374(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23375(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23376(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23377(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23378(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23379(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23380(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23381(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23382(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23383(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23384(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23385(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23386(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23387(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23388(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23389(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23390(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23391(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23392(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23393(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23394(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23395(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23396(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23397(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23398(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23399(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23400(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23401(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23402(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23403(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23404(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23405(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23406(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23407(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23408(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23409(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23410(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23411(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23412(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23413(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23414(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23415(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23416(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23417(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23418(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23419(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23420(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23421(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23422(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23423(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23424(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23425(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23426(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23427(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23428(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23429(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23430(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23431(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23432(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23433(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23434(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23435(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23436(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23437(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23438(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23439(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23440(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23441(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23442(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23443(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23444(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23445(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23446(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23447(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23448(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23449(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23450(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23451(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23452(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23453(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23454(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23455(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23456(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23457(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23458(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23459(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23460(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23461(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23462(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23463(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23464(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23465(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23466(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23467(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23468(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23469(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23470(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23471(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23472(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23473(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23474(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23475(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23476(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23477(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23478(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23479(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23480(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23481(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23482(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23483(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23484(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23485(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23486(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23487(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23488(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23489(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23490(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23491(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23492(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23493(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23494(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23495(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23496(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23497(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23498(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23499(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23500(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23501(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23502(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23503(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23504(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23505(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23506(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23507(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23508(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23509(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23510(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23511(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23512(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23513(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23514(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23515(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23516(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23517(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23518(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23519(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23520(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23521(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23522(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23523(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23524(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23525(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23526(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23527(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23528(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23529(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23530(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23531(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23532(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23533(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23534(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23535(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23536(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23537(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23538(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23539(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23540(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23541(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23542(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23543(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23544(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23545(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23546(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23547(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23548(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23549(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23550(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23551(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23552(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23553(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23554(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23555(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23556(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23557(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23558(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23559(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23560(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23561(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23562(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23563(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23564(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23565(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23566(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23567(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23568(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23569(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23570(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23571(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23572(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23573(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23574(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23575(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23576(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23577(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23578(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23579(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23580(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23581(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23582(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23583(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23584(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23585(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23586(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23587(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23588(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23589(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23590(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23591(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23592(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23593(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23594(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23595(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23596(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23597(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23598(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23599(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23600(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23601(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23602(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23603(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23604(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23605(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23606(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23607(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23608(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23609(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23610(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23611(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23612(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23613(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23614(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23615(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23616(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23617(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23618(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23619(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23620(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23621(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23622(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23623(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23624(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23625(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23626(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23627(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23628(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23629(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23630(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23631(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23632(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23633(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23634(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23635(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23636(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23637(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23638(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23639(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23640(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23641(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23642(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23643(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23644(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23645(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23646(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23647(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23648(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23649(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23650(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23651(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23652(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23653(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23654(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23655(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23656(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23657(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23658(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23659(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23660(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23661(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23662(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23663(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23664(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23665(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23666(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23667(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23668(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23669(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23670(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23671(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23672(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23673(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23674(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23675(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23676(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23677(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23678(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23679(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23680(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23681(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23682(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23683(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23684(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23685(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23686(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23687(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23688(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23689(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23690(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23691(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23692(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23693(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23694(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23695(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23696(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23697(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23698(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23699(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23700(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23701(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23702(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23703(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23704(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23705(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23706(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23707(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23708(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23709(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23710(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23711(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23712(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23713(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23714(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23715(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23716(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23717(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23718(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23719(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23720(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23721(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23722(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23723(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23724(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23725(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23726(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23727(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23728(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23729(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23730(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23731(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23732(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23733(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23734(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23735(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23736(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23737(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23738(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23739(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23740(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23741(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23742(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23743(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23744(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23745(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23746(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23747(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23748(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23749(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23750(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23751(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23752(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23753(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23754(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23755(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23756(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23757(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23758(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23759(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23760(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23761(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23762(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23763(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23764(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23765(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23766(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23767(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23768(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23769(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23770(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23771(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23772(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23773(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23774(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23775(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23776(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23777(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23778(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23779(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23780(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23781(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23782(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23783(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23784(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23785(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23786(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23787(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23788(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23789(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23790(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23791(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23792(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23793(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23794(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23795(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23796(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23797(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23798(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23799(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23800(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23801(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23802(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23803(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23804(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23805(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23806(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23807(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23808(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23809(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23810(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23811(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23812(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23813(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23814(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23815(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23816(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23817(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23818(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23819(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23820(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23821(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23822(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23823(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23824(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23825(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23826(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23827(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23828(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23829(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23830(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23831(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23832(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23833(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23834(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23835(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23836(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23837(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23838(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23839(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23840(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23841(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23842(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23843(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23844(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23845(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23846(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23847(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23848(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23849(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23850(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23851(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23852(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23853(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23854(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23855(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23856(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23857(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23858(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23859(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23860(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23861(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23862(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23863(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23864(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23865(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23866(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23867(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23868(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23869(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23870(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23871(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23872(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23873(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23874(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23875(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23876(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23877(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23878(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23879(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23880(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23881(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23882(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23883(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23884(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23885(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23886(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23887(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23888(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23889(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23890(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23891(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23892(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23893(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23894(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23895(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23896(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23897(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23898(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23899(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23900(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23901(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23902(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23903(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23904(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23905(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23906(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23907(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23908(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23909(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23910(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23911(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23912(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23913(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23914(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23915(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23916(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23917(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23918(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23919(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23920(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23921(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23922(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23923(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23924(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23925(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23926(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23927(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23928(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23929(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23930(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23931(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23932(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23933(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23934(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23935(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23936(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23937(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23938(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23939(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23940(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23941(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23942(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23943(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23944(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23945(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23946(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23947(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23948(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23949(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23950(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23951(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23952(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23953(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23954(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_23955(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_23956(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_23957(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_23958(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_23959(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_23960(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_23961(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_23962(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_23963(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_23964(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_23965(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_23966(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_23967(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_23968(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_23969(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_23970(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_23971(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_23972(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_23973(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_23974(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_23975(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_23976(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_23977(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_23978(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_23979(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_23980(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_23981(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_23982(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_23983(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_23984(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_23985(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_23986(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_23987(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_23988(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_23989(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_23990(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_23991(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_23992(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_23993(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_23994(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_23995(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_23996(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_23997(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_23998(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_23999(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24000(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24001(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24002(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24003(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24004(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24005(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24006(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24007(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24008(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24009(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24010(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24011(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24012(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24013(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24014(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24015(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24016(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24017(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24018(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24019(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24020(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24021(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24022(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24023(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24024(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24025(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24026(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24027(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24028(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24029(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24030(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24031(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24032(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24033(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24034(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24035(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24036(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24037(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24038(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24039(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24040(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24041(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24042(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24043(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24044(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24045(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24046(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24047(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24048(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24049(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24050(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24051(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24052(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24053(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24054(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24055(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24056(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24057(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24058(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24059(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24060(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24061(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24062(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24063(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24064(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24065(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24066(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24067(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24068(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24069(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24070(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24071(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24072(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24073(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24074(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24075(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24076(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24077(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24078(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24079(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24080(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24081(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24082(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24083(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24084(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24085(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24086(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24087(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24088(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24089(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24090(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24091(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24092(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24093(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24094(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24095(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24096(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24097(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24098(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24099(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24100(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24101(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24102(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24103(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24104(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24105(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24106(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24107(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24108(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24109(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24110(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24111(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24112(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24113(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24114(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24115(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24116(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24117(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24118(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24119(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24120(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24121(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24122(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24123(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24124(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24125(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24126(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24127(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24128(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24129(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24130(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24131(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24132(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24133(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24134(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24135(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24136(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24137(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24138(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24139(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24140(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24141(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24142(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24143(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24144(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24145(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24146(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24147(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24148(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24149(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24150(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24151(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24152(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24153(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24154(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24155(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24156(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24157(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24158(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24159(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24160(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24161(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24162(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24163(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24164(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24165(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24166(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24167(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24168(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24169(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24170(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24171(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24172(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24173(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24174(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24175(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24176(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24177(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24178(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24179(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24180(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24181(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24182(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24183(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24184(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24185(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24186(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24187(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24188(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24189(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24190(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24191(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24192(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24193(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24194(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24195(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24196(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24197(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24198(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24199(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24200(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24201(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24202(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24203(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24204(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24205(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24206(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24207(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24208(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24209(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24210(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24211(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24212(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24213(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24214(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24215(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24216(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24217(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24218(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24219(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24220(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24221(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24222(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24223(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24224(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24225(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24226(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24227(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24228(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24229(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24230(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24231(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24232(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24233(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24234(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24235(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24236(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24237(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24238(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24239(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24240(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24241(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24242(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24243(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24244(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24245(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24246(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24247(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24248(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24249(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24250(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24251(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24252(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24253(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24254(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24255(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24256(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24257(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24258(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24259(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24260(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24261(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24262(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24263(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24264(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24265(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24266(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24267(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24268(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24269(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24270(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24271(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24272(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24273(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24274(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24275(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24276(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24277(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24278(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24279(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24280(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24281(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24282(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24283(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24284(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24285(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24286(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24287(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24288(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24289(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24290(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24291(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24292(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24293(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24294(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24295(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24296(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24297(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24298(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24299(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24300(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24301(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24302(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24303(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24304(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24305(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24306(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24307(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24308(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24309(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24310(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24311(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24312(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24313(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24314(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24315(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24316(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24317(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24318(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24319(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24320(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24321(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24322(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24323(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24324(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24325(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24326(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24327(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24328(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24329(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24330(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24331(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24332(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24333(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24334(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24335(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24336(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24337(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24338(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24339(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24340(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24341(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24342(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24343(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24344(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24345(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24346(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24347(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24348(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24349(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24350(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24351(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24352(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24353(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24354(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24355(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24356(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24357(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24358(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24359(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24360(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24361(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24362(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24363(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24364(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24365(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24366(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24367(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24368(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24369(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24370(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24371(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24372(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24373(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24374(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24375(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24376(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24377(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24378(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24379(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24380(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24381(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24382(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24383(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24384(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24385(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24386(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24387(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24388(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24389(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24390(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24391(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24392(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24393(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24394(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24395(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24396(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24397(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24398(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24399(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24400(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24401(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24402(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24403(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24404(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24405(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24406(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24407(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24408(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24409(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24410(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24411(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24412(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24413(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24414(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24415(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24416(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24417(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24418(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24419(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24420(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24421(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24422(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24423(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24424(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24425(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24426(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24427(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24428(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24429(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24430(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24431(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24432(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24433(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24434(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24435(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24436(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24437(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24438(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24439(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24440(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24441(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24442(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24443(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24444(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24445(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24446(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24447(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24448(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24449(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24450(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24451(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24452(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24453(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24454(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24455(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24456(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24457(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24458(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24459(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24460(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24461(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24462(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24463(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24464(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24465(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24466(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24467(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24468(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24469(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24470(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24471(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24472(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24473(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24474(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24475(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24476(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24477(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24478(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24479(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24480(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24481(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24482(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24483(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24484(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24485(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24486(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24487(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24488(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24489(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24490(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24491(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24492(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24493(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24494(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24495(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24496(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24497(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24498(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24499(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24500(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24501(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24502(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24503(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24504(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24505(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24506(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24507(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24508(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24509(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24510(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24511(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24512(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24513(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24514(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24515(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24516(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24517(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24518(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24519(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24520(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24521(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24522(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24523(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24524(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24525(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24526(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24527(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24528(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24529(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24530(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24531(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24532(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24533(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24534(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24535(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24536(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24537(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24538(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24539(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24540(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24541(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24542(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24543(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24544(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24545(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24546(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24547(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24548(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24549(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24550(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24551(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24552(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24553(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24554(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24555(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24556(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24557(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24558(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24559(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24560(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24561(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24562(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24563(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24564(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24565(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24566(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24567(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24568(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24569(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24570(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24571(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24572(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24573(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24574(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24575(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24576(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24577(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24578(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24579(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24580(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24581(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24582(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24583(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24584(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24585(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24586(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24587(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24588(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24589(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24590(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24591(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24592(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24593(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24594(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24595(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24596(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24597(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24598(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24599(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24600(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24601(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24602(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24603(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24604(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24605(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24606(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24607(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24608(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24609(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24610(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24611(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24612(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24613(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24614(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24615(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24616(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24617(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24618(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24619(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24620(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24621(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24622(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24623(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24624(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24625(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24626(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24627(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24628(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24629(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24630(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24631(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24632(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24633(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24634(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24635(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24636(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24637(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24638(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24639(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24640(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24641(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24642(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24643(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24644(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24645(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24646(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24647(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24648(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24649(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24650(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24651(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24652(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24653(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24654(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24655(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24656(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24657(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24658(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24659(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24660(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24661(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24662(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24663(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24664(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24665(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24666(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24667(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24668(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24669(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24670(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24671(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24672(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24673(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24674(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24675(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24676(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24677(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24678(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24679(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24680(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24681(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24682(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24683(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24684(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24685(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24686(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24687(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24688(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24689(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24690(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24691(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24692(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24693(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24694(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24695(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24696(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24697(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24698(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24699(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24700(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24701(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24702(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24703(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24704(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24705(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24706(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24707(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24708(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24709(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24710(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24711(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24712(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24713(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24714(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24715(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24716(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24717(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24718(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24719(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24720(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24721(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24722(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24723(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24724(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24725(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24726(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24727(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24728(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24729(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24730(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24731(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24732(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24733(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24734(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24735(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24736(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24737(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24738(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24739(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24740(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24741(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24742(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24743(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24744(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24745(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24746(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24747(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24748(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24749(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24750(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24751(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24752(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24753(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24754(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24755(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24756(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24757(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24758(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24759(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24760(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24761(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24762(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24763(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24764(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24765(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24766(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24767(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24768(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24769(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24770(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24771(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24772(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24773(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24774(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24775(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24776(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24777(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24778(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24779(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24780(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24781(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24782(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24783(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24784(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24785(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24786(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24787(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24788(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24789(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24790(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24791(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24792(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24793(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24794(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24795(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24796(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24797(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24798(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24799(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24800(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24801(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24802(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24803(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24804(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24805(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24806(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24807(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24808(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24809(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24810(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24811(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24812(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24813(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24814(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24815(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24816(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24817(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24818(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24819(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24820(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24821(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24822(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24823(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24824(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24825(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24826(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24827(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24828(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24829(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24830(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24831(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24832(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24833(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24834(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24835(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24836(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24837(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24838(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24839(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24840(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24841(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24842(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24843(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24844(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24845(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24846(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24847(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24848(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24849(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24850(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24851(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24852(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24853(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24854(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24855(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24856(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24857(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24858(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24859(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24860(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24861(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24862(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24863(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24864(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24865(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24866(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24867(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24868(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24869(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24870(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24871(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24872(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24873(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24874(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24875(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24876(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24877(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24878(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24879(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24880(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24881(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24882(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24883(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24884(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24885(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24886(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24887(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24888(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24889(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24890(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24891(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24892(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24893(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24894(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24895(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24896(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24897(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24898(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24899(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24900(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24901(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24902(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24903(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24904(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24905(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24906(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24907(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24908(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24909(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24910(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24911(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24912(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24913(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24914(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24915(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24916(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24917(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24918(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24919(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24920(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24921(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24922(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24923(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24924(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24925(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24926(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24927(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24928(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24929(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24930(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24931(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24932(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24933(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24934(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24935(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24936(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24937(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24938(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24939(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24940(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24941(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24942(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24943(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24944(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24945(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24946(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24947(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24948(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24949(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24950(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24951(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24952(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24953(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24954(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_24955(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_24956(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_24957(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_24958(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_24959(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_24960(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_24961(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_24962(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_24963(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_24964(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_24965(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_24966(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_24967(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_24968(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_24969(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_24970(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_24971(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_24972(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_24973(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_24974(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_24975(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_24976(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_24977(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_24978(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_24979(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_24980(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_24981(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_24982(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_24983(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_24984(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_24985(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_24986(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_24987(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_24988(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_24989(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_24990(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_24991(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_24992(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_24993(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_24994(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_24995(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_24996(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_24997(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_24998(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_24999(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25000(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25001(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25002(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25003(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25004(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25005(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25006(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25007(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25008(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25009(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25010(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25011(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25012(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25013(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25014(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25015(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25016(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25017(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25018(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25019(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25020(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25021(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25022(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25023(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25024(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25025(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25026(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25027(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25028(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25029(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25030(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25031(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25032(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25033(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25034(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25035(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25036(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25037(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25038(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25039(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25040(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25041(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25042(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25043(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25044(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25045(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25046(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25047(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25048(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25049(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25050(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25051(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25052(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25053(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25054(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25055(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25056(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25057(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25058(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25059(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25060(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25061(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25062(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25063(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25064(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25065(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25066(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25067(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25068(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25069(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25070(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25071(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25072(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25073(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25074(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25075(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25076(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25077(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25078(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25079(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25080(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25081(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25082(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25083(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25084(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25085(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25086(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25087(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25088(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25089(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25090(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25091(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25092(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25093(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25094(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25095(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25096(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25097(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25098(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25099(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25100(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25101(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25102(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25103(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25104(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25105(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25106(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25107(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25108(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25109(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25110(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25111(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25112(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25113(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25114(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25115(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25116(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25117(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25118(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25119(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25120(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25121(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25122(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25123(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25124(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25125(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25126(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25127(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25128(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25129(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25130(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25131(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25132(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25133(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25134(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25135(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25136(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25137(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25138(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25139(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25140(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25141(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25142(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25143(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25144(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25145(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25146(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25147(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25148(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25149(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25150(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25151(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25152(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25153(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25154(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25155(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25156(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25157(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25158(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25159(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25160(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25161(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25162(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25163(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25164(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25165(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25166(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25167(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25168(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25169(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25170(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25171(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25172(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25173(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25174(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25175(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25176(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25177(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25178(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25179(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25180(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25181(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25182(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25183(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25184(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25185(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25186(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25187(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25188(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25189(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25190(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25191(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25192(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25193(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25194(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25195(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25196(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25197(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25198(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25199(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25200(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25201(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25202(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25203(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25204(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25205(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25206(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25207(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25208(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25209(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25210(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25211(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25212(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25213(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25214(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25215(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25216(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25217(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25218(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25219(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25220(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25221(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25222(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25223(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25224(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25225(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25226(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25227(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25228(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25229(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25230(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25231(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25232(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25233(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25234(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25235(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25236(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25237(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25238(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25239(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25240(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25241(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25242(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25243(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25244(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25245(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25246(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25247(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25248(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25249(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25250(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25251(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25252(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25253(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25254(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25255(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25256(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25257(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25258(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25259(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25260(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25261(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25262(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25263(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25264(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25265(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25266(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25267(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25268(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25269(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25270(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25271(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25272(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25273(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25274(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25275(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25276(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25277(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25278(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25279(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25280(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25281(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25282(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25283(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25284(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25285(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25286(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25287(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25288(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25289(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25290(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25291(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25292(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25293(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25294(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25295(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25296(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25297(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25298(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25299(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25300(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25301(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25302(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25303(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25304(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25305(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25306(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25307(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25308(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25309(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25310(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25311(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25312(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25313(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25314(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25315(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25316(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25317(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25318(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25319(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25320(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25321(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25322(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25323(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25324(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25325(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25326(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25327(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25328(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25329(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25330(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25331(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25332(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25333(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25334(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25335(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25336(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25337(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25338(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25339(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25340(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25341(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25342(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25343(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25344(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25345(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25346(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25347(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25348(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25349(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25350(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25351(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25352(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25353(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25354(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25355(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25356(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25357(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25358(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25359(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25360(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25361(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25362(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25363(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25364(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25365(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25366(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25367(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25368(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25369(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25370(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25371(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25372(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25373(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25374(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25375(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25376(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25377(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25378(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25379(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25380(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25381(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25382(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25383(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25384(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25385(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25386(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25387(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25388(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25389(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25390(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25391(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25392(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25393(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25394(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25395(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25396(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25397(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25398(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25399(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25400(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25401(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25402(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25403(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25404(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25405(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25406(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25407(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25408(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25409(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25410(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25411(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25412(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25413(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25414(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25415(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25416(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25417(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25418(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25419(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25420(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25421(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25422(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25423(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25424(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25425(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25426(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25427(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25428(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25429(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25430(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25431(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25432(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25433(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25434(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25435(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25436(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25437(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25438(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25439(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25440(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25441(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25442(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25443(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25444(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25445(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25446(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25447(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25448(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25449(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25450(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25451(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25452(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25453(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25454(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25455(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25456(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25457(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25458(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25459(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25460(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25461(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25462(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25463(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25464(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25465(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25466(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25467(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25468(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25469(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25470(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25471(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25472(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25473(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25474(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25475(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25476(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25477(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25478(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25479(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25480(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25481(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25482(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25483(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25484(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25485(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25486(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25487(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25488(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25489(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25490(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25491(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25492(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25493(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25494(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25495(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25496(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25497(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25498(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25499(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25500(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25501(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25502(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25503(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25504(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25505(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25506(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25507(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25508(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25509(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25510(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25511(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25512(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25513(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25514(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25515(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25516(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25517(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25518(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25519(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25520(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25521(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25522(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25523(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25524(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25525(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25526(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25527(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25528(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25529(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25530(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25531(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25532(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25533(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25534(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25535(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25536(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25537(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25538(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25539(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25540(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25541(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25542(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25543(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25544(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25545(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25546(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25547(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25548(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25549(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25550(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25551(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25552(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25553(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25554(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25555(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25556(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25557(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25558(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25559(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25560(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25561(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25562(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25563(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25564(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25565(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25566(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25567(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25568(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25569(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25570(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25571(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25572(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25573(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25574(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25575(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25576(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25577(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25578(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25579(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25580(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25581(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25582(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25583(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25584(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25585(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25586(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25587(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25588(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25589(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25590(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25591(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25592(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25593(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25594(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25595(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25596(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25597(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25598(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25599(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25600(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25601(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25602(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25603(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25604(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25605(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25606(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25607(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25608(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25609(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25610(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25611(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25612(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25613(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25614(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25615(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25616(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25617(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25618(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25619(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25620(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25621(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25622(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25623(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25624(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25625(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25626(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25627(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25628(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25629(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25630(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25631(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25632(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25633(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25634(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25635(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25636(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25637(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25638(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25639(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25640(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25641(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25642(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25643(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25644(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25645(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25646(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25647(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25648(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25649(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25650(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25651(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25652(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25653(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25654(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25655(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25656(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25657(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25658(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25659(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25660(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25661(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25662(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25663(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25664(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25665(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25666(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25667(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25668(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25669(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25670(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25671(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25672(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25673(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25674(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25675(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25676(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25677(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25678(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25679(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25680(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25681(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25682(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25683(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25684(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25685(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25686(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25687(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25688(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25689(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25690(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25691(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25692(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25693(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25694(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25695(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25696(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25697(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25698(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25699(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25700(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25701(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25702(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25703(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25704(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25705(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25706(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25707(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25708(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25709(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25710(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25711(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25712(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25713(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25714(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25715(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25716(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25717(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25718(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25719(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25720(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25721(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25722(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25723(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25724(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25725(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25726(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25727(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25728(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25729(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25730(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25731(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25732(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25733(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25734(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25735(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25736(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25737(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25738(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25739(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25740(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25741(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25742(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25743(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25744(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25745(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25746(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25747(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25748(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25749(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25750(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25751(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25752(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25753(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25754(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25755(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25756(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25757(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25758(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25759(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25760(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25761(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25762(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25763(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25764(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25765(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25766(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25767(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25768(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25769(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25770(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25771(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25772(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25773(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25774(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25775(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25776(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25777(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25778(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25779(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25780(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25781(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25782(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25783(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25784(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25785(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25786(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25787(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25788(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25789(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25790(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25791(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25792(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25793(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25794(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25795(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25796(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25797(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25798(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25799(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25800(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25801(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25802(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25803(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25804(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25805(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25806(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25807(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25808(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25809(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25810(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25811(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25812(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25813(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25814(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25815(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25816(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25817(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25818(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25819(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25820(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25821(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25822(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25823(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25824(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25825(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25826(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25827(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25828(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25829(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25830(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25831(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25832(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25833(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25834(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25835(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25836(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25837(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25838(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25839(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25840(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25841(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25842(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25843(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25844(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25845(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25846(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25847(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25848(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25849(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25850(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25851(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25852(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25853(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25854(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25855(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25856(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25857(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25858(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25859(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25860(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25861(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25862(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25863(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25864(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25865(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25866(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25867(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25868(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25869(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25870(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25871(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25872(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25873(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25874(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25875(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25876(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25877(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25878(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25879(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25880(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25881(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25882(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25883(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25884(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25885(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25886(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25887(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25888(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25889(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25890(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25891(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25892(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25893(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25894(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25895(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25896(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25897(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25898(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25899(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25900(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25901(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25902(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25903(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25904(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25905(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25906(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25907(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25908(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25909(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25910(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25911(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25912(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25913(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25914(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25915(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25916(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25917(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25918(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25919(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25920(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25921(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25922(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25923(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25924(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25925(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25926(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25927(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25928(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25929(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25930(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25931(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25932(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25933(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25934(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25935(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25936(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25937(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25938(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25939(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25940(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25941(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25942(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25943(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25944(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25945(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25946(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25947(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25948(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25949(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25950(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25951(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25952(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25953(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25954(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_25955(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_25956(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_25957(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_25958(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_25959(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_25960(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_25961(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_25962(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_25963(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_25964(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_25965(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_25966(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_25967(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_25968(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_25969(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_25970(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_25971(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_25972(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_25973(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_25974(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_25975(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_25976(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_25977(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_25978(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_25979(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_25980(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_25981(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_25982(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_25983(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_25984(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_25985(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_25986(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_25987(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_25988(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_25989(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_25990(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_25991(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_25992(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_25993(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_25994(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_25995(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_25996(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_25997(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_25998(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_25999(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26000(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26001(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26002(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26003(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26004(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26005(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26006(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26007(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26008(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26009(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26010(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26011(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26012(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26013(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26014(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26015(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26016(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26017(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26018(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26019(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26020(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26021(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26022(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26023(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26024(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26025(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26026(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26027(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26028(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26029(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26030(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26031(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26032(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26033(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26034(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26035(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26036(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26037(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26038(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26039(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26040(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26041(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26042(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26043(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26044(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26045(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26046(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26047(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26048(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26049(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26050(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26051(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26052(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26053(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26054(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26055(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26056(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26057(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26058(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26059(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26060(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26061(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26062(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26063(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26064(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26065(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26066(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26067(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26068(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26069(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26070(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26071(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26072(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26073(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26074(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26075(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26076(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26077(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26078(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26079(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26080(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26081(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26082(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26083(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26084(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26085(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26086(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26087(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26088(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26089(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26090(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26091(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26092(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26093(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26094(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26095(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26096(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26097(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26098(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26099(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26100(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26101(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26102(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26103(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26104(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26105(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26106(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26107(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26108(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26109(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26110(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26111(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26112(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26113(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26114(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26115(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26116(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26117(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26118(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26119(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26120(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26121(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26122(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26123(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26124(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26125(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26126(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26127(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26128(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26129(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26130(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26131(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26132(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26133(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26134(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26135(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26136(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26137(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26138(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26139(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26140(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26141(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26142(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26143(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26144(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26145(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26146(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26147(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26148(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26149(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26150(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26151(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26152(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26153(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26154(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26155(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26156(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26157(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26158(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26159(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26160(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26161(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26162(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26163(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26164(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26165(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26166(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26167(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26168(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26169(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26170(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26171(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26172(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26173(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26174(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26175(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26176(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26177(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26178(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26179(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26180(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26181(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26182(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26183(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26184(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26185(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26186(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26187(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26188(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26189(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26190(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26191(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26192(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26193(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26194(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26195(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26196(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26197(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26198(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26199(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26200(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26201(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26202(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26203(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26204(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26205(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26206(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26207(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26208(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26209(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26210(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26211(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26212(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26213(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26214(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26215(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26216(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26217(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26218(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26219(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26220(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26221(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26222(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26223(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26224(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26225(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26226(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26227(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26228(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26229(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26230(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26231(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26232(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26233(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26234(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26235(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26236(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26237(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26238(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26239(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26240(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26241(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26242(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26243(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26244(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26245(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26246(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26247(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26248(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26249(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26250(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26251(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26252(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26253(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26254(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26255(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26256(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26257(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26258(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26259(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26260(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26261(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26262(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26263(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26264(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26265(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26266(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26267(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26268(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26269(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26270(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26271(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26272(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26273(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26274(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26275(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26276(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26277(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26278(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26279(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26280(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26281(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26282(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26283(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26284(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26285(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26286(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26287(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26288(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26289(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26290(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26291(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26292(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26293(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26294(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26295(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26296(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26297(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26298(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26299(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26300(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26301(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26302(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26303(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26304(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26305(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26306(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26307(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26308(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26309(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26310(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26311(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26312(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26313(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26314(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26315(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26316(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26317(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26318(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26319(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26320(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26321(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26322(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26323(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26324(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26325(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26326(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26327(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26328(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26329(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26330(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26331(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26332(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26333(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26334(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26335(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26336(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26337(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26338(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26339(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26340(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26341(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26342(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26343(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26344(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26345(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26346(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26347(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26348(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26349(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26350(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26351(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26352(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26353(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26354(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26355(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26356(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26357(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26358(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26359(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26360(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26361(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26362(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26363(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26364(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26365(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26366(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26367(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26368(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26369(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26370(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26371(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26372(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26373(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26374(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26375(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26376(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26377(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26378(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26379(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26380(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26381(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26382(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26383(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26384(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26385(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26386(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26387(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26388(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26389(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26390(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26391(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26392(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26393(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26394(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26395(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26396(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26397(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26398(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26399(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26400(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26401(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26402(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26403(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26404(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26405(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26406(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26407(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26408(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26409(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26410(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26411(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26412(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26413(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26414(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26415(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26416(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26417(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26418(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26419(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26420(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26421(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26422(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26423(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26424(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26425(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26426(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26427(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26428(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26429(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26430(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26431(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26432(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26433(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26434(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26435(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26436(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26437(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26438(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26439(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26440(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26441(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26442(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26443(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26444(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26445(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26446(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26447(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26448(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26449(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26450(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26451(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26452(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26453(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26454(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26455(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26456(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26457(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26458(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26459(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26460(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26461(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26462(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26463(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26464(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26465(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26466(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26467(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26468(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26469(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26470(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26471(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26472(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26473(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26474(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26475(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26476(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26477(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26478(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26479(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26480(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26481(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26482(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26483(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26484(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26485(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26486(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26487(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26488(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26489(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26490(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26491(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26492(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26493(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26494(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26495(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26496(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26497(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26498(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26499(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26500(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26501(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26502(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26503(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26504(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26505(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26506(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26507(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26508(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26509(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26510(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26511(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26512(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26513(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26514(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26515(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26516(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26517(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26518(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26519(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26520(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26521(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26522(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26523(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26524(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26525(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26526(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26527(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26528(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26529(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26530(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26531(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26532(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26533(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26534(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26535(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26536(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26537(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26538(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26539(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26540(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26541(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26542(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26543(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26544(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26545(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26546(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26547(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26548(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26549(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26550(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26551(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26552(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26553(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26554(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26555(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26556(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26557(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26558(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26559(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26560(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26561(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26562(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26563(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26564(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26565(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26566(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26567(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26568(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26569(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26570(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26571(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26572(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26573(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26574(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26575(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26576(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26577(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26578(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26579(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26580(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26581(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26582(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26583(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26584(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26585(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26586(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26587(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26588(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26589(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26590(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26591(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26592(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26593(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26594(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26595(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26596(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26597(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26598(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26599(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26600(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26601(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26602(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26603(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26604(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26605(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26606(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26607(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26608(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26609(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26610(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26611(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26612(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26613(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26614(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26615(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26616(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26617(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26618(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26619(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26620(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26621(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26622(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26623(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26624(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26625(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26626(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26627(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26628(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26629(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26630(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26631(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26632(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26633(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26634(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26635(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26636(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26637(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26638(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26639(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26640(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26641(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26642(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26643(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26644(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26645(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26646(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26647(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26648(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26649(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26650(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26651(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26652(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26653(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26654(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26655(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26656(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26657(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26658(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26659(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26660(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26661(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26662(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26663(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26664(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26665(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26666(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26667(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26668(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26669(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26670(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26671(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26672(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26673(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26674(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26675(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26676(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26677(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26678(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26679(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26680(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26681(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26682(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26683(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26684(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26685(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26686(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26687(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26688(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26689(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26690(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26691(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26692(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26693(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26694(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26695(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26696(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26697(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26698(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26699(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26700(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26701(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26702(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26703(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26704(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26705(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26706(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26707(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26708(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26709(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26710(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26711(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26712(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26713(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26714(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26715(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26716(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26717(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26718(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26719(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26720(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26721(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26722(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26723(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26724(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26725(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26726(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26727(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26728(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26729(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26730(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26731(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26732(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26733(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26734(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26735(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26736(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26737(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26738(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26739(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26740(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26741(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26742(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26743(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26744(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26745(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26746(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26747(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26748(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26749(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26750(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26751(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26752(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26753(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26754(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26755(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26756(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26757(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26758(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26759(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26760(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26761(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26762(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26763(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26764(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26765(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26766(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26767(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26768(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26769(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26770(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26771(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26772(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26773(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26774(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26775(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26776(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26777(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26778(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26779(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26780(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26781(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26782(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26783(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26784(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26785(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26786(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26787(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26788(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26789(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26790(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26791(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26792(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26793(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26794(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26795(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26796(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26797(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26798(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26799(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26800(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26801(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26802(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26803(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26804(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26805(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26806(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26807(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26808(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26809(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26810(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26811(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26812(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26813(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26814(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26815(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26816(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26817(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26818(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26819(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26820(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26821(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26822(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26823(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26824(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26825(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26826(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26827(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26828(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26829(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26830(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26831(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26832(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26833(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26834(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26835(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26836(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26837(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26838(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26839(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26840(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26841(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26842(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26843(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26844(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26845(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26846(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26847(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26848(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26849(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26850(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26851(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26852(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26853(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26854(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26855(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26856(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26857(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26858(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26859(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26860(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26861(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26862(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26863(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26864(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26865(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26866(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26867(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26868(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26869(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26870(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26871(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26872(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26873(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26874(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26875(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26876(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26877(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26878(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26879(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26880(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26881(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26882(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26883(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26884(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26885(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26886(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26887(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26888(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26889(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26890(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26891(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26892(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26893(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26894(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26895(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26896(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26897(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26898(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26899(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26900(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26901(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26902(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26903(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26904(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26905(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26906(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26907(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26908(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26909(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26910(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26911(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26912(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26913(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26914(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26915(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26916(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26917(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26918(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26919(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26920(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26921(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26922(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26923(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26924(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26925(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26926(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26927(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26928(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26929(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26930(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26931(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26932(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26933(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26934(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26935(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26936(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26937(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26938(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26939(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26940(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26941(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26942(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26943(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26944(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26945(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26946(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26947(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26948(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26949(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26950(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26951(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26952(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26953(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26954(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_26955(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_26956(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_26957(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_26958(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_26959(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_26960(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_26961(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_26962(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_26963(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_26964(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_26965(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_26966(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_26967(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_26968(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_26969(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_26970(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_26971(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_26972(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_26973(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_26974(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_26975(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_26976(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_26977(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_26978(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_26979(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_26980(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_26981(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_26982(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_26983(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_26984(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_26985(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_26986(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_26987(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_26988(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_26989(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_26990(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_26991(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_26992(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_26993(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_26994(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_26995(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_26996(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_26997(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_26998(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_26999(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27000(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27001(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27002(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27003(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27004(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27005(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27006(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27007(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27008(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27009(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27010(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27011(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27012(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27013(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27014(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27015(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27016(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27017(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27018(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27019(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27020(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27021(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27022(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27023(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27024(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27025(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27026(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27027(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27028(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27029(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27030(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27031(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27032(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27033(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27034(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27035(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27036(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27037(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27038(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27039(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27040(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27041(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27042(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27043(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27044(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27045(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27046(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27047(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27048(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27049(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27050(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27051(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27052(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27053(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27054(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27055(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27056(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27057(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27058(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27059(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27060(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27061(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27062(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27063(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27064(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27065(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27066(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27067(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27068(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27069(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27070(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27071(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27072(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27073(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27074(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27075(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27076(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27077(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27078(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27079(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27080(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27081(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27082(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27083(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27084(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27085(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27086(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27087(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27088(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27089(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27090(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27091(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27092(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27093(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27094(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27095(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27096(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27097(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27098(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27099(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27100(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27101(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27102(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27103(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27104(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27105(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27106(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27107(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27108(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27109(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27110(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27111(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27112(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27113(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27114(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27115(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27116(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27117(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27118(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27119(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27120(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27121(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27122(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27123(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27124(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27125(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27126(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27127(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27128(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27129(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27130(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27131(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27132(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27133(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27134(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27135(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27136(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27137(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27138(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27139(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27140(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27141(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27142(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27143(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27144(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27145(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27146(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27147(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27148(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27149(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27150(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27151(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27152(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27153(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27154(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27155(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27156(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27157(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27158(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27159(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27160(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27161(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27162(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27163(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27164(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27165(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27166(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27167(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27168(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27169(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27170(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27171(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27172(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27173(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27174(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27175(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27176(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27177(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27178(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27179(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27180(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27181(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27182(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27183(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27184(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27185(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27186(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27187(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27188(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27189(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27190(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27191(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27192(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27193(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27194(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27195(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27196(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27197(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27198(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27199(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27200(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27201(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27202(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27203(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27204(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27205(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27206(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27207(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27208(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27209(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27210(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27211(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27212(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27213(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27214(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27215(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27216(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27217(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27218(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27219(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27220(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27221(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27222(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27223(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27224(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27225(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27226(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27227(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27228(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27229(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27230(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27231(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27232(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27233(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27234(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27235(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27236(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27237(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27238(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27239(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27240(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27241(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27242(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27243(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27244(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27245(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27246(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27247(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27248(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27249(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27250(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27251(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27252(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27253(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27254(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27255(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27256(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27257(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27258(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27259(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27260(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27261(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27262(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27263(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27264(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27265(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27266(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27267(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27268(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27269(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27270(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27271(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27272(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27273(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27274(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27275(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27276(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27277(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27278(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27279(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27280(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27281(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27282(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27283(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27284(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27285(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27286(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27287(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27288(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27289(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27290(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27291(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27292(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27293(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27294(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27295(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27296(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27297(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27298(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27299(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27300(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27301(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27302(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27303(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27304(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27305(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27306(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27307(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27308(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27309(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27310(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27311(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27312(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27313(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27314(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27315(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27316(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27317(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27318(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27319(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27320(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27321(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27322(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27323(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27324(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27325(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27326(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27327(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27328(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27329(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27330(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27331(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27332(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27333(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27334(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27335(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27336(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27337(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27338(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27339(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27340(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27341(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27342(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27343(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27344(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27345(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27346(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27347(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27348(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27349(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27350(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27351(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27352(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27353(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27354(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27355(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27356(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27357(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27358(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27359(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27360(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27361(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27362(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27363(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27364(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27365(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27366(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27367(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27368(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27369(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27370(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27371(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27372(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27373(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27374(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27375(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27376(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27377(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27378(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27379(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27380(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27381(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27382(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27383(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27384(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27385(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27386(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27387(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27388(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27389(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27390(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27391(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27392(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27393(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27394(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27395(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27396(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27397(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27398(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27399(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27400(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27401(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27402(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27403(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27404(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27405(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27406(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27407(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27408(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27409(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27410(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27411(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27412(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27413(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27414(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27415(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27416(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27417(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27418(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27419(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27420(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27421(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27422(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27423(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27424(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27425(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27426(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27427(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27428(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27429(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27430(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27431(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27432(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27433(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27434(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27435(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27436(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27437(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27438(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27439(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27440(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27441(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27442(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27443(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27444(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27445(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27446(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27447(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27448(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27449(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27450(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27451(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27452(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27453(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27454(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27455(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27456(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27457(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27458(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27459(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27460(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27461(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27462(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27463(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27464(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27465(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27466(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27467(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27468(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27469(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27470(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27471(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27472(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27473(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27474(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27475(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27476(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27477(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27478(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27479(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27480(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27481(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27482(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27483(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27484(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27485(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27486(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27487(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27488(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27489(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27490(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27491(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27492(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27493(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27494(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27495(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27496(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27497(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27498(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27499(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27500(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27501(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27502(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27503(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27504(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27505(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27506(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27507(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27508(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27509(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27510(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27511(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27512(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27513(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27514(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27515(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27516(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27517(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27518(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27519(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27520(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27521(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27522(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27523(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27524(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27525(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27526(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27527(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27528(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27529(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27530(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27531(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27532(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27533(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27534(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27535(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27536(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27537(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27538(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27539(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27540(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27541(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27542(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27543(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27544(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27545(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27546(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27547(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27548(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27549(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27550(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27551(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27552(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27553(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27554(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27555(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27556(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27557(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27558(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27559(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27560(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27561(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27562(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27563(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27564(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27565(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27566(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27567(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27568(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27569(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27570(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27571(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27572(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27573(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27574(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27575(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27576(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27577(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27578(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27579(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27580(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27581(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27582(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27583(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27584(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27585(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27586(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27587(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27588(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27589(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27590(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27591(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27592(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27593(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27594(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27595(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27596(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27597(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27598(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27599(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27600(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27601(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27602(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27603(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27604(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27605(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27606(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27607(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27608(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27609(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27610(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27611(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27612(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27613(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27614(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27615(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27616(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27617(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27618(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27619(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27620(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27621(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27622(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27623(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27624(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27625(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27626(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27627(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27628(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27629(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27630(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27631(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27632(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27633(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27634(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27635(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27636(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27637(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27638(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27639(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27640(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27641(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27642(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27643(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27644(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27645(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27646(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27647(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27648(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27649(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27650(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27651(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27652(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27653(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27654(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27655(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27656(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27657(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27658(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27659(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27660(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27661(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27662(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27663(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27664(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27665(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27666(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27667(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27668(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27669(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27670(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27671(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27672(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27673(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27674(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27675(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27676(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27677(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27678(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27679(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27680(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27681(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27682(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27683(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27684(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27685(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27686(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27687(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27688(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27689(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27690(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27691(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27692(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27693(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27694(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27695(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27696(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27697(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27698(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27699(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27700(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27701(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27702(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27703(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27704(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27705(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27706(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27707(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27708(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27709(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27710(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27711(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27712(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27713(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27714(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27715(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27716(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27717(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27718(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27719(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27720(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27721(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27722(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27723(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27724(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27725(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27726(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27727(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27728(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27729(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27730(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27731(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27732(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27733(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27734(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27735(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27736(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27737(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27738(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27739(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27740(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27741(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27742(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27743(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27744(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27745(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27746(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27747(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27748(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27749(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27750(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27751(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27752(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27753(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27754(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27755(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27756(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27757(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27758(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27759(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27760(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27761(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27762(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27763(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27764(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27765(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27766(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27767(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27768(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27769(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27770(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27771(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27772(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27773(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27774(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27775(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27776(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27777(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27778(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27779(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27780(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27781(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27782(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27783(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27784(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27785(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27786(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27787(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27788(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27789(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27790(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27791(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27792(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27793(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27794(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27795(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27796(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27797(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27798(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27799(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27800(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27801(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27802(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27803(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27804(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27805(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27806(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27807(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27808(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27809(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27810(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27811(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27812(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27813(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27814(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27815(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27816(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27817(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27818(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27819(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27820(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27821(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27822(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27823(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27824(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27825(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27826(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27827(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27828(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27829(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27830(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27831(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27832(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27833(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27834(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27835(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27836(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27837(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27838(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27839(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27840(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27841(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27842(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27843(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27844(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27845(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27846(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27847(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27848(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27849(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27850(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27851(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27852(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27853(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27854(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27855(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27856(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27857(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27858(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27859(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27860(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27861(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27862(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27863(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27864(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27865(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27866(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27867(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27868(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27869(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27870(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27871(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27872(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27873(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27874(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27875(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27876(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27877(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27878(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27879(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27880(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27881(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27882(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27883(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27884(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27885(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27886(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27887(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27888(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27889(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27890(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27891(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27892(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27893(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27894(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27895(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27896(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27897(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27898(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27899(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27900(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27901(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27902(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27903(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27904(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27905(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27906(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27907(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27908(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27909(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27910(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27911(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27912(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27913(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27914(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27915(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27916(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27917(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27918(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27919(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27920(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27921(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27922(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27923(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27924(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27925(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27926(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27927(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27928(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27929(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27930(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27931(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27932(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27933(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27934(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27935(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27936(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27937(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27938(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27939(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27940(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27941(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27942(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27943(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27944(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27945(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27946(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27947(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27948(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27949(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27950(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27951(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27952(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27953(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27954(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_27955(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)
def rule_27956(world):
    world.seed_bank = torch.clamp(world.seed_bank + 0.001*world.sediment,0,2)
def rule_27957(world):
    world.soil_carbon = torch.clamp(world.soil_carbon - 0.001*world.salinity,0,2)
def rule_27958(world):
    world.surface_ice = torch.clamp(world.surface_ice + 0.001*world.algae*world.algae,0,2)
def rule_27959(world):
    world.temperature = torch.clamp(world.temperature + 0.001*(world.organic_matter-world.temperature),0,2)
def rule_27960(world):
    world.surface_water = torch.clamp(world.surface_water + 0.001*torch.tanh(world.deadwood),0,2)
def rule_27961(world):
    world.humidity = torch.clamp(world.humidity + 0.001*world.pollinators,0,2)
def rule_27962(world):
    world.cloud = torch.clamp(world.cloud - 0.001*world.flowers,0,2)
def rule_27963(world):
    world.rain = torch.clamp(world.rain + 0.001*world.seed_bank*world.seed_bank,0,2)
def rule_27964(world):
    world.soil_moisture = torch.clamp(world.soil_moisture + 0.001*(world.soil_carbon-world.soil_moisture),0,2)
def rule_27965(world):
    world.runoff = torch.clamp(world.runoff + 0.001*torch.tanh(world.surface_ice),0,2)
def rule_27966(world):
    world.wind_x = torch.clamp(world.wind_x + 0.001*world.temperature,0,2)
def rule_27967(world):
    world.wind_y = torch.clamp(world.wind_y - 0.001*world.surface_water,0,2)
def rule_27968(world):
    world.vegetation = torch.clamp(world.vegetation + 0.001*world.humidity*world.humidity,0,2)
def rule_27969(world):
    world.biomass = torch.clamp(world.biomass + 0.001*(world.cloud-world.biomass),0,2)
def rule_27970(world):
    world.herbivore = torch.clamp(world.herbivore + 0.001*torch.tanh(world.rain),0,2)
def rule_27971(world):
    world.predator = torch.clamp(world.predator + 0.001*world.soil_moisture,0,2)
def rule_27972(world):
    world.carrion = torch.clamp(world.carrion - 0.001*world.runoff,0,2)
def rule_27973(world):
    world.nutrients = torch.clamp(world.nutrients + 0.001*world.wind_x*world.wind_x,0,2)
def rule_27974(world):
    world.decomposition_rate = torch.clamp(world.decomposition_rate + 0.001*(world.wind_y-world.decomposition_rate),0,2)
def rule_27975(world):
    world.oxygen = torch.clamp(world.oxygen + 0.001*torch.tanh(world.vegetation),0,2)
def rule_27976(world):
    world.co2 = torch.clamp(world.co2 + 0.001*world.biomass,0,2)
def rule_27977(world):
    world.photosynthesis_factor = torch.clamp(world.photosynthesis_factor - 0.001*world.herbivore,0,2)
def rule_27978(world):
    world.ice = torch.clamp(world.ice + 0.001*world.predator*world.predator,0,2)
def rule_27979(world):
    world.evaporation = torch.clamp(world.evaporation + 0.001*(world.carrion-world.evaporation),0,2)
def rule_27980(world):
    world.detritus = torch.clamp(world.detritus + 0.001*torch.tanh(world.nutrients),0,2)
def rule_27981(world):
    world.methane = torch.clamp(world.methane + 0.001*world.decomposition_rate,0,2)
def rule_27982(world):
    world.pathogen_load = torch.clamp(world.pathogen_load - 0.001*world.oxygen,0,2)
def rule_27983(world):
    world.biodiversity = torch.clamp(world.biodiversity + 0.001*world.co2*world.co2,0,2)
def rule_27984(world):
    world.habitat_stress = torch.clamp(world.habitat_stress + 0.001*(world.photosynthesis_factor-world.habitat_stress),0,2)
def rule_27985(world):
    world.erosion = torch.clamp(world.erosion + 0.001*torch.tanh(world.ice),0,2)
def rule_27986(world):
    world.soil_depth = torch.clamp(world.soil_depth + 0.001*world.evaporation,0,2)
def rule_27987(world):
    world.root_density = torch.clamp(world.root_density - 0.001*world.detritus,0,2)
def rule_27988(world):
    world.wetland = torch.clamp(world.wetland + 0.001*world.methane*world.methane,0,2)
def rule_27989(world):
    world.carbon_storage = torch.clamp(world.carbon_storage + 0.001*(world.pathogen_load-world.carbon_storage),0,2)
def rule_27990(world):
    world.fire_risk = torch.clamp(world.fire_risk + 0.001*torch.tanh(world.biodiversity),0,2)
def rule_27991(world):
    world.ash = torch.clamp(world.ash + 0.001*world.habitat_stress,0,2)
def rule_27992(world):
    world.snowpack = torch.clamp(world.snowpack - 0.001*world.erosion,0,2)
def rule_27993(world):
    world.groundwater = torch.clamp(world.groundwater + 0.001*world.soil_depth*world.soil_depth,0,2)
def rule_27994(world):
    world.sediment = torch.clamp(world.sediment + 0.001*(world.root_density-world.sediment),0,2)
def rule_27995(world):
    world.salinity = torch.clamp(world.salinity + 0.001*torch.tanh(world.wetland),0,2)
def rule_27996(world):
    world.algae = torch.clamp(world.algae + 0.001*world.carbon_storage,0,2)
def rule_27997(world):
    world.organic_matter = torch.clamp(world.organic_matter - 0.001*world.fire_risk,0,2)
def rule_27998(world):
    world.deadwood = torch.clamp(world.deadwood + 0.001*world.ash*world.ash,0,2)
def rule_27999(world):
    world.pollinators = torch.clamp(world.pollinators + 0.001*(world.snowpack-world.pollinators),0,2)
def rule_28000(world):
    world.flowers = torch.clamp(world.flowers + 0.001*torch.tanh(world.groundwater),0,2)

RULES=[rule_20001,rule_20002,rule_20003,rule_20004,rule_20005,rule_20006,rule_20007,rule_20008,rule_20009,rule_20010,rule_20011,rule_20012,rule_20013,rule_20014,rule_20015,rule_20016,rule_20017,rule_20018,rule_20019,rule_20020,rule_20021,rule_20022,rule_20023,rule_20024,rule_20025,rule_20026,rule_20027,rule_20028,rule_20029,rule_20030,rule_20031,rule_20032,rule_20033,rule_20034,rule_20035,rule_20036,rule_20037,rule_20038,rule_20039,rule_20040,rule_20041,rule_20042,rule_20043,rule_20044,rule_20045,rule_20046,rule_20047,rule_20048,rule_20049,rule_20050,rule_20051,rule_20052,rule_20053,rule_20054,rule_20055,rule_20056,rule_20057,rule_20058,rule_20059,rule_20060,rule_20061,rule_20062,rule_20063,rule_20064,rule_20065,rule_20066,rule_20067,rule_20068,rule_20069,rule_20070,rule_20071,rule_20072,rule_20073,rule_20074,rule_20075,rule_20076,rule_20077,rule_20078,rule_20079,rule_20080,rule_20081,rule_20082,rule_20083,rule_20084,rule_20085,rule_20086,rule_20087,rule_20088,rule_20089,rule_20090,rule_20091,rule_20092,rule_20093,rule_20094,rule_20095,rule_20096,rule_20097,rule_20098,rule_20099,rule_20100,rule_20101,rule_20102,rule_20103,rule_20104,rule_20105,rule_20106,rule_20107,rule_20108,rule_20109,rule_20110,rule_20111,rule_20112,rule_20113,rule_20114,rule_20115,rule_20116,rule_20117,rule_20118,rule_20119,rule_20120,rule_20121,rule_20122,rule_20123,rule_20124,rule_20125,rule_20126,rule_20127,rule_20128,rule_20129,rule_20130,rule_20131,rule_20132,rule_20133,rule_20134,rule_20135,rule_20136,rule_20137,rule_20138,rule_20139,rule_20140,rule_20141,rule_20142,rule_20143,rule_20144,rule_20145,rule_20146,rule_20147,rule_20148,rule_20149,rule_20150,rule_20151,rule_20152,rule_20153,rule_20154,rule_20155,rule_20156,rule_20157,rule_20158,rule_20159,rule_20160,rule_20161,rule_20162,rule_20163,rule_20164,rule_20165,rule_20166,rule_20167,rule_20168,rule_20169,rule_20170,rule_20171,rule_20172,rule_20173,rule_20174,rule_20175,rule_20176,rule_20177,rule_20178,rule_20179,rule_20180,rule_20181,rule_20182,rule_20183,rule_20184,rule_20185,rule_20186,rule_20187,rule_20188,rule_20189,rule_20190,rule_20191,rule_20192,rule_20193,rule_20194,rule_20195,rule_20196,rule_20197,rule_20198,rule_20199,rule_20200,rule_20201,rule_20202,rule_20203,rule_20204,rule_20205,rule_20206,rule_20207,rule_20208,rule_20209,rule_20210,rule_20211,rule_20212,rule_20213,rule_20214,rule_20215,rule_20216,rule_20217,rule_20218,rule_20219,rule_20220,rule_20221,rule_20222,rule_20223,rule_20224,rule_20225,rule_20226,rule_20227,rule_20228,rule_20229,rule_20230,rule_20231,rule_20232,rule_20233,rule_20234,rule_20235,rule_20236,rule_20237,rule_20238,rule_20239,rule_20240,rule_20241,rule_20242,rule_20243,rule_20244,rule_20245,rule_20246,rule_20247,rule_20248,rule_20249,rule_20250,rule_20251,rule_20252,rule_20253,rule_20254,rule_20255,rule_20256,rule_20257,rule_20258,rule_20259,rule_20260,rule_20261,rule_20262,rule_20263,rule_20264,rule_20265,rule_20266,rule_20267,rule_20268,rule_20269,rule_20270,rule_20271,rule_20272,rule_20273,rule_20274,rule_20275,rule_20276,rule_20277,rule_20278,rule_20279,rule_20280,rule_20281,rule_20282,rule_20283,rule_20284,rule_20285,rule_20286,rule_20287,rule_20288,rule_20289,rule_20290,rule_20291,rule_20292,rule_20293,rule_20294,rule_20295,rule_20296,rule_20297,rule_20298,rule_20299,rule_20300,rule_20301,rule_20302,rule_20303,rule_20304,rule_20305,rule_20306,rule_20307,rule_20308,rule_20309,rule_20310,rule_20311,rule_20312,rule_20313,rule_20314,rule_20315,rule_20316,rule_20317,rule_20318,rule_20319,rule_20320,rule_20321,rule_20322,rule_20323,rule_20324,rule_20325,rule_20326,rule_20327,rule_20328,rule_20329,rule_20330,rule_20331,rule_20332,rule_20333,rule_20334,rule_20335,rule_20336,rule_20337,rule_20338,rule_20339,rule_20340,rule_20341,rule_20342,rule_20343,rule_20344,rule_20345,rule_20346,rule_20347,rule_20348,rule_20349,rule_20350,rule_20351,rule_20352,rule_20353,rule_20354,rule_20355,rule_20356,rule_20357,rule_20358,rule_20359,rule_20360,rule_20361,rule_20362,rule_20363,rule_20364,rule_20365,rule_20366,rule_20367,rule_20368,rule_20369,rule_20370,rule_20371,rule_20372,rule_20373,rule_20374,rule_20375,rule_20376,rule_20377,rule_20378,rule_20379,rule_20380,rule_20381,rule_20382,rule_20383,rule_20384,rule_20385,rule_20386,rule_20387,rule_20388,rule_20389,rule_20390,rule_20391,rule_20392,rule_20393,rule_20394,rule_20395,rule_20396,rule_20397,rule_20398,rule_20399,rule_20400,rule_20401,rule_20402,rule_20403,rule_20404,rule_20405,rule_20406,rule_20407,rule_20408,rule_20409,rule_20410,rule_20411,rule_20412,rule_20413,rule_20414,rule_20415,rule_20416,rule_20417,rule_20418,rule_20419,rule_20420,rule_20421,rule_20422,rule_20423,rule_20424,rule_20425,rule_20426,rule_20427,rule_20428,rule_20429,rule_20430,rule_20431,rule_20432,rule_20433,rule_20434,rule_20435,rule_20436,rule_20437,rule_20438,rule_20439,rule_20440,rule_20441,rule_20442,rule_20443,rule_20444,rule_20445,rule_20446,rule_20447,rule_20448,rule_20449,rule_20450,rule_20451,rule_20452,rule_20453,rule_20454,rule_20455,rule_20456,rule_20457,rule_20458,rule_20459,rule_20460,rule_20461,rule_20462,rule_20463,rule_20464,rule_20465,rule_20466,rule_20467,rule_20468,rule_20469,rule_20470,rule_20471,rule_20472,rule_20473,rule_20474,rule_20475,rule_20476,rule_20477,rule_20478,rule_20479,rule_20480,rule_20481,rule_20482,rule_20483,rule_20484,rule_20485,rule_20486,rule_20487,rule_20488,rule_20489,rule_20490,rule_20491,rule_20492,rule_20493,rule_20494,rule_20495,rule_20496,rule_20497,rule_20498,rule_20499,rule_20500,rule_20501,rule_20502,rule_20503,rule_20504,rule_20505,rule_20506,rule_20507,rule_20508,rule_20509,rule_20510,rule_20511,rule_20512,rule_20513,rule_20514,rule_20515,rule_20516,rule_20517,rule_20518,rule_20519,rule_20520,rule_20521,rule_20522,rule_20523,rule_20524,rule_20525,rule_20526,rule_20527,rule_20528,rule_20529,rule_20530,rule_20531,rule_20532,rule_20533,rule_20534,rule_20535,rule_20536,rule_20537,rule_20538,rule_20539,rule_20540,rule_20541,rule_20542,rule_20543,rule_20544,rule_20545,rule_20546,rule_20547,rule_20548,rule_20549,rule_20550,rule_20551,rule_20552,rule_20553,rule_20554,rule_20555,rule_20556,rule_20557,rule_20558,rule_20559,rule_20560,rule_20561,rule_20562,rule_20563,rule_20564,rule_20565,rule_20566,rule_20567,rule_20568,rule_20569,rule_20570,rule_20571,rule_20572,rule_20573,rule_20574,rule_20575,rule_20576,rule_20577,rule_20578,rule_20579,rule_20580,rule_20581,rule_20582,rule_20583,rule_20584,rule_20585,rule_20586,rule_20587,rule_20588,rule_20589,rule_20590,rule_20591,rule_20592,rule_20593,rule_20594,rule_20595,rule_20596,rule_20597,rule_20598,rule_20599,rule_20600,rule_20601,rule_20602,rule_20603,rule_20604,rule_20605,rule_20606,rule_20607,rule_20608,rule_20609,rule_20610,rule_20611,rule_20612,rule_20613,rule_20614,rule_20615,rule_20616,rule_20617,rule_20618,rule_20619,rule_20620,rule_20621,rule_20622,rule_20623,rule_20624,rule_20625,rule_20626,rule_20627,rule_20628,rule_20629,rule_20630,rule_20631,rule_20632,rule_20633,rule_20634,rule_20635,rule_20636,rule_20637,rule_20638,rule_20639,rule_20640,rule_20641,rule_20642,rule_20643,rule_20644,rule_20645,rule_20646,rule_20647,rule_20648,rule_20649,rule_20650,rule_20651,rule_20652,rule_20653,rule_20654,rule_20655,rule_20656,rule_20657,rule_20658,rule_20659,rule_20660,rule_20661,rule_20662,rule_20663,rule_20664,rule_20665,rule_20666,rule_20667,rule_20668,rule_20669,rule_20670,rule_20671,rule_20672,rule_20673,rule_20674,rule_20675,rule_20676,rule_20677,rule_20678,rule_20679,rule_20680,rule_20681,rule_20682,rule_20683,rule_20684,rule_20685,rule_20686,rule_20687,rule_20688,rule_20689,rule_20690,rule_20691,rule_20692,rule_20693,rule_20694,rule_20695,rule_20696,rule_20697,rule_20698,rule_20699,rule_20700,rule_20701,rule_20702,rule_20703,rule_20704,rule_20705,rule_20706,rule_20707,rule_20708,rule_20709,rule_20710,rule_20711,rule_20712,rule_20713,rule_20714,rule_20715,rule_20716,rule_20717,rule_20718,rule_20719,rule_20720,rule_20721,rule_20722,rule_20723,rule_20724,rule_20725,rule_20726,rule_20727,rule_20728,rule_20729,rule_20730,rule_20731,rule_20732,rule_20733,rule_20734,rule_20735,rule_20736,rule_20737,rule_20738,rule_20739,rule_20740,rule_20741,rule_20742,rule_20743,rule_20744,rule_20745,rule_20746,rule_20747,rule_20748,rule_20749,rule_20750,rule_20751,rule_20752,rule_20753,rule_20754,rule_20755,rule_20756,rule_20757,rule_20758,rule_20759,rule_20760,rule_20761,rule_20762,rule_20763,rule_20764,rule_20765,rule_20766,rule_20767,rule_20768,rule_20769,rule_20770,rule_20771,rule_20772,rule_20773,rule_20774,rule_20775,rule_20776,rule_20777,rule_20778,rule_20779,rule_20780,rule_20781,rule_20782,rule_20783,rule_20784,rule_20785,rule_20786,rule_20787,rule_20788,rule_20789,rule_20790,rule_20791,rule_20792,rule_20793,rule_20794,rule_20795,rule_20796,rule_20797,rule_20798,rule_20799,rule_20800,rule_20801,rule_20802,rule_20803,rule_20804,rule_20805,rule_20806,rule_20807,rule_20808,rule_20809,rule_20810,rule_20811,rule_20812,rule_20813,rule_20814,rule_20815,rule_20816,rule_20817,rule_20818,rule_20819,rule_20820,rule_20821,rule_20822,rule_20823,rule_20824,rule_20825,rule_20826,rule_20827,rule_20828,rule_20829,rule_20830,rule_20831,rule_20832,rule_20833,rule_20834,rule_20835,rule_20836,rule_20837,rule_20838,rule_20839,rule_20840,rule_20841,rule_20842,rule_20843,rule_20844,rule_20845,rule_20846,rule_20847,rule_20848,rule_20849,rule_20850,rule_20851,rule_20852,rule_20853,rule_20854,rule_20855,rule_20856,rule_20857,rule_20858,rule_20859,rule_20860,rule_20861,rule_20862,rule_20863,rule_20864,rule_20865,rule_20866,rule_20867,rule_20868,rule_20869,rule_20870,rule_20871,rule_20872,rule_20873,rule_20874,rule_20875,rule_20876,rule_20877,rule_20878,rule_20879,rule_20880,rule_20881,rule_20882,rule_20883,rule_20884,rule_20885,rule_20886,rule_20887,rule_20888,rule_20889,rule_20890,rule_20891,rule_20892,rule_20893,rule_20894,rule_20895,rule_20896,rule_20897,rule_20898,rule_20899,rule_20900,rule_20901,rule_20902,rule_20903,rule_20904,rule_20905,rule_20906,rule_20907,rule_20908,rule_20909,rule_20910,rule_20911,rule_20912,rule_20913,rule_20914,rule_20915,rule_20916,rule_20917,rule_20918,rule_20919,rule_20920,rule_20921,rule_20922,rule_20923,rule_20924,rule_20925,rule_20926,rule_20927,rule_20928,rule_20929,rule_20930,rule_20931,rule_20932,rule_20933,rule_20934,rule_20935,rule_20936,rule_20937,rule_20938,rule_20939,rule_20940,rule_20941,rule_20942,rule_20943,rule_20944,rule_20945,rule_20946,rule_20947,rule_20948,rule_20949,rule_20950,rule_20951,rule_20952,rule_20953,rule_20954,rule_20955,rule_20956,rule_20957,rule_20958,rule_20959,rule_20960,rule_20961,rule_20962,rule_20963,rule_20964,rule_20965,rule_20966,rule_20967,rule_20968,rule_20969,rule_20970,rule_20971,rule_20972,rule_20973,rule_20974,rule_20975,rule_20976,rule_20977,rule_20978,rule_20979,rule_20980,rule_20981,rule_20982,rule_20983,rule_20984,rule_20985,rule_20986,rule_20987,rule_20988,rule_20989,rule_20990,rule_20991,rule_20992,rule_20993,rule_20994,rule_20995,rule_20996,rule_20997,rule_20998,rule_20999,rule_21000,rule_21001,rule_21002,rule_21003,rule_21004,rule_21005,rule_21006,rule_21007,rule_21008,rule_21009,rule_21010,rule_21011,rule_21012,rule_21013,rule_21014,rule_21015,rule_21016,rule_21017,rule_21018,rule_21019,rule_21020,rule_21021,rule_21022,rule_21023,rule_21024,rule_21025,rule_21026,rule_21027,rule_21028,rule_21029,rule_21030,rule_21031,rule_21032,rule_21033,rule_21034,rule_21035,rule_21036,rule_21037,rule_21038,rule_21039,rule_21040,rule_21041,rule_21042,rule_21043,rule_21044,rule_21045,rule_21046,rule_21047,rule_21048,rule_21049,rule_21050,rule_21051,rule_21052,rule_21053,rule_21054,rule_21055,rule_21056,rule_21057,rule_21058,rule_21059,rule_21060,rule_21061,rule_21062,rule_21063,rule_21064,rule_21065,rule_21066,rule_21067,rule_21068,rule_21069,rule_21070,rule_21071,rule_21072,rule_21073,rule_21074,rule_21075,rule_21076,rule_21077,rule_21078,rule_21079,rule_21080,rule_21081,rule_21082,rule_21083,rule_21084,rule_21085,rule_21086,rule_21087,rule_21088,rule_21089,rule_21090,rule_21091,rule_21092,rule_21093,rule_21094,rule_21095,rule_21096,rule_21097,rule_21098,rule_21099,rule_21100,rule_21101,rule_21102,rule_21103,rule_21104,rule_21105,rule_21106,rule_21107,rule_21108,rule_21109,rule_21110,rule_21111,rule_21112,rule_21113,rule_21114,rule_21115,rule_21116,rule_21117,rule_21118,rule_21119,rule_21120,rule_21121,rule_21122,rule_21123,rule_21124,rule_21125,rule_21126,rule_21127,rule_21128,rule_21129,rule_21130,rule_21131,rule_21132,rule_21133,rule_21134,rule_21135,rule_21136,rule_21137,rule_21138,rule_21139,rule_21140,rule_21141,rule_21142,rule_21143,rule_21144,rule_21145,rule_21146,rule_21147,rule_21148,rule_21149,rule_21150,rule_21151,rule_21152,rule_21153,rule_21154,rule_21155,rule_21156,rule_21157,rule_21158,rule_21159,rule_21160,rule_21161,rule_21162,rule_21163,rule_21164,rule_21165,rule_21166,rule_21167,rule_21168,rule_21169,rule_21170,rule_21171,rule_21172,rule_21173,rule_21174,rule_21175,rule_21176,rule_21177,rule_21178,rule_21179,rule_21180,rule_21181,rule_21182,rule_21183,rule_21184,rule_21185,rule_21186,rule_21187,rule_21188,rule_21189,rule_21190,rule_21191,rule_21192,rule_21193,rule_21194,rule_21195,rule_21196,rule_21197,rule_21198,rule_21199,rule_21200,rule_21201,rule_21202,rule_21203,rule_21204,rule_21205,rule_21206,rule_21207,rule_21208,rule_21209,rule_21210,rule_21211,rule_21212,rule_21213,rule_21214,rule_21215,rule_21216,rule_21217,rule_21218,rule_21219,rule_21220,rule_21221,rule_21222,rule_21223,rule_21224,rule_21225,rule_21226,rule_21227,rule_21228,rule_21229,rule_21230,rule_21231,rule_21232,rule_21233,rule_21234,rule_21235,rule_21236,rule_21237,rule_21238,rule_21239,rule_21240,rule_21241,rule_21242,rule_21243,rule_21244,rule_21245,rule_21246,rule_21247,rule_21248,rule_21249,rule_21250,rule_21251,rule_21252,rule_21253,rule_21254,rule_21255,rule_21256,rule_21257,rule_21258,rule_21259,rule_21260,rule_21261,rule_21262,rule_21263,rule_21264,rule_21265,rule_21266,rule_21267,rule_21268,rule_21269,rule_21270,rule_21271,rule_21272,rule_21273,rule_21274,rule_21275,rule_21276,rule_21277,rule_21278,rule_21279,rule_21280,rule_21281,rule_21282,rule_21283,rule_21284,rule_21285,rule_21286,rule_21287,rule_21288,rule_21289,rule_21290,rule_21291,rule_21292,rule_21293,rule_21294,rule_21295,rule_21296,rule_21297,rule_21298,rule_21299,rule_21300,rule_21301,rule_21302,rule_21303,rule_21304,rule_21305,rule_21306,rule_21307,rule_21308,rule_21309,rule_21310,rule_21311,rule_21312,rule_21313,rule_21314,rule_21315,rule_21316,rule_21317,rule_21318,rule_21319,rule_21320,rule_21321,rule_21322,rule_21323,rule_21324,rule_21325,rule_21326,rule_21327,rule_21328,rule_21329,rule_21330,rule_21331,rule_21332,rule_21333,rule_21334,rule_21335,rule_21336,rule_21337,rule_21338,rule_21339,rule_21340,rule_21341,rule_21342,rule_21343,rule_21344,rule_21345,rule_21346,rule_21347,rule_21348,rule_21349,rule_21350,rule_21351,rule_21352,rule_21353,rule_21354,rule_21355,rule_21356,rule_21357,rule_21358,rule_21359,rule_21360,rule_21361,rule_21362,rule_21363,rule_21364,rule_21365,rule_21366,rule_21367,rule_21368,rule_21369,rule_21370,rule_21371,rule_21372,rule_21373,rule_21374,rule_21375,rule_21376,rule_21377,rule_21378,rule_21379,rule_21380,rule_21381,rule_21382,rule_21383,rule_21384,rule_21385,rule_21386,rule_21387,rule_21388,rule_21389,rule_21390,rule_21391,rule_21392,rule_21393,rule_21394,rule_21395,rule_21396,rule_21397,rule_21398,rule_21399,rule_21400,rule_21401,rule_21402,rule_21403,rule_21404,rule_21405,rule_21406,rule_21407,rule_21408,rule_21409,rule_21410,rule_21411,rule_21412,rule_21413,rule_21414,rule_21415,rule_21416,rule_21417,rule_21418,rule_21419,rule_21420,rule_21421,rule_21422,rule_21423,rule_21424,rule_21425,rule_21426,rule_21427,rule_21428,rule_21429,rule_21430,rule_21431,rule_21432,rule_21433,rule_21434,rule_21435,rule_21436,rule_21437,rule_21438,rule_21439,rule_21440,rule_21441,rule_21442,rule_21443,rule_21444,rule_21445,rule_21446,rule_21447,rule_21448,rule_21449,rule_21450,rule_21451,rule_21452,rule_21453,rule_21454,rule_21455,rule_21456,rule_21457,rule_21458,rule_21459,rule_21460,rule_21461,rule_21462,rule_21463,rule_21464,rule_21465,rule_21466,rule_21467,rule_21468,rule_21469,rule_21470,rule_21471,rule_21472,rule_21473,rule_21474,rule_21475,rule_21476,rule_21477,rule_21478,rule_21479,rule_21480,rule_21481,rule_21482,rule_21483,rule_21484,rule_21485,rule_21486,rule_21487,rule_21488,rule_21489,rule_21490,rule_21491,rule_21492,rule_21493,rule_21494,rule_21495,rule_21496,rule_21497,rule_21498,rule_21499,rule_21500,rule_21501,rule_21502,rule_21503,rule_21504,rule_21505,rule_21506,rule_21507,rule_21508,rule_21509,rule_21510,rule_21511,rule_21512,rule_21513,rule_21514,rule_21515,rule_21516,rule_21517,rule_21518,rule_21519,rule_21520,rule_21521,rule_21522,rule_21523,rule_21524,rule_21525,rule_21526,rule_21527,rule_21528,rule_21529,rule_21530,rule_21531,rule_21532,rule_21533,rule_21534,rule_21535,rule_21536,rule_21537,rule_21538,rule_21539,rule_21540,rule_21541,rule_21542,rule_21543,rule_21544,rule_21545,rule_21546,rule_21547,rule_21548,rule_21549,rule_21550,rule_21551,rule_21552,rule_21553,rule_21554,rule_21555,rule_21556,rule_21557,rule_21558,rule_21559,rule_21560,rule_21561,rule_21562,rule_21563,rule_21564,rule_21565,rule_21566,rule_21567,rule_21568,rule_21569,rule_21570,rule_21571,rule_21572,rule_21573,rule_21574,rule_21575,rule_21576,rule_21577,rule_21578,rule_21579,rule_21580,rule_21581,rule_21582,rule_21583,rule_21584,rule_21585,rule_21586,rule_21587,rule_21588,rule_21589,rule_21590,rule_21591,rule_21592,rule_21593,rule_21594,rule_21595,rule_21596,rule_21597,rule_21598,rule_21599,rule_21600,rule_21601,rule_21602,rule_21603,rule_21604,rule_21605,rule_21606,rule_21607,rule_21608,rule_21609,rule_21610,rule_21611,rule_21612,rule_21613,rule_21614,rule_21615,rule_21616,rule_21617,rule_21618,rule_21619,rule_21620,rule_21621,rule_21622,rule_21623,rule_21624,rule_21625,rule_21626,rule_21627,rule_21628,rule_21629,rule_21630,rule_21631,rule_21632,rule_21633,rule_21634,rule_21635,rule_21636,rule_21637,rule_21638,rule_21639,rule_21640,rule_21641,rule_21642,rule_21643,rule_21644,rule_21645,rule_21646,rule_21647,rule_21648,rule_21649,rule_21650,rule_21651,rule_21652,rule_21653,rule_21654,rule_21655,rule_21656,rule_21657,rule_21658,rule_21659,rule_21660,rule_21661,rule_21662,rule_21663,rule_21664,rule_21665,rule_21666,rule_21667,rule_21668,rule_21669,rule_21670,rule_21671,rule_21672,rule_21673,rule_21674,rule_21675,rule_21676,rule_21677,rule_21678,rule_21679,rule_21680,rule_21681,rule_21682,rule_21683,rule_21684,rule_21685,rule_21686,rule_21687,rule_21688,rule_21689,rule_21690,rule_21691,rule_21692,rule_21693,rule_21694,rule_21695,rule_21696,rule_21697,rule_21698,rule_21699,rule_21700,rule_21701,rule_21702,rule_21703,rule_21704,rule_21705,rule_21706,rule_21707,rule_21708,rule_21709,rule_21710,rule_21711,rule_21712,rule_21713,rule_21714,rule_21715,rule_21716,rule_21717,rule_21718,rule_21719,rule_21720,rule_21721,rule_21722,rule_21723,rule_21724,rule_21725,rule_21726,rule_21727,rule_21728,rule_21729,rule_21730,rule_21731,rule_21732,rule_21733,rule_21734,rule_21735,rule_21736,rule_21737,rule_21738,rule_21739,rule_21740,rule_21741,rule_21742,rule_21743,rule_21744,rule_21745,rule_21746,rule_21747,rule_21748,rule_21749,rule_21750,rule_21751,rule_21752,rule_21753,rule_21754,rule_21755,rule_21756,rule_21757,rule_21758,rule_21759,rule_21760,rule_21761,rule_21762,rule_21763,rule_21764,rule_21765,rule_21766,rule_21767,rule_21768,rule_21769,rule_21770,rule_21771,rule_21772,rule_21773,rule_21774,rule_21775,rule_21776,rule_21777,rule_21778,rule_21779,rule_21780,rule_21781,rule_21782,rule_21783,rule_21784,rule_21785,rule_21786,rule_21787,rule_21788,rule_21789,rule_21790,rule_21791,rule_21792,rule_21793,rule_21794,rule_21795,rule_21796,rule_21797,rule_21798,rule_21799,rule_21800,rule_21801,rule_21802,rule_21803,rule_21804,rule_21805,rule_21806,rule_21807,rule_21808,rule_21809,rule_21810,rule_21811,rule_21812,rule_21813,rule_21814,rule_21815,rule_21816,rule_21817,rule_21818,rule_21819,rule_21820,rule_21821,rule_21822,rule_21823,rule_21824,rule_21825,rule_21826,rule_21827,rule_21828,rule_21829,rule_21830,rule_21831,rule_21832,rule_21833,rule_21834,rule_21835,rule_21836,rule_21837,rule_21838,rule_21839,rule_21840,rule_21841,rule_21842,rule_21843,rule_21844,rule_21845,rule_21846,rule_21847,rule_21848,rule_21849,rule_21850,rule_21851,rule_21852,rule_21853,rule_21854,rule_21855,rule_21856,rule_21857,rule_21858,rule_21859,rule_21860,rule_21861,rule_21862,rule_21863,rule_21864,rule_21865,rule_21866,rule_21867,rule_21868,rule_21869,rule_21870,rule_21871,rule_21872,rule_21873,rule_21874,rule_21875,rule_21876,rule_21877,rule_21878,rule_21879,rule_21880,rule_21881,rule_21882,rule_21883,rule_21884,rule_21885,rule_21886,rule_21887,rule_21888,rule_21889,rule_21890,rule_21891,rule_21892,rule_21893,rule_21894,rule_21895,rule_21896,rule_21897,rule_21898,rule_21899,rule_21900,rule_21901,rule_21902,rule_21903,rule_21904,rule_21905,rule_21906,rule_21907,rule_21908,rule_21909,rule_21910,rule_21911,rule_21912,rule_21913,rule_21914,rule_21915,rule_21916,rule_21917,rule_21918,rule_21919,rule_21920,rule_21921,rule_21922,rule_21923,rule_21924,rule_21925,rule_21926,rule_21927,rule_21928,rule_21929,rule_21930,rule_21931,rule_21932,rule_21933,rule_21934,rule_21935,rule_21936,rule_21937,rule_21938,rule_21939,rule_21940,rule_21941,rule_21942,rule_21943,rule_21944,rule_21945,rule_21946,rule_21947,rule_21948,rule_21949,rule_21950,rule_21951,rule_21952,rule_21953,rule_21954,rule_21955,rule_21956,rule_21957,rule_21958,rule_21959,rule_21960,rule_21961,rule_21962,rule_21963,rule_21964,rule_21965,rule_21966,rule_21967,rule_21968,rule_21969,rule_21970,rule_21971,rule_21972,rule_21973,rule_21974,rule_21975,rule_21976,rule_21977,rule_21978,rule_21979,rule_21980,rule_21981,rule_21982,rule_21983,rule_21984,rule_21985,rule_21986,rule_21987,rule_21988,rule_21989,rule_21990,rule_21991,rule_21992,rule_21993,rule_21994,rule_21995,rule_21996,rule_21997,rule_21998,rule_21999,rule_22000,rule_22001,rule_22002,rule_22003,rule_22004,rule_22005,rule_22006,rule_22007,rule_22008,rule_22009,rule_22010,rule_22011,rule_22012,rule_22013,rule_22014,rule_22015,rule_22016,rule_22017,rule_22018,rule_22019,rule_22020,rule_22021,rule_22022,rule_22023,rule_22024,rule_22025,rule_22026,rule_22027,rule_22028,rule_22029,rule_22030,rule_22031,rule_22032,rule_22033,rule_22034,rule_22035,rule_22036,rule_22037,rule_22038,rule_22039,rule_22040,rule_22041,rule_22042,rule_22043,rule_22044,rule_22045,rule_22046,rule_22047,rule_22048,rule_22049,rule_22050,rule_22051,rule_22052,rule_22053,rule_22054,rule_22055,rule_22056,rule_22057,rule_22058,rule_22059,rule_22060,rule_22061,rule_22062,rule_22063,rule_22064,rule_22065,rule_22066,rule_22067,rule_22068,rule_22069,rule_22070,rule_22071,rule_22072,rule_22073,rule_22074,rule_22075,rule_22076,rule_22077,rule_22078,rule_22079,rule_22080,rule_22081,rule_22082,rule_22083,rule_22084,rule_22085,rule_22086,rule_22087,rule_22088,rule_22089,rule_22090,rule_22091,rule_22092,rule_22093,rule_22094,rule_22095,rule_22096,rule_22097,rule_22098,rule_22099,rule_22100,rule_22101,rule_22102,rule_22103,rule_22104,rule_22105,rule_22106,rule_22107,rule_22108,rule_22109,rule_22110,rule_22111,rule_22112,rule_22113,rule_22114,rule_22115,rule_22116,rule_22117,rule_22118,rule_22119,rule_22120,rule_22121,rule_22122,rule_22123,rule_22124,rule_22125,rule_22126,rule_22127,rule_22128,rule_22129,rule_22130,rule_22131,rule_22132,rule_22133,rule_22134,rule_22135,rule_22136,rule_22137,rule_22138,rule_22139,rule_22140,rule_22141,rule_22142,rule_22143,rule_22144,rule_22145,rule_22146,rule_22147,rule_22148,rule_22149,rule_22150,rule_22151,rule_22152,rule_22153,rule_22154,rule_22155,rule_22156,rule_22157,rule_22158,rule_22159,rule_22160,rule_22161,rule_22162,rule_22163,rule_22164,rule_22165,rule_22166,rule_22167,rule_22168,rule_22169,rule_22170,rule_22171,rule_22172,rule_22173,rule_22174,rule_22175,rule_22176,rule_22177,rule_22178,rule_22179,rule_22180,rule_22181,rule_22182,rule_22183,rule_22184,rule_22185,rule_22186,rule_22187,rule_22188,rule_22189,rule_22190,rule_22191,rule_22192,rule_22193,rule_22194,rule_22195,rule_22196,rule_22197,rule_22198,rule_22199,rule_22200,rule_22201,rule_22202,rule_22203,rule_22204,rule_22205,rule_22206,rule_22207,rule_22208,rule_22209,rule_22210,rule_22211,rule_22212,rule_22213,rule_22214,rule_22215,rule_22216,rule_22217,rule_22218,rule_22219,rule_22220,rule_22221,rule_22222,rule_22223,rule_22224,rule_22225,rule_22226,rule_22227,rule_22228,rule_22229,rule_22230,rule_22231,rule_22232,rule_22233,rule_22234,rule_22235,rule_22236,rule_22237,rule_22238,rule_22239,rule_22240,rule_22241,rule_22242,rule_22243,rule_22244,rule_22245,rule_22246,rule_22247,rule_22248,rule_22249,rule_22250,rule_22251,rule_22252,rule_22253,rule_22254,rule_22255,rule_22256,rule_22257,rule_22258,rule_22259,rule_22260,rule_22261,rule_22262,rule_22263,rule_22264,rule_22265,rule_22266,rule_22267,rule_22268,rule_22269,rule_22270,rule_22271,rule_22272,rule_22273,rule_22274,rule_22275,rule_22276,rule_22277,rule_22278,rule_22279,rule_22280,rule_22281,rule_22282,rule_22283,rule_22284,rule_22285,rule_22286,rule_22287,rule_22288,rule_22289,rule_22290,rule_22291,rule_22292,rule_22293,rule_22294,rule_22295,rule_22296,rule_22297,rule_22298,rule_22299,rule_22300,rule_22301,rule_22302,rule_22303,rule_22304,rule_22305,rule_22306,rule_22307,rule_22308,rule_22309,rule_22310,rule_22311,rule_22312,rule_22313,rule_22314,rule_22315,rule_22316,rule_22317,rule_22318,rule_22319,rule_22320,rule_22321,rule_22322,rule_22323,rule_22324,rule_22325,rule_22326,rule_22327,rule_22328,rule_22329,rule_22330,rule_22331,rule_22332,rule_22333,rule_22334,rule_22335,rule_22336,rule_22337,rule_22338,rule_22339,rule_22340,rule_22341,rule_22342,rule_22343,rule_22344,rule_22345,rule_22346,rule_22347,rule_22348,rule_22349,rule_22350,rule_22351,rule_22352,rule_22353,rule_22354,rule_22355,rule_22356,rule_22357,rule_22358,rule_22359,rule_22360,rule_22361,rule_22362,rule_22363,rule_22364,rule_22365,rule_22366,rule_22367,rule_22368,rule_22369,rule_22370,rule_22371,rule_22372,rule_22373,rule_22374,rule_22375,rule_22376,rule_22377,rule_22378,rule_22379,rule_22380,rule_22381,rule_22382,rule_22383,rule_22384,rule_22385,rule_22386,rule_22387,rule_22388,rule_22389,rule_22390,rule_22391,rule_22392,rule_22393,rule_22394,rule_22395,rule_22396,rule_22397,rule_22398,rule_22399,rule_22400,rule_22401,rule_22402,rule_22403,rule_22404,rule_22405,rule_22406,rule_22407,rule_22408,rule_22409,rule_22410,rule_22411,rule_22412,rule_22413,rule_22414,rule_22415,rule_22416,rule_22417,rule_22418,rule_22419,rule_22420,rule_22421,rule_22422,rule_22423,rule_22424,rule_22425,rule_22426,rule_22427,rule_22428,rule_22429,rule_22430,rule_22431,rule_22432,rule_22433,rule_22434,rule_22435,rule_22436,rule_22437,rule_22438,rule_22439,rule_22440,rule_22441,rule_22442,rule_22443,rule_22444,rule_22445,rule_22446,rule_22447,rule_22448,rule_22449,rule_22450,rule_22451,rule_22452,rule_22453,rule_22454,rule_22455,rule_22456,rule_22457,rule_22458,rule_22459,rule_22460,rule_22461,rule_22462,rule_22463,rule_22464,rule_22465,rule_22466,rule_22467,rule_22468,rule_22469,rule_22470,rule_22471,rule_22472,rule_22473,rule_22474,rule_22475,rule_22476,rule_22477,rule_22478,rule_22479,rule_22480,rule_22481,rule_22482,rule_22483,rule_22484,rule_22485,rule_22486,rule_22487,rule_22488,rule_22489,rule_22490,rule_22491,rule_22492,rule_22493,rule_22494,rule_22495,rule_22496,rule_22497,rule_22498,rule_22499,rule_22500,rule_22501,rule_22502,rule_22503,rule_22504,rule_22505,rule_22506,rule_22507,rule_22508,rule_22509,rule_22510,rule_22511,rule_22512,rule_22513,rule_22514,rule_22515,rule_22516,rule_22517,rule_22518,rule_22519,rule_22520,rule_22521,rule_22522,rule_22523,rule_22524,rule_22525,rule_22526,rule_22527,rule_22528,rule_22529,rule_22530,rule_22531,rule_22532,rule_22533,rule_22534,rule_22535,rule_22536,rule_22537,rule_22538,rule_22539,rule_22540,rule_22541,rule_22542,rule_22543,rule_22544,rule_22545,rule_22546,rule_22547,rule_22548,rule_22549,rule_22550,rule_22551,rule_22552,rule_22553,rule_22554,rule_22555,rule_22556,rule_22557,rule_22558,rule_22559,rule_22560,rule_22561,rule_22562,rule_22563,rule_22564,rule_22565,rule_22566,rule_22567,rule_22568,rule_22569,rule_22570,rule_22571,rule_22572,rule_22573,rule_22574,rule_22575,rule_22576,rule_22577,rule_22578,rule_22579,rule_22580,rule_22581,rule_22582,rule_22583,rule_22584,rule_22585,rule_22586,rule_22587,rule_22588,rule_22589,rule_22590,rule_22591,rule_22592,rule_22593,rule_22594,rule_22595,rule_22596,rule_22597,rule_22598,rule_22599,rule_22600,rule_22601,rule_22602,rule_22603,rule_22604,rule_22605,rule_22606,rule_22607,rule_22608,rule_22609,rule_22610,rule_22611,rule_22612,rule_22613,rule_22614,rule_22615,rule_22616,rule_22617,rule_22618,rule_22619,rule_22620,rule_22621,rule_22622,rule_22623,rule_22624,rule_22625,rule_22626,rule_22627,rule_22628,rule_22629,rule_22630,rule_22631,rule_22632,rule_22633,rule_22634,rule_22635,rule_22636,rule_22637,rule_22638,rule_22639,rule_22640,rule_22641,rule_22642,rule_22643,rule_22644,rule_22645,rule_22646,rule_22647,rule_22648,rule_22649,rule_22650,rule_22651,rule_22652,rule_22653,rule_22654,rule_22655,rule_22656,rule_22657,rule_22658,rule_22659,rule_22660,rule_22661,rule_22662,rule_22663,rule_22664,rule_22665,rule_22666,rule_22667,rule_22668,rule_22669,rule_22670,rule_22671,rule_22672,rule_22673,rule_22674,rule_22675,rule_22676,rule_22677,rule_22678,rule_22679,rule_22680,rule_22681,rule_22682,rule_22683,rule_22684,rule_22685,rule_22686,rule_22687,rule_22688,rule_22689,rule_22690,rule_22691,rule_22692,rule_22693,rule_22694,rule_22695,rule_22696,rule_22697,rule_22698,rule_22699,rule_22700,rule_22701,rule_22702,rule_22703,rule_22704,rule_22705,rule_22706,rule_22707,rule_22708,rule_22709,rule_22710,rule_22711,rule_22712,rule_22713,rule_22714,rule_22715,rule_22716,rule_22717,rule_22718,rule_22719,rule_22720,rule_22721,rule_22722,rule_22723,rule_22724,rule_22725,rule_22726,rule_22727,rule_22728,rule_22729,rule_22730,rule_22731,rule_22732,rule_22733,rule_22734,rule_22735,rule_22736,rule_22737,rule_22738,rule_22739,rule_22740,rule_22741,rule_22742,rule_22743,rule_22744,rule_22745,rule_22746,rule_22747,rule_22748,rule_22749,rule_22750,rule_22751,rule_22752,rule_22753,rule_22754,rule_22755,rule_22756,rule_22757,rule_22758,rule_22759,rule_22760,rule_22761,rule_22762,rule_22763,rule_22764,rule_22765,rule_22766,rule_22767,rule_22768,rule_22769,rule_22770,rule_22771,rule_22772,rule_22773,rule_22774,rule_22775,rule_22776,rule_22777,rule_22778,rule_22779,rule_22780,rule_22781,rule_22782,rule_22783,rule_22784,rule_22785,rule_22786,rule_22787,rule_22788,rule_22789,rule_22790,rule_22791,rule_22792,rule_22793,rule_22794,rule_22795,rule_22796,rule_22797,rule_22798,rule_22799,rule_22800,rule_22801,rule_22802,rule_22803,rule_22804,rule_22805,rule_22806,rule_22807,rule_22808,rule_22809,rule_22810,rule_22811,rule_22812,rule_22813,rule_22814,rule_22815,rule_22816,rule_22817,rule_22818,rule_22819,rule_22820,rule_22821,rule_22822,rule_22823,rule_22824,rule_22825,rule_22826,rule_22827,rule_22828,rule_22829,rule_22830,rule_22831,rule_22832,rule_22833,rule_22834,rule_22835,rule_22836,rule_22837,rule_22838,rule_22839,rule_22840,rule_22841,rule_22842,rule_22843,rule_22844,rule_22845,rule_22846,rule_22847,rule_22848,rule_22849,rule_22850,rule_22851,rule_22852,rule_22853,rule_22854,rule_22855,rule_22856,rule_22857,rule_22858,rule_22859,rule_22860,rule_22861,rule_22862,rule_22863,rule_22864,rule_22865,rule_22866,rule_22867,rule_22868,rule_22869,rule_22870,rule_22871,rule_22872,rule_22873,rule_22874,rule_22875,rule_22876,rule_22877,rule_22878,rule_22879,rule_22880,rule_22881,rule_22882,rule_22883,rule_22884,rule_22885,rule_22886,rule_22887,rule_22888,rule_22889,rule_22890,rule_22891,rule_22892,rule_22893,rule_22894,rule_22895,rule_22896,rule_22897,rule_22898,rule_22899,rule_22900,rule_22901,rule_22902,rule_22903,rule_22904,rule_22905,rule_22906,rule_22907,rule_22908,rule_22909,rule_22910,rule_22911,rule_22912,rule_22913,rule_22914,rule_22915,rule_22916,rule_22917,rule_22918,rule_22919,rule_22920,rule_22921,rule_22922,rule_22923,rule_22924,rule_22925,rule_22926,rule_22927,rule_22928,rule_22929,rule_22930,rule_22931,rule_22932,rule_22933,rule_22934,rule_22935,rule_22936,rule_22937,rule_22938,rule_22939,rule_22940,rule_22941,rule_22942,rule_22943,rule_22944,rule_22945,rule_22946,rule_22947,rule_22948,rule_22949,rule_22950,rule_22951,rule_22952,rule_22953,rule_22954,rule_22955,rule_22956,rule_22957,rule_22958,rule_22959,rule_22960,rule_22961,rule_22962,rule_22963,rule_22964,rule_22965,rule_22966,rule_22967,rule_22968,rule_22969,rule_22970,rule_22971,rule_22972,rule_22973,rule_22974,rule_22975,rule_22976,rule_22977,rule_22978,rule_22979,rule_22980,rule_22981,rule_22982,rule_22983,rule_22984,rule_22985,rule_22986,rule_22987,rule_22988,rule_22989,rule_22990,rule_22991,rule_22992,rule_22993,rule_22994,rule_22995,rule_22996,rule_22997,rule_22998,rule_22999,rule_23000,rule_23001,rule_23002,rule_23003,rule_23004,rule_23005,rule_23006,rule_23007,rule_23008,rule_23009,rule_23010,rule_23011,rule_23012,rule_23013,rule_23014,rule_23015,rule_23016,rule_23017,rule_23018,rule_23019,rule_23020,rule_23021,rule_23022,rule_23023,rule_23024,rule_23025,rule_23026,rule_23027,rule_23028,rule_23029,rule_23030,rule_23031,rule_23032,rule_23033,rule_23034,rule_23035,rule_23036,rule_23037,rule_23038,rule_23039,rule_23040,rule_23041,rule_23042,rule_23043,rule_23044,rule_23045,rule_23046,rule_23047,rule_23048,rule_23049,rule_23050,rule_23051,rule_23052,rule_23053,rule_23054,rule_23055,rule_23056,rule_23057,rule_23058,rule_23059,rule_23060,rule_23061,rule_23062,rule_23063,rule_23064,rule_23065,rule_23066,rule_23067,rule_23068,rule_23069,rule_23070,rule_23071,rule_23072,rule_23073,rule_23074,rule_23075,rule_23076,rule_23077,rule_23078,rule_23079,rule_23080,rule_23081,rule_23082,rule_23083,rule_23084,rule_23085,rule_23086,rule_23087,rule_23088,rule_23089,rule_23090,rule_23091,rule_23092,rule_23093,rule_23094,rule_23095,rule_23096,rule_23097,rule_23098,rule_23099,rule_23100,rule_23101,rule_23102,rule_23103,rule_23104,rule_23105,rule_23106,rule_23107,rule_23108,rule_23109,rule_23110,rule_23111,rule_23112,rule_23113,rule_23114,rule_23115,rule_23116,rule_23117,rule_23118,rule_23119,rule_23120,rule_23121,rule_23122,rule_23123,rule_23124,rule_23125,rule_23126,rule_23127,rule_23128,rule_23129,rule_23130,rule_23131,rule_23132,rule_23133,rule_23134,rule_23135,rule_23136,rule_23137,rule_23138,rule_23139,rule_23140,rule_23141,rule_23142,rule_23143,rule_23144,rule_23145,rule_23146,rule_23147,rule_23148,rule_23149,rule_23150,rule_23151,rule_23152,rule_23153,rule_23154,rule_23155,rule_23156,rule_23157,rule_23158,rule_23159,rule_23160,rule_23161,rule_23162,rule_23163,rule_23164,rule_23165,rule_23166,rule_23167,rule_23168,rule_23169,rule_23170,rule_23171,rule_23172,rule_23173,rule_23174,rule_23175,rule_23176,rule_23177,rule_23178,rule_23179,rule_23180,rule_23181,rule_23182,rule_23183,rule_23184,rule_23185,rule_23186,rule_23187,rule_23188,rule_23189,rule_23190,rule_23191,rule_23192,rule_23193,rule_23194,rule_23195,rule_23196,rule_23197,rule_23198,rule_23199,rule_23200,rule_23201,rule_23202,rule_23203,rule_23204,rule_23205,rule_23206,rule_23207,rule_23208,rule_23209,rule_23210,rule_23211,rule_23212,rule_23213,rule_23214,rule_23215,rule_23216,rule_23217,rule_23218,rule_23219,rule_23220,rule_23221,rule_23222,rule_23223,rule_23224,rule_23225,rule_23226,rule_23227,rule_23228,rule_23229,rule_23230,rule_23231,rule_23232,rule_23233,rule_23234,rule_23235,rule_23236,rule_23237,rule_23238,rule_23239,rule_23240,rule_23241,rule_23242,rule_23243,rule_23244,rule_23245,rule_23246,rule_23247,rule_23248,rule_23249,rule_23250,rule_23251,rule_23252,rule_23253,rule_23254,rule_23255,rule_23256,rule_23257,rule_23258,rule_23259,rule_23260,rule_23261,rule_23262,rule_23263,rule_23264,rule_23265,rule_23266,rule_23267,rule_23268,rule_23269,rule_23270,rule_23271,rule_23272,rule_23273,rule_23274,rule_23275,rule_23276,rule_23277,rule_23278,rule_23279,rule_23280,rule_23281,rule_23282,rule_23283,rule_23284,rule_23285,rule_23286,rule_23287,rule_23288,rule_23289,rule_23290,rule_23291,rule_23292,rule_23293,rule_23294,rule_23295,rule_23296,rule_23297,rule_23298,rule_23299,rule_23300,rule_23301,rule_23302,rule_23303,rule_23304,rule_23305,rule_23306,rule_23307,rule_23308,rule_23309,rule_23310,rule_23311,rule_23312,rule_23313,rule_23314,rule_23315,rule_23316,rule_23317,rule_23318,rule_23319,rule_23320,rule_23321,rule_23322,rule_23323,rule_23324,rule_23325,rule_23326,rule_23327,rule_23328,rule_23329,rule_23330,rule_23331,rule_23332,rule_23333,rule_23334,rule_23335,rule_23336,rule_23337,rule_23338,rule_23339,rule_23340,rule_23341,rule_23342,rule_23343,rule_23344,rule_23345,rule_23346,rule_23347,rule_23348,rule_23349,rule_23350,rule_23351,rule_23352,rule_23353,rule_23354,rule_23355,rule_23356,rule_23357,rule_23358,rule_23359,rule_23360,rule_23361,rule_23362,rule_23363,rule_23364,rule_23365,rule_23366,rule_23367,rule_23368,rule_23369,rule_23370,rule_23371,rule_23372,rule_23373,rule_23374,rule_23375,rule_23376,rule_23377,rule_23378,rule_23379,rule_23380,rule_23381,rule_23382,rule_23383,rule_23384,rule_23385,rule_23386,rule_23387,rule_23388,rule_23389,rule_23390,rule_23391,rule_23392,rule_23393,rule_23394,rule_23395,rule_23396,rule_23397,rule_23398,rule_23399,rule_23400,rule_23401,rule_23402,rule_23403,rule_23404,rule_23405,rule_23406,rule_23407,rule_23408,rule_23409,rule_23410,rule_23411,rule_23412,rule_23413,rule_23414,rule_23415,rule_23416,rule_23417,rule_23418,rule_23419,rule_23420,rule_23421,rule_23422,rule_23423,rule_23424,rule_23425,rule_23426,rule_23427,rule_23428,rule_23429,rule_23430,rule_23431,rule_23432,rule_23433,rule_23434,rule_23435,rule_23436,rule_23437,rule_23438,rule_23439,rule_23440,rule_23441,rule_23442,rule_23443,rule_23444,rule_23445,rule_23446,rule_23447,rule_23448,rule_23449,rule_23450,rule_23451,rule_23452,rule_23453,rule_23454,rule_23455,rule_23456,rule_23457,rule_23458,rule_23459,rule_23460,rule_23461,rule_23462,rule_23463,rule_23464,rule_23465,rule_23466,rule_23467,rule_23468,rule_23469,rule_23470,rule_23471,rule_23472,rule_23473,rule_23474,rule_23475,rule_23476,rule_23477,rule_23478,rule_23479,rule_23480,rule_23481,rule_23482,rule_23483,rule_23484,rule_23485,rule_23486,rule_23487,rule_23488,rule_23489,rule_23490,rule_23491,rule_23492,rule_23493,rule_23494,rule_23495,rule_23496,rule_23497,rule_23498,rule_23499,rule_23500,rule_23501,rule_23502,rule_23503,rule_23504,rule_23505,rule_23506,rule_23507,rule_23508,rule_23509,rule_23510,rule_23511,rule_23512,rule_23513,rule_23514,rule_23515,rule_23516,rule_23517,rule_23518,rule_23519,rule_23520,rule_23521,rule_23522,rule_23523,rule_23524,rule_23525,rule_23526,rule_23527,rule_23528,rule_23529,rule_23530,rule_23531,rule_23532,rule_23533,rule_23534,rule_23535,rule_23536,rule_23537,rule_23538,rule_23539,rule_23540,rule_23541,rule_23542,rule_23543,rule_23544,rule_23545,rule_23546,rule_23547,rule_23548,rule_23549,rule_23550,rule_23551,rule_23552,rule_23553,rule_23554,rule_23555,rule_23556,rule_23557,rule_23558,rule_23559,rule_23560,rule_23561,rule_23562,rule_23563,rule_23564,rule_23565,rule_23566,rule_23567,rule_23568,rule_23569,rule_23570,rule_23571,rule_23572,rule_23573,rule_23574,rule_23575,rule_23576,rule_23577,rule_23578,rule_23579,rule_23580,rule_23581,rule_23582,rule_23583,rule_23584,rule_23585,rule_23586,rule_23587,rule_23588,rule_23589,rule_23590,rule_23591,rule_23592,rule_23593,rule_23594,rule_23595,rule_23596,rule_23597,rule_23598,rule_23599,rule_23600,rule_23601,rule_23602,rule_23603,rule_23604,rule_23605,rule_23606,rule_23607,rule_23608,rule_23609,rule_23610,rule_23611,rule_23612,rule_23613,rule_23614,rule_23615,rule_23616,rule_23617,rule_23618,rule_23619,rule_23620,rule_23621,rule_23622,rule_23623,rule_23624,rule_23625,rule_23626,rule_23627,rule_23628,rule_23629,rule_23630,rule_23631,rule_23632,rule_23633,rule_23634,rule_23635,rule_23636,rule_23637,rule_23638,rule_23639,rule_23640,rule_23641,rule_23642,rule_23643,rule_23644,rule_23645,rule_23646,rule_23647,rule_23648,rule_23649,rule_23650,rule_23651,rule_23652,rule_23653,rule_23654,rule_23655,rule_23656,rule_23657,rule_23658,rule_23659,rule_23660,rule_23661,rule_23662,rule_23663,rule_23664,rule_23665,rule_23666,rule_23667,rule_23668,rule_23669,rule_23670,rule_23671,rule_23672,rule_23673,rule_23674,rule_23675,rule_23676,rule_23677,rule_23678,rule_23679,rule_23680,rule_23681,rule_23682,rule_23683,rule_23684,rule_23685,rule_23686,rule_23687,rule_23688,rule_23689,rule_23690,rule_23691,rule_23692,rule_23693,rule_23694,rule_23695,rule_23696,rule_23697,rule_23698,rule_23699,rule_23700,rule_23701,rule_23702,rule_23703,rule_23704,rule_23705,rule_23706,rule_23707,rule_23708,rule_23709,rule_23710,rule_23711,rule_23712,rule_23713,rule_23714,rule_23715,rule_23716,rule_23717,rule_23718,rule_23719,rule_23720,rule_23721,rule_23722,rule_23723,rule_23724,rule_23725,rule_23726,rule_23727,rule_23728,rule_23729,rule_23730,rule_23731,rule_23732,rule_23733,rule_23734,rule_23735,rule_23736,rule_23737,rule_23738,rule_23739,rule_23740,rule_23741,rule_23742,rule_23743,rule_23744,rule_23745,rule_23746,rule_23747,rule_23748,rule_23749,rule_23750,rule_23751,rule_23752,rule_23753,rule_23754,rule_23755,rule_23756,rule_23757,rule_23758,rule_23759,rule_23760,rule_23761,rule_23762,rule_23763,rule_23764,rule_23765,rule_23766,rule_23767,rule_23768,rule_23769,rule_23770,rule_23771,rule_23772,rule_23773,rule_23774,rule_23775,rule_23776,rule_23777,rule_23778,rule_23779,rule_23780,rule_23781,rule_23782,rule_23783,rule_23784,rule_23785,rule_23786,rule_23787,rule_23788,rule_23789,rule_23790,rule_23791,rule_23792,rule_23793,rule_23794,rule_23795,rule_23796,rule_23797,rule_23798,rule_23799,rule_23800,rule_23801,rule_23802,rule_23803,rule_23804,rule_23805,rule_23806,rule_23807,rule_23808,rule_23809,rule_23810,rule_23811,rule_23812,rule_23813,rule_23814,rule_23815,rule_23816,rule_23817,rule_23818,rule_23819,rule_23820,rule_23821,rule_23822,rule_23823,rule_23824,rule_23825,rule_23826,rule_23827,rule_23828,rule_23829,rule_23830,rule_23831,rule_23832,rule_23833,rule_23834,rule_23835,rule_23836,rule_23837,rule_23838,rule_23839,rule_23840,rule_23841,rule_23842,rule_23843,rule_23844,rule_23845,rule_23846,rule_23847,rule_23848,rule_23849,rule_23850,rule_23851,rule_23852,rule_23853,rule_23854,rule_23855,rule_23856,rule_23857,rule_23858,rule_23859,rule_23860,rule_23861,rule_23862,rule_23863,rule_23864,rule_23865,rule_23866,rule_23867,rule_23868,rule_23869,rule_23870,rule_23871,rule_23872,rule_23873,rule_23874,rule_23875,rule_23876,rule_23877,rule_23878,rule_23879,rule_23880,rule_23881,rule_23882,rule_23883,rule_23884,rule_23885,rule_23886,rule_23887,rule_23888,rule_23889,rule_23890,rule_23891,rule_23892,rule_23893,rule_23894,rule_23895,rule_23896,rule_23897,rule_23898,rule_23899,rule_23900,rule_23901,rule_23902,rule_23903,rule_23904,rule_23905,rule_23906,rule_23907,rule_23908,rule_23909,rule_23910,rule_23911,rule_23912,rule_23913,rule_23914,rule_23915,rule_23916,rule_23917,rule_23918,rule_23919,rule_23920,rule_23921,rule_23922,rule_23923,rule_23924,rule_23925,rule_23926,rule_23927,rule_23928,rule_23929,rule_23930,rule_23931,rule_23932,rule_23933,rule_23934,rule_23935,rule_23936,rule_23937,rule_23938,rule_23939,rule_23940,rule_23941,rule_23942,rule_23943,rule_23944,rule_23945,rule_23946,rule_23947,rule_23948,rule_23949,rule_23950,rule_23951,rule_23952,rule_23953,rule_23954,rule_23955,rule_23956,rule_23957,rule_23958,rule_23959,rule_23960,rule_23961,rule_23962,rule_23963,rule_23964,rule_23965,rule_23966,rule_23967,rule_23968,rule_23969,rule_23970,rule_23971,rule_23972,rule_23973,rule_23974,rule_23975,rule_23976,rule_23977,rule_23978,rule_23979,rule_23980,rule_23981,rule_23982,rule_23983,rule_23984,rule_23985,rule_23986,rule_23987,rule_23988,rule_23989,rule_23990,rule_23991,rule_23992,rule_23993,rule_23994,rule_23995,rule_23996,rule_23997,rule_23998,rule_23999,rule_24000,rule_24001,rule_24002,rule_24003,rule_24004,rule_24005,rule_24006,rule_24007,rule_24008,rule_24009,rule_24010,rule_24011,rule_24012,rule_24013,rule_24014,rule_24015,rule_24016,rule_24017,rule_24018,rule_24019,rule_24020,rule_24021,rule_24022,rule_24023,rule_24024,rule_24025,rule_24026,rule_24027,rule_24028,rule_24029,rule_24030,rule_24031,rule_24032,rule_24033,rule_24034,rule_24035,rule_24036,rule_24037,rule_24038,rule_24039,rule_24040,rule_24041,rule_24042,rule_24043,rule_24044,rule_24045,rule_24046,rule_24047,rule_24048,rule_24049,rule_24050,rule_24051,rule_24052,rule_24053,rule_24054,rule_24055,rule_24056,rule_24057,rule_24058,rule_24059,rule_24060,rule_24061,rule_24062,rule_24063,rule_24064,rule_24065,rule_24066,rule_24067,rule_24068,rule_24069,rule_24070,rule_24071,rule_24072,rule_24073,rule_24074,rule_24075,rule_24076,rule_24077,rule_24078,rule_24079,rule_24080,rule_24081,rule_24082,rule_24083,rule_24084,rule_24085,rule_24086,rule_24087,rule_24088,rule_24089,rule_24090,rule_24091,rule_24092,rule_24093,rule_24094,rule_24095,rule_24096,rule_24097,rule_24098,rule_24099,rule_24100,rule_24101,rule_24102,rule_24103,rule_24104,rule_24105,rule_24106,rule_24107,rule_24108,rule_24109,rule_24110,rule_24111,rule_24112,rule_24113,rule_24114,rule_24115,rule_24116,rule_24117,rule_24118,rule_24119,rule_24120,rule_24121,rule_24122,rule_24123,rule_24124,rule_24125,rule_24126,rule_24127,rule_24128,rule_24129,rule_24130,rule_24131,rule_24132,rule_24133,rule_24134,rule_24135,rule_24136,rule_24137,rule_24138,rule_24139,rule_24140,rule_24141,rule_24142,rule_24143,rule_24144,rule_24145,rule_24146,rule_24147,rule_24148,rule_24149,rule_24150,rule_24151,rule_24152,rule_24153,rule_24154,rule_24155,rule_24156,rule_24157,rule_24158,rule_24159,rule_24160,rule_24161,rule_24162,rule_24163,rule_24164,rule_24165,rule_24166,rule_24167,rule_24168,rule_24169,rule_24170,rule_24171,rule_24172,rule_24173,rule_24174,rule_24175,rule_24176,rule_24177,rule_24178,rule_24179,rule_24180,rule_24181,rule_24182,rule_24183,rule_24184,rule_24185,rule_24186,rule_24187,rule_24188,rule_24189,rule_24190,rule_24191,rule_24192,rule_24193,rule_24194,rule_24195,rule_24196,rule_24197,rule_24198,rule_24199,rule_24200,rule_24201,rule_24202,rule_24203,rule_24204,rule_24205,rule_24206,rule_24207,rule_24208,rule_24209,rule_24210,rule_24211,rule_24212,rule_24213,rule_24214,rule_24215,rule_24216,rule_24217,rule_24218,rule_24219,rule_24220,rule_24221,rule_24222,rule_24223,rule_24224,rule_24225,rule_24226,rule_24227,rule_24228,rule_24229,rule_24230,rule_24231,rule_24232,rule_24233,rule_24234,rule_24235,rule_24236,rule_24237,rule_24238,rule_24239,rule_24240,rule_24241,rule_24242,rule_24243,rule_24244,rule_24245,rule_24246,rule_24247,rule_24248,rule_24249,rule_24250,rule_24251,rule_24252,rule_24253,rule_24254,rule_24255,rule_24256,rule_24257,rule_24258,rule_24259,rule_24260,rule_24261,rule_24262,rule_24263,rule_24264,rule_24265,rule_24266,rule_24267,rule_24268,rule_24269,rule_24270,rule_24271,rule_24272,rule_24273,rule_24274,rule_24275,rule_24276,rule_24277,rule_24278,rule_24279,rule_24280,rule_24281,rule_24282,rule_24283,rule_24284,rule_24285,rule_24286,rule_24287,rule_24288,rule_24289,rule_24290,rule_24291,rule_24292,rule_24293,rule_24294,rule_24295,rule_24296,rule_24297,rule_24298,rule_24299,rule_24300,rule_24301,rule_24302,rule_24303,rule_24304,rule_24305,rule_24306,rule_24307,rule_24308,rule_24309,rule_24310,rule_24311,rule_24312,rule_24313,rule_24314,rule_24315,rule_24316,rule_24317,rule_24318,rule_24319,rule_24320,rule_24321,rule_24322,rule_24323,rule_24324,rule_24325,rule_24326,rule_24327,rule_24328,rule_24329,rule_24330,rule_24331,rule_24332,rule_24333,rule_24334,rule_24335,rule_24336,rule_24337,rule_24338,rule_24339,rule_24340,rule_24341,rule_24342,rule_24343,rule_24344,rule_24345,rule_24346,rule_24347,rule_24348,rule_24349,rule_24350,rule_24351,rule_24352,rule_24353,rule_24354,rule_24355,rule_24356,rule_24357,rule_24358,rule_24359,rule_24360,rule_24361,rule_24362,rule_24363,rule_24364,rule_24365,rule_24366,rule_24367,rule_24368,rule_24369,rule_24370,rule_24371,rule_24372,rule_24373,rule_24374,rule_24375,rule_24376,rule_24377,rule_24378,rule_24379,rule_24380,rule_24381,rule_24382,rule_24383,rule_24384,rule_24385,rule_24386,rule_24387,rule_24388,rule_24389,rule_24390,rule_24391,rule_24392,rule_24393,rule_24394,rule_24395,rule_24396,rule_24397,rule_24398,rule_24399,rule_24400,rule_24401,rule_24402,rule_24403,rule_24404,rule_24405,rule_24406,rule_24407,rule_24408,rule_24409,rule_24410,rule_24411,rule_24412,rule_24413,rule_24414,rule_24415,rule_24416,rule_24417,rule_24418,rule_24419,rule_24420,rule_24421,rule_24422,rule_24423,rule_24424,rule_24425,rule_24426,rule_24427,rule_24428,rule_24429,rule_24430,rule_24431,rule_24432,rule_24433,rule_24434,rule_24435,rule_24436,rule_24437,rule_24438,rule_24439,rule_24440,rule_24441,rule_24442,rule_24443,rule_24444,rule_24445,rule_24446,rule_24447,rule_24448,rule_24449,rule_24450,rule_24451,rule_24452,rule_24453,rule_24454,rule_24455,rule_24456,rule_24457,rule_24458,rule_24459,rule_24460,rule_24461,rule_24462,rule_24463,rule_24464,rule_24465,rule_24466,rule_24467,rule_24468,rule_24469,rule_24470,rule_24471,rule_24472,rule_24473,rule_24474,rule_24475,rule_24476,rule_24477,rule_24478,rule_24479,rule_24480,rule_24481,rule_24482,rule_24483,rule_24484,rule_24485,rule_24486,rule_24487,rule_24488,rule_24489,rule_24490,rule_24491,rule_24492,rule_24493,rule_24494,rule_24495,rule_24496,rule_24497,rule_24498,rule_24499,rule_24500,rule_24501,rule_24502,rule_24503,rule_24504,rule_24505,rule_24506,rule_24507,rule_24508,rule_24509,rule_24510,rule_24511,rule_24512,rule_24513,rule_24514,rule_24515,rule_24516,rule_24517,rule_24518,rule_24519,rule_24520,rule_24521,rule_24522,rule_24523,rule_24524,rule_24525,rule_24526,rule_24527,rule_24528,rule_24529,rule_24530,rule_24531,rule_24532,rule_24533,rule_24534,rule_24535,rule_24536,rule_24537,rule_24538,rule_24539,rule_24540,rule_24541,rule_24542,rule_24543,rule_24544,rule_24545,rule_24546,rule_24547,rule_24548,rule_24549,rule_24550,rule_24551,rule_24552,rule_24553,rule_24554,rule_24555,rule_24556,rule_24557,rule_24558,rule_24559,rule_24560,rule_24561,rule_24562,rule_24563,rule_24564,rule_24565,rule_24566,rule_24567,rule_24568,rule_24569,rule_24570,rule_24571,rule_24572,rule_24573,rule_24574,rule_24575,rule_24576,rule_24577,rule_24578,rule_24579,rule_24580,rule_24581,rule_24582,rule_24583,rule_24584,rule_24585,rule_24586,rule_24587,rule_24588,rule_24589,rule_24590,rule_24591,rule_24592,rule_24593,rule_24594,rule_24595,rule_24596,rule_24597,rule_24598,rule_24599,rule_24600,rule_24601,rule_24602,rule_24603,rule_24604,rule_24605,rule_24606,rule_24607,rule_24608,rule_24609,rule_24610,rule_24611,rule_24612,rule_24613,rule_24614,rule_24615,rule_24616,rule_24617,rule_24618,rule_24619,rule_24620,rule_24621,rule_24622,rule_24623,rule_24624,rule_24625,rule_24626,rule_24627,rule_24628,rule_24629,rule_24630,rule_24631,rule_24632,rule_24633,rule_24634,rule_24635,rule_24636,rule_24637,rule_24638,rule_24639,rule_24640,rule_24641,rule_24642,rule_24643,rule_24644,rule_24645,rule_24646,rule_24647,rule_24648,rule_24649,rule_24650,rule_24651,rule_24652,rule_24653,rule_24654,rule_24655,rule_24656,rule_24657,rule_24658,rule_24659,rule_24660,rule_24661,rule_24662,rule_24663,rule_24664,rule_24665,rule_24666,rule_24667,rule_24668,rule_24669,rule_24670,rule_24671,rule_24672,rule_24673,rule_24674,rule_24675,rule_24676,rule_24677,rule_24678,rule_24679,rule_24680,rule_24681,rule_24682,rule_24683,rule_24684,rule_24685,rule_24686,rule_24687,rule_24688,rule_24689,rule_24690,rule_24691,rule_24692,rule_24693,rule_24694,rule_24695,rule_24696,rule_24697,rule_24698,rule_24699,rule_24700,rule_24701,rule_24702,rule_24703,rule_24704,rule_24705,rule_24706,rule_24707,rule_24708,rule_24709,rule_24710,rule_24711,rule_24712,rule_24713,rule_24714,rule_24715,rule_24716,rule_24717,rule_24718,rule_24719,rule_24720,rule_24721,rule_24722,rule_24723,rule_24724,rule_24725,rule_24726,rule_24727,rule_24728,rule_24729,rule_24730,rule_24731,rule_24732,rule_24733,rule_24734,rule_24735,rule_24736,rule_24737,rule_24738,rule_24739,rule_24740,rule_24741,rule_24742,rule_24743,rule_24744,rule_24745,rule_24746,rule_24747,rule_24748,rule_24749,rule_24750,rule_24751,rule_24752,rule_24753,rule_24754,rule_24755,rule_24756,rule_24757,rule_24758,rule_24759,rule_24760,rule_24761,rule_24762,rule_24763,rule_24764,rule_24765,rule_24766,rule_24767,rule_24768,rule_24769,rule_24770,rule_24771,rule_24772,rule_24773,rule_24774,rule_24775,rule_24776,rule_24777,rule_24778,rule_24779,rule_24780,rule_24781,rule_24782,rule_24783,rule_24784,rule_24785,rule_24786,rule_24787,rule_24788,rule_24789,rule_24790,rule_24791,rule_24792,rule_24793,rule_24794,rule_24795,rule_24796,rule_24797,rule_24798,rule_24799,rule_24800,rule_24801,rule_24802,rule_24803,rule_24804,rule_24805,rule_24806,rule_24807,rule_24808,rule_24809,rule_24810,rule_24811,rule_24812,rule_24813,rule_24814,rule_24815,rule_24816,rule_24817,rule_24818,rule_24819,rule_24820,rule_24821,rule_24822,rule_24823,rule_24824,rule_24825,rule_24826,rule_24827,rule_24828,rule_24829,rule_24830,rule_24831,rule_24832,rule_24833,rule_24834,rule_24835,rule_24836,rule_24837,rule_24838,rule_24839,rule_24840,rule_24841,rule_24842,rule_24843,rule_24844,rule_24845,rule_24846,rule_24847,rule_24848,rule_24849,rule_24850,rule_24851,rule_24852,rule_24853,rule_24854,rule_24855,rule_24856,rule_24857,rule_24858,rule_24859,rule_24860,rule_24861,rule_24862,rule_24863,rule_24864,rule_24865,rule_24866,rule_24867,rule_24868,rule_24869,rule_24870,rule_24871,rule_24872,rule_24873,rule_24874,rule_24875,rule_24876,rule_24877,rule_24878,rule_24879,rule_24880,rule_24881,rule_24882,rule_24883,rule_24884,rule_24885,rule_24886,rule_24887,rule_24888,rule_24889,rule_24890,rule_24891,rule_24892,rule_24893,rule_24894,rule_24895,rule_24896,rule_24897,rule_24898,rule_24899,rule_24900,rule_24901,rule_24902,rule_24903,rule_24904,rule_24905,rule_24906,rule_24907,rule_24908,rule_24909,rule_24910,rule_24911,rule_24912,rule_24913,rule_24914,rule_24915,rule_24916,rule_24917,rule_24918,rule_24919,rule_24920,rule_24921,rule_24922,rule_24923,rule_24924,rule_24925,rule_24926,rule_24927,rule_24928,rule_24929,rule_24930,rule_24931,rule_24932,rule_24933,rule_24934,rule_24935,rule_24936,rule_24937,rule_24938,rule_24939,rule_24940,rule_24941,rule_24942,rule_24943,rule_24944,rule_24945,rule_24946,rule_24947,rule_24948,rule_24949,rule_24950,rule_24951,rule_24952,rule_24953,rule_24954,rule_24955,rule_24956,rule_24957,rule_24958,rule_24959,rule_24960,rule_24961,rule_24962,rule_24963,rule_24964,rule_24965,rule_24966,rule_24967,rule_24968,rule_24969,rule_24970,rule_24971,rule_24972,rule_24973,rule_24974,rule_24975,rule_24976,rule_24977,rule_24978,rule_24979,rule_24980,rule_24981,rule_24982,rule_24983,rule_24984,rule_24985,rule_24986,rule_24987,rule_24988,rule_24989,rule_24990,rule_24991,rule_24992,rule_24993,rule_24994,rule_24995,rule_24996,rule_24997,rule_24998,rule_24999,rule_25000,rule_25001,rule_25002,rule_25003,rule_25004,rule_25005,rule_25006,rule_25007,rule_25008,rule_25009,rule_25010,rule_25011,rule_25012,rule_25013,rule_25014,rule_25015,rule_25016,rule_25017,rule_25018,rule_25019,rule_25020,rule_25021,rule_25022,rule_25023,rule_25024,rule_25025,rule_25026,rule_25027,rule_25028,rule_25029,rule_25030,rule_25031,rule_25032,rule_25033,rule_25034,rule_25035,rule_25036,rule_25037,rule_25038,rule_25039,rule_25040,rule_25041,rule_25042,rule_25043,rule_25044,rule_25045,rule_25046,rule_25047,rule_25048,rule_25049,rule_25050,rule_25051,rule_25052,rule_25053,rule_25054,rule_25055,rule_25056,rule_25057,rule_25058,rule_25059,rule_25060,rule_25061,rule_25062,rule_25063,rule_25064,rule_25065,rule_25066,rule_25067,rule_25068,rule_25069,rule_25070,rule_25071,rule_25072,rule_25073,rule_25074,rule_25075,rule_25076,rule_25077,rule_25078,rule_25079,rule_25080,rule_25081,rule_25082,rule_25083,rule_25084,rule_25085,rule_25086,rule_25087,rule_25088,rule_25089,rule_25090,rule_25091,rule_25092,rule_25093,rule_25094,rule_25095,rule_25096,rule_25097,rule_25098,rule_25099,rule_25100,rule_25101,rule_25102,rule_25103,rule_25104,rule_25105,rule_25106,rule_25107,rule_25108,rule_25109,rule_25110,rule_25111,rule_25112,rule_25113,rule_25114,rule_25115,rule_25116,rule_25117,rule_25118,rule_25119,rule_25120,rule_25121,rule_25122,rule_25123,rule_25124,rule_25125,rule_25126,rule_25127,rule_25128,rule_25129,rule_25130,rule_25131,rule_25132,rule_25133,rule_25134,rule_25135,rule_25136,rule_25137,rule_25138,rule_25139,rule_25140,rule_25141,rule_25142,rule_25143,rule_25144,rule_25145,rule_25146,rule_25147,rule_25148,rule_25149,rule_25150,rule_25151,rule_25152,rule_25153,rule_25154,rule_25155,rule_25156,rule_25157,rule_25158,rule_25159,rule_25160,rule_25161,rule_25162,rule_25163,rule_25164,rule_25165,rule_25166,rule_25167,rule_25168,rule_25169,rule_25170,rule_25171,rule_25172,rule_25173,rule_25174,rule_25175,rule_25176,rule_25177,rule_25178,rule_25179,rule_25180,rule_25181,rule_25182,rule_25183,rule_25184,rule_25185,rule_25186,rule_25187,rule_25188,rule_25189,rule_25190,rule_25191,rule_25192,rule_25193,rule_25194,rule_25195,rule_25196,rule_25197,rule_25198,rule_25199,rule_25200,rule_25201,rule_25202,rule_25203,rule_25204,rule_25205,rule_25206,rule_25207,rule_25208,rule_25209,rule_25210,rule_25211,rule_25212,rule_25213,rule_25214,rule_25215,rule_25216,rule_25217,rule_25218,rule_25219,rule_25220,rule_25221,rule_25222,rule_25223,rule_25224,rule_25225,rule_25226,rule_25227,rule_25228,rule_25229,rule_25230,rule_25231,rule_25232,rule_25233,rule_25234,rule_25235,rule_25236,rule_25237,rule_25238,rule_25239,rule_25240,rule_25241,rule_25242,rule_25243,rule_25244,rule_25245,rule_25246,rule_25247,rule_25248,rule_25249,rule_25250,rule_25251,rule_25252,rule_25253,rule_25254,rule_25255,rule_25256,rule_25257,rule_25258,rule_25259,rule_25260,rule_25261,rule_25262,rule_25263,rule_25264,rule_25265,rule_25266,rule_25267,rule_25268,rule_25269,rule_25270,rule_25271,rule_25272,rule_25273,rule_25274,rule_25275,rule_25276,rule_25277,rule_25278,rule_25279,rule_25280,rule_25281,rule_25282,rule_25283,rule_25284,rule_25285,rule_25286,rule_25287,rule_25288,rule_25289,rule_25290,rule_25291,rule_25292,rule_25293,rule_25294,rule_25295,rule_25296,rule_25297,rule_25298,rule_25299,rule_25300,rule_25301,rule_25302,rule_25303,rule_25304,rule_25305,rule_25306,rule_25307,rule_25308,rule_25309,rule_25310,rule_25311,rule_25312,rule_25313,rule_25314,rule_25315,rule_25316,rule_25317,rule_25318,rule_25319,rule_25320,rule_25321,rule_25322,rule_25323,rule_25324,rule_25325,rule_25326,rule_25327,rule_25328,rule_25329,rule_25330,rule_25331,rule_25332,rule_25333,rule_25334,rule_25335,rule_25336,rule_25337,rule_25338,rule_25339,rule_25340,rule_25341,rule_25342,rule_25343,rule_25344,rule_25345,rule_25346,rule_25347,rule_25348,rule_25349,rule_25350,rule_25351,rule_25352,rule_25353,rule_25354,rule_25355,rule_25356,rule_25357,rule_25358,rule_25359,rule_25360,rule_25361,rule_25362,rule_25363,rule_25364,rule_25365,rule_25366,rule_25367,rule_25368,rule_25369,rule_25370,rule_25371,rule_25372,rule_25373,rule_25374,rule_25375,rule_25376,rule_25377,rule_25378,rule_25379,rule_25380,rule_25381,rule_25382,rule_25383,rule_25384,rule_25385,rule_25386,rule_25387,rule_25388,rule_25389,rule_25390,rule_25391,rule_25392,rule_25393,rule_25394,rule_25395,rule_25396,rule_25397,rule_25398,rule_25399,rule_25400,rule_25401,rule_25402,rule_25403,rule_25404,rule_25405,rule_25406,rule_25407,rule_25408,rule_25409,rule_25410,rule_25411,rule_25412,rule_25413,rule_25414,rule_25415,rule_25416,rule_25417,rule_25418,rule_25419,rule_25420,rule_25421,rule_25422,rule_25423,rule_25424,rule_25425,rule_25426,rule_25427,rule_25428,rule_25429,rule_25430,rule_25431,rule_25432,rule_25433,rule_25434,rule_25435,rule_25436,rule_25437,rule_25438,rule_25439,rule_25440,rule_25441,rule_25442,rule_25443,rule_25444,rule_25445,rule_25446,rule_25447,rule_25448,rule_25449,rule_25450,rule_25451,rule_25452,rule_25453,rule_25454,rule_25455,rule_25456,rule_25457,rule_25458,rule_25459,rule_25460,rule_25461,rule_25462,rule_25463,rule_25464,rule_25465,rule_25466,rule_25467,rule_25468,rule_25469,rule_25470,rule_25471,rule_25472,rule_25473,rule_25474,rule_25475,rule_25476,rule_25477,rule_25478,rule_25479,rule_25480,rule_25481,rule_25482,rule_25483,rule_25484,rule_25485,rule_25486,rule_25487,rule_25488,rule_25489,rule_25490,rule_25491,rule_25492,rule_25493,rule_25494,rule_25495,rule_25496,rule_25497,rule_25498,rule_25499,rule_25500,rule_25501,rule_25502,rule_25503,rule_25504,rule_25505,rule_25506,rule_25507,rule_25508,rule_25509,rule_25510,rule_25511,rule_25512,rule_25513,rule_25514,rule_25515,rule_25516,rule_25517,rule_25518,rule_25519,rule_25520,rule_25521,rule_25522,rule_25523,rule_25524,rule_25525,rule_25526,rule_25527,rule_25528,rule_25529,rule_25530,rule_25531,rule_25532,rule_25533,rule_25534,rule_25535,rule_25536,rule_25537,rule_25538,rule_25539,rule_25540,rule_25541,rule_25542,rule_25543,rule_25544,rule_25545,rule_25546,rule_25547,rule_25548,rule_25549,rule_25550,rule_25551,rule_25552,rule_25553,rule_25554,rule_25555,rule_25556,rule_25557,rule_25558,rule_25559,rule_25560,rule_25561,rule_25562,rule_25563,rule_25564,rule_25565,rule_25566,rule_25567,rule_25568,rule_25569,rule_25570,rule_25571,rule_25572,rule_25573,rule_25574,rule_25575,rule_25576,rule_25577,rule_25578,rule_25579,rule_25580,rule_25581,rule_25582,rule_25583,rule_25584,rule_25585,rule_25586,rule_25587,rule_25588,rule_25589,rule_25590,rule_25591,rule_25592,rule_25593,rule_25594,rule_25595,rule_25596,rule_25597,rule_25598,rule_25599,rule_25600,rule_25601,rule_25602,rule_25603,rule_25604,rule_25605,rule_25606,rule_25607,rule_25608,rule_25609,rule_25610,rule_25611,rule_25612,rule_25613,rule_25614,rule_25615,rule_25616,rule_25617,rule_25618,rule_25619,rule_25620,rule_25621,rule_25622,rule_25623,rule_25624,rule_25625,rule_25626,rule_25627,rule_25628,rule_25629,rule_25630,rule_25631,rule_25632,rule_25633,rule_25634,rule_25635,rule_25636,rule_25637,rule_25638,rule_25639,rule_25640,rule_25641,rule_25642,rule_25643,rule_25644,rule_25645,rule_25646,rule_25647,rule_25648,rule_25649,rule_25650,rule_25651,rule_25652,rule_25653,rule_25654,rule_25655,rule_25656,rule_25657,rule_25658,rule_25659,rule_25660,rule_25661,rule_25662,rule_25663,rule_25664,rule_25665,rule_25666,rule_25667,rule_25668,rule_25669,rule_25670,rule_25671,rule_25672,rule_25673,rule_25674,rule_25675,rule_25676,rule_25677,rule_25678,rule_25679,rule_25680,rule_25681,rule_25682,rule_25683,rule_25684,rule_25685,rule_25686,rule_25687,rule_25688,rule_25689,rule_25690,rule_25691,rule_25692,rule_25693,rule_25694,rule_25695,rule_25696,rule_25697,rule_25698,rule_25699,rule_25700,rule_25701,rule_25702,rule_25703,rule_25704,rule_25705,rule_25706,rule_25707,rule_25708,rule_25709,rule_25710,rule_25711,rule_25712,rule_25713,rule_25714,rule_25715,rule_25716,rule_25717,rule_25718,rule_25719,rule_25720,rule_25721,rule_25722,rule_25723,rule_25724,rule_25725,rule_25726,rule_25727,rule_25728,rule_25729,rule_25730,rule_25731,rule_25732,rule_25733,rule_25734,rule_25735,rule_25736,rule_25737,rule_25738,rule_25739,rule_25740,rule_25741,rule_25742,rule_25743,rule_25744,rule_25745,rule_25746,rule_25747,rule_25748,rule_25749,rule_25750,rule_25751,rule_25752,rule_25753,rule_25754,rule_25755,rule_25756,rule_25757,rule_25758,rule_25759,rule_25760,rule_25761,rule_25762,rule_25763,rule_25764,rule_25765,rule_25766,rule_25767,rule_25768,rule_25769,rule_25770,rule_25771,rule_25772,rule_25773,rule_25774,rule_25775,rule_25776,rule_25777,rule_25778,rule_25779,rule_25780,rule_25781,rule_25782,rule_25783,rule_25784,rule_25785,rule_25786,rule_25787,rule_25788,rule_25789,rule_25790,rule_25791,rule_25792,rule_25793,rule_25794,rule_25795,rule_25796,rule_25797,rule_25798,rule_25799,rule_25800,rule_25801,rule_25802,rule_25803,rule_25804,rule_25805,rule_25806,rule_25807,rule_25808,rule_25809,rule_25810,rule_25811,rule_25812,rule_25813,rule_25814,rule_25815,rule_25816,rule_25817,rule_25818,rule_25819,rule_25820,rule_25821,rule_25822,rule_25823,rule_25824,rule_25825,rule_25826,rule_25827,rule_25828,rule_25829,rule_25830,rule_25831,rule_25832,rule_25833,rule_25834,rule_25835,rule_25836,rule_25837,rule_25838,rule_25839,rule_25840,rule_25841,rule_25842,rule_25843,rule_25844,rule_25845,rule_25846,rule_25847,rule_25848,rule_25849,rule_25850,rule_25851,rule_25852,rule_25853,rule_25854,rule_25855,rule_25856,rule_25857,rule_25858,rule_25859,rule_25860,rule_25861,rule_25862,rule_25863,rule_25864,rule_25865,rule_25866,rule_25867,rule_25868,rule_25869,rule_25870,rule_25871,rule_25872,rule_25873,rule_25874,rule_25875,rule_25876,rule_25877,rule_25878,rule_25879,rule_25880,rule_25881,rule_25882,rule_25883,rule_25884,rule_25885,rule_25886,rule_25887,rule_25888,rule_25889,rule_25890,rule_25891,rule_25892,rule_25893,rule_25894,rule_25895,rule_25896,rule_25897,rule_25898,rule_25899,rule_25900,rule_25901,rule_25902,rule_25903,rule_25904,rule_25905,rule_25906,rule_25907,rule_25908,rule_25909,rule_25910,rule_25911,rule_25912,rule_25913,rule_25914,rule_25915,rule_25916,rule_25917,rule_25918,rule_25919,rule_25920,rule_25921,rule_25922,rule_25923,rule_25924,rule_25925,rule_25926,rule_25927,rule_25928,rule_25929,rule_25930,rule_25931,rule_25932,rule_25933,rule_25934,rule_25935,rule_25936,rule_25937,rule_25938,rule_25939,rule_25940,rule_25941,rule_25942,rule_25943,rule_25944,rule_25945,rule_25946,rule_25947,rule_25948,rule_25949,rule_25950,rule_25951,rule_25952,rule_25953,rule_25954,rule_25955,rule_25956,rule_25957,rule_25958,rule_25959,rule_25960,rule_25961,rule_25962,rule_25963,rule_25964,rule_25965,rule_25966,rule_25967,rule_25968,rule_25969,rule_25970,rule_25971,rule_25972,rule_25973,rule_25974,rule_25975,rule_25976,rule_25977,rule_25978,rule_25979,rule_25980,rule_25981,rule_25982,rule_25983,rule_25984,rule_25985,rule_25986,rule_25987,rule_25988,rule_25989,rule_25990,rule_25991,rule_25992,rule_25993,rule_25994,rule_25995,rule_25996,rule_25997,rule_25998,rule_25999,rule_26000,rule_26001,rule_26002,rule_26003,rule_26004,rule_26005,rule_26006,rule_26007,rule_26008,rule_26009,rule_26010,rule_26011,rule_26012,rule_26013,rule_26014,rule_26015,rule_26016,rule_26017,rule_26018,rule_26019,rule_26020,rule_26021,rule_26022,rule_26023,rule_26024,rule_26025,rule_26026,rule_26027,rule_26028,rule_26029,rule_26030,rule_26031,rule_26032,rule_26033,rule_26034,rule_26035,rule_26036,rule_26037,rule_26038,rule_26039,rule_26040,rule_26041,rule_26042,rule_26043,rule_26044,rule_26045,rule_26046,rule_26047,rule_26048,rule_26049,rule_26050,rule_26051,rule_26052,rule_26053,rule_26054,rule_26055,rule_26056,rule_26057,rule_26058,rule_26059,rule_26060,rule_26061,rule_26062,rule_26063,rule_26064,rule_26065,rule_26066,rule_26067,rule_26068,rule_26069,rule_26070,rule_26071,rule_26072,rule_26073,rule_26074,rule_26075,rule_26076,rule_26077,rule_26078,rule_26079,rule_26080,rule_26081,rule_26082,rule_26083,rule_26084,rule_26085,rule_26086,rule_26087,rule_26088,rule_26089,rule_26090,rule_26091,rule_26092,rule_26093,rule_26094,rule_26095,rule_26096,rule_26097,rule_26098,rule_26099,rule_26100,rule_26101,rule_26102,rule_26103,rule_26104,rule_26105,rule_26106,rule_26107,rule_26108,rule_26109,rule_26110,rule_26111,rule_26112,rule_26113,rule_26114,rule_26115,rule_26116,rule_26117,rule_26118,rule_26119,rule_26120,rule_26121,rule_26122,rule_26123,rule_26124,rule_26125,rule_26126,rule_26127,rule_26128,rule_26129,rule_26130,rule_26131,rule_26132,rule_26133,rule_26134,rule_26135,rule_26136,rule_26137,rule_26138,rule_26139,rule_26140,rule_26141,rule_26142,rule_26143,rule_26144,rule_26145,rule_26146,rule_26147,rule_26148,rule_26149,rule_26150,rule_26151,rule_26152,rule_26153,rule_26154,rule_26155,rule_26156,rule_26157,rule_26158,rule_26159,rule_26160,rule_26161,rule_26162,rule_26163,rule_26164,rule_26165,rule_26166,rule_26167,rule_26168,rule_26169,rule_26170,rule_26171,rule_26172,rule_26173,rule_26174,rule_26175,rule_26176,rule_26177,rule_26178,rule_26179,rule_26180,rule_26181,rule_26182,rule_26183,rule_26184,rule_26185,rule_26186,rule_26187,rule_26188,rule_26189,rule_26190,rule_26191,rule_26192,rule_26193,rule_26194,rule_26195,rule_26196,rule_26197,rule_26198,rule_26199,rule_26200,rule_26201,rule_26202,rule_26203,rule_26204,rule_26205,rule_26206,rule_26207,rule_26208,rule_26209,rule_26210,rule_26211,rule_26212,rule_26213,rule_26214,rule_26215,rule_26216,rule_26217,rule_26218,rule_26219,rule_26220,rule_26221,rule_26222,rule_26223,rule_26224,rule_26225,rule_26226,rule_26227,rule_26228,rule_26229,rule_26230,rule_26231,rule_26232,rule_26233,rule_26234,rule_26235,rule_26236,rule_26237,rule_26238,rule_26239,rule_26240,rule_26241,rule_26242,rule_26243,rule_26244,rule_26245,rule_26246,rule_26247,rule_26248,rule_26249,rule_26250,rule_26251,rule_26252,rule_26253,rule_26254,rule_26255,rule_26256,rule_26257,rule_26258,rule_26259,rule_26260,rule_26261,rule_26262,rule_26263,rule_26264,rule_26265,rule_26266,rule_26267,rule_26268,rule_26269,rule_26270,rule_26271,rule_26272,rule_26273,rule_26274,rule_26275,rule_26276,rule_26277,rule_26278,rule_26279,rule_26280,rule_26281,rule_26282,rule_26283,rule_26284,rule_26285,rule_26286,rule_26287,rule_26288,rule_26289,rule_26290,rule_26291,rule_26292,rule_26293,rule_26294,rule_26295,rule_26296,rule_26297,rule_26298,rule_26299,rule_26300,rule_26301,rule_26302,rule_26303,rule_26304,rule_26305,rule_26306,rule_26307,rule_26308,rule_26309,rule_26310,rule_26311,rule_26312,rule_26313,rule_26314,rule_26315,rule_26316,rule_26317,rule_26318,rule_26319,rule_26320,rule_26321,rule_26322,rule_26323,rule_26324,rule_26325,rule_26326,rule_26327,rule_26328,rule_26329,rule_26330,rule_26331,rule_26332,rule_26333,rule_26334,rule_26335,rule_26336,rule_26337,rule_26338,rule_26339,rule_26340,rule_26341,rule_26342,rule_26343,rule_26344,rule_26345,rule_26346,rule_26347,rule_26348,rule_26349,rule_26350,rule_26351,rule_26352,rule_26353,rule_26354,rule_26355,rule_26356,rule_26357,rule_26358,rule_26359,rule_26360,rule_26361,rule_26362,rule_26363,rule_26364,rule_26365,rule_26366,rule_26367,rule_26368,rule_26369,rule_26370,rule_26371,rule_26372,rule_26373,rule_26374,rule_26375,rule_26376,rule_26377,rule_26378,rule_26379,rule_26380,rule_26381,rule_26382,rule_26383,rule_26384,rule_26385,rule_26386,rule_26387,rule_26388,rule_26389,rule_26390,rule_26391,rule_26392,rule_26393,rule_26394,rule_26395,rule_26396,rule_26397,rule_26398,rule_26399,rule_26400,rule_26401,rule_26402,rule_26403,rule_26404,rule_26405,rule_26406,rule_26407,rule_26408,rule_26409,rule_26410,rule_26411,rule_26412,rule_26413,rule_26414,rule_26415,rule_26416,rule_26417,rule_26418,rule_26419,rule_26420,rule_26421,rule_26422,rule_26423,rule_26424,rule_26425,rule_26426,rule_26427,rule_26428,rule_26429,rule_26430,rule_26431,rule_26432,rule_26433,rule_26434,rule_26435,rule_26436,rule_26437,rule_26438,rule_26439,rule_26440,rule_26441,rule_26442,rule_26443,rule_26444,rule_26445,rule_26446,rule_26447,rule_26448,rule_26449,rule_26450,rule_26451,rule_26452,rule_26453,rule_26454,rule_26455,rule_26456,rule_26457,rule_26458,rule_26459,rule_26460,rule_26461,rule_26462,rule_26463,rule_26464,rule_26465,rule_26466,rule_26467,rule_26468,rule_26469,rule_26470,rule_26471,rule_26472,rule_26473,rule_26474,rule_26475,rule_26476,rule_26477,rule_26478,rule_26479,rule_26480,rule_26481,rule_26482,rule_26483,rule_26484,rule_26485,rule_26486,rule_26487,rule_26488,rule_26489,rule_26490,rule_26491,rule_26492,rule_26493,rule_26494,rule_26495,rule_26496,rule_26497,rule_26498,rule_26499,rule_26500,rule_26501,rule_26502,rule_26503,rule_26504,rule_26505,rule_26506,rule_26507,rule_26508,rule_26509,rule_26510,rule_26511,rule_26512,rule_26513,rule_26514,rule_26515,rule_26516,rule_26517,rule_26518,rule_26519,rule_26520,rule_26521,rule_26522,rule_26523,rule_26524,rule_26525,rule_26526,rule_26527,rule_26528,rule_26529,rule_26530,rule_26531,rule_26532,rule_26533,rule_26534,rule_26535,rule_26536,rule_26537,rule_26538,rule_26539,rule_26540,rule_26541,rule_26542,rule_26543,rule_26544,rule_26545,rule_26546,rule_26547,rule_26548,rule_26549,rule_26550,rule_26551,rule_26552,rule_26553,rule_26554,rule_26555,rule_26556,rule_26557,rule_26558,rule_26559,rule_26560,rule_26561,rule_26562,rule_26563,rule_26564,rule_26565,rule_26566,rule_26567,rule_26568,rule_26569,rule_26570,rule_26571,rule_26572,rule_26573,rule_26574,rule_26575,rule_26576,rule_26577,rule_26578,rule_26579,rule_26580,rule_26581,rule_26582,rule_26583,rule_26584,rule_26585,rule_26586,rule_26587,rule_26588,rule_26589,rule_26590,rule_26591,rule_26592,rule_26593,rule_26594,rule_26595,rule_26596,rule_26597,rule_26598,rule_26599,rule_26600,rule_26601,rule_26602,rule_26603,rule_26604,rule_26605,rule_26606,rule_26607,rule_26608,rule_26609,rule_26610,rule_26611,rule_26612,rule_26613,rule_26614,rule_26615,rule_26616,rule_26617,rule_26618,rule_26619,rule_26620,rule_26621,rule_26622,rule_26623,rule_26624,rule_26625,rule_26626,rule_26627,rule_26628,rule_26629,rule_26630,rule_26631,rule_26632,rule_26633,rule_26634,rule_26635,rule_26636,rule_26637,rule_26638,rule_26639,rule_26640,rule_26641,rule_26642,rule_26643,rule_26644,rule_26645,rule_26646,rule_26647,rule_26648,rule_26649,rule_26650,rule_26651,rule_26652,rule_26653,rule_26654,rule_26655,rule_26656,rule_26657,rule_26658,rule_26659,rule_26660,rule_26661,rule_26662,rule_26663,rule_26664,rule_26665,rule_26666,rule_26667,rule_26668,rule_26669,rule_26670,rule_26671,rule_26672,rule_26673,rule_26674,rule_26675,rule_26676,rule_26677,rule_26678,rule_26679,rule_26680,rule_26681,rule_26682,rule_26683,rule_26684,rule_26685,rule_26686,rule_26687,rule_26688,rule_26689,rule_26690,rule_26691,rule_26692,rule_26693,rule_26694,rule_26695,rule_26696,rule_26697,rule_26698,rule_26699,rule_26700,rule_26701,rule_26702,rule_26703,rule_26704,rule_26705,rule_26706,rule_26707,rule_26708,rule_26709,rule_26710,rule_26711,rule_26712,rule_26713,rule_26714,rule_26715,rule_26716,rule_26717,rule_26718,rule_26719,rule_26720,rule_26721,rule_26722,rule_26723,rule_26724,rule_26725,rule_26726,rule_26727,rule_26728,rule_26729,rule_26730,rule_26731,rule_26732,rule_26733,rule_26734,rule_26735,rule_26736,rule_26737,rule_26738,rule_26739,rule_26740,rule_26741,rule_26742,rule_26743,rule_26744,rule_26745,rule_26746,rule_26747,rule_26748,rule_26749,rule_26750,rule_26751,rule_26752,rule_26753,rule_26754,rule_26755,rule_26756,rule_26757,rule_26758,rule_26759,rule_26760,rule_26761,rule_26762,rule_26763,rule_26764,rule_26765,rule_26766,rule_26767,rule_26768,rule_26769,rule_26770,rule_26771,rule_26772,rule_26773,rule_26774,rule_26775,rule_26776,rule_26777,rule_26778,rule_26779,rule_26780,rule_26781,rule_26782,rule_26783,rule_26784,rule_26785,rule_26786,rule_26787,rule_26788,rule_26789,rule_26790,rule_26791,rule_26792,rule_26793,rule_26794,rule_26795,rule_26796,rule_26797,rule_26798,rule_26799,rule_26800,rule_26801,rule_26802,rule_26803,rule_26804,rule_26805,rule_26806,rule_26807,rule_26808,rule_26809,rule_26810,rule_26811,rule_26812,rule_26813,rule_26814,rule_26815,rule_26816,rule_26817,rule_26818,rule_26819,rule_26820,rule_26821,rule_26822,rule_26823,rule_26824,rule_26825,rule_26826,rule_26827,rule_26828,rule_26829,rule_26830,rule_26831,rule_26832,rule_26833,rule_26834,rule_26835,rule_26836,rule_26837,rule_26838,rule_26839,rule_26840,rule_26841,rule_26842,rule_26843,rule_26844,rule_26845,rule_26846,rule_26847,rule_26848,rule_26849,rule_26850,rule_26851,rule_26852,rule_26853,rule_26854,rule_26855,rule_26856,rule_26857,rule_26858,rule_26859,rule_26860,rule_26861,rule_26862,rule_26863,rule_26864,rule_26865,rule_26866,rule_26867,rule_26868,rule_26869,rule_26870,rule_26871,rule_26872,rule_26873,rule_26874,rule_26875,rule_26876,rule_26877,rule_26878,rule_26879,rule_26880,rule_26881,rule_26882,rule_26883,rule_26884,rule_26885,rule_26886,rule_26887,rule_26888,rule_26889,rule_26890,rule_26891,rule_26892,rule_26893,rule_26894,rule_26895,rule_26896,rule_26897,rule_26898,rule_26899,rule_26900,rule_26901,rule_26902,rule_26903,rule_26904,rule_26905,rule_26906,rule_26907,rule_26908,rule_26909,rule_26910,rule_26911,rule_26912,rule_26913,rule_26914,rule_26915,rule_26916,rule_26917,rule_26918,rule_26919,rule_26920,rule_26921,rule_26922,rule_26923,rule_26924,rule_26925,rule_26926,rule_26927,rule_26928,rule_26929,rule_26930,rule_26931,rule_26932,rule_26933,rule_26934,rule_26935,rule_26936,rule_26937,rule_26938,rule_26939,rule_26940,rule_26941,rule_26942,rule_26943,rule_26944,rule_26945,rule_26946,rule_26947,rule_26948,rule_26949,rule_26950,rule_26951,rule_26952,rule_26953,rule_26954,rule_26955,rule_26956,rule_26957,rule_26958,rule_26959,rule_26960,rule_26961,rule_26962,rule_26963,rule_26964,rule_26965,rule_26966,rule_26967,rule_26968,rule_26969,rule_26970,rule_26971,rule_26972,rule_26973,rule_26974,rule_26975,rule_26976,rule_26977,rule_26978,rule_26979,rule_26980,rule_26981,rule_26982,rule_26983,rule_26984,rule_26985,rule_26986,rule_26987,rule_26988,rule_26989,rule_26990,rule_26991,rule_26992,rule_26993,rule_26994,rule_26995,rule_26996,rule_26997,rule_26998,rule_26999,rule_27000,rule_27001,rule_27002,rule_27003,rule_27004,rule_27005,rule_27006,rule_27007,rule_27008,rule_27009,rule_27010,rule_27011,rule_27012,rule_27013,rule_27014,rule_27015,rule_27016,rule_27017,rule_27018,rule_27019,rule_27020,rule_27021,rule_27022,rule_27023,rule_27024,rule_27025,rule_27026,rule_27027,rule_27028,rule_27029,rule_27030,rule_27031,rule_27032,rule_27033,rule_27034,rule_27035,rule_27036,rule_27037,rule_27038,rule_27039,rule_27040,rule_27041,rule_27042,rule_27043,rule_27044,rule_27045,rule_27046,rule_27047,rule_27048,rule_27049,rule_27050,rule_27051,rule_27052,rule_27053,rule_27054,rule_27055,rule_27056,rule_27057,rule_27058,rule_27059,rule_27060,rule_27061,rule_27062,rule_27063,rule_27064,rule_27065,rule_27066,rule_27067,rule_27068,rule_27069,rule_27070,rule_27071,rule_27072,rule_27073,rule_27074,rule_27075,rule_27076,rule_27077,rule_27078,rule_27079,rule_27080,rule_27081,rule_27082,rule_27083,rule_27084,rule_27085,rule_27086,rule_27087,rule_27088,rule_27089,rule_27090,rule_27091,rule_27092,rule_27093,rule_27094,rule_27095,rule_27096,rule_27097,rule_27098,rule_27099,rule_27100,rule_27101,rule_27102,rule_27103,rule_27104,rule_27105,rule_27106,rule_27107,rule_27108,rule_27109,rule_27110,rule_27111,rule_27112,rule_27113,rule_27114,rule_27115,rule_27116,rule_27117,rule_27118,rule_27119,rule_27120,rule_27121,rule_27122,rule_27123,rule_27124,rule_27125,rule_27126,rule_27127,rule_27128,rule_27129,rule_27130,rule_27131,rule_27132,rule_27133,rule_27134,rule_27135,rule_27136,rule_27137,rule_27138,rule_27139,rule_27140,rule_27141,rule_27142,rule_27143,rule_27144,rule_27145,rule_27146,rule_27147,rule_27148,rule_27149,rule_27150,rule_27151,rule_27152,rule_27153,rule_27154,rule_27155,rule_27156,rule_27157,rule_27158,rule_27159,rule_27160,rule_27161,rule_27162,rule_27163,rule_27164,rule_27165,rule_27166,rule_27167,rule_27168,rule_27169,rule_27170,rule_27171,rule_27172,rule_27173,rule_27174,rule_27175,rule_27176,rule_27177,rule_27178,rule_27179,rule_27180,rule_27181,rule_27182,rule_27183,rule_27184,rule_27185,rule_27186,rule_27187,rule_27188,rule_27189,rule_27190,rule_27191,rule_27192,rule_27193,rule_27194,rule_27195,rule_27196,rule_27197,rule_27198,rule_27199,rule_27200,rule_27201,rule_27202,rule_27203,rule_27204,rule_27205,rule_27206,rule_27207,rule_27208,rule_27209,rule_27210,rule_27211,rule_27212,rule_27213,rule_27214,rule_27215,rule_27216,rule_27217,rule_27218,rule_27219,rule_27220,rule_27221,rule_27222,rule_27223,rule_27224,rule_27225,rule_27226,rule_27227,rule_27228,rule_27229,rule_27230,rule_27231,rule_27232,rule_27233,rule_27234,rule_27235,rule_27236,rule_27237,rule_27238,rule_27239,rule_27240,rule_27241,rule_27242,rule_27243,rule_27244,rule_27245,rule_27246,rule_27247,rule_27248,rule_27249,rule_27250,rule_27251,rule_27252,rule_27253,rule_27254,rule_27255,rule_27256,rule_27257,rule_27258,rule_27259,rule_27260,rule_27261,rule_27262,rule_27263,rule_27264,rule_27265,rule_27266,rule_27267,rule_27268,rule_27269,rule_27270,rule_27271,rule_27272,rule_27273,rule_27274,rule_27275,rule_27276,rule_27277,rule_27278,rule_27279,rule_27280,rule_27281,rule_27282,rule_27283,rule_27284,rule_27285,rule_27286,rule_27287,rule_27288,rule_27289,rule_27290,rule_27291,rule_27292,rule_27293,rule_27294,rule_27295,rule_27296,rule_27297,rule_27298,rule_27299,rule_27300,rule_27301,rule_27302,rule_27303,rule_27304,rule_27305,rule_27306,rule_27307,rule_27308,rule_27309,rule_27310,rule_27311,rule_27312,rule_27313,rule_27314,rule_27315,rule_27316,rule_27317,rule_27318,rule_27319,rule_27320,rule_27321,rule_27322,rule_27323,rule_27324,rule_27325,rule_27326,rule_27327,rule_27328,rule_27329,rule_27330,rule_27331,rule_27332,rule_27333,rule_27334,rule_27335,rule_27336,rule_27337,rule_27338,rule_27339,rule_27340,rule_27341,rule_27342,rule_27343,rule_27344,rule_27345,rule_27346,rule_27347,rule_27348,rule_27349,rule_27350,rule_27351,rule_27352,rule_27353,rule_27354,rule_27355,rule_27356,rule_27357,rule_27358,rule_27359,rule_27360,rule_27361,rule_27362,rule_27363,rule_27364,rule_27365,rule_27366,rule_27367,rule_27368,rule_27369,rule_27370,rule_27371,rule_27372,rule_27373,rule_27374,rule_27375,rule_27376,rule_27377,rule_27378,rule_27379,rule_27380,rule_27381,rule_27382,rule_27383,rule_27384,rule_27385,rule_27386,rule_27387,rule_27388,rule_27389,rule_27390,rule_27391,rule_27392,rule_27393,rule_27394,rule_27395,rule_27396,rule_27397,rule_27398,rule_27399,rule_27400,rule_27401,rule_27402,rule_27403,rule_27404,rule_27405,rule_27406,rule_27407,rule_27408,rule_27409,rule_27410,rule_27411,rule_27412,rule_27413,rule_27414,rule_27415,rule_27416,rule_27417,rule_27418,rule_27419,rule_27420,rule_27421,rule_27422,rule_27423,rule_27424,rule_27425,rule_27426,rule_27427,rule_27428,rule_27429,rule_27430,rule_27431,rule_27432,rule_27433,rule_27434,rule_27435,rule_27436,rule_27437,rule_27438,rule_27439,rule_27440,rule_27441,rule_27442,rule_27443,rule_27444,rule_27445,rule_27446,rule_27447,rule_27448,rule_27449,rule_27450,rule_27451,rule_27452,rule_27453,rule_27454,rule_27455,rule_27456,rule_27457,rule_27458,rule_27459,rule_27460,rule_27461,rule_27462,rule_27463,rule_27464,rule_27465,rule_27466,rule_27467,rule_27468,rule_27469,rule_27470,rule_27471,rule_27472,rule_27473,rule_27474,rule_27475,rule_27476,rule_27477,rule_27478,rule_27479,rule_27480,rule_27481,rule_27482,rule_27483,rule_27484,rule_27485,rule_27486,rule_27487,rule_27488,rule_27489,rule_27490,rule_27491,rule_27492,rule_27493,rule_27494,rule_27495,rule_27496,rule_27497,rule_27498,rule_27499,rule_27500,rule_27501,rule_27502,rule_27503,rule_27504,rule_27505,rule_27506,rule_27507,rule_27508,rule_27509,rule_27510,rule_27511,rule_27512,rule_27513,rule_27514,rule_27515,rule_27516,rule_27517,rule_27518,rule_27519,rule_27520,rule_27521,rule_27522,rule_27523,rule_27524,rule_27525,rule_27526,rule_27527,rule_27528,rule_27529,rule_27530,rule_27531,rule_27532,rule_27533,rule_27534,rule_27535,rule_27536,rule_27537,rule_27538,rule_27539,rule_27540,rule_27541,rule_27542,rule_27543,rule_27544,rule_27545,rule_27546,rule_27547,rule_27548,rule_27549,rule_27550,rule_27551,rule_27552,rule_27553,rule_27554,rule_27555,rule_27556,rule_27557,rule_27558,rule_27559,rule_27560,rule_27561,rule_27562,rule_27563,rule_27564,rule_27565,rule_27566,rule_27567,rule_27568,rule_27569,rule_27570,rule_27571,rule_27572,rule_27573,rule_27574,rule_27575,rule_27576,rule_27577,rule_27578,rule_27579,rule_27580,rule_27581,rule_27582,rule_27583,rule_27584,rule_27585,rule_27586,rule_27587,rule_27588,rule_27589,rule_27590,rule_27591,rule_27592,rule_27593,rule_27594,rule_27595,rule_27596,rule_27597,rule_27598,rule_27599,rule_27600,rule_27601,rule_27602,rule_27603,rule_27604,rule_27605,rule_27606,rule_27607,rule_27608,rule_27609,rule_27610,rule_27611,rule_27612,rule_27613,rule_27614,rule_27615,rule_27616,rule_27617,rule_27618,rule_27619,rule_27620,rule_27621,rule_27622,rule_27623,rule_27624,rule_27625,rule_27626,rule_27627,rule_27628,rule_27629,rule_27630,rule_27631,rule_27632,rule_27633,rule_27634,rule_27635,rule_27636,rule_27637,rule_27638,rule_27639,rule_27640,rule_27641,rule_27642,rule_27643,rule_27644,rule_27645,rule_27646,rule_27647,rule_27648,rule_27649,rule_27650,rule_27651,rule_27652,rule_27653,rule_27654,rule_27655,rule_27656,rule_27657,rule_27658,rule_27659,rule_27660,rule_27661,rule_27662,rule_27663,rule_27664,rule_27665,rule_27666,rule_27667,rule_27668,rule_27669,rule_27670,rule_27671,rule_27672,rule_27673,rule_27674,rule_27675,rule_27676,rule_27677,rule_27678,rule_27679,rule_27680,rule_27681,rule_27682,rule_27683,rule_27684,rule_27685,rule_27686,rule_27687,rule_27688,rule_27689,rule_27690,rule_27691,rule_27692,rule_27693,rule_27694,rule_27695,rule_27696,rule_27697,rule_27698,rule_27699,rule_27700,rule_27701,rule_27702,rule_27703,rule_27704,rule_27705,rule_27706,rule_27707,rule_27708,rule_27709,rule_27710,rule_27711,rule_27712,rule_27713,rule_27714,rule_27715,rule_27716,rule_27717,rule_27718,rule_27719,rule_27720,rule_27721,rule_27722,rule_27723,rule_27724,rule_27725,rule_27726,rule_27727,rule_27728,rule_27729,rule_27730,rule_27731,rule_27732,rule_27733,rule_27734,rule_27735,rule_27736,rule_27737,rule_27738,rule_27739,rule_27740,rule_27741,rule_27742,rule_27743,rule_27744,rule_27745,rule_27746,rule_27747,rule_27748,rule_27749,rule_27750,rule_27751,rule_27752,rule_27753,rule_27754,rule_27755,rule_27756,rule_27757,rule_27758,rule_27759,rule_27760,rule_27761,rule_27762,rule_27763,rule_27764,rule_27765,rule_27766,rule_27767,rule_27768,rule_27769,rule_27770,rule_27771,rule_27772,rule_27773,rule_27774,rule_27775,rule_27776,rule_27777,rule_27778,rule_27779,rule_27780,rule_27781,rule_27782,rule_27783,rule_27784,rule_27785,rule_27786,rule_27787,rule_27788,rule_27789,rule_27790,rule_27791,rule_27792,rule_27793,rule_27794,rule_27795,rule_27796,rule_27797,rule_27798,rule_27799,rule_27800,rule_27801,rule_27802,rule_27803,rule_27804,rule_27805,rule_27806,rule_27807,rule_27808,rule_27809,rule_27810,rule_27811,rule_27812,rule_27813,rule_27814,rule_27815,rule_27816,rule_27817,rule_27818,rule_27819,rule_27820,rule_27821,rule_27822,rule_27823,rule_27824,rule_27825,rule_27826,rule_27827,rule_27828,rule_27829,rule_27830,rule_27831,rule_27832,rule_27833,rule_27834,rule_27835,rule_27836,rule_27837,rule_27838,rule_27839,rule_27840,rule_27841,rule_27842,rule_27843,rule_27844,rule_27845,rule_27846,rule_27847,rule_27848,rule_27849,rule_27850,rule_27851,rule_27852,rule_27853,rule_27854,rule_27855,rule_27856,rule_27857,rule_27858,rule_27859,rule_27860,rule_27861,rule_27862,rule_27863,rule_27864,rule_27865,rule_27866,rule_27867,rule_27868,rule_27869,rule_27870,rule_27871,rule_27872,rule_27873,rule_27874,rule_27875,rule_27876,rule_27877,rule_27878,rule_27879,rule_27880,rule_27881,rule_27882,rule_27883,rule_27884,rule_27885,rule_27886,rule_27887,rule_27888,rule_27889,rule_27890,rule_27891,rule_27892,rule_27893,rule_27894,rule_27895,rule_27896,rule_27897,rule_27898,rule_27899,rule_27900,rule_27901,rule_27902,rule_27903,rule_27904,rule_27905,rule_27906,rule_27907,rule_27908,rule_27909,rule_27910,rule_27911,rule_27912,rule_27913,rule_27914,rule_27915,rule_27916,rule_27917,rule_27918,rule_27919,rule_27920,rule_27921,rule_27922,rule_27923,rule_27924,rule_27925,rule_27926,rule_27927,rule_27928,rule_27929,rule_27930,rule_27931,rule_27932,rule_27933,rule_27934,rule_27935,rule_27936,rule_27937,rule_27938,rule_27939,rule_27940,rule_27941,rule_27942,rule_27943,rule_27944,rule_27945,rule_27946,rule_27947,rule_27948,rule_27949,rule_27950,rule_27951,rule_27952,rule_27953,rule_27954,rule_27955,rule_27956,rule_27957,rule_27958,rule_27959,rule_27960,rule_27961,rule_27962,rule_27963,rule_27964,rule_27965,rule_27966,rule_27967,rule_27968,rule_27969,rule_27970,rule_27971,rule_27972,rule_27973,rule_27974,rule_27975,rule_27976,rule_27977,rule_27978,rule_27979,rule_27980,rule_27981,rule_27982,rule_27983,rule_27984,rule_27985,rule_27986,rule_27987,rule_27988,rule_27989,rule_27990,rule_27991,rule_27992,rule_27993,rule_27994,rule_27995,rule_27996,rule_27997,rule_27998,rule_27999,rule_28000]
