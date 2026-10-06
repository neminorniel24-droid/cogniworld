import torch
from genome.agents import Agents

def _check(logic, source, target, sign=1):
    a=Agents(2,4,100,torch.device("cpu"))
    getattr(a,source).fill_(1.0)
    if sign < 0 and target != "payoff":
        getattr(a,target).fill_(1.0)
    before=getattr(a,target).clone()
    logic(a,None)
    assert torch.any(getattr(a,target) != before)
def test_logic_622():
    from agent_rules.rules import logic_622
    _check(logic_622, 'health', 'risk_score', 1)
def test_logic_623():
    from agent_rules.rules import logic_623
    _check(logic_623, 'hydration', 'safety_score', 1)
def test_logic_624():
    from agent_rules.rules import logic_624
    _check(logic_624, 'thirst', 'survival_score', -1)
