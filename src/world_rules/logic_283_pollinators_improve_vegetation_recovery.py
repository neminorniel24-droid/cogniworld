def apply(world):
    world.vegetation = (world.vegetation + world.pollinators * 0.002).clamp(0.0, 1.0)
