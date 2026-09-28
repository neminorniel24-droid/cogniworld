import torch

from world.biome import World, PLAINS, RIVER, MOUNTAIN, DESERT, CAVE

DEVICE = torch.device("cpu")

MINI_CONFIG = {
    "world_size": 8,
    "seed": 1,
    "elevation_scale": 0.1,
    "moisture_scale": 0.1,
    "octaves": 2,
}


def test_classify_biomes_thresholds():
    # self is unused inside _classify_biomes, so we can call it unbound
    # with crafted elevation/moisture to check each threshold directly
    elevation = torch.tensor([[0.9, 0.6, 0.1, 0.6]])
    moisture = torch.tensor([[0.5, 0.8, 0.1, 0.1]])
    biome = World._classify_biomes(None, elevation, moisture)
    assert biome[0, 0].item() == MOUNTAIN  # elevation > 0.75
    assert biome[0, 1].item() == RIVER     # elevation < 0.75, moisture > 0.65
    assert biome[0, 2].item() == DESERT    # elevation < 0.4, moisture < 0.25
    assert biome[0, 3].item() == CAVE      # 0.5 < elevation <= 0.75, moisture < 0.3


def test_world_builds_expected_shapes():
    world = World(MINI_CONFIG, DEVICE)
    n = MINI_CONFIG["world_size"]
    assert world.food.shape == (n, n)
    assert world.biome.shape == (n, n)
    assert world.shelter.shape == (n, n)


def test_food_never_exceeds_cap_after_many_steps():
    world = World(MINI_CONFIG, DEVICE)
    for _ in range(50):
        world.step()
    assert torch.all(world.food <= 1.0)
    assert torch.all(world.food >= 0.0)


def test_food_regenerates_toward_cap():
    world = World(MINI_CONFIG, DEVICE)
    world.food.zero_()
    before = world.food.clone()
    world.step()
    assert torch.all(world.food >= before)  # regen should only add, never subtract
