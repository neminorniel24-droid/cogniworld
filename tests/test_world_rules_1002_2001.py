import torch
from world.biome import World
from world_rules.logic_1002_2001 import logic_1002
from world_rules.registry import RULES

def _world():
    return World({
        "world_size": 8, "seed": 42,
        "elevation_scale": 0.05, "moisture_scale": 0.08, "octaves": 2,
    }, torch.device("cpu"))

def test_batch_rules_are_registered():
    names = {getattr(rule, "__name__", "") for rule in RULES}
    batch = [n for n in names if n.startswith("logic_") and 1002 <= int(n.split("_")[1]) <= 2001]
    assert len(batch) == 1000

def test_logic_1002_is_bounded_and_causal():
    w = _world()
    before = w.surface_water.clone()
    w.rain.fill_(1.0)
    logic_1002(w)
    assert torch.isfinite(w.surface_water).all()
    assert (w.surface_water >= 0).all()
    assert (w.surface_water <= 1).all()
    assert torch.all(w.surface_water >= before)
