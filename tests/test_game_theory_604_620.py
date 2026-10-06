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
def test_payoff_in_ledger():
    assert "payoff" in _event()
def test_trust_in_ledger():
    assert "trust" in _event()
def test_reputation_in_ledger():
    assert "reputation" in _event()
def test_cooperation_in_ledger():
    assert "cooperation" in _event()
def test_defection_in_ledger():
    assert "defection" in _event()
def test_attack_success_in_ledger():
    assert "attack_success" in _event()
def test_defense_score_in_ledger():
    assert "defense_score" in _event()
def test_resource_scarcity_in_ledger():
    assert "resource_scarcity" in _event()
def test_resource_abundance_in_ledger():
    assert "resource_abundance" in _event()
def test_habitat_stress_in_ledger():
    assert "habitat_stress" in _event()
def test_last_interaction_in_ledger():
    assert "last_interaction" in _event()
