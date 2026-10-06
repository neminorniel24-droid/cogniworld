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
