def apply(world):
    world.fire_risk = (world.fire_risk + 0.008 * world.vegetation * (1.0 - world.soil_moisture)).clamp(0.0, 1.0)
