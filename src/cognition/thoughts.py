"""
Turns an agent's numeric state into a short readable "thought" sentence.
No LLM -- just templated text keyed on goal + dominant emotion + biome,
with light randomization so agents don't feel robotic.
"""
import random
from cognition.goals import SEEK_FOOD, FLEE, EXPLORE, REST

TEMPLATES = {
    SEEK_FOOD: [
        "getting hungry, looking for food",
        "scanning nearby tiles for something to eat",
        "energy is dropping, need to eat soon",
    ],
    FLEE: [
        "energy critically low, feels dangerous here",
        "seeking safety, this spot feels risky",
        "on edge, needs to find shelter",
    ],
    EXPLORE: [
        "wandering, nothing urgent right now",
        "curious about what's over there",
        "taking stock of the surroundings",
    ],
    REST: [
        "feeling good, settling in for a while",
        "content here, no need to move",
        "well-fed and relaxed",
    ],
}

BIOME_FLAVOR = {
    0: "in the open plains",
    1: "by the river",
    2: "up in the mountains",
    3: "out in the desert",
    4: "deep in a cave",
}


def generate_thought(goal_id: int, biome_id: int) -> str:
    base = random.choice(TEMPLATES[goal_id])
    flavor = BIOME_FLAVOR.get(biome_id, "")
    return f"{base}, {flavor}" if flavor else base
