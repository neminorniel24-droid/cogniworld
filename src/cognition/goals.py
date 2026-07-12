"""
Goal selection: a simple priority rule over each agent's emotion vector.
This is Layer 3 (executive/goal selection) without any LLM -- pure
threshold logic, batched as a tensor operation.
"""
import torch
from emotion.state import FEAR, HUNGER, CURIOSITY, CONTENTMENT

SEEK_FOOD, FLEE, EXPLORE, REST = 0, 1, 2, 3
GOAL_NAMES = ["seeking food", "fleeing danger", "exploring", "resting"]


def select_goals(emotion_values: torch.Tensor) -> torch.Tensor:
    """emotion_values: [N, 4] -> returns goal id per agent [N]"""
    fear = emotion_values[:, FEAR]
    hunger = emotion_values[:, HUNGER]
    curiosity = emotion_values[:, CURIOSITY]
    contentment = emotion_values[:, CONTENTMENT]

    goals = torch.full((emotion_values.shape[0],), EXPLORE, dtype=torch.int64,
                        device=emotion_values.device)

    goals[contentment > 0.75] = REST
    goals[hunger > 0.5] = SEEK_FOOD
    goals[fear > 0.5] = FLEE  # fear overrides hunger -- survival first

    return goals
