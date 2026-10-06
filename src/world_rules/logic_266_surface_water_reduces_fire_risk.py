def apply(world):
    world.fire_risk = (world.fire_risk - world.surface_water * 0.004).clamp(0.0, 1.0)
