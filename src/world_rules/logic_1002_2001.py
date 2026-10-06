# Bounded Earth-system feedbacks for commits 1002-2001.
import torch

_RATE = 2.0e-5

def _gate(world, variant):
    if variant == "baseline":
        return torch.ones_like(world.food)
    if variant == "dry_gate":
        return (1.0 - world.soil_moisture).clamp(0.0, 1.0)
    if variant == "wet_gate":
        return world.soil_moisture.clamp(0.0, 1.0)
    if variant == "heat_gate":
        return world.temperature.clamp(0.0, 1.0)
    if variant == "cold_gate":
        return (1.0 - world.temperature).clamp(0.0, 1.0)
    if variant == "fire_gate":
        return world.fire_risk.clamp(0.0, 1.0)
    if variant == "water_gate":
        return world.surface_water.clamp(0.0, 1.0)
    if variant == "scarcity_gate":
        return (1.0 - world.vegetation).clamp(0.0, 1.0)
    if variant == "biomass_gate":
        return world.biomass.clamp(0.0, 1.0)
    if variant == "stress_gate":
        return world.habitat_stress.clamp(0.0, 1.0)
    if variant == "seasonal_gate":
        return (0.5 + 0.5 * torch.sin(world.temperature * 3.14159265)).clamp(0.0, 1.0)
    if variant == "saturation":
        return (1.0 - world.temperature * 0.5).clamp(0.25, 1.0)
    if variant == "threshold":
        return (world.food > 0.5).to(world.food.dtype)
    if variant == "recovery":
        return (0.25 + 0.75 * world.biodiversity).clamp(0.25, 1.0)
    return torch.ones_like(world.food)

def _feedback(world, source_name, target_name, sign, variant):
    source = getattr(world, source_name).clamp(0.0, 1.0)
    target = getattr(world, target_name)
    gate = _gate(world, variant)
    desired = source * gate if sign > 0 else 1.0 - source * gate
    setattr(world, target_name, (target + _RATE * (desired - target)).clamp(0.0, 1.0))

def logic_1002(world):
    # rainfall raises surface water; direct.
    _feedback(world, 'rain', 'surface_water', 1, 'baseline')

def logic_1003(world):
    # rainfall raises surface water; stronger when soil is dry.
    _feedback(world, 'rain', 'surface_water', 1, 'dry_gate')

def logic_1004(world):
    # rainfall raises surface water; stronger when soil is wet.
    _feedback(world, 'rain', 'surface_water', 1, 'wet_gate')

def logic_1005(world):
    # rainfall raises surface water; stronger when temperature is high.
    _feedback(world, 'rain', 'surface_water', 1, 'heat_gate')

def logic_1006(world):
    # rainfall raises surface water; stronger when temperature is low.
    _feedback(world, 'rain', 'surface_water', 1, 'cold_gate')

def logic_1007(world):
    # rainfall raises surface water; stronger under fire pressure.
    _feedback(world, 'rain', 'surface_water', 1, 'fire_gate')

def logic_1008(world):
    # rainfall raises surface water; stronger when surface water is high.
    _feedback(world, 'rain', 'surface_water', 1, 'water_gate')

def logic_1009(world):
    # rainfall raises surface water; stronger when vegetation is scarce.
    _feedback(world, 'rain', 'surface_water', 1, 'scarcity_gate')

def logic_1010(world):
    # rainfall raises surface water; stronger when biomass is high.
    _feedback(world, 'rain', 'surface_water', 1, 'biomass_gate')

def logic_1011(world):
    # rainfall raises surface water; stronger under habitat stress.
    _feedback(world, 'rain', 'surface_water', 1, 'stress_gate')

def logic_1012(world):
    # rainfall raises surface water; modulated by temperature.
    _feedback(world, 'rain', 'surface_water', 1, 'seasonal_gate')

def logic_1013(world):
    # rainfall raises surface water; saturates at high source levels.
    _feedback(world, 'rain', 'surface_water', 1, 'saturation')

def logic_1014(world):
    # rainfall raises surface water; activates above a food threshold.
    _feedback(world, 'rain', 'surface_water', 1, 'threshold')

def logic_1015(world):
    # rainfall raises surface water; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'rain', 'surface_water', 1, 'recovery')

def logic_1016(world):
    # rainfall wets soil; direct.
    _feedback(world, 'rain', 'soil_moisture', 1, 'baseline')

def logic_1017(world):
    # rainfall wets soil; stronger when soil is dry.
    _feedback(world, 'rain', 'soil_moisture', 1, 'dry_gate')

def logic_1018(world):
    # rainfall wets soil; stronger when soil is wet.
    _feedback(world, 'rain', 'soil_moisture', 1, 'wet_gate')

def logic_1019(world):
    # rainfall wets soil; stronger when temperature is high.
    _feedback(world, 'rain', 'soil_moisture', 1, 'heat_gate')

def logic_1020(world):
    # rainfall wets soil; stronger when temperature is low.
    _feedback(world, 'rain', 'soil_moisture', 1, 'cold_gate')

def logic_1021(world):
    # rainfall wets soil; stronger under fire pressure.
    _feedback(world, 'rain', 'soil_moisture', 1, 'fire_gate')

def logic_1022(world):
    # rainfall wets soil; stronger when surface water is high.
    _feedback(world, 'rain', 'soil_moisture', 1, 'water_gate')

def logic_1023(world):
    # rainfall wets soil; stronger when vegetation is scarce.
    _feedback(world, 'rain', 'soil_moisture', 1, 'scarcity_gate')

def logic_1024(world):
    # rainfall wets soil; stronger when biomass is high.
    _feedback(world, 'rain', 'soil_moisture', 1, 'biomass_gate')

def logic_1025(world):
    # rainfall wets soil; stronger under habitat stress.
    _feedback(world, 'rain', 'soil_moisture', 1, 'stress_gate')

def logic_1026(world):
    # rainfall wets soil; modulated by temperature.
    _feedback(world, 'rain', 'soil_moisture', 1, 'seasonal_gate')

def logic_1027(world):
    # rainfall wets soil; saturates at high source levels.
    _feedback(world, 'rain', 'soil_moisture', 1, 'saturation')

def logic_1028(world):
    # rainfall wets soil; activates above a food threshold.
    _feedback(world, 'rain', 'soil_moisture', 1, 'threshold')

def logic_1029(world):
    # rainfall wets soil; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'rain', 'soil_moisture', 1, 'recovery')

def logic_1030(world):
    # rain recharges groundwater; direct.
    _feedback(world, 'rain', 'groundwater', 1, 'baseline')

def logic_1031(world):
    # rain recharges groundwater; stronger when soil is dry.
    _feedback(world, 'rain', 'groundwater', 1, 'dry_gate')

def logic_1032(world):
    # rain recharges groundwater; stronger when soil is wet.
    _feedback(world, 'rain', 'groundwater', 1, 'wet_gate')

def logic_1033(world):
    # rain recharges groundwater; stronger when temperature is high.
    _feedback(world, 'rain', 'groundwater', 1, 'heat_gate')

def logic_1034(world):
    # rain recharges groundwater; stronger when temperature is low.
    _feedback(world, 'rain', 'groundwater', 1, 'cold_gate')

def logic_1035(world):
    # rain recharges groundwater; stronger under fire pressure.
    _feedback(world, 'rain', 'groundwater', 1, 'fire_gate')

def logic_1036(world):
    # rain recharges groundwater; stronger when surface water is high.
    _feedback(world, 'rain', 'groundwater', 1, 'water_gate')

def logic_1037(world):
    # rain recharges groundwater; stronger when vegetation is scarce.
    _feedback(world, 'rain', 'groundwater', 1, 'scarcity_gate')

def logic_1038(world):
    # rain recharges groundwater; stronger when biomass is high.
    _feedback(world, 'rain', 'groundwater', 1, 'biomass_gate')

def logic_1039(world):
    # rain recharges groundwater; stronger under habitat stress.
    _feedback(world, 'rain', 'groundwater', 1, 'stress_gate')

def logic_1040(world):
    # rain recharges groundwater; modulated by temperature.
    _feedback(world, 'rain', 'groundwater', 1, 'seasonal_gate')

def logic_1041(world):
    # rain recharges groundwater; saturates at high source levels.
    _feedback(world, 'rain', 'groundwater', 1, 'saturation')

def logic_1042(world):
    # rain recharges groundwater; activates above a food threshold.
    _feedback(world, 'rain', 'groundwater', 1, 'threshold')

def logic_1043(world):
    # rain recharges groundwater; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'rain', 'groundwater', 1, 'recovery')

def logic_1044(world):
    # snowmelt supplies surface water; direct.
    _feedback(world, 'snowpack', 'surface_water', 1, 'baseline')

def logic_1045(world):
    # snowmelt supplies surface water; stronger when soil is dry.
    _feedback(world, 'snowpack', 'surface_water', 1, 'dry_gate')

def logic_1046(world):
    # snowmelt supplies surface water; stronger when soil is wet.
    _feedback(world, 'snowpack', 'surface_water', 1, 'wet_gate')

def logic_1047(world):
    # snowmelt supplies surface water; stronger when temperature is high.
    _feedback(world, 'snowpack', 'surface_water', 1, 'heat_gate')

def logic_1048(world):
    # snowmelt supplies surface water; stronger when temperature is low.
    _feedback(world, 'snowpack', 'surface_water', 1, 'cold_gate')

def logic_1049(world):
    # snowmelt supplies surface water; stronger under fire pressure.
    _feedback(world, 'snowpack', 'surface_water', 1, 'fire_gate')

def logic_1050(world):
    # snowmelt supplies surface water; stronger when surface water is high.
    _feedback(world, 'snowpack', 'surface_water', 1, 'water_gate')

def logic_1051(world):
    # snowmelt supplies surface water; stronger when vegetation is scarce.
    _feedback(world, 'snowpack', 'surface_water', 1, 'scarcity_gate')

def logic_1052(world):
    # snowmelt supplies surface water; stronger when biomass is high.
    _feedback(world, 'snowpack', 'surface_water', 1, 'biomass_gate')

def logic_1053(world):
    # snowmelt supplies surface water; stronger under habitat stress.
    _feedback(world, 'snowpack', 'surface_water', 1, 'stress_gate')

def logic_1054(world):
    # snowmelt supplies surface water; modulated by temperature.
    _feedback(world, 'snowpack', 'surface_water', 1, 'seasonal_gate')

def logic_1055(world):
    # snowmelt supplies surface water; saturates at high source levels.
    _feedback(world, 'snowpack', 'surface_water', 1, 'saturation')

def logic_1056(world):
    # snowmelt supplies surface water; activates above a food threshold.
    _feedback(world, 'snowpack', 'surface_water', 1, 'threshold')

def logic_1057(world):
    # snowmelt supplies surface water; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'snowpack', 'surface_water', 1, 'recovery')

def logic_1058(world):
    # snowpack supports groundwater recharge; direct.
    _feedback(world, 'snowpack', 'groundwater', 1, 'baseline')

def logic_1059(world):
    # snowpack supports groundwater recharge; stronger when soil is dry.
    _feedback(world, 'snowpack', 'groundwater', 1, 'dry_gate')

def logic_1060(world):
    # snowpack supports groundwater recharge; stronger when soil is wet.
    _feedback(world, 'snowpack', 'groundwater', 1, 'wet_gate')

def logic_1061(world):
    # snowpack supports groundwater recharge; stronger when temperature is high.
    _feedback(world, 'snowpack', 'groundwater', 1, 'heat_gate')

def logic_1062(world):
    # snowpack supports groundwater recharge; stronger when temperature is low.
    _feedback(world, 'snowpack', 'groundwater', 1, 'cold_gate')

def logic_1063(world):
    # snowpack supports groundwater recharge; stronger under fire pressure.
    _feedback(world, 'snowpack', 'groundwater', 1, 'fire_gate')

def logic_1064(world):
    # snowpack supports groundwater recharge; stronger when surface water is high.
    _feedback(world, 'snowpack', 'groundwater', 1, 'water_gate')

def logic_1065(world):
    # snowpack supports groundwater recharge; stronger when vegetation is scarce.
    _feedback(world, 'snowpack', 'groundwater', 1, 'scarcity_gate')

def logic_1066(world):
    # snowpack supports groundwater recharge; stronger when biomass is high.
    _feedback(world, 'snowpack', 'groundwater', 1, 'biomass_gate')

def logic_1067(world):
    # snowpack supports groundwater recharge; stronger under habitat stress.
    _feedback(world, 'snowpack', 'groundwater', 1, 'stress_gate')

def logic_1068(world):
    # snowpack supports groundwater recharge; modulated by temperature.
    _feedback(world, 'snowpack', 'groundwater', 1, 'seasonal_gate')

def logic_1069(world):
    # snowpack supports groundwater recharge; saturates at high source levels.
    _feedback(world, 'snowpack', 'groundwater', 1, 'saturation')

def logic_1070(world):
    # snowpack supports groundwater recharge; activates above a food threshold.
    _feedback(world, 'snowpack', 'groundwater', 1, 'threshold')

def logic_1071(world):
    # snowpack supports groundwater recharge; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'snowpack', 'groundwater', 1, 'recovery')

def logic_1072(world):
    # open water raises local humidity; direct.
    _feedback(world, 'surface_water', 'humidity', 1, 'baseline')

def logic_1073(world):
    # open water raises local humidity; stronger when soil is dry.
    _feedback(world, 'surface_water', 'humidity', 1, 'dry_gate')

def logic_1074(world):
    # open water raises local humidity; stronger when soil is wet.
    _feedback(world, 'surface_water', 'humidity', 1, 'wet_gate')

def logic_1075(world):
    # open water raises local humidity; stronger when temperature is high.
    _feedback(world, 'surface_water', 'humidity', 1, 'heat_gate')

def logic_1076(world):
    # open water raises local humidity; stronger when temperature is low.
    _feedback(world, 'surface_water', 'humidity', 1, 'cold_gate')

def logic_1077(world):
    # open water raises local humidity; stronger under fire pressure.
    _feedback(world, 'surface_water', 'humidity', 1, 'fire_gate')

def logic_1078(world):
    # open water raises local humidity; stronger when surface water is high.
    _feedback(world, 'surface_water', 'humidity', 1, 'water_gate')

def logic_1079(world):
    # open water raises local humidity; stronger when vegetation is scarce.
    _feedback(world, 'surface_water', 'humidity', 1, 'scarcity_gate')

def logic_1080(world):
    # open water raises local humidity; stronger when biomass is high.
    _feedback(world, 'surface_water', 'humidity', 1, 'biomass_gate')

def logic_1081(world):
    # open water raises local humidity; stronger under habitat stress.
    _feedback(world, 'surface_water', 'humidity', 1, 'stress_gate')

def logic_1082(world):
    # open water raises local humidity; modulated by temperature.
    _feedback(world, 'surface_water', 'humidity', 1, 'seasonal_gate')

def logic_1083(world):
    # open water raises local humidity; saturates at high source levels.
    _feedback(world, 'surface_water', 'humidity', 1, 'saturation')

def logic_1084(world):
    # open water raises local humidity; activates above a food threshold.
    _feedback(world, 'surface_water', 'humidity', 1, 'threshold')

def logic_1085(world):
    # open water raises local humidity; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'surface_water', 'humidity', 1, 'recovery')

def logic_1086(world):
    # persistent surface water expands wetlands; direct.
    _feedback(world, 'surface_water', 'wetland', 1, 'baseline')

def logic_1087(world):
    # persistent surface water expands wetlands; stronger when soil is dry.
    _feedback(world, 'surface_water', 'wetland', 1, 'dry_gate')

def logic_1088(world):
    # persistent surface water expands wetlands; stronger when soil is wet.
    _feedback(world, 'surface_water', 'wetland', 1, 'wet_gate')

def logic_1089(world):
    # persistent surface water expands wetlands; stronger when temperature is high.
    _feedback(world, 'surface_water', 'wetland', 1, 'heat_gate')

def logic_1090(world):
    # persistent surface water expands wetlands; stronger when temperature is low.
    _feedback(world, 'surface_water', 'wetland', 1, 'cold_gate')

def logic_1091(world):
    # persistent surface water expands wetlands; stronger under fire pressure.
    _feedback(world, 'surface_water', 'wetland', 1, 'fire_gate')

def logic_1092(world):
    # persistent surface water expands wetlands; stronger when surface water is high.
    _feedback(world, 'surface_water', 'wetland', 1, 'water_gate')

def logic_1093(world):
    # persistent surface water expands wetlands; stronger when vegetation is scarce.
    _feedback(world, 'surface_water', 'wetland', 1, 'scarcity_gate')

def logic_1094(world):
    # persistent surface water expands wetlands; stronger when biomass is high.
    _feedback(world, 'surface_water', 'wetland', 1, 'biomass_gate')

def logic_1095(world):
    # persistent surface water expands wetlands; stronger under habitat stress.
    _feedback(world, 'surface_water', 'wetland', 1, 'stress_gate')

def logic_1096(world):
    # persistent surface water expands wetlands; modulated by temperature.
    _feedback(world, 'surface_water', 'wetland', 1, 'seasonal_gate')

def logic_1097(world):
    # persistent surface water expands wetlands; saturates at high source levels.
    _feedback(world, 'surface_water', 'wetland', 1, 'saturation')

def logic_1098(world):
    # persistent surface water expands wetlands; activates above a food threshold.
    _feedback(world, 'surface_water', 'wetland', 1, 'threshold')

def logic_1099(world):
    # persistent surface water expands wetlands; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'surface_water', 'wetland', 1, 'recovery')

def logic_1100(world):
    # surface water supports algae; direct.
    _feedback(world, 'surface_water', 'algae', 1, 'baseline')

def logic_1101(world):
    # surface water supports algae; stronger when soil is dry.
    _feedback(world, 'surface_water', 'algae', 1, 'dry_gate')

def logic_1102(world):
    # surface water supports algae; stronger when soil is wet.
    _feedback(world, 'surface_water', 'algae', 1, 'wet_gate')

def logic_1103(world):
    # surface water supports algae; stronger when temperature is high.
    _feedback(world, 'surface_water', 'algae', 1, 'heat_gate')

def logic_1104(world):
    # surface water supports algae; stronger when temperature is low.
    _feedback(world, 'surface_water', 'algae', 1, 'cold_gate')

def logic_1105(world):
    # surface water supports algae; stronger under fire pressure.
    _feedback(world, 'surface_water', 'algae', 1, 'fire_gate')

def logic_1106(world):
    # surface water supports algae; stronger when surface water is high.
    _feedback(world, 'surface_water', 'algae', 1, 'water_gate')

def logic_1107(world):
    # surface water supports algae; stronger when vegetation is scarce.
    _feedback(world, 'surface_water', 'algae', 1, 'scarcity_gate')

def logic_1108(world):
    # surface water supports algae; stronger when biomass is high.
    _feedback(world, 'surface_water', 'algae', 1, 'biomass_gate')

def logic_1109(world):
    # surface water supports algae; stronger under habitat stress.
    _feedback(world, 'surface_water', 'algae', 1, 'stress_gate')

def logic_1110(world):
    # surface water supports algae; modulated by temperature.
    _feedback(world, 'surface_water', 'algae', 1, 'seasonal_gate')

def logic_1111(world):
    # surface water supports algae; saturates at high source levels.
    _feedback(world, 'surface_water', 'algae', 1, 'saturation')

def logic_1112(world):
    # surface water supports algae; activates above a food threshold.
    _feedback(world, 'surface_water', 'algae', 1, 'threshold')

def logic_1113(world):
    # surface water supports algae; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'surface_water', 'algae', 1, 'recovery')

def logic_1114(world):
    # groundwater buffers soil moisture; direct.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'baseline')

def logic_1115(world):
    # groundwater buffers soil moisture; stronger when soil is dry.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'dry_gate')

def logic_1116(world):
    # groundwater buffers soil moisture; stronger when soil is wet.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'wet_gate')

def logic_1117(world):
    # groundwater buffers soil moisture; stronger when temperature is high.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'heat_gate')

def logic_1118(world):
    # groundwater buffers soil moisture; stronger when temperature is low.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'cold_gate')

def logic_1119(world):
    # groundwater buffers soil moisture; stronger under fire pressure.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'fire_gate')

def logic_1120(world):
    # groundwater buffers soil moisture; stronger when surface water is high.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'water_gate')

def logic_1121(world):
    # groundwater buffers soil moisture; stronger when vegetation is scarce.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'scarcity_gate')

def logic_1122(world):
    # groundwater buffers soil moisture; stronger when biomass is high.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'biomass_gate')

def logic_1123(world):
    # groundwater buffers soil moisture; stronger under habitat stress.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'stress_gate')

def logic_1124(world):
    # groundwater buffers soil moisture; modulated by temperature.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'seasonal_gate')

def logic_1125(world):
    # groundwater buffers soil moisture; saturates at high source levels.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'saturation')

def logic_1126(world):
    # groundwater buffers soil moisture; activates above a food threshold.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'threshold')

def logic_1127(world):
    # groundwater buffers soil moisture; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'groundwater', 'soil_moisture', 1, 'recovery')

def logic_1128(world):
    # groundwater supports wetlands; direct.
    _feedback(world, 'groundwater', 'wetland', 1, 'baseline')

def logic_1129(world):
    # groundwater supports wetlands; stronger when soil is dry.
    _feedback(world, 'groundwater', 'wetland', 1, 'dry_gate')

def logic_1130(world):
    # groundwater supports wetlands; stronger when soil is wet.
    _feedback(world, 'groundwater', 'wetland', 1, 'wet_gate')

def logic_1131(world):
    # groundwater supports wetlands; stronger when temperature is high.
    _feedback(world, 'groundwater', 'wetland', 1, 'heat_gate')

def logic_1132(world):
    # groundwater supports wetlands; stronger when temperature is low.
    _feedback(world, 'groundwater', 'wetland', 1, 'cold_gate')

def logic_1133(world):
    # groundwater supports wetlands; stronger under fire pressure.
    _feedback(world, 'groundwater', 'wetland', 1, 'fire_gate')

def logic_1134(world):
    # groundwater supports wetlands; stronger when surface water is high.
    _feedback(world, 'groundwater', 'wetland', 1, 'water_gate')

def logic_1135(world):
    # groundwater supports wetlands; stronger when vegetation is scarce.
    _feedback(world, 'groundwater', 'wetland', 1, 'scarcity_gate')

def logic_1136(world):
    # groundwater supports wetlands; stronger when biomass is high.
    _feedback(world, 'groundwater', 'wetland', 1, 'biomass_gate')

def logic_1137(world):
    # groundwater supports wetlands; stronger under habitat stress.
    _feedback(world, 'groundwater', 'wetland', 1, 'stress_gate')

def logic_1138(world):
    # groundwater supports wetlands; modulated by temperature.
    _feedback(world, 'groundwater', 'wetland', 1, 'seasonal_gate')

def logic_1139(world):
    # groundwater supports wetlands; saturates at high source levels.
    _feedback(world, 'groundwater', 'wetland', 1, 'saturation')

def logic_1140(world):
    # groundwater supports wetlands; activates above a food threshold.
    _feedback(world, 'groundwater', 'wetland', 1, 'threshold')

def logic_1141(world):
    # groundwater supports wetlands; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'groundwater', 'wetland', 1, 'recovery')

def logic_1142(world):
    # soil moisture supports vegetation; direct.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'baseline')

def logic_1143(world):
    # soil moisture supports vegetation; stronger when soil is dry.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'dry_gate')

def logic_1144(world):
    # soil moisture supports vegetation; stronger when soil is wet.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'wet_gate')

def logic_1145(world):
    # soil moisture supports vegetation; stronger when temperature is high.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'heat_gate')

def logic_1146(world):
    # soil moisture supports vegetation; stronger when temperature is low.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'cold_gate')

def logic_1147(world):
    # soil moisture supports vegetation; stronger under fire pressure.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'fire_gate')

def logic_1148(world):
    # soil moisture supports vegetation; stronger when surface water is high.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'water_gate')

def logic_1149(world):
    # soil moisture supports vegetation; stronger when vegetation is scarce.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'scarcity_gate')

def logic_1150(world):
    # soil moisture supports vegetation; stronger when biomass is high.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'biomass_gate')

def logic_1151(world):
    # soil moisture supports vegetation; stronger under habitat stress.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'stress_gate')

def logic_1152(world):
    # soil moisture supports vegetation; modulated by temperature.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'seasonal_gate')

def logic_1153(world):
    # soil moisture supports vegetation; saturates at high source levels.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'saturation')

def logic_1154(world):
    # soil moisture supports vegetation; activates above a food threshold.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'threshold')

def logic_1155(world):
    # soil moisture supports vegetation; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'soil_moisture', 'vegetation', 1, 'recovery')

def logic_1156(world):
    # soil moisture supports flowering; direct.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'baseline')

def logic_1157(world):
    # soil moisture supports flowering; stronger when soil is dry.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'dry_gate')

def logic_1158(world):
    # soil moisture supports flowering; stronger when soil is wet.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'wet_gate')

def logic_1159(world):
    # soil moisture supports flowering; stronger when temperature is high.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'heat_gate')

def logic_1160(world):
    # soil moisture supports flowering; stronger when temperature is low.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'cold_gate')

def logic_1161(world):
    # soil moisture supports flowering; stronger under fire pressure.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'fire_gate')

def logic_1162(world):
    # soil moisture supports flowering; stronger when surface water is high.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'water_gate')

def logic_1163(world):
    # soil moisture supports flowering; stronger when vegetation is scarce.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'scarcity_gate')

def logic_1164(world):
    # soil moisture supports flowering; stronger when biomass is high.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'biomass_gate')

def logic_1165(world):
    # soil moisture supports flowering; stronger under habitat stress.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'stress_gate')

def logic_1166(world):
    # soil moisture supports flowering; modulated by temperature.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'seasonal_gate')

def logic_1167(world):
    # soil moisture supports flowering; saturates at high source levels.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'saturation')

def logic_1168(world):
    # soil moisture supports flowering; activates above a food threshold.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'threshold')

def logic_1169(world):
    # soil moisture supports flowering; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'soil_moisture', 'flowers', 1, 'recovery')

def logic_1170(world):
    # soil moisture supports seed persistence; direct.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'baseline')

def logic_1171(world):
    # soil moisture supports seed persistence; stronger when soil is dry.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'dry_gate')

def logic_1172(world):
    # soil moisture supports seed persistence; stronger when soil is wet.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'wet_gate')

def logic_1173(world):
    # soil moisture supports seed persistence; stronger when temperature is high.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'heat_gate')

def logic_1174(world):
    # soil moisture supports seed persistence; stronger when temperature is low.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'cold_gate')

def logic_1175(world):
    # soil moisture supports seed persistence; stronger under fire pressure.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'fire_gate')

def logic_1176(world):
    # soil moisture supports seed persistence; stronger when surface water is high.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'water_gate')

def logic_1177(world):
    # soil moisture supports seed persistence; stronger when vegetation is scarce.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'scarcity_gate')

def logic_1178(world):
    # soil moisture supports seed persistence; stronger when biomass is high.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'biomass_gate')

def logic_1179(world):
    # soil moisture supports seed persistence; stronger under habitat stress.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'stress_gate')

def logic_1180(world):
    # soil moisture supports seed persistence; modulated by temperature.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'seasonal_gate')

def logic_1181(world):
    # soil moisture supports seed persistence; saturates at high source levels.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'saturation')

def logic_1182(world):
    # soil moisture supports seed persistence; activates above a food threshold.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'threshold')

def logic_1183(world):
    # soil moisture supports seed persistence; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'soil_moisture', 'seed_bank', 1, 'recovery')

def logic_1184(world):
    # humidity promotes cloud formation; direct.
    _feedback(world, 'humidity', 'cloud', 1, 'baseline')

def logic_1185(world):
    # humidity promotes cloud formation; stronger when soil is dry.
    _feedback(world, 'humidity', 'cloud', 1, 'dry_gate')

def logic_1186(world):
    # humidity promotes cloud formation; stronger when soil is wet.
    _feedback(world, 'humidity', 'cloud', 1, 'wet_gate')

def logic_1187(world):
    # humidity promotes cloud formation; stronger when temperature is high.
    _feedback(world, 'humidity', 'cloud', 1, 'heat_gate')

def logic_1188(world):
    # humidity promotes cloud formation; stronger when temperature is low.
    _feedback(world, 'humidity', 'cloud', 1, 'cold_gate')

def logic_1189(world):
    # humidity promotes cloud formation; stronger under fire pressure.
    _feedback(world, 'humidity', 'cloud', 1, 'fire_gate')

def logic_1190(world):
    # humidity promotes cloud formation; stronger when surface water is high.
    _feedback(world, 'humidity', 'cloud', 1, 'water_gate')

def logic_1191(world):
    # humidity promotes cloud formation; stronger when vegetation is scarce.
    _feedback(world, 'humidity', 'cloud', 1, 'scarcity_gate')

def logic_1192(world):
    # humidity promotes cloud formation; stronger when biomass is high.
    _feedback(world, 'humidity', 'cloud', 1, 'biomass_gate')

def logic_1193(world):
    # humidity promotes cloud formation; stronger under habitat stress.
    _feedback(world, 'humidity', 'cloud', 1, 'stress_gate')

def logic_1194(world):
    # humidity promotes cloud formation; modulated by temperature.
    _feedback(world, 'humidity', 'cloud', 1, 'seasonal_gate')

def logic_1195(world):
    # humidity promotes cloud formation; saturates at high source levels.
    _feedback(world, 'humidity', 'cloud', 1, 'saturation')

def logic_1196(world):
    # humidity promotes cloud formation; activates above a food threshold.
    _feedback(world, 'humidity', 'cloud', 1, 'threshold')

def logic_1197(world):
    # humidity promotes cloud formation; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'humidity', 'cloud', 1, 'recovery')

def logic_1198(world):
    # cloud water produces rain; direct.
    _feedback(world, 'cloud', 'rain', 1, 'baseline')

def logic_1199(world):
    # cloud water produces rain; stronger when soil is dry.
    _feedback(world, 'cloud', 'rain', 1, 'dry_gate')

def logic_1200(world):
    # cloud water produces rain; stronger when soil is wet.
    _feedback(world, 'cloud', 'rain', 1, 'wet_gate')

def logic_1201(world):
    # cloud water produces rain; stronger when temperature is high.
    _feedback(world, 'cloud', 'rain', 1, 'heat_gate')

def logic_1202(world):
    # cloud water produces rain; stronger when temperature is low.
    _feedback(world, 'cloud', 'rain', 1, 'cold_gate')

def logic_1203(world):
    # cloud water produces rain; stronger under fire pressure.
    _feedback(world, 'cloud', 'rain', 1, 'fire_gate')

def logic_1204(world):
    # cloud water produces rain; stronger when surface water is high.
    _feedback(world, 'cloud', 'rain', 1, 'water_gate')

def logic_1205(world):
    # cloud water produces rain; stronger when vegetation is scarce.
    _feedback(world, 'cloud', 'rain', 1, 'scarcity_gate')

def logic_1206(world):
    # cloud water produces rain; stronger when biomass is high.
    _feedback(world, 'cloud', 'rain', 1, 'biomass_gate')

def logic_1207(world):
    # cloud water produces rain; stronger under habitat stress.
    _feedback(world, 'cloud', 'rain', 1, 'stress_gate')

def logic_1208(world):
    # cloud water produces rain; modulated by temperature.
    _feedback(world, 'cloud', 'rain', 1, 'seasonal_gate')

def logic_1209(world):
    # cloud water produces rain; saturates at high source levels.
    _feedback(world, 'cloud', 'rain', 1, 'saturation')

def logic_1210(world):
    # cloud water produces rain; activates above a food threshold.
    _feedback(world, 'cloud', 'rain', 1, 'threshold')

def logic_1211(world):
    # cloud water produces rain; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'cloud', 'rain', 1, 'recovery')

def logic_1212(world):
    # cloud cover reduces heating; direct.
    _feedback(world, 'cloud', 'temperature', -1, 'baseline')

def logic_1213(world):
    # cloud cover reduces heating; stronger when soil is dry.
    _feedback(world, 'cloud', 'temperature', -1, 'dry_gate')

def logic_1214(world):
    # cloud cover reduces heating; stronger when soil is wet.
    _feedback(world, 'cloud', 'temperature', -1, 'wet_gate')

def logic_1215(world):
    # cloud cover reduces heating; stronger when temperature is high.
    _feedback(world, 'cloud', 'temperature', -1, 'heat_gate')

def logic_1216(world):
    # cloud cover reduces heating; stronger when temperature is low.
    _feedback(world, 'cloud', 'temperature', -1, 'cold_gate')

def logic_1217(world):
    # cloud cover reduces heating; stronger under fire pressure.
    _feedback(world, 'cloud', 'temperature', -1, 'fire_gate')

def logic_1218(world):
    # cloud cover reduces heating; stronger when surface water is high.
    _feedback(world, 'cloud', 'temperature', -1, 'water_gate')

def logic_1219(world):
    # cloud cover reduces heating; stronger when vegetation is scarce.
    _feedback(world, 'cloud', 'temperature', -1, 'scarcity_gate')

def logic_1220(world):
    # cloud cover reduces heating; stronger when biomass is high.
    _feedback(world, 'cloud', 'temperature', -1, 'biomass_gate')

def logic_1221(world):
    # cloud cover reduces heating; stronger under habitat stress.
    _feedback(world, 'cloud', 'temperature', -1, 'stress_gate')

def logic_1222(world):
    # cloud cover reduces heating; modulated by temperature.
    _feedback(world, 'cloud', 'temperature', -1, 'seasonal_gate')

def logic_1223(world):
    # cloud cover reduces heating; saturates at high source levels.
    _feedback(world, 'cloud', 'temperature', -1, 'saturation')

def logic_1224(world):
    # cloud cover reduces heating; activates above a food threshold.
    _feedback(world, 'cloud', 'temperature', -1, 'threshold')

def logic_1225(world):
    # cloud cover reduces heating; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'cloud', 'temperature', -1, 'recovery')

def logic_1226(world):
    # warmth increases evaporation; direct.
    _feedback(world, 'temperature', 'evaporation', 1, 'baseline')

def logic_1227(world):
    # warmth increases evaporation; stronger when soil is dry.
    _feedback(world, 'temperature', 'evaporation', 1, 'dry_gate')

def logic_1228(world):
    # warmth increases evaporation; stronger when soil is wet.
    _feedback(world, 'temperature', 'evaporation', 1, 'wet_gate')

def logic_1229(world):
    # warmth increases evaporation; stronger when temperature is high.
    _feedback(world, 'temperature', 'evaporation', 1, 'heat_gate')

def logic_1230(world):
    # warmth increases evaporation; stronger when temperature is low.
    _feedback(world, 'temperature', 'evaporation', 1, 'cold_gate')

def logic_1231(world):
    # warmth increases evaporation; stronger under fire pressure.
    _feedback(world, 'temperature', 'evaporation', 1, 'fire_gate')

def logic_1232(world):
    # warmth increases evaporation; stronger when surface water is high.
    _feedback(world, 'temperature', 'evaporation', 1, 'water_gate')

def logic_1233(world):
    # warmth increases evaporation; stronger when vegetation is scarce.
    _feedback(world, 'temperature', 'evaporation', 1, 'scarcity_gate')

def logic_1234(world):
    # warmth increases evaporation; stronger when biomass is high.
    _feedback(world, 'temperature', 'evaporation', 1, 'biomass_gate')

def logic_1235(world):
    # warmth increases evaporation; stronger under habitat stress.
    _feedback(world, 'temperature', 'evaporation', 1, 'stress_gate')

def logic_1236(world):
    # warmth increases evaporation; modulated by temperature.
    _feedback(world, 'temperature', 'evaporation', 1, 'seasonal_gate')

def logic_1237(world):
    # warmth increases evaporation; saturates at high source levels.
    _feedback(world, 'temperature', 'evaporation', 1, 'saturation')

def logic_1238(world):
    # warmth increases evaporation; activates above a food threshold.
    _feedback(world, 'temperature', 'evaporation', 1, 'threshold')

def logic_1239(world):
    # warmth increases evaporation; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'temperature', 'evaporation', 1, 'recovery')

def logic_1240(world):
    # warmth melts snowpack; direct.
    _feedback(world, 'temperature', 'snowpack', -1, 'baseline')

def logic_1241(world):
    # warmth melts snowpack; stronger when soil is dry.
    _feedback(world, 'temperature', 'snowpack', -1, 'dry_gate')

def logic_1242(world):
    # warmth melts snowpack; stronger when soil is wet.
    _feedback(world, 'temperature', 'snowpack', -1, 'wet_gate')

def logic_1243(world):
    # warmth melts snowpack; stronger when temperature is high.
    _feedback(world, 'temperature', 'snowpack', -1, 'heat_gate')

def logic_1244(world):
    # warmth melts snowpack; stronger when temperature is low.
    _feedback(world, 'temperature', 'snowpack', -1, 'cold_gate')

def logic_1245(world):
    # warmth melts snowpack; stronger under fire pressure.
    _feedback(world, 'temperature', 'snowpack', -1, 'fire_gate')

def logic_1246(world):
    # warmth melts snowpack; stronger when surface water is high.
    _feedback(world, 'temperature', 'snowpack', -1, 'water_gate')

def logic_1247(world):
    # warmth melts snowpack; stronger when vegetation is scarce.
    _feedback(world, 'temperature', 'snowpack', -1, 'scarcity_gate')

def logic_1248(world):
    # warmth melts snowpack; stronger when biomass is high.
    _feedback(world, 'temperature', 'snowpack', -1, 'biomass_gate')

def logic_1249(world):
    # warmth melts snowpack; stronger under habitat stress.
    _feedback(world, 'temperature', 'snowpack', -1, 'stress_gate')

def logic_1250(world):
    # warmth melts snowpack; modulated by temperature.
    _feedback(world, 'temperature', 'snowpack', -1, 'seasonal_gate')

def logic_1251(world):
    # warmth melts snowpack; saturates at high source levels.
    _feedback(world, 'temperature', 'snowpack', -1, 'saturation')

def logic_1252(world):
    # warmth melts snowpack; activates above a food threshold.
    _feedback(world, 'temperature', 'snowpack', -1, 'threshold')

def logic_1253(world):
    # warmth melts snowpack; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'temperature', 'snowpack', -1, 'recovery')

def logic_1254(world):
    # warmth melts ice; direct.
    _feedback(world, 'temperature', 'ice', -1, 'baseline')

def logic_1255(world):
    # warmth melts ice; stronger when soil is dry.
    _feedback(world, 'temperature', 'ice', -1, 'dry_gate')

def logic_1256(world):
    # warmth melts ice; stronger when soil is wet.
    _feedback(world, 'temperature', 'ice', -1, 'wet_gate')

def logic_1257(world):
    # warmth melts ice; stronger when temperature is high.
    _feedback(world, 'temperature', 'ice', -1, 'heat_gate')

def logic_1258(world):
    # warmth melts ice; stronger when temperature is low.
    _feedback(world, 'temperature', 'ice', -1, 'cold_gate')

def logic_1259(world):
    # warmth melts ice; stronger under fire pressure.
    _feedback(world, 'temperature', 'ice', -1, 'fire_gate')

def logic_1260(world):
    # warmth melts ice; stronger when surface water is high.
    _feedback(world, 'temperature', 'ice', -1, 'water_gate')

def logic_1261(world):
    # warmth melts ice; stronger when vegetation is scarce.
    _feedback(world, 'temperature', 'ice', -1, 'scarcity_gate')

def logic_1262(world):
    # warmth melts ice; stronger when biomass is high.
    _feedback(world, 'temperature', 'ice', -1, 'biomass_gate')

def logic_1263(world):
    # warmth melts ice; stronger under habitat stress.
    _feedback(world, 'temperature', 'ice', -1, 'stress_gate')

def logic_1264(world):
    # warmth melts ice; modulated by temperature.
    _feedback(world, 'temperature', 'ice', -1, 'seasonal_gate')

def logic_1265(world):
    # warmth melts ice; saturates at high source levels.
    _feedback(world, 'temperature', 'ice', -1, 'saturation')

def logic_1266(world):
    # warmth melts ice; activates above a food threshold.
    _feedback(world, 'temperature', 'ice', -1, 'threshold')
