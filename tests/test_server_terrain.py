import torch

import server
from world.biome import World

MINI = {"world_size": 8, "seed": 3, "elevation_scale": 0.1, "moisture_scale": 0.1, "octaves": 2}


def test_terrain_payload_shape_and_ranges():
    world = World(MINI, torch.device("cpu"))
    t = server.terrain_payload(world)
    assert t["size"] == 8
    assert len(t["elevation"]) == 8 and all(len(r) == 8 for r in t["elevation"])
    assert len(t["biome"]) == 8 and all(len(r) == 8 for r in t["biome"])
    flat_e = [v for r in t["elevation"] for v in r]
    assert all(0.0 <= v <= 1.0 for v in flat_e)
    assert {b for r in t["biome"] for b in r} <= {0, 1, 2, 3, 4}


def test_terrain_payload_is_json_serializable():
    import json
    world = World(MINI, torch.device("cpu"))
    json.dumps(server.terrain_payload(world))  # must not raise
