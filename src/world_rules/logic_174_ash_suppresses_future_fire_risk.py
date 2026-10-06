def apply(world):
    world.fire_risk = (world.fire_risk * (1.0 - 0.05 * world.ash)).clamp(0.0, 1.0)
