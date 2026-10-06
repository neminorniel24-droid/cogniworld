import torch
from world.biome import World
from world_rules import registry as wr
from agent_rules import registry as ar

def make_world():
    return World({"world_size":8,"seed":42,"elevation_scale":0.05,"moisture_scale":0.08,"octaves":2},torch.device("cpu"))

def test_world_batch_registered():
    names={getattr(r,"__name__","") for r in wr.RULES}
    assert sum(n.startswith("logic_") and 2002<=int(n.split("_")[1])<=3001 for n in names)==1000

def test_agent_batch_registered():
    names={getattr(r,"__name__","") for r in ar.RULES}
    assert sum(n.startswith("logic_") and 3002<=int(n.split("_")[1])<=4001 for n in names)==1000

def test_world_rule_is_causal_and_bounded():
    w=make_world(); before=w.surface_water.clone(); w.rain.fill_(1.0)
    from world_rules.logic_2002_4001 import logic_2002
    logic_2002(w)
    assert torch.isfinite(w.surface_water).all()
    assert (w.surface_water>=before).all()
    assert (w.surface_water<=1).all()
