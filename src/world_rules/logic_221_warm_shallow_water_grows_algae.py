def apply(world):
    world.algae = (world.algae + world.surface_water * world.temperature * 0.02).clamp(0.0, 1.0)
