"""
Holds per-agent physical state (position, energy, alive flag) as tensors,
and computes sensor readings from the world for the brain to consume.

Sensor layout (8 values):
  0: local food level
  1: local shelter value
  2: own energy (normalized)
  3-6: food level in N/S/E/W neighbor tile
  7: bias (constant 1.0)
"""
import torch

MOVES = torch.tensor([
    [0, -1],  # N
    [0, 1],   # S
    [1, 0],   # E
    [-1, 0],  # W
], dtype=torch.int64)


class Agents:
    def __init__(self, n_agents: int, world_size: int, start_energy: float, device: torch.device):
        self.n = n_agents
        self.world_size = world_size
        self.device = device

        self.pos = torch.randint(0, world_size, (n_agents, 2), device=device)
        self.energy = torch.full((n_agents,), start_energy, device=device)
        # Resource-state signals used by the agent causal-rule layer.
        self.energy_surplus = torch.zeros(n_agents, dtype=torch.float32, device=device)
        self.resource_scarcity = torch.zeros(n_agents, dtype=torch.float32, device=device)
        self.resource_abundance = torch.zeros(n_agents, dtype=torch.float32, device=device)
        self.alive = torch.ones(n_agents, dtype=torch.bool, device=device)
        # scarcity tracking: consecutive ticks since this agent last ate.
        # feeds migration pressure (see migration/pressure.py) -- an agent
        # stuck too long without food gets a movement discount to encourage
        # traveling further to find a better biome instead of starving in place.
        self.ticks_since_food = torch.zeros(n_agents, dtype=torch.int64, device=device)
        # disease state (see disease/sir.py): 0=susceptible, 1=infected, 2=recovered
        self.infection = torch.zeros(n_agents, dtype=torch.int64, device=device)
        self.infection_timer = torch.zeros(n_agents, dtype=torch.int64, device=device)  # ticks infected

        # Agent-environment and game-theory state.
        self.hydration = torch.ones(n_agents, device=device) if 'hydration' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.thirst = torch.ones(n_agents, device=device) if 'thirst' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.hunger = torch.ones(n_agents, device=device) if 'hunger' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.health = torch.ones(n_agents, device=device) if 'health' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.thermal_stress = torch.ones(n_agents, device=device) if 'thermal_stress' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.dehydration = torch.ones(n_agents, device=device) if 'dehydration' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.pathogen_risk = torch.ones(n_agents, device=device) if 'pathogen_risk' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.infection_risk = torch.ones(n_agents, device=device) if 'infection_risk' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.alertness = torch.ones(n_agents, device=device) if 'alertness' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.fear = torch.ones(n_agents, device=device) if 'fear' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.recovery = torch.ones(n_agents, device=device) if 'recovery' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.metabolic_cost = torch.ones(n_agents, device=device) if 'metabolic_cost' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.reproduction_drive = torch.ones(n_agents, device=device) if 'reproduction_drive' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.migration_drive = torch.ones(n_agents, device=device) if 'migration_drive' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.exploration_drive = torch.ones(n_agents, device=device) if 'exploration_drive' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.food_access = torch.ones(n_agents, device=device) if 'food_access' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.wealth = torch.ones(n_agents, device=device) if 'wealth' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.stability = torch.ones(n_agents, device=device) if 'stability' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.habitat_stress = torch.ones(n_agents, device=device) if 'habitat_stress' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.social_tolerance = torch.ones(n_agents, device=device) if 'social_tolerance' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.reputation = torch.ones(n_agents, device=device) if 'reputation' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.trust = torch.ones(n_agents, device=device) if 'trust' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.cooperation = torch.ones(n_agents, device=device) if 'cooperation' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.defection = torch.ones(n_agents, device=device) if 'defection' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.aggression = torch.ones(n_agents, device=device) if 'aggression' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.conflict_pressure = torch.ones(n_agents, device=device) if 'conflict_pressure' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.competition_pressure = torch.ones(n_agents, device=device) if 'competition_pressure' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.territoriality = torch.ones(n_agents, device=device) if 'territoriality' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.group_stability = torch.ones(n_agents, device=device) if 'group_stability' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.sharing_capacity = torch.ones(n_agents, device=device) if 'sharing_capacity' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.help_drive = torch.ones(n_agents, device=device) if 'help_drive' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.social_avoidance = torch.ones(n_agents, device=device) if 'social_avoidance' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.selfishness = torch.ones(n_agents, device=device) if 'selfishness' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.generosity = torch.ones(n_agents, device=device) if 'generosity' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.gratitude = torch.ones(n_agents, device=device) if 'gratitude' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.caution = torch.ones(n_agents, device=device) if 'caution' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.confidence = torch.ones(n_agents, device=device) if 'confidence' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.strategy_confidence = torch.ones(n_agents, device=device) if 'strategy_confidence' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.future_help = torch.ones(n_agents, device=device) if 'future_help' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.resource_discovery = torch.ones(n_agents, device=device) if 'resource_discovery' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.empathy = torch.ones(n_agents, device=device) if 'empathy' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.attack_threshold = torch.ones(n_agents, device=device) if 'attack_threshold' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.defection_threshold = torch.ones(n_agents, device=device) if 'defection_threshold' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.oxygen_need = torch.ones(n_agents, device=device) if 'oxygen_need' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.shelter_need = torch.ones(n_agents, device=device) if 'shelter_need' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.fire_fear = torch.ones(n_agents, device=device) if 'fire_fear' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.resource_competition = torch.ones(n_agents, device=device) if 'resource_competition' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.vegetation_expectation = torch.ones(n_agents, device=device) if 'vegetation_expectation' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.stress = torch.ones(n_agents, device=device) if 'stress' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.social_need = torch.ones(n_agents, device=device) if 'social_need' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.neighbor_energy_gap = torch.ones(n_agents, device=device) if 'neighbor_energy_gap' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.neighbor_health_gap = torch.ones(n_agents, device=device) if 'neighbor_health_gap' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.betrayal_memory = torch.ones(n_agents, device=device) if 'betrayal_memory' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.conflict_history = torch.ones(n_agents, device=device) if 'conflict_history' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.cooperation_history = torch.ones(n_agents, device=device) if 'cooperation_history' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.help_received = torch.ones(n_agents, device=device) if 'help_received' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.help_given = torch.ones(n_agents, device=device) if 'help_given' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.local_density = torch.ones(n_agents, device=device) if 'local_density' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.last_reward = torch.ones(n_agents, device=device) if 'last_reward' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.last_energy_delta = torch.ones(n_agents, device=device) if 'last_energy_delta' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.last_food = torch.ones(n_agents, device=device) if 'last_food' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.last_interaction = torch.ones(n_agents, device=device) if 'last_interaction' in ('hydration','health','stability','social_tolerance','attack_threshold','defection_threshold') else torch.zeros(n_agents, device=device)
        self.risk_tolerance = torch.full((n_agents,),0.5,device=device)
        self.last_action = torch.zeros(n_agents,dtype=torch.int64,device=device)
        self.strategy_score=torch.zeros(n_agents,device=device)
        self.cooperation_score=torch.zeros(n_agents,device=device)
        self.competition_score=torch.zeros(n_agents,device=device)
        self.defection_score=torch.zeros(n_agents,device=device)
        self.reciprocity_score=torch.zeros(n_agents,device=device)
        self.risk_score=torch.zeros(n_agents,device=device)
        self.safety_score=torch.zeros(n_agents,device=device)
        self.exploration_score=torch.zeros(n_agents,device=device)
        self.foraging_score=torch.zeros(n_agents,device=device)
        self.survival_score=torch.zeros(n_agents,device=device)
        self.fitness_score=torch.zeros(n_agents,device=device)
        self.help_score=torch.zeros(n_agents,device=device)
        self.attack_success=torch.zeros(n_agents,device=device)
        self.retaliation_risk=torch.zeros(n_agents,device=device)
        self.defense_score=torch.zeros(n_agents,device=device)
        self.migration_score=torch.zeros(n_agents,device=device)
        self.reproduction_score=torch.zeros(n_agents,device=device)
        self.sharing_score=torch.zeros(n_agents,device=device)
        self.strategy_persistence=torch.zeros(n_agents,device=device)
        self.strategy_mixing=torch.zeros(n_agents,device=device)
        self.learning_rate=torch.zeros(n_agents,device=device)
        self.memory_update=torch.zeros(n_agents,device=device)
        self.future_payoff_weight=torch.zeros(n_agents,device=device)
        self.self_preservation=torch.zeros(n_agents,device=device)
        self.payoff=torch.zeros(n_agents,device=device)
        self.moves = MOVES.to(device)

    def shelter_here(self, world) -> torch.Tensor:
        x, y = self.pos[:, 0], self.pos[:, 1]
        return world.shelter[y, x]

    def sense(self, world) -> torch.Tensor:
        x, y = self.pos[:, 0], self.pos[:, 1]
        food_here = world.food[y, x]
        shelter_here = world.shelter[y, x]
        energy_norm = (self.energy / 200.0).clamp(0, 1)

        neighbor_food = []
        for dx, dy in self.moves.tolist():
            nx = (x + dx).clamp(0, self.world_size - 1)
            ny = (y + dy).clamp(0, self.world_size - 1)
            neighbor_food.append(world.food[ny, nx])
        neighbor_food = torch.stack(neighbor_food, dim=1)  # [N, 4]

        bias = torch.ones(self.n, device=self.device)

        sensors = torch.cat([
            food_here.unsqueeze(1),
            shelter_here.unsqueeze(1),
            energy_norm.unsqueeze(1),
            neighbor_food,
            bias.unsqueeze(1),
        ], dim=1)
        return sensors

    def act(self, action_logits: torch.Tensor, world, move_cost: float, metabolism_cost: float, max_energy: float = 200.0,
             food_energy_value: float = 40.0):
        """Move each alive agent toward its argmax action, consume energy, eat food."""
        # Brain outputs movement logits first. Strategy logits are optional
        # for backward compatibility with the original 4-action callers.
        move_action = torch.argmax(action_logits[:, :4], dim=1)

        if action_logits.shape[1] >= 8:
            # logits 4:8 -> strategy (share/attack/defend/wait)
            strategy_action = torch.argmax(action_logits[:, 4:8], dim=1)
        else:
            # Legacy 4-action brains have no strategy head: wait.
            strategy_action = torch.zeros_like(move_action)

        self.last_action = move_action.clone()
        delta = self.moves[move_action]  # [N, 2]

        new_pos = self.pos + delta
        new_pos[:, 0] = new_pos[:, 0].clamp(0, self.world_size - 1)
        new_pos[:, 1] = new_pos[:, 1].clamp(0, self.world_size - 1)
        self.pos = torch.where(self.alive.unsqueeze(1), new_pos, self.pos)

        # eat: consume food at new tile, gain energy
        x, y = self.pos[:, 0], self.pos[:, 1]
        eaten = world.food[y, x].clone()
        world.food[y, x] -= eaten
        before_energy=self.energy.clone()
        self.energy += eaten * food_energy_value  # food -> energy conversion

        # Strategic actions: 0=share, 1=attack, 2=defend, 3=wait.
        self.last_strategy_action = strategy_action.clone()
        self.last_interaction = (strategy_action != 3).float()
        self.help_given += (strategy_action == 0).float() * 0.01
        self.aggression += (strategy_action == 1).float() * 0.01
        self.defense_score += (strategy_action == 2).float() * 0.01

        # costs
        self.energy -= (move_cost + metabolism_cost)
        self.energy = self.energy.clamp(min=0, max=max_energy)
        self.last_food=eaten.clone(); self.last_energy_delta=self.energy-before_energy; self.last_reward=self.last_energy_delta

        # death
        self.alive &= self.energy > 0

        ate = eaten > 0.01
        self.ticks_since_food = torch.where(
            ate, torch.zeros_like(self.ticks_since_food), self.ticks_since_food + 1
        )

        return ate
