def apply(world):
    world.runoff = (world.runoff * (1.0 - 0.20 * world.wetland)).clamp(0.0, 1.0)
