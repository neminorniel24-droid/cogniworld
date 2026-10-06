def apply(world):
    world.root_density = (world.root_density * (0.2 + 0.8 * world.soil_depth)).clamp(0.0, 1.0)
