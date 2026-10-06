def apply(world):
    world.biodiversity = (world.biodiversity + 0.002 * world.detritus).clamp(0.0, 1.0)
