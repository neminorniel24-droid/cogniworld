def apply(world):
    world.organic_matter = (world.organic_matter + world.deadwood * 0.004).clamp(0.0, 1.0)
