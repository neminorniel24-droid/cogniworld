def apply(world):
    world.fire_risk = (world.fire_risk - 0.006 * world.humidity).clamp(0.0, 1.0)
