def apply(world):
    world.wind_x = world.wind_x * (1.0 - 0.05 * world.vegetation); world.wind_y = world.wind_y * (1.0 - 0.05 * world.vegetation)
