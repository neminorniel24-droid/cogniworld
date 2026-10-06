def apply(world):
    world.surface_ice = (world.surface_ice - world.fire_risk * 0.005).clamp(0.0, 1.0)
