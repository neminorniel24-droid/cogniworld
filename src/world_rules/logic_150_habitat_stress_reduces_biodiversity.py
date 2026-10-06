def apply(world):
    world.biodiversity = (world.biodiversity - 0.006 * world.habitat_stress).clamp(0.0, 1.0)
