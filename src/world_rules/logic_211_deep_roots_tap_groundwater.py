def apply(world):
    world.soil_moisture = (world.soil_moisture + world.groundwater * world.root_density * 0.01).clamp(0.0, 1.0)
