import torch

from cognition.goals import select_goals, SEEK_FOOD, FLEE, EXPLORE, REST
from emotion.state import FEAR, HUNGER, CURIOSITY, CONTENTMENT


def make_emotions(fear=0.0, hunger=0.0, curiosity=0.0, contentment=0.0):
    v = torch.zeros(1, 4)
    v[0, FEAR] = fear
    v[0, HUNGER] = hunger
    v[0, CURIOSITY] = curiosity
    v[0, CONTENTMENT] = contentment
    return v


def test_default_goal_is_explore():
    goals = select_goals(make_emotions())
    assert goals[0].item() == EXPLORE


def test_high_contentment_selects_rest():
    goals = select_goals(make_emotions(contentment=0.9))
    assert goals[0].item() == REST


def test_high_hunger_selects_seek_food():
    goals = select_goals(make_emotions(hunger=0.8))
    assert goals[0].item() == SEEK_FOOD


def test_fear_overrides_hunger():
    # both hunger and fear are high -- fear must win (survival first)
    goals = select_goals(make_emotions(hunger=0.9, fear=0.9))
    assert goals[0].item() == FLEE


def test_fear_overrides_contentment_too():
    goals = select_goals(make_emotions(contentment=0.9, fear=0.6))
    assert goals[0].item() == FLEE


def test_batched_goal_selection_independent_per_agent():
    v = torch.zeros(3, 4)
    v[0, CONTENTMENT] = 0.9   # -> REST
    v[1, HUNGER] = 0.9        # -> SEEK_FOOD
    v[2, FEAR] = 0.9          # -> FLEE
    goals = select_goals(v)
    assert goals.tolist() == [REST, SEEK_FOOD, FLEE]
