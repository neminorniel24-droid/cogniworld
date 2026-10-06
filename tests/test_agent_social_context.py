import torch
from genome.agents import Agents

def test_social_context_measures_density_and_gaps():
    a=Agents(3,4,100,torch.device("cpu"))
    a.pos[:] = torch.tensor([[1,1],[1,1],[2,2]])
    a.energy[:] = torch.tensor([100.,150.,50.])
    a.health[:] = torch.tensor([1.,2.,0.5])
    a.update_social_context(None)
    assert torch.allclose(a.local_density, torch.tensor([1.,1.,0.]))
    assert a.neighbor_energy_gap[0] > 0
    assert a.neighbor_health_gap[0] > 0
    assert a.resource_competition[0] > 0
