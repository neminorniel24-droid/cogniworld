def apply(world):
    world.vegetation = (world.vegetation - 0.006 * (world.herbivore**2)).clamp(0.0, 1.0)
