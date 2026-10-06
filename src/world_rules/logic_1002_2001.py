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

def logic_1267(world):
    # warmth melts ice; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'temperature', 'ice', -1, 'recovery')

def logic_1268(world):
    # warmth melts surface ice; direct.
    _feedback(world, 'temperature', 'surface_ice', -1, 'baseline')

def logic_1269(world):
    # warmth melts surface ice; stronger when soil is dry.
    _feedback(world, 'temperature', 'surface_ice', -1, 'dry_gate')

def logic_1270(world):
    # warmth melts surface ice; stronger when soil is wet.
    _feedback(world, 'temperature', 'surface_ice', -1, 'wet_gate')

def logic_1271(world):
    # warmth melts surface ice; stronger when temperature is high.
    _feedback(world, 'temperature', 'surface_ice', -1, 'heat_gate')

def logic_1272(world):
    # warmth melts surface ice; stronger when temperature is low.
    _feedback(world, 'temperature', 'surface_ice', -1, 'cold_gate')

def logic_1273(world):
    # warmth melts surface ice; stronger under fire pressure.
    _feedback(world, 'temperature', 'surface_ice', -1, 'fire_gate')

def logic_1274(world):
    # warmth melts surface ice; stronger when surface water is high.
    _feedback(world, 'temperature', 'surface_ice', -1, 'water_gate')

def logic_1275(world):
    # warmth melts surface ice; stronger when vegetation is scarce.
    _feedback(world, 'temperature', 'surface_ice', -1, 'scarcity_gate')

def logic_1276(world):
    # warmth melts surface ice; stronger when biomass is high.
    _feedback(world, 'temperature', 'surface_ice', -1, 'biomass_gate')

def logic_1277(world):
    # warmth melts surface ice; stronger under habitat stress.
    _feedback(world, 'temperature', 'surface_ice', -1, 'stress_gate')

def logic_1278(world):
    # warmth melts surface ice; modulated by temperature.
    _feedback(world, 'temperature', 'surface_ice', -1, 'seasonal_gate')

def logic_1279(world):
    # warmth melts surface ice; saturates at high source levels.
    _feedback(world, 'temperature', 'surface_ice', -1, 'saturation')

def logic_1280(world):
    # warmth melts surface ice; activates above a food threshold.
    _feedback(world, 'temperature', 'surface_ice', -1, 'threshold')

def logic_1281(world):
    # warmth melts surface ice; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'temperature', 'surface_ice', -1, 'recovery')

def logic_1282(world):
    # wind enhances evaporation; direct.
    _feedback(world, 'wind_x', 'evaporation', 1, 'baseline')

def logic_1283(world):
    # wind enhances evaporation; stronger when soil is dry.
    _feedback(world, 'wind_x', 'evaporation', 1, 'dry_gate')

def logic_1284(world):
    # wind enhances evaporation; stronger when soil is wet.
    _feedback(world, 'wind_x', 'evaporation', 1, 'wet_gate')

def logic_1285(world):
    # wind enhances evaporation; stronger when temperature is high.
    _feedback(world, 'wind_x', 'evaporation', 1, 'heat_gate')

def logic_1286(world):
    # wind enhances evaporation; stronger when temperature is low.
    _feedback(world, 'wind_x', 'evaporation', 1, 'cold_gate')

def logic_1287(world):
    # wind enhances evaporation; stronger under fire pressure.
    _feedback(world, 'wind_x', 'evaporation', 1, 'fire_gate')

def logic_1288(world):
    # wind enhances evaporation; stronger when surface water is high.
    _feedback(world, 'wind_x', 'evaporation', 1, 'water_gate')

def logic_1289(world):
    # wind enhances evaporation; stronger when vegetation is scarce.
    _feedback(world, 'wind_x', 'evaporation', 1, 'scarcity_gate')

def logic_1290(world):
    # wind enhances evaporation; stronger when biomass is high.
    _feedback(world, 'wind_x', 'evaporation', 1, 'biomass_gate')

def logic_1291(world):
    # wind enhances evaporation; stronger under habitat stress.
    _feedback(world, 'wind_x', 'evaporation', 1, 'stress_gate')

def logic_1292(world):
    # wind enhances evaporation; modulated by temperature.
    _feedback(world, 'wind_x', 'evaporation', 1, 'seasonal_gate')

def logic_1293(world):
    # wind enhances evaporation; saturates at high source levels.
    _feedback(world, 'wind_x', 'evaporation', 1, 'saturation')

def logic_1294(world):
    # wind enhances evaporation; activates above a food threshold.
    _feedback(world, 'wind_x', 'evaporation', 1, 'threshold')

def logic_1295(world):
    # wind enhances evaporation; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'wind_x', 'evaporation', 1, 'recovery')

def logic_1296(world):
    # wind enhances evaporation; direct.
    _feedback(world, 'wind_y', 'evaporation', 1, 'baseline')

def logic_1297(world):
    # wind enhances evaporation; stronger when soil is dry.
    _feedback(world, 'wind_y', 'evaporation', 1, 'dry_gate')

def logic_1298(world):
    # wind enhances evaporation; stronger when soil is wet.
    _feedback(world, 'wind_y', 'evaporation', 1, 'wet_gate')

def logic_1299(world):
    # wind enhances evaporation; stronger when temperature is high.
    _feedback(world, 'wind_y', 'evaporation', 1, 'heat_gate')

def logic_1300(world):
    # wind enhances evaporation; stronger when temperature is low.
    _feedback(world, 'wind_y', 'evaporation', 1, 'cold_gate')

def logic_1301(world):
    # wind enhances evaporation; stronger under fire pressure.
    _feedback(world, 'wind_y', 'evaporation', 1, 'fire_gate')

def logic_1302(world):
    # wind enhances evaporation; stronger when surface water is high.
    _feedback(world, 'wind_y', 'evaporation', 1, 'water_gate')

def logic_1303(world):
    # wind enhances evaporation; stronger when vegetation is scarce.
    _feedback(world, 'wind_y', 'evaporation', 1, 'scarcity_gate')

def logic_1304(world):
    # wind enhances evaporation; stronger when biomass is high.
    _feedback(world, 'wind_y', 'evaporation', 1, 'biomass_gate')

def logic_1305(world):
    # wind enhances evaporation; stronger under habitat stress.
    _feedback(world, 'wind_y', 'evaporation', 1, 'stress_gate')

def logic_1306(world):
    # wind enhances evaporation; modulated by temperature.
    _feedback(world, 'wind_y', 'evaporation', 1, 'seasonal_gate')

def logic_1307(world):
    # wind enhances evaporation; saturates at high source levels.
    _feedback(world, 'wind_y', 'evaporation', 1, 'saturation')

def logic_1308(world):
    # wind enhances evaporation; activates above a food threshold.
    _feedback(world, 'wind_y', 'evaporation', 1, 'threshold')

def logic_1309(world):
    # wind enhances evaporation; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'wind_y', 'evaporation', 1, 'recovery')

def logic_1310(world):
    # evaporation replenishes humidity; direct.
    _feedback(world, 'evaporation', 'humidity', 1, 'baseline')

def logic_1311(world):
    # evaporation replenishes humidity; stronger when soil is dry.
    _feedback(world, 'evaporation', 'humidity', 1, 'dry_gate')

def logic_1312(world):
    # evaporation replenishes humidity; stronger when soil is wet.
    _feedback(world, 'evaporation', 'humidity', 1, 'wet_gate')

def logic_1313(world):
    # evaporation replenishes humidity; stronger when temperature is high.
    _feedback(world, 'evaporation', 'humidity', 1, 'heat_gate')

def logic_1314(world):
    # evaporation replenishes humidity; stronger when temperature is low.
    _feedback(world, 'evaporation', 'humidity', 1, 'cold_gate')

def logic_1315(world):
    # evaporation replenishes humidity; stronger under fire pressure.
    _feedback(world, 'evaporation', 'humidity', 1, 'fire_gate')

def logic_1316(world):
    # evaporation replenishes humidity; stronger when surface water is high.
    _feedback(world, 'evaporation', 'humidity', 1, 'water_gate')

def logic_1317(world):
    # evaporation replenishes humidity; stronger when vegetation is scarce.
    _feedback(world, 'evaporation', 'humidity', 1, 'scarcity_gate')

def logic_1318(world):
    # evaporation replenishes humidity; stronger when biomass is high.
    _feedback(world, 'evaporation', 'humidity', 1, 'biomass_gate')

def logic_1319(world):
    # evaporation replenishes humidity; stronger under habitat stress.
    _feedback(world, 'evaporation', 'humidity', 1, 'stress_gate')

def logic_1320(world):
    # evaporation replenishes humidity; modulated by temperature.
    _feedback(world, 'evaporation', 'humidity', 1, 'seasonal_gate')

def logic_1321(world):
    # evaporation replenishes humidity; saturates at high source levels.
    _feedback(world, 'evaporation', 'humidity', 1, 'saturation')

def logic_1322(world):
    # evaporation replenishes humidity; activates above a food threshold.
    _feedback(world, 'evaporation', 'humidity', 1, 'threshold')

def logic_1323(world):
    # evaporation replenishes humidity; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'evaporation', 'humidity', 1, 'recovery')

def logic_1324(world):
    # evaporation removes surface water; direct.
    _feedback(world, 'evaporation', 'surface_water', -1, 'baseline')

def logic_1325(world):
    # evaporation removes surface water; stronger when soil is dry.
    _feedback(world, 'evaporation', 'surface_water', -1, 'dry_gate')

def logic_1326(world):
    # evaporation removes surface water; stronger when soil is wet.
    _feedback(world, 'evaporation', 'surface_water', -1, 'wet_gate')

def logic_1327(world):
    # evaporation removes surface water; stronger when temperature is high.
    _feedback(world, 'evaporation', 'surface_water', -1, 'heat_gate')

def logic_1328(world):
    # evaporation removes surface water; stronger when temperature is low.
    _feedback(world, 'evaporation', 'surface_water', -1, 'cold_gate')

def logic_1329(world):
    # evaporation removes surface water; stronger under fire pressure.
    _feedback(world, 'evaporation', 'surface_water', -1, 'fire_gate')

def logic_1330(world):
    # evaporation removes surface water; stronger when surface water is high.
    _feedback(world, 'evaporation', 'surface_water', -1, 'water_gate')

def logic_1331(world):
    # evaporation removes surface water; stronger when vegetation is scarce.
    _feedback(world, 'evaporation', 'surface_water', -1, 'scarcity_gate')

def logic_1332(world):
    # evaporation removes surface water; stronger when biomass is high.
    _feedback(world, 'evaporation', 'surface_water', -1, 'biomass_gate')

def logic_1333(world):
    # evaporation removes surface water; stronger under habitat stress.
    _feedback(world, 'evaporation', 'surface_water', -1, 'stress_gate')

def logic_1334(world):
    # evaporation removes surface water; modulated by temperature.
    _feedback(world, 'evaporation', 'surface_water', -1, 'seasonal_gate')

def logic_1335(world):
    # evaporation removes surface water; saturates at high source levels.
    _feedback(world, 'evaporation', 'surface_water', -1, 'saturation')

def logic_1336(world):
    # evaporation removes surface water; activates above a food threshold.
    _feedback(world, 'evaporation', 'surface_water', -1, 'threshold')

def logic_1337(world):
    # evaporation removes surface water; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'evaporation', 'surface_water', -1, 'recovery')

def logic_1338(world):
    # runoff mobilizes sediment; direct.
    _feedback(world, 'runoff', 'sediment', 1, 'baseline')

def logic_1339(world):
    # runoff mobilizes sediment; stronger when soil is dry.
    _feedback(world, 'runoff', 'sediment', 1, 'dry_gate')

def logic_1340(world):
    # runoff mobilizes sediment; stronger when soil is wet.
    _feedback(world, 'runoff', 'sediment', 1, 'wet_gate')

def logic_1341(world):
    # runoff mobilizes sediment; stronger when temperature is high.
    _feedback(world, 'runoff', 'sediment', 1, 'heat_gate')

def logic_1342(world):
    # runoff mobilizes sediment; stronger when temperature is low.
    _feedback(world, 'runoff', 'sediment', 1, 'cold_gate')

def logic_1343(world):
    # runoff mobilizes sediment; stronger under fire pressure.
    _feedback(world, 'runoff', 'sediment', 1, 'fire_gate')

def logic_1344(world):
    # runoff mobilizes sediment; stronger when surface water is high.
    _feedback(world, 'runoff', 'sediment', 1, 'water_gate')

def logic_1345(world):
    # runoff mobilizes sediment; stronger when vegetation is scarce.
    _feedback(world, 'runoff', 'sediment', 1, 'scarcity_gate')

def logic_1346(world):
    # runoff mobilizes sediment; stronger when biomass is high.
    _feedback(world, 'runoff', 'sediment', 1, 'biomass_gate')

def logic_1347(world):
    # runoff mobilizes sediment; stronger under habitat stress.
    _feedback(world, 'runoff', 'sediment', 1, 'stress_gate')

def logic_1348(world):
    # runoff mobilizes sediment; modulated by temperature.
    _feedback(world, 'runoff', 'sediment', 1, 'seasonal_gate')

def logic_1349(world):
    # runoff mobilizes sediment; saturates at high source levels.
    _feedback(world, 'runoff', 'sediment', 1, 'saturation')

def logic_1350(world):
    # runoff mobilizes sediment; activates above a food threshold.
    _feedback(world, 'runoff', 'sediment', 1, 'threshold')

def logic_1351(world):
    # runoff mobilizes sediment; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'runoff', 'sediment', 1, 'recovery')

def logic_1352(world):
    # sediment export reduces soil depth; direct.
    _feedback(world, 'sediment', 'soil_depth', -1, 'baseline')

def logic_1353(world):
    # sediment export reduces soil depth; stronger when soil is dry.
    _feedback(world, 'sediment', 'soil_depth', -1, 'dry_gate')

def logic_1354(world):
    # sediment export reduces soil depth; stronger when soil is wet.
    _feedback(world, 'sediment', 'soil_depth', -1, 'wet_gate')

def logic_1355(world):
    # sediment export reduces soil depth; stronger when temperature is high.
    _feedback(world, 'sediment', 'soil_depth', -1, 'heat_gate')

def logic_1356(world):
    # sediment export reduces soil depth; stronger when temperature is low.
    _feedback(world, 'sediment', 'soil_depth', -1, 'cold_gate')

def logic_1357(world):
    # sediment export reduces soil depth; stronger under fire pressure.
    _feedback(world, 'sediment', 'soil_depth', -1, 'fire_gate')

def logic_1358(world):
    # sediment export reduces soil depth; stronger when surface water is high.
    _feedback(world, 'sediment', 'soil_depth', -1, 'water_gate')

def logic_1359(world):
    # sediment export reduces soil depth; stronger when vegetation is scarce.
    _feedback(world, 'sediment', 'soil_depth', -1, 'scarcity_gate')

def logic_1360(world):
    # sediment export reduces soil depth; stronger when biomass is high.
    _feedback(world, 'sediment', 'soil_depth', -1, 'biomass_gate')

def logic_1361(world):
    # sediment export reduces soil depth; stronger under habitat stress.
    _feedback(world, 'sediment', 'soil_depth', -1, 'stress_gate')

def logic_1362(world):
    # sediment export reduces soil depth; modulated by temperature.
    _feedback(world, 'sediment', 'soil_depth', -1, 'seasonal_gate')

def logic_1363(world):
    # sediment export reduces soil depth; saturates at high source levels.
    _feedback(world, 'sediment', 'soil_depth', -1, 'saturation')

def logic_1364(world):
    # sediment export reduces soil depth; activates above a food threshold.
    _feedback(world, 'sediment', 'soil_depth', -1, 'threshold')

def logic_1365(world):
    # sediment export reduces soil depth; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'sediment', 'soil_depth', -1, 'recovery')

def logic_1366(world):
    # erosion removes soil depth; direct.
    _feedback(world, 'erosion', 'soil_depth', -1, 'baseline')

def logic_1367(world):
    # erosion removes soil depth; stronger when soil is dry.
    _feedback(world, 'erosion', 'soil_depth', -1, 'dry_gate')

def logic_1368(world):
    # erosion removes soil depth; stronger when soil is wet.
    _feedback(world, 'erosion', 'soil_depth', -1, 'wet_gate')

def logic_1369(world):
    # erosion removes soil depth; stronger when temperature is high.
    _feedback(world, 'erosion', 'soil_depth', -1, 'heat_gate')

def logic_1370(world):
    # erosion removes soil depth; stronger when temperature is low.
    _feedback(world, 'erosion', 'soil_depth', -1, 'cold_gate')

def logic_1371(world):
    # erosion removes soil depth; stronger under fire pressure.
    _feedback(world, 'erosion', 'soil_depth', -1, 'fire_gate')

def logic_1372(world):
    # erosion removes soil depth; stronger when surface water is high.
    _feedback(world, 'erosion', 'soil_depth', -1, 'water_gate')

def logic_1373(world):
    # erosion removes soil depth; stronger when vegetation is scarce.
    _feedback(world, 'erosion', 'soil_depth', -1, 'scarcity_gate')

def logic_1374(world):
    # erosion removes soil depth; stronger when biomass is high.
    _feedback(world, 'erosion', 'soil_depth', -1, 'biomass_gate')

def logic_1375(world):
    # erosion removes soil depth; stronger under habitat stress.
    _feedback(world, 'erosion', 'soil_depth', -1, 'stress_gate')

def logic_1376(world):
    # erosion removes soil depth; modulated by temperature.
    _feedback(world, 'erosion', 'soil_depth', -1, 'seasonal_gate')

def logic_1377(world):
    # erosion removes soil depth; saturates at high source levels.
    _feedback(world, 'erosion', 'soil_depth', -1, 'saturation')

def logic_1378(world):
    # erosion removes soil depth; activates above a food threshold.
    _feedback(world, 'erosion', 'soil_depth', -1, 'threshold')

def logic_1379(world):
    # erosion removes soil depth; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'erosion', 'soil_depth', -1, 'recovery')

def logic_1380(world):
    # vegetation roots suppress erosion; direct.
    _feedback(world, 'vegetation', 'erosion', -1, 'baseline')

def logic_1381(world):
    # vegetation roots suppress erosion; stronger when soil is dry.
    _feedback(world, 'vegetation', 'erosion', -1, 'dry_gate')

def logic_1382(world):
    # vegetation roots suppress erosion; stronger when soil is wet.
    _feedback(world, 'vegetation', 'erosion', -1, 'wet_gate')

def logic_1383(world):
    # vegetation roots suppress erosion; stronger when temperature is high.
    _feedback(world, 'vegetation', 'erosion', -1, 'heat_gate')

def logic_1384(world):
    # vegetation roots suppress erosion; stronger when temperature is low.
    _feedback(world, 'vegetation', 'erosion', -1, 'cold_gate')

def logic_1385(world):
    # vegetation roots suppress erosion; stronger under fire pressure.
    _feedback(world, 'vegetation', 'erosion', -1, 'fire_gate')

def logic_1386(world):
    # vegetation roots suppress erosion; stronger when surface water is high.
    _feedback(world, 'vegetation', 'erosion', -1, 'water_gate')

def logic_1387(world):
    # vegetation roots suppress erosion; stronger when vegetation is scarce.
    _feedback(world, 'vegetation', 'erosion', -1, 'scarcity_gate')

def logic_1388(world):
    # vegetation roots suppress erosion; stronger when biomass is high.
    _feedback(world, 'vegetation', 'erosion', -1, 'biomass_gate')

def logic_1389(world):
    # vegetation roots suppress erosion; stronger under habitat stress.
    _feedback(world, 'vegetation', 'erosion', -1, 'stress_gate')

def logic_1390(world):
    # vegetation roots suppress erosion; modulated by temperature.
    _feedback(world, 'vegetation', 'erosion', -1, 'seasonal_gate')

def logic_1391(world):
    # vegetation roots suppress erosion; saturates at high source levels.
    _feedback(world, 'vegetation', 'erosion', -1, 'saturation')

def logic_1392(world):
    # vegetation roots suppress erosion; activates above a food threshold.
    _feedback(world, 'vegetation', 'erosion', -1, 'threshold')

def logic_1393(world):
    # vegetation roots suppress erosion; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'vegetation', 'erosion', -1, 'recovery')

def logic_1394(world):
    # roots stabilize soil; direct.
    _feedback(world, 'root_density', 'erosion', -1, 'baseline')

def logic_1395(world):
    # roots stabilize soil; stronger when soil is dry.
    _feedback(world, 'root_density', 'erosion', -1, 'dry_gate')

def logic_1396(world):
    # roots stabilize soil; stronger when soil is wet.
    _feedback(world, 'root_density', 'erosion', -1, 'wet_gate')

def logic_1397(world):
    # roots stabilize soil; stronger when temperature is high.
    _feedback(world, 'root_density', 'erosion', -1, 'heat_gate')

def logic_1398(world):
    # roots stabilize soil; stronger when temperature is low.
    _feedback(world, 'root_density', 'erosion', -1, 'cold_gate')

def logic_1399(world):
    # roots stabilize soil; stronger under fire pressure.
    _feedback(world, 'root_density', 'erosion', -1, 'fire_gate')

def logic_1400(world):
    # roots stabilize soil; stronger when surface water is high.
    _feedback(world, 'root_density', 'erosion', -1, 'water_gate')

def logic_1401(world):
    # roots stabilize soil; stronger when vegetation is scarce.
    _feedback(world, 'root_density', 'erosion', -1, 'scarcity_gate')

def logic_1402(world):
    # roots stabilize soil; stronger when biomass is high.
    _feedback(world, 'root_density', 'erosion', -1, 'biomass_gate')

def logic_1403(world):
    # roots stabilize soil; stronger under habitat stress.
    _feedback(world, 'root_density', 'erosion', -1, 'stress_gate')

def logic_1404(world):
    # roots stabilize soil; modulated by temperature.
    _feedback(world, 'root_density', 'erosion', -1, 'seasonal_gate')

def logic_1405(world):
    # roots stabilize soil; saturates at high source levels.
    _feedback(world, 'root_density', 'erosion', -1, 'saturation')

def logic_1406(world):
    # roots stabilize soil; activates above a food threshold.
    _feedback(world, 'root_density', 'erosion', -1, 'threshold')

def logic_1407(world):
    # roots stabilize soil; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'root_density', 'erosion', -1, 'recovery')

def logic_1408(world):
    # roots retain soil; direct.
    _feedback(world, 'root_density', 'soil_depth', 1, 'baseline')

def logic_1409(world):
    # roots retain soil; stronger when soil is dry.
    _feedback(world, 'root_density', 'soil_depth', 1, 'dry_gate')

def logic_1410(world):
    # roots retain soil; stronger when soil is wet.
    _feedback(world, 'root_density', 'soil_depth', 1, 'wet_gate')

def logic_1411(world):
    # roots retain soil; stronger when temperature is high.
    _feedback(world, 'root_density', 'soil_depth', 1, 'heat_gate')

def logic_1412(world):
    # roots retain soil; stronger when temperature is low.
    _feedback(world, 'root_density', 'soil_depth', 1, 'cold_gate')

def logic_1413(world):
    # roots retain soil; stronger under fire pressure.
    _feedback(world, 'root_density', 'soil_depth', 1, 'fire_gate')

def logic_1414(world):
    # roots retain soil; stronger when surface water is high.
    _feedback(world, 'root_density', 'soil_depth', 1, 'water_gate')

def logic_1415(world):
    # roots retain soil; stronger when vegetation is scarce.
    _feedback(world, 'root_density', 'soil_depth', 1, 'scarcity_gate')

def logic_1416(world):
    # roots retain soil; stronger when biomass is high.
    _feedback(world, 'root_density', 'soil_depth', 1, 'biomass_gate')

def logic_1417(world):
    # roots retain soil; stronger under habitat stress.
    _feedback(world, 'root_density', 'soil_depth', 1, 'stress_gate')

def logic_1418(world):
    # roots retain soil; modulated by temperature.
    _feedback(world, 'root_density', 'soil_depth', 1, 'seasonal_gate')

def logic_1419(world):
    # roots retain soil; saturates at high source levels.
    _feedback(world, 'root_density', 'soil_depth', 1, 'saturation')

def logic_1420(world):
    # roots retain soil; activates above a food threshold.
    _feedback(world, 'root_density', 'soil_depth', 1, 'threshold')

def logic_1421(world):
    # roots retain soil; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'root_density', 'soil_depth', 1, 'recovery')

def logic_1422(world):
    # vegetation stores carbon; direct.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'baseline')

def logic_1423(world):
    # vegetation stores carbon; stronger when soil is dry.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'dry_gate')

def logic_1424(world):
    # vegetation stores carbon; stronger when soil is wet.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'wet_gate')

def logic_1425(world):
    # vegetation stores carbon; stronger when temperature is high.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'heat_gate')

def logic_1426(world):
    # vegetation stores carbon; stronger when temperature is low.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'cold_gate')

def logic_1427(world):
    # vegetation stores carbon; stronger under fire pressure.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'fire_gate')

def logic_1428(world):
    # vegetation stores carbon; stronger when surface water is high.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'water_gate')

def logic_1429(world):
    # vegetation stores carbon; stronger when vegetation is scarce.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'scarcity_gate')

def logic_1430(world):
    # vegetation stores carbon; stronger when biomass is high.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'biomass_gate')

def logic_1431(world):
    # vegetation stores carbon; stronger under habitat stress.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'stress_gate')

def logic_1432(world):
    # vegetation stores carbon; modulated by temperature.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'seasonal_gate')

def logic_1433(world):
    # vegetation stores carbon; saturates at high source levels.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'saturation')

def logic_1434(world):
    # vegetation stores carbon; activates above a food threshold.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'threshold')

def logic_1435(world):
    # vegetation stores carbon; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'vegetation', 'carbon_storage', 1, 'recovery')

def logic_1436(world):
    # biomass stores carbon; direct.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'baseline')

def logic_1437(world):
    # biomass stores carbon; stronger when soil is dry.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'dry_gate')

def logic_1438(world):
    # biomass stores carbon; stronger when soil is wet.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'wet_gate')

def logic_1439(world):
    # biomass stores carbon; stronger when temperature is high.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'heat_gate')

def logic_1440(world):
    # biomass stores carbon; stronger when temperature is low.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'cold_gate')

def logic_1441(world):
    # biomass stores carbon; stronger under fire pressure.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'fire_gate')

def logic_1442(world):
    # biomass stores carbon; stronger when surface water is high.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'water_gate')

def logic_1443(world):
    # biomass stores carbon; stronger when vegetation is scarce.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'scarcity_gate')

def logic_1444(world):
    # biomass stores carbon; stronger when biomass is high.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'biomass_gate')

def logic_1445(world):
    # biomass stores carbon; stronger under habitat stress.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'stress_gate')

def logic_1446(world):
    # biomass stores carbon; modulated by temperature.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'seasonal_gate')

def logic_1447(world):
    # biomass stores carbon; saturates at high source levels.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'saturation')

def logic_1448(world):
    # biomass stores carbon; activates above a food threshold.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'threshold')

def logic_1449(world):
    # biomass stores carbon; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'biomass', 'carbon_storage', 1, 'recovery')

def logic_1450(world):
    # biomass contributes oxygen; direct.
    _feedback(world, 'biomass', 'oxygen', 1, 'baseline')

def logic_1451(world):
    # biomass contributes oxygen; stronger when soil is dry.
    _feedback(world, 'biomass', 'oxygen', 1, 'dry_gate')

def logic_1452(world):
    # biomass contributes oxygen; stronger when soil is wet.
    _feedback(world, 'biomass', 'oxygen', 1, 'wet_gate')

def logic_1453(world):
    # biomass contributes oxygen; stronger when temperature is high.
    _feedback(world, 'biomass', 'oxygen', 1, 'heat_gate')

def logic_1454(world):
    # biomass contributes oxygen; stronger when temperature is low.
    _feedback(world, 'biomass', 'oxygen', 1, 'cold_gate')

def logic_1455(world):
    # biomass contributes oxygen; stronger under fire pressure.
    _feedback(world, 'biomass', 'oxygen', 1, 'fire_gate')

def logic_1456(world):
    # biomass contributes oxygen; stronger when surface water is high.
    _feedback(world, 'biomass', 'oxygen', 1, 'water_gate')

def logic_1457(world):
    # biomass contributes oxygen; stronger when vegetation is scarce.
    _feedback(world, 'biomass', 'oxygen', 1, 'scarcity_gate')

def logic_1458(world):
    # biomass contributes oxygen; stronger when biomass is high.
    _feedback(world, 'biomass', 'oxygen', 1, 'biomass_gate')

def logic_1459(world):
    # biomass contributes oxygen; stronger under habitat stress.
    _feedback(world, 'biomass', 'oxygen', 1, 'stress_gate')

def logic_1460(world):
    # biomass contributes oxygen; modulated by temperature.
    _feedback(world, 'biomass', 'oxygen', 1, 'seasonal_gate')

def logic_1461(world):
    # biomass contributes oxygen; saturates at high source levels.
    _feedback(world, 'biomass', 'oxygen', 1, 'saturation')

def logic_1462(world):
    # biomass contributes oxygen; activates above a food threshold.
    _feedback(world, 'biomass', 'oxygen', 1, 'threshold')

def logic_1463(world):
    # biomass contributes oxygen; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'biomass', 'oxygen', 1, 'recovery')

def logic_1464(world):
    # high CO2 stress reduces photosynthetic efficiency; direct.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'baseline')

def logic_1465(world):
    # high CO2 stress reduces photosynthetic efficiency; stronger when soil is dry.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'dry_gate')

def logic_1466(world):
    # high CO2 stress reduces photosynthetic efficiency; stronger when soil is wet.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'wet_gate')

def logic_1467(world):
    # high CO2 stress reduces photosynthetic efficiency; stronger when temperature is high.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'heat_gate')

def logic_1468(world):
    # high CO2 stress reduces photosynthetic efficiency; stronger when temperature is low.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'cold_gate')

def logic_1469(world):
    # high CO2 stress reduces photosynthetic efficiency; stronger under fire pressure.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'fire_gate')

def logic_1470(world):
    # high CO2 stress reduces photosynthetic efficiency; stronger when surface water is high.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'water_gate')

def logic_1471(world):
    # high CO2 stress reduces photosynthetic efficiency; stronger when vegetation is scarce.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'scarcity_gate')

def logic_1472(world):
    # high CO2 stress reduces photosynthetic efficiency; stronger when biomass is high.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'biomass_gate')

def logic_1473(world):
    # high CO2 stress reduces photosynthetic efficiency; stronger under habitat stress.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'stress_gate')

def logic_1474(world):
    # high CO2 stress reduces photosynthetic efficiency; modulated by temperature.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'seasonal_gate')

def logic_1475(world):
    # high CO2 stress reduces photosynthetic efficiency; saturates at high source levels.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'saturation')

def logic_1476(world):
    # high CO2 stress reduces photosynthetic efficiency; activates above a food threshold.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'threshold')

def logic_1477(world):
    # high CO2 stress reduces photosynthetic efficiency; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'co2', 'photosynthesis_factor', -1, 'recovery')

def logic_1478(world):
    # photosynthesis builds biomass; direct.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'baseline')

def logic_1479(world):
    # photosynthesis builds biomass; stronger when soil is dry.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'dry_gate')

def logic_1480(world):
    # photosynthesis builds biomass; stronger when soil is wet.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'wet_gate')

def logic_1481(world):
    # photosynthesis builds biomass; stronger when temperature is high.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'heat_gate')

def logic_1482(world):
    # photosynthesis builds biomass; stronger when temperature is low.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'cold_gate')

def logic_1483(world):
    # photosynthesis builds biomass; stronger under fire pressure.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'fire_gate')

def logic_1484(world):
    # photosynthesis builds biomass; stronger when surface water is high.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'water_gate')

def logic_1485(world):
    # photosynthesis builds biomass; stronger when vegetation is scarce.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'scarcity_gate')

def logic_1486(world):
    # photosynthesis builds biomass; stronger when biomass is high.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'biomass_gate')

def logic_1487(world):
    # photosynthesis builds biomass; stronger under habitat stress.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'stress_gate')

def logic_1488(world):
    # photosynthesis builds biomass; modulated by temperature.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'seasonal_gate')

def logic_1489(world):
    # photosynthesis builds biomass; saturates at high source levels.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'saturation')

def logic_1490(world):
    # photosynthesis builds biomass; activates above a food threshold.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'threshold')

def logic_1491(world):
    # photosynthesis builds biomass; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'photosynthesis_factor', 'biomass', 1, 'recovery')

def logic_1492(world):
    # nutrients support vegetation; direct.
    _feedback(world, 'nutrients', 'vegetation', 1, 'baseline')

def logic_1493(world):
    # nutrients support vegetation; stronger when soil is dry.
    _feedback(world, 'nutrients', 'vegetation', 1, 'dry_gate')

def logic_1494(world):
    # nutrients support vegetation; stronger when soil is wet.
    _feedback(world, 'nutrients', 'vegetation', 1, 'wet_gate')

def logic_1495(world):
    # nutrients support vegetation; stronger when temperature is high.
    _feedback(world, 'nutrients', 'vegetation', 1, 'heat_gate')

def logic_1496(world):
    # nutrients support vegetation; stronger when temperature is low.
    _feedback(world, 'nutrients', 'vegetation', 1, 'cold_gate')

def logic_1497(world):
    # nutrients support vegetation; stronger under fire pressure.
    _feedback(world, 'nutrients', 'vegetation', 1, 'fire_gate')

def logic_1498(world):
    # nutrients support vegetation; stronger when surface water is high.
    _feedback(world, 'nutrients', 'vegetation', 1, 'water_gate')

def logic_1499(world):
    # nutrients support vegetation; stronger when vegetation is scarce.
    _feedback(world, 'nutrients', 'vegetation', 1, 'scarcity_gate')

def logic_1500(world):
    # nutrients support vegetation; stronger when biomass is high.
    _feedback(world, 'nutrients', 'vegetation', 1, 'biomass_gate')

def logic_1501(world):
    # nutrients support vegetation; stronger under habitat stress.
    _feedback(world, 'nutrients', 'vegetation', 1, 'stress_gate')

def logic_1502(world):
    # nutrients support vegetation; modulated by temperature.
    _feedback(world, 'nutrients', 'vegetation', 1, 'seasonal_gate')

def logic_1503(world):
    # nutrients support vegetation; saturates at high source levels.
    _feedback(world, 'nutrients', 'vegetation', 1, 'saturation')

def logic_1504(world):
    # nutrients support vegetation; activates above a food threshold.
    _feedback(world, 'nutrients', 'vegetation', 1, 'threshold')

def logic_1505(world):
    # nutrients support vegetation; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'nutrients', 'vegetation', 1, 'recovery')

def logic_1506(world):
    # organic matter mineralizes nutrients; direct.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'baseline')

def logic_1507(world):
    # organic matter mineralizes nutrients; stronger when soil is dry.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'dry_gate')

def logic_1508(world):
    # organic matter mineralizes nutrients; stronger when soil is wet.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'wet_gate')

def logic_1509(world):
    # organic matter mineralizes nutrients; stronger when temperature is high.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'heat_gate')

def logic_1510(world):
    # organic matter mineralizes nutrients; stronger when temperature is low.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'cold_gate')

def logic_1511(world):
    # organic matter mineralizes nutrients; stronger under fire pressure.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'fire_gate')

def logic_1512(world):
    # organic matter mineralizes nutrients; stronger when surface water is high.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'water_gate')

def logic_1513(world):
    # organic matter mineralizes nutrients; stronger when vegetation is scarce.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'scarcity_gate')

def logic_1514(world):
    # organic matter mineralizes nutrients; stronger when biomass is high.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'biomass_gate')

def logic_1515(world):
    # organic matter mineralizes nutrients; stronger under habitat stress.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'stress_gate')

def logic_1516(world):
    # organic matter mineralizes nutrients; modulated by temperature.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'seasonal_gate')

def logic_1517(world):
    # organic matter mineralizes nutrients; saturates at high source levels.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'saturation')

def logic_1518(world):
    # organic matter mineralizes nutrients; activates above a food threshold.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'threshold')

def logic_1519(world):
    # organic matter mineralizes nutrients; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'organic_matter', 'nutrients', 1, 'recovery')

def logic_1520(world):
    # decomposition releases nutrients; direct.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'baseline')

def logic_1521(world):
    # decomposition releases nutrients; stronger when soil is dry.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'dry_gate')

def logic_1522(world):
    # decomposition releases nutrients; stronger when soil is wet.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'wet_gate')

def logic_1523(world):
    # decomposition releases nutrients; stronger when temperature is high.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'heat_gate')

def logic_1524(world):
    # decomposition releases nutrients; stronger when temperature is low.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'cold_gate')

def logic_1525(world):
    # decomposition releases nutrients; stronger under fire pressure.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'fire_gate')

def logic_1526(world):
    # decomposition releases nutrients; stronger when surface water is high.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'water_gate')

def logic_1527(world):
    # decomposition releases nutrients; stronger when vegetation is scarce.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'scarcity_gate')

def logic_1528(world):
    # decomposition releases nutrients; stronger when biomass is high.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'biomass_gate')

def logic_1529(world):
    # decomposition releases nutrients; stronger under habitat stress.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'stress_gate')

def logic_1530(world):
    # decomposition releases nutrients; modulated by temperature.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'seasonal_gate')

def logic_1531(world):
    # decomposition releases nutrients; saturates at high source levels.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'saturation')

def logic_1532(world):
    # decomposition releases nutrients; activates above a food threshold.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'threshold')

def logic_1533(world):
    # decomposition releases nutrients; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'decomposition_rate', 'nutrients', 1, 'recovery')

def logic_1534(world):
    # deadwood feeds organic matter; direct.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'baseline')

def logic_1535(world):
    # deadwood feeds organic matter; stronger when soil is dry.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'dry_gate')

def logic_1536(world):
    # deadwood feeds organic matter; stronger when soil is wet.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'wet_gate')

def logic_1537(world):
    # deadwood feeds organic matter; stronger when temperature is high.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'heat_gate')

def logic_1538(world):
    # deadwood feeds organic matter; stronger when temperature is low.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'cold_gate')

def logic_1539(world):
    # deadwood feeds organic matter; stronger under fire pressure.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'fire_gate')

def logic_1540(world):
    # deadwood feeds organic matter; stronger when surface water is high.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'water_gate')

def logic_1541(world):
    # deadwood feeds organic matter; stronger when vegetation is scarce.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'scarcity_gate')

def logic_1542(world):
    # deadwood feeds organic matter; stronger when biomass is high.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'biomass_gate')

def logic_1543(world):
    # deadwood feeds organic matter; stronger under habitat stress.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'stress_gate')

def logic_1544(world):
    # deadwood feeds organic matter; modulated by temperature.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'seasonal_gate')

def logic_1545(world):
    # deadwood feeds organic matter; saturates at high source levels.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'saturation')

def logic_1546(world):
    # deadwood feeds organic matter; activates above a food threshold.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'threshold')

def logic_1547(world):
    # deadwood feeds organic matter; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'deadwood', 'organic_matter', 1, 'recovery')

def logic_1548(world):
    # ash supplies mineral nutrients; direct.
    _feedback(world, 'ash', 'nutrients', 1, 'baseline')

def logic_1549(world):
    # ash supplies mineral nutrients; stronger when soil is dry.
    _feedback(world, 'ash', 'nutrients', 1, 'dry_gate')

def logic_1550(world):
    # ash supplies mineral nutrients; stronger when soil is wet.
    _feedback(world, 'ash', 'nutrients', 1, 'wet_gate')

def logic_1551(world):
    # ash supplies mineral nutrients; stronger when temperature is high.
    _feedback(world, 'ash', 'nutrients', 1, 'heat_gate')

def logic_1552(world):
    # ash supplies mineral nutrients; stronger when temperature is low.
    _feedback(world, 'ash', 'nutrients', 1, 'cold_gate')

def logic_1553(world):
    # ash supplies mineral nutrients; stronger under fire pressure.
    _feedback(world, 'ash', 'nutrients', 1, 'fire_gate')

def logic_1554(world):
    # ash supplies mineral nutrients; stronger when surface water is high.
    _feedback(world, 'ash', 'nutrients', 1, 'water_gate')

def logic_1555(world):
    # ash supplies mineral nutrients; stronger when vegetation is scarce.
    _feedback(world, 'ash', 'nutrients', 1, 'scarcity_gate')

def logic_1556(world):
    # ash supplies mineral nutrients; stronger when biomass is high.
    _feedback(world, 'ash', 'nutrients', 1, 'biomass_gate')

def logic_1557(world):
    # ash supplies mineral nutrients; stronger under habitat stress.
    _feedback(world, 'ash', 'nutrients', 1, 'stress_gate')

def logic_1558(world):
    # ash supplies mineral nutrients; modulated by temperature.
    _feedback(world, 'ash', 'nutrients', 1, 'seasonal_gate')

def logic_1559(world):
    # ash supplies mineral nutrients; saturates at high source levels.
    _feedback(world, 'ash', 'nutrients', 1, 'saturation')

def logic_1560(world):
    # ash supplies mineral nutrients; activates above a food threshold.
    _feedback(world, 'ash', 'nutrients', 1, 'threshold')

def logic_1561(world):
    # ash supplies mineral nutrients; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'ash', 'nutrients', 1, 'recovery')

def logic_1562(world):
    # fire consumes deadwood; direct.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'baseline')

def logic_1563(world):
    # fire consumes deadwood; stronger when soil is dry.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'dry_gate')

def logic_1564(world):
    # fire consumes deadwood; stronger when soil is wet.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'wet_gate')

def logic_1565(world):
    # fire consumes deadwood; stronger when temperature is high.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'heat_gate')

def logic_1566(world):
    # fire consumes deadwood; stronger when temperature is low.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'cold_gate')

def logic_1567(world):
    # fire consumes deadwood; stronger under fire pressure.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'fire_gate')

def logic_1568(world):
    # fire consumes deadwood; stronger when surface water is high.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'water_gate')

def logic_1569(world):
    # fire consumes deadwood; stronger when vegetation is scarce.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'scarcity_gate')

def logic_1570(world):
    # fire consumes deadwood; stronger when biomass is high.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'biomass_gate')

def logic_1571(world):
    # fire consumes deadwood; stronger under habitat stress.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'stress_gate')

def logic_1572(world):
    # fire consumes deadwood; modulated by temperature.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'seasonal_gate')

def logic_1573(world):
    # fire consumes deadwood; saturates at high source levels.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'saturation')

def logic_1574(world):
    # fire consumes deadwood; activates above a food threshold.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'threshold')

def logic_1575(world):
    # fire consumes deadwood; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'fire_risk', 'deadwood', -1, 'recovery')

def logic_1576(world):
    # fire reduces vegetation; direct.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'baseline')

def logic_1577(world):
    # fire reduces vegetation; stronger when soil is dry.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'dry_gate')

def logic_1578(world):
    # fire reduces vegetation; stronger when soil is wet.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'wet_gate')

def logic_1579(world):
    # fire reduces vegetation; stronger when temperature is high.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'heat_gate')

def logic_1580(world):
    # fire reduces vegetation; stronger when temperature is low.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'cold_gate')

def logic_1581(world):
    # fire reduces vegetation; stronger under fire pressure.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'fire_gate')

def logic_1582(world):
    # fire reduces vegetation; stronger when surface water is high.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'water_gate')

def logic_1583(world):
    # fire reduces vegetation; stronger when vegetation is scarce.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'scarcity_gate')

def logic_1584(world):
    # fire reduces vegetation; stronger when biomass is high.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'biomass_gate')

def logic_1585(world):
    # fire reduces vegetation; stronger under habitat stress.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'stress_gate')

def logic_1586(world):
    # fire reduces vegetation; modulated by temperature.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'seasonal_gate')

def logic_1587(world):
    # fire reduces vegetation; saturates at high source levels.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'saturation')

def logic_1588(world):
    # fire reduces vegetation; activates above a food threshold.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'threshold')

def logic_1589(world):
    # fire reduces vegetation; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'fire_risk', 'vegetation', -1, 'recovery')

def logic_1590(world):
    # fire reduces biomass; direct.
    _feedback(world, 'fire_risk', 'biomass', -1, 'baseline')

def logic_1591(world):
    # fire reduces biomass; stronger when soil is dry.
    _feedback(world, 'fire_risk', 'biomass', -1, 'dry_gate')

def logic_1592(world):
    # fire reduces biomass; stronger when soil is wet.
    _feedback(world, 'fire_risk', 'biomass', -1, 'wet_gate')

def logic_1593(world):
    # fire reduces biomass; stronger when temperature is high.
    _feedback(world, 'fire_risk', 'biomass', -1, 'heat_gate')

def logic_1594(world):
    # fire reduces biomass; stronger when temperature is low.
    _feedback(world, 'fire_risk', 'biomass', -1, 'cold_gate')

def logic_1595(world):
    # fire reduces biomass; stronger under fire pressure.
    _feedback(world, 'fire_risk', 'biomass', -1, 'fire_gate')

def logic_1596(world):
    # fire reduces biomass; stronger when surface water is high.
    _feedback(world, 'fire_risk', 'biomass', -1, 'water_gate')

def logic_1597(world):
    # fire reduces biomass; stronger when vegetation is scarce.
    _feedback(world, 'fire_risk', 'biomass', -1, 'scarcity_gate')

def logic_1598(world):
    # fire reduces biomass; stronger when biomass is high.
    _feedback(world, 'fire_risk', 'biomass', -1, 'biomass_gate')

def logic_1599(world):
    # fire reduces biomass; stronger under habitat stress.
    _feedback(world, 'fire_risk', 'biomass', -1, 'stress_gate')

def logic_1600(world):
    # fire reduces biomass; modulated by temperature.
    _feedback(world, 'fire_risk', 'biomass', -1, 'seasonal_gate')

def logic_1601(world):
    # fire reduces biomass; saturates at high source levels.
    _feedback(world, 'fire_risk', 'biomass', -1, 'saturation')

def logic_1602(world):
    # fire reduces biomass; activates above a food threshold.
    _feedback(world, 'fire_risk', 'biomass', -1, 'threshold')

def logic_1603(world):
    # fire reduces biomass; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'fire_risk', 'biomass', -1, 'recovery')

def logic_1604(world):
    # fire releases stored carbon; direct.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'baseline')

def logic_1605(world):
    # fire releases stored carbon; stronger when soil is dry.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'dry_gate')

def logic_1606(world):
    # fire releases stored carbon; stronger when soil is wet.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'wet_gate')

def logic_1607(world):
    # fire releases stored carbon; stronger when temperature is high.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'heat_gate')

def logic_1608(world):
    # fire releases stored carbon; stronger when temperature is low.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'cold_gate')

def logic_1609(world):
    # fire releases stored carbon; stronger under fire pressure.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'fire_gate')

def logic_1610(world):
    # fire releases stored carbon; stronger when surface water is high.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'water_gate')

def logic_1611(world):
    # fire releases stored carbon; stronger when vegetation is scarce.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'scarcity_gate')

def logic_1612(world):
    # fire releases stored carbon; stronger when biomass is high.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'biomass_gate')

def logic_1613(world):
    # fire releases stored carbon; stronger under habitat stress.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'stress_gate')

def logic_1614(world):
    # fire releases stored carbon; modulated by temperature.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'seasonal_gate')

def logic_1615(world):
    # fire releases stored carbon; saturates at high source levels.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'saturation')

def logic_1616(world):
    # fire releases stored carbon; activates above a food threshold.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'threshold')

def logic_1617(world):
    # fire releases stored carbon; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'fire_risk', 'carbon_storage', -1, 'recovery')

def logic_1618(world):
    # ash alters soil carbon inputs; direct.
    _feedback(world, 'ash', 'soil_carbon', 1, 'baseline')

def logic_1619(world):
    # ash alters soil carbon inputs; stronger when soil is dry.
    _feedback(world, 'ash', 'soil_carbon', 1, 'dry_gate')

def logic_1620(world):
    # ash alters soil carbon inputs; stronger when soil is wet.
    _feedback(world, 'ash', 'soil_carbon', 1, 'wet_gate')

def logic_1621(world):
    # ash alters soil carbon inputs; stronger when temperature is high.
    _feedback(world, 'ash', 'soil_carbon', 1, 'heat_gate')

def logic_1622(world):
    # ash alters soil carbon inputs; stronger when temperature is low.
    _feedback(world, 'ash', 'soil_carbon', 1, 'cold_gate')

def logic_1623(world):
    # ash alters soil carbon inputs; stronger under fire pressure.
    _feedback(world, 'ash', 'soil_carbon', 1, 'fire_gate')

def logic_1624(world):
    # ash alters soil carbon inputs; stronger when surface water is high.
    _feedback(world, 'ash', 'soil_carbon', 1, 'water_gate')

def logic_1625(world):
    # ash alters soil carbon inputs; stronger when vegetation is scarce.
    _feedback(world, 'ash', 'soil_carbon', 1, 'scarcity_gate')

def logic_1626(world):
    # ash alters soil carbon inputs; stronger when biomass is high.
    _feedback(world, 'ash', 'soil_carbon', 1, 'biomass_gate')

def logic_1627(world):
    # ash alters soil carbon inputs; stronger under habitat stress.
    _feedback(world, 'ash', 'soil_carbon', 1, 'stress_gate')

def logic_1628(world):
    # ash alters soil carbon inputs; modulated by temperature.
    _feedback(world, 'ash', 'soil_carbon', 1, 'seasonal_gate')

def logic_1629(world):
    # ash alters soil carbon inputs; saturates at high source levels.
    _feedback(world, 'ash', 'soil_carbon', 1, 'saturation')

def logic_1630(world):
    # ash alters soil carbon inputs; activates above a food threshold.
    _feedback(world, 'ash', 'soil_carbon', 1, 'threshold')

def logic_1631(world):
    # ash alters soil carbon inputs; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'ash', 'soil_carbon', 1, 'recovery')

def logic_1632(world):
    # soil carbon contributes ecosystem carbon; direct.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'baseline')

def logic_1633(world):
    # soil carbon contributes ecosystem carbon; stronger when soil is dry.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'dry_gate')

def logic_1634(world):
    # soil carbon contributes ecosystem carbon; stronger when soil is wet.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'wet_gate')

def logic_1635(world):
    # soil carbon contributes ecosystem carbon; stronger when temperature is high.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'heat_gate')

def logic_1636(world):
    # soil carbon contributes ecosystem carbon; stronger when temperature is low.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'cold_gate')

def logic_1637(world):
    # soil carbon contributes ecosystem carbon; stronger under fire pressure.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'fire_gate')

def logic_1638(world):
    # soil carbon contributes ecosystem carbon; stronger when surface water is high.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'water_gate')

def logic_1639(world):
    # soil carbon contributes ecosystem carbon; stronger when vegetation is scarce.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'scarcity_gate')

def logic_1640(world):
    # soil carbon contributes ecosystem carbon; stronger when biomass is high.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'biomass_gate')

def logic_1641(world):
    # soil carbon contributes ecosystem carbon; stronger under habitat stress.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'stress_gate')

def logic_1642(world):
    # soil carbon contributes ecosystem carbon; modulated by temperature.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'seasonal_gate')

def logic_1643(world):
    # soil carbon contributes ecosystem carbon; saturates at high source levels.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'saturation')

def logic_1644(world):
    # soil carbon contributes ecosystem carbon; activates above a food threshold.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'threshold')

def logic_1645(world):
    # soil carbon contributes ecosystem carbon; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'soil_carbon', 'carbon_storage', 1, 'recovery')

def logic_1646(world):
    # flowers support pollinators; direct.
    _feedback(world, 'flowers', 'pollinators', 1, 'baseline')

def logic_1647(world):
    # flowers support pollinators; stronger when soil is dry.
    _feedback(world, 'flowers', 'pollinators', 1, 'dry_gate')

def logic_1648(world):
    # flowers support pollinators; stronger when soil is wet.
    _feedback(world, 'flowers', 'pollinators', 1, 'wet_gate')

def logic_1649(world):
    # flowers support pollinators; stronger when temperature is high.
    _feedback(world, 'flowers', 'pollinators', 1, 'heat_gate')

def logic_1650(world):
    # flowers support pollinators; stronger when temperature is low.
    _feedback(world, 'flowers', 'pollinators', 1, 'cold_gate')

def logic_1651(world):
    # flowers support pollinators; stronger under fire pressure.
    _feedback(world, 'flowers', 'pollinators', 1, 'fire_gate')

def logic_1652(world):
    # flowers support pollinators; stronger when surface water is high.
    _feedback(world, 'flowers', 'pollinators', 1, 'water_gate')

def logic_1653(world):
    # flowers support pollinators; stronger when vegetation is scarce.
    _feedback(world, 'flowers', 'pollinators', 1, 'scarcity_gate')

def logic_1654(world):
    # flowers support pollinators; stronger when biomass is high.
    _feedback(world, 'flowers', 'pollinators', 1, 'biomass_gate')

def logic_1655(world):
    # flowers support pollinators; stronger under habitat stress.
    _feedback(world, 'flowers', 'pollinators', 1, 'stress_gate')

def logic_1656(world):
    # flowers support pollinators; modulated by temperature.
    _feedback(world, 'flowers', 'pollinators', 1, 'seasonal_gate')

def logic_1657(world):
    # flowers support pollinators; saturates at high source levels.
    _feedback(world, 'flowers', 'pollinators', 1, 'saturation')

def logic_1658(world):
    # flowers support pollinators; activates above a food threshold.
    _feedback(world, 'flowers', 'pollinators', 1, 'threshold')

def logic_1659(world):
    # flowers support pollinators; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'flowers', 'pollinators', 1, 'recovery')

def logic_1660(world):
    # pollination sustains flowering; direct.
    _feedback(world, 'pollinators', 'flowers', 1, 'baseline')

def logic_1661(world):
    # pollination sustains flowering; stronger when soil is dry.
    _feedback(world, 'pollinators', 'flowers', 1, 'dry_gate')

def logic_1662(world):
    # pollination sustains flowering; stronger when soil is wet.
    _feedback(world, 'pollinators', 'flowers', 1, 'wet_gate')

def logic_1663(world):
    # pollination sustains flowering; stronger when temperature is high.
    _feedback(world, 'pollinators', 'flowers', 1, 'heat_gate')

def logic_1664(world):
    # pollination sustains flowering; stronger when temperature is low.
    _feedback(world, 'pollinators', 'flowers', 1, 'cold_gate')

def logic_1665(world):
    # pollination sustains flowering; stronger under fire pressure.
    _feedback(world, 'pollinators', 'flowers', 1, 'fire_gate')

def logic_1666(world):
    # pollination sustains flowering; stronger when surface water is high.
    _feedback(world, 'pollinators', 'flowers', 1, 'water_gate')

def logic_1667(world):
    # pollination sustains flowering; stronger when vegetation is scarce.
    _feedback(world, 'pollinators', 'flowers', 1, 'scarcity_gate')

def logic_1668(world):
    # pollination sustains flowering; stronger when biomass is high.
    _feedback(world, 'pollinators', 'flowers', 1, 'biomass_gate')

def logic_1669(world):
    # pollination sustains flowering; stronger under habitat stress.
    _feedback(world, 'pollinators', 'flowers', 1, 'stress_gate')

def logic_1670(world):
    # pollination sustains flowering; modulated by temperature.
    _feedback(world, 'pollinators', 'flowers', 1, 'seasonal_gate')

def logic_1671(world):
    # pollination sustains flowering; saturates at high source levels.
    _feedback(world, 'pollinators', 'flowers', 1, 'saturation')

def logic_1672(world):
    # pollination sustains flowering; activates above a food threshold.
    _feedback(world, 'pollinators', 'flowers', 1, 'threshold')

def logic_1673(world):
    # pollination sustains flowering; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'pollinators', 'flowers', 1, 'recovery')

def logic_1674(world):
    # seed banks support vegetation recovery; direct.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'baseline')

def logic_1675(world):
    # seed banks support vegetation recovery; stronger when soil is dry.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'dry_gate')

def logic_1676(world):
    # seed banks support vegetation recovery; stronger when soil is wet.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'wet_gate')

def logic_1677(world):
    # seed banks support vegetation recovery; stronger when temperature is high.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'heat_gate')

def logic_1678(world):
    # seed banks support vegetation recovery; stronger when temperature is low.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'cold_gate')

def logic_1679(world):
    # seed banks support vegetation recovery; stronger under fire pressure.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'fire_gate')

def logic_1680(world):
    # seed banks support vegetation recovery; stronger when surface water is high.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'water_gate')

def logic_1681(world):
    # seed banks support vegetation recovery; stronger when vegetation is scarce.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'scarcity_gate')

def logic_1682(world):
    # seed banks support vegetation recovery; stronger when biomass is high.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'biomass_gate')

def logic_1683(world):
    # seed banks support vegetation recovery; stronger under habitat stress.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'stress_gate')

def logic_1684(world):
    # seed banks support vegetation recovery; modulated by temperature.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'seasonal_gate')

def logic_1685(world):
    # seed banks support vegetation recovery; saturates at high source levels.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'saturation')

def logic_1686(world):
    # seed banks support vegetation recovery; activates above a food threshold.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'threshold')

def logic_1687(world):
    # seed banks support vegetation recovery; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'seed_bank', 'vegetation', 1, 'recovery')

def logic_1688(world):
    # vegetation replenishes seeds; direct.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'baseline')

def logic_1689(world):
    # vegetation replenishes seeds; stronger when soil is dry.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'dry_gate')

def logic_1690(world):
    # vegetation replenishes seeds; stronger when soil is wet.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'wet_gate')

def logic_1691(world):
    # vegetation replenishes seeds; stronger when temperature is high.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'heat_gate')

def logic_1692(world):
    # vegetation replenishes seeds; stronger when temperature is low.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'cold_gate')

def logic_1693(world):
    # vegetation replenishes seeds; stronger under fire pressure.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'fire_gate')

def logic_1694(world):
    # vegetation replenishes seeds; stronger when surface water is high.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'water_gate')

def logic_1695(world):
    # vegetation replenishes seeds; stronger when vegetation is scarce.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'scarcity_gate')

def logic_1696(world):
    # vegetation replenishes seeds; stronger when biomass is high.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'biomass_gate')

def logic_1697(world):
    # vegetation replenishes seeds; stronger under habitat stress.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'stress_gate')

def logic_1698(world):
    # vegetation replenishes seeds; modulated by temperature.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'seasonal_gate')

def logic_1699(world):
    # vegetation replenishes seeds; saturates at high source levels.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'saturation')

def logic_1700(world):
    # vegetation replenishes seeds; activates above a food threshold.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'threshold')

def logic_1701(world):
    # vegetation replenishes seeds; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'vegetation', 'seed_bank', 1, 'recovery')

def logic_1702(world):
    # herbivory consumes vegetation; direct.
    _feedback(world, 'herbivore', 'vegetation', -1, 'baseline')

def logic_1703(world):
    # herbivory consumes vegetation; stronger when soil is dry.
    _feedback(world, 'herbivore', 'vegetation', -1, 'dry_gate')

def logic_1704(world):
    # herbivory consumes vegetation; stronger when soil is wet.
    _feedback(world, 'herbivore', 'vegetation', -1, 'wet_gate')

def logic_1705(world):
    # herbivory consumes vegetation; stronger when temperature is high.
    _feedback(world, 'herbivore', 'vegetation', -1, 'heat_gate')

def logic_1706(world):
    # herbivory consumes vegetation; stronger when temperature is low.
    _feedback(world, 'herbivore', 'vegetation', -1, 'cold_gate')

def logic_1707(world):
    # herbivory consumes vegetation; stronger under fire pressure.
    _feedback(world, 'herbivore', 'vegetation', -1, 'fire_gate')

def logic_1708(world):
    # herbivory consumes vegetation; stronger when surface water is high.
    _feedback(world, 'herbivore', 'vegetation', -1, 'water_gate')

def logic_1709(world):
    # herbivory consumes vegetation; stronger when vegetation is scarce.
    _feedback(world, 'herbivore', 'vegetation', -1, 'scarcity_gate')

def logic_1710(world):
    # herbivory consumes vegetation; stronger when biomass is high.
    _feedback(world, 'herbivore', 'vegetation', -1, 'biomass_gate')

def logic_1711(world):
    # herbivory consumes vegetation; stronger under habitat stress.
    _feedback(world, 'herbivore', 'vegetation', -1, 'stress_gate')

def logic_1712(world):
    # herbivory consumes vegetation; modulated by temperature.
    _feedback(world, 'herbivore', 'vegetation', -1, 'seasonal_gate')

def logic_1713(world):
    # herbivory consumes vegetation; saturates at high source levels.
    _feedback(world, 'herbivore', 'vegetation', -1, 'saturation')

def logic_1714(world):
    # herbivory consumes vegetation; activates above a food threshold.
    _feedback(world, 'herbivore', 'vegetation', -1, 'threshold')

def logic_1715(world):
    # herbivory consumes vegetation; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'herbivore', 'vegetation', -1, 'recovery')

def logic_1716(world):
    # vegetation supports herbivores; direct.
    _feedback(world, 'vegetation', 'herbivore', 1, 'baseline')

def logic_1717(world):
    # vegetation supports herbivores; stronger when soil is dry.
    _feedback(world, 'vegetation', 'herbivore', 1, 'dry_gate')

def logic_1718(world):
    # vegetation supports herbivores; stronger when soil is wet.
    _feedback(world, 'vegetation', 'herbivore', 1, 'wet_gate')

def logic_1719(world):
    # vegetation supports herbivores; stronger when temperature is high.
    _feedback(world, 'vegetation', 'herbivore', 1, 'heat_gate')

def logic_1720(world):
    # vegetation supports herbivores; stronger when temperature is low.
    _feedback(world, 'vegetation', 'herbivore', 1, 'cold_gate')

def logic_1721(world):
    # vegetation supports herbivores; stronger under fire pressure.
    _feedback(world, 'vegetation', 'herbivore', 1, 'fire_gate')

def logic_1722(world):
    # vegetation supports herbivores; stronger when surface water is high.
    _feedback(world, 'vegetation', 'herbivore', 1, 'water_gate')

def logic_1723(world):
    # vegetation supports herbivores; stronger when vegetation is scarce.
    _feedback(world, 'vegetation', 'herbivore', 1, 'scarcity_gate')

def logic_1724(world):
    # vegetation supports herbivores; stronger when biomass is high.
    _feedback(world, 'vegetation', 'herbivore', 1, 'biomass_gate')

def logic_1725(world):
    # vegetation supports herbivores; stronger under habitat stress.
    _feedback(world, 'vegetation', 'herbivore', 1, 'stress_gate')

def logic_1726(world):
    # vegetation supports herbivores; modulated by temperature.
    _feedback(world, 'vegetation', 'herbivore', 1, 'seasonal_gate')

def logic_1727(world):
    # vegetation supports herbivores; saturates at high source levels.
    _feedback(world, 'vegetation', 'herbivore', 1, 'saturation')

def logic_1728(world):
    # vegetation supports herbivores; activates above a food threshold.
    _feedback(world, 'vegetation', 'herbivore', 1, 'threshold')

def logic_1729(world):
    # vegetation supports herbivores; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'vegetation', 'herbivore', 1, 'recovery')

def logic_1730(world):
    # herbivore mortality contributes carrion; direct.
    _feedback(world, 'herbivore', 'carrion', 1, 'baseline')

def logic_1731(world):
    # herbivore mortality contributes carrion; stronger when soil is dry.
    _feedback(world, 'herbivore', 'carrion', 1, 'dry_gate')

def logic_1732(world):
    # herbivore mortality contributes carrion; stronger when soil is wet.
    _feedback(world, 'herbivore', 'carrion', 1, 'wet_gate')

def logic_1733(world):
    # herbivore mortality contributes carrion; stronger when temperature is high.
    _feedback(world, 'herbivore', 'carrion', 1, 'heat_gate')

def logic_1734(world):
    # herbivore mortality contributes carrion; stronger when temperature is low.
    _feedback(world, 'herbivore', 'carrion', 1, 'cold_gate')

def logic_1735(world):
    # herbivore mortality contributes carrion; stronger under fire pressure.
    _feedback(world, 'herbivore', 'carrion', 1, 'fire_gate')

def logic_1736(world):
    # herbivore mortality contributes carrion; stronger when surface water is high.
    _feedback(world, 'herbivore', 'carrion', 1, 'water_gate')

def logic_1737(world):
    # herbivore mortality contributes carrion; stronger when vegetation is scarce.
    _feedback(world, 'herbivore', 'carrion', 1, 'scarcity_gate')

def logic_1738(world):
    # herbivore mortality contributes carrion; stronger when biomass is high.
    _feedback(world, 'herbivore', 'carrion', 1, 'biomass_gate')

def logic_1739(world):
    # herbivore mortality contributes carrion; stronger under habitat stress.
    _feedback(world, 'herbivore', 'carrion', 1, 'stress_gate')

def logic_1740(world):
    # herbivore mortality contributes carrion; modulated by temperature.
    _feedback(world, 'herbivore', 'carrion', 1, 'seasonal_gate')

def logic_1741(world):
    # herbivore mortality contributes carrion; saturates at high source levels.
    _feedback(world, 'herbivore', 'carrion', 1, 'saturation')

def logic_1742(world):
    # herbivore mortality contributes carrion; activates above a food threshold.
    _feedback(world, 'herbivore', 'carrion', 1, 'threshold')

def logic_1743(world):
    # herbivore mortality contributes carrion; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'herbivore', 'carrion', 1, 'recovery')

def logic_1744(world):
    # predation reduces herbivores; direct.
    _feedback(world, 'predator', 'herbivore', -1, 'baseline')

def logic_1745(world):
    # predation reduces herbivores; stronger when soil is dry.
    _feedback(world, 'predator', 'herbivore', -1, 'dry_gate')

def logic_1746(world):
    # predation reduces herbivores; stronger when soil is wet.
    _feedback(world, 'predator', 'herbivore', -1, 'wet_gate')

def logic_1747(world):
    # predation reduces herbivores; stronger when temperature is high.
    _feedback(world, 'predator', 'herbivore', -1, 'heat_gate')

def logic_1748(world):
    # predation reduces herbivores; stronger when temperature is low.
    _feedback(world, 'predator', 'herbivore', -1, 'cold_gate')

def logic_1749(world):
    # predation reduces herbivores; stronger under fire pressure.
    _feedback(world, 'predator', 'herbivore', -1, 'fire_gate')

def logic_1750(world):
    # predation reduces herbivores; stronger when surface water is high.
    _feedback(world, 'predator', 'herbivore', -1, 'water_gate')

def logic_1751(world):
    # predation reduces herbivores; stronger when vegetation is scarce.
    _feedback(world, 'predator', 'herbivore', -1, 'scarcity_gate')

def logic_1752(world):
    # predation reduces herbivores; stronger when biomass is high.
    _feedback(world, 'predator', 'herbivore', -1, 'biomass_gate')

def logic_1753(world):
    # predation reduces herbivores; stronger under habitat stress.
    _feedback(world, 'predator', 'herbivore', -1, 'stress_gate')

def logic_1754(world):
    # predation reduces herbivores; modulated by temperature.
    _feedback(world, 'predator', 'herbivore', -1, 'seasonal_gate')

def logic_1755(world):
    # predation reduces herbivores; saturates at high source levels.
    _feedback(world, 'predator', 'herbivore', -1, 'saturation')

def logic_1756(world):
    # predation reduces herbivores; activates above a food threshold.
    _feedback(world, 'predator', 'herbivore', -1, 'threshold')

def logic_1757(world):
    # predation reduces herbivores; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'predator', 'herbivore', -1, 'recovery')

def logic_1758(world):
    # herbivores support predators; direct.
    _feedback(world, 'herbivore', 'predator', 1, 'baseline')

def logic_1759(world):
    # herbivores support predators; stronger when soil is dry.
    _feedback(world, 'herbivore', 'predator', 1, 'dry_gate')

def logic_1760(world):
    # herbivores support predators; stronger when soil is wet.
    _feedback(world, 'herbivore', 'predator', 1, 'wet_gate')

def logic_1761(world):
    # herbivores support predators; stronger when temperature is high.
    _feedback(world, 'herbivore', 'predator', 1, 'heat_gate')

def logic_1762(world):
    # herbivores support predators; stronger when temperature is low.
    _feedback(world, 'herbivore', 'predator', 1, 'cold_gate')

def logic_1763(world):
    # herbivores support predators; stronger under fire pressure.
    _feedback(world, 'herbivore', 'predator', 1, 'fire_gate')

def logic_1764(world):
    # herbivores support predators; stronger when surface water is high.
    _feedback(world, 'herbivore', 'predator', 1, 'water_gate')

def logic_1765(world):
    # herbivores support predators; stronger when vegetation is scarce.
    _feedback(world, 'herbivore', 'predator', 1, 'scarcity_gate')

def logic_1766(world):
    # herbivores support predators; stronger when biomass is high.
    _feedback(world, 'herbivore', 'predator', 1, 'biomass_gate')

def logic_1767(world):
    # herbivores support predators; stronger under habitat stress.
    _feedback(world, 'herbivore', 'predator', 1, 'stress_gate')

def logic_1768(world):
    # herbivores support predators; modulated by temperature.
    _feedback(world, 'herbivore', 'predator', 1, 'seasonal_gate')

def logic_1769(world):
    # herbivores support predators; saturates at high source levels.
    _feedback(world, 'herbivore', 'predator', 1, 'saturation')

def logic_1770(world):
    # herbivores support predators; activates above a food threshold.
    _feedback(world, 'herbivore', 'predator', 1, 'threshold')

def logic_1771(world):
    # herbivores support predators; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'herbivore', 'predator', 1, 'recovery')

def logic_1772(world):
    # predator mortality contributes carrion; direct.
    _feedback(world, 'predator', 'carrion', 1, 'baseline')

def logic_1773(world):
    # predator mortality contributes carrion; stronger when soil is dry.
    _feedback(world, 'predator', 'carrion', 1, 'dry_gate')

def logic_1774(world):
    # predator mortality contributes carrion; stronger when soil is wet.
    _feedback(world, 'predator', 'carrion', 1, 'wet_gate')

def logic_1775(world):
    # predator mortality contributes carrion; stronger when temperature is high.
    _feedback(world, 'predator', 'carrion', 1, 'heat_gate')

def logic_1776(world):
    # predator mortality contributes carrion; stronger when temperature is low.
    _feedback(world, 'predator', 'carrion', 1, 'cold_gate')

def logic_1777(world):
    # predator mortality contributes carrion; stronger under fire pressure.
    _feedback(world, 'predator', 'carrion', 1, 'fire_gate')

def logic_1778(world):
    # predator mortality contributes carrion; stronger when surface water is high.
    _feedback(world, 'predator', 'carrion', 1, 'water_gate')

def logic_1779(world):
    # predator mortality contributes carrion; stronger when vegetation is scarce.
    _feedback(world, 'predator', 'carrion', 1, 'scarcity_gate')

def logic_1780(world):
    # predator mortality contributes carrion; stronger when biomass is high.
    _feedback(world, 'predator', 'carrion', 1, 'biomass_gate')

def logic_1781(world):
    # predator mortality contributes carrion; stronger under habitat stress.
    _feedback(world, 'predator', 'carrion', 1, 'stress_gate')

def logic_1782(world):
    # predator mortality contributes carrion; modulated by temperature.
    _feedback(world, 'predator', 'carrion', 1, 'seasonal_gate')

def logic_1783(world):
    # predator mortality contributes carrion; saturates at high source levels.
    _feedback(world, 'predator', 'carrion', 1, 'saturation')

def logic_1784(world):
    # predator mortality contributes carrion; activates above a food threshold.
    _feedback(world, 'predator', 'carrion', 1, 'threshold')

def logic_1785(world):
    # predator mortality contributes carrion; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'predator', 'carrion', 1, 'recovery')

def logic_1786(world):
    # carrion feeds decomposers; direct.
    _feedback(world, 'carrion', 'organic_matter', 1, 'baseline')

def logic_1787(world):
    # carrion feeds decomposers; stronger when soil is dry.
    _feedback(world, 'carrion', 'organic_matter', 1, 'dry_gate')

def logic_1788(world):
    # carrion feeds decomposers; stronger when soil is wet.
    _feedback(world, 'carrion', 'organic_matter', 1, 'wet_gate')

def logic_1789(world):
    # carrion feeds decomposers; stronger when temperature is high.
    _feedback(world, 'carrion', 'organic_matter', 1, 'heat_gate')

def logic_1790(world):
    # carrion feeds decomposers; stronger when temperature is low.
    _feedback(world, 'carrion', 'organic_matter', 1, 'cold_gate')

def logic_1791(world):
    # carrion feeds decomposers; stronger under fire pressure.
    _feedback(world, 'carrion', 'organic_matter', 1, 'fire_gate')

def logic_1792(world):
    # carrion feeds decomposers; stronger when surface water is high.
    _feedback(world, 'carrion', 'organic_matter', 1, 'water_gate')

def logic_1793(world):
    # carrion feeds decomposers; stronger when vegetation is scarce.
    _feedback(world, 'carrion', 'organic_matter', 1, 'scarcity_gate')

def logic_1794(world):
    # carrion feeds decomposers; stronger when biomass is high.
    _feedback(world, 'carrion', 'organic_matter', 1, 'biomass_gate')

def logic_1795(world):
    # carrion feeds decomposers; stronger under habitat stress.
    _feedback(world, 'carrion', 'organic_matter', 1, 'stress_gate')

def logic_1796(world):
    # carrion feeds decomposers; modulated by temperature.
    _feedback(world, 'carrion', 'organic_matter', 1, 'seasonal_gate')

def logic_1797(world):
    # carrion feeds decomposers; saturates at high source levels.
    _feedback(world, 'carrion', 'organic_matter', 1, 'saturation')

def logic_1798(world):
    # carrion feeds decomposers; activates above a food threshold.
    _feedback(world, 'carrion', 'organic_matter', 1, 'threshold')

def logic_1799(world):
    # carrion feeds decomposers; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'carrion', 'organic_matter', 1, 'recovery')

def logic_1800(world):
    # pathogens reduce biodiversity; direct.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'baseline')

def logic_1801(world):
    # pathogens reduce biodiversity; stronger when soil is dry.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'dry_gate')

def logic_1802(world):
    # pathogens reduce biodiversity; stronger when soil is wet.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'wet_gate')

def logic_1803(world):
    # pathogens reduce biodiversity; stronger when temperature is high.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'heat_gate')

def logic_1804(world):
    # pathogens reduce biodiversity; stronger when temperature is low.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'cold_gate')

def logic_1805(world):
    # pathogens reduce biodiversity; stronger under fire pressure.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'fire_gate')

def logic_1806(world):
    # pathogens reduce biodiversity; stronger when surface water is high.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'water_gate')

def logic_1807(world):
    # pathogens reduce biodiversity; stronger when vegetation is scarce.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'scarcity_gate')

def logic_1808(world):
    # pathogens reduce biodiversity; stronger when biomass is high.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'biomass_gate')

def logic_1809(world):
    # pathogens reduce biodiversity; stronger under habitat stress.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'stress_gate')

def logic_1810(world):
    # pathogens reduce biodiversity; modulated by temperature.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'seasonal_gate')

def logic_1811(world):
    # pathogens reduce biodiversity; saturates at high source levels.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'saturation')

def logic_1812(world):
    # pathogens reduce biodiversity; activates above a food threshold.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'threshold')

def logic_1813(world):
    # pathogens reduce biodiversity; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'pathogen_load', 'biodiversity', -1, 'recovery')

def logic_1814(world):
    # diverse communities dilute pathogens; direct.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'baseline')

def logic_1815(world):
    # diverse communities dilute pathogens; stronger when soil is dry.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'dry_gate')

def logic_1816(world):
    # diverse communities dilute pathogens; stronger when soil is wet.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'wet_gate')

def logic_1817(world):
    # diverse communities dilute pathogens; stronger when temperature is high.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'heat_gate')

def logic_1818(world):
    # diverse communities dilute pathogens; stronger when temperature is low.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'cold_gate')

def logic_1819(world):
    # diverse communities dilute pathogens; stronger under fire pressure.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'fire_gate')

def logic_1820(world):
    # diverse communities dilute pathogens; stronger when surface water is high.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'water_gate')

def logic_1821(world):
    # diverse communities dilute pathogens; stronger when vegetation is scarce.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'scarcity_gate')

def logic_1822(world):
    # diverse communities dilute pathogens; stronger when biomass is high.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'biomass_gate')

def logic_1823(world):
    # diverse communities dilute pathogens; stronger under habitat stress.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'stress_gate')

def logic_1824(world):
    # diverse communities dilute pathogens; modulated by temperature.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'seasonal_gate')

def logic_1825(world):
    # diverse communities dilute pathogens; saturates at high source levels.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'saturation')

def logic_1826(world):
    # diverse communities dilute pathogens; activates above a food threshold.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'threshold')

def logic_1827(world):
    # diverse communities dilute pathogens; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'biodiversity', 'pathogen_load', -1, 'recovery')

def logic_1828(world):
    # diversity buffers habitat stress; direct.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'baseline')

def logic_1829(world):
    # diversity buffers habitat stress; stronger when soil is dry.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'dry_gate')

def logic_1830(world):
    # diversity buffers habitat stress; stronger when soil is wet.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'wet_gate')

def logic_1831(world):
    # diversity buffers habitat stress; stronger when temperature is high.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'heat_gate')

def logic_1832(world):
    # diversity buffers habitat stress; stronger when temperature is low.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'cold_gate')

def logic_1833(world):
    # diversity buffers habitat stress; stronger under fire pressure.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'fire_gate')

def logic_1834(world):
    # diversity buffers habitat stress; stronger when surface water is high.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'water_gate')

def logic_1835(world):
    # diversity buffers habitat stress; stronger when vegetation is scarce.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'scarcity_gate')

def logic_1836(world):
    # diversity buffers habitat stress; stronger when biomass is high.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'biomass_gate')

def logic_1837(world):
    # diversity buffers habitat stress; stronger under habitat stress.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'stress_gate')

def logic_1838(world):
    # diversity buffers habitat stress; modulated by temperature.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'seasonal_gate')

def logic_1839(world):
    # diversity buffers habitat stress; saturates at high source levels.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'saturation')

def logic_1840(world):
    # diversity buffers habitat stress; activates above a food threshold.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'threshold')

def logic_1841(world):
    # diversity buffers habitat stress; relaxes toward a biodiversity-linked equilibrium.
    _feedback(world, 'biodiversity', 'habitat_stress', -1, 'recovery')

def logic_1842(world):
    # habitat stress erodes diversity; direct.
    _feedback(world, 'habitat_stress', 'biodiversity', -1, 'baseline')

def logic_1843(world):
    # habitat stress erodes diversity; stronger when soil is dry.
    _feedback(world, 'habitat_stress', 'biodiversity', -1, 'dry_gate')

def logic_1844(world):
    # habitat stress erodes diversity; stronger when soil is wet.
    _feedback(world, 'habitat_stress', 'biodiversity', -1, 'wet_gate')
