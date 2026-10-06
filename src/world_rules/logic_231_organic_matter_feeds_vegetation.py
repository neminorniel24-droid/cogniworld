def apply(world):
    world.vegetation = (world.vegetation + world.organic_matter * 0.005).clamp(0.0, 1.0)
