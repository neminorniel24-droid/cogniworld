def apply(world):
    world.carbon_storage = (world.carbon_storage - world.fire_risk * world.deadwood * 0.004).clamp(0.0, 1.0)
