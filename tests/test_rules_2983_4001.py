import torch
from world.biome import World
from world_rules import registry as wr
from agent_rules import registry as ar

def _world():
    return World({"world_size":8,"seed":42,"elevation_scale":0.05,
                  "moisture_scale":0.08,"octaves":2}, torch.device("cpu"))

def test_world_batch_registered():
    names={getattr(r,"__name__","") for r in wr.RULES}
    assert sum(n.startswith("logic_") and 2983<=int(n.split("_")[1])<=3001 for n in names)==19

def test_agent_batch_registered():
    names={getattr(r,"__name__","") for r in ar.RULES}
    assert sum(n.startswith("logic_") and 3002<=int(n.split("_")[1])<=4001 for n in names)==1000

def test_world_rule_bounded():
    w=_world()
    w.rain.fill_(1.0)
    from world_rules.logic_2983_4001 import logic_2983
    logic_2983(w)
    assert torch.isfinite(w.surface_water).all()
    assert ((w.surface_water>=0)&(w.surface_water<=1)).all()

def test_agent_rule_bounded():
    w=_world()
    n=4
    # Use the project's actual agent constructor through a minimal import path.
    from genome.agents import Agents
    a=Agents(n, w, torch.device("cpu"))
    a.pos[:,0]=0; a.pos[:,1]=0
    from agent_rules.logic_2983_4001 import logic_3002
    logic_3002(a,w)
    assert torch.isfinite(a.hydration).all()
