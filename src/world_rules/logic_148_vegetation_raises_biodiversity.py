def apply(world):
    world.biodiversity = (world.biodiversity + 0.005 * world.vegetation).clamp(0.0, 1.0)
