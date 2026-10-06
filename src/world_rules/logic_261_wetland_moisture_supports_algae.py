def apply(world):
    world.algae = (world.algae + world.wetland * world.soil_moisture * 0.008).clamp(0.0, 1.0)
