def apply(world):
    world.soil_moisture = (world.soil_moisture + 0.002 * world.humidity * world.vegetation).clamp(0.0, 1.0)
