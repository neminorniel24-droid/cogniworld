import torch
from genome.agents import Agents
from game_theory.ledger import GameTheoryLedger

def _event():
    a=Agents(2,4,100,torch.device("cpu"))
    l=GameTheoryLedger()
    l.record(a,7)
    return l.events[0]

def test_strategy_action_in_ledger():
    assert "strategy_action" in _event()
