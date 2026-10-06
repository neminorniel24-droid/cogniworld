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
