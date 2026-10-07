import torch

RATE = 0.008


def _world_signal(world, name):
    x = getattr(world, name, None)
    if x is None:
        return None
    return torch.nan_to_num(x).float()


def _agent_local(world, agents, name):
    x = agents.pos[:, 0].long()
    y = agents.pos[:, 1].long()
    field = getattr(world, name, None)
    if field is None:
        return None
    return torch.nan_to_num(field[y, x]).to(dtype=agents.energy.dtype)


def _norm(x):
    return torch.sigmoid(torch.nan_to_num(x))


def _world_apply(world, source, target, mode):
    s = _world_signal(world, source)
    t = _world_signal(world, target)
    if s is None or t is None:
        return
    s = _norm(s)
    if mode == "inverse": d = 1 - s
    elif mode == "square": d = s * s
    elif mode == "sqrt": d = torch.sqrt(s.clamp_min(0))
    elif mode == "pulse": d = 4 * s * (1 - s)
    elif mode == "threshold": d = (s > 0.5).float()
    elif mode == "saturation": d = s / (0.25 + s)
    elif mode == "reciprocal": d = 1 / (1 + s)
    else: d = s
    t = torch.nan_to_num(t)
    setattr(world, target, t + RATE * (d - t))


def _agent_source(world, agents, name):
    if hasattr(agents, name):
        return torch.nan_to_num(getattr(agents, name)).to(dtype=agents.energy.dtype)
    return _agent_local(world, agents, name)


def _agent_apply(world, agents, source, target, mode):
    s = _agent_source(world, agents, source)
    if s is None or not hasattr(agents, target):
        return
    s = _norm(s)
    x = torch.nan_to_num(getattr(agents, target))
    t = _norm(x)
    if mode == "inverse": d = 1 - s
    elif mode == "square": d = s * s
    elif mode == "sqrt": d = torch.sqrt(s.clamp_min(0))
    elif mode == "pulse": d = 4 * s * (1 - s)
    elif mode == "feedback": d = s * t
    elif mode == "scarcity": d = (1 - s) * _norm(getattr(agents, "hunger"))
    elif mode == "reserve": d = s * _norm(getattr(agents, "energy_surplus"))
    elif mode == "stress": d = s * _norm(getattr(agents, "stress"))
    elif mode == "recovery": d = s * _norm(getattr(agents, "health"))
    elif mode == "persistence": d = s * _norm(getattr(agents, "memory_update"))
    elif mode == "risk": d = s * _norm(getattr(agents, "risk_tolerance"))
    elif mode == "competition": d = s * _norm(getattr(agents, "competition_pressure"))
    elif mode == "social": d = s * _norm(getattr(agents, "social_need"))
    elif mode == "resource": d = s * _norm(getattr(agents, "resource_abundance"))
    elif mode == "threshold": d = (s > 0.5).to(s.dtype)
    elif mode == "saturation": d = s / (0.25 + s)
    elif mode == "gap": d = torch.abs(s - t)
    elif mode == "reciprocal": d = 1 / (1 + s)
    else: d = s
    new_signal = t + RATE * (d - t)
    setattr(agents, target, torch.logit(new_signal.clamp(1e-5, 1 - 1e-5)))

def logic_9201(agents, world):
    _agent_apply(world, agents, 'temperature', 'hydration', 'direct')

def logic_9202(agents, world):
    _agent_apply(world, agents, 'surface_water', 'hydration', 'direct')

def logic_9203(agents, world):
    _agent_apply(world, agents, 'humidity', 'hydration', 'direct')

def logic_9204(agents, world):
    _agent_apply(world, agents, 'cloud', 'hydration', 'direct')

def logic_9205(agents, world):
    _agent_apply(world, agents, 'rain', 'hydration', 'direct')

def logic_9206(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'hydration', 'direct')

def logic_9207(agents, world):
    _agent_apply(world, agents, 'runoff', 'hydration', 'direct')

def logic_9208(agents, world):
    _agent_apply(world, agents, 'wind_x', 'hydration', 'direct')

def logic_9209(agents, world):
    _agent_apply(world, agents, 'wind_y', 'hydration', 'direct')

def logic_9210(agents, world):
    _agent_apply(world, agents, 'vegetation', 'hydration', 'direct')

def logic_9211(agents, world):
    _agent_apply(world, agents, 'biomass', 'hydration', 'direct')

def logic_9212(agents, world):
    _agent_apply(world, agents, 'herbivore', 'hydration', 'direct')

def logic_9213(agents, world):
    _agent_apply(world, agents, 'predator', 'hydration', 'direct')

def logic_9214(agents, world):
    _agent_apply(world, agents, 'carrion', 'hydration', 'direct')

def logic_9215(agents, world):
    _agent_apply(world, agents, 'nutrients', 'hydration', 'direct')

def logic_9216(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'hydration', 'direct')

def logic_9217(agents, world):
    _agent_apply(world, agents, 'oxygen', 'hydration', 'direct')

def logic_9218(agents, world):
    _agent_apply(world, agents, 'co2', 'hydration', 'direct')

def logic_9219(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'hydration', 'direct')

def logic_9220(agents, world):
    _agent_apply(world, agents, 'ice', 'hydration', 'direct')

def logic_9221(agents, world):
    _agent_apply(world, agents, 'evaporation', 'hydration', 'direct')

def logic_9222(agents, world):
    _agent_apply(world, agents, 'detritus', 'hydration', 'direct')

def logic_9223(agents, world):
    _agent_apply(world, agents, 'methane', 'hydration', 'direct')

def logic_9224(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'hydration', 'direct')

def logic_9225(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'hydration', 'direct')

def logic_9226(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'hydration', 'direct')

def logic_9227(agents, world):
    _agent_apply(world, agents, 'erosion', 'hydration', 'direct')

def logic_9228(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'hydration', 'direct')

def logic_9229(agents, world):
    _agent_apply(world, agents, 'root_density', 'hydration', 'direct')

def logic_9230(agents, world):
    _agent_apply(world, agents, 'wetland', 'hydration', 'direct')

def logic_9231(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'hydration', 'direct')

def logic_9232(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'hydration', 'direct')

def logic_9233(agents, world):
    _agent_apply(world, agents, 'ash', 'hydration', 'direct')

def logic_9234(agents, world):
    _agent_apply(world, agents, 'snowpack', 'hydration', 'direct')

def logic_9235(agents, world):
    _agent_apply(world, agents, 'groundwater', 'hydration', 'direct')

def logic_9236(agents, world):
    _agent_apply(world, agents, 'sediment', 'hydration', 'direct')

def logic_9237(agents, world):
    _agent_apply(world, agents, 'salinity', 'hydration', 'direct')

def logic_9238(agents, world):
    _agent_apply(world, agents, 'algae', 'hydration', 'direct')

def logic_9239(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'hydration', 'direct')

def logic_9240(agents, world):
    _agent_apply(world, agents, 'deadwood', 'hydration', 'direct')

def logic_9241(agents, world):
    _agent_apply(world, agents, 'pollinators', 'hydration', 'direct')

def logic_9242(agents, world):
    _agent_apply(world, agents, 'flowers', 'hydration', 'direct')

def logic_9243(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'hydration', 'direct')

def logic_9244(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'hydration', 'direct')

def logic_9245(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'hydration', 'direct')

def logic_9246(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'hydration', 'direct')

def logic_9247(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'hydration', 'direct')

def logic_9248(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'hydration', 'direct')

def logic_9249(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'hydration', 'direct')

def logic_9250(agents, world):
    _agent_apply(world, agents, 'hydration', 'hydration', 'direct')

def logic_9251(agents, world):
    _agent_apply(world, agents, 'thirst', 'hydration', 'direct')

def logic_9252(agents, world):
    _agent_apply(world, agents, 'hunger', 'hydration', 'direct')

def logic_9253(agents, world):
    _agent_apply(world, agents, 'health', 'hydration', 'direct')

def logic_9254(agents, world):
    _agent_apply(world, agents, 'stress', 'hydration', 'direct')

def logic_9255(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'hydration', 'direct')

def logic_9256(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'hydration', 'direct')

def logic_9257(agents, world):
    _agent_apply(world, agents, 'social_need', 'hydration', 'direct')

def logic_9258(agents, world):
    _agent_apply(world, agents, 'cooperation', 'hydration', 'direct')

def logic_9259(agents, world):
    _agent_apply(world, agents, 'defection', 'hydration', 'direct')

def logic_9260(agents, world):
    _agent_apply(world, agents, 'trust', 'hydration', 'direct')

def logic_9261(agents, world):
    _agent_apply(world, agents, 'reputation', 'hydration', 'direct')

def logic_9262(agents, world):
    _agent_apply(world, agents, 'help_received', 'hydration', 'direct')

def logic_9263(agents, world):
    _agent_apply(world, agents, 'help_given', 'hydration', 'direct')

def logic_9264(agents, world):
    _agent_apply(world, agents, 'local_density', 'hydration', 'direct')

def logic_9265(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'hydration', 'direct')

def logic_9266(agents, world):
    _agent_apply(world, agents, 'survival_score', 'hydration', 'direct')

def logic_9267(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'hydration', 'direct')

def logic_9268(agents, world):
    _agent_apply(world, agents, 'payoff', 'hydration', 'direct')

def logic_9269(agents, world):
    _agent_apply(world, agents, 'temperature', 'thirst', 'direct')

def logic_9270(agents, world):
    _agent_apply(world, agents, 'surface_water', 'thirst', 'direct')

def logic_9271(agents, world):
    _agent_apply(world, agents, 'humidity', 'thirst', 'direct')

def logic_9272(agents, world):
    _agent_apply(world, agents, 'cloud', 'thirst', 'direct')

def logic_9273(agents, world):
    _agent_apply(world, agents, 'rain', 'thirst', 'direct')

def logic_9274(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'thirst', 'direct')

def logic_9275(agents, world):
    _agent_apply(world, agents, 'runoff', 'thirst', 'direct')

def logic_9276(agents, world):
    _agent_apply(world, agents, 'wind_x', 'thirst', 'direct')

def logic_9277(agents, world):
    _agent_apply(world, agents, 'wind_y', 'thirst', 'direct')

def logic_9278(agents, world):
    _agent_apply(world, agents, 'vegetation', 'thirst', 'direct')

def logic_9279(agents, world):
    _agent_apply(world, agents, 'biomass', 'thirst', 'direct')

def logic_9280(agents, world):
    _agent_apply(world, agents, 'herbivore', 'thirst', 'direct')

def logic_9281(agents, world):
    _agent_apply(world, agents, 'predator', 'thirst', 'direct')

def logic_9282(agents, world):
    _agent_apply(world, agents, 'carrion', 'thirst', 'direct')

def logic_9283(agents, world):
    _agent_apply(world, agents, 'nutrients', 'thirst', 'direct')

def logic_9284(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'thirst', 'direct')

def logic_9285(agents, world):
    _agent_apply(world, agents, 'oxygen', 'thirst', 'direct')

def logic_9286(agents, world):
    _agent_apply(world, agents, 'co2', 'thirst', 'direct')

def logic_9287(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'thirst', 'direct')

def logic_9288(agents, world):
    _agent_apply(world, agents, 'ice', 'thirst', 'direct')

def logic_9289(agents, world):
    _agent_apply(world, agents, 'evaporation', 'thirst', 'direct')

def logic_9290(agents, world):
    _agent_apply(world, agents, 'detritus', 'thirst', 'direct')

def logic_9291(agents, world):
    _agent_apply(world, agents, 'methane', 'thirst', 'direct')

def logic_9292(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'thirst', 'direct')

def logic_9293(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'thirst', 'direct')

def logic_9294(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'thirst', 'direct')

def logic_9295(agents, world):
    _agent_apply(world, agents, 'erosion', 'thirst', 'direct')

def logic_9296(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'thirst', 'direct')

def logic_9297(agents, world):
    _agent_apply(world, agents, 'root_density', 'thirst', 'direct')

def logic_9298(agents, world):
    _agent_apply(world, agents, 'wetland', 'thirst', 'direct')

def logic_9299(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'thirst', 'direct')

def logic_9300(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'thirst', 'direct')

def logic_9301(agents, world):
    _agent_apply(world, agents, 'ash', 'thirst', 'direct')

def logic_9302(agents, world):
    _agent_apply(world, agents, 'snowpack', 'thirst', 'direct')

def logic_9303(agents, world):
    _agent_apply(world, agents, 'groundwater', 'thirst', 'direct')

def logic_9304(agents, world):
    _agent_apply(world, agents, 'sediment', 'thirst', 'direct')

def logic_9305(agents, world):
    _agent_apply(world, agents, 'salinity', 'thirst', 'direct')

def logic_9306(agents, world):
    _agent_apply(world, agents, 'algae', 'thirst', 'direct')

def logic_9307(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'thirst', 'direct')

def logic_9308(agents, world):
    _agent_apply(world, agents, 'deadwood', 'thirst', 'direct')

def logic_9309(agents, world):
    _agent_apply(world, agents, 'pollinators', 'thirst', 'direct')

def logic_9310(agents, world):
    _agent_apply(world, agents, 'flowers', 'thirst', 'direct')

def logic_9311(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'thirst', 'direct')

def logic_9312(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'thirst', 'direct')

def logic_9313(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'thirst', 'direct')

def logic_9314(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'thirst', 'direct')

def logic_9315(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'thirst', 'direct')

def logic_9316(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'thirst', 'direct')

def logic_9317(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'thirst', 'direct')

def logic_9318(agents, world):
    _agent_apply(world, agents, 'hydration', 'thirst', 'direct')

def logic_9319(agents, world):
    _agent_apply(world, agents, 'thirst', 'thirst', 'direct')

def logic_9320(agents, world):
    _agent_apply(world, agents, 'hunger', 'thirst', 'direct')

def logic_9321(agents, world):
    _agent_apply(world, agents, 'health', 'thirst', 'direct')

def logic_9322(agents, world):
    _agent_apply(world, agents, 'stress', 'thirst', 'direct')

def logic_9323(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'thirst', 'direct')

def logic_9324(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'thirst', 'direct')

def logic_9325(agents, world):
    _agent_apply(world, agents, 'social_need', 'thirst', 'direct')

def logic_9326(agents, world):
    _agent_apply(world, agents, 'cooperation', 'thirst', 'direct')

def logic_9327(agents, world):
    _agent_apply(world, agents, 'defection', 'thirst', 'direct')

def logic_9328(agents, world):
    _agent_apply(world, agents, 'trust', 'thirst', 'direct')

def logic_9329(agents, world):
    _agent_apply(world, agents, 'reputation', 'thirst', 'direct')

def logic_9330(agents, world):
    _agent_apply(world, agents, 'help_received', 'thirst', 'direct')

def logic_9331(agents, world):
    _agent_apply(world, agents, 'help_given', 'thirst', 'direct')

def logic_9332(agents, world):
    _agent_apply(world, agents, 'local_density', 'thirst', 'direct')

def logic_9333(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'thirst', 'direct')

def logic_9334(agents, world):
    _agent_apply(world, agents, 'survival_score', 'thirst', 'direct')

def logic_9335(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'thirst', 'direct')

def logic_9336(agents, world):
    _agent_apply(world, agents, 'payoff', 'thirst', 'direct')

def logic_9337(agents, world):
    _agent_apply(world, agents, 'temperature', 'hunger', 'direct')

def logic_9338(agents, world):
    _agent_apply(world, agents, 'surface_water', 'hunger', 'direct')

def logic_9339(agents, world):
    _agent_apply(world, agents, 'humidity', 'hunger', 'direct')

def logic_9340(agents, world):
    _agent_apply(world, agents, 'cloud', 'hunger', 'direct')

def logic_9341(agents, world):
    _agent_apply(world, agents, 'rain', 'hunger', 'direct')

def logic_9342(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'hunger', 'direct')

def logic_9343(agents, world):
    _agent_apply(world, agents, 'runoff', 'hunger', 'direct')

def logic_9344(agents, world):
    _agent_apply(world, agents, 'wind_x', 'hunger', 'direct')

def logic_9345(agents, world):
    _agent_apply(world, agents, 'wind_y', 'hunger', 'direct')

def logic_9346(agents, world):
    _agent_apply(world, agents, 'vegetation', 'hunger', 'direct')

def logic_9347(agents, world):
    _agent_apply(world, agents, 'biomass', 'hunger', 'direct')

def logic_9348(agents, world):
    _agent_apply(world, agents, 'herbivore', 'hunger', 'direct')

def logic_9349(agents, world):
    _agent_apply(world, agents, 'predator', 'hunger', 'direct')

def logic_9350(agents, world):
    _agent_apply(world, agents, 'carrion', 'hunger', 'direct')

def logic_9351(agents, world):
    _agent_apply(world, agents, 'nutrients', 'hunger', 'direct')

def logic_9352(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'hunger', 'direct')

def logic_9353(agents, world):
    _agent_apply(world, agents, 'oxygen', 'hunger', 'direct')

def logic_9354(agents, world):
    _agent_apply(world, agents, 'co2', 'hunger', 'direct')

def logic_9355(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'hunger', 'direct')

def logic_9356(agents, world):
    _agent_apply(world, agents, 'ice', 'hunger', 'direct')

def logic_9357(agents, world):
    _agent_apply(world, agents, 'evaporation', 'hunger', 'direct')

def logic_9358(agents, world):
    _agent_apply(world, agents, 'detritus', 'hunger', 'direct')

def logic_9359(agents, world):
    _agent_apply(world, agents, 'methane', 'hunger', 'direct')

def logic_9360(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'hunger', 'direct')

def logic_9361(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'hunger', 'direct')

def logic_9362(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'hunger', 'direct')

def logic_9363(agents, world):
    _agent_apply(world, agents, 'erosion', 'hunger', 'direct')

def logic_9364(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'hunger', 'direct')

def logic_9365(agents, world):
    _agent_apply(world, agents, 'root_density', 'hunger', 'direct')

def logic_9366(agents, world):
    _agent_apply(world, agents, 'wetland', 'hunger', 'direct')

def logic_9367(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'hunger', 'direct')

def logic_9368(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'hunger', 'direct')

def logic_9369(agents, world):
    _agent_apply(world, agents, 'ash', 'hunger', 'direct')

def logic_9370(agents, world):
    _agent_apply(world, agents, 'snowpack', 'hunger', 'direct')

def logic_9371(agents, world):
    _agent_apply(world, agents, 'groundwater', 'hunger', 'direct')

def logic_9372(agents, world):
    _agent_apply(world, agents, 'sediment', 'hunger', 'direct')

def logic_9373(agents, world):
    _agent_apply(world, agents, 'salinity', 'hunger', 'direct')

def logic_9374(agents, world):
    _agent_apply(world, agents, 'algae', 'hunger', 'direct')

def logic_9375(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'hunger', 'direct')

def logic_9376(agents, world):
    _agent_apply(world, agents, 'deadwood', 'hunger', 'direct')

def logic_9377(agents, world):
    _agent_apply(world, agents, 'pollinators', 'hunger', 'direct')

def logic_9378(agents, world):
    _agent_apply(world, agents, 'flowers', 'hunger', 'direct')

def logic_9379(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'hunger', 'direct')

def logic_9380(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'hunger', 'direct')

def logic_9381(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'hunger', 'direct')

def logic_9382(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'hunger', 'direct')

def logic_9383(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'hunger', 'direct')

def logic_9384(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'hunger', 'direct')

def logic_9385(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'hunger', 'direct')

def logic_9386(agents, world):
    _agent_apply(world, agents, 'hydration', 'hunger', 'direct')

def logic_9387(agents, world):
    _agent_apply(world, agents, 'thirst', 'hunger', 'direct')

def logic_9388(agents, world):
    _agent_apply(world, agents, 'hunger', 'hunger', 'direct')

def logic_9389(agents, world):
    _agent_apply(world, agents, 'health', 'hunger', 'direct')

def logic_9390(agents, world):
    _agent_apply(world, agents, 'stress', 'hunger', 'direct')

def logic_9391(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'hunger', 'direct')

def logic_9392(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'hunger', 'direct')

def logic_9393(agents, world):
    _agent_apply(world, agents, 'social_need', 'hunger', 'direct')

def logic_9394(agents, world):
    _agent_apply(world, agents, 'cooperation', 'hunger', 'direct')

def logic_9395(agents, world):
    _agent_apply(world, agents, 'defection', 'hunger', 'direct')

def logic_9396(agents, world):
    _agent_apply(world, agents, 'trust', 'hunger', 'direct')

def logic_9397(agents, world):
    _agent_apply(world, agents, 'reputation', 'hunger', 'direct')

def logic_9398(agents, world):
    _agent_apply(world, agents, 'help_received', 'hunger', 'direct')

def logic_9399(agents, world):
    _agent_apply(world, agents, 'help_given', 'hunger', 'direct')

def logic_9400(agents, world):
    _agent_apply(world, agents, 'local_density', 'hunger', 'direct')

def logic_9401(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'hunger', 'direct')

def logic_9402(agents, world):
    _agent_apply(world, agents, 'survival_score', 'hunger', 'direct')

def logic_9403(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'hunger', 'direct')

def logic_9404(agents, world):
    _agent_apply(world, agents, 'payoff', 'hunger', 'direct')

def logic_9405(agents, world):
    _agent_apply(world, agents, 'temperature', 'health', 'direct')

def logic_9406(agents, world):
    _agent_apply(world, agents, 'surface_water', 'health', 'direct')

def logic_9407(agents, world):
    _agent_apply(world, agents, 'humidity', 'health', 'direct')

def logic_9408(agents, world):
    _agent_apply(world, agents, 'cloud', 'health', 'direct')

def logic_9409(agents, world):
    _agent_apply(world, agents, 'rain', 'health', 'direct')

def logic_9410(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'health', 'direct')

def logic_9411(agents, world):
    _agent_apply(world, agents, 'runoff', 'health', 'direct')

def logic_9412(agents, world):
    _agent_apply(world, agents, 'wind_x', 'health', 'direct')

def logic_9413(agents, world):
    _agent_apply(world, agents, 'wind_y', 'health', 'direct')

def logic_9414(agents, world):
    _agent_apply(world, agents, 'vegetation', 'health', 'direct')

def logic_9415(agents, world):
    _agent_apply(world, agents, 'biomass', 'health', 'direct')

def logic_9416(agents, world):
    _agent_apply(world, agents, 'herbivore', 'health', 'direct')

def logic_9417(agents, world):
    _agent_apply(world, agents, 'predator', 'health', 'direct')

def logic_9418(agents, world):
    _agent_apply(world, agents, 'carrion', 'health', 'direct')

def logic_9419(agents, world):
    _agent_apply(world, agents, 'nutrients', 'health', 'direct')

def logic_9420(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'health', 'direct')

def logic_9421(agents, world):
    _agent_apply(world, agents, 'oxygen', 'health', 'direct')

def logic_9422(agents, world):
    _agent_apply(world, agents, 'co2', 'health', 'direct')

def logic_9423(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'health', 'direct')

def logic_9424(agents, world):
    _agent_apply(world, agents, 'ice', 'health', 'direct')

def logic_9425(agents, world):
    _agent_apply(world, agents, 'evaporation', 'health', 'direct')

def logic_9426(agents, world):
    _agent_apply(world, agents, 'detritus', 'health', 'direct')

def logic_9427(agents, world):
    _agent_apply(world, agents, 'methane', 'health', 'direct')

def logic_9428(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'health', 'direct')

def logic_9429(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'health', 'direct')

def logic_9430(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'health', 'direct')

def logic_9431(agents, world):
    _agent_apply(world, agents, 'erosion', 'health', 'direct')

def logic_9432(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'health', 'direct')

def logic_9433(agents, world):
    _agent_apply(world, agents, 'root_density', 'health', 'direct')

def logic_9434(agents, world):
    _agent_apply(world, agents, 'wetland', 'health', 'direct')

def logic_9435(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'health', 'direct')

def logic_9436(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'health', 'direct')

def logic_9437(agents, world):
    _agent_apply(world, agents, 'ash', 'health', 'direct')

def logic_9438(agents, world):
    _agent_apply(world, agents, 'snowpack', 'health', 'direct')

def logic_9439(agents, world):
    _agent_apply(world, agents, 'groundwater', 'health', 'direct')

def logic_9440(agents, world):
    _agent_apply(world, agents, 'sediment', 'health', 'direct')

def logic_9441(agents, world):
    _agent_apply(world, agents, 'salinity', 'health', 'direct')

def logic_9442(agents, world):
    _agent_apply(world, agents, 'algae', 'health', 'direct')

def logic_9443(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'health', 'direct')

def logic_9444(agents, world):
    _agent_apply(world, agents, 'deadwood', 'health', 'direct')

def logic_9445(agents, world):
    _agent_apply(world, agents, 'pollinators', 'health', 'direct')

def logic_9446(agents, world):
    _agent_apply(world, agents, 'flowers', 'health', 'direct')

def logic_9447(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'health', 'direct')

def logic_9448(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'health', 'direct')

def logic_9449(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'health', 'direct')

def logic_9450(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'health', 'direct')

def logic_9451(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'health', 'direct')

def logic_9452(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'health', 'direct')

def logic_9453(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'health', 'direct')

def logic_9454(agents, world):
    _agent_apply(world, agents, 'hydration', 'health', 'direct')

def logic_9455(agents, world):
    _agent_apply(world, agents, 'thirst', 'health', 'direct')

def logic_9456(agents, world):
    _agent_apply(world, agents, 'hunger', 'health', 'direct')

def logic_9457(agents, world):
    _agent_apply(world, agents, 'health', 'health', 'direct')

def logic_9458(agents, world):
    _agent_apply(world, agents, 'stress', 'health', 'direct')

def logic_9459(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'health', 'direct')

def logic_9460(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'health', 'direct')

def logic_9461(agents, world):
    _agent_apply(world, agents, 'social_need', 'health', 'direct')

def logic_9462(agents, world):
    _agent_apply(world, agents, 'cooperation', 'health', 'direct')

def logic_9463(agents, world):
    _agent_apply(world, agents, 'defection', 'health', 'direct')

def logic_9464(agents, world):
    _agent_apply(world, agents, 'trust', 'health', 'direct')

def logic_9465(agents, world):
    _agent_apply(world, agents, 'reputation', 'health', 'direct')

def logic_9466(agents, world):
    _agent_apply(world, agents, 'help_received', 'health', 'direct')

def logic_9467(agents, world):
    _agent_apply(world, agents, 'help_given', 'health', 'direct')

def logic_9468(agents, world):
    _agent_apply(world, agents, 'local_density', 'health', 'direct')

def logic_9469(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'health', 'direct')

def logic_9470(agents, world):
    _agent_apply(world, agents, 'survival_score', 'health', 'direct')

def logic_9471(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'health', 'direct')

def logic_9472(agents, world):
    _agent_apply(world, agents, 'payoff', 'health', 'direct')

def logic_9473(agents, world):
    _agent_apply(world, agents, 'temperature', 'thermal_stress', 'direct')

def logic_9474(agents, world):
    _agent_apply(world, agents, 'surface_water', 'thermal_stress', 'direct')

def logic_9475(agents, world):
    _agent_apply(world, agents, 'humidity', 'thermal_stress', 'direct')

def logic_9476(agents, world):
    _agent_apply(world, agents, 'cloud', 'thermal_stress', 'direct')

def logic_9477(agents, world):
    _agent_apply(world, agents, 'rain', 'thermal_stress', 'direct')

def logic_9478(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'thermal_stress', 'direct')

def logic_9479(agents, world):
    _agent_apply(world, agents, 'runoff', 'thermal_stress', 'direct')

def logic_9480(agents, world):
    _agent_apply(world, agents, 'wind_x', 'thermal_stress', 'direct')

def logic_9481(agents, world):
    _agent_apply(world, agents, 'wind_y', 'thermal_stress', 'direct')

def logic_9482(agents, world):
    _agent_apply(world, agents, 'vegetation', 'thermal_stress', 'direct')

def logic_9483(agents, world):
    _agent_apply(world, agents, 'biomass', 'thermal_stress', 'direct')

def logic_9484(agents, world):
    _agent_apply(world, agents, 'herbivore', 'thermal_stress', 'direct')

def logic_9485(agents, world):
    _agent_apply(world, agents, 'predator', 'thermal_stress', 'direct')

def logic_9486(agents, world):
    _agent_apply(world, agents, 'carrion', 'thermal_stress', 'direct')

def logic_9487(agents, world):
    _agent_apply(world, agents, 'nutrients', 'thermal_stress', 'direct')

def logic_9488(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'thermal_stress', 'direct')

def logic_9489(agents, world):
    _agent_apply(world, agents, 'oxygen', 'thermal_stress', 'direct')

def logic_9490(agents, world):
    _agent_apply(world, agents, 'co2', 'thermal_stress', 'direct')

def logic_9491(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'thermal_stress', 'direct')

def logic_9492(agents, world):
    _agent_apply(world, agents, 'ice', 'thermal_stress', 'direct')

def logic_9493(agents, world):
    _agent_apply(world, agents, 'evaporation', 'thermal_stress', 'direct')

def logic_9494(agents, world):
    _agent_apply(world, agents, 'detritus', 'thermal_stress', 'direct')

def logic_9495(agents, world):
    _agent_apply(world, agents, 'methane', 'thermal_stress', 'direct')

def logic_9496(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'thermal_stress', 'direct')

def logic_9497(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'thermal_stress', 'direct')

def logic_9498(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'thermal_stress', 'direct')

def logic_9499(agents, world):
    _agent_apply(world, agents, 'erosion', 'thermal_stress', 'direct')

def logic_9500(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'thermal_stress', 'direct')

def logic_9501(agents, world):
    _agent_apply(world, agents, 'root_density', 'thermal_stress', 'direct')

def logic_9502(agents, world):
    _agent_apply(world, agents, 'wetland', 'thermal_stress', 'direct')

def logic_9503(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'thermal_stress', 'direct')

def logic_9504(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'thermal_stress', 'direct')

def logic_9505(agents, world):
    _agent_apply(world, agents, 'ash', 'thermal_stress', 'direct')

def logic_9506(agents, world):
    _agent_apply(world, agents, 'snowpack', 'thermal_stress', 'direct')

def logic_9507(agents, world):
    _agent_apply(world, agents, 'groundwater', 'thermal_stress', 'direct')

def logic_9508(agents, world):
    _agent_apply(world, agents, 'sediment', 'thermal_stress', 'direct')

def logic_9509(agents, world):
    _agent_apply(world, agents, 'salinity', 'thermal_stress', 'direct')

def logic_9510(agents, world):
    _agent_apply(world, agents, 'algae', 'thermal_stress', 'direct')

def logic_9511(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'thermal_stress', 'direct')

def logic_9512(agents, world):
    _agent_apply(world, agents, 'deadwood', 'thermal_stress', 'direct')

def logic_9513(agents, world):
    _agent_apply(world, agents, 'pollinators', 'thermal_stress', 'direct')

def logic_9514(agents, world):
    _agent_apply(world, agents, 'flowers', 'thermal_stress', 'direct')

def logic_9515(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'thermal_stress', 'direct')

def logic_9516(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'thermal_stress', 'direct')

def logic_9517(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'thermal_stress', 'direct')

def logic_9518(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'thermal_stress', 'direct')

def logic_9519(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'thermal_stress', 'direct')

def logic_9520(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'thermal_stress', 'direct')

def logic_9521(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'thermal_stress', 'direct')

def logic_9522(agents, world):
    _agent_apply(world, agents, 'hydration', 'thermal_stress', 'direct')

def logic_9523(agents, world):
    _agent_apply(world, agents, 'thirst', 'thermal_stress', 'direct')

def logic_9524(agents, world):
    _agent_apply(world, agents, 'hunger', 'thermal_stress', 'direct')

def logic_9525(agents, world):
    _agent_apply(world, agents, 'health', 'thermal_stress', 'direct')

def logic_9526(agents, world):
    _agent_apply(world, agents, 'stress', 'thermal_stress', 'direct')

def logic_9527(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'thermal_stress', 'direct')

def logic_9528(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'thermal_stress', 'direct')

def logic_9529(agents, world):
    _agent_apply(world, agents, 'social_need', 'thermal_stress', 'direct')

def logic_9530(agents, world):
    _agent_apply(world, agents, 'cooperation', 'thermal_stress', 'direct')

def logic_9531(agents, world):
    _agent_apply(world, agents, 'defection', 'thermal_stress', 'direct')

def logic_9532(agents, world):
    _agent_apply(world, agents, 'trust', 'thermal_stress', 'direct')

def logic_9533(agents, world):
    _agent_apply(world, agents, 'reputation', 'thermal_stress', 'direct')

def logic_9534(agents, world):
    _agent_apply(world, agents, 'help_received', 'thermal_stress', 'direct')

def logic_9535(agents, world):
    _agent_apply(world, agents, 'help_given', 'thermal_stress', 'direct')

def logic_9536(agents, world):
    _agent_apply(world, agents, 'local_density', 'thermal_stress', 'direct')

def logic_9537(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'thermal_stress', 'direct')

def logic_9538(agents, world):
    _agent_apply(world, agents, 'survival_score', 'thermal_stress', 'direct')

def logic_9539(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'thermal_stress', 'direct')

def logic_9540(agents, world):
    _agent_apply(world, agents, 'payoff', 'thermal_stress', 'direct')

def logic_9541(agents, world):
    _agent_apply(world, agents, 'temperature', 'dehydration', 'direct')

def logic_9542(agents, world):
    _agent_apply(world, agents, 'surface_water', 'dehydration', 'direct')

def logic_9543(agents, world):
    _agent_apply(world, agents, 'humidity', 'dehydration', 'direct')

def logic_9544(agents, world):
    _agent_apply(world, agents, 'cloud', 'dehydration', 'direct')

def logic_9545(agents, world):
    _agent_apply(world, agents, 'rain', 'dehydration', 'direct')

def logic_9546(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'dehydration', 'direct')

def logic_9547(agents, world):
    _agent_apply(world, agents, 'runoff', 'dehydration', 'direct')

def logic_9548(agents, world):
    _agent_apply(world, agents, 'wind_x', 'dehydration', 'direct')

def logic_9549(agents, world):
    _agent_apply(world, agents, 'wind_y', 'dehydration', 'direct')

def logic_9550(agents, world):
    _agent_apply(world, agents, 'vegetation', 'dehydration', 'direct')

def logic_9551(agents, world):
    _agent_apply(world, agents, 'biomass', 'dehydration', 'direct')

def logic_9552(agents, world):
    _agent_apply(world, agents, 'herbivore', 'dehydration', 'direct')

def logic_9553(agents, world):
    _agent_apply(world, agents, 'predator', 'dehydration', 'direct')

def logic_9554(agents, world):
    _agent_apply(world, agents, 'carrion', 'dehydration', 'direct')

def logic_9555(agents, world):
    _agent_apply(world, agents, 'nutrients', 'dehydration', 'direct')

def logic_9556(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'dehydration', 'direct')

def logic_9557(agents, world):
    _agent_apply(world, agents, 'oxygen', 'dehydration', 'direct')

def logic_9558(agents, world):
    _agent_apply(world, agents, 'co2', 'dehydration', 'direct')

def logic_9559(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'dehydration', 'direct')

def logic_9560(agents, world):
    _agent_apply(world, agents, 'ice', 'dehydration', 'direct')

def logic_9561(agents, world):
    _agent_apply(world, agents, 'evaporation', 'dehydration', 'direct')

def logic_9562(agents, world):
    _agent_apply(world, agents, 'detritus', 'dehydration', 'direct')

def logic_9563(agents, world):
    _agent_apply(world, agents, 'methane', 'dehydration', 'direct')

def logic_9564(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'dehydration', 'direct')

def logic_9565(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'dehydration', 'direct')

def logic_9566(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'dehydration', 'direct')

def logic_9567(agents, world):
    _agent_apply(world, agents, 'erosion', 'dehydration', 'direct')

def logic_9568(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'dehydration', 'direct')

def logic_9569(agents, world):
    _agent_apply(world, agents, 'root_density', 'dehydration', 'direct')

def logic_9570(agents, world):
    _agent_apply(world, agents, 'wetland', 'dehydration', 'direct')

def logic_9571(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'dehydration', 'direct')

def logic_9572(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'dehydration', 'direct')

def logic_9573(agents, world):
    _agent_apply(world, agents, 'ash', 'dehydration', 'direct')

def logic_9574(agents, world):
    _agent_apply(world, agents, 'snowpack', 'dehydration', 'direct')

def logic_9575(agents, world):
    _agent_apply(world, agents, 'groundwater', 'dehydration', 'direct')

def logic_9576(agents, world):
    _agent_apply(world, agents, 'sediment', 'dehydration', 'direct')

def logic_9577(agents, world):
    _agent_apply(world, agents, 'salinity', 'dehydration', 'direct')

def logic_9578(agents, world):
    _agent_apply(world, agents, 'algae', 'dehydration', 'direct')

def logic_9579(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'dehydration', 'direct')

def logic_9580(agents, world):
    _agent_apply(world, agents, 'deadwood', 'dehydration', 'direct')

def logic_9581(agents, world):
    _agent_apply(world, agents, 'pollinators', 'dehydration', 'direct')

def logic_9582(agents, world):
    _agent_apply(world, agents, 'flowers', 'dehydration', 'direct')

def logic_9583(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'dehydration', 'direct')

def logic_9584(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'dehydration', 'direct')

def logic_9585(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'dehydration', 'direct')

def logic_9586(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'dehydration', 'direct')

def logic_9587(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'dehydration', 'direct')

def logic_9588(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'dehydration', 'direct')

def logic_9589(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'dehydration', 'direct')

def logic_9590(agents, world):
    _agent_apply(world, agents, 'hydration', 'dehydration', 'direct')

def logic_9591(agents, world):
    _agent_apply(world, agents, 'thirst', 'dehydration', 'direct')

def logic_9592(agents, world):
    _agent_apply(world, agents, 'hunger', 'dehydration', 'direct')

def logic_9593(agents, world):
    _agent_apply(world, agents, 'health', 'dehydration', 'direct')

def logic_9594(agents, world):
    _agent_apply(world, agents, 'stress', 'dehydration', 'direct')

def logic_9595(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'dehydration', 'direct')

def logic_9596(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'dehydration', 'direct')

def logic_9597(agents, world):
    _agent_apply(world, agents, 'social_need', 'dehydration', 'direct')

def logic_9598(agents, world):
    _agent_apply(world, agents, 'cooperation', 'dehydration', 'direct')

def logic_9599(agents, world):
    _agent_apply(world, agents, 'defection', 'dehydration', 'direct')

def logic_9600(agents, world):
    _agent_apply(world, agents, 'trust', 'dehydration', 'direct')

def logic_9601(agents, world):
    _agent_apply(world, agents, 'reputation', 'dehydration', 'direct')

def logic_9602(agents, world):
    _agent_apply(world, agents, 'help_received', 'dehydration', 'direct')

def logic_9603(agents, world):
    _agent_apply(world, agents, 'help_given', 'dehydration', 'direct')

def logic_9604(agents, world):
    _agent_apply(world, agents, 'local_density', 'dehydration', 'direct')

def logic_9605(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'dehydration', 'direct')

def logic_9606(agents, world):
    _agent_apply(world, agents, 'survival_score', 'dehydration', 'direct')

def logic_9607(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'dehydration', 'direct')

def logic_9608(agents, world):
    _agent_apply(world, agents, 'payoff', 'dehydration', 'direct')

def logic_9609(agents, world):
    _agent_apply(world, agents, 'temperature', 'pathogen_risk', 'direct')

def logic_9610(agents, world):
    _agent_apply(world, agents, 'surface_water', 'pathogen_risk', 'direct')

def logic_9611(agents, world):
    _agent_apply(world, agents, 'humidity', 'pathogen_risk', 'direct')

def logic_9612(agents, world):
    _agent_apply(world, agents, 'cloud', 'pathogen_risk', 'direct')

def logic_9613(agents, world):
    _agent_apply(world, agents, 'rain', 'pathogen_risk', 'direct')

def logic_9614(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'pathogen_risk', 'direct')

def logic_9615(agents, world):
    _agent_apply(world, agents, 'runoff', 'pathogen_risk', 'direct')

def logic_9616(agents, world):
    _agent_apply(world, agents, 'wind_x', 'pathogen_risk', 'direct')

def logic_9617(agents, world):
    _agent_apply(world, agents, 'wind_y', 'pathogen_risk', 'direct')

def logic_9618(agents, world):
    _agent_apply(world, agents, 'vegetation', 'pathogen_risk', 'direct')

def logic_9619(agents, world):
    _agent_apply(world, agents, 'biomass', 'pathogen_risk', 'direct')

def logic_9620(agents, world):
    _agent_apply(world, agents, 'herbivore', 'pathogen_risk', 'direct')

def logic_9621(agents, world):
    _agent_apply(world, agents, 'predator', 'pathogen_risk', 'direct')

def logic_9622(agents, world):
    _agent_apply(world, agents, 'carrion', 'pathogen_risk', 'direct')

def logic_9623(agents, world):
    _agent_apply(world, agents, 'nutrients', 'pathogen_risk', 'direct')

def logic_9624(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'pathogen_risk', 'direct')

def logic_9625(agents, world):
    _agent_apply(world, agents, 'oxygen', 'pathogen_risk', 'direct')

def logic_9626(agents, world):
    _agent_apply(world, agents, 'co2', 'pathogen_risk', 'direct')

def logic_9627(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'pathogen_risk', 'direct')

def logic_9628(agents, world):
    _agent_apply(world, agents, 'ice', 'pathogen_risk', 'direct')

def logic_9629(agents, world):
    _agent_apply(world, agents, 'evaporation', 'pathogen_risk', 'direct')

def logic_9630(agents, world):
    _agent_apply(world, agents, 'detritus', 'pathogen_risk', 'direct')

def logic_9631(agents, world):
    _agent_apply(world, agents, 'methane', 'pathogen_risk', 'direct')

def logic_9632(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'pathogen_risk', 'direct')

def logic_9633(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'pathogen_risk', 'direct')

def logic_9634(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'pathogen_risk', 'direct')

def logic_9635(agents, world):
    _agent_apply(world, agents, 'erosion', 'pathogen_risk', 'direct')

def logic_9636(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'pathogen_risk', 'direct')

def logic_9637(agents, world):
    _agent_apply(world, agents, 'root_density', 'pathogen_risk', 'direct')

def logic_9638(agents, world):
    _agent_apply(world, agents, 'wetland', 'pathogen_risk', 'direct')

def logic_9639(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'pathogen_risk', 'direct')

def logic_9640(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'pathogen_risk', 'direct')

def logic_9641(agents, world):
    _agent_apply(world, agents, 'ash', 'pathogen_risk', 'direct')

def logic_9642(agents, world):
    _agent_apply(world, agents, 'snowpack', 'pathogen_risk', 'direct')

def logic_9643(agents, world):
    _agent_apply(world, agents, 'groundwater', 'pathogen_risk', 'direct')

def logic_9644(agents, world):
    _agent_apply(world, agents, 'sediment', 'pathogen_risk', 'direct')

def logic_9645(agents, world):
    _agent_apply(world, agents, 'salinity', 'pathogen_risk', 'direct')

def logic_9646(agents, world):
    _agent_apply(world, agents, 'algae', 'pathogen_risk', 'direct')

def logic_9647(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'pathogen_risk', 'direct')

def logic_9648(agents, world):
    _agent_apply(world, agents, 'deadwood', 'pathogen_risk', 'direct')

def logic_9649(agents, world):
    _agent_apply(world, agents, 'pollinators', 'pathogen_risk', 'direct')

def logic_9650(agents, world):
    _agent_apply(world, agents, 'flowers', 'pathogen_risk', 'direct')

def logic_9651(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'pathogen_risk', 'direct')

def logic_9652(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'pathogen_risk', 'direct')

def logic_9653(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'pathogen_risk', 'direct')

def logic_9654(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'pathogen_risk', 'direct')

def logic_9655(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'pathogen_risk', 'direct')

def logic_9656(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'pathogen_risk', 'direct')

def logic_9657(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'pathogen_risk', 'direct')

def logic_9658(agents, world):
    _agent_apply(world, agents, 'hydration', 'pathogen_risk', 'direct')

def logic_9659(agents, world):
    _agent_apply(world, agents, 'thirst', 'pathogen_risk', 'direct')

def logic_9660(agents, world):
    _agent_apply(world, agents, 'hunger', 'pathogen_risk', 'direct')

def logic_9661(agents, world):
    _agent_apply(world, agents, 'health', 'pathogen_risk', 'direct')

def logic_9662(agents, world):
    _agent_apply(world, agents, 'stress', 'pathogen_risk', 'direct')

def logic_9663(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'pathogen_risk', 'direct')

def logic_9664(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'pathogen_risk', 'direct')

def logic_9665(agents, world):
    _agent_apply(world, agents, 'social_need', 'pathogen_risk', 'direct')

def logic_9666(agents, world):
    _agent_apply(world, agents, 'cooperation', 'pathogen_risk', 'direct')

def logic_9667(agents, world):
    _agent_apply(world, agents, 'defection', 'pathogen_risk', 'direct')

def logic_9668(agents, world):
    _agent_apply(world, agents, 'trust', 'pathogen_risk', 'direct')

def logic_9669(agents, world):
    _agent_apply(world, agents, 'reputation', 'pathogen_risk', 'direct')

def logic_9670(agents, world):
    _agent_apply(world, agents, 'help_received', 'pathogen_risk', 'direct')

def logic_9671(agents, world):
    _agent_apply(world, agents, 'help_given', 'pathogen_risk', 'direct')

def logic_9672(agents, world):
    _agent_apply(world, agents, 'local_density', 'pathogen_risk', 'direct')

def logic_9673(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'pathogen_risk', 'direct')

def logic_9674(agents, world):
    _agent_apply(world, agents, 'survival_score', 'pathogen_risk', 'direct')

def logic_9675(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'pathogen_risk', 'direct')

def logic_9676(agents, world):
    _agent_apply(world, agents, 'payoff', 'pathogen_risk', 'direct')

def logic_9677(agents, world):
    _agent_apply(world, agents, 'temperature', 'infection_risk', 'direct')

def logic_9678(agents, world):
    _agent_apply(world, agents, 'surface_water', 'infection_risk', 'direct')

def logic_9679(agents, world):
    _agent_apply(world, agents, 'humidity', 'infection_risk', 'direct')

def logic_9680(agents, world):
    _agent_apply(world, agents, 'cloud', 'infection_risk', 'direct')

def logic_9681(agents, world):
    _agent_apply(world, agents, 'rain', 'infection_risk', 'direct')

def logic_9682(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'infection_risk', 'direct')

def logic_9683(agents, world):
    _agent_apply(world, agents, 'runoff', 'infection_risk', 'direct')

def logic_9684(agents, world):
    _agent_apply(world, agents, 'wind_x', 'infection_risk', 'direct')

def logic_9685(agents, world):
    _agent_apply(world, agents, 'wind_y', 'infection_risk', 'direct')

def logic_9686(agents, world):
    _agent_apply(world, agents, 'vegetation', 'infection_risk', 'direct')

def logic_9687(agents, world):
    _agent_apply(world, agents, 'biomass', 'infection_risk', 'direct')

def logic_9688(agents, world):
    _agent_apply(world, agents, 'herbivore', 'infection_risk', 'direct')

def logic_9689(agents, world):
    _agent_apply(world, agents, 'predator', 'infection_risk', 'direct')

def logic_9690(agents, world):
    _agent_apply(world, agents, 'carrion', 'infection_risk', 'direct')

def logic_9691(agents, world):
    _agent_apply(world, agents, 'nutrients', 'infection_risk', 'direct')

def logic_9692(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'infection_risk', 'direct')

def logic_9693(agents, world):
    _agent_apply(world, agents, 'oxygen', 'infection_risk', 'direct')

def logic_9694(agents, world):
    _agent_apply(world, agents, 'co2', 'infection_risk', 'direct')

def logic_9695(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'infection_risk', 'direct')

def logic_9696(agents, world):
    _agent_apply(world, agents, 'ice', 'infection_risk', 'direct')

def logic_9697(agents, world):
    _agent_apply(world, agents, 'evaporation', 'infection_risk', 'direct')

def logic_9698(agents, world):
    _agent_apply(world, agents, 'detritus', 'infection_risk', 'direct')

def logic_9699(agents, world):
    _agent_apply(world, agents, 'methane', 'infection_risk', 'direct')

def logic_9700(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'infection_risk', 'direct')

def logic_9701(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'infection_risk', 'direct')

def logic_9702(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'infection_risk', 'direct')

def logic_9703(agents, world):
    _agent_apply(world, agents, 'erosion', 'infection_risk', 'direct')

def logic_9704(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'infection_risk', 'direct')

def logic_9705(agents, world):
    _agent_apply(world, agents, 'root_density', 'infection_risk', 'direct')

def logic_9706(agents, world):
    _agent_apply(world, agents, 'wetland', 'infection_risk', 'direct')

def logic_9707(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'infection_risk', 'direct')

def logic_9708(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'infection_risk', 'direct')

def logic_9709(agents, world):
    _agent_apply(world, agents, 'ash', 'infection_risk', 'direct')

def logic_9710(agents, world):
    _agent_apply(world, agents, 'snowpack', 'infection_risk', 'direct')

def logic_9711(agents, world):
    _agent_apply(world, agents, 'groundwater', 'infection_risk', 'direct')

def logic_9712(agents, world):
    _agent_apply(world, agents, 'sediment', 'infection_risk', 'direct')

def logic_9713(agents, world):
    _agent_apply(world, agents, 'salinity', 'infection_risk', 'direct')

def logic_9714(agents, world):
    _agent_apply(world, agents, 'algae', 'infection_risk', 'direct')

def logic_9715(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'infection_risk', 'direct')

def logic_9716(agents, world):
    _agent_apply(world, agents, 'deadwood', 'infection_risk', 'direct')

def logic_9717(agents, world):
    _agent_apply(world, agents, 'pollinators', 'infection_risk', 'direct')

def logic_9718(agents, world):
    _agent_apply(world, agents, 'flowers', 'infection_risk', 'direct')

def logic_9719(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'infection_risk', 'direct')

def logic_9720(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'infection_risk', 'direct')

def logic_9721(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'infection_risk', 'direct')

def logic_9722(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'infection_risk', 'direct')

def logic_9723(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'infection_risk', 'direct')

def logic_9724(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'infection_risk', 'direct')

def logic_9725(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'infection_risk', 'direct')

def logic_9726(agents, world):
    _agent_apply(world, agents, 'hydration', 'infection_risk', 'direct')

def logic_9727(agents, world):
    _agent_apply(world, agents, 'thirst', 'infection_risk', 'direct')

def logic_9728(agents, world):
    _agent_apply(world, agents, 'hunger', 'infection_risk', 'direct')

def logic_9729(agents, world):
    _agent_apply(world, agents, 'health', 'infection_risk', 'direct')

def logic_9730(agents, world):
    _agent_apply(world, agents, 'stress', 'infection_risk', 'direct')

def logic_9731(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'infection_risk', 'direct')

def logic_9732(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'infection_risk', 'direct')

def logic_9733(agents, world):
    _agent_apply(world, agents, 'social_need', 'infection_risk', 'direct')

def logic_9734(agents, world):
    _agent_apply(world, agents, 'cooperation', 'infection_risk', 'direct')

def logic_9735(agents, world):
    _agent_apply(world, agents, 'defection', 'infection_risk', 'direct')

def logic_9736(agents, world):
    _agent_apply(world, agents, 'trust', 'infection_risk', 'direct')

def logic_9737(agents, world):
    _agent_apply(world, agents, 'reputation', 'infection_risk', 'direct')

def logic_9738(agents, world):
    _agent_apply(world, agents, 'help_received', 'infection_risk', 'direct')

def logic_9739(agents, world):
    _agent_apply(world, agents, 'help_given', 'infection_risk', 'direct')

def logic_9740(agents, world):
    _agent_apply(world, agents, 'local_density', 'infection_risk', 'direct')

def logic_9741(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'infection_risk', 'direct')

def logic_9742(agents, world):
    _agent_apply(world, agents, 'survival_score', 'infection_risk', 'direct')

def logic_9743(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'infection_risk', 'direct')

def logic_9744(agents, world):
    _agent_apply(world, agents, 'payoff', 'infection_risk', 'direct')

def logic_9745(agents, world):
    _agent_apply(world, agents, 'temperature', 'alertness', 'direct')

def logic_9746(agents, world):
    _agent_apply(world, agents, 'surface_water', 'alertness', 'direct')

def logic_9747(agents, world):
    _agent_apply(world, agents, 'humidity', 'alertness', 'direct')

def logic_9748(agents, world):
    _agent_apply(world, agents, 'cloud', 'alertness', 'direct')

def logic_9749(agents, world):
    _agent_apply(world, agents, 'rain', 'alertness', 'direct')

def logic_9750(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'alertness', 'direct')

def logic_9751(agents, world):
    _agent_apply(world, agents, 'runoff', 'alertness', 'direct')
