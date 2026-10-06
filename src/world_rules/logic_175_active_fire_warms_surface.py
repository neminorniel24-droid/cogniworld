def apply(world):
    world.temperature_target = (world.temperature_target + 0.01 * (world.fire_risk > 0.8).float()).clamp(0.0, 1.0)
