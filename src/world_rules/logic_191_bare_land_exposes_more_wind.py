def apply(world):
    world.wind_x = (world.wind_x + 0.004 * (1.0 - world.vegetation)).clamp(-1.0, 1.0); world.wind_y = (world.wind_y + 0.004 * (1.0 - world.vegetation)).clamp(-1.0, 1.0)
