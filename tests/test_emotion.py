import torch

from emotion.state import EmotionState, FEAR, HUNGER, CURIOSITY, CONTENTMENT

DEVICE = torch.device("cpu")


class FakeAgents:
    def __init__(self, energy):
        self.energy = torch.tensor(energy)

    def shelter_here(self, world):
        return torch.zeros_like(self.energy)


def test_hunger_is_inverse_of_energy_fraction():
    emotions = EmotionState(n_agents=2, device=DEVICE)
    agents = FakeAgents([200.0, 0.0])
    ate = torch.tensor([False, False])
    emotions.update(agents, world=None, ate_food=ate)
    assert abs(emotions.values[0, HUNGER].item() - 0.0) < 1e-6
    assert abs(emotions.values[1, HUNGER].item() - 1.0) < 1e-6


def test_fear_rises_only_near_zero_energy():
    emotions = EmotionState(n_agents=2, device=DEVICE)
    agents = FakeAgents([200.0, 5.0])  # 5/200 = 0.025 energy fraction
    ate = torch.tensor([False, False])
    emotions.update(agents, world=None, ate_food=ate)
    assert emotions.values[0, FEAR].item() == 0.0  # full energy -> no fear
    assert emotions.values[1, FEAR].item() > 0.5   # near-death -> high fear


def test_eating_dampens_curiosity():
    emotions = EmotionState(n_agents=1, device=DEVICE)
    emotions.values[0, CURIOSITY] = 1.0
    agents = FakeAgents([100.0])
    ate = torch.tensor([True])
    emotions.update(agents, world=None, ate_food=ate)
    assert emotions.values[0, CURIOSITY].item() < 0.35  # damped by *0.3 (plus drift)


def test_values_stay_within_unit_range():
    emotions = EmotionState(n_agents=3, device=DEVICE)
    agents = FakeAgents([1000.0, -50.0, 100.0])  # deliberately out-of-range energy
    ate = torch.tensor([False, True, False])
    emotions.update(agents, world=None, ate_food=ate)
    assert torch.all(emotions.values >= 0.0)
    assert torch.all(emotions.values <= 1.0)


def test_dominant_returns_correct_emotion_name():
    emotions = EmotionState(n_agents=1, device=DEVICE)
    emotions.values[0] = torch.tensor([0.1, 0.2, 0.9, 0.3])  # curiosity is max
    assert emotions.dominant(0) == "curiosity"
