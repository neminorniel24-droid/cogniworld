def apply(world):
    world.organic_matter = (world.organic_matter - world.decomposition_rate * 0.02).clamp(0.0, 1.0)
