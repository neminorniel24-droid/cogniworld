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
    return torch.sigmoid(x)


def _world_apply(world, source, target, mode):
    s = _world_signal(world, source)
    t = _world_signal(world, target)
    if s is None or t is None:
        return
    s = _norm(s)
    if mode == "inverse":
        d = 1 - s
    elif mode == "square":
        d = s * s
    elif mode == "sqrt":
        d = torch.sqrt(s.clamp_min(0))
    elif mode == "pulse":
        d = 4 * s * (1 - s)
    elif mode == "threshold":
        d = (s > 0.5).float()
    elif mode == "saturation":
        d = s / (0.25 + s)
    elif mode == "reciprocal":
        d = 1 / (1 + s)
    else:
        d = s
    setattr(world, target, torch.nan_to_num(t) + RATE * (d - torch.nan_to_num(t)))


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
    if mode == "inverse":
        d = 1 - s
    elif mode == "square":
        d = s * s
    elif mode == "sqrt":
        d = torch.sqrt(s.clamp_min(0))
    elif mode == "pulse":
        d = 4 * s * (1 - s)
    elif mode == "feedback":
        d = s * t
    elif mode == "scarcity":
        d = (1 - s) * _norm(getattr(agents, "hunger"))
    elif mode == "reserve":
        d = s * _norm(getattr(agents, "energy_surplus"))
    elif mode == "stress":
        d = s * _norm(getattr(agents, "stress"))
    elif mode == "recovery":
        d = s * _norm(getattr(agents, "health"))
    elif mode == "persistence":
        d = s * _norm(getattr(agents, "memory_update"))
    elif mode == "risk":
        d = s * _norm(getattr(agents, "risk_tolerance"))
    elif mode == "competition":
        d = s * _norm(getattr(agents, "competition_pressure"))
    elif mode == "social":
        d = s * _norm(getattr(agents, "social_need"))
    elif mode == "resource":
        d = s * _norm(getattr(agents, "resource_abundance"))
    elif mode == "threshold":
        d = (s > 0.5).to(s.dtype)
    elif mode == "saturation":
        d = s / (0.25 + s)
    elif mode == "gap":
        d = torch.abs(s - t)
    elif mode == "reciprocal":
        d = 1 / (1 + s)
    else:
        d = s
    new_signal = t + RATE * (d - t)
    setattr(agents, target, torch.logit(new_signal.clamp(1e-5, 1 - 1e-5)))

def logic_4102(agents, world):
    _agent_apply(world, agents, 'temperature', 'hydration', 'direct')

def logic_4103(agents, world):
    _agent_apply(world, agents, 'surface_water', 'hydration', 'direct')

def logic_4104(agents, world):
    _agent_apply(world, agents, 'humidity', 'hydration', 'direct')

def logic_4105(agents, world):
    _agent_apply(world, agents, 'cloud', 'hydration', 'direct')

def logic_4106(agents, world):
    _agent_apply(world, agents, 'rain', 'hydration', 'direct')

def logic_4107(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'hydration', 'direct')

def logic_4108(agents, world):
    _agent_apply(world, agents, 'runoff', 'hydration', 'direct')

def logic_4109(agents, world):
    _agent_apply(world, agents, 'wind_x', 'hydration', 'direct')

def logic_4110(agents, world):
    _agent_apply(world, agents, 'wind_y', 'hydration', 'direct')

def logic_4111(agents, world):
    _agent_apply(world, agents, 'vegetation', 'hydration', 'direct')

def logic_4112(agents, world):
    _agent_apply(world, agents, 'biomass', 'hydration', 'direct')

def logic_4113(agents, world):
    _agent_apply(world, agents, 'herbivore', 'hydration', 'direct')

def logic_4114(agents, world):
    _agent_apply(world, agents, 'predator', 'hydration', 'direct')

def logic_4115(agents, world):
    _agent_apply(world, agents, 'carrion', 'hydration', 'direct')

def logic_4116(agents, world):
    _agent_apply(world, agents, 'nutrients', 'hydration', 'direct')

def logic_4117(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'hydration', 'direct')

def logic_4118(agents, world):
    _agent_apply(world, agents, 'oxygen', 'hydration', 'direct')

def logic_4119(agents, world):
    _agent_apply(world, agents, 'co2', 'hydration', 'direct')

def logic_4120(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'hydration', 'direct')

def logic_4121(agents, world):
    _agent_apply(world, agents, 'ice', 'hydration', 'direct')

def logic_4122(agents, world):
    _agent_apply(world, agents, 'evaporation', 'hydration', 'direct')

def logic_4123(agents, world):
    _agent_apply(world, agents, 'detritus', 'hydration', 'direct')

def logic_4124(agents, world):
    _agent_apply(world, agents, 'methane', 'hydration', 'direct')

def logic_4125(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'hydration', 'direct')

def logic_4126(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'hydration', 'direct')

def logic_4127(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'hydration', 'direct')

def logic_4128(agents, world):
    _agent_apply(world, agents, 'erosion', 'hydration', 'direct')

def logic_4129(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'hydration', 'direct')

def logic_4130(agents, world):
    _agent_apply(world, agents, 'root_density', 'hydration', 'direct')

def logic_4131(agents, world):
    _agent_apply(world, agents, 'wetland', 'hydration', 'direct')

def logic_4132(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'hydration', 'direct')

def logic_4133(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'hydration', 'direct')

def logic_4134(agents, world):
    _agent_apply(world, agents, 'ash', 'hydration', 'direct')

def logic_4135(agents, world):
    _agent_apply(world, agents, 'snowpack', 'hydration', 'direct')

def logic_4136(agents, world):
    _agent_apply(world, agents, 'groundwater', 'hydration', 'direct')

def logic_4137(agents, world):
    _agent_apply(world, agents, 'sediment', 'hydration', 'direct')

def logic_4138(agents, world):
    _agent_apply(world, agents, 'salinity', 'hydration', 'direct')

def logic_4139(agents, world):
    _agent_apply(world, agents, 'algae', 'hydration', 'direct')

def logic_4140(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'hydration', 'direct')

def logic_4141(agents, world):
    _agent_apply(world, agents, 'deadwood', 'hydration', 'direct')

def logic_4142(agents, world):
    _agent_apply(world, agents, 'pollinators', 'hydration', 'direct')

def logic_4143(agents, world):
    _agent_apply(world, agents, 'flowers', 'hydration', 'direct')

def logic_4144(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'hydration', 'direct')

def logic_4145(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'hydration', 'direct')

def logic_4146(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'hydration', 'direct')

def logic_4147(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'hydration', 'direct')

def logic_4148(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'hydration', 'direct')

def logic_4149(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'hydration', 'direct')

def logic_4150(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'hydration', 'direct')

def logic_4151(agents, world):
    _agent_apply(world, agents, 'hydration', 'hydration', 'direct')

def logic_4152(agents, world):
    _agent_apply(world, agents, 'thirst', 'hydration', 'direct')

def logic_4153(agents, world):
    _agent_apply(world, agents, 'hunger', 'hydration', 'direct')

def logic_4154(agents, world):
    _agent_apply(world, agents, 'health', 'hydration', 'direct')

def logic_4155(agents, world):
    _agent_apply(world, agents, 'stress', 'hydration', 'direct')

def logic_4156(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'hydration', 'direct')

def logic_4157(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'hydration', 'direct')

def logic_4158(agents, world):
    _agent_apply(world, agents, 'social_need', 'hydration', 'direct')

def logic_4159(agents, world):
    _agent_apply(world, agents, 'cooperation', 'hydration', 'direct')

def logic_4160(agents, world):
    _agent_apply(world, agents, 'defection', 'hydration', 'direct')

def logic_4161(agents, world):
    _agent_apply(world, agents, 'trust', 'hydration', 'direct')

def logic_4162(agents, world):
    _agent_apply(world, agents, 'reputation', 'hydration', 'direct')

def logic_4163(agents, world):
    _agent_apply(world, agents, 'help_received', 'hydration', 'direct')

def logic_4164(agents, world):
    _agent_apply(world, agents, 'help_given', 'hydration', 'direct')

def logic_4165(agents, world):
    _agent_apply(world, agents, 'local_density', 'hydration', 'direct')

def logic_4166(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'hydration', 'direct')

def logic_4167(agents, world):
    _agent_apply(world, agents, 'survival_score', 'hydration', 'direct')

def logic_4168(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'hydration', 'direct')

def logic_4169(agents, world):
    _agent_apply(world, agents, 'payoff', 'hydration', 'direct')

def logic_4170(agents, world):
    _agent_apply(world, agents, 'temperature', 'thirst', 'direct')

def logic_4171(agents, world):
    _agent_apply(world, agents, 'surface_water', 'thirst', 'direct')

def logic_4172(agents, world):
    _agent_apply(world, agents, 'humidity', 'thirst', 'direct')

def logic_4173(agents, world):
    _agent_apply(world, agents, 'cloud', 'thirst', 'direct')

def logic_4174(agents, world):
    _agent_apply(world, agents, 'rain', 'thirst', 'direct')

def logic_4175(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'thirst', 'direct')

def logic_4176(agents, world):
    _agent_apply(world, agents, 'runoff', 'thirst', 'direct')

def logic_4177(agents, world):
    _agent_apply(world, agents, 'wind_x', 'thirst', 'direct')

def logic_4178(agents, world):
    _agent_apply(world, agents, 'wind_y', 'thirst', 'direct')

def logic_4179(agents, world):
    _agent_apply(world, agents, 'vegetation', 'thirst', 'direct')

def logic_4180(agents, world):
    _agent_apply(world, agents, 'biomass', 'thirst', 'direct')

def logic_4181(agents, world):
    _agent_apply(world, agents, 'herbivore', 'thirst', 'direct')

def logic_4182(agents, world):
    _agent_apply(world, agents, 'predator', 'thirst', 'direct')

def logic_4183(agents, world):
    _agent_apply(world, agents, 'carrion', 'thirst', 'direct')

def logic_4184(agents, world):
    _agent_apply(world, agents, 'nutrients', 'thirst', 'direct')

def logic_4185(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'thirst', 'direct')

def logic_4186(agents, world):
    _agent_apply(world, agents, 'oxygen', 'thirst', 'direct')

def logic_4187(agents, world):
    _agent_apply(world, agents, 'co2', 'thirst', 'direct')

def logic_4188(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'thirst', 'direct')

def logic_4189(agents, world):
    _agent_apply(world, agents, 'ice', 'thirst', 'direct')

def logic_4190(agents, world):
    _agent_apply(world, agents, 'evaporation', 'thirst', 'direct')

def logic_4191(agents, world):
    _agent_apply(world, agents, 'detritus', 'thirst', 'direct')

def logic_4192(agents, world):
    _agent_apply(world, agents, 'methane', 'thirst', 'direct')

def logic_4193(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'thirst', 'direct')

def logic_4194(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'thirst', 'direct')

def logic_4195(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'thirst', 'direct')

def logic_4196(agents, world):
    _agent_apply(world, agents, 'erosion', 'thirst', 'direct')

def logic_4197(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'thirst', 'direct')

def logic_4198(agents, world):
    _agent_apply(world, agents, 'root_density', 'thirst', 'direct')

def logic_4199(agents, world):
    _agent_apply(world, agents, 'wetland', 'thirst', 'direct')

def logic_4200(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'thirst', 'direct')

def logic_4201(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'thirst', 'direct')

def logic_4202(agents, world):
    _agent_apply(world, agents, 'ash', 'thirst', 'direct')

def logic_4203(agents, world):
    _agent_apply(world, agents, 'snowpack', 'thirst', 'direct')

def logic_4204(agents, world):
    _agent_apply(world, agents, 'groundwater', 'thirst', 'direct')

def logic_4205(agents, world):
    _agent_apply(world, agents, 'sediment', 'thirst', 'direct')

def logic_4206(agents, world):
    _agent_apply(world, agents, 'salinity', 'thirst', 'direct')

def logic_4207(agents, world):
    _agent_apply(world, agents, 'algae', 'thirst', 'direct')

def logic_4208(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'thirst', 'direct')

def logic_4209(agents, world):
    _agent_apply(world, agents, 'deadwood', 'thirst', 'direct')

def logic_4210(agents, world):
    _agent_apply(world, agents, 'pollinators', 'thirst', 'direct')

def logic_4211(agents, world):
    _agent_apply(world, agents, 'flowers', 'thirst', 'direct')

def logic_4212(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'thirst', 'direct')

def logic_4213(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'thirst', 'direct')

def logic_4214(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'thirst', 'direct')

def logic_4215(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'thirst', 'direct')

def logic_4216(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'thirst', 'direct')

def logic_4217(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'thirst', 'direct')

def logic_4218(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'thirst', 'direct')

def logic_4219(agents, world):
    _agent_apply(world, agents, 'hydration', 'thirst', 'direct')

def logic_4220(agents, world):
    _agent_apply(world, agents, 'thirst', 'thirst', 'direct')

def logic_4221(agents, world):
    _agent_apply(world, agents, 'hunger', 'thirst', 'direct')

def logic_4222(agents, world):
    _agent_apply(world, agents, 'health', 'thirst', 'direct')

def logic_4223(agents, world):
    _agent_apply(world, agents, 'stress', 'thirst', 'direct')

def logic_4224(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'thirst', 'direct')

def logic_4225(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'thirst', 'direct')

def logic_4226(agents, world):
    _agent_apply(world, agents, 'social_need', 'thirst', 'direct')

def logic_4227(agents, world):
    _agent_apply(world, agents, 'cooperation', 'thirst', 'direct')

def logic_4228(agents, world):
    _agent_apply(world, agents, 'defection', 'thirst', 'direct')

def logic_4229(agents, world):
    _agent_apply(world, agents, 'trust', 'thirst', 'direct')

def logic_4230(agents, world):
    _agent_apply(world, agents, 'reputation', 'thirst', 'direct')

def logic_4231(agents, world):
    _agent_apply(world, agents, 'help_received', 'thirst', 'direct')

def logic_4232(agents, world):
    _agent_apply(world, agents, 'help_given', 'thirst', 'direct')

def logic_4233(agents, world):
    _agent_apply(world, agents, 'local_density', 'thirst', 'direct')

def logic_4234(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'thirst', 'direct')

def logic_4235(agents, world):
    _agent_apply(world, agents, 'survival_score', 'thirst', 'direct')

def logic_4236(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'thirst', 'direct')

def logic_4237(agents, world):
    _agent_apply(world, agents, 'payoff', 'thirst', 'direct')

def logic_4238(agents, world):
    _agent_apply(world, agents, 'temperature', 'hunger', 'direct')

def logic_4239(agents, world):
    _agent_apply(world, agents, 'surface_water', 'hunger', 'direct')

def logic_4240(agents, world):
    _agent_apply(world, agents, 'humidity', 'hunger', 'direct')

def logic_4241(agents, world):
    _agent_apply(world, agents, 'cloud', 'hunger', 'direct')

def logic_4242(agents, world):
    _agent_apply(world, agents, 'rain', 'hunger', 'direct')

def logic_4243(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'hunger', 'direct')

def logic_4244(agents, world):
    _agent_apply(world, agents, 'runoff', 'hunger', 'direct')

def logic_4245(agents, world):
    _agent_apply(world, agents, 'wind_x', 'hunger', 'direct')

def logic_4246(agents, world):
    _agent_apply(world, agents, 'wind_y', 'hunger', 'direct')

def logic_4247(agents, world):
    _agent_apply(world, agents, 'vegetation', 'hunger', 'direct')

def logic_4248(agents, world):
    _agent_apply(world, agents, 'biomass', 'hunger', 'direct')

def logic_4249(agents, world):
    _agent_apply(world, agents, 'herbivore', 'hunger', 'direct')

def logic_4250(agents, world):
    _agent_apply(world, agents, 'predator', 'hunger', 'direct')

def logic_4251(agents, world):
    _agent_apply(world, agents, 'carrion', 'hunger', 'direct')

def logic_4252(agents, world):
    _agent_apply(world, agents, 'nutrients', 'hunger', 'direct')

def logic_4253(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'hunger', 'direct')

def logic_4254(agents, world):
    _agent_apply(world, agents, 'oxygen', 'hunger', 'direct')

def logic_4255(agents, world):
    _agent_apply(world, agents, 'co2', 'hunger', 'direct')

def logic_4256(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'hunger', 'direct')

def logic_4257(agents, world):
    _agent_apply(world, agents, 'ice', 'hunger', 'direct')

def logic_4258(agents, world):
    _agent_apply(world, agents, 'evaporation', 'hunger', 'direct')

def logic_4259(agents, world):
    _agent_apply(world, agents, 'detritus', 'hunger', 'direct')

def logic_4260(agents, world):
    _agent_apply(world, agents, 'methane', 'hunger', 'direct')

def logic_4261(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'hunger', 'direct')

def logic_4262(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'hunger', 'direct')

def logic_4263(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'hunger', 'direct')

def logic_4264(agents, world):
    _agent_apply(world, agents, 'erosion', 'hunger', 'direct')

def logic_4265(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'hunger', 'direct')

def logic_4266(agents, world):
    _agent_apply(world, agents, 'root_density', 'hunger', 'direct')

def logic_4267(agents, world):
    _agent_apply(world, agents, 'wetland', 'hunger', 'direct')

def logic_4268(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'hunger', 'direct')

def logic_4269(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'hunger', 'direct')

def logic_4270(agents, world):
    _agent_apply(world, agents, 'ash', 'hunger', 'direct')

def logic_4271(agents, world):
    _agent_apply(world, agents, 'snowpack', 'hunger', 'direct')

def logic_4272(agents, world):
    _agent_apply(world, agents, 'groundwater', 'hunger', 'direct')

def logic_4273(agents, world):
    _agent_apply(world, agents, 'sediment', 'hunger', 'direct')

def logic_4274(agents, world):
    _agent_apply(world, agents, 'salinity', 'hunger', 'direct')

def logic_4275(agents, world):
    _agent_apply(world, agents, 'algae', 'hunger', 'direct')

def logic_4276(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'hunger', 'direct')

def logic_4277(agents, world):
    _agent_apply(world, agents, 'deadwood', 'hunger', 'direct')

def logic_4278(agents, world):
    _agent_apply(world, agents, 'pollinators', 'hunger', 'direct')

def logic_4279(agents, world):
    _agent_apply(world, agents, 'flowers', 'hunger', 'direct')

def logic_4280(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'hunger', 'direct')

def logic_4281(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'hunger', 'direct')

def logic_4282(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'hunger', 'direct')

def logic_4283(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'hunger', 'direct')

def logic_4284(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'hunger', 'direct')

def logic_4285(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'hunger', 'direct')

def logic_4286(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'hunger', 'direct')

def logic_4287(agents, world):
    _agent_apply(world, agents, 'hydration', 'hunger', 'direct')

def logic_4288(agents, world):
    _agent_apply(world, agents, 'thirst', 'hunger', 'direct')

def logic_4289(agents, world):
    _agent_apply(world, agents, 'hunger', 'hunger', 'direct')

def logic_4290(agents, world):
    _agent_apply(world, agents, 'health', 'hunger', 'direct')

def logic_4291(agents, world):
    _agent_apply(world, agents, 'stress', 'hunger', 'direct')

def logic_4292(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'hunger', 'direct')

def logic_4293(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'hunger', 'direct')

def logic_4294(agents, world):
    _agent_apply(world, agents, 'social_need', 'hunger', 'direct')

def logic_4295(agents, world):
    _agent_apply(world, agents, 'cooperation', 'hunger', 'direct')

def logic_4296(agents, world):
    _agent_apply(world, agents, 'defection', 'hunger', 'direct')

def logic_4297(agents, world):
    _agent_apply(world, agents, 'trust', 'hunger', 'direct')

def logic_4298(agents, world):
    _agent_apply(world, agents, 'reputation', 'hunger', 'direct')

def logic_4299(agents, world):
    _agent_apply(world, agents, 'help_received', 'hunger', 'direct')

def logic_4300(agents, world):
    _agent_apply(world, agents, 'help_given', 'hunger', 'direct')

def logic_4301(agents, world):
    _agent_apply(world, agents, 'local_density', 'hunger', 'direct')

def logic_4302(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'hunger', 'direct')

def logic_4303(agents, world):
    _agent_apply(world, agents, 'survival_score', 'hunger', 'direct')

def logic_4304(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'hunger', 'direct')

def logic_4305(agents, world):
    _agent_apply(world, agents, 'payoff', 'hunger', 'direct')

def logic_4306(agents, world):
    _agent_apply(world, agents, 'temperature', 'health', 'direct')

def logic_4307(agents, world):
    _agent_apply(world, agents, 'surface_water', 'health', 'direct')

def logic_4308(agents, world):
    _agent_apply(world, agents, 'humidity', 'health', 'direct')

def logic_4309(agents, world):
    _agent_apply(world, agents, 'cloud', 'health', 'direct')

def logic_4310(agents, world):
    _agent_apply(world, agents, 'rain', 'health', 'direct')

def logic_4311(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'health', 'direct')

def logic_4312(agents, world):
    _agent_apply(world, agents, 'runoff', 'health', 'direct')

def logic_4313(agents, world):
    _agent_apply(world, agents, 'wind_x', 'health', 'direct')

def logic_4314(agents, world):
    _agent_apply(world, agents, 'wind_y', 'health', 'direct')

def logic_4315(agents, world):
    _agent_apply(world, agents, 'vegetation', 'health', 'direct')

def logic_4316(agents, world):
    _agent_apply(world, agents, 'biomass', 'health', 'direct')

def logic_4317(agents, world):
    _agent_apply(world, agents, 'herbivore', 'health', 'direct')

def logic_4318(agents, world):
    _agent_apply(world, agents, 'predator', 'health', 'direct')

def logic_4319(agents, world):
    _agent_apply(world, agents, 'carrion', 'health', 'direct')

def logic_4320(agents, world):
    _agent_apply(world, agents, 'nutrients', 'health', 'direct')

def logic_4321(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'health', 'direct')

def logic_4322(agents, world):
    _agent_apply(world, agents, 'oxygen', 'health', 'direct')

def logic_4323(agents, world):
    _agent_apply(world, agents, 'co2', 'health', 'direct')

def logic_4324(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'health', 'direct')

def logic_4325(agents, world):
    _agent_apply(world, agents, 'ice', 'health', 'direct')

def logic_4326(agents, world):
    _agent_apply(world, agents, 'evaporation', 'health', 'direct')

def logic_4327(agents, world):
    _agent_apply(world, agents, 'detritus', 'health', 'direct')

def logic_4328(agents, world):
    _agent_apply(world, agents, 'methane', 'health', 'direct')

def logic_4329(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'health', 'direct')

def logic_4330(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'health', 'direct')

def logic_4331(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'health', 'direct')

def logic_4332(agents, world):
    _agent_apply(world, agents, 'erosion', 'health', 'direct')

def logic_4333(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'health', 'direct')

def logic_4334(agents, world):
    _agent_apply(world, agents, 'root_density', 'health', 'direct')

def logic_4335(agents, world):
    _agent_apply(world, agents, 'wetland', 'health', 'direct')

def logic_4336(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'health', 'direct')

def logic_4337(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'health', 'direct')

def logic_4338(agents, world):
    _agent_apply(world, agents, 'ash', 'health', 'direct')

def logic_4339(agents, world):
    _agent_apply(world, agents, 'snowpack', 'health', 'direct')

def logic_4340(agents, world):
    _agent_apply(world, agents, 'groundwater', 'health', 'direct')

def logic_4341(agents, world):
    _agent_apply(world, agents, 'sediment', 'health', 'direct')

def logic_4342(agents, world):
    _agent_apply(world, agents, 'salinity', 'health', 'direct')

def logic_4343(agents, world):
    _agent_apply(world, agents, 'algae', 'health', 'direct')

def logic_4344(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'health', 'direct')

def logic_4345(agents, world):
    _agent_apply(world, agents, 'deadwood', 'health', 'direct')

def logic_4346(agents, world):
    _agent_apply(world, agents, 'pollinators', 'health', 'direct')

def logic_4347(agents, world):
    _agent_apply(world, agents, 'flowers', 'health', 'direct')

def logic_4348(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'health', 'direct')

def logic_4349(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'health', 'direct')

def logic_4350(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'health', 'direct')

def logic_4351(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'health', 'direct')

def logic_4352(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'health', 'direct')

def logic_4353(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'health', 'direct')

def logic_4354(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'health', 'direct')

def logic_4355(agents, world):
    _agent_apply(world, agents, 'hydration', 'health', 'direct')

def logic_4356(agents, world):
    _agent_apply(world, agents, 'thirst', 'health', 'direct')

def logic_4357(agents, world):
    _agent_apply(world, agents, 'hunger', 'health', 'direct')

def logic_4358(agents, world):
    _agent_apply(world, agents, 'health', 'health', 'direct')

def logic_4359(agents, world):
    _agent_apply(world, agents, 'stress', 'health', 'direct')

def logic_4360(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'health', 'direct')

def logic_4361(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'health', 'direct')

def logic_4362(agents, world):
    _agent_apply(world, agents, 'social_need', 'health', 'direct')

def logic_4363(agents, world):
    _agent_apply(world, agents, 'cooperation', 'health', 'direct')

def logic_4364(agents, world):
    _agent_apply(world, agents, 'defection', 'health', 'direct')

def logic_4365(agents, world):
    _agent_apply(world, agents, 'trust', 'health', 'direct')

def logic_4366(agents, world):
    _agent_apply(world, agents, 'reputation', 'health', 'direct')

def logic_4367(agents, world):
    _agent_apply(world, agents, 'help_received', 'health', 'direct')

def logic_4368(agents, world):
    _agent_apply(world, agents, 'help_given', 'health', 'direct')

def logic_4369(agents, world):
    _agent_apply(world, agents, 'local_density', 'health', 'direct')

def logic_4370(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'health', 'direct')

def logic_4371(agents, world):
    _agent_apply(world, agents, 'survival_score', 'health', 'direct')

def logic_4372(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'health', 'direct')

def logic_4373(agents, world):
    _agent_apply(world, agents, 'payoff', 'health', 'direct')

def logic_4374(agents, world):
    _agent_apply(world, agents, 'temperature', 'thermal_stress', 'direct')

def logic_4375(agents, world):
    _agent_apply(world, agents, 'surface_water', 'thermal_stress', 'direct')

def logic_4376(agents, world):
    _agent_apply(world, agents, 'humidity', 'thermal_stress', 'direct')

def logic_4377(agents, world):
    _agent_apply(world, agents, 'cloud', 'thermal_stress', 'direct')

def logic_4378(agents, world):
    _agent_apply(world, agents, 'rain', 'thermal_stress', 'direct')

def logic_4379(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'thermal_stress', 'direct')

def logic_4380(agents, world):
    _agent_apply(world, agents, 'runoff', 'thermal_stress', 'direct')

def logic_4381(agents, world):
    _agent_apply(world, agents, 'wind_x', 'thermal_stress', 'direct')

def logic_4382(agents, world):
    _agent_apply(world, agents, 'wind_y', 'thermal_stress', 'direct')

def logic_4383(agents, world):
    _agent_apply(world, agents, 'vegetation', 'thermal_stress', 'direct')

def logic_4384(agents, world):
    _agent_apply(world, agents, 'biomass', 'thermal_stress', 'direct')

def logic_4385(agents, world):
    _agent_apply(world, agents, 'herbivore', 'thermal_stress', 'direct')

def logic_4386(agents, world):
    _agent_apply(world, agents, 'predator', 'thermal_stress', 'direct')

def logic_4387(agents, world):
    _agent_apply(world, agents, 'carrion', 'thermal_stress', 'direct')

def logic_4388(agents, world):
    _agent_apply(world, agents, 'nutrients', 'thermal_stress', 'direct')

def logic_4389(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'thermal_stress', 'direct')

def logic_4390(agents, world):
    _agent_apply(world, agents, 'oxygen', 'thermal_stress', 'direct')

def logic_4391(agents, world):
    _agent_apply(world, agents, 'co2', 'thermal_stress', 'direct')

def logic_4392(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'thermal_stress', 'direct')

def logic_4393(agents, world):
    _agent_apply(world, agents, 'ice', 'thermal_stress', 'direct')

def logic_4394(agents, world):
    _agent_apply(world, agents, 'evaporation', 'thermal_stress', 'direct')

def logic_4395(agents, world):
    _agent_apply(world, agents, 'detritus', 'thermal_stress', 'direct')

def logic_4396(agents, world):
    _agent_apply(world, agents, 'methane', 'thermal_stress', 'direct')

def logic_4397(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'thermal_stress', 'direct')

def logic_4398(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'thermal_stress', 'direct')

def logic_4399(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'thermal_stress', 'direct')

def logic_4400(agents, world):
    _agent_apply(world, agents, 'erosion', 'thermal_stress', 'direct')

def logic_4401(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'thermal_stress', 'direct')

def logic_4402(agents, world):
    _agent_apply(world, agents, 'root_density', 'thermal_stress', 'direct')

def logic_4403(agents, world):
    _agent_apply(world, agents, 'wetland', 'thermal_stress', 'direct')

def logic_4404(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'thermal_stress', 'direct')

def logic_4405(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'thermal_stress', 'direct')

def logic_4406(agents, world):
    _agent_apply(world, agents, 'ash', 'thermal_stress', 'direct')

def logic_4407(agents, world):
    _agent_apply(world, agents, 'snowpack', 'thermal_stress', 'direct')

def logic_4408(agents, world):
    _agent_apply(world, agents, 'groundwater', 'thermal_stress', 'direct')

def logic_4409(agents, world):
    _agent_apply(world, agents, 'sediment', 'thermal_stress', 'direct')

def logic_4410(agents, world):
    _agent_apply(world, agents, 'salinity', 'thermal_stress', 'direct')

def logic_4411(agents, world):
    _agent_apply(world, agents, 'algae', 'thermal_stress', 'direct')

def logic_4412(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'thermal_stress', 'direct')

def logic_4413(agents, world):
    _agent_apply(world, agents, 'deadwood', 'thermal_stress', 'direct')

def logic_4414(agents, world):
    _agent_apply(world, agents, 'pollinators', 'thermal_stress', 'direct')

def logic_4415(agents, world):
    _agent_apply(world, agents, 'flowers', 'thermal_stress', 'direct')

def logic_4416(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'thermal_stress', 'direct')

def logic_4417(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'thermal_stress', 'direct')

def logic_4418(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'thermal_stress', 'direct')

def logic_4419(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'thermal_stress', 'direct')

def logic_4420(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'thermal_stress', 'direct')

def logic_4421(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'thermal_stress', 'direct')

def logic_4422(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'thermal_stress', 'direct')

def logic_4423(agents, world):
    _agent_apply(world, agents, 'hydration', 'thermal_stress', 'direct')

def logic_4424(agents, world):
    _agent_apply(world, agents, 'thirst', 'thermal_stress', 'direct')

def logic_4425(agents, world):
    _agent_apply(world, agents, 'hunger', 'thermal_stress', 'direct')

def logic_4426(agents, world):
    _agent_apply(world, agents, 'health', 'thermal_stress', 'direct')

def logic_4427(agents, world):
    _agent_apply(world, agents, 'stress', 'thermal_stress', 'direct')

def logic_4428(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'thermal_stress', 'direct')

def logic_4429(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'thermal_stress', 'direct')

def logic_4430(agents, world):
    _agent_apply(world, agents, 'social_need', 'thermal_stress', 'direct')

def logic_4431(agents, world):
    _agent_apply(world, agents, 'cooperation', 'thermal_stress', 'direct')

def logic_4432(agents, world):
    _agent_apply(world, agents, 'defection', 'thermal_stress', 'direct')

def logic_4433(agents, world):
    _agent_apply(world, agents, 'trust', 'thermal_stress', 'direct')

def logic_4434(agents, world):
    _agent_apply(world, agents, 'reputation', 'thermal_stress', 'direct')

def logic_4435(agents, world):
    _agent_apply(world, agents, 'help_received', 'thermal_stress', 'direct')

def logic_4436(agents, world):
    _agent_apply(world, agents, 'help_given', 'thermal_stress', 'direct')

def logic_4437(agents, world):
    _agent_apply(world, agents, 'local_density', 'thermal_stress', 'direct')

def logic_4438(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'thermal_stress', 'direct')

def logic_4439(agents, world):
    _agent_apply(world, agents, 'survival_score', 'thermal_stress', 'direct')

def logic_4440(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'thermal_stress', 'direct')

def logic_4441(agents, world):
    _agent_apply(world, agents, 'payoff', 'thermal_stress', 'direct')

def logic_4442(agents, world):
    _agent_apply(world, agents, 'temperature', 'dehydration', 'direct')

def logic_4443(agents, world):
    _agent_apply(world, agents, 'surface_water', 'dehydration', 'direct')

def logic_4444(agents, world):
    _agent_apply(world, agents, 'humidity', 'dehydration', 'direct')

def logic_4445(agents, world):
    _agent_apply(world, agents, 'cloud', 'dehydration', 'direct')

def logic_4446(agents, world):
    _agent_apply(world, agents, 'rain', 'dehydration', 'direct')

def logic_4447(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'dehydration', 'direct')

def logic_4448(agents, world):
    _agent_apply(world, agents, 'runoff', 'dehydration', 'direct')

def logic_4449(agents, world):
    _agent_apply(world, agents, 'wind_x', 'dehydration', 'direct')

def logic_4450(agents, world):
    _agent_apply(world, agents, 'wind_y', 'dehydration', 'direct')

def logic_4451(agents, world):
    _agent_apply(world, agents, 'vegetation', 'dehydration', 'direct')

def logic_4452(agents, world):
    _agent_apply(world, agents, 'biomass', 'dehydration', 'direct')

def logic_4453(agents, world):
    _agent_apply(world, agents, 'herbivore', 'dehydration', 'direct')

def logic_4454(agents, world):
    _agent_apply(world, agents, 'predator', 'dehydration', 'direct')

def logic_4455(agents, world):
    _agent_apply(world, agents, 'carrion', 'dehydration', 'direct')

def logic_4456(agents, world):
    _agent_apply(world, agents, 'nutrients', 'dehydration', 'direct')

def logic_4457(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'dehydration', 'direct')

def logic_4458(agents, world):
    _agent_apply(world, agents, 'oxygen', 'dehydration', 'direct')

def logic_4459(agents, world):
    _agent_apply(world, agents, 'co2', 'dehydration', 'direct')

def logic_4460(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'dehydration', 'direct')

def logic_4461(agents, world):
    _agent_apply(world, agents, 'ice', 'dehydration', 'direct')

def logic_4462(agents, world):
    _agent_apply(world, agents, 'evaporation', 'dehydration', 'direct')

def logic_4463(agents, world):
    _agent_apply(world, agents, 'detritus', 'dehydration', 'direct')

def logic_4464(agents, world):
    _agent_apply(world, agents, 'methane', 'dehydration', 'direct')

def logic_4465(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'dehydration', 'direct')

def logic_4466(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'dehydration', 'direct')

def logic_4467(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'dehydration', 'direct')

def logic_4468(agents, world):
    _agent_apply(world, agents, 'erosion', 'dehydration', 'direct')

def logic_4469(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'dehydration', 'direct')

def logic_4470(agents, world):
    _agent_apply(world, agents, 'root_density', 'dehydration', 'direct')

def logic_4471(agents, world):
    _agent_apply(world, agents, 'wetland', 'dehydration', 'direct')

def logic_4472(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'dehydration', 'direct')

def logic_4473(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'dehydration', 'direct')

def logic_4474(agents, world):
    _agent_apply(world, agents, 'ash', 'dehydration', 'direct')

def logic_4475(agents, world):
    _agent_apply(world, agents, 'snowpack', 'dehydration', 'direct')

def logic_4476(agents, world):
    _agent_apply(world, agents, 'groundwater', 'dehydration', 'direct')

def logic_4477(agents, world):
    _agent_apply(world, agents, 'sediment', 'dehydration', 'direct')

def logic_4478(agents, world):
    _agent_apply(world, agents, 'salinity', 'dehydration', 'direct')

def logic_4479(agents, world):
    _agent_apply(world, agents, 'algae', 'dehydration', 'direct')

def logic_4480(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'dehydration', 'direct')

def logic_4481(agents, world):
    _agent_apply(world, agents, 'deadwood', 'dehydration', 'direct')

def logic_4482(agents, world):
    _agent_apply(world, agents, 'pollinators', 'dehydration', 'direct')

def logic_4483(agents, world):
    _agent_apply(world, agents, 'flowers', 'dehydration', 'direct')

def logic_4484(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'dehydration', 'direct')

def logic_4485(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'dehydration', 'direct')

def logic_4486(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'dehydration', 'direct')

def logic_4487(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'dehydration', 'direct')

def logic_4488(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'dehydration', 'direct')

def logic_4489(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'dehydration', 'direct')

def logic_4490(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'dehydration', 'direct')

def logic_4491(agents, world):
    _agent_apply(world, agents, 'hydration', 'dehydration', 'direct')

def logic_4492(agents, world):
    _agent_apply(world, agents, 'thirst', 'dehydration', 'direct')

def logic_4493(agents, world):
    _agent_apply(world, agents, 'hunger', 'dehydration', 'direct')

def logic_4494(agents, world):
    _agent_apply(world, agents, 'health', 'dehydration', 'direct')

def logic_4495(agents, world):
    _agent_apply(world, agents, 'stress', 'dehydration', 'direct')

def logic_4496(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'dehydration', 'direct')

def logic_4497(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'dehydration', 'direct')

def logic_4498(agents, world):
    _agent_apply(world, agents, 'social_need', 'dehydration', 'direct')

def logic_4499(agents, world):
    _agent_apply(world, agents, 'cooperation', 'dehydration', 'direct')

def logic_4500(agents, world):
    _agent_apply(world, agents, 'defection', 'dehydration', 'direct')

def logic_4501(agents, world):
    _agent_apply(world, agents, 'trust', 'dehydration', 'direct')

def logic_4502(agents, world):
    _agent_apply(world, agents, 'reputation', 'dehydration', 'direct')

def logic_4503(agents, world):
    _agent_apply(world, agents, 'help_received', 'dehydration', 'direct')

def logic_4504(agents, world):
    _agent_apply(world, agents, 'help_given', 'dehydration', 'direct')

def logic_4505(agents, world):
    _agent_apply(world, agents, 'local_density', 'dehydration', 'direct')

def logic_4506(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'dehydration', 'direct')

def logic_4507(agents, world):
    _agent_apply(world, agents, 'survival_score', 'dehydration', 'direct')

def logic_4508(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'dehydration', 'direct')

def logic_4509(agents, world):
    _agent_apply(world, agents, 'payoff', 'dehydration', 'direct')

def logic_4510(agents, world):
    _agent_apply(world, agents, 'temperature', 'pathogen_risk', 'direct')

def logic_4511(agents, world):
    _agent_apply(world, agents, 'surface_water', 'pathogen_risk', 'direct')

def logic_4512(agents, world):
    _agent_apply(world, agents, 'humidity', 'pathogen_risk', 'direct')

def logic_4513(agents, world):
    _agent_apply(world, agents, 'cloud', 'pathogen_risk', 'direct')

def logic_4514(agents, world):
    _agent_apply(world, agents, 'rain', 'pathogen_risk', 'direct')

def logic_4515(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'pathogen_risk', 'direct')

def logic_4516(agents, world):
    _agent_apply(world, agents, 'runoff', 'pathogen_risk', 'direct')

def logic_4517(agents, world):
    _agent_apply(world, agents, 'wind_x', 'pathogen_risk', 'direct')

def logic_4518(agents, world):
    _agent_apply(world, agents, 'wind_y', 'pathogen_risk', 'direct')

def logic_4519(agents, world):
    _agent_apply(world, agents, 'vegetation', 'pathogen_risk', 'direct')

def logic_4520(agents, world):
    _agent_apply(world, agents, 'biomass', 'pathogen_risk', 'direct')

def logic_4521(agents, world):
    _agent_apply(world, agents, 'herbivore', 'pathogen_risk', 'direct')

def logic_4522(agents, world):
    _agent_apply(world, agents, 'predator', 'pathogen_risk', 'direct')

def logic_4523(agents, world):
    _agent_apply(world, agents, 'carrion', 'pathogen_risk', 'direct')

def logic_4524(agents, world):
    _agent_apply(world, agents, 'nutrients', 'pathogen_risk', 'direct')

def logic_4525(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'pathogen_risk', 'direct')

def logic_4526(agents, world):
    _agent_apply(world, agents, 'oxygen', 'pathogen_risk', 'direct')

def logic_4527(agents, world):
    _agent_apply(world, agents, 'co2', 'pathogen_risk', 'direct')

def logic_4528(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'pathogen_risk', 'direct')

def logic_4529(agents, world):
    _agent_apply(world, agents, 'ice', 'pathogen_risk', 'direct')

def logic_4530(agents, world):
    _agent_apply(world, agents, 'evaporation', 'pathogen_risk', 'direct')

def logic_4531(agents, world):
    _agent_apply(world, agents, 'detritus', 'pathogen_risk', 'direct')

def logic_4532(agents, world):
    _agent_apply(world, agents, 'methane', 'pathogen_risk', 'direct')

def logic_4533(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'pathogen_risk', 'direct')

def logic_4534(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'pathogen_risk', 'direct')

def logic_4535(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'pathogen_risk', 'direct')

def logic_4536(agents, world):
    _agent_apply(world, agents, 'erosion', 'pathogen_risk', 'direct')

def logic_4537(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'pathogen_risk', 'direct')

def logic_4538(agents, world):
    _agent_apply(world, agents, 'root_density', 'pathogen_risk', 'direct')

def logic_4539(agents, world):
    _agent_apply(world, agents, 'wetland', 'pathogen_risk', 'direct')

def logic_4540(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'pathogen_risk', 'direct')

def logic_4541(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'pathogen_risk', 'direct')

def logic_4542(agents, world):
    _agent_apply(world, agents, 'ash', 'pathogen_risk', 'direct')

def logic_4543(agents, world):
    _agent_apply(world, agents, 'snowpack', 'pathogen_risk', 'direct')

def logic_4544(agents, world):
    _agent_apply(world, agents, 'groundwater', 'pathogen_risk', 'direct')

def logic_4545(agents, world):
    _agent_apply(world, agents, 'sediment', 'pathogen_risk', 'direct')

def logic_4546(agents, world):
    _agent_apply(world, agents, 'salinity', 'pathogen_risk', 'direct')

def logic_4547(agents, world):
    _agent_apply(world, agents, 'algae', 'pathogen_risk', 'direct')

def logic_4548(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'pathogen_risk', 'direct')

def logic_4549(agents, world):
    _agent_apply(world, agents, 'deadwood', 'pathogen_risk', 'direct')

def logic_4550(agents, world):
    _agent_apply(world, agents, 'pollinators', 'pathogen_risk', 'direct')

def logic_4551(agents, world):
    _agent_apply(world, agents, 'flowers', 'pathogen_risk', 'direct')

def logic_4552(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'pathogen_risk', 'direct')

def logic_4553(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'pathogen_risk', 'direct')

def logic_4554(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'pathogen_risk', 'direct')

def logic_4555(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'pathogen_risk', 'direct')

def logic_4556(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'pathogen_risk', 'direct')

def logic_4557(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'pathogen_risk', 'direct')

def logic_4558(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'pathogen_risk', 'direct')

def logic_4559(agents, world):
    _agent_apply(world, agents, 'hydration', 'pathogen_risk', 'direct')

def logic_4560(agents, world):
    _agent_apply(world, agents, 'thirst', 'pathogen_risk', 'direct')

def logic_4561(agents, world):
    _agent_apply(world, agents, 'hunger', 'pathogen_risk', 'direct')

def logic_4562(agents, world):
    _agent_apply(world, agents, 'health', 'pathogen_risk', 'direct')

def logic_4563(agents, world):
    _agent_apply(world, agents, 'stress', 'pathogen_risk', 'direct')

def logic_4564(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'pathogen_risk', 'direct')

def logic_4565(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'pathogen_risk', 'direct')

def logic_4566(agents, world):
    _agent_apply(world, agents, 'social_need', 'pathogen_risk', 'direct')

def logic_4567(agents, world):
    _agent_apply(world, agents, 'cooperation', 'pathogen_risk', 'direct')

def logic_4568(agents, world):
    _agent_apply(world, agents, 'defection', 'pathogen_risk', 'direct')

def logic_4569(agents, world):
    _agent_apply(world, agents, 'trust', 'pathogen_risk', 'direct')

def logic_4570(agents, world):
    _agent_apply(world, agents, 'reputation', 'pathogen_risk', 'direct')

def logic_4571(agents, world):
    _agent_apply(world, agents, 'help_received', 'pathogen_risk', 'direct')

def logic_4572(agents, world):
    _agent_apply(world, agents, 'help_given', 'pathogen_risk', 'direct')

def logic_4573(agents, world):
    _agent_apply(world, agents, 'local_density', 'pathogen_risk', 'direct')

def logic_4574(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'pathogen_risk', 'direct')

def logic_4575(agents, world):
    _agent_apply(world, agents, 'survival_score', 'pathogen_risk', 'direct')

def logic_4576(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'pathogen_risk', 'direct')

def logic_4577(agents, world):
    _agent_apply(world, agents, 'payoff', 'pathogen_risk', 'direct')

def logic_4578(agents, world):
    _agent_apply(world, agents, 'temperature', 'infection_risk', 'direct')

def logic_4579(agents, world):
    _agent_apply(world, agents, 'surface_water', 'infection_risk', 'direct')

def logic_4580(agents, world):
    _agent_apply(world, agents, 'humidity', 'infection_risk', 'direct')

def logic_4581(agents, world):
    _agent_apply(world, agents, 'cloud', 'infection_risk', 'direct')

def logic_4582(agents, world):
    _agent_apply(world, agents, 'rain', 'infection_risk', 'direct')

def logic_4583(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'infection_risk', 'direct')

def logic_4584(agents, world):
    _agent_apply(world, agents, 'runoff', 'infection_risk', 'direct')

def logic_4585(agents, world):
    _agent_apply(world, agents, 'wind_x', 'infection_risk', 'direct')

def logic_4586(agents, world):
    _agent_apply(world, agents, 'wind_y', 'infection_risk', 'direct')

def logic_4587(agents, world):
    _agent_apply(world, agents, 'vegetation', 'infection_risk', 'direct')

def logic_4588(agents, world):
    _agent_apply(world, agents, 'biomass', 'infection_risk', 'direct')

def logic_4589(agents, world):
    _agent_apply(world, agents, 'herbivore', 'infection_risk', 'direct')

def logic_4590(agents, world):
    _agent_apply(world, agents, 'predator', 'infection_risk', 'direct')

def logic_4591(agents, world):
    _agent_apply(world, agents, 'carrion', 'infection_risk', 'direct')

def logic_4592(agents, world):
    _agent_apply(world, agents, 'nutrients', 'infection_risk', 'direct')

def logic_4593(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'infection_risk', 'direct')

def logic_4594(agents, world):
    _agent_apply(world, agents, 'oxygen', 'infection_risk', 'direct')

def logic_4595(agents, world):
    _agent_apply(world, agents, 'co2', 'infection_risk', 'direct')

def logic_4596(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'infection_risk', 'direct')

def logic_4597(agents, world):
    _agent_apply(world, agents, 'ice', 'infection_risk', 'direct')

def logic_4598(agents, world):
    _agent_apply(world, agents, 'evaporation', 'infection_risk', 'direct')

def logic_4599(agents, world):
    _agent_apply(world, agents, 'detritus', 'infection_risk', 'direct')

def logic_4600(agents, world):
    _agent_apply(world, agents, 'methane', 'infection_risk', 'direct')

def logic_4601(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'infection_risk', 'direct')

def logic_4602(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'infection_risk', 'direct')

def logic_4603(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'infection_risk', 'direct')

def logic_4604(agents, world):
    _agent_apply(world, agents, 'erosion', 'infection_risk', 'direct')

def logic_4605(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'infection_risk', 'direct')

def logic_4606(agents, world):
    _agent_apply(world, agents, 'root_density', 'infection_risk', 'direct')

def logic_4607(agents, world):
    _agent_apply(world, agents, 'wetland', 'infection_risk', 'direct')

def logic_4608(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'infection_risk', 'direct')

def logic_4609(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'infection_risk', 'direct')

def logic_4610(agents, world):
    _agent_apply(world, agents, 'ash', 'infection_risk', 'direct')

def logic_4611(agents, world):
    _agent_apply(world, agents, 'snowpack', 'infection_risk', 'direct')

def logic_4612(agents, world):
    _agent_apply(world, agents, 'groundwater', 'infection_risk', 'direct')

def logic_4613(agents, world):
    _agent_apply(world, agents, 'sediment', 'infection_risk', 'direct')

def logic_4614(agents, world):
    _agent_apply(world, agents, 'salinity', 'infection_risk', 'direct')

def logic_4615(agents, world):
    _agent_apply(world, agents, 'algae', 'infection_risk', 'direct')

def logic_4616(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'infection_risk', 'direct')

def logic_4617(agents, world):
    _agent_apply(world, agents, 'deadwood', 'infection_risk', 'direct')

def logic_4618(agents, world):
    _agent_apply(world, agents, 'pollinators', 'infection_risk', 'direct')

def logic_4619(agents, world):
    _agent_apply(world, agents, 'flowers', 'infection_risk', 'direct')

def logic_4620(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'infection_risk', 'direct')

def logic_4621(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'infection_risk', 'direct')

def logic_4622(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'infection_risk', 'direct')

def logic_4623(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'infection_risk', 'direct')

def logic_4624(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'infection_risk', 'direct')

def logic_4625(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'infection_risk', 'direct')

def logic_4626(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'infection_risk', 'direct')

def logic_4627(agents, world):
    _agent_apply(world, agents, 'hydration', 'infection_risk', 'direct')

def logic_4628(agents, world):
    _agent_apply(world, agents, 'thirst', 'infection_risk', 'direct')

def logic_4629(agents, world):
    _agent_apply(world, agents, 'hunger', 'infection_risk', 'direct')

def logic_4630(agents, world):
    _agent_apply(world, agents, 'health', 'infection_risk', 'direct')

def logic_4631(agents, world):
    _agent_apply(world, agents, 'stress', 'infection_risk', 'direct')

def logic_4632(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'infection_risk', 'direct')

def logic_4633(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'infection_risk', 'direct')

def logic_4634(agents, world):
    _agent_apply(world, agents, 'social_need', 'infection_risk', 'direct')

def logic_4635(agents, world):
    _agent_apply(world, agents, 'cooperation', 'infection_risk', 'direct')

def logic_4636(agents, world):
    _agent_apply(world, agents, 'defection', 'infection_risk', 'direct')

def logic_4637(agents, world):
    _agent_apply(world, agents, 'trust', 'infection_risk', 'direct')

def logic_4638(agents, world):
    _agent_apply(world, agents, 'reputation', 'infection_risk', 'direct')

def logic_4639(agents, world):
    _agent_apply(world, agents, 'help_received', 'infection_risk', 'direct')

def logic_4640(agents, world):
    _agent_apply(world, agents, 'help_given', 'infection_risk', 'direct')

def logic_4641(agents, world):
    _agent_apply(world, agents, 'local_density', 'infection_risk', 'direct')

def logic_4642(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'infection_risk', 'direct')

def logic_4643(agents, world):
    _agent_apply(world, agents, 'survival_score', 'infection_risk', 'direct')

def logic_4644(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'infection_risk', 'direct')

def logic_4645(agents, world):
    _agent_apply(world, agents, 'payoff', 'infection_risk', 'direct')

def logic_4646(agents, world):
    _agent_apply(world, agents, 'temperature', 'alertness', 'direct')

def logic_4647(agents, world):
    _agent_apply(world, agents, 'surface_water', 'alertness', 'direct')

def logic_4648(agents, world):
    _agent_apply(world, agents, 'humidity', 'alertness', 'direct')

def logic_4649(agents, world):
    _agent_apply(world, agents, 'cloud', 'alertness', 'direct')

def logic_4650(agents, world):
    _agent_apply(world, agents, 'rain', 'alertness', 'direct')

def logic_4651(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'alertness', 'direct')

def logic_4652(agents, world):
    _agent_apply(world, agents, 'runoff', 'alertness', 'direct')

def logic_4653(agents, world):
    _agent_apply(world, agents, 'wind_x', 'alertness', 'direct')

def logic_4654(agents, world):
    _agent_apply(world, agents, 'wind_y', 'alertness', 'direct')

def logic_4655(agents, world):
    _agent_apply(world, agents, 'vegetation', 'alertness', 'direct')

def logic_4656(agents, world):
    _agent_apply(world, agents, 'biomass', 'alertness', 'direct')

def logic_4657(agents, world):
    _agent_apply(world, agents, 'herbivore', 'alertness', 'direct')

def logic_4658(agents, world):
    _agent_apply(world, agents, 'predator', 'alertness', 'direct')

def logic_4659(agents, world):
    _agent_apply(world, agents, 'carrion', 'alertness', 'direct')

def logic_4660(agents, world):
    _agent_apply(world, agents, 'nutrients', 'alertness', 'direct')

def logic_4661(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'alertness', 'direct')

def logic_4662(agents, world):
    _agent_apply(world, agents, 'oxygen', 'alertness', 'direct')

def logic_4663(agents, world):
    _agent_apply(world, agents, 'co2', 'alertness', 'direct')

def logic_4664(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'alertness', 'direct')

def logic_4665(agents, world):
    _agent_apply(world, agents, 'ice', 'alertness', 'direct')

def logic_4666(agents, world):
    _agent_apply(world, agents, 'evaporation', 'alertness', 'direct')

def logic_4667(agents, world):
    _agent_apply(world, agents, 'detritus', 'alertness', 'direct')

def logic_4668(agents, world):
    _agent_apply(world, agents, 'methane', 'alertness', 'direct')

def logic_4669(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'alertness', 'direct')

def logic_4670(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'alertness', 'direct')

def logic_4671(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'alertness', 'direct')

def logic_4672(agents, world):
    _agent_apply(world, agents, 'erosion', 'alertness', 'direct')

def logic_4673(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'alertness', 'direct')

def logic_4674(agents, world):
    _agent_apply(world, agents, 'root_density', 'alertness', 'direct')

def logic_4675(agents, world):
    _agent_apply(world, agents, 'wetland', 'alertness', 'direct')

def logic_4676(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'alertness', 'direct')

def logic_4677(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'alertness', 'direct')

def logic_4678(agents, world):
    _agent_apply(world, agents, 'ash', 'alertness', 'direct')

def logic_4679(agents, world):
    _agent_apply(world, agents, 'snowpack', 'alertness', 'direct')

def logic_4680(agents, world):
    _agent_apply(world, agents, 'groundwater', 'alertness', 'direct')

def logic_4681(agents, world):
    _agent_apply(world, agents, 'sediment', 'alertness', 'direct')

def logic_4682(agents, world):
    _agent_apply(world, agents, 'salinity', 'alertness', 'direct')

def logic_4683(agents, world):
    _agent_apply(world, agents, 'algae', 'alertness', 'direct')

def logic_4684(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'alertness', 'direct')

def logic_4685(agents, world):
    _agent_apply(world, agents, 'deadwood', 'alertness', 'direct')

def logic_4686(agents, world):
    _agent_apply(world, agents, 'pollinators', 'alertness', 'direct')

def logic_4687(agents, world):
    _agent_apply(world, agents, 'flowers', 'alertness', 'direct')

def logic_4688(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'alertness', 'direct')

def logic_4689(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'alertness', 'direct')

def logic_4690(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'alertness', 'direct')

def logic_4691(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'alertness', 'direct')

def logic_4692(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'alertness', 'direct')

def logic_4693(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'alertness', 'direct')

def logic_4694(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'alertness', 'direct')

def logic_4695(agents, world):
    _agent_apply(world, agents, 'hydration', 'alertness', 'direct')

def logic_4696(agents, world):
    _agent_apply(world, agents, 'thirst', 'alertness', 'direct')

def logic_4697(agents, world):
    _agent_apply(world, agents, 'hunger', 'alertness', 'direct')

def logic_4698(agents, world):
    _agent_apply(world, agents, 'health', 'alertness', 'direct')

def logic_4699(agents, world):
    _agent_apply(world, agents, 'stress', 'alertness', 'direct')

def logic_4700(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'alertness', 'direct')

def logic_4701(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'alertness', 'direct')

def logic_4702(agents, world):
    _agent_apply(world, agents, 'social_need', 'alertness', 'direct')

def logic_4703(agents, world):
    _agent_apply(world, agents, 'cooperation', 'alertness', 'direct')

def logic_4704(agents, world):
    _agent_apply(world, agents, 'defection', 'alertness', 'direct')

def logic_4705(agents, world):
    _agent_apply(world, agents, 'trust', 'alertness', 'direct')

def logic_4706(agents, world):
    _agent_apply(world, agents, 'reputation', 'alertness', 'direct')

def logic_4707(agents, world):
    _agent_apply(world, agents, 'help_received', 'alertness', 'direct')

def logic_4708(agents, world):
    _agent_apply(world, agents, 'help_given', 'alertness', 'direct')

def logic_4709(agents, world):
    _agent_apply(world, agents, 'local_density', 'alertness', 'direct')

def logic_4710(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'alertness', 'direct')

def logic_4711(agents, world):
    _agent_apply(world, agents, 'survival_score', 'alertness', 'direct')

def logic_4712(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'alertness', 'direct')

def logic_4713(agents, world):
    _agent_apply(world, agents, 'payoff', 'alertness', 'direct')

def logic_4714(agents, world):
    _agent_apply(world, agents, 'temperature', 'fear', 'direct')

def logic_4715(agents, world):
    _agent_apply(world, agents, 'surface_water', 'fear', 'direct')

def logic_4716(agents, world):
    _agent_apply(world, agents, 'humidity', 'fear', 'direct')

def logic_4717(agents, world):
    _agent_apply(world, agents, 'cloud', 'fear', 'direct')

def logic_4718(agents, world):
    _agent_apply(world, agents, 'rain', 'fear', 'direct')

def logic_4719(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'fear', 'direct')

def logic_4720(agents, world):
    _agent_apply(world, agents, 'runoff', 'fear', 'direct')

def logic_4721(agents, world):
    _agent_apply(world, agents, 'wind_x', 'fear', 'direct')

def logic_4722(agents, world):
    _agent_apply(world, agents, 'wind_y', 'fear', 'direct')

def logic_4723(agents, world):
    _agent_apply(world, agents, 'vegetation', 'fear', 'direct')

def logic_4724(agents, world):
    _agent_apply(world, agents, 'biomass', 'fear', 'direct')

def logic_4725(agents, world):
    _agent_apply(world, agents, 'herbivore', 'fear', 'direct')

def logic_4726(agents, world):
    _agent_apply(world, agents, 'predator', 'fear', 'direct')

def logic_4727(agents, world):
    _agent_apply(world, agents, 'carrion', 'fear', 'direct')

def logic_4728(agents, world):
    _agent_apply(world, agents, 'nutrients', 'fear', 'direct')

def logic_4729(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'fear', 'direct')

def logic_4730(agents, world):
    _agent_apply(world, agents, 'oxygen', 'fear', 'direct')

def logic_4731(agents, world):
    _agent_apply(world, agents, 'co2', 'fear', 'direct')

def logic_4732(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'fear', 'direct')

def logic_4733(agents, world):
    _agent_apply(world, agents, 'ice', 'fear', 'direct')

def logic_4734(agents, world):
    _agent_apply(world, agents, 'evaporation', 'fear', 'direct')

def logic_4735(agents, world):
    _agent_apply(world, agents, 'detritus', 'fear', 'direct')

def logic_4736(agents, world):
    _agent_apply(world, agents, 'methane', 'fear', 'direct')

def logic_4737(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'fear', 'direct')

def logic_4738(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'fear', 'direct')

def logic_4739(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'fear', 'direct')

def logic_4740(agents, world):
    _agent_apply(world, agents, 'erosion', 'fear', 'direct')

def logic_4741(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'fear', 'direct')

def logic_4742(agents, world):
    _agent_apply(world, agents, 'root_density', 'fear', 'direct')

def logic_4743(agents, world):
    _agent_apply(world, agents, 'wetland', 'fear', 'direct')

def logic_4744(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'fear', 'direct')

def logic_4745(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'fear', 'direct')

def logic_4746(agents, world):
    _agent_apply(world, agents, 'ash', 'fear', 'direct')

def logic_4747(agents, world):
    _agent_apply(world, agents, 'snowpack', 'fear', 'direct')

def logic_4748(agents, world):
    _agent_apply(world, agents, 'groundwater', 'fear', 'direct')

def logic_4749(agents, world):
    _agent_apply(world, agents, 'sediment', 'fear', 'direct')

def logic_4750(agents, world):
    _agent_apply(world, agents, 'salinity', 'fear', 'direct')

def logic_4751(agents, world):
    _agent_apply(world, agents, 'algae', 'fear', 'direct')

def logic_4752(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'fear', 'direct')

def logic_4753(agents, world):
    _agent_apply(world, agents, 'deadwood', 'fear', 'direct')

def logic_4754(agents, world):
    _agent_apply(world, agents, 'pollinators', 'fear', 'direct')

def logic_4755(agents, world):
    _agent_apply(world, agents, 'flowers', 'fear', 'direct')

def logic_4756(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'fear', 'direct')

def logic_4757(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'fear', 'direct')

def logic_4758(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'fear', 'direct')

def logic_4759(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'fear', 'direct')

def logic_4760(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'fear', 'direct')

def logic_4761(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'fear', 'direct')

def logic_4762(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'fear', 'direct')

def logic_4763(agents, world):
    _agent_apply(world, agents, 'hydration', 'fear', 'direct')

def logic_4764(agents, world):
    _agent_apply(world, agents, 'thirst', 'fear', 'direct')

def logic_4765(agents, world):
    _agent_apply(world, agents, 'hunger', 'fear', 'direct')

def logic_4766(agents, world):
    _agent_apply(world, agents, 'health', 'fear', 'direct')

def logic_4767(agents, world):
    _agent_apply(world, agents, 'stress', 'fear', 'direct')

def logic_4768(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'fear', 'direct')

def logic_4769(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'fear', 'direct')

def logic_4770(agents, world):
    _agent_apply(world, agents, 'social_need', 'fear', 'direct')

def logic_4771(agents, world):
    _agent_apply(world, agents, 'cooperation', 'fear', 'direct')

def logic_4772(agents, world):
    _agent_apply(world, agents, 'defection', 'fear', 'direct')

def logic_4773(agents, world):
    _agent_apply(world, agents, 'trust', 'fear', 'direct')

def logic_4774(agents, world):
    _agent_apply(world, agents, 'reputation', 'fear', 'direct')

def logic_4775(agents, world):
    _agent_apply(world, agents, 'help_received', 'fear', 'direct')

def logic_4776(agents, world):
    _agent_apply(world, agents, 'help_given', 'fear', 'direct')

def logic_4777(agents, world):
    _agent_apply(world, agents, 'local_density', 'fear', 'direct')

def logic_4778(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'fear', 'direct')

def logic_4779(agents, world):
    _agent_apply(world, agents, 'survival_score', 'fear', 'direct')

def logic_4780(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'fear', 'direct')

def logic_4781(agents, world):
    _agent_apply(world, agents, 'payoff', 'fear', 'direct')

def logic_4782(agents, world):
    _agent_apply(world, agents, 'temperature', 'recovery', 'direct')

def logic_4783(agents, world):
    _agent_apply(world, agents, 'surface_water', 'recovery', 'direct')

def logic_4784(agents, world):
    _agent_apply(world, agents, 'humidity', 'recovery', 'direct')

def logic_4785(agents, world):
    _agent_apply(world, agents, 'cloud', 'recovery', 'direct')

def logic_4786(agents, world):
    _agent_apply(world, agents, 'rain', 'recovery', 'direct')

def logic_4787(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'recovery', 'direct')

def logic_4788(agents, world):
    _agent_apply(world, agents, 'runoff', 'recovery', 'direct')

def logic_4789(agents, world):
    _agent_apply(world, agents, 'wind_x', 'recovery', 'direct')

def logic_4790(agents, world):
    _agent_apply(world, agents, 'wind_y', 'recovery', 'direct')

def logic_4791(agents, world):
    _agent_apply(world, agents, 'vegetation', 'recovery', 'direct')

def logic_4792(agents, world):
    _agent_apply(world, agents, 'biomass', 'recovery', 'direct')

def logic_4793(agents, world):
    _agent_apply(world, agents, 'herbivore', 'recovery', 'direct')

def logic_4794(agents, world):
    _agent_apply(world, agents, 'predator', 'recovery', 'direct')

def logic_4795(agents, world):
    _agent_apply(world, agents, 'carrion', 'recovery', 'direct')

def logic_4796(agents, world):
    _agent_apply(world, agents, 'nutrients', 'recovery', 'direct')

def logic_4797(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'recovery', 'direct')

def logic_4798(agents, world):
    _agent_apply(world, agents, 'oxygen', 'recovery', 'direct')

def logic_4799(agents, world):
    _agent_apply(world, agents, 'co2', 'recovery', 'direct')

def logic_4800(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'recovery', 'direct')

def logic_4801(agents, world):
    _agent_apply(world, agents, 'ice', 'recovery', 'direct')

def logic_4802(agents, world):
    _agent_apply(world, agents, 'evaporation', 'recovery', 'direct')

def logic_4803(agents, world):
    _agent_apply(world, agents, 'detritus', 'recovery', 'direct')

def logic_4804(agents, world):
    _agent_apply(world, agents, 'methane', 'recovery', 'direct')

def logic_4805(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'recovery', 'direct')

def logic_4806(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'recovery', 'direct')

def logic_4807(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'recovery', 'direct')

def logic_4808(agents, world):
    _agent_apply(world, agents, 'erosion', 'recovery', 'direct')

def logic_4809(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'recovery', 'direct')

def logic_4810(agents, world):
    _agent_apply(world, agents, 'root_density', 'recovery', 'direct')

def logic_4811(agents, world):
    _agent_apply(world, agents, 'wetland', 'recovery', 'direct')

def logic_4812(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'recovery', 'direct')

def logic_4813(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'recovery', 'direct')

def logic_4814(agents, world):
    _agent_apply(world, agents, 'ash', 'recovery', 'direct')

def logic_4815(agents, world):
    _agent_apply(world, agents, 'snowpack', 'recovery', 'direct')

def logic_4816(agents, world):
    _agent_apply(world, agents, 'groundwater', 'recovery', 'direct')

def logic_4817(agents, world):
    _agent_apply(world, agents, 'sediment', 'recovery', 'direct')

def logic_4818(agents, world):
    _agent_apply(world, agents, 'salinity', 'recovery', 'direct')

def logic_4819(agents, world):
    _agent_apply(world, agents, 'algae', 'recovery', 'direct')

def logic_4820(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'recovery', 'direct')

def logic_4821(agents, world):
    _agent_apply(world, agents, 'deadwood', 'recovery', 'direct')

def logic_4822(agents, world):
    _agent_apply(world, agents, 'pollinators', 'recovery', 'direct')

def logic_4823(agents, world):
    _agent_apply(world, agents, 'flowers', 'recovery', 'direct')

def logic_4824(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'recovery', 'direct')

def logic_4825(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'recovery', 'direct')

def logic_4826(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'recovery', 'direct')

def logic_4827(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'recovery', 'direct')

def logic_4828(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'recovery', 'direct')

def logic_4829(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'recovery', 'direct')

def logic_4830(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'recovery', 'direct')

def logic_4831(agents, world):
    _agent_apply(world, agents, 'hydration', 'recovery', 'direct')

def logic_4832(agents, world):
    _agent_apply(world, agents, 'thirst', 'recovery', 'direct')

def logic_4833(agents, world):
    _agent_apply(world, agents, 'hunger', 'recovery', 'direct')

def logic_4834(agents, world):
    _agent_apply(world, agents, 'health', 'recovery', 'direct')

def logic_4835(agents, world):
    _agent_apply(world, agents, 'stress', 'recovery', 'direct')

def logic_4836(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'recovery', 'direct')

def logic_4837(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'recovery', 'direct')

def logic_4838(agents, world):
    _agent_apply(world, agents, 'social_need', 'recovery', 'direct')

def logic_4839(agents, world):
    _agent_apply(world, agents, 'cooperation', 'recovery', 'direct')

def logic_4840(agents, world):
    _agent_apply(world, agents, 'defection', 'recovery', 'direct')

def logic_4841(agents, world):
    _agent_apply(world, agents, 'trust', 'recovery', 'direct')

def logic_4842(agents, world):
    _agent_apply(world, agents, 'reputation', 'recovery', 'direct')

def logic_4843(agents, world):
    _agent_apply(world, agents, 'help_received', 'recovery', 'direct')

def logic_4844(agents, world):
    _agent_apply(world, agents, 'help_given', 'recovery', 'direct')

def logic_4845(agents, world):
    _agent_apply(world, agents, 'local_density', 'recovery', 'direct')

def logic_4846(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'recovery', 'direct')

def logic_4847(agents, world):
    _agent_apply(world, agents, 'survival_score', 'recovery', 'direct')

def logic_4848(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'recovery', 'direct')

def logic_4849(agents, world):
    _agent_apply(world, agents, 'payoff', 'recovery', 'direct')

def logic_4850(agents, world):
    _agent_apply(world, agents, 'temperature', 'metabolic_cost', 'direct')

def logic_4851(agents, world):
    _agent_apply(world, agents, 'surface_water', 'metabolic_cost', 'direct')

def logic_4852(agents, world):
    _agent_apply(world, agents, 'humidity', 'metabolic_cost', 'direct')

def logic_4853(agents, world):
    _agent_apply(world, agents, 'cloud', 'metabolic_cost', 'direct')

def logic_4854(agents, world):
    _agent_apply(world, agents, 'rain', 'metabolic_cost', 'direct')

def logic_4855(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'metabolic_cost', 'direct')

def logic_4856(agents, world):
    _agent_apply(world, agents, 'runoff', 'metabolic_cost', 'direct')

def logic_4857(agents, world):
    _agent_apply(world, agents, 'wind_x', 'metabolic_cost', 'direct')

def logic_4858(agents, world):
    _agent_apply(world, agents, 'wind_y', 'metabolic_cost', 'direct')

def logic_4859(agents, world):
    _agent_apply(world, agents, 'vegetation', 'metabolic_cost', 'direct')

def logic_4860(agents, world):
    _agent_apply(world, agents, 'biomass', 'metabolic_cost', 'direct')

def logic_4861(agents, world):
    _agent_apply(world, agents, 'herbivore', 'metabolic_cost', 'direct')

def logic_4862(agents, world):
    _agent_apply(world, agents, 'predator', 'metabolic_cost', 'direct')

def logic_4863(agents, world):
    _agent_apply(world, agents, 'carrion', 'metabolic_cost', 'direct')

def logic_4864(agents, world):
    _agent_apply(world, agents, 'nutrients', 'metabolic_cost', 'direct')

def logic_4865(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'metabolic_cost', 'direct')

def logic_4866(agents, world):
    _agent_apply(world, agents, 'oxygen', 'metabolic_cost', 'direct')

def logic_4867(agents, world):
    _agent_apply(world, agents, 'co2', 'metabolic_cost', 'direct')

def logic_4868(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'metabolic_cost', 'direct')

def logic_4869(agents, world):
    _agent_apply(world, agents, 'ice', 'metabolic_cost', 'direct')

def logic_4870(agents, world):
    _agent_apply(world, agents, 'evaporation', 'metabolic_cost', 'direct')

def logic_4871(agents, world):
    _agent_apply(world, agents, 'detritus', 'metabolic_cost', 'direct')

def logic_4872(agents, world):
    _agent_apply(world, agents, 'methane', 'metabolic_cost', 'direct')

def logic_4873(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'metabolic_cost', 'direct')

def logic_4874(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'metabolic_cost', 'direct')

def logic_4875(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'metabolic_cost', 'direct')

def logic_4876(agents, world):
    _agent_apply(world, agents, 'erosion', 'metabolic_cost', 'direct')

def logic_4877(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'metabolic_cost', 'direct')

def logic_4878(agents, world):
    _agent_apply(world, agents, 'root_density', 'metabolic_cost', 'direct')

def logic_4879(agents, world):
    _agent_apply(world, agents, 'wetland', 'metabolic_cost', 'direct')

def logic_4880(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'metabolic_cost', 'direct')

def logic_4881(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'metabolic_cost', 'direct')

def logic_4882(agents, world):
    _agent_apply(world, agents, 'ash', 'metabolic_cost', 'direct')

def logic_4883(agents, world):
    _agent_apply(world, agents, 'snowpack', 'metabolic_cost', 'direct')

def logic_4884(agents, world):
    _agent_apply(world, agents, 'groundwater', 'metabolic_cost', 'direct')

def logic_4885(agents, world):
    _agent_apply(world, agents, 'sediment', 'metabolic_cost', 'direct')

def logic_4886(agents, world):
    _agent_apply(world, agents, 'salinity', 'metabolic_cost', 'direct')

def logic_4887(agents, world):
    _agent_apply(world, agents, 'algae', 'metabolic_cost', 'direct')

def logic_4888(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'metabolic_cost', 'direct')

def logic_4889(agents, world):
    _agent_apply(world, agents, 'deadwood', 'metabolic_cost', 'direct')

def logic_4890(agents, world):
    _agent_apply(world, agents, 'pollinators', 'metabolic_cost', 'direct')

def logic_4891(agents, world):
    _agent_apply(world, agents, 'flowers', 'metabolic_cost', 'direct')

def logic_4892(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'metabolic_cost', 'direct')

def logic_4893(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'metabolic_cost', 'direct')

def logic_4894(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'metabolic_cost', 'direct')

def logic_4895(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'metabolic_cost', 'direct')

def logic_4896(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'metabolic_cost', 'direct')

def logic_4897(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'metabolic_cost', 'direct')

def logic_4898(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'metabolic_cost', 'direct')

def logic_4899(agents, world):
    _agent_apply(world, agents, 'hydration', 'metabolic_cost', 'direct')

def logic_4900(agents, world):
    _agent_apply(world, agents, 'thirst', 'metabolic_cost', 'direct')

def logic_4901(agents, world):
    _agent_apply(world, agents, 'hunger', 'metabolic_cost', 'direct')

def logic_4902(agents, world):
    _agent_apply(world, agents, 'health', 'metabolic_cost', 'direct')

def logic_4903(agents, world):
    _agent_apply(world, agents, 'stress', 'metabolic_cost', 'direct')

def logic_4904(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'metabolic_cost', 'direct')

def logic_4905(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'metabolic_cost', 'direct')

def logic_4906(agents, world):
    _agent_apply(world, agents, 'social_need', 'metabolic_cost', 'direct')

def logic_4907(agents, world):
    _agent_apply(world, agents, 'cooperation', 'metabolic_cost', 'direct')

def logic_4908(agents, world):
    _agent_apply(world, agents, 'defection', 'metabolic_cost', 'direct')

def logic_4909(agents, world):
    _agent_apply(world, agents, 'trust', 'metabolic_cost', 'direct')

def logic_4910(agents, world):
    _agent_apply(world, agents, 'reputation', 'metabolic_cost', 'direct')

def logic_4911(agents, world):
    _agent_apply(world, agents, 'help_received', 'metabolic_cost', 'direct')

def logic_4912(agents, world):
    _agent_apply(world, agents, 'help_given', 'metabolic_cost', 'direct')

def logic_4913(agents, world):
    _agent_apply(world, agents, 'local_density', 'metabolic_cost', 'direct')

def logic_4914(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'metabolic_cost', 'direct')

def logic_4915(agents, world):
    _agent_apply(world, agents, 'survival_score', 'metabolic_cost', 'direct')

def logic_4916(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'metabolic_cost', 'direct')

def logic_4917(agents, world):
    _agent_apply(world, agents, 'payoff', 'metabolic_cost', 'direct')

def logic_4918(agents, world):
    _agent_apply(world, agents, 'temperature', 'reproduction_drive', 'direct')

def logic_4919(agents, world):
    _agent_apply(world, agents, 'surface_water', 'reproduction_drive', 'direct')

def logic_4920(agents, world):
    _agent_apply(world, agents, 'humidity', 'reproduction_drive', 'direct')

def logic_4921(agents, world):
    _agent_apply(world, agents, 'cloud', 'reproduction_drive', 'direct')

def logic_4922(agents, world):
    _agent_apply(world, agents, 'rain', 'reproduction_drive', 'direct')

def logic_4923(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'reproduction_drive', 'direct')

def logic_4924(agents, world):
    _agent_apply(world, agents, 'runoff', 'reproduction_drive', 'direct')

def logic_4925(agents, world):
    _agent_apply(world, agents, 'wind_x', 'reproduction_drive', 'direct')

def logic_4926(agents, world):
    _agent_apply(world, agents, 'wind_y', 'reproduction_drive', 'direct')

def logic_4927(agents, world):
    _agent_apply(world, agents, 'vegetation', 'reproduction_drive', 'direct')

def logic_4928(agents, world):
    _agent_apply(world, agents, 'biomass', 'reproduction_drive', 'direct')

def logic_4929(agents, world):
    _agent_apply(world, agents, 'herbivore', 'reproduction_drive', 'direct')

def logic_4930(agents, world):
    _agent_apply(world, agents, 'predator', 'reproduction_drive', 'direct')

def logic_4931(agents, world):
    _agent_apply(world, agents, 'carrion', 'reproduction_drive', 'direct')

def logic_4932(agents, world):
    _agent_apply(world, agents, 'nutrients', 'reproduction_drive', 'direct')

def logic_4933(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'reproduction_drive', 'direct')

def logic_4934(agents, world):
    _agent_apply(world, agents, 'oxygen', 'reproduction_drive', 'direct')

def logic_4935(agents, world):
    _agent_apply(world, agents, 'co2', 'reproduction_drive', 'direct')

def logic_4936(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'reproduction_drive', 'direct')

def logic_4937(agents, world):
    _agent_apply(world, agents, 'ice', 'reproduction_drive', 'direct')

def logic_4938(agents, world):
    _agent_apply(world, agents, 'evaporation', 'reproduction_drive', 'direct')

def logic_4939(agents, world):
    _agent_apply(world, agents, 'detritus', 'reproduction_drive', 'direct')

def logic_4940(agents, world):
    _agent_apply(world, agents, 'methane', 'reproduction_drive', 'direct')

def logic_4941(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'reproduction_drive', 'direct')

def logic_4942(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'reproduction_drive', 'direct')

def logic_4943(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'reproduction_drive', 'direct')

def logic_4944(agents, world):
    _agent_apply(world, agents, 'erosion', 'reproduction_drive', 'direct')

def logic_4945(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'reproduction_drive', 'direct')

def logic_4946(agents, world):
    _agent_apply(world, agents, 'root_density', 'reproduction_drive', 'direct')

def logic_4947(agents, world):
    _agent_apply(world, agents, 'wetland', 'reproduction_drive', 'direct')

def logic_4948(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'reproduction_drive', 'direct')

def logic_4949(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'reproduction_drive', 'direct')

def logic_4950(agents, world):
    _agent_apply(world, agents, 'ash', 'reproduction_drive', 'direct')

def logic_4951(agents, world):
    _agent_apply(world, agents, 'snowpack', 'reproduction_drive', 'direct')

def logic_4952(agents, world):
    _agent_apply(world, agents, 'groundwater', 'reproduction_drive', 'direct')

def logic_4953(agents, world):
    _agent_apply(world, agents, 'sediment', 'reproduction_drive', 'direct')

def logic_4954(agents, world):
    _agent_apply(world, agents, 'salinity', 'reproduction_drive', 'direct')

def logic_4955(agents, world):
    _agent_apply(world, agents, 'algae', 'reproduction_drive', 'direct')

def logic_4956(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'reproduction_drive', 'direct')

def logic_4957(agents, world):
    _agent_apply(world, agents, 'deadwood', 'reproduction_drive', 'direct')

def logic_4958(agents, world):
    _agent_apply(world, agents, 'pollinators', 'reproduction_drive', 'direct')

def logic_4959(agents, world):
    _agent_apply(world, agents, 'flowers', 'reproduction_drive', 'direct')

def logic_4960(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'reproduction_drive', 'direct')

def logic_4961(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'reproduction_drive', 'direct')

def logic_4962(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'reproduction_drive', 'direct')

def logic_4963(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'reproduction_drive', 'direct')

def logic_4964(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'reproduction_drive', 'direct')

def logic_4965(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'reproduction_drive', 'direct')

def logic_4966(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'reproduction_drive', 'direct')

def logic_4967(agents, world):
    _agent_apply(world, agents, 'hydration', 'reproduction_drive', 'direct')

def logic_4968(agents, world):
    _agent_apply(world, agents, 'thirst', 'reproduction_drive', 'direct')

def logic_4969(agents, world):
    _agent_apply(world, agents, 'hunger', 'reproduction_drive', 'direct')

def logic_4970(agents, world):
    _agent_apply(world, agents, 'health', 'reproduction_drive', 'direct')

def logic_4971(agents, world):
    _agent_apply(world, agents, 'stress', 'reproduction_drive', 'direct')

def logic_4972(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'reproduction_drive', 'direct')

def logic_4973(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'reproduction_drive', 'direct')

def logic_4974(agents, world):
    _agent_apply(world, agents, 'social_need', 'reproduction_drive', 'direct')

def logic_4975(agents, world):
    _agent_apply(world, agents, 'cooperation', 'reproduction_drive', 'direct')

def logic_4976(agents, world):
    _agent_apply(world, agents, 'defection', 'reproduction_drive', 'direct')

def logic_4977(agents, world):
    _agent_apply(world, agents, 'trust', 'reproduction_drive', 'direct')

def logic_4978(agents, world):
    _agent_apply(world, agents, 'reputation', 'reproduction_drive', 'direct')

def logic_4979(agents, world):
    _agent_apply(world, agents, 'help_received', 'reproduction_drive', 'direct')

def logic_4980(agents, world):
    _agent_apply(world, agents, 'help_given', 'reproduction_drive', 'direct')

def logic_4981(agents, world):
    _agent_apply(world, agents, 'local_density', 'reproduction_drive', 'direct')

def logic_4982(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'reproduction_drive', 'direct')

def logic_4983(agents, world):
    _agent_apply(world, agents, 'survival_score', 'reproduction_drive', 'direct')

def logic_4984(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'reproduction_drive', 'direct')

def logic_4985(agents, world):
    _agent_apply(world, agents, 'payoff', 'reproduction_drive', 'direct')

def logic_4986(agents, world):
    _agent_apply(world, agents, 'temperature', 'migration_drive', 'direct')

def logic_4987(agents, world):
    _agent_apply(world, agents, 'surface_water', 'migration_drive', 'direct')

def logic_4988(agents, world):
    _agent_apply(world, agents, 'humidity', 'migration_drive', 'direct')

def logic_4989(agents, world):
    _agent_apply(world, agents, 'cloud', 'migration_drive', 'direct')

def logic_4990(agents, world):
    _agent_apply(world, agents, 'rain', 'migration_drive', 'direct')

def logic_4991(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'migration_drive', 'direct')

def logic_4992(agents, world):
    _agent_apply(world, agents, 'runoff', 'migration_drive', 'direct')

def logic_4993(agents, world):
    _agent_apply(world, agents, 'wind_x', 'migration_drive', 'direct')

def logic_4994(agents, world):
    _agent_apply(world, agents, 'wind_y', 'migration_drive', 'direct')

def logic_4995(agents, world):
    _agent_apply(world, agents, 'vegetation', 'migration_drive', 'direct')

def logic_4996(agents, world):
    _agent_apply(world, agents, 'biomass', 'migration_drive', 'direct')

def logic_4997(agents, world):
    _agent_apply(world, agents, 'herbivore', 'migration_drive', 'direct')

def logic_4998(agents, world):
    _agent_apply(world, agents, 'predator', 'migration_drive', 'direct')

def logic_4999(agents, world):
    _agent_apply(world, agents, 'carrion', 'migration_drive', 'direct')

def logic_5000(agents, world):
    _agent_apply(world, agents, 'nutrients', 'migration_drive', 'direct')

def logic_5001(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'migration_drive', 'direct')

def logic_5002(agents, world):
    _agent_apply(world, agents, 'oxygen', 'migration_drive', 'direct')

def logic_5003(agents, world):
    _agent_apply(world, agents, 'co2', 'migration_drive', 'direct')

def logic_5004(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'migration_drive', 'direct')

def logic_5005(agents, world):
    _agent_apply(world, agents, 'ice', 'migration_drive', 'direct')

def logic_5006(agents, world):
    _agent_apply(world, agents, 'evaporation', 'migration_drive', 'direct')

def logic_5007(agents, world):
    _agent_apply(world, agents, 'detritus', 'migration_drive', 'direct')

def logic_5008(agents, world):
    _agent_apply(world, agents, 'methane', 'migration_drive', 'direct')

def logic_5009(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'migration_drive', 'direct')

def logic_5010(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'migration_drive', 'direct')

def logic_5011(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'migration_drive', 'direct')

def logic_5012(agents, world):
    _agent_apply(world, agents, 'erosion', 'migration_drive', 'direct')

def logic_5013(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'migration_drive', 'direct')

def logic_5014(agents, world):
    _agent_apply(world, agents, 'root_density', 'migration_drive', 'direct')

def logic_5015(agents, world):
    _agent_apply(world, agents, 'wetland', 'migration_drive', 'direct')

def logic_5016(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'migration_drive', 'direct')

def logic_5017(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'migration_drive', 'direct')

def logic_5018(agents, world):
    _agent_apply(world, agents, 'ash', 'migration_drive', 'direct')

def logic_5019(agents, world):
    _agent_apply(world, agents, 'snowpack', 'migration_drive', 'direct')

def logic_5020(agents, world):
    _agent_apply(world, agents, 'groundwater', 'migration_drive', 'direct')

def logic_5021(agents, world):
    _agent_apply(world, agents, 'sediment', 'migration_drive', 'direct')

def logic_5022(agents, world):
    _agent_apply(world, agents, 'salinity', 'migration_drive', 'direct')

def logic_5023(agents, world):
    _agent_apply(world, agents, 'algae', 'migration_drive', 'direct')

def logic_5024(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'migration_drive', 'direct')

def logic_5025(agents, world):
    _agent_apply(world, agents, 'deadwood', 'migration_drive', 'direct')

def logic_5026(agents, world):
    _agent_apply(world, agents, 'pollinators', 'migration_drive', 'direct')

def logic_5027(agents, world):
    _agent_apply(world, agents, 'flowers', 'migration_drive', 'direct')

def logic_5028(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'migration_drive', 'direct')

def logic_5029(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'migration_drive', 'direct')

def logic_5030(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'migration_drive', 'direct')

def logic_5031(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'migration_drive', 'direct')

def logic_5032(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'migration_drive', 'direct')

def logic_5033(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'migration_drive', 'direct')

def logic_5034(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'migration_drive', 'direct')

def logic_5035(agents, world):
    _agent_apply(world, agents, 'hydration', 'migration_drive', 'direct')

def logic_5036(agents, world):
    _agent_apply(world, agents, 'thirst', 'migration_drive', 'direct')

def logic_5037(agents, world):
    _agent_apply(world, agents, 'hunger', 'migration_drive', 'direct')

def logic_5038(agents, world):
    _agent_apply(world, agents, 'health', 'migration_drive', 'direct')

def logic_5039(agents, world):
    _agent_apply(world, agents, 'stress', 'migration_drive', 'direct')

def logic_5040(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'migration_drive', 'direct')

def logic_5041(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'migration_drive', 'direct')

def logic_5042(agents, world):
    _agent_apply(world, agents, 'social_need', 'migration_drive', 'direct')

def logic_5043(agents, world):
    _agent_apply(world, agents, 'cooperation', 'migration_drive', 'direct')

def logic_5044(agents, world):
    _agent_apply(world, agents, 'defection', 'migration_drive', 'direct')

def logic_5045(agents, world):
    _agent_apply(world, agents, 'trust', 'migration_drive', 'direct')

def logic_5046(agents, world):
    _agent_apply(world, agents, 'reputation', 'migration_drive', 'direct')

def logic_5047(agents, world):
    _agent_apply(world, agents, 'help_received', 'migration_drive', 'direct')

def logic_5048(agents, world):
    _agent_apply(world, agents, 'help_given', 'migration_drive', 'direct')

def logic_5049(agents, world):
    _agent_apply(world, agents, 'local_density', 'migration_drive', 'direct')

def logic_5050(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'migration_drive', 'direct')

def logic_5051(agents, world):
    _agent_apply(world, agents, 'survival_score', 'migration_drive', 'direct')

def logic_5052(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'migration_drive', 'direct')

def logic_5053(agents, world):
    _agent_apply(world, agents, 'payoff', 'migration_drive', 'direct')

def logic_5054(agents, world):
    _agent_apply(world, agents, 'temperature', 'exploration_drive', 'direct')

def logic_5055(agents, world):
    _agent_apply(world, agents, 'surface_water', 'exploration_drive', 'direct')

def logic_5056(agents, world):
    _agent_apply(world, agents, 'humidity', 'exploration_drive', 'direct')

def logic_5057(agents, world):
    _agent_apply(world, agents, 'cloud', 'exploration_drive', 'direct')

def logic_5058(agents, world):
    _agent_apply(world, agents, 'rain', 'exploration_drive', 'direct')

def logic_5059(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'exploration_drive', 'direct')

def logic_5060(agents, world):
    _agent_apply(world, agents, 'runoff', 'exploration_drive', 'direct')

def logic_5061(agents, world):
    _agent_apply(world, agents, 'wind_x', 'exploration_drive', 'direct')

def logic_5062(agents, world):
    _agent_apply(world, agents, 'wind_y', 'exploration_drive', 'direct')

def logic_5063(agents, world):
    _agent_apply(world, agents, 'vegetation', 'exploration_drive', 'direct')

def logic_5064(agents, world):
    _agent_apply(world, agents, 'biomass', 'exploration_drive', 'direct')

def logic_5065(agents, world):
    _agent_apply(world, agents, 'herbivore', 'exploration_drive', 'direct')

def logic_5066(agents, world):
    _agent_apply(world, agents, 'predator', 'exploration_drive', 'direct')

def logic_5067(agents, world):
    _agent_apply(world, agents, 'carrion', 'exploration_drive', 'direct')

def logic_5068(agents, world):
    _agent_apply(world, agents, 'nutrients', 'exploration_drive', 'direct')

def logic_5069(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'exploration_drive', 'direct')

def logic_5070(agents, world):
    _agent_apply(world, agents, 'oxygen', 'exploration_drive', 'direct')

def logic_5071(agents, world):
    _agent_apply(world, agents, 'co2', 'exploration_drive', 'direct')

def logic_5072(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'exploration_drive', 'direct')

def logic_5073(agents, world):
    _agent_apply(world, agents, 'ice', 'exploration_drive', 'direct')

def logic_5074(agents, world):
    _agent_apply(world, agents, 'evaporation', 'exploration_drive', 'direct')

def logic_5075(agents, world):
    _agent_apply(world, agents, 'detritus', 'exploration_drive', 'direct')

def logic_5076(agents, world):
    _agent_apply(world, agents, 'methane', 'exploration_drive', 'direct')

def logic_5077(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'exploration_drive', 'direct')

def logic_5078(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'exploration_drive', 'direct')

def logic_5079(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'exploration_drive', 'direct')

def logic_5080(agents, world):
    _agent_apply(world, agents, 'erosion', 'exploration_drive', 'direct')

def logic_5081(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'exploration_drive', 'direct')

def logic_5082(agents, world):
    _agent_apply(world, agents, 'root_density', 'exploration_drive', 'direct')

def logic_5083(agents, world):
    _agent_apply(world, agents, 'wetland', 'exploration_drive', 'direct')

def logic_5084(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'exploration_drive', 'direct')

def logic_5085(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'exploration_drive', 'direct')

def logic_5086(agents, world):
    _agent_apply(world, agents, 'ash', 'exploration_drive', 'direct')

def logic_5087(agents, world):
    _agent_apply(world, agents, 'snowpack', 'exploration_drive', 'direct')

def logic_5088(agents, world):
    _agent_apply(world, agents, 'groundwater', 'exploration_drive', 'direct')

def logic_5089(agents, world):
    _agent_apply(world, agents, 'sediment', 'exploration_drive', 'direct')

def logic_5090(agents, world):
    _agent_apply(world, agents, 'salinity', 'exploration_drive', 'direct')

def logic_5091(agents, world):
    _agent_apply(world, agents, 'algae', 'exploration_drive', 'direct')

def logic_5092(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'exploration_drive', 'direct')

def logic_5093(agents, world):
    _agent_apply(world, agents, 'deadwood', 'exploration_drive', 'direct')

def logic_5094(agents, world):
    _agent_apply(world, agents, 'pollinators', 'exploration_drive', 'direct')

def logic_5095(agents, world):
    _agent_apply(world, agents, 'flowers', 'exploration_drive', 'direct')

def logic_5096(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'exploration_drive', 'direct')

def logic_5097(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'exploration_drive', 'direct')

def logic_5098(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'exploration_drive', 'direct')

def logic_5099(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'exploration_drive', 'direct')

def logic_5100(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'exploration_drive', 'direct')

def logic_5101(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'exploration_drive', 'direct')

def logic_5102(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'exploration_drive', 'direct')

def logic_5103(agents, world):
    _agent_apply(world, agents, 'hydration', 'exploration_drive', 'direct')

def logic_5104(agents, world):
    _agent_apply(world, agents, 'thirst', 'exploration_drive', 'direct')

def logic_5105(agents, world):
    _agent_apply(world, agents, 'hunger', 'exploration_drive', 'direct')

def logic_5106(agents, world):
    _agent_apply(world, agents, 'health', 'exploration_drive', 'direct')

def logic_5107(agents, world):
    _agent_apply(world, agents, 'stress', 'exploration_drive', 'direct')

def logic_5108(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'exploration_drive', 'direct')

def logic_5109(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'exploration_drive', 'direct')

def logic_5110(agents, world):
    _agent_apply(world, agents, 'social_need', 'exploration_drive', 'direct')

def logic_5111(agents, world):
    _agent_apply(world, agents, 'cooperation', 'exploration_drive', 'direct')

def logic_5112(agents, world):
    _agent_apply(world, agents, 'defection', 'exploration_drive', 'direct')

def logic_5113(agents, world):
    _agent_apply(world, agents, 'trust', 'exploration_drive', 'direct')

def logic_5114(agents, world):
    _agent_apply(world, agents, 'reputation', 'exploration_drive', 'direct')

def logic_5115(agents, world):
    _agent_apply(world, agents, 'help_received', 'exploration_drive', 'direct')

def logic_5116(agents, world):
    _agent_apply(world, agents, 'help_given', 'exploration_drive', 'direct')

def logic_5117(agents, world):
    _agent_apply(world, agents, 'local_density', 'exploration_drive', 'direct')

def logic_5118(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'exploration_drive', 'direct')

def logic_5119(agents, world):
    _agent_apply(world, agents, 'survival_score', 'exploration_drive', 'direct')

def logic_5120(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'exploration_drive', 'direct')

def logic_5121(agents, world):
    _agent_apply(world, agents, 'payoff', 'exploration_drive', 'direct')

def logic_5122(agents, world):
    _agent_apply(world, agents, 'temperature', 'food_access', 'direct')

def logic_5123(agents, world):
    _agent_apply(world, agents, 'surface_water', 'food_access', 'direct')

def logic_5124(agents, world):
    _agent_apply(world, agents, 'humidity', 'food_access', 'direct')

def logic_5125(agents, world):
    _agent_apply(world, agents, 'cloud', 'food_access', 'direct')

def logic_5126(agents, world):
    _agent_apply(world, agents, 'rain', 'food_access', 'direct')

def logic_5127(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'food_access', 'direct')

def logic_5128(agents, world):
    _agent_apply(world, agents, 'runoff', 'food_access', 'direct')

def logic_5129(agents, world):
    _agent_apply(world, agents, 'wind_x', 'food_access', 'direct')

def logic_5130(agents, world):
    _agent_apply(world, agents, 'wind_y', 'food_access', 'direct')

def logic_5131(agents, world):
    _agent_apply(world, agents, 'vegetation', 'food_access', 'direct')

def logic_5132(agents, world):
    _agent_apply(world, agents, 'biomass', 'food_access', 'direct')

def logic_5133(agents, world):
    _agent_apply(world, agents, 'herbivore', 'food_access', 'direct')

def logic_5134(agents, world):
    _agent_apply(world, agents, 'predator', 'food_access', 'direct')

def logic_5135(agents, world):
    _agent_apply(world, agents, 'carrion', 'food_access', 'direct')

def logic_5136(agents, world):
    _agent_apply(world, agents, 'nutrients', 'food_access', 'direct')

def logic_5137(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'food_access', 'direct')

def logic_5138(agents, world):
    _agent_apply(world, agents, 'oxygen', 'food_access', 'direct')

def logic_5139(agents, world):
    _agent_apply(world, agents, 'co2', 'food_access', 'direct')

def logic_5140(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'food_access', 'direct')

def logic_5141(agents, world):
    _agent_apply(world, agents, 'ice', 'food_access', 'direct')

def logic_5142(agents, world):
    _agent_apply(world, agents, 'evaporation', 'food_access', 'direct')

def logic_5143(agents, world):
    _agent_apply(world, agents, 'detritus', 'food_access', 'direct')

def logic_5144(agents, world):
    _agent_apply(world, agents, 'methane', 'food_access', 'direct')

def logic_5145(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'food_access', 'direct')

def logic_5146(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'food_access', 'direct')

def logic_5147(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'food_access', 'direct')

def logic_5148(agents, world):
    _agent_apply(world, agents, 'erosion', 'food_access', 'direct')

def logic_5149(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'food_access', 'direct')

def logic_5150(agents, world):
    _agent_apply(world, agents, 'root_density', 'food_access', 'direct')

def logic_5151(agents, world):
    _agent_apply(world, agents, 'wetland', 'food_access', 'direct')

def logic_5152(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'food_access', 'direct')

def logic_5153(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'food_access', 'direct')

def logic_5154(agents, world):
    _agent_apply(world, agents, 'ash', 'food_access', 'direct')

def logic_5155(agents, world):
    _agent_apply(world, agents, 'snowpack', 'food_access', 'direct')

def logic_5156(agents, world):
    _agent_apply(world, agents, 'groundwater', 'food_access', 'direct')

def logic_5157(agents, world):
    _agent_apply(world, agents, 'sediment', 'food_access', 'direct')

def logic_5158(agents, world):
    _agent_apply(world, agents, 'salinity', 'food_access', 'direct')

def logic_5159(agents, world):
    _agent_apply(world, agents, 'algae', 'food_access', 'direct')

def logic_5160(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'food_access', 'direct')

def logic_5161(agents, world):
    _agent_apply(world, agents, 'deadwood', 'food_access', 'direct')

def logic_5162(agents, world):
    _agent_apply(world, agents, 'pollinators', 'food_access', 'direct')

def logic_5163(agents, world):
    _agent_apply(world, agents, 'flowers', 'food_access', 'direct')

def logic_5164(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'food_access', 'direct')

def logic_5165(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'food_access', 'direct')

def logic_5166(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'food_access', 'direct')

def logic_5167(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'food_access', 'direct')

def logic_5168(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'food_access', 'direct')

def logic_5169(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'food_access', 'direct')

def logic_5170(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'food_access', 'direct')

def logic_5171(agents, world):
    _agent_apply(world, agents, 'hydration', 'food_access', 'direct')

def logic_5172(agents, world):
    _agent_apply(world, agents, 'thirst', 'food_access', 'direct')

def logic_5173(agents, world):
    _agent_apply(world, agents, 'hunger', 'food_access', 'direct')

def logic_5174(agents, world):
    _agent_apply(world, agents, 'health', 'food_access', 'direct')

def logic_5175(agents, world):
    _agent_apply(world, agents, 'stress', 'food_access', 'direct')

def logic_5176(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'food_access', 'direct')

def logic_5177(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'food_access', 'direct')

def logic_5178(agents, world):
    _agent_apply(world, agents, 'social_need', 'food_access', 'direct')

def logic_5179(agents, world):
    _agent_apply(world, agents, 'cooperation', 'food_access', 'direct')

def logic_5180(agents, world):
    _agent_apply(world, agents, 'defection', 'food_access', 'direct')

def logic_5181(agents, world):
    _agent_apply(world, agents, 'trust', 'food_access', 'direct')

def logic_5182(agents, world):
    _agent_apply(world, agents, 'reputation', 'food_access', 'direct')

def logic_5183(agents, world):
    _agent_apply(world, agents, 'help_received', 'food_access', 'direct')

def logic_5184(agents, world):
    _agent_apply(world, agents, 'help_given', 'food_access', 'direct')

def logic_5185(agents, world):
    _agent_apply(world, agents, 'local_density', 'food_access', 'direct')

def logic_5186(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'food_access', 'direct')

def logic_5187(agents, world):
    _agent_apply(world, agents, 'survival_score', 'food_access', 'direct')

def logic_5188(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'food_access', 'direct')

def logic_5189(agents, world):
    _agent_apply(world, agents, 'payoff', 'food_access', 'direct')

def logic_5190(agents, world):
    _agent_apply(world, agents, 'temperature', 'wealth', 'direct')

def logic_5191(agents, world):
    _agent_apply(world, agents, 'surface_water', 'wealth', 'direct')

def logic_5192(agents, world):
    _agent_apply(world, agents, 'humidity', 'wealth', 'direct')

def logic_5193(agents, world):
    _agent_apply(world, agents, 'cloud', 'wealth', 'direct')

def logic_5194(agents, world):
    _agent_apply(world, agents, 'rain', 'wealth', 'direct')

def logic_5195(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'wealth', 'direct')

def logic_5196(agents, world):
    _agent_apply(world, agents, 'runoff', 'wealth', 'direct')

def logic_5197(agents, world):
    _agent_apply(world, agents, 'wind_x', 'wealth', 'direct')

def logic_5198(agents, world):
    _agent_apply(world, agents, 'wind_y', 'wealth', 'direct')

def logic_5199(agents, world):
    _agent_apply(world, agents, 'vegetation', 'wealth', 'direct')

def logic_5200(agents, world):
    _agent_apply(world, agents, 'biomass', 'wealth', 'direct')

def logic_5201(agents, world):
    _agent_apply(world, agents, 'herbivore', 'wealth', 'direct')

def logic_5202(agents, world):
    _agent_apply(world, agents, 'predator', 'wealth', 'direct')

def logic_5203(agents, world):
    _agent_apply(world, agents, 'carrion', 'wealth', 'direct')

def logic_5204(agents, world):
    _agent_apply(world, agents, 'nutrients', 'wealth', 'direct')

def logic_5205(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'wealth', 'direct')

def logic_5206(agents, world):
    _agent_apply(world, agents, 'oxygen', 'wealth', 'direct')

def logic_5207(agents, world):
    _agent_apply(world, agents, 'co2', 'wealth', 'direct')

def logic_5208(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'wealth', 'direct')

def logic_5209(agents, world):
    _agent_apply(world, agents, 'ice', 'wealth', 'direct')

def logic_5210(agents, world):
    _agent_apply(world, agents, 'evaporation', 'wealth', 'direct')

def logic_5211(agents, world):
    _agent_apply(world, agents, 'detritus', 'wealth', 'direct')

def logic_5212(agents, world):
    _agent_apply(world, agents, 'methane', 'wealth', 'direct')

def logic_5213(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'wealth', 'direct')

def logic_5214(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'wealth', 'direct')

def logic_5215(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'wealth', 'direct')

def logic_5216(agents, world):
    _agent_apply(world, agents, 'erosion', 'wealth', 'direct')

def logic_5217(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'wealth', 'direct')

def logic_5218(agents, world):
    _agent_apply(world, agents, 'root_density', 'wealth', 'direct')

def logic_5219(agents, world):
    _agent_apply(world, agents, 'wetland', 'wealth', 'direct')

def logic_5220(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'wealth', 'direct')

def logic_5221(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'wealth', 'direct')

def logic_5222(agents, world):
    _agent_apply(world, agents, 'ash', 'wealth', 'direct')

def logic_5223(agents, world):
    _agent_apply(world, agents, 'snowpack', 'wealth', 'direct')

def logic_5224(agents, world):
    _agent_apply(world, agents, 'groundwater', 'wealth', 'direct')

def logic_5225(agents, world):
    _agent_apply(world, agents, 'sediment', 'wealth', 'direct')

def logic_5226(agents, world):
    _agent_apply(world, agents, 'salinity', 'wealth', 'direct')

def logic_5227(agents, world):
    _agent_apply(world, agents, 'algae', 'wealth', 'direct')

def logic_5228(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'wealth', 'direct')

def logic_5229(agents, world):
    _agent_apply(world, agents, 'deadwood', 'wealth', 'direct')

def logic_5230(agents, world):
    _agent_apply(world, agents, 'pollinators', 'wealth', 'direct')

def logic_5231(agents, world):
    _agent_apply(world, agents, 'flowers', 'wealth', 'direct')

def logic_5232(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'wealth', 'direct')

def logic_5233(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'wealth', 'direct')

def logic_5234(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'wealth', 'direct')

def logic_5235(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'wealth', 'direct')

def logic_5236(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'wealth', 'direct')

def logic_5237(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'wealth', 'direct')

def logic_5238(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'wealth', 'direct')

def logic_5239(agents, world):
    _agent_apply(world, agents, 'hydration', 'wealth', 'direct')

def logic_5240(agents, world):
    _agent_apply(world, agents, 'thirst', 'wealth', 'direct')

def logic_5241(agents, world):
    _agent_apply(world, agents, 'hunger', 'wealth', 'direct')

def logic_5242(agents, world):
    _agent_apply(world, agents, 'health', 'wealth', 'direct')

def logic_5243(agents, world):
    _agent_apply(world, agents, 'stress', 'wealth', 'direct')

def logic_5244(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'wealth', 'direct')

def logic_5245(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'wealth', 'direct')

def logic_5246(agents, world):
    _agent_apply(world, agents, 'social_need', 'wealth', 'direct')

def logic_5247(agents, world):
    _agent_apply(world, agents, 'cooperation', 'wealth', 'direct')

def logic_5248(agents, world):
    _agent_apply(world, agents, 'defection', 'wealth', 'direct')

def logic_5249(agents, world):
    _agent_apply(world, agents, 'trust', 'wealth', 'direct')

def logic_5250(agents, world):
    _agent_apply(world, agents, 'reputation', 'wealth', 'direct')

def logic_5251(agents, world):
    _agent_apply(world, agents, 'help_received', 'wealth', 'direct')

def logic_5252(agents, world):
    _agent_apply(world, agents, 'help_given', 'wealth', 'direct')

def logic_5253(agents, world):
    _agent_apply(world, agents, 'local_density', 'wealth', 'direct')

def logic_5254(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'wealth', 'direct')

def logic_5255(agents, world):
    _agent_apply(world, agents, 'survival_score', 'wealth', 'direct')

def logic_5256(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'wealth', 'direct')

def logic_5257(agents, world):
    _agent_apply(world, agents, 'payoff', 'wealth', 'direct')

def logic_5258(agents, world):
    _agent_apply(world, agents, 'temperature', 'stability', 'direct')

def logic_5259(agents, world):
    _agent_apply(world, agents, 'surface_water', 'stability', 'direct')

def logic_5260(agents, world):
    _agent_apply(world, agents, 'humidity', 'stability', 'direct')

def logic_5261(agents, world):
    _agent_apply(world, agents, 'cloud', 'stability', 'direct')

def logic_5262(agents, world):
    _agent_apply(world, agents, 'rain', 'stability', 'direct')

def logic_5263(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'stability', 'direct')

def logic_5264(agents, world):
    _agent_apply(world, agents, 'runoff', 'stability', 'direct')

def logic_5265(agents, world):
    _agent_apply(world, agents, 'wind_x', 'stability', 'direct')

def logic_5266(agents, world):
    _agent_apply(world, agents, 'wind_y', 'stability', 'direct')

def logic_5267(agents, world):
    _agent_apply(world, agents, 'vegetation', 'stability', 'direct')

def logic_5268(agents, world):
    _agent_apply(world, agents, 'biomass', 'stability', 'direct')

def logic_5269(agents, world):
    _agent_apply(world, agents, 'herbivore', 'stability', 'direct')

def logic_5270(agents, world):
    _agent_apply(world, agents, 'predator', 'stability', 'direct')

def logic_5271(agents, world):
    _agent_apply(world, agents, 'carrion', 'stability', 'direct')

def logic_5272(agents, world):
    _agent_apply(world, agents, 'nutrients', 'stability', 'direct')

def logic_5273(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'stability', 'direct')

def logic_5274(agents, world):
    _agent_apply(world, agents, 'oxygen', 'stability', 'direct')

def logic_5275(agents, world):
    _agent_apply(world, agents, 'co2', 'stability', 'direct')

def logic_5276(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'stability', 'direct')

def logic_5277(agents, world):
    _agent_apply(world, agents, 'ice', 'stability', 'direct')

def logic_5278(agents, world):
    _agent_apply(world, agents, 'evaporation', 'stability', 'direct')

def logic_5279(agents, world):
    _agent_apply(world, agents, 'detritus', 'stability', 'direct')

def logic_5280(agents, world):
    _agent_apply(world, agents, 'methane', 'stability', 'direct')

def logic_5281(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'stability', 'direct')

def logic_5282(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'stability', 'direct')

def logic_5283(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'stability', 'direct')

def logic_5284(agents, world):
    _agent_apply(world, agents, 'erosion', 'stability', 'direct')

def logic_5285(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'stability', 'direct')

def logic_5286(agents, world):
    _agent_apply(world, agents, 'root_density', 'stability', 'direct')

def logic_5287(agents, world):
    _agent_apply(world, agents, 'wetland', 'stability', 'direct')

def logic_5288(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'stability', 'direct')

def logic_5289(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'stability', 'direct')

def logic_5290(agents, world):
    _agent_apply(world, agents, 'ash', 'stability', 'direct')

def logic_5291(agents, world):
    _agent_apply(world, agents, 'snowpack', 'stability', 'direct')

def logic_5292(agents, world):
    _agent_apply(world, agents, 'groundwater', 'stability', 'direct')

def logic_5293(agents, world):
    _agent_apply(world, agents, 'sediment', 'stability', 'direct')

def logic_5294(agents, world):
    _agent_apply(world, agents, 'salinity', 'stability', 'direct')

def logic_5295(agents, world):
    _agent_apply(world, agents, 'algae', 'stability', 'direct')

def logic_5296(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'stability', 'direct')

def logic_5297(agents, world):
    _agent_apply(world, agents, 'deadwood', 'stability', 'direct')

def logic_5298(agents, world):
    _agent_apply(world, agents, 'pollinators', 'stability', 'direct')

def logic_5299(agents, world):
    _agent_apply(world, agents, 'flowers', 'stability', 'direct')

def logic_5300(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'stability', 'direct')

def logic_5301(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'stability', 'direct')

def logic_5302(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'stability', 'direct')

def logic_5303(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'stability', 'direct')

def logic_5304(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'stability', 'direct')

def logic_5305(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'stability', 'direct')

def logic_5306(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'stability', 'direct')

def logic_5307(agents, world):
    _agent_apply(world, agents, 'hydration', 'stability', 'direct')

def logic_5308(agents, world):
    _agent_apply(world, agents, 'thirst', 'stability', 'direct')

def logic_5309(agents, world):
    _agent_apply(world, agents, 'hunger', 'stability', 'direct')

def logic_5310(agents, world):
    _agent_apply(world, agents, 'health', 'stability', 'direct')

def logic_5311(agents, world):
    _agent_apply(world, agents, 'stress', 'stability', 'direct')

def logic_5312(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'stability', 'direct')

def logic_5313(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'stability', 'direct')

def logic_5314(agents, world):
    _agent_apply(world, agents, 'social_need', 'stability', 'direct')

def logic_5315(agents, world):
    _agent_apply(world, agents, 'cooperation', 'stability', 'direct')

def logic_5316(agents, world):
    _agent_apply(world, agents, 'defection', 'stability', 'direct')

def logic_5317(agents, world):
    _agent_apply(world, agents, 'trust', 'stability', 'direct')

def logic_5318(agents, world):
    _agent_apply(world, agents, 'reputation', 'stability', 'direct')

def logic_5319(agents, world):
    _agent_apply(world, agents, 'help_received', 'stability', 'direct')

def logic_5320(agents, world):
    _agent_apply(world, agents, 'help_given', 'stability', 'direct')

def logic_5321(agents, world):
    _agent_apply(world, agents, 'local_density', 'stability', 'direct')

def logic_5322(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'stability', 'direct')

def logic_5323(agents, world):
    _agent_apply(world, agents, 'survival_score', 'stability', 'direct')

def logic_5324(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'stability', 'direct')

def logic_5325(agents, world):
    _agent_apply(world, agents, 'payoff', 'stability', 'direct')

def logic_5326(agents, world):
    _agent_apply(world, agents, 'temperature', 'habitat_stress', 'direct')

def logic_5327(agents, world):
    _agent_apply(world, agents, 'surface_water', 'habitat_stress', 'direct')

def logic_5328(agents, world):
    _agent_apply(world, agents, 'humidity', 'habitat_stress', 'direct')

def logic_5329(agents, world):
    _agent_apply(world, agents, 'cloud', 'habitat_stress', 'direct')

def logic_5330(agents, world):
    _agent_apply(world, agents, 'rain', 'habitat_stress', 'direct')

def logic_5331(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'habitat_stress', 'direct')

def logic_5332(agents, world):
    _agent_apply(world, agents, 'runoff', 'habitat_stress', 'direct')

def logic_5333(agents, world):
    _agent_apply(world, agents, 'wind_x', 'habitat_stress', 'direct')

def logic_5334(agents, world):
    _agent_apply(world, agents, 'wind_y', 'habitat_stress', 'direct')

def logic_5335(agents, world):
    _agent_apply(world, agents, 'vegetation', 'habitat_stress', 'direct')

def logic_5336(agents, world):
    _agent_apply(world, agents, 'biomass', 'habitat_stress', 'direct')

def logic_5337(agents, world):
    _agent_apply(world, agents, 'herbivore', 'habitat_stress', 'direct')

def logic_5338(agents, world):
    _agent_apply(world, agents, 'predator', 'habitat_stress', 'direct')

def logic_5339(agents, world):
    _agent_apply(world, agents, 'carrion', 'habitat_stress', 'direct')

def logic_5340(agents, world):
    _agent_apply(world, agents, 'nutrients', 'habitat_stress', 'direct')

def logic_5341(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'habitat_stress', 'direct')

def logic_5342(agents, world):
    _agent_apply(world, agents, 'oxygen', 'habitat_stress', 'direct')

def logic_5343(agents, world):
    _agent_apply(world, agents, 'co2', 'habitat_stress', 'direct')

def logic_5344(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'habitat_stress', 'direct')

def logic_5345(agents, world):
    _agent_apply(world, agents, 'ice', 'habitat_stress', 'direct')

def logic_5346(agents, world):
    _agent_apply(world, agents, 'evaporation', 'habitat_stress', 'direct')

def logic_5347(agents, world):
    _agent_apply(world, agents, 'detritus', 'habitat_stress', 'direct')

def logic_5348(agents, world):
    _agent_apply(world, agents, 'methane', 'habitat_stress', 'direct')

def logic_5349(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'habitat_stress', 'direct')

def logic_5350(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'habitat_stress', 'direct')

def logic_5351(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'habitat_stress', 'direct')

def logic_5352(agents, world):
    _agent_apply(world, agents, 'erosion', 'habitat_stress', 'direct')

def logic_5353(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'habitat_stress', 'direct')

def logic_5354(agents, world):
    _agent_apply(world, agents, 'root_density', 'habitat_stress', 'direct')

def logic_5355(agents, world):
    _agent_apply(world, agents, 'wetland', 'habitat_stress', 'direct')

def logic_5356(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'habitat_stress', 'direct')

def logic_5357(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'habitat_stress', 'direct')

def logic_5358(agents, world):
    _agent_apply(world, agents, 'ash', 'habitat_stress', 'direct')

def logic_5359(agents, world):
    _agent_apply(world, agents, 'snowpack', 'habitat_stress', 'direct')

def logic_5360(agents, world):
    _agent_apply(world, agents, 'groundwater', 'habitat_stress', 'direct')

def logic_5361(agents, world):
    _agent_apply(world, agents, 'sediment', 'habitat_stress', 'direct')

def logic_5362(agents, world):
    _agent_apply(world, agents, 'salinity', 'habitat_stress', 'direct')

def logic_5363(agents, world):
    _agent_apply(world, agents, 'algae', 'habitat_stress', 'direct')

def logic_5364(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'habitat_stress', 'direct')

def logic_5365(agents, world):
    _agent_apply(world, agents, 'deadwood', 'habitat_stress', 'direct')

def logic_5366(agents, world):
    _agent_apply(world, agents, 'pollinators', 'habitat_stress', 'direct')

def logic_5367(agents, world):
    _agent_apply(world, agents, 'flowers', 'habitat_stress', 'direct')

def logic_5368(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'habitat_stress', 'direct')

def logic_5369(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'habitat_stress', 'direct')

def logic_5370(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'habitat_stress', 'direct')

def logic_5371(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'habitat_stress', 'direct')

def logic_5372(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'habitat_stress', 'direct')

def logic_5373(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'habitat_stress', 'direct')

def logic_5374(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'habitat_stress', 'direct')

def logic_5375(agents, world):
    _agent_apply(world, agents, 'hydration', 'habitat_stress', 'direct')

def logic_5376(agents, world):
    _agent_apply(world, agents, 'thirst', 'habitat_stress', 'direct')

def logic_5377(agents, world):
    _agent_apply(world, agents, 'hunger', 'habitat_stress', 'direct')

def logic_5378(agents, world):
    _agent_apply(world, agents, 'health', 'habitat_stress', 'direct')

def logic_5379(agents, world):
    _agent_apply(world, agents, 'stress', 'habitat_stress', 'direct')

def logic_5380(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'habitat_stress', 'direct')

def logic_5381(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'habitat_stress', 'direct')

def logic_5382(agents, world):
    _agent_apply(world, agents, 'social_need', 'habitat_stress', 'direct')

def logic_5383(agents, world):
    _agent_apply(world, agents, 'cooperation', 'habitat_stress', 'direct')

def logic_5384(agents, world):
    _agent_apply(world, agents, 'defection', 'habitat_stress', 'direct')

def logic_5385(agents, world):
    _agent_apply(world, agents, 'trust', 'habitat_stress', 'direct')

def logic_5386(agents, world):
    _agent_apply(world, agents, 'reputation', 'habitat_stress', 'direct')

def logic_5387(agents, world):
    _agent_apply(world, agents, 'help_received', 'habitat_stress', 'direct')

def logic_5388(agents, world):
    _agent_apply(world, agents, 'help_given', 'habitat_stress', 'direct')

def logic_5389(agents, world):
    _agent_apply(world, agents, 'local_density', 'habitat_stress', 'direct')

def logic_5390(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'habitat_stress', 'direct')

def logic_5391(agents, world):
    _agent_apply(world, agents, 'survival_score', 'habitat_stress', 'direct')

def logic_5392(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'habitat_stress', 'direct')

def logic_5393(agents, world):
    _agent_apply(world, agents, 'payoff', 'habitat_stress', 'direct')

def logic_5394(agents, world):
    _agent_apply(world, agents, 'temperature', 'social_tolerance', 'direct')

def logic_5395(agents, world):
    _agent_apply(world, agents, 'surface_water', 'social_tolerance', 'direct')

def logic_5396(agents, world):
    _agent_apply(world, agents, 'humidity', 'social_tolerance', 'direct')

def logic_5397(agents, world):
    _agent_apply(world, agents, 'cloud', 'social_tolerance', 'direct')

def logic_5398(agents, world):
    _agent_apply(world, agents, 'rain', 'social_tolerance', 'direct')

def logic_5399(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'social_tolerance', 'direct')

def logic_5400(agents, world):
    _agent_apply(world, agents, 'runoff', 'social_tolerance', 'direct')

def logic_5401(agents, world):
    _agent_apply(world, agents, 'wind_x', 'social_tolerance', 'direct')

def logic_5402(agents, world):
    _agent_apply(world, agents, 'wind_y', 'social_tolerance', 'direct')

def logic_5403(agents, world):
    _agent_apply(world, agents, 'vegetation', 'social_tolerance', 'direct')

def logic_5404(agents, world):
    _agent_apply(world, agents, 'biomass', 'social_tolerance', 'direct')

def logic_5405(agents, world):
    _agent_apply(world, agents, 'herbivore', 'social_tolerance', 'direct')

def logic_5406(agents, world):
    _agent_apply(world, agents, 'predator', 'social_tolerance', 'direct')

def logic_5407(agents, world):
    _agent_apply(world, agents, 'carrion', 'social_tolerance', 'direct')

def logic_5408(agents, world):
    _agent_apply(world, agents, 'nutrients', 'social_tolerance', 'direct')

def logic_5409(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'social_tolerance', 'direct')

def logic_5410(agents, world):
    _agent_apply(world, agents, 'oxygen', 'social_tolerance', 'direct')

def logic_5411(agents, world):
    _agent_apply(world, agents, 'co2', 'social_tolerance', 'direct')

def logic_5412(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'social_tolerance', 'direct')

def logic_5413(agents, world):
    _agent_apply(world, agents, 'ice', 'social_tolerance', 'direct')

def logic_5414(agents, world):
    _agent_apply(world, agents, 'evaporation', 'social_tolerance', 'direct')

def logic_5415(agents, world):
    _agent_apply(world, agents, 'detritus', 'social_tolerance', 'direct')

def logic_5416(agents, world):
    _agent_apply(world, agents, 'methane', 'social_tolerance', 'direct')

def logic_5417(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'social_tolerance', 'direct')

def logic_5418(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'social_tolerance', 'direct')

def logic_5419(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'social_tolerance', 'direct')

def logic_5420(agents, world):
    _agent_apply(world, agents, 'erosion', 'social_tolerance', 'direct')

def logic_5421(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'social_tolerance', 'direct')

def logic_5422(agents, world):
    _agent_apply(world, agents, 'root_density', 'social_tolerance', 'direct')

def logic_5423(agents, world):
    _agent_apply(world, agents, 'wetland', 'social_tolerance', 'direct')

def logic_5424(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'social_tolerance', 'direct')

def logic_5425(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'social_tolerance', 'direct')

def logic_5426(agents, world):
    _agent_apply(world, agents, 'ash', 'social_tolerance', 'direct')

def logic_5427(agents, world):
    _agent_apply(world, agents, 'snowpack', 'social_tolerance', 'direct')

def logic_5428(agents, world):
    _agent_apply(world, agents, 'groundwater', 'social_tolerance', 'direct')

def logic_5429(agents, world):
    _agent_apply(world, agents, 'sediment', 'social_tolerance', 'direct')

def logic_5430(agents, world):
    _agent_apply(world, agents, 'salinity', 'social_tolerance', 'direct')

def logic_5431(agents, world):
    _agent_apply(world, agents, 'algae', 'social_tolerance', 'direct')

def logic_5432(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'social_tolerance', 'direct')

def logic_5433(agents, world):
    _agent_apply(world, agents, 'deadwood', 'social_tolerance', 'direct')

def logic_5434(agents, world):
    _agent_apply(world, agents, 'pollinators', 'social_tolerance', 'direct')

def logic_5435(agents, world):
    _agent_apply(world, agents, 'flowers', 'social_tolerance', 'direct')

def logic_5436(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'social_tolerance', 'direct')

def logic_5437(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'social_tolerance', 'direct')

def logic_5438(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'social_tolerance', 'direct')

def logic_5439(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'social_tolerance', 'direct')

def logic_5440(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'social_tolerance', 'direct')

def logic_5441(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'social_tolerance', 'direct')

def logic_5442(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'social_tolerance', 'direct')

def logic_5443(agents, world):
    _agent_apply(world, agents, 'hydration', 'social_tolerance', 'direct')

def logic_5444(agents, world):
    _agent_apply(world, agents, 'thirst', 'social_tolerance', 'direct')

def logic_5445(agents, world):
    _agent_apply(world, agents, 'hunger', 'social_tolerance', 'direct')

def logic_5446(agents, world):
    _agent_apply(world, agents, 'health', 'social_tolerance', 'direct')

def logic_5447(agents, world):
    _agent_apply(world, agents, 'stress', 'social_tolerance', 'direct')

def logic_5448(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'social_tolerance', 'direct')

def logic_5449(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'social_tolerance', 'direct')

def logic_5450(agents, world):
    _agent_apply(world, agents, 'social_need', 'social_tolerance', 'direct')

def logic_5451(agents, world):
    _agent_apply(world, agents, 'cooperation', 'social_tolerance', 'direct')

def logic_5452(agents, world):
    _agent_apply(world, agents, 'defection', 'social_tolerance', 'direct')

def logic_5453(agents, world):
    _agent_apply(world, agents, 'trust', 'social_tolerance', 'direct')

def logic_5454(agents, world):
    _agent_apply(world, agents, 'reputation', 'social_tolerance', 'direct')

def logic_5455(agents, world):
    _agent_apply(world, agents, 'help_received', 'social_tolerance', 'direct')

def logic_5456(agents, world):
    _agent_apply(world, agents, 'help_given', 'social_tolerance', 'direct')

def logic_5457(agents, world):
    _agent_apply(world, agents, 'local_density', 'social_tolerance', 'direct')

def logic_5458(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'social_tolerance', 'direct')

def logic_5459(agents, world):
    _agent_apply(world, agents, 'survival_score', 'social_tolerance', 'direct')

def logic_5460(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'social_tolerance', 'direct')

def logic_5461(agents, world):
    _agent_apply(world, agents, 'payoff', 'social_tolerance', 'direct')

def logic_5462(agents, world):
    _agent_apply(world, agents, 'temperature', 'reputation', 'direct')

def logic_5463(agents, world):
    _agent_apply(world, agents, 'surface_water', 'reputation', 'direct')

def logic_5464(agents, world):
    _agent_apply(world, agents, 'humidity', 'reputation', 'direct')

def logic_5465(agents, world):
    _agent_apply(world, agents, 'cloud', 'reputation', 'direct')

def logic_5466(agents, world):
    _agent_apply(world, agents, 'rain', 'reputation', 'direct')

def logic_5467(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'reputation', 'direct')

def logic_5468(agents, world):
    _agent_apply(world, agents, 'runoff', 'reputation', 'direct')

def logic_5469(agents, world):
    _agent_apply(world, agents, 'wind_x', 'reputation', 'direct')

def logic_5470(agents, world):
    _agent_apply(world, agents, 'wind_y', 'reputation', 'direct')

def logic_5471(agents, world):
    _agent_apply(world, agents, 'vegetation', 'reputation', 'direct')

def logic_5472(agents, world):
    _agent_apply(world, agents, 'biomass', 'reputation', 'direct')

def logic_5473(agents, world):
    _agent_apply(world, agents, 'herbivore', 'reputation', 'direct')

def logic_5474(agents, world):
    _agent_apply(world, agents, 'predator', 'reputation', 'direct')

def logic_5475(agents, world):
    _agent_apply(world, agents, 'carrion', 'reputation', 'direct')

def logic_5476(agents, world):
    _agent_apply(world, agents, 'nutrients', 'reputation', 'direct')

def logic_5477(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'reputation', 'direct')

def logic_5478(agents, world):
    _agent_apply(world, agents, 'oxygen', 'reputation', 'direct')

def logic_5479(agents, world):
    _agent_apply(world, agents, 'co2', 'reputation', 'direct')

def logic_5480(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'reputation', 'direct')

def logic_5481(agents, world):
    _agent_apply(world, agents, 'ice', 'reputation', 'direct')

def logic_5482(agents, world):
    _agent_apply(world, agents, 'evaporation', 'reputation', 'direct')

def logic_5483(agents, world):
    _agent_apply(world, agents, 'detritus', 'reputation', 'direct')

def logic_5484(agents, world):
    _agent_apply(world, agents, 'methane', 'reputation', 'direct')

def logic_5485(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'reputation', 'direct')

def logic_5486(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'reputation', 'direct')

def logic_5487(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'reputation', 'direct')

def logic_5488(agents, world):
    _agent_apply(world, agents, 'erosion', 'reputation', 'direct')

def logic_5489(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'reputation', 'direct')

def logic_5490(agents, world):
    _agent_apply(world, agents, 'root_density', 'reputation', 'direct')

def logic_5491(agents, world):
    _agent_apply(world, agents, 'wetland', 'reputation', 'direct')

def logic_5492(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'reputation', 'direct')

def logic_5493(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'reputation', 'direct')

def logic_5494(agents, world):
    _agent_apply(world, agents, 'ash', 'reputation', 'direct')

def logic_5495(agents, world):
    _agent_apply(world, agents, 'snowpack', 'reputation', 'direct')

def logic_5496(agents, world):
    _agent_apply(world, agents, 'groundwater', 'reputation', 'direct')

def logic_5497(agents, world):
    _agent_apply(world, agents, 'sediment', 'reputation', 'direct')

def logic_5498(agents, world):
    _agent_apply(world, agents, 'salinity', 'reputation', 'direct')

def logic_5499(agents, world):
    _agent_apply(world, agents, 'algae', 'reputation', 'direct')

def logic_5500(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'reputation', 'direct')

def logic_5501(agents, world):
    _agent_apply(world, agents, 'deadwood', 'reputation', 'direct')

def logic_5502(agents, world):
    _agent_apply(world, agents, 'pollinators', 'reputation', 'direct')

def logic_5503(agents, world):
    _agent_apply(world, agents, 'flowers', 'reputation', 'direct')

def logic_5504(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'reputation', 'direct')

def logic_5505(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'reputation', 'direct')

def logic_5506(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'reputation', 'direct')

def logic_5507(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'reputation', 'direct')

def logic_5508(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'reputation', 'direct')

def logic_5509(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'reputation', 'direct')

def logic_5510(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'reputation', 'direct')

def logic_5511(agents, world):
    _agent_apply(world, agents, 'hydration', 'reputation', 'direct')

def logic_5512(agents, world):
    _agent_apply(world, agents, 'thirst', 'reputation', 'direct')

def logic_5513(agents, world):
    _agent_apply(world, agents, 'hunger', 'reputation', 'direct')

def logic_5514(agents, world):
    _agent_apply(world, agents, 'health', 'reputation', 'direct')

def logic_5515(agents, world):
    _agent_apply(world, agents, 'stress', 'reputation', 'direct')

def logic_5516(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'reputation', 'direct')

def logic_5517(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'reputation', 'direct')

def logic_5518(agents, world):
    _agent_apply(world, agents, 'social_need', 'reputation', 'direct')

def logic_5519(agents, world):
    _agent_apply(world, agents, 'cooperation', 'reputation', 'direct')

def logic_5520(agents, world):
    _agent_apply(world, agents, 'defection', 'reputation', 'direct')

def logic_5521(agents, world):
    _agent_apply(world, agents, 'trust', 'reputation', 'direct')

def logic_5522(agents, world):
    _agent_apply(world, agents, 'reputation', 'reputation', 'direct')

def logic_5523(agents, world):
    _agent_apply(world, agents, 'help_received', 'reputation', 'direct')

def logic_5524(agents, world):
    _agent_apply(world, agents, 'help_given', 'reputation', 'direct')

def logic_5525(agents, world):
    _agent_apply(world, agents, 'local_density', 'reputation', 'direct')

def logic_5526(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'reputation', 'direct')

def logic_5527(agents, world):
    _agent_apply(world, agents, 'survival_score', 'reputation', 'direct')

def logic_5528(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'reputation', 'direct')

def logic_5529(agents, world):
    _agent_apply(world, agents, 'payoff', 'reputation', 'direct')

def logic_5530(agents, world):
    _agent_apply(world, agents, 'temperature', 'trust', 'direct')

def logic_5531(agents, world):
    _agent_apply(world, agents, 'surface_water', 'trust', 'direct')

def logic_5532(agents, world):
    _agent_apply(world, agents, 'humidity', 'trust', 'direct')

def logic_5533(agents, world):
    _agent_apply(world, agents, 'cloud', 'trust', 'direct')

def logic_5534(agents, world):
    _agent_apply(world, agents, 'rain', 'trust', 'direct')

def logic_5535(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'trust', 'direct')

def logic_5536(agents, world):
    _agent_apply(world, agents, 'runoff', 'trust', 'direct')

def logic_5537(agents, world):
    _agent_apply(world, agents, 'wind_x', 'trust', 'direct')

def logic_5538(agents, world):
    _agent_apply(world, agents, 'wind_y', 'trust', 'direct')

def logic_5539(agents, world):
    _agent_apply(world, agents, 'vegetation', 'trust', 'direct')

def logic_5540(agents, world):
    _agent_apply(world, agents, 'biomass', 'trust', 'direct')

def logic_5541(agents, world):
    _agent_apply(world, agents, 'herbivore', 'trust', 'direct')

def logic_5542(agents, world):
    _agent_apply(world, agents, 'predator', 'trust', 'direct')

def logic_5543(agents, world):
    _agent_apply(world, agents, 'carrion', 'trust', 'direct')

def logic_5544(agents, world):
    _agent_apply(world, agents, 'nutrients', 'trust', 'direct')

def logic_5545(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'trust', 'direct')

def logic_5546(agents, world):
    _agent_apply(world, agents, 'oxygen', 'trust', 'direct')

def logic_5547(agents, world):
    _agent_apply(world, agents, 'co2', 'trust', 'direct')

def logic_5548(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'trust', 'direct')

def logic_5549(agents, world):
    _agent_apply(world, agents, 'ice', 'trust', 'direct')

def logic_5550(agents, world):
    _agent_apply(world, agents, 'evaporation', 'trust', 'direct')

def logic_5551(agents, world):
    _agent_apply(world, agents, 'detritus', 'trust', 'direct')

def logic_5552(agents, world):
    _agent_apply(world, agents, 'methane', 'trust', 'direct')

def logic_5553(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'trust', 'direct')

def logic_5554(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'trust', 'direct')

def logic_5555(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'trust', 'direct')

def logic_5556(agents, world):
    _agent_apply(world, agents, 'erosion', 'trust', 'direct')

def logic_5557(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'trust', 'direct')

def logic_5558(agents, world):
    _agent_apply(world, agents, 'root_density', 'trust', 'direct')

def logic_5559(agents, world):
    _agent_apply(world, agents, 'wetland', 'trust', 'direct')

def logic_5560(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'trust', 'direct')

def logic_5561(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'trust', 'direct')

def logic_5562(agents, world):
    _agent_apply(world, agents, 'ash', 'trust', 'direct')

def logic_5563(agents, world):
    _agent_apply(world, agents, 'snowpack', 'trust', 'direct')

def logic_5564(agents, world):
    _agent_apply(world, agents, 'groundwater', 'trust', 'direct')

def logic_5565(agents, world):
    _agent_apply(world, agents, 'sediment', 'trust', 'direct')

def logic_5566(agents, world):
    _agent_apply(world, agents, 'salinity', 'trust', 'direct')

def logic_5567(agents, world):
    _agent_apply(world, agents, 'algae', 'trust', 'direct')

def logic_5568(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'trust', 'direct')

def logic_5569(agents, world):
    _agent_apply(world, agents, 'deadwood', 'trust', 'direct')

def logic_5570(agents, world):
    _agent_apply(world, agents, 'pollinators', 'trust', 'direct')

def logic_5571(agents, world):
    _agent_apply(world, agents, 'flowers', 'trust', 'direct')

def logic_5572(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'trust', 'direct')

def logic_5573(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'trust', 'direct')

def logic_5574(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'trust', 'direct')

def logic_5575(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'trust', 'direct')

def logic_5576(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'trust', 'direct')

def logic_5577(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'trust', 'direct')

def logic_5578(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'trust', 'direct')

def logic_5579(agents, world):
    _agent_apply(world, agents, 'hydration', 'trust', 'direct')

def logic_5580(agents, world):
    _agent_apply(world, agents, 'thirst', 'trust', 'direct')

def logic_5581(agents, world):
    _agent_apply(world, agents, 'hunger', 'trust', 'direct')

def logic_5582(agents, world):
    _agent_apply(world, agents, 'health', 'trust', 'direct')

def logic_5583(agents, world):
    _agent_apply(world, agents, 'stress', 'trust', 'direct')

def logic_5584(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'trust', 'direct')

def logic_5585(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'trust', 'direct')

def logic_5586(agents, world):
    _agent_apply(world, agents, 'social_need', 'trust', 'direct')

def logic_5587(agents, world):
    _agent_apply(world, agents, 'cooperation', 'trust', 'direct')

def logic_5588(agents, world):
    _agent_apply(world, agents, 'defection', 'trust', 'direct')

def logic_5589(agents, world):
    _agent_apply(world, agents, 'trust', 'trust', 'direct')

def logic_5590(agents, world):
    _agent_apply(world, agents, 'reputation', 'trust', 'direct')

def logic_5591(agents, world):
    _agent_apply(world, agents, 'help_received', 'trust', 'direct')

def logic_5592(agents, world):
    _agent_apply(world, agents, 'help_given', 'trust', 'direct')

def logic_5593(agents, world):
    _agent_apply(world, agents, 'local_density', 'trust', 'direct')

def logic_5594(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'trust', 'direct')

def logic_5595(agents, world):
    _agent_apply(world, agents, 'survival_score', 'trust', 'direct')

def logic_5596(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'trust', 'direct')

def logic_5597(agents, world):
    _agent_apply(world, agents, 'payoff', 'trust', 'direct')

def logic_5598(agents, world):
    _agent_apply(world, agents, 'temperature', 'cooperation', 'direct')

def logic_5599(agents, world):
    _agent_apply(world, agents, 'surface_water', 'cooperation', 'direct')

def logic_5600(agents, world):
    _agent_apply(world, agents, 'humidity', 'cooperation', 'direct')

def logic_5601(agents, world):
    _agent_apply(world, agents, 'cloud', 'cooperation', 'direct')

def logic_5602(agents, world):
    _agent_apply(world, agents, 'rain', 'cooperation', 'direct')

def logic_5603(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'cooperation', 'direct')

def logic_5604(agents, world):
    _agent_apply(world, agents, 'runoff', 'cooperation', 'direct')

def logic_5605(agents, world):
    _agent_apply(world, agents, 'wind_x', 'cooperation', 'direct')

def logic_5606(agents, world):
    _agent_apply(world, agents, 'wind_y', 'cooperation', 'direct')

def logic_5607(agents, world):
    _agent_apply(world, agents, 'vegetation', 'cooperation', 'direct')

def logic_5608(agents, world):
    _agent_apply(world, agents, 'biomass', 'cooperation', 'direct')

def logic_5609(agents, world):
    _agent_apply(world, agents, 'herbivore', 'cooperation', 'direct')

def logic_5610(agents, world):
    _agent_apply(world, agents, 'predator', 'cooperation', 'direct')

def logic_5611(agents, world):
    _agent_apply(world, agents, 'carrion', 'cooperation', 'direct')

def logic_5612(agents, world):
    _agent_apply(world, agents, 'nutrients', 'cooperation', 'direct')

def logic_5613(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'cooperation', 'direct')

def logic_5614(agents, world):
    _agent_apply(world, agents, 'oxygen', 'cooperation', 'direct')

def logic_5615(agents, world):
    _agent_apply(world, agents, 'co2', 'cooperation', 'direct')

def logic_5616(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'cooperation', 'direct')

def logic_5617(agents, world):
    _agent_apply(world, agents, 'ice', 'cooperation', 'direct')

def logic_5618(agents, world):
    _agent_apply(world, agents, 'evaporation', 'cooperation', 'direct')

def logic_5619(agents, world):
    _agent_apply(world, agents, 'detritus', 'cooperation', 'direct')

def logic_5620(agents, world):
    _agent_apply(world, agents, 'methane', 'cooperation', 'direct')

def logic_5621(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'cooperation', 'direct')

def logic_5622(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'cooperation', 'direct')

def logic_5623(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'cooperation', 'direct')

def logic_5624(agents, world):
    _agent_apply(world, agents, 'erosion', 'cooperation', 'direct')

def logic_5625(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'cooperation', 'direct')

def logic_5626(agents, world):
    _agent_apply(world, agents, 'root_density', 'cooperation', 'direct')

def logic_5627(agents, world):
    _agent_apply(world, agents, 'wetland', 'cooperation', 'direct')

def logic_5628(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'cooperation', 'direct')

def logic_5629(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'cooperation', 'direct')

def logic_5630(agents, world):
    _agent_apply(world, agents, 'ash', 'cooperation', 'direct')

def logic_5631(agents, world):
    _agent_apply(world, agents, 'snowpack', 'cooperation', 'direct')

def logic_5632(agents, world):
    _agent_apply(world, agents, 'groundwater', 'cooperation', 'direct')

def logic_5633(agents, world):
    _agent_apply(world, agents, 'sediment', 'cooperation', 'direct')

def logic_5634(agents, world):
    _agent_apply(world, agents, 'salinity', 'cooperation', 'direct')

def logic_5635(agents, world):
    _agent_apply(world, agents, 'algae', 'cooperation', 'direct')

def logic_5636(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'cooperation', 'direct')

def logic_5637(agents, world):
    _agent_apply(world, agents, 'deadwood', 'cooperation', 'direct')

def logic_5638(agents, world):
    _agent_apply(world, agents, 'pollinators', 'cooperation', 'direct')

def logic_5639(agents, world):
    _agent_apply(world, agents, 'flowers', 'cooperation', 'direct')

def logic_5640(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'cooperation', 'direct')

def logic_5641(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'cooperation', 'direct')

def logic_5642(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'cooperation', 'direct')

def logic_5643(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'cooperation', 'direct')

def logic_5644(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'cooperation', 'direct')

def logic_5645(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'cooperation', 'direct')

def logic_5646(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'cooperation', 'direct')

def logic_5647(agents, world):
    _agent_apply(world, agents, 'hydration', 'cooperation', 'direct')

def logic_5648(agents, world):
    _agent_apply(world, agents, 'thirst', 'cooperation', 'direct')

def logic_5649(agents, world):
    _agent_apply(world, agents, 'hunger', 'cooperation', 'direct')

def logic_5650(agents, world):
    _agent_apply(world, agents, 'health', 'cooperation', 'direct')

def logic_5651(agents, world):
    _agent_apply(world, agents, 'stress', 'cooperation', 'direct')

def logic_5652(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'cooperation', 'direct')

def logic_5653(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'cooperation', 'direct')

def logic_5654(agents, world):
    _agent_apply(world, agents, 'social_need', 'cooperation', 'direct')

def logic_5655(agents, world):
    _agent_apply(world, agents, 'cooperation', 'cooperation', 'direct')

def logic_5656(agents, world):
    _agent_apply(world, agents, 'defection', 'cooperation', 'direct')

def logic_5657(agents, world):
    _agent_apply(world, agents, 'trust', 'cooperation', 'direct')

def logic_5658(agents, world):
    _agent_apply(world, agents, 'reputation', 'cooperation', 'direct')

def logic_5659(agents, world):
    _agent_apply(world, agents, 'help_received', 'cooperation', 'direct')

def logic_5660(agents, world):
    _agent_apply(world, agents, 'help_given', 'cooperation', 'direct')

def logic_5661(agents, world):
    _agent_apply(world, agents, 'local_density', 'cooperation', 'direct')

def logic_5662(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'cooperation', 'direct')

def logic_5663(agents, world):
    _agent_apply(world, agents, 'survival_score', 'cooperation', 'direct')

def logic_5664(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'cooperation', 'direct')

def logic_5665(agents, world):
    _agent_apply(world, agents, 'payoff', 'cooperation', 'direct')

def logic_5666(agents, world):
    _agent_apply(world, agents, 'temperature', 'defection', 'direct')

def logic_5667(agents, world):
    _agent_apply(world, agents, 'surface_water', 'defection', 'direct')

def logic_5668(agents, world):
    _agent_apply(world, agents, 'humidity', 'defection', 'direct')

def logic_5669(agents, world):
    _agent_apply(world, agents, 'cloud', 'defection', 'direct')

def logic_5670(agents, world):
    _agent_apply(world, agents, 'rain', 'defection', 'direct')

def logic_5671(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'defection', 'direct')

def logic_5672(agents, world):
    _agent_apply(world, agents, 'runoff', 'defection', 'direct')

def logic_5673(agents, world):
    _agent_apply(world, agents, 'wind_x', 'defection', 'direct')

def logic_5674(agents, world):
    _agent_apply(world, agents, 'wind_y', 'defection', 'direct')

def logic_5675(agents, world):
    _agent_apply(world, agents, 'vegetation', 'defection', 'direct')

def logic_5676(agents, world):
    _agent_apply(world, agents, 'biomass', 'defection', 'direct')

def logic_5677(agents, world):
    _agent_apply(world, agents, 'herbivore', 'defection', 'direct')

def logic_5678(agents, world):
    _agent_apply(world, agents, 'predator', 'defection', 'direct')

def logic_5679(agents, world):
    _agent_apply(world, agents, 'carrion', 'defection', 'direct')

def logic_5680(agents, world):
    _agent_apply(world, agents, 'nutrients', 'defection', 'direct')

def logic_5681(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'defection', 'direct')

def logic_5682(agents, world):
    _agent_apply(world, agents, 'oxygen', 'defection', 'direct')

def logic_5683(agents, world):
    _agent_apply(world, agents, 'co2', 'defection', 'direct')

def logic_5684(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'defection', 'direct')

def logic_5685(agents, world):
    _agent_apply(world, agents, 'ice', 'defection', 'direct')

def logic_5686(agents, world):
    _agent_apply(world, agents, 'evaporation', 'defection', 'direct')

def logic_5687(agents, world):
    _agent_apply(world, agents, 'detritus', 'defection', 'direct')

def logic_5688(agents, world):
    _agent_apply(world, agents, 'methane', 'defection', 'direct')

def logic_5689(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'defection', 'direct')

def logic_5690(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'defection', 'direct')

def logic_5691(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'defection', 'direct')

def logic_5692(agents, world):
    _agent_apply(world, agents, 'erosion', 'defection', 'direct')

def logic_5693(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'defection', 'direct')

def logic_5694(agents, world):
    _agent_apply(world, agents, 'root_density', 'defection', 'direct')

def logic_5695(agents, world):
    _agent_apply(world, agents, 'wetland', 'defection', 'direct')

def logic_5696(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'defection', 'direct')

def logic_5697(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'defection', 'direct')

def logic_5698(agents, world):
    _agent_apply(world, agents, 'ash', 'defection', 'direct')

def logic_5699(agents, world):
    _agent_apply(world, agents, 'snowpack', 'defection', 'direct')

def logic_5700(agents, world):
    _agent_apply(world, agents, 'groundwater', 'defection', 'direct')

def logic_5701(agents, world):
    _agent_apply(world, agents, 'sediment', 'defection', 'direct')

def logic_5702(agents, world):
    _agent_apply(world, agents, 'salinity', 'defection', 'direct')

def logic_5703(agents, world):
    _agent_apply(world, agents, 'algae', 'defection', 'direct')

def logic_5704(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'defection', 'direct')

def logic_5705(agents, world):
    _agent_apply(world, agents, 'deadwood', 'defection', 'direct')

def logic_5706(agents, world):
    _agent_apply(world, agents, 'pollinators', 'defection', 'direct')

def logic_5707(agents, world):
    _agent_apply(world, agents, 'flowers', 'defection', 'direct')

def logic_5708(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'defection', 'direct')

def logic_5709(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'defection', 'direct')

def logic_5710(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'defection', 'direct')

def logic_5711(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'defection', 'direct')

def logic_5712(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'defection', 'direct')

def logic_5713(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'defection', 'direct')

def logic_5714(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'defection', 'direct')

def logic_5715(agents, world):
    _agent_apply(world, agents, 'hydration', 'defection', 'direct')

def logic_5716(agents, world):
    _agent_apply(world, agents, 'thirst', 'defection', 'direct')

def logic_5717(agents, world):
    _agent_apply(world, agents, 'hunger', 'defection', 'direct')

def logic_5718(agents, world):
    _agent_apply(world, agents, 'health', 'defection', 'direct')

def logic_5719(agents, world):
    _agent_apply(world, agents, 'stress', 'defection', 'direct')

def logic_5720(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'defection', 'direct')

def logic_5721(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'defection', 'direct')

def logic_5722(agents, world):
    _agent_apply(world, agents, 'social_need', 'defection', 'direct')

def logic_5723(agents, world):
    _agent_apply(world, agents, 'cooperation', 'defection', 'direct')

def logic_5724(agents, world):
    _agent_apply(world, agents, 'defection', 'defection', 'direct')

def logic_5725(agents, world):
    _agent_apply(world, agents, 'trust', 'defection', 'direct')

def logic_5726(agents, world):
    _agent_apply(world, agents, 'reputation', 'defection', 'direct')

def logic_5727(agents, world):
    _agent_apply(world, agents, 'help_received', 'defection', 'direct')

def logic_5728(agents, world):
    _agent_apply(world, agents, 'help_given', 'defection', 'direct')

def logic_5729(agents, world):
    _agent_apply(world, agents, 'local_density', 'defection', 'direct')

def logic_5730(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'defection', 'direct')

def logic_5731(agents, world):
    _agent_apply(world, agents, 'survival_score', 'defection', 'direct')

def logic_5732(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'defection', 'direct')

def logic_5733(agents, world):
    _agent_apply(world, agents, 'payoff', 'defection', 'direct')

def logic_5734(agents, world):
    _agent_apply(world, agents, 'temperature', 'aggression', 'direct')

def logic_5735(agents, world):
    _agent_apply(world, agents, 'surface_water', 'aggression', 'direct')

def logic_5736(agents, world):
    _agent_apply(world, agents, 'humidity', 'aggression', 'direct')

def logic_5737(agents, world):
    _agent_apply(world, agents, 'cloud', 'aggression', 'direct')

def logic_5738(agents, world):
    _agent_apply(world, agents, 'rain', 'aggression', 'direct')

def logic_5739(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'aggression', 'direct')

def logic_5740(agents, world):
    _agent_apply(world, agents, 'runoff', 'aggression', 'direct')

def logic_5741(agents, world):
    _agent_apply(world, agents, 'wind_x', 'aggression', 'direct')

def logic_5742(agents, world):
    _agent_apply(world, agents, 'wind_y', 'aggression', 'direct')

def logic_5743(agents, world):
    _agent_apply(world, agents, 'vegetation', 'aggression', 'direct')

def logic_5744(agents, world):
    _agent_apply(world, agents, 'biomass', 'aggression', 'direct')

def logic_5745(agents, world):
    _agent_apply(world, agents, 'herbivore', 'aggression', 'direct')

def logic_5746(agents, world):
    _agent_apply(world, agents, 'predator', 'aggression', 'direct')

def logic_5747(agents, world):
    _agent_apply(world, agents, 'carrion', 'aggression', 'direct')

def logic_5748(agents, world):
    _agent_apply(world, agents, 'nutrients', 'aggression', 'direct')

def logic_5749(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'aggression', 'direct')

def logic_5750(agents, world):
    _agent_apply(world, agents, 'oxygen', 'aggression', 'direct')

def logic_5751(agents, world):
    _agent_apply(world, agents, 'co2', 'aggression', 'direct')

def logic_5752(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'aggression', 'direct')

def logic_5753(agents, world):
    _agent_apply(world, agents, 'ice', 'aggression', 'direct')

def logic_5754(agents, world):
    _agent_apply(world, agents, 'evaporation', 'aggression', 'direct')

def logic_5755(agents, world):
    _agent_apply(world, agents, 'detritus', 'aggression', 'direct')

def logic_5756(agents, world):
    _agent_apply(world, agents, 'methane', 'aggression', 'direct')

def logic_5757(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'aggression', 'direct')

def logic_5758(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'aggression', 'direct')

def logic_5759(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'aggression', 'direct')

def logic_5760(agents, world):
    _agent_apply(world, agents, 'erosion', 'aggression', 'direct')

def logic_5761(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'aggression', 'direct')

def logic_5762(agents, world):
    _agent_apply(world, agents, 'root_density', 'aggression', 'direct')

def logic_5763(agents, world):
    _agent_apply(world, agents, 'wetland', 'aggression', 'direct')

def logic_5764(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'aggression', 'direct')

def logic_5765(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'aggression', 'direct')

def logic_5766(agents, world):
    _agent_apply(world, agents, 'ash', 'aggression', 'direct')

def logic_5767(agents, world):
    _agent_apply(world, agents, 'snowpack', 'aggression', 'direct')

def logic_5768(agents, world):
    _agent_apply(world, agents, 'groundwater', 'aggression', 'direct')

def logic_5769(agents, world):
    _agent_apply(world, agents, 'sediment', 'aggression', 'direct')

def logic_5770(agents, world):
    _agent_apply(world, agents, 'salinity', 'aggression', 'direct')

def logic_5771(agents, world):
    _agent_apply(world, agents, 'algae', 'aggression', 'direct')

def logic_5772(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'aggression', 'direct')

def logic_5773(agents, world):
    _agent_apply(world, agents, 'deadwood', 'aggression', 'direct')

def logic_5774(agents, world):
    _agent_apply(world, agents, 'pollinators', 'aggression', 'direct')

def logic_5775(agents, world):
    _agent_apply(world, agents, 'flowers', 'aggression', 'direct')

def logic_5776(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'aggression', 'direct')

def logic_5777(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'aggression', 'direct')

def logic_5778(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'aggression', 'direct')

def logic_5779(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'aggression', 'direct')

def logic_5780(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'aggression', 'direct')

def logic_5781(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'aggression', 'direct')

def logic_5782(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'aggression', 'direct')

def logic_5783(agents, world):
    _agent_apply(world, agents, 'hydration', 'aggression', 'direct')

def logic_5784(agents, world):
    _agent_apply(world, agents, 'thirst', 'aggression', 'direct')

def logic_5785(agents, world):
    _agent_apply(world, agents, 'hunger', 'aggression', 'direct')

def logic_5786(agents, world):
    _agent_apply(world, agents, 'health', 'aggression', 'direct')

def logic_5787(agents, world):
    _agent_apply(world, agents, 'stress', 'aggression', 'direct')

def logic_5788(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'aggression', 'direct')

def logic_5789(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'aggression', 'direct')

def logic_5790(agents, world):
    _agent_apply(world, agents, 'social_need', 'aggression', 'direct')

def logic_5791(agents, world):
    _agent_apply(world, agents, 'cooperation', 'aggression', 'direct')

def logic_5792(agents, world):
    _agent_apply(world, agents, 'defection', 'aggression', 'direct')

def logic_5793(agents, world):
    _agent_apply(world, agents, 'trust', 'aggression', 'direct')

def logic_5794(agents, world):
    _agent_apply(world, agents, 'reputation', 'aggression', 'direct')

def logic_5795(agents, world):
    _agent_apply(world, agents, 'help_received', 'aggression', 'direct')

def logic_5796(agents, world):
    _agent_apply(world, agents, 'help_given', 'aggression', 'direct')

def logic_5797(agents, world):
    _agent_apply(world, agents, 'local_density', 'aggression', 'direct')

def logic_5798(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'aggression', 'direct')

def logic_5799(agents, world):
    _agent_apply(world, agents, 'survival_score', 'aggression', 'direct')

def logic_5800(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'aggression', 'direct')

def logic_5801(agents, world):
    _agent_apply(world, agents, 'payoff', 'aggression', 'direct')

def logic_5802(agents, world):
    _agent_apply(world, agents, 'temperature', 'conflict_pressure', 'direct')

def logic_5803(agents, world):
    _agent_apply(world, agents, 'surface_water', 'conflict_pressure', 'direct')

def logic_5804(agents, world):
    _agent_apply(world, agents, 'humidity', 'conflict_pressure', 'direct')

def logic_5805(agents, world):
    _agent_apply(world, agents, 'cloud', 'conflict_pressure', 'direct')

def logic_5806(agents, world):
    _agent_apply(world, agents, 'rain', 'conflict_pressure', 'direct')

def logic_5807(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'conflict_pressure', 'direct')

def logic_5808(agents, world):
    _agent_apply(world, agents, 'runoff', 'conflict_pressure', 'direct')

def logic_5809(agents, world):
    _agent_apply(world, agents, 'wind_x', 'conflict_pressure', 'direct')

def logic_5810(agents, world):
    _agent_apply(world, agents, 'wind_y', 'conflict_pressure', 'direct')

def logic_5811(agents, world):
    _agent_apply(world, agents, 'vegetation', 'conflict_pressure', 'direct')

def logic_5812(agents, world):
    _agent_apply(world, agents, 'biomass', 'conflict_pressure', 'direct')

def logic_5813(agents, world):
    _agent_apply(world, agents, 'herbivore', 'conflict_pressure', 'direct')

def logic_5814(agents, world):
    _agent_apply(world, agents, 'predator', 'conflict_pressure', 'direct')

def logic_5815(agents, world):
    _agent_apply(world, agents, 'carrion', 'conflict_pressure', 'direct')

def logic_5816(agents, world):
    _agent_apply(world, agents, 'nutrients', 'conflict_pressure', 'direct')

def logic_5817(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'conflict_pressure', 'direct')

def logic_5818(agents, world):
    _agent_apply(world, agents, 'oxygen', 'conflict_pressure', 'direct')

def logic_5819(agents, world):
    _agent_apply(world, agents, 'co2', 'conflict_pressure', 'direct')

def logic_5820(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'conflict_pressure', 'direct')

def logic_5821(agents, world):
    _agent_apply(world, agents, 'ice', 'conflict_pressure', 'direct')

def logic_5822(agents, world):
    _agent_apply(world, agents, 'evaporation', 'conflict_pressure', 'direct')

def logic_5823(agents, world):
    _agent_apply(world, agents, 'detritus', 'conflict_pressure', 'direct')

def logic_5824(agents, world):
    _agent_apply(world, agents, 'methane', 'conflict_pressure', 'direct')

def logic_5825(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'conflict_pressure', 'direct')

def logic_5826(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'conflict_pressure', 'direct')

def logic_5827(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'conflict_pressure', 'direct')

def logic_5828(agents, world):
    _agent_apply(world, agents, 'erosion', 'conflict_pressure', 'direct')

def logic_5829(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'conflict_pressure', 'direct')

def logic_5830(agents, world):
    _agent_apply(world, agents, 'root_density', 'conflict_pressure', 'direct')

def logic_5831(agents, world):
    _agent_apply(world, agents, 'wetland', 'conflict_pressure', 'direct')

def logic_5832(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'conflict_pressure', 'direct')

def logic_5833(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'conflict_pressure', 'direct')

def logic_5834(agents, world):
    _agent_apply(world, agents, 'ash', 'conflict_pressure', 'direct')

def logic_5835(agents, world):
    _agent_apply(world, agents, 'snowpack', 'conflict_pressure', 'direct')

def logic_5836(agents, world):
    _agent_apply(world, agents, 'groundwater', 'conflict_pressure', 'direct')

def logic_5837(agents, world):
    _agent_apply(world, agents, 'sediment', 'conflict_pressure', 'direct')

def logic_5838(agents, world):
    _agent_apply(world, agents, 'salinity', 'conflict_pressure', 'direct')

def logic_5839(agents, world):
    _agent_apply(world, agents, 'algae', 'conflict_pressure', 'direct')

def logic_5840(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'conflict_pressure', 'direct')

def logic_5841(agents, world):
    _agent_apply(world, agents, 'deadwood', 'conflict_pressure', 'direct')

def logic_5842(agents, world):
    _agent_apply(world, agents, 'pollinators', 'conflict_pressure', 'direct')

def logic_5843(agents, world):
    _agent_apply(world, agents, 'flowers', 'conflict_pressure', 'direct')

def logic_5844(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'conflict_pressure', 'direct')

def logic_5845(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'conflict_pressure', 'direct')

def logic_5846(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'conflict_pressure', 'direct')

def logic_5847(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'conflict_pressure', 'direct')

def logic_5848(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'conflict_pressure', 'direct')

def logic_5849(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'conflict_pressure', 'direct')

def logic_5850(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'conflict_pressure', 'direct')

def logic_5851(agents, world):
    _agent_apply(world, agents, 'hydration', 'conflict_pressure', 'direct')

def logic_5852(agents, world):
    _agent_apply(world, agents, 'thirst', 'conflict_pressure', 'direct')

def logic_5853(agents, world):
    _agent_apply(world, agents, 'hunger', 'conflict_pressure', 'direct')

def logic_5854(agents, world):
    _agent_apply(world, agents, 'health', 'conflict_pressure', 'direct')

def logic_5855(agents, world):
    _agent_apply(world, agents, 'stress', 'conflict_pressure', 'direct')

def logic_5856(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'conflict_pressure', 'direct')

def logic_5857(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'conflict_pressure', 'direct')

def logic_5858(agents, world):
    _agent_apply(world, agents, 'social_need', 'conflict_pressure', 'direct')

def logic_5859(agents, world):
    _agent_apply(world, agents, 'cooperation', 'conflict_pressure', 'direct')

def logic_5860(agents, world):
    _agent_apply(world, agents, 'defection', 'conflict_pressure', 'direct')

def logic_5861(agents, world):
    _agent_apply(world, agents, 'trust', 'conflict_pressure', 'direct')

def logic_5862(agents, world):
    _agent_apply(world, agents, 'reputation', 'conflict_pressure', 'direct')

def logic_5863(agents, world):
    _agent_apply(world, agents, 'help_received', 'conflict_pressure', 'direct')

def logic_5864(agents, world):
    _agent_apply(world, agents, 'help_given', 'conflict_pressure', 'direct')

def logic_5865(agents, world):
    _agent_apply(world, agents, 'local_density', 'conflict_pressure', 'direct')

def logic_5866(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'conflict_pressure', 'direct')

def logic_5867(agents, world):
    _agent_apply(world, agents, 'survival_score', 'conflict_pressure', 'direct')

def logic_5868(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'conflict_pressure', 'direct')

def logic_5869(agents, world):
    _agent_apply(world, agents, 'payoff', 'conflict_pressure', 'direct')

def logic_5870(agents, world):
    _agent_apply(world, agents, 'temperature', 'competition_pressure', 'direct')

def logic_5871(agents, world):
    _agent_apply(world, agents, 'surface_water', 'competition_pressure', 'direct')

def logic_5872(agents, world):
    _agent_apply(world, agents, 'humidity', 'competition_pressure', 'direct')

def logic_5873(agents, world):
    _agent_apply(world, agents, 'cloud', 'competition_pressure', 'direct')

def logic_5874(agents, world):
    _agent_apply(world, agents, 'rain', 'competition_pressure', 'direct')

def logic_5875(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'competition_pressure', 'direct')

def logic_5876(agents, world):
    _agent_apply(world, agents, 'runoff', 'competition_pressure', 'direct')

def logic_5877(agents, world):
    _agent_apply(world, agents, 'wind_x', 'competition_pressure', 'direct')

def logic_5878(agents, world):
    _agent_apply(world, agents, 'wind_y', 'competition_pressure', 'direct')

def logic_5879(agents, world):
    _agent_apply(world, agents, 'vegetation', 'competition_pressure', 'direct')

def logic_5880(agents, world):
    _agent_apply(world, agents, 'biomass', 'competition_pressure', 'direct')

def logic_5881(agents, world):
    _agent_apply(world, agents, 'herbivore', 'competition_pressure', 'direct')

def logic_5882(agents, world):
    _agent_apply(world, agents, 'predator', 'competition_pressure', 'direct')

def logic_5883(agents, world):
    _agent_apply(world, agents, 'carrion', 'competition_pressure', 'direct')

def logic_5884(agents, world):
    _agent_apply(world, agents, 'nutrients', 'competition_pressure', 'direct')

def logic_5885(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'competition_pressure', 'direct')

def logic_5886(agents, world):
    _agent_apply(world, agents, 'oxygen', 'competition_pressure', 'direct')

def logic_5887(agents, world):
    _agent_apply(world, agents, 'co2', 'competition_pressure', 'direct')

def logic_5888(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'competition_pressure', 'direct')

def logic_5889(agents, world):
    _agent_apply(world, agents, 'ice', 'competition_pressure', 'direct')

def logic_5890(agents, world):
    _agent_apply(world, agents, 'evaporation', 'competition_pressure', 'direct')

def logic_5891(agents, world):
    _agent_apply(world, agents, 'detritus', 'competition_pressure', 'direct')

def logic_5892(agents, world):
    _agent_apply(world, agents, 'methane', 'competition_pressure', 'direct')

def logic_5893(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'competition_pressure', 'direct')

def logic_5894(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'competition_pressure', 'direct')

def logic_5895(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'competition_pressure', 'direct')

def logic_5896(agents, world):
    _agent_apply(world, agents, 'erosion', 'competition_pressure', 'direct')

def logic_5897(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'competition_pressure', 'direct')

def logic_5898(agents, world):
    _agent_apply(world, agents, 'root_density', 'competition_pressure', 'direct')

def logic_5899(agents, world):
    _agent_apply(world, agents, 'wetland', 'competition_pressure', 'direct')

def logic_5900(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'competition_pressure', 'direct')

def logic_5901(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'competition_pressure', 'direct')

def logic_5902(agents, world):
    _agent_apply(world, agents, 'ash', 'competition_pressure', 'direct')

def logic_5903(agents, world):
    _agent_apply(world, agents, 'snowpack', 'competition_pressure', 'direct')

def logic_5904(agents, world):
    _agent_apply(world, agents, 'groundwater', 'competition_pressure', 'direct')

def logic_5905(agents, world):
    _agent_apply(world, agents, 'sediment', 'competition_pressure', 'direct')

def logic_5906(agents, world):
    _agent_apply(world, agents, 'salinity', 'competition_pressure', 'direct')

def logic_5907(agents, world):
    _agent_apply(world, agents, 'algae', 'competition_pressure', 'direct')

def logic_5908(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'competition_pressure', 'direct')

def logic_5909(agents, world):
    _agent_apply(world, agents, 'deadwood', 'competition_pressure', 'direct')

def logic_5910(agents, world):
    _agent_apply(world, agents, 'pollinators', 'competition_pressure', 'direct')

def logic_5911(agents, world):
    _agent_apply(world, agents, 'flowers', 'competition_pressure', 'direct')

def logic_5912(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'competition_pressure', 'direct')

def logic_5913(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'competition_pressure', 'direct')

def logic_5914(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'competition_pressure', 'direct')

def logic_5915(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'competition_pressure', 'direct')

def logic_5916(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'competition_pressure', 'direct')

def logic_5917(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'competition_pressure', 'direct')

def logic_5918(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'competition_pressure', 'direct')

def logic_5919(agents, world):
    _agent_apply(world, agents, 'hydration', 'competition_pressure', 'direct')

def logic_5920(agents, world):
    _agent_apply(world, agents, 'thirst', 'competition_pressure', 'direct')

def logic_5921(agents, world):
    _agent_apply(world, agents, 'hunger', 'competition_pressure', 'direct')

def logic_5922(agents, world):
    _agent_apply(world, agents, 'health', 'competition_pressure', 'direct')

def logic_5923(agents, world):
    _agent_apply(world, agents, 'stress', 'competition_pressure', 'direct')

def logic_5924(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'competition_pressure', 'direct')

def logic_5925(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'competition_pressure', 'direct')

def logic_5926(agents, world):
    _agent_apply(world, agents, 'social_need', 'competition_pressure', 'direct')

def logic_5927(agents, world):
    _agent_apply(world, agents, 'cooperation', 'competition_pressure', 'direct')

def logic_5928(agents, world):
    _agent_apply(world, agents, 'defection', 'competition_pressure', 'direct')

def logic_5929(agents, world):
    _agent_apply(world, agents, 'trust', 'competition_pressure', 'direct')

def logic_5930(agents, world):
    _agent_apply(world, agents, 'reputation', 'competition_pressure', 'direct')

def logic_5931(agents, world):
    _agent_apply(world, agents, 'help_received', 'competition_pressure', 'direct')

def logic_5932(agents, world):
    _agent_apply(world, agents, 'help_given', 'competition_pressure', 'direct')

def logic_5933(agents, world):
    _agent_apply(world, agents, 'local_density', 'competition_pressure', 'direct')

def logic_5934(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'competition_pressure', 'direct')

def logic_5935(agents, world):
    _agent_apply(world, agents, 'survival_score', 'competition_pressure', 'direct')

def logic_5936(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'competition_pressure', 'direct')

def logic_5937(agents, world):
    _agent_apply(world, agents, 'payoff', 'competition_pressure', 'direct')

def logic_5938(agents, world):
    _agent_apply(world, agents, 'temperature', 'territoriality', 'direct')

def logic_5939(agents, world):
    _agent_apply(world, agents, 'surface_water', 'territoriality', 'direct')

def logic_5940(agents, world):
    _agent_apply(world, agents, 'humidity', 'territoriality', 'direct')

def logic_5941(agents, world):
    _agent_apply(world, agents, 'cloud', 'territoriality', 'direct')

def logic_5942(agents, world):
    _agent_apply(world, agents, 'rain', 'territoriality', 'direct')

def logic_5943(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'territoriality', 'direct')

def logic_5944(agents, world):
    _agent_apply(world, agents, 'runoff', 'territoriality', 'direct')

def logic_5945(agents, world):
    _agent_apply(world, agents, 'wind_x', 'territoriality', 'direct')

def logic_5946(agents, world):
    _agent_apply(world, agents, 'wind_y', 'territoriality', 'direct')

def logic_5947(agents, world):
    _agent_apply(world, agents, 'vegetation', 'territoriality', 'direct')

def logic_5948(agents, world):
    _agent_apply(world, agents, 'biomass', 'territoriality', 'direct')

def logic_5949(agents, world):
    _agent_apply(world, agents, 'herbivore', 'territoriality', 'direct')

def logic_5950(agents, world):
    _agent_apply(world, agents, 'predator', 'territoriality', 'direct')

def logic_5951(agents, world):
    _agent_apply(world, agents, 'carrion', 'territoriality', 'direct')

def logic_5952(agents, world):
    _agent_apply(world, agents, 'nutrients', 'territoriality', 'direct')

def logic_5953(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'territoriality', 'direct')

def logic_5954(agents, world):
    _agent_apply(world, agents, 'oxygen', 'territoriality', 'direct')

def logic_5955(agents, world):
    _agent_apply(world, agents, 'co2', 'territoriality', 'direct')

def logic_5956(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'territoriality', 'direct')

def logic_5957(agents, world):
    _agent_apply(world, agents, 'ice', 'territoriality', 'direct')

def logic_5958(agents, world):
    _agent_apply(world, agents, 'evaporation', 'territoriality', 'direct')

def logic_5959(agents, world):
    _agent_apply(world, agents, 'detritus', 'territoriality', 'direct')

def logic_5960(agents, world):
    _agent_apply(world, agents, 'methane', 'territoriality', 'direct')

def logic_5961(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'territoriality', 'direct')

def logic_5962(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'territoriality', 'direct')

def logic_5963(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'territoriality', 'direct')

def logic_5964(agents, world):
    _agent_apply(world, agents, 'erosion', 'territoriality', 'direct')

def logic_5965(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'territoriality', 'direct')

def logic_5966(agents, world):
    _agent_apply(world, agents, 'root_density', 'territoriality', 'direct')

def logic_5967(agents, world):
    _agent_apply(world, agents, 'wetland', 'territoriality', 'direct')

def logic_5968(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'territoriality', 'direct')

def logic_5969(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'territoriality', 'direct')

def logic_5970(agents, world):
    _agent_apply(world, agents, 'ash', 'territoriality', 'direct')

def logic_5971(agents, world):
    _agent_apply(world, agents, 'snowpack', 'territoriality', 'direct')

def logic_5972(agents, world):
    _agent_apply(world, agents, 'groundwater', 'territoriality', 'direct')

def logic_5973(agents, world):
    _agent_apply(world, agents, 'sediment', 'territoriality', 'direct')

def logic_5974(agents, world):
    _agent_apply(world, agents, 'salinity', 'territoriality', 'direct')

def logic_5975(agents, world):
    _agent_apply(world, agents, 'algae', 'territoriality', 'direct')

def logic_5976(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'territoriality', 'direct')

def logic_5977(agents, world):
    _agent_apply(world, agents, 'deadwood', 'territoriality', 'direct')

def logic_5978(agents, world):
    _agent_apply(world, agents, 'pollinators', 'territoriality', 'direct')

def logic_5979(agents, world):
    _agent_apply(world, agents, 'flowers', 'territoriality', 'direct')

def logic_5980(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'territoriality', 'direct')

def logic_5981(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'territoriality', 'direct')

def logic_5982(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'territoriality', 'direct')

def logic_5983(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'territoriality', 'direct')

def logic_5984(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'territoriality', 'direct')

def logic_5985(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'territoriality', 'direct')

def logic_5986(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'territoriality', 'direct')

def logic_5987(agents, world):
    _agent_apply(world, agents, 'hydration', 'territoriality', 'direct')

def logic_5988(agents, world):
    _agent_apply(world, agents, 'thirst', 'territoriality', 'direct')

def logic_5989(agents, world):
    _agent_apply(world, agents, 'hunger', 'territoriality', 'direct')

def logic_5990(agents, world):
    _agent_apply(world, agents, 'health', 'territoriality', 'direct')

def logic_5991(agents, world):
    _agent_apply(world, agents, 'stress', 'territoriality', 'direct')

def logic_5992(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'territoriality', 'direct')

def logic_5993(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'territoriality', 'direct')

def logic_5994(agents, world):
    _agent_apply(world, agents, 'social_need', 'territoriality', 'direct')

def logic_5995(agents, world):
    _agent_apply(world, agents, 'cooperation', 'territoriality', 'direct')

def logic_5996(agents, world):
    _agent_apply(world, agents, 'defection', 'territoriality', 'direct')

def logic_5997(agents, world):
    _agent_apply(world, agents, 'trust', 'territoriality', 'direct')

def logic_5998(agents, world):
    _agent_apply(world, agents, 'reputation', 'territoriality', 'direct')

def logic_5999(agents, world):
    _agent_apply(world, agents, 'help_received', 'territoriality', 'direct')

def logic_6000(agents, world):
    _agent_apply(world, agents, 'help_given', 'territoriality', 'direct')

def logic_6001(agents, world):
    _agent_apply(world, agents, 'local_density', 'territoriality', 'direct')

def logic_6002(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'territoriality', 'direct')

def logic_6003(agents, world):
    _agent_apply(world, agents, 'survival_score', 'territoriality', 'direct')

def logic_6004(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'territoriality', 'direct')

def logic_6005(agents, world):
    _agent_apply(world, agents, 'payoff', 'territoriality', 'direct')

def logic_6006(agents, world):
    _agent_apply(world, agents, 'temperature', 'group_stability', 'direct')

def logic_6007(agents, world):
    _agent_apply(world, agents, 'surface_water', 'group_stability', 'direct')

def logic_6008(agents, world):
    _agent_apply(world, agents, 'humidity', 'group_stability', 'direct')

def logic_6009(agents, world):
    _agent_apply(world, agents, 'cloud', 'group_stability', 'direct')

def logic_6010(agents, world):
    _agent_apply(world, agents, 'rain', 'group_stability', 'direct')

def logic_6011(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'group_stability', 'direct')

def logic_6012(agents, world):
    _agent_apply(world, agents, 'runoff', 'group_stability', 'direct')

def logic_6013(agents, world):
    _agent_apply(world, agents, 'wind_x', 'group_stability', 'direct')

def logic_6014(agents, world):
    _agent_apply(world, agents, 'wind_y', 'group_stability', 'direct')

def logic_6015(agents, world):
    _agent_apply(world, agents, 'vegetation', 'group_stability', 'direct')

def logic_6016(agents, world):
    _agent_apply(world, agents, 'biomass', 'group_stability', 'direct')

def logic_6017(agents, world):
    _agent_apply(world, agents, 'herbivore', 'group_stability', 'direct')

def logic_6018(agents, world):
    _agent_apply(world, agents, 'predator', 'group_stability', 'direct')

def logic_6019(agents, world):
    _agent_apply(world, agents, 'carrion', 'group_stability', 'direct')

def logic_6020(agents, world):
    _agent_apply(world, agents, 'nutrients', 'group_stability', 'direct')

def logic_6021(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'group_stability', 'direct')

def logic_6022(agents, world):
    _agent_apply(world, agents, 'oxygen', 'group_stability', 'direct')

def logic_6023(agents, world):
    _agent_apply(world, agents, 'co2', 'group_stability', 'direct')

def logic_6024(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'group_stability', 'direct')

def logic_6025(agents, world):
    _agent_apply(world, agents, 'ice', 'group_stability', 'direct')

def logic_6026(agents, world):
    _agent_apply(world, agents, 'evaporation', 'group_stability', 'direct')

def logic_6027(agents, world):
    _agent_apply(world, agents, 'detritus', 'group_stability', 'direct')

def logic_6028(agents, world):
    _agent_apply(world, agents, 'methane', 'group_stability', 'direct')

def logic_6029(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'group_stability', 'direct')

def logic_6030(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'group_stability', 'direct')

def logic_6031(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'group_stability', 'direct')

def logic_6032(agents, world):
    _agent_apply(world, agents, 'erosion', 'group_stability', 'direct')

def logic_6033(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'group_stability', 'direct')

def logic_6034(agents, world):
    _agent_apply(world, agents, 'root_density', 'group_stability', 'direct')

def logic_6035(agents, world):
    _agent_apply(world, agents, 'wetland', 'group_stability', 'direct')

def logic_6036(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'group_stability', 'direct')

def logic_6037(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'group_stability', 'direct')

def logic_6038(agents, world):
    _agent_apply(world, agents, 'ash', 'group_stability', 'direct')

def logic_6039(agents, world):
    _agent_apply(world, agents, 'snowpack', 'group_stability', 'direct')

def logic_6040(agents, world):
    _agent_apply(world, agents, 'groundwater', 'group_stability', 'direct')

def logic_6041(agents, world):
    _agent_apply(world, agents, 'sediment', 'group_stability', 'direct')

def logic_6042(agents, world):
    _agent_apply(world, agents, 'salinity', 'group_stability', 'direct')

def logic_6043(agents, world):
    _agent_apply(world, agents, 'algae', 'group_stability', 'direct')

def logic_6044(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'group_stability', 'direct')

def logic_6045(agents, world):
    _agent_apply(world, agents, 'deadwood', 'group_stability', 'direct')

def logic_6046(agents, world):
    _agent_apply(world, agents, 'pollinators', 'group_stability', 'direct')

def logic_6047(agents, world):
    _agent_apply(world, agents, 'flowers', 'group_stability', 'direct')

def logic_6048(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'group_stability', 'direct')

def logic_6049(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'group_stability', 'direct')

def logic_6050(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'group_stability', 'direct')

def logic_6051(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'group_stability', 'direct')

def logic_6052(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'group_stability', 'direct')

def logic_6053(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'group_stability', 'direct')

def logic_6054(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'group_stability', 'direct')

def logic_6055(agents, world):
    _agent_apply(world, agents, 'hydration', 'group_stability', 'direct')

def logic_6056(agents, world):
    _agent_apply(world, agents, 'thirst', 'group_stability', 'direct')

def logic_6057(agents, world):
    _agent_apply(world, agents, 'hunger', 'group_stability', 'direct')

def logic_6058(agents, world):
    _agent_apply(world, agents, 'health', 'group_stability', 'direct')

def logic_6059(agents, world):
    _agent_apply(world, agents, 'stress', 'group_stability', 'direct')

def logic_6060(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'group_stability', 'direct')

def logic_6061(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'group_stability', 'direct')

def logic_6062(agents, world):
    _agent_apply(world, agents, 'social_need', 'group_stability', 'direct')

def logic_6063(agents, world):
    _agent_apply(world, agents, 'cooperation', 'group_stability', 'direct')

def logic_6064(agents, world):
    _agent_apply(world, agents, 'defection', 'group_stability', 'direct')

def logic_6065(agents, world):
    _agent_apply(world, agents, 'trust', 'group_stability', 'direct')

def logic_6066(agents, world):
    _agent_apply(world, agents, 'reputation', 'group_stability', 'direct')

def logic_6067(agents, world):
    _agent_apply(world, agents, 'help_received', 'group_stability', 'direct')

def logic_6068(agents, world):
    _agent_apply(world, agents, 'help_given', 'group_stability', 'direct')

def logic_6069(agents, world):
    _agent_apply(world, agents, 'local_density', 'group_stability', 'direct')

def logic_6070(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'group_stability', 'direct')

def logic_6071(agents, world):
    _agent_apply(world, agents, 'survival_score', 'group_stability', 'direct')

def logic_6072(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'group_stability', 'direct')

def logic_6073(agents, world):
    _agent_apply(world, agents, 'payoff', 'group_stability', 'direct')

def logic_6074(agents, world):
    _agent_apply(world, agents, 'temperature', 'sharing_capacity', 'direct')

def logic_6075(agents, world):
    _agent_apply(world, agents, 'surface_water', 'sharing_capacity', 'direct')

def logic_6076(agents, world):
    _agent_apply(world, agents, 'humidity', 'sharing_capacity', 'direct')

def logic_6077(agents, world):
    _agent_apply(world, agents, 'cloud', 'sharing_capacity', 'direct')

def logic_6078(agents, world):
    _agent_apply(world, agents, 'rain', 'sharing_capacity', 'direct')

def logic_6079(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'sharing_capacity', 'direct')

def logic_6080(agents, world):
    _agent_apply(world, agents, 'runoff', 'sharing_capacity', 'direct')

def logic_6081(agents, world):
    _agent_apply(world, agents, 'wind_x', 'sharing_capacity', 'direct')

def logic_6082(agents, world):
    _agent_apply(world, agents, 'wind_y', 'sharing_capacity', 'direct')

def logic_6083(agents, world):
    _agent_apply(world, agents, 'vegetation', 'sharing_capacity', 'direct')

def logic_6084(agents, world):
    _agent_apply(world, agents, 'biomass', 'sharing_capacity', 'direct')

def logic_6085(agents, world):
    _agent_apply(world, agents, 'herbivore', 'sharing_capacity', 'direct')

def logic_6086(agents, world):
    _agent_apply(world, agents, 'predator', 'sharing_capacity', 'direct')

def logic_6087(agents, world):
    _agent_apply(world, agents, 'carrion', 'sharing_capacity', 'direct')

def logic_6088(agents, world):
    _agent_apply(world, agents, 'nutrients', 'sharing_capacity', 'direct')

def logic_6089(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'sharing_capacity', 'direct')

def logic_6090(agents, world):
    _agent_apply(world, agents, 'oxygen', 'sharing_capacity', 'direct')

def logic_6091(agents, world):
    _agent_apply(world, agents, 'co2', 'sharing_capacity', 'direct')

def logic_6092(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'sharing_capacity', 'direct')

def logic_6093(agents, world):
    _agent_apply(world, agents, 'ice', 'sharing_capacity', 'direct')

def logic_6094(agents, world):
    _agent_apply(world, agents, 'evaporation', 'sharing_capacity', 'direct')

def logic_6095(agents, world):
    _agent_apply(world, agents, 'detritus', 'sharing_capacity', 'direct')

def logic_6096(agents, world):
    _agent_apply(world, agents, 'methane', 'sharing_capacity', 'direct')

def logic_6097(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'sharing_capacity', 'direct')

def logic_6098(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'sharing_capacity', 'direct')

def logic_6099(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'sharing_capacity', 'direct')

def logic_6100(agents, world):
    _agent_apply(world, agents, 'erosion', 'sharing_capacity', 'direct')

def logic_6101(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'sharing_capacity', 'direct')

def logic_6102(agents, world):
    _agent_apply(world, agents, 'root_density', 'sharing_capacity', 'direct')

def logic_6103(agents, world):
    _agent_apply(world, agents, 'wetland', 'sharing_capacity', 'direct')

def logic_6104(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'sharing_capacity', 'direct')

def logic_6105(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'sharing_capacity', 'direct')

def logic_6106(agents, world):
    _agent_apply(world, agents, 'ash', 'sharing_capacity', 'direct')

def logic_6107(agents, world):
    _agent_apply(world, agents, 'snowpack', 'sharing_capacity', 'direct')

def logic_6108(agents, world):
    _agent_apply(world, agents, 'groundwater', 'sharing_capacity', 'direct')

def logic_6109(agents, world):
    _agent_apply(world, agents, 'sediment', 'sharing_capacity', 'direct')

def logic_6110(agents, world):
    _agent_apply(world, agents, 'salinity', 'sharing_capacity', 'direct')

def logic_6111(agents, world):
    _agent_apply(world, agents, 'algae', 'sharing_capacity', 'direct')

def logic_6112(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'sharing_capacity', 'direct')

def logic_6113(agents, world):
    _agent_apply(world, agents, 'deadwood', 'sharing_capacity', 'direct')

def logic_6114(agents, world):
    _agent_apply(world, agents, 'pollinators', 'sharing_capacity', 'direct')

def logic_6115(agents, world):
    _agent_apply(world, agents, 'flowers', 'sharing_capacity', 'direct')

def logic_6116(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'sharing_capacity', 'direct')

def logic_6117(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'sharing_capacity', 'direct')

def logic_6118(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'sharing_capacity', 'direct')

def logic_6119(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'sharing_capacity', 'direct')

def logic_6120(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'sharing_capacity', 'direct')

def logic_6121(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'sharing_capacity', 'direct')

def logic_6122(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'sharing_capacity', 'direct')

def logic_6123(agents, world):
    _agent_apply(world, agents, 'hydration', 'sharing_capacity', 'direct')

def logic_6124(agents, world):
    _agent_apply(world, agents, 'thirst', 'sharing_capacity', 'direct')

def logic_6125(agents, world):
    _agent_apply(world, agents, 'hunger', 'sharing_capacity', 'direct')

def logic_6126(agents, world):
    _agent_apply(world, agents, 'health', 'sharing_capacity', 'direct')

def logic_6127(agents, world):
    _agent_apply(world, agents, 'stress', 'sharing_capacity', 'direct')

def logic_6128(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'sharing_capacity', 'direct')

def logic_6129(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'sharing_capacity', 'direct')

def logic_6130(agents, world):
    _agent_apply(world, agents, 'social_need', 'sharing_capacity', 'direct')

def logic_6131(agents, world):
    _agent_apply(world, agents, 'cooperation', 'sharing_capacity', 'direct')

def logic_6132(agents, world):
    _agent_apply(world, agents, 'defection', 'sharing_capacity', 'direct')

def logic_6133(agents, world):
    _agent_apply(world, agents, 'trust', 'sharing_capacity', 'direct')

def logic_6134(agents, world):
    _agent_apply(world, agents, 'reputation', 'sharing_capacity', 'direct')

def logic_6135(agents, world):
    _agent_apply(world, agents, 'help_received', 'sharing_capacity', 'direct')

def logic_6136(agents, world):
    _agent_apply(world, agents, 'help_given', 'sharing_capacity', 'direct')

def logic_6137(agents, world):
    _agent_apply(world, agents, 'local_density', 'sharing_capacity', 'direct')

def logic_6138(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'sharing_capacity', 'direct')

def logic_6139(agents, world):
    _agent_apply(world, agents, 'survival_score', 'sharing_capacity', 'direct')

def logic_6140(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'sharing_capacity', 'direct')

def logic_6141(agents, world):
    _agent_apply(world, agents, 'payoff', 'sharing_capacity', 'direct')

def logic_6142(agents, world):
    _agent_apply(world, agents, 'temperature', 'help_drive', 'direct')

def logic_6143(agents, world):
    _agent_apply(world, agents, 'surface_water', 'help_drive', 'direct')

def logic_6144(agents, world):
    _agent_apply(world, agents, 'humidity', 'help_drive', 'direct')

def logic_6145(agents, world):
    _agent_apply(world, agents, 'cloud', 'help_drive', 'direct')

def logic_6146(agents, world):
    _agent_apply(world, agents, 'rain', 'help_drive', 'direct')

def logic_6147(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'help_drive', 'direct')

def logic_6148(agents, world):
    _agent_apply(world, agents, 'runoff', 'help_drive', 'direct')

def logic_6149(agents, world):
    _agent_apply(world, agents, 'wind_x', 'help_drive', 'direct')

def logic_6150(agents, world):
    _agent_apply(world, agents, 'wind_y', 'help_drive', 'direct')

def logic_6151(agents, world):
    _agent_apply(world, agents, 'vegetation', 'help_drive', 'direct')

def logic_6152(agents, world):
    _agent_apply(world, agents, 'biomass', 'help_drive', 'direct')

def logic_6153(agents, world):
    _agent_apply(world, agents, 'herbivore', 'help_drive', 'direct')

def logic_6154(agents, world):
    _agent_apply(world, agents, 'predator', 'help_drive', 'direct')

def logic_6155(agents, world):
    _agent_apply(world, agents, 'carrion', 'help_drive', 'direct')

def logic_6156(agents, world):
    _agent_apply(world, agents, 'nutrients', 'help_drive', 'direct')

def logic_6157(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'help_drive', 'direct')

def logic_6158(agents, world):
    _agent_apply(world, agents, 'oxygen', 'help_drive', 'direct')

def logic_6159(agents, world):
    _agent_apply(world, agents, 'co2', 'help_drive', 'direct')

def logic_6160(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'help_drive', 'direct')

def logic_6161(agents, world):
    _agent_apply(world, agents, 'ice', 'help_drive', 'direct')

def logic_6162(agents, world):
    _agent_apply(world, agents, 'evaporation', 'help_drive', 'direct')

def logic_6163(agents, world):
    _agent_apply(world, agents, 'detritus', 'help_drive', 'direct')

def logic_6164(agents, world):
    _agent_apply(world, agents, 'methane', 'help_drive', 'direct')

def logic_6165(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'help_drive', 'direct')

def logic_6166(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'help_drive', 'direct')

def logic_6167(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'help_drive', 'direct')

def logic_6168(agents, world):
    _agent_apply(world, agents, 'erosion', 'help_drive', 'direct')

def logic_6169(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'help_drive', 'direct')

def logic_6170(agents, world):
    _agent_apply(world, agents, 'root_density', 'help_drive', 'direct')

def logic_6171(agents, world):
    _agent_apply(world, agents, 'wetland', 'help_drive', 'direct')

def logic_6172(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'help_drive', 'direct')

def logic_6173(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'help_drive', 'direct')

def logic_6174(agents, world):
    _agent_apply(world, agents, 'ash', 'help_drive', 'direct')

def logic_6175(agents, world):
    _agent_apply(world, agents, 'snowpack', 'help_drive', 'direct')

def logic_6176(agents, world):
    _agent_apply(world, agents, 'groundwater', 'help_drive', 'direct')

def logic_6177(agents, world):
    _agent_apply(world, agents, 'sediment', 'help_drive', 'direct')

def logic_6178(agents, world):
    _agent_apply(world, agents, 'salinity', 'help_drive', 'direct')

def logic_6179(agents, world):
    _agent_apply(world, agents, 'algae', 'help_drive', 'direct')

def logic_6180(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'help_drive', 'direct')

def logic_6181(agents, world):
    _agent_apply(world, agents, 'deadwood', 'help_drive', 'direct')

def logic_6182(agents, world):
    _agent_apply(world, agents, 'pollinators', 'help_drive', 'direct')

def logic_6183(agents, world):
    _agent_apply(world, agents, 'flowers', 'help_drive', 'direct')

def logic_6184(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'help_drive', 'direct')

def logic_6185(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'help_drive', 'direct')

def logic_6186(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'help_drive', 'direct')

def logic_6187(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'help_drive', 'direct')

def logic_6188(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'help_drive', 'direct')

def logic_6189(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'help_drive', 'direct')

def logic_6190(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'help_drive', 'direct')

def logic_6191(agents, world):
    _agent_apply(world, agents, 'hydration', 'help_drive', 'direct')

def logic_6192(agents, world):
    _agent_apply(world, agents, 'thirst', 'help_drive', 'direct')

def logic_6193(agents, world):
    _agent_apply(world, agents, 'hunger', 'help_drive', 'direct')

def logic_6194(agents, world):
    _agent_apply(world, agents, 'health', 'help_drive', 'direct')

def logic_6195(agents, world):
    _agent_apply(world, agents, 'stress', 'help_drive', 'direct')

def logic_6196(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'help_drive', 'direct')

def logic_6197(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'help_drive', 'direct')

def logic_6198(agents, world):
    _agent_apply(world, agents, 'social_need', 'help_drive', 'direct')

def logic_6199(agents, world):
    _agent_apply(world, agents, 'cooperation', 'help_drive', 'direct')

def logic_6200(agents, world):
    _agent_apply(world, agents, 'defection', 'help_drive', 'direct')

def logic_6201(agents, world):
    _agent_apply(world, agents, 'trust', 'help_drive', 'direct')

def logic_6202(agents, world):
    _agent_apply(world, agents, 'reputation', 'help_drive', 'direct')

def logic_6203(agents, world):
    _agent_apply(world, agents, 'help_received', 'help_drive', 'direct')

def logic_6204(agents, world):
    _agent_apply(world, agents, 'help_given', 'help_drive', 'direct')

def logic_6205(agents, world):
    _agent_apply(world, agents, 'local_density', 'help_drive', 'direct')

def logic_6206(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'help_drive', 'direct')

def logic_6207(agents, world):
    _agent_apply(world, agents, 'survival_score', 'help_drive', 'direct')

def logic_6208(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'help_drive', 'direct')

def logic_6209(agents, world):
    _agent_apply(world, agents, 'payoff', 'help_drive', 'direct')

def logic_6210(agents, world):
    _agent_apply(world, agents, 'temperature', 'social_avoidance', 'direct')

def logic_6211(agents, world):
    _agent_apply(world, agents, 'surface_water', 'social_avoidance', 'direct')

def logic_6212(agents, world):
    _agent_apply(world, agents, 'humidity', 'social_avoidance', 'direct')

def logic_6213(agents, world):
    _agent_apply(world, agents, 'cloud', 'social_avoidance', 'direct')

def logic_6214(agents, world):
    _agent_apply(world, agents, 'rain', 'social_avoidance', 'direct')

def logic_6215(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'social_avoidance', 'direct')

def logic_6216(agents, world):
    _agent_apply(world, agents, 'runoff', 'social_avoidance', 'direct')

def logic_6217(agents, world):
    _agent_apply(world, agents, 'wind_x', 'social_avoidance', 'direct')

def logic_6218(agents, world):
    _agent_apply(world, agents, 'wind_y', 'social_avoidance', 'direct')

def logic_6219(agents, world):
    _agent_apply(world, agents, 'vegetation', 'social_avoidance', 'direct')

def logic_6220(agents, world):
    _agent_apply(world, agents, 'biomass', 'social_avoidance', 'direct')

def logic_6221(agents, world):
    _agent_apply(world, agents, 'herbivore', 'social_avoidance', 'direct')

def logic_6222(agents, world):
    _agent_apply(world, agents, 'predator', 'social_avoidance', 'direct')

def logic_6223(agents, world):
    _agent_apply(world, agents, 'carrion', 'social_avoidance', 'direct')

def logic_6224(agents, world):
    _agent_apply(world, agents, 'nutrients', 'social_avoidance', 'direct')

def logic_6225(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'social_avoidance', 'direct')

def logic_6226(agents, world):
    _agent_apply(world, agents, 'oxygen', 'social_avoidance', 'direct')

def logic_6227(agents, world):
    _agent_apply(world, agents, 'co2', 'social_avoidance', 'direct')

def logic_6228(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'social_avoidance', 'direct')

def logic_6229(agents, world):
    _agent_apply(world, agents, 'ice', 'social_avoidance', 'direct')

def logic_6230(agents, world):
    _agent_apply(world, agents, 'evaporation', 'social_avoidance', 'direct')

def logic_6231(agents, world):
    _agent_apply(world, agents, 'detritus', 'social_avoidance', 'direct')

def logic_6232(agents, world):
    _agent_apply(world, agents, 'methane', 'social_avoidance', 'direct')

def logic_6233(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'social_avoidance', 'direct')

def logic_6234(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'social_avoidance', 'direct')

def logic_6235(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'social_avoidance', 'direct')

def logic_6236(agents, world):
    _agent_apply(world, agents, 'erosion', 'social_avoidance', 'direct')

def logic_6237(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'social_avoidance', 'direct')

def logic_6238(agents, world):
    _agent_apply(world, agents, 'root_density', 'social_avoidance', 'direct')

def logic_6239(agents, world):
    _agent_apply(world, agents, 'wetland', 'social_avoidance', 'direct')

def logic_6240(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'social_avoidance', 'direct')

def logic_6241(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'social_avoidance', 'direct')

def logic_6242(agents, world):
    _agent_apply(world, agents, 'ash', 'social_avoidance', 'direct')

def logic_6243(agents, world):
    _agent_apply(world, agents, 'snowpack', 'social_avoidance', 'direct')

def logic_6244(agents, world):
    _agent_apply(world, agents, 'groundwater', 'social_avoidance', 'direct')

def logic_6245(agents, world):
    _agent_apply(world, agents, 'sediment', 'social_avoidance', 'direct')

def logic_6246(agents, world):
    _agent_apply(world, agents, 'salinity', 'social_avoidance', 'direct')

def logic_6247(agents, world):
    _agent_apply(world, agents, 'algae', 'social_avoidance', 'direct')

def logic_6248(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'social_avoidance', 'direct')

def logic_6249(agents, world):
    _agent_apply(world, agents, 'deadwood', 'social_avoidance', 'direct')

def logic_6250(agents, world):
    _agent_apply(world, agents, 'pollinators', 'social_avoidance', 'direct')

def logic_6251(agents, world):
    _agent_apply(world, agents, 'flowers', 'social_avoidance', 'direct')

def logic_6252(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'social_avoidance', 'direct')

def logic_6253(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'social_avoidance', 'direct')

def logic_6254(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'social_avoidance', 'direct')

def logic_6255(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'social_avoidance', 'direct')

def logic_6256(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'social_avoidance', 'direct')

def logic_6257(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'social_avoidance', 'direct')

def logic_6258(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'social_avoidance', 'direct')

def logic_6259(agents, world):
    _agent_apply(world, agents, 'hydration', 'social_avoidance', 'direct')

def logic_6260(agents, world):
    _agent_apply(world, agents, 'thirst', 'social_avoidance', 'direct')

def logic_6261(agents, world):
    _agent_apply(world, agents, 'hunger', 'social_avoidance', 'direct')

def logic_6262(agents, world):
    _agent_apply(world, agents, 'health', 'social_avoidance', 'direct')

def logic_6263(agents, world):
    _agent_apply(world, agents, 'stress', 'social_avoidance', 'direct')

def logic_6264(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'social_avoidance', 'direct')

def logic_6265(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'social_avoidance', 'direct')

def logic_6266(agents, world):
    _agent_apply(world, agents, 'social_need', 'social_avoidance', 'direct')

def logic_6267(agents, world):
    _agent_apply(world, agents, 'cooperation', 'social_avoidance', 'direct')

def logic_6268(agents, world):
    _agent_apply(world, agents, 'defection', 'social_avoidance', 'direct')

def logic_6269(agents, world):
    _agent_apply(world, agents, 'trust', 'social_avoidance', 'direct')

def logic_6270(agents, world):
    _agent_apply(world, agents, 'reputation', 'social_avoidance', 'direct')

def logic_6271(agents, world):
    _agent_apply(world, agents, 'help_received', 'social_avoidance', 'direct')

def logic_6272(agents, world):
    _agent_apply(world, agents, 'help_given', 'social_avoidance', 'direct')

def logic_6273(agents, world):
    _agent_apply(world, agents, 'local_density', 'social_avoidance', 'direct')

def logic_6274(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'social_avoidance', 'direct')

def logic_6275(agents, world):
    _agent_apply(world, agents, 'survival_score', 'social_avoidance', 'direct')

def logic_6276(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'social_avoidance', 'direct')

def logic_6277(agents, world):
    _agent_apply(world, agents, 'payoff', 'social_avoidance', 'direct')

def logic_6278(agents, world):
    _agent_apply(world, agents, 'temperature', 'selfishness', 'direct')

def logic_6279(agents, world):
    _agent_apply(world, agents, 'surface_water', 'selfishness', 'direct')

def logic_6280(agents, world):
    _agent_apply(world, agents, 'humidity', 'selfishness', 'direct')

def logic_6281(agents, world):
    _agent_apply(world, agents, 'cloud', 'selfishness', 'direct')

def logic_6282(agents, world):
    _agent_apply(world, agents, 'rain', 'selfishness', 'direct')

def logic_6283(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'selfishness', 'direct')

def logic_6284(agents, world):
    _agent_apply(world, agents, 'runoff', 'selfishness', 'direct')

def logic_6285(agents, world):
    _agent_apply(world, agents, 'wind_x', 'selfishness', 'direct')

def logic_6286(agents, world):
    _agent_apply(world, agents, 'wind_y', 'selfishness', 'direct')

def logic_6287(agents, world):
    _agent_apply(world, agents, 'vegetation', 'selfishness', 'direct')

def logic_6288(agents, world):
    _agent_apply(world, agents, 'biomass', 'selfishness', 'direct')

def logic_6289(agents, world):
    _agent_apply(world, agents, 'herbivore', 'selfishness', 'direct')

def logic_6290(agents, world):
    _agent_apply(world, agents, 'predator', 'selfishness', 'direct')

def logic_6291(agents, world):
    _agent_apply(world, agents, 'carrion', 'selfishness', 'direct')

def logic_6292(agents, world):
    _agent_apply(world, agents, 'nutrients', 'selfishness', 'direct')

def logic_6293(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'selfishness', 'direct')

def logic_6294(agents, world):
    _agent_apply(world, agents, 'oxygen', 'selfishness', 'direct')

def logic_6295(agents, world):
    _agent_apply(world, agents, 'co2', 'selfishness', 'direct')

def logic_6296(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'selfishness', 'direct')

def logic_6297(agents, world):
    _agent_apply(world, agents, 'ice', 'selfishness', 'direct')

def logic_6298(agents, world):
    _agent_apply(world, agents, 'evaporation', 'selfishness', 'direct')

def logic_6299(agents, world):
    _agent_apply(world, agents, 'detritus', 'selfishness', 'direct')

def logic_6300(agents, world):
    _agent_apply(world, agents, 'methane', 'selfishness', 'direct')

def logic_6301(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'selfishness', 'direct')

def logic_6302(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'selfishness', 'direct')

def logic_6303(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'selfishness', 'direct')

def logic_6304(agents, world):
    _agent_apply(world, agents, 'erosion', 'selfishness', 'direct')

def logic_6305(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'selfishness', 'direct')

def logic_6306(agents, world):
    _agent_apply(world, agents, 'root_density', 'selfishness', 'direct')

def logic_6307(agents, world):
    _agent_apply(world, agents, 'wetland', 'selfishness', 'direct')

def logic_6308(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'selfishness', 'direct')

def logic_6309(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'selfishness', 'direct')

def logic_6310(agents, world):
    _agent_apply(world, agents, 'ash', 'selfishness', 'direct')

def logic_6311(agents, world):
    _agent_apply(world, agents, 'snowpack', 'selfishness', 'direct')

def logic_6312(agents, world):
    _agent_apply(world, agents, 'groundwater', 'selfishness', 'direct')

def logic_6313(agents, world):
    _agent_apply(world, agents, 'sediment', 'selfishness', 'direct')

def logic_6314(agents, world):
    _agent_apply(world, agents, 'salinity', 'selfishness', 'direct')

def logic_6315(agents, world):
    _agent_apply(world, agents, 'algae', 'selfishness', 'direct')

def logic_6316(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'selfishness', 'direct')

def logic_6317(agents, world):
    _agent_apply(world, agents, 'deadwood', 'selfishness', 'direct')

def logic_6318(agents, world):
    _agent_apply(world, agents, 'pollinators', 'selfishness', 'direct')

def logic_6319(agents, world):
    _agent_apply(world, agents, 'flowers', 'selfishness', 'direct')

def logic_6320(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'selfishness', 'direct')

def logic_6321(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'selfishness', 'direct')

def logic_6322(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'selfishness', 'direct')

def logic_6323(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'selfishness', 'direct')

def logic_6324(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'selfishness', 'direct')

def logic_6325(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'selfishness', 'direct')

def logic_6326(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'selfishness', 'direct')

def logic_6327(agents, world):
    _agent_apply(world, agents, 'hydration', 'selfishness', 'direct')

def logic_6328(agents, world):
    _agent_apply(world, agents, 'thirst', 'selfishness', 'direct')

def logic_6329(agents, world):
    _agent_apply(world, agents, 'hunger', 'selfishness', 'direct')

def logic_6330(agents, world):
    _agent_apply(world, agents, 'health', 'selfishness', 'direct')

def logic_6331(agents, world):
    _agent_apply(world, agents, 'stress', 'selfishness', 'direct')

def logic_6332(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'selfishness', 'direct')

def logic_6333(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'selfishness', 'direct')

def logic_6334(agents, world):
    _agent_apply(world, agents, 'social_need', 'selfishness', 'direct')

def logic_6335(agents, world):
    _agent_apply(world, agents, 'cooperation', 'selfishness', 'direct')

def logic_6336(agents, world):
    _agent_apply(world, agents, 'defection', 'selfishness', 'direct')

def logic_6337(agents, world):
    _agent_apply(world, agents, 'trust', 'selfishness', 'direct')

def logic_6338(agents, world):
    _agent_apply(world, agents, 'reputation', 'selfishness', 'direct')

def logic_6339(agents, world):
    _agent_apply(world, agents, 'help_received', 'selfishness', 'direct')

def logic_6340(agents, world):
    _agent_apply(world, agents, 'help_given', 'selfishness', 'direct')

def logic_6341(agents, world):
    _agent_apply(world, agents, 'local_density', 'selfishness', 'direct')

def logic_6342(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'selfishness', 'direct')

def logic_6343(agents, world):
    _agent_apply(world, agents, 'survival_score', 'selfishness', 'direct')

def logic_6344(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'selfishness', 'direct')

def logic_6345(agents, world):
    _agent_apply(world, agents, 'payoff', 'selfishness', 'direct')

def logic_6346(agents, world):
    _agent_apply(world, agents, 'temperature', 'generosity', 'direct')

def logic_6347(agents, world):
    _agent_apply(world, agents, 'surface_water', 'generosity', 'direct')

def logic_6348(agents, world):
    _agent_apply(world, agents, 'humidity', 'generosity', 'direct')

def logic_6349(agents, world):
    _agent_apply(world, agents, 'cloud', 'generosity', 'direct')

def logic_6350(agents, world):
    _agent_apply(world, agents, 'rain', 'generosity', 'direct')

def logic_6351(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'generosity', 'direct')

def logic_6352(agents, world):
    _agent_apply(world, agents, 'runoff', 'generosity', 'direct')

def logic_6353(agents, world):
    _agent_apply(world, agents, 'wind_x', 'generosity', 'direct')

def logic_6354(agents, world):
    _agent_apply(world, agents, 'wind_y', 'generosity', 'direct')

def logic_6355(agents, world):
    _agent_apply(world, agents, 'vegetation', 'generosity', 'direct')

def logic_6356(agents, world):
    _agent_apply(world, agents, 'biomass', 'generosity', 'direct')

def logic_6357(agents, world):
    _agent_apply(world, agents, 'herbivore', 'generosity', 'direct')

def logic_6358(agents, world):
    _agent_apply(world, agents, 'predator', 'generosity', 'direct')

def logic_6359(agents, world):
    _agent_apply(world, agents, 'carrion', 'generosity', 'direct')

def logic_6360(agents, world):
    _agent_apply(world, agents, 'nutrients', 'generosity', 'direct')

def logic_6361(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'generosity', 'direct')

def logic_6362(agents, world):
    _agent_apply(world, agents, 'oxygen', 'generosity', 'direct')

def logic_6363(agents, world):
    _agent_apply(world, agents, 'co2', 'generosity', 'direct')

def logic_6364(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'generosity', 'direct')

def logic_6365(agents, world):
    _agent_apply(world, agents, 'ice', 'generosity', 'direct')

def logic_6366(agents, world):
    _agent_apply(world, agents, 'evaporation', 'generosity', 'direct')

def logic_6367(agents, world):
    _agent_apply(world, agents, 'detritus', 'generosity', 'direct')

def logic_6368(agents, world):
    _agent_apply(world, agents, 'methane', 'generosity', 'direct')

def logic_6369(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'generosity', 'direct')

def logic_6370(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'generosity', 'direct')

def logic_6371(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'generosity', 'direct')

def logic_6372(agents, world):
    _agent_apply(world, agents, 'erosion', 'generosity', 'direct')

def logic_6373(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'generosity', 'direct')

def logic_6374(agents, world):
    _agent_apply(world, agents, 'root_density', 'generosity', 'direct')

def logic_6375(agents, world):
    _agent_apply(world, agents, 'wetland', 'generosity', 'direct')

def logic_6376(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'generosity', 'direct')

def logic_6377(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'generosity', 'direct')

def logic_6378(agents, world):
    _agent_apply(world, agents, 'ash', 'generosity', 'direct')

def logic_6379(agents, world):
    _agent_apply(world, agents, 'snowpack', 'generosity', 'direct')

def logic_6380(agents, world):
    _agent_apply(world, agents, 'groundwater', 'generosity', 'direct')

def logic_6381(agents, world):
    _agent_apply(world, agents, 'sediment', 'generosity', 'direct')

def logic_6382(agents, world):
    _agent_apply(world, agents, 'salinity', 'generosity', 'direct')

def logic_6383(agents, world):
    _agent_apply(world, agents, 'algae', 'generosity', 'direct')

def logic_6384(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'generosity', 'direct')

def logic_6385(agents, world):
    _agent_apply(world, agents, 'deadwood', 'generosity', 'direct')

def logic_6386(agents, world):
    _agent_apply(world, agents, 'pollinators', 'generosity', 'direct')

def logic_6387(agents, world):
    _agent_apply(world, agents, 'flowers', 'generosity', 'direct')

def logic_6388(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'generosity', 'direct')

def logic_6389(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'generosity', 'direct')

def logic_6390(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'generosity', 'direct')

def logic_6391(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'generosity', 'direct')

def logic_6392(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'generosity', 'direct')

def logic_6393(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'generosity', 'direct')

def logic_6394(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'generosity', 'direct')

def logic_6395(agents, world):
    _agent_apply(world, agents, 'hydration', 'generosity', 'direct')

def logic_6396(agents, world):
    _agent_apply(world, agents, 'thirst', 'generosity', 'direct')

def logic_6397(agents, world):
    _agent_apply(world, agents, 'hunger', 'generosity', 'direct')

def logic_6398(agents, world):
    _agent_apply(world, agents, 'health', 'generosity', 'direct')

def logic_6399(agents, world):
    _agent_apply(world, agents, 'stress', 'generosity', 'direct')

def logic_6400(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'generosity', 'direct')

def logic_6401(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'generosity', 'direct')

def logic_6402(agents, world):
    _agent_apply(world, agents, 'social_need', 'generosity', 'direct')

def logic_6403(agents, world):
    _agent_apply(world, agents, 'cooperation', 'generosity', 'direct')

def logic_6404(agents, world):
    _agent_apply(world, agents, 'defection', 'generosity', 'direct')

def logic_6405(agents, world):
    _agent_apply(world, agents, 'trust', 'generosity', 'direct')

def logic_6406(agents, world):
    _agent_apply(world, agents, 'reputation', 'generosity', 'direct')

def logic_6407(agents, world):
    _agent_apply(world, agents, 'help_received', 'generosity', 'direct')

def logic_6408(agents, world):
    _agent_apply(world, agents, 'help_given', 'generosity', 'direct')

def logic_6409(agents, world):
    _agent_apply(world, agents, 'local_density', 'generosity', 'direct')

def logic_6410(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'generosity', 'direct')

def logic_6411(agents, world):
    _agent_apply(world, agents, 'survival_score', 'generosity', 'direct')

def logic_6412(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'generosity', 'direct')

def logic_6413(agents, world):
    _agent_apply(world, agents, 'payoff', 'generosity', 'direct')

def logic_6414(agents, world):
    _agent_apply(world, agents, 'temperature', 'gratitude', 'direct')

def logic_6415(agents, world):
    _agent_apply(world, agents, 'surface_water', 'gratitude', 'direct')

def logic_6416(agents, world):
    _agent_apply(world, agents, 'humidity', 'gratitude', 'direct')

def logic_6417(agents, world):
    _agent_apply(world, agents, 'cloud', 'gratitude', 'direct')

def logic_6418(agents, world):
    _agent_apply(world, agents, 'rain', 'gratitude', 'direct')

def logic_6419(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'gratitude', 'direct')

def logic_6420(agents, world):
    _agent_apply(world, agents, 'runoff', 'gratitude', 'direct')

def logic_6421(agents, world):
    _agent_apply(world, agents, 'wind_x', 'gratitude', 'direct')

def logic_6422(agents, world):
    _agent_apply(world, agents, 'wind_y', 'gratitude', 'direct')

def logic_6423(agents, world):
    _agent_apply(world, agents, 'vegetation', 'gratitude', 'direct')

def logic_6424(agents, world):
    _agent_apply(world, agents, 'biomass', 'gratitude', 'direct')

def logic_6425(agents, world):
    _agent_apply(world, agents, 'herbivore', 'gratitude', 'direct')

def logic_6426(agents, world):
    _agent_apply(world, agents, 'predator', 'gratitude', 'direct')

def logic_6427(agents, world):
    _agent_apply(world, agents, 'carrion', 'gratitude', 'direct')

def logic_6428(agents, world):
    _agent_apply(world, agents, 'nutrients', 'gratitude', 'direct')

def logic_6429(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'gratitude', 'direct')

def logic_6430(agents, world):
    _agent_apply(world, agents, 'oxygen', 'gratitude', 'direct')

def logic_6431(agents, world):
    _agent_apply(world, agents, 'co2', 'gratitude', 'direct')

def logic_6432(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'gratitude', 'direct')

def logic_6433(agents, world):
    _agent_apply(world, agents, 'ice', 'gratitude', 'direct')

def logic_6434(agents, world):
    _agent_apply(world, agents, 'evaporation', 'gratitude', 'direct')

def logic_6435(agents, world):
    _agent_apply(world, agents, 'detritus', 'gratitude', 'direct')

def logic_6436(agents, world):
    _agent_apply(world, agents, 'methane', 'gratitude', 'direct')

def logic_6437(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'gratitude', 'direct')

def logic_6438(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'gratitude', 'direct')

def logic_6439(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'gratitude', 'direct')

def logic_6440(agents, world):
    _agent_apply(world, agents, 'erosion', 'gratitude', 'direct')

def logic_6441(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'gratitude', 'direct')

def logic_6442(agents, world):
    _agent_apply(world, agents, 'root_density', 'gratitude', 'direct')

def logic_6443(agents, world):
    _agent_apply(world, agents, 'wetland', 'gratitude', 'direct')

def logic_6444(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'gratitude', 'direct')

def logic_6445(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'gratitude', 'direct')

def logic_6446(agents, world):
    _agent_apply(world, agents, 'ash', 'gratitude', 'direct')

def logic_6447(agents, world):
    _agent_apply(world, agents, 'snowpack', 'gratitude', 'direct')

def logic_6448(agents, world):
    _agent_apply(world, agents, 'groundwater', 'gratitude', 'direct')

def logic_6449(agents, world):
    _agent_apply(world, agents, 'sediment', 'gratitude', 'direct')

def logic_6450(agents, world):
    _agent_apply(world, agents, 'salinity', 'gratitude', 'direct')

def logic_6451(agents, world):
    _agent_apply(world, agents, 'algae', 'gratitude', 'direct')

def logic_6452(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'gratitude', 'direct')

def logic_6453(agents, world):
    _agent_apply(world, agents, 'deadwood', 'gratitude', 'direct')

def logic_6454(agents, world):
    _agent_apply(world, agents, 'pollinators', 'gratitude', 'direct')

def logic_6455(agents, world):
    _agent_apply(world, agents, 'flowers', 'gratitude', 'direct')

def logic_6456(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'gratitude', 'direct')

def logic_6457(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'gratitude', 'direct')

def logic_6458(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'gratitude', 'direct')

def logic_6459(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'gratitude', 'direct')

def logic_6460(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'gratitude', 'direct')

def logic_6461(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'gratitude', 'direct')

def logic_6462(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'gratitude', 'direct')

def logic_6463(agents, world):
    _agent_apply(world, agents, 'hydration', 'gratitude', 'direct')

def logic_6464(agents, world):
    _agent_apply(world, agents, 'thirst', 'gratitude', 'direct')

def logic_6465(agents, world):
    _agent_apply(world, agents, 'hunger', 'gratitude', 'direct')

def logic_6466(agents, world):
    _agent_apply(world, agents, 'health', 'gratitude', 'direct')

def logic_6467(agents, world):
    _agent_apply(world, agents, 'stress', 'gratitude', 'direct')

def logic_6468(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'gratitude', 'direct')

def logic_6469(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'gratitude', 'direct')

def logic_6470(agents, world):
    _agent_apply(world, agents, 'social_need', 'gratitude', 'direct')

def logic_6471(agents, world):
    _agent_apply(world, agents, 'cooperation', 'gratitude', 'direct')

def logic_6472(agents, world):
    _agent_apply(world, agents, 'defection', 'gratitude', 'direct')

def logic_6473(agents, world):
    _agent_apply(world, agents, 'trust', 'gratitude', 'direct')

def logic_6474(agents, world):
    _agent_apply(world, agents, 'reputation', 'gratitude', 'direct')

def logic_6475(agents, world):
    _agent_apply(world, agents, 'help_received', 'gratitude', 'direct')

def logic_6476(agents, world):
    _agent_apply(world, agents, 'help_given', 'gratitude', 'direct')

def logic_6477(agents, world):
    _agent_apply(world, agents, 'local_density', 'gratitude', 'direct')

def logic_6478(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'gratitude', 'direct')

def logic_6479(agents, world):
    _agent_apply(world, agents, 'survival_score', 'gratitude', 'direct')

def logic_6480(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'gratitude', 'direct')

def logic_6481(agents, world):
    _agent_apply(world, agents, 'payoff', 'gratitude', 'direct')

def logic_6482(agents, world):
    _agent_apply(world, agents, 'temperature', 'caution', 'direct')

def logic_6483(agents, world):
    _agent_apply(world, agents, 'surface_water', 'caution', 'direct')

def logic_6484(agents, world):
    _agent_apply(world, agents, 'humidity', 'caution', 'direct')

def logic_6485(agents, world):
    _agent_apply(world, agents, 'cloud', 'caution', 'direct')

def logic_6486(agents, world):
    _agent_apply(world, agents, 'rain', 'caution', 'direct')

def logic_6487(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'caution', 'direct')

def logic_6488(agents, world):
    _agent_apply(world, agents, 'runoff', 'caution', 'direct')

def logic_6489(agents, world):
    _agent_apply(world, agents, 'wind_x', 'caution', 'direct')

def logic_6490(agents, world):
    _agent_apply(world, agents, 'wind_y', 'caution', 'direct')

def logic_6491(agents, world):
    _agent_apply(world, agents, 'vegetation', 'caution', 'direct')

def logic_6492(agents, world):
    _agent_apply(world, agents, 'biomass', 'caution', 'direct')

def logic_6493(agents, world):
    _agent_apply(world, agents, 'herbivore', 'caution', 'direct')

def logic_6494(agents, world):
    _agent_apply(world, agents, 'predator', 'caution', 'direct')

def logic_6495(agents, world):
    _agent_apply(world, agents, 'carrion', 'caution', 'direct')

def logic_6496(agents, world):
    _agent_apply(world, agents, 'nutrients', 'caution', 'direct')

def logic_6497(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'caution', 'direct')

def logic_6498(agents, world):
    _agent_apply(world, agents, 'oxygen', 'caution', 'direct')

def logic_6499(agents, world):
    _agent_apply(world, agents, 'co2', 'caution', 'direct')

def logic_6500(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'caution', 'direct')

def logic_6501(agents, world):
    _agent_apply(world, agents, 'ice', 'caution', 'direct')

def logic_6502(agents, world):
    _agent_apply(world, agents, 'evaporation', 'caution', 'direct')

def logic_6503(agents, world):
    _agent_apply(world, agents, 'detritus', 'caution', 'direct')

def logic_6504(agents, world):
    _agent_apply(world, agents, 'methane', 'caution', 'direct')

def logic_6505(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'caution', 'direct')

def logic_6506(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'caution', 'direct')

def logic_6507(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'caution', 'direct')

def logic_6508(agents, world):
    _agent_apply(world, agents, 'erosion', 'caution', 'direct')

def logic_6509(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'caution', 'direct')

def logic_6510(agents, world):
    _agent_apply(world, agents, 'root_density', 'caution', 'direct')

def logic_6511(agents, world):
    _agent_apply(world, agents, 'wetland', 'caution', 'direct')

def logic_6512(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'caution', 'direct')

def logic_6513(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'caution', 'direct')

def logic_6514(agents, world):
    _agent_apply(world, agents, 'ash', 'caution', 'direct')

def logic_6515(agents, world):
    _agent_apply(world, agents, 'snowpack', 'caution', 'direct')

def logic_6516(agents, world):
    _agent_apply(world, agents, 'groundwater', 'caution', 'direct')

def logic_6517(agents, world):
    _agent_apply(world, agents, 'sediment', 'caution', 'direct')

def logic_6518(agents, world):
    _agent_apply(world, agents, 'salinity', 'caution', 'direct')

def logic_6519(agents, world):
    _agent_apply(world, agents, 'algae', 'caution', 'direct')

def logic_6520(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'caution', 'direct')

def logic_6521(agents, world):
    _agent_apply(world, agents, 'deadwood', 'caution', 'direct')

def logic_6522(agents, world):
    _agent_apply(world, agents, 'pollinators', 'caution', 'direct')

def logic_6523(agents, world):
    _agent_apply(world, agents, 'flowers', 'caution', 'direct')

def logic_6524(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'caution', 'direct')

def logic_6525(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'caution', 'direct')

def logic_6526(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'caution', 'direct')

def logic_6527(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'caution', 'direct')

def logic_6528(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'caution', 'direct')

def logic_6529(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'caution', 'direct')

def logic_6530(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'caution', 'direct')

def logic_6531(agents, world):
    _agent_apply(world, agents, 'hydration', 'caution', 'direct')

def logic_6532(agents, world):
    _agent_apply(world, agents, 'thirst', 'caution', 'direct')

def logic_6533(agents, world):
    _agent_apply(world, agents, 'hunger', 'caution', 'direct')

def logic_6534(agents, world):
    _agent_apply(world, agents, 'health', 'caution', 'direct')

def logic_6535(agents, world):
    _agent_apply(world, agents, 'stress', 'caution', 'direct')

def logic_6536(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'caution', 'direct')

def logic_6537(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'caution', 'direct')

def logic_6538(agents, world):
    _agent_apply(world, agents, 'social_need', 'caution', 'direct')

def logic_6539(agents, world):
    _agent_apply(world, agents, 'cooperation', 'caution', 'direct')

def logic_6540(agents, world):
    _agent_apply(world, agents, 'defection', 'caution', 'direct')

def logic_6541(agents, world):
    _agent_apply(world, agents, 'trust', 'caution', 'direct')

def logic_6542(agents, world):
    _agent_apply(world, agents, 'reputation', 'caution', 'direct')

def logic_6543(agents, world):
    _agent_apply(world, agents, 'help_received', 'caution', 'direct')

def logic_6544(agents, world):
    _agent_apply(world, agents, 'help_given', 'caution', 'direct')

def logic_6545(agents, world):
    _agent_apply(world, agents, 'local_density', 'caution', 'direct')

def logic_6546(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'caution', 'direct')

def logic_6547(agents, world):
    _agent_apply(world, agents, 'survival_score', 'caution', 'direct')

def logic_6548(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'caution', 'direct')

def logic_6549(agents, world):
    _agent_apply(world, agents, 'payoff', 'caution', 'direct')

def logic_6550(agents, world):
    _agent_apply(world, agents, 'temperature', 'confidence', 'direct')

def logic_6551(agents, world):
    _agent_apply(world, agents, 'surface_water', 'confidence', 'direct')

def logic_6552(agents, world):
    _agent_apply(world, agents, 'humidity', 'confidence', 'direct')

def logic_6553(agents, world):
    _agent_apply(world, agents, 'cloud', 'confidence', 'direct')

def logic_6554(agents, world):
    _agent_apply(world, agents, 'rain', 'confidence', 'direct')

def logic_6555(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'confidence', 'direct')

def logic_6556(agents, world):
    _agent_apply(world, agents, 'runoff', 'confidence', 'direct')

def logic_6557(agents, world):
    _agent_apply(world, agents, 'wind_x', 'confidence', 'direct')

def logic_6558(agents, world):
    _agent_apply(world, agents, 'wind_y', 'confidence', 'direct')

def logic_6559(agents, world):
    _agent_apply(world, agents, 'vegetation', 'confidence', 'direct')

def logic_6560(agents, world):
    _agent_apply(world, agents, 'biomass', 'confidence', 'direct')

def logic_6561(agents, world):
    _agent_apply(world, agents, 'herbivore', 'confidence', 'direct')

def logic_6562(agents, world):
    _agent_apply(world, agents, 'predator', 'confidence', 'direct')

def logic_6563(agents, world):
    _agent_apply(world, agents, 'carrion', 'confidence', 'direct')

def logic_6564(agents, world):
    _agent_apply(world, agents, 'nutrients', 'confidence', 'direct')

def logic_6565(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'confidence', 'direct')

def logic_6566(agents, world):
    _agent_apply(world, agents, 'oxygen', 'confidence', 'direct')

def logic_6567(agents, world):
    _agent_apply(world, agents, 'co2', 'confidence', 'direct')

def logic_6568(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'confidence', 'direct')

def logic_6569(agents, world):
    _agent_apply(world, agents, 'ice', 'confidence', 'direct')

def logic_6570(agents, world):
    _agent_apply(world, agents, 'evaporation', 'confidence', 'direct')

def logic_6571(agents, world):
    _agent_apply(world, agents, 'detritus', 'confidence', 'direct')

def logic_6572(agents, world):
    _agent_apply(world, agents, 'methane', 'confidence', 'direct')

def logic_6573(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'confidence', 'direct')

def logic_6574(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'confidence', 'direct')

def logic_6575(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'confidence', 'direct')

def logic_6576(agents, world):
    _agent_apply(world, agents, 'erosion', 'confidence', 'direct')

def logic_6577(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'confidence', 'direct')

def logic_6578(agents, world):
    _agent_apply(world, agents, 'root_density', 'confidence', 'direct')

def logic_6579(agents, world):
    _agent_apply(world, agents, 'wetland', 'confidence', 'direct')

def logic_6580(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'confidence', 'direct')

def logic_6581(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'confidence', 'direct')

def logic_6582(agents, world):
    _agent_apply(world, agents, 'ash', 'confidence', 'direct')

def logic_6583(agents, world):
    _agent_apply(world, agents, 'snowpack', 'confidence', 'direct')

def logic_6584(agents, world):
    _agent_apply(world, agents, 'groundwater', 'confidence', 'direct')

def logic_6585(agents, world):
    _agent_apply(world, agents, 'sediment', 'confidence', 'direct')

def logic_6586(agents, world):
    _agent_apply(world, agents, 'salinity', 'confidence', 'direct')

def logic_6587(agents, world):
    _agent_apply(world, agents, 'algae', 'confidence', 'direct')

def logic_6588(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'confidence', 'direct')

def logic_6589(agents, world):
    _agent_apply(world, agents, 'deadwood', 'confidence', 'direct')

def logic_6590(agents, world):
    _agent_apply(world, agents, 'pollinators', 'confidence', 'direct')

def logic_6591(agents, world):
    _agent_apply(world, agents, 'flowers', 'confidence', 'direct')

def logic_6592(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'confidence', 'direct')

def logic_6593(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'confidence', 'direct')

def logic_6594(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'confidence', 'direct')

def logic_6595(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'confidence', 'direct')

def logic_6596(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'confidence', 'direct')

def logic_6597(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'confidence', 'direct')

def logic_6598(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'confidence', 'direct')

def logic_6599(agents, world):
    _agent_apply(world, agents, 'hydration', 'confidence', 'direct')

def logic_6600(agents, world):
    _agent_apply(world, agents, 'thirst', 'confidence', 'direct')

def logic_6601(agents, world):
    _agent_apply(world, agents, 'hunger', 'confidence', 'direct')

def logic_6602(agents, world):
    _agent_apply(world, agents, 'health', 'confidence', 'direct')

def logic_6603(agents, world):
    _agent_apply(world, agents, 'stress', 'confidence', 'direct')

def logic_6604(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'confidence', 'direct')

def logic_6605(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'confidence', 'direct')

def logic_6606(agents, world):
    _agent_apply(world, agents, 'social_need', 'confidence', 'direct')

def logic_6607(agents, world):
    _agent_apply(world, agents, 'cooperation', 'confidence', 'direct')

def logic_6608(agents, world):
    _agent_apply(world, agents, 'defection', 'confidence', 'direct')

def logic_6609(agents, world):
    _agent_apply(world, agents, 'trust', 'confidence', 'direct')

def logic_6610(agents, world):
    _agent_apply(world, agents, 'reputation', 'confidence', 'direct')

def logic_6611(agents, world):
    _agent_apply(world, agents, 'help_received', 'confidence', 'direct')

def logic_6612(agents, world):
    _agent_apply(world, agents, 'help_given', 'confidence', 'direct')

def logic_6613(agents, world):
    _agent_apply(world, agents, 'local_density', 'confidence', 'direct')

def logic_6614(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'confidence', 'direct')

def logic_6615(agents, world):
    _agent_apply(world, agents, 'survival_score', 'confidence', 'direct')

def logic_6616(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'confidence', 'direct')

def logic_6617(agents, world):
    _agent_apply(world, agents, 'payoff', 'confidence', 'direct')

def logic_6618(agents, world):
    _agent_apply(world, agents, 'temperature', 'strategy_confidence', 'direct')

def logic_6619(agents, world):
    _agent_apply(world, agents, 'surface_water', 'strategy_confidence', 'direct')

def logic_6620(agents, world):
    _agent_apply(world, agents, 'humidity', 'strategy_confidence', 'direct')

def logic_6621(agents, world):
    _agent_apply(world, agents, 'cloud', 'strategy_confidence', 'direct')

def logic_6622(agents, world):
    _agent_apply(world, agents, 'rain', 'strategy_confidence', 'direct')

def logic_6623(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'strategy_confidence', 'direct')

def logic_6624(agents, world):
    _agent_apply(world, agents, 'runoff', 'strategy_confidence', 'direct')

def logic_6625(agents, world):
    _agent_apply(world, agents, 'wind_x', 'strategy_confidence', 'direct')

def logic_6626(agents, world):
    _agent_apply(world, agents, 'wind_y', 'strategy_confidence', 'direct')

def logic_6627(agents, world):
    _agent_apply(world, agents, 'vegetation', 'strategy_confidence', 'direct')

def logic_6628(agents, world):
    _agent_apply(world, agents, 'biomass', 'strategy_confidence', 'direct')

def logic_6629(agents, world):
    _agent_apply(world, agents, 'herbivore', 'strategy_confidence', 'direct')

def logic_6630(agents, world):
    _agent_apply(world, agents, 'predator', 'strategy_confidence', 'direct')

def logic_6631(agents, world):
    _agent_apply(world, agents, 'carrion', 'strategy_confidence', 'direct')

def logic_6632(agents, world):
    _agent_apply(world, agents, 'nutrients', 'strategy_confidence', 'direct')

def logic_6633(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'strategy_confidence', 'direct')

def logic_6634(agents, world):
    _agent_apply(world, agents, 'oxygen', 'strategy_confidence', 'direct')

def logic_6635(agents, world):
    _agent_apply(world, agents, 'co2', 'strategy_confidence', 'direct')

def logic_6636(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'strategy_confidence', 'direct')

def logic_6637(agents, world):
    _agent_apply(world, agents, 'ice', 'strategy_confidence', 'direct')

def logic_6638(agents, world):
    _agent_apply(world, agents, 'evaporation', 'strategy_confidence', 'direct')

def logic_6639(agents, world):
    _agent_apply(world, agents, 'detritus', 'strategy_confidence', 'direct')

def logic_6640(agents, world):
    _agent_apply(world, agents, 'methane', 'strategy_confidence', 'direct')

def logic_6641(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'strategy_confidence', 'direct')

def logic_6642(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'strategy_confidence', 'direct')

def logic_6643(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'strategy_confidence', 'direct')

def logic_6644(agents, world):
    _agent_apply(world, agents, 'erosion', 'strategy_confidence', 'direct')

def logic_6645(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'strategy_confidence', 'direct')

def logic_6646(agents, world):
    _agent_apply(world, agents, 'root_density', 'strategy_confidence', 'direct')

def logic_6647(agents, world):
    _agent_apply(world, agents, 'wetland', 'strategy_confidence', 'direct')

def logic_6648(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'strategy_confidence', 'direct')

def logic_6649(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'strategy_confidence', 'direct')

def logic_6650(agents, world):
    _agent_apply(world, agents, 'ash', 'strategy_confidence', 'direct')

def logic_6651(agents, world):
    _agent_apply(world, agents, 'snowpack', 'strategy_confidence', 'direct')

def logic_6652(agents, world):
    _agent_apply(world, agents, 'groundwater', 'strategy_confidence', 'direct')

def logic_6653(agents, world):
    _agent_apply(world, agents, 'sediment', 'strategy_confidence', 'direct')

def logic_6654(agents, world):
    _agent_apply(world, agents, 'salinity', 'strategy_confidence', 'direct')

def logic_6655(agents, world):
    _agent_apply(world, agents, 'algae', 'strategy_confidence', 'direct')

def logic_6656(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'strategy_confidence', 'direct')

def logic_6657(agents, world):
    _agent_apply(world, agents, 'deadwood', 'strategy_confidence', 'direct')

def logic_6658(agents, world):
    _agent_apply(world, agents, 'pollinators', 'strategy_confidence', 'direct')

def logic_6659(agents, world):
    _agent_apply(world, agents, 'flowers', 'strategy_confidence', 'direct')

def logic_6660(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'strategy_confidence', 'direct')

def logic_6661(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'strategy_confidence', 'direct')

def logic_6662(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'strategy_confidence', 'direct')

def logic_6663(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'strategy_confidence', 'direct')

def logic_6664(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'strategy_confidence', 'direct')

def logic_6665(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'strategy_confidence', 'direct')

def logic_6666(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'strategy_confidence', 'direct')

def logic_6667(agents, world):
    _agent_apply(world, agents, 'hydration', 'strategy_confidence', 'direct')

def logic_6668(agents, world):
    _agent_apply(world, agents, 'thirst', 'strategy_confidence', 'direct')

def logic_6669(agents, world):
    _agent_apply(world, agents, 'hunger', 'strategy_confidence', 'direct')

def logic_6670(agents, world):
    _agent_apply(world, agents, 'health', 'strategy_confidence', 'direct')

def logic_6671(agents, world):
    _agent_apply(world, agents, 'stress', 'strategy_confidence', 'direct')

def logic_6672(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'strategy_confidence', 'direct')

def logic_6673(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'strategy_confidence', 'direct')

def logic_6674(agents, world):
    _agent_apply(world, agents, 'social_need', 'strategy_confidence', 'direct')

def logic_6675(agents, world):
    _agent_apply(world, agents, 'cooperation', 'strategy_confidence', 'direct')

def logic_6676(agents, world):
    _agent_apply(world, agents, 'defection', 'strategy_confidence', 'direct')

def logic_6677(agents, world):
    _agent_apply(world, agents, 'trust', 'strategy_confidence', 'direct')

def logic_6678(agents, world):
    _agent_apply(world, agents, 'reputation', 'strategy_confidence', 'direct')

def logic_6679(agents, world):
    _agent_apply(world, agents, 'help_received', 'strategy_confidence', 'direct')

def logic_6680(agents, world):
    _agent_apply(world, agents, 'help_given', 'strategy_confidence', 'direct')

def logic_6681(agents, world):
    _agent_apply(world, agents, 'local_density', 'strategy_confidence', 'direct')

def logic_6682(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'strategy_confidence', 'direct')

def logic_6683(agents, world):
    _agent_apply(world, agents, 'survival_score', 'strategy_confidence', 'direct')

def logic_6684(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'strategy_confidence', 'direct')

def logic_6685(agents, world):
    _agent_apply(world, agents, 'payoff', 'strategy_confidence', 'direct')

def logic_6686(agents, world):
    _agent_apply(world, agents, 'temperature', 'future_help', 'direct')

def logic_6687(agents, world):
    _agent_apply(world, agents, 'surface_water', 'future_help', 'direct')

def logic_6688(agents, world):
    _agent_apply(world, agents, 'humidity', 'future_help', 'direct')

def logic_6689(agents, world):
    _agent_apply(world, agents, 'cloud', 'future_help', 'direct')

def logic_6690(agents, world):
    _agent_apply(world, agents, 'rain', 'future_help', 'direct')

def logic_6691(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'future_help', 'direct')

def logic_6692(agents, world):
    _agent_apply(world, agents, 'runoff', 'future_help', 'direct')

def logic_6693(agents, world):
    _agent_apply(world, agents, 'wind_x', 'future_help', 'direct')

def logic_6694(agents, world):
    _agent_apply(world, agents, 'wind_y', 'future_help', 'direct')

def logic_6695(agents, world):
    _agent_apply(world, agents, 'vegetation', 'future_help', 'direct')

def logic_6696(agents, world):
    _agent_apply(world, agents, 'biomass', 'future_help', 'direct')

def logic_6697(agents, world):
    _agent_apply(world, agents, 'herbivore', 'future_help', 'direct')

def logic_6698(agents, world):
    _agent_apply(world, agents, 'predator', 'future_help', 'direct')

def logic_6699(agents, world):
    _agent_apply(world, agents, 'carrion', 'future_help', 'direct')

def logic_6700(agents, world):
    _agent_apply(world, agents, 'nutrients', 'future_help', 'direct')

def logic_6701(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'future_help', 'direct')

def logic_6702(agents, world):
    _agent_apply(world, agents, 'oxygen', 'future_help', 'direct')

def logic_6703(agents, world):
    _agent_apply(world, agents, 'co2', 'future_help', 'direct')

def logic_6704(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'future_help', 'direct')

def logic_6705(agents, world):
    _agent_apply(world, agents, 'ice', 'future_help', 'direct')

def logic_6706(agents, world):
    _agent_apply(world, agents, 'evaporation', 'future_help', 'direct')

def logic_6707(agents, world):
    _agent_apply(world, agents, 'detritus', 'future_help', 'direct')

def logic_6708(agents, world):
    _agent_apply(world, agents, 'methane', 'future_help', 'direct')

def logic_6709(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'future_help', 'direct')

def logic_6710(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'future_help', 'direct')

def logic_6711(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'future_help', 'direct')

def logic_6712(agents, world):
    _agent_apply(world, agents, 'erosion', 'future_help', 'direct')

def logic_6713(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'future_help', 'direct')

def logic_6714(agents, world):
    _agent_apply(world, agents, 'root_density', 'future_help', 'direct')

def logic_6715(agents, world):
    _agent_apply(world, agents, 'wetland', 'future_help', 'direct')

def logic_6716(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'future_help', 'direct')

def logic_6717(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'future_help', 'direct')

def logic_6718(agents, world):
    _agent_apply(world, agents, 'ash', 'future_help', 'direct')

def logic_6719(agents, world):
    _agent_apply(world, agents, 'snowpack', 'future_help', 'direct')

def logic_6720(agents, world):
    _agent_apply(world, agents, 'groundwater', 'future_help', 'direct')

def logic_6721(agents, world):
    _agent_apply(world, agents, 'sediment', 'future_help', 'direct')

def logic_6722(agents, world):
    _agent_apply(world, agents, 'salinity', 'future_help', 'direct')

def logic_6723(agents, world):
    _agent_apply(world, agents, 'algae', 'future_help', 'direct')

def logic_6724(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'future_help', 'direct')

def logic_6725(agents, world):
    _agent_apply(world, agents, 'deadwood', 'future_help', 'direct')

def logic_6726(agents, world):
    _agent_apply(world, agents, 'pollinators', 'future_help', 'direct')

def logic_6727(agents, world):
    _agent_apply(world, agents, 'flowers', 'future_help', 'direct')

def logic_6728(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'future_help', 'direct')

def logic_6729(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'future_help', 'direct')

def logic_6730(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'future_help', 'direct')

def logic_6731(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'future_help', 'direct')

def logic_6732(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'future_help', 'direct')

def logic_6733(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'future_help', 'direct')

def logic_6734(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'future_help', 'direct')

def logic_6735(agents, world):
    _agent_apply(world, agents, 'hydration', 'future_help', 'direct')

def logic_6736(agents, world):
    _agent_apply(world, agents, 'thirst', 'future_help', 'direct')

def logic_6737(agents, world):
    _agent_apply(world, agents, 'hunger', 'future_help', 'direct')

def logic_6738(agents, world):
    _agent_apply(world, agents, 'health', 'future_help', 'direct')

def logic_6739(agents, world):
    _agent_apply(world, agents, 'stress', 'future_help', 'direct')

def logic_6740(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'future_help', 'direct')

def logic_6741(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'future_help', 'direct')

def logic_6742(agents, world):
    _agent_apply(world, agents, 'social_need', 'future_help', 'direct')

def logic_6743(agents, world):
    _agent_apply(world, agents, 'cooperation', 'future_help', 'direct')

def logic_6744(agents, world):
    _agent_apply(world, agents, 'defection', 'future_help', 'direct')

def logic_6745(agents, world):
    _agent_apply(world, agents, 'trust', 'future_help', 'direct')

def logic_6746(agents, world):
    _agent_apply(world, agents, 'reputation', 'future_help', 'direct')

def logic_6747(agents, world):
    _agent_apply(world, agents, 'help_received', 'future_help', 'direct')

def logic_6748(agents, world):
    _agent_apply(world, agents, 'help_given', 'future_help', 'direct')

def logic_6749(agents, world):
    _agent_apply(world, agents, 'local_density', 'future_help', 'direct')

def logic_6750(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'future_help', 'direct')

def logic_6751(agents, world):
    _agent_apply(world, agents, 'survival_score', 'future_help', 'direct')

def logic_6752(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'future_help', 'direct')

def logic_6753(agents, world):
    _agent_apply(world, agents, 'payoff', 'future_help', 'direct')

def logic_6754(agents, world):
    _agent_apply(world, agents, 'temperature', 'resource_discovery', 'direct')

def logic_6755(agents, world):
    _agent_apply(world, agents, 'surface_water', 'resource_discovery', 'direct')

def logic_6756(agents, world):
    _agent_apply(world, agents, 'humidity', 'resource_discovery', 'direct')

def logic_6757(agents, world):
    _agent_apply(world, agents, 'cloud', 'resource_discovery', 'direct')

def logic_6758(agents, world):
    _agent_apply(world, agents, 'rain', 'resource_discovery', 'direct')

def logic_6759(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'resource_discovery', 'direct')

def logic_6760(agents, world):
    _agent_apply(world, agents, 'runoff', 'resource_discovery', 'direct')

def logic_6761(agents, world):
    _agent_apply(world, agents, 'wind_x', 'resource_discovery', 'direct')

def logic_6762(agents, world):
    _agent_apply(world, agents, 'wind_y', 'resource_discovery', 'direct')

def logic_6763(agents, world):
    _agent_apply(world, agents, 'vegetation', 'resource_discovery', 'direct')

def logic_6764(agents, world):
    _agent_apply(world, agents, 'biomass', 'resource_discovery', 'direct')

def logic_6765(agents, world):
    _agent_apply(world, agents, 'herbivore', 'resource_discovery', 'direct')

def logic_6766(agents, world):
    _agent_apply(world, agents, 'predator', 'resource_discovery', 'direct')

def logic_6767(agents, world):
    _agent_apply(world, agents, 'carrion', 'resource_discovery', 'direct')

def logic_6768(agents, world):
    _agent_apply(world, agents, 'nutrients', 'resource_discovery', 'direct')

def logic_6769(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'resource_discovery', 'direct')

def logic_6770(agents, world):
    _agent_apply(world, agents, 'oxygen', 'resource_discovery', 'direct')

def logic_6771(agents, world):
    _agent_apply(world, agents, 'co2', 'resource_discovery', 'direct')

def logic_6772(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'resource_discovery', 'direct')

def logic_6773(agents, world):
    _agent_apply(world, agents, 'ice', 'resource_discovery', 'direct')

def logic_6774(agents, world):
    _agent_apply(world, agents, 'evaporation', 'resource_discovery', 'direct')

def logic_6775(agents, world):
    _agent_apply(world, agents, 'detritus', 'resource_discovery', 'direct')

def logic_6776(agents, world):
    _agent_apply(world, agents, 'methane', 'resource_discovery', 'direct')

def logic_6777(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'resource_discovery', 'direct')

def logic_6778(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'resource_discovery', 'direct')

def logic_6779(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'resource_discovery', 'direct')

def logic_6780(agents, world):
    _agent_apply(world, agents, 'erosion', 'resource_discovery', 'direct')

def logic_6781(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'resource_discovery', 'direct')

def logic_6782(agents, world):
    _agent_apply(world, agents, 'root_density', 'resource_discovery', 'direct')

def logic_6783(agents, world):
    _agent_apply(world, agents, 'wetland', 'resource_discovery', 'direct')

def logic_6784(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'resource_discovery', 'direct')

def logic_6785(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'resource_discovery', 'direct')

def logic_6786(agents, world):
    _agent_apply(world, agents, 'ash', 'resource_discovery', 'direct')

def logic_6787(agents, world):
    _agent_apply(world, agents, 'snowpack', 'resource_discovery', 'direct')

def logic_6788(agents, world):
    _agent_apply(world, agents, 'groundwater', 'resource_discovery', 'direct')

def logic_6789(agents, world):
    _agent_apply(world, agents, 'sediment', 'resource_discovery', 'direct')

def logic_6790(agents, world):
    _agent_apply(world, agents, 'salinity', 'resource_discovery', 'direct')

def logic_6791(agents, world):
    _agent_apply(world, agents, 'algae', 'resource_discovery', 'direct')

def logic_6792(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'resource_discovery', 'direct')

def logic_6793(agents, world):
    _agent_apply(world, agents, 'deadwood', 'resource_discovery', 'direct')

def logic_6794(agents, world):
    _agent_apply(world, agents, 'pollinators', 'resource_discovery', 'direct')

def logic_6795(agents, world):
    _agent_apply(world, agents, 'flowers', 'resource_discovery', 'direct')

def logic_6796(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'resource_discovery', 'direct')

def logic_6797(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'resource_discovery', 'direct')

def logic_6798(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'resource_discovery', 'direct')

def logic_6799(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'resource_discovery', 'direct')

def logic_6800(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'resource_discovery', 'direct')

def logic_6801(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'resource_discovery', 'direct')

def logic_6802(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'resource_discovery', 'direct')

def logic_6803(agents, world):
    _agent_apply(world, agents, 'hydration', 'resource_discovery', 'direct')

def logic_6804(agents, world):
    _agent_apply(world, agents, 'thirst', 'resource_discovery', 'direct')

def logic_6805(agents, world):
    _agent_apply(world, agents, 'hunger', 'resource_discovery', 'direct')

def logic_6806(agents, world):
    _agent_apply(world, agents, 'health', 'resource_discovery', 'direct')

def logic_6807(agents, world):
    _agent_apply(world, agents, 'stress', 'resource_discovery', 'direct')

def logic_6808(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'resource_discovery', 'direct')

def logic_6809(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'resource_discovery', 'direct')

def logic_6810(agents, world):
    _agent_apply(world, agents, 'social_need', 'resource_discovery', 'direct')

def logic_6811(agents, world):
    _agent_apply(world, agents, 'cooperation', 'resource_discovery', 'direct')

def logic_6812(agents, world):
    _agent_apply(world, agents, 'defection', 'resource_discovery', 'direct')

def logic_6813(agents, world):
    _agent_apply(world, agents, 'trust', 'resource_discovery', 'direct')

def logic_6814(agents, world):
    _agent_apply(world, agents, 'reputation', 'resource_discovery', 'direct')

def logic_6815(agents, world):
    _agent_apply(world, agents, 'help_received', 'resource_discovery', 'direct')

def logic_6816(agents, world):
    _agent_apply(world, agents, 'help_given', 'resource_discovery', 'direct')

def logic_6817(agents, world):
    _agent_apply(world, agents, 'local_density', 'resource_discovery', 'direct')

def logic_6818(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'resource_discovery', 'direct')

def logic_6819(agents, world):
    _agent_apply(world, agents, 'survival_score', 'resource_discovery', 'direct')

def logic_6820(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'resource_discovery', 'direct')

def logic_6821(agents, world):
    _agent_apply(world, agents, 'payoff', 'resource_discovery', 'direct')

def logic_6822(agents, world):
    _agent_apply(world, agents, 'temperature', 'empathy', 'direct')

def logic_6823(agents, world):
    _agent_apply(world, agents, 'surface_water', 'empathy', 'direct')

def logic_6824(agents, world):
    _agent_apply(world, agents, 'humidity', 'empathy', 'direct')

def logic_6825(agents, world):
    _agent_apply(world, agents, 'cloud', 'empathy', 'direct')

def logic_6826(agents, world):
    _agent_apply(world, agents, 'rain', 'empathy', 'direct')

def logic_6827(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'empathy', 'direct')

def logic_6828(agents, world):
    _agent_apply(world, agents, 'runoff', 'empathy', 'direct')

def logic_6829(agents, world):
    _agent_apply(world, agents, 'wind_x', 'empathy', 'direct')

def logic_6830(agents, world):
    _agent_apply(world, agents, 'wind_y', 'empathy', 'direct')

def logic_6831(agents, world):
    _agent_apply(world, agents, 'vegetation', 'empathy', 'direct')

def logic_6832(agents, world):
    _agent_apply(world, agents, 'biomass', 'empathy', 'direct')

def logic_6833(agents, world):
    _agent_apply(world, agents, 'herbivore', 'empathy', 'direct')

def logic_6834(agents, world):
    _agent_apply(world, agents, 'predator', 'empathy', 'direct')

def logic_6835(agents, world):
    _agent_apply(world, agents, 'carrion', 'empathy', 'direct')

def logic_6836(agents, world):
    _agent_apply(world, agents, 'nutrients', 'empathy', 'direct')

def logic_6837(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'empathy', 'direct')

def logic_6838(agents, world):
    _agent_apply(world, agents, 'oxygen', 'empathy', 'direct')

def logic_6839(agents, world):
    _agent_apply(world, agents, 'co2', 'empathy', 'direct')

def logic_6840(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'empathy', 'direct')

def logic_6841(agents, world):
    _agent_apply(world, agents, 'ice', 'empathy', 'direct')

def logic_6842(agents, world):
    _agent_apply(world, agents, 'evaporation', 'empathy', 'direct')

def logic_6843(agents, world):
    _agent_apply(world, agents, 'detritus', 'empathy', 'direct')

def logic_6844(agents, world):
    _agent_apply(world, agents, 'methane', 'empathy', 'direct')

def logic_6845(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'empathy', 'direct')

def logic_6846(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'empathy', 'direct')

def logic_6847(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'empathy', 'direct')

def logic_6848(agents, world):
    _agent_apply(world, agents, 'erosion', 'empathy', 'direct')

def logic_6849(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'empathy', 'direct')

def logic_6850(agents, world):
    _agent_apply(world, agents, 'root_density', 'empathy', 'direct')

def logic_6851(agents, world):
    _agent_apply(world, agents, 'wetland', 'empathy', 'direct')

def logic_6852(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'empathy', 'direct')

def logic_6853(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'empathy', 'direct')

def logic_6854(agents, world):
    _agent_apply(world, agents, 'ash', 'empathy', 'direct')

def logic_6855(agents, world):
    _agent_apply(world, agents, 'snowpack', 'empathy', 'direct')

def logic_6856(agents, world):
    _agent_apply(world, agents, 'groundwater', 'empathy', 'direct')

def logic_6857(agents, world):
    _agent_apply(world, agents, 'sediment', 'empathy', 'direct')

def logic_6858(agents, world):
    _agent_apply(world, agents, 'salinity', 'empathy', 'direct')

def logic_6859(agents, world):
    _agent_apply(world, agents, 'algae', 'empathy', 'direct')

def logic_6860(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'empathy', 'direct')

def logic_6861(agents, world):
    _agent_apply(world, agents, 'deadwood', 'empathy', 'direct')

def logic_6862(agents, world):
    _agent_apply(world, agents, 'pollinators', 'empathy', 'direct')

def logic_6863(agents, world):
    _agent_apply(world, agents, 'flowers', 'empathy', 'direct')

def logic_6864(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'empathy', 'direct')

def logic_6865(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'empathy', 'direct')

def logic_6866(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'empathy', 'direct')

def logic_6867(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'empathy', 'direct')

def logic_6868(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'empathy', 'direct')

def logic_6869(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'empathy', 'direct')

def logic_6870(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'empathy', 'direct')

def logic_6871(agents, world):
    _agent_apply(world, agents, 'hydration', 'empathy', 'direct')

def logic_6872(agents, world):
    _agent_apply(world, agents, 'thirst', 'empathy', 'direct')

def logic_6873(agents, world):
    _agent_apply(world, agents, 'hunger', 'empathy', 'direct')

def logic_6874(agents, world):
    _agent_apply(world, agents, 'health', 'empathy', 'direct')

def logic_6875(agents, world):
    _agent_apply(world, agents, 'stress', 'empathy', 'direct')

def logic_6876(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'empathy', 'direct')

def logic_6877(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'empathy', 'direct')

def logic_6878(agents, world):
    _agent_apply(world, agents, 'social_need', 'empathy', 'direct')

def logic_6879(agents, world):
    _agent_apply(world, agents, 'cooperation', 'empathy', 'direct')

def logic_6880(agents, world):
    _agent_apply(world, agents, 'defection', 'empathy', 'direct')

def logic_6881(agents, world):
    _agent_apply(world, agents, 'trust', 'empathy', 'direct')

def logic_6882(agents, world):
    _agent_apply(world, agents, 'reputation', 'empathy', 'direct')

def logic_6883(agents, world):
    _agent_apply(world, agents, 'help_received', 'empathy', 'direct')

def logic_6884(agents, world):
    _agent_apply(world, agents, 'help_given', 'empathy', 'direct')

def logic_6885(agents, world):
    _agent_apply(world, agents, 'local_density', 'empathy', 'direct')

def logic_6886(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'empathy', 'direct')

def logic_6887(agents, world):
    _agent_apply(world, agents, 'survival_score', 'empathy', 'direct')

def logic_6888(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'empathy', 'direct')

def logic_6889(agents, world):
    _agent_apply(world, agents, 'payoff', 'empathy', 'direct')

def logic_6890(agents, world):
    _agent_apply(world, agents, 'temperature', 'attack_threshold', 'direct')

def logic_6891(agents, world):
    _agent_apply(world, agents, 'surface_water', 'attack_threshold', 'direct')

def logic_6892(agents, world):
    _agent_apply(world, agents, 'humidity', 'attack_threshold', 'direct')

def logic_6893(agents, world):
    _agent_apply(world, agents, 'cloud', 'attack_threshold', 'direct')

def logic_6894(agents, world):
    _agent_apply(world, agents, 'rain', 'attack_threshold', 'direct')

def logic_6895(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'attack_threshold', 'direct')

def logic_6896(agents, world):
    _agent_apply(world, agents, 'runoff', 'attack_threshold', 'direct')

def logic_6897(agents, world):
    _agent_apply(world, agents, 'wind_x', 'attack_threshold', 'direct')

def logic_6898(agents, world):
    _agent_apply(world, agents, 'wind_y', 'attack_threshold', 'direct')

def logic_6899(agents, world):
    _agent_apply(world, agents, 'vegetation', 'attack_threshold', 'direct')

def logic_6900(agents, world):
    _agent_apply(world, agents, 'biomass', 'attack_threshold', 'direct')

def logic_6901(agents, world):
    _agent_apply(world, agents, 'herbivore', 'attack_threshold', 'direct')

def logic_6902(agents, world):
    _agent_apply(world, agents, 'predator', 'attack_threshold', 'direct')

def logic_6903(agents, world):
    _agent_apply(world, agents, 'carrion', 'attack_threshold', 'direct')

def logic_6904(agents, world):
    _agent_apply(world, agents, 'nutrients', 'attack_threshold', 'direct')

def logic_6905(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'attack_threshold', 'direct')

def logic_6906(agents, world):
    _agent_apply(world, agents, 'oxygen', 'attack_threshold', 'direct')

def logic_6907(agents, world):
    _agent_apply(world, agents, 'co2', 'attack_threshold', 'direct')

def logic_6908(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'attack_threshold', 'direct')

def logic_6909(agents, world):
    _agent_apply(world, agents, 'ice', 'attack_threshold', 'direct')

def logic_6910(agents, world):
    _agent_apply(world, agents, 'evaporation', 'attack_threshold', 'direct')

def logic_6911(agents, world):
    _agent_apply(world, agents, 'detritus', 'attack_threshold', 'direct')

def logic_6912(agents, world):
    _agent_apply(world, agents, 'methane', 'attack_threshold', 'direct')

def logic_6913(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'attack_threshold', 'direct')

def logic_6914(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'attack_threshold', 'direct')

def logic_6915(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'attack_threshold', 'direct')

def logic_6916(agents, world):
    _agent_apply(world, agents, 'erosion', 'attack_threshold', 'direct')

def logic_6917(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'attack_threshold', 'direct')

def logic_6918(agents, world):
    _agent_apply(world, agents, 'root_density', 'attack_threshold', 'direct')

def logic_6919(agents, world):
    _agent_apply(world, agents, 'wetland', 'attack_threshold', 'direct')

def logic_6920(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'attack_threshold', 'direct')

def logic_6921(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'attack_threshold', 'direct')

def logic_6922(agents, world):
    _agent_apply(world, agents, 'ash', 'attack_threshold', 'direct')

def logic_6923(agents, world):
    _agent_apply(world, agents, 'snowpack', 'attack_threshold', 'direct')

def logic_6924(agents, world):
    _agent_apply(world, agents, 'groundwater', 'attack_threshold', 'direct')

def logic_6925(agents, world):
    _agent_apply(world, agents, 'sediment', 'attack_threshold', 'direct')

def logic_6926(agents, world):
    _agent_apply(world, agents, 'salinity', 'attack_threshold', 'direct')

def logic_6927(agents, world):
    _agent_apply(world, agents, 'algae', 'attack_threshold', 'direct')

def logic_6928(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'attack_threshold', 'direct')

def logic_6929(agents, world):
    _agent_apply(world, agents, 'deadwood', 'attack_threshold', 'direct')

def logic_6930(agents, world):
    _agent_apply(world, agents, 'pollinators', 'attack_threshold', 'direct')

def logic_6931(agents, world):
    _agent_apply(world, agents, 'flowers', 'attack_threshold', 'direct')

def logic_6932(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'attack_threshold', 'direct')

def logic_6933(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'attack_threshold', 'direct')

def logic_6934(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'attack_threshold', 'direct')

def logic_6935(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'attack_threshold', 'direct')

def logic_6936(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'attack_threshold', 'direct')

def logic_6937(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'attack_threshold', 'direct')

def logic_6938(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'attack_threshold', 'direct')

def logic_6939(agents, world):
    _agent_apply(world, agents, 'hydration', 'attack_threshold', 'direct')

def logic_6940(agents, world):
    _agent_apply(world, agents, 'thirst', 'attack_threshold', 'direct')

def logic_6941(agents, world):
    _agent_apply(world, agents, 'hunger', 'attack_threshold', 'direct')

def logic_6942(agents, world):
    _agent_apply(world, agents, 'health', 'attack_threshold', 'direct')

def logic_6943(agents, world):
    _agent_apply(world, agents, 'stress', 'attack_threshold', 'direct')

def logic_6944(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'attack_threshold', 'direct')

def logic_6945(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'attack_threshold', 'direct')

def logic_6946(agents, world):
    _agent_apply(world, agents, 'social_need', 'attack_threshold', 'direct')

def logic_6947(agents, world):
    _agent_apply(world, agents, 'cooperation', 'attack_threshold', 'direct')

def logic_6948(agents, world):
    _agent_apply(world, agents, 'defection', 'attack_threshold', 'direct')

def logic_6949(agents, world):
    _agent_apply(world, agents, 'trust', 'attack_threshold', 'direct')

def logic_6950(agents, world):
    _agent_apply(world, agents, 'reputation', 'attack_threshold', 'direct')

def logic_6951(agents, world):
    _agent_apply(world, agents, 'help_received', 'attack_threshold', 'direct')

def logic_6952(agents, world):
    _agent_apply(world, agents, 'help_given', 'attack_threshold', 'direct')

def logic_6953(agents, world):
    _agent_apply(world, agents, 'local_density', 'attack_threshold', 'direct')

def logic_6954(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'attack_threshold', 'direct')

def logic_6955(agents, world):
    _agent_apply(world, agents, 'survival_score', 'attack_threshold', 'direct')

def logic_6956(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'attack_threshold', 'direct')

def logic_6957(agents, world):
    _agent_apply(world, agents, 'payoff', 'attack_threshold', 'direct')

def logic_6958(agents, world):
    _agent_apply(world, agents, 'temperature', 'defection_threshold', 'direct')

def logic_6959(agents, world):
    _agent_apply(world, agents, 'surface_water', 'defection_threshold', 'direct')

def logic_6960(agents, world):
    _agent_apply(world, agents, 'humidity', 'defection_threshold', 'direct')

def logic_6961(agents, world):
    _agent_apply(world, agents, 'cloud', 'defection_threshold', 'direct')

def logic_6962(agents, world):
    _agent_apply(world, agents, 'rain', 'defection_threshold', 'direct')

def logic_6963(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'defection_threshold', 'direct')

def logic_6964(agents, world):
    _agent_apply(world, agents, 'runoff', 'defection_threshold', 'direct')

def logic_6965(agents, world):
    _agent_apply(world, agents, 'wind_x', 'defection_threshold', 'direct')

def logic_6966(agents, world):
    _agent_apply(world, agents, 'wind_y', 'defection_threshold', 'direct')

def logic_6967(agents, world):
    _agent_apply(world, agents, 'vegetation', 'defection_threshold', 'direct')

def logic_6968(agents, world):
    _agent_apply(world, agents, 'biomass', 'defection_threshold', 'direct')

def logic_6969(agents, world):
    _agent_apply(world, agents, 'herbivore', 'defection_threshold', 'direct')

def logic_6970(agents, world):
    _agent_apply(world, agents, 'predator', 'defection_threshold', 'direct')

def logic_6971(agents, world):
    _agent_apply(world, agents, 'carrion', 'defection_threshold', 'direct')

def logic_6972(agents, world):
    _agent_apply(world, agents, 'nutrients', 'defection_threshold', 'direct')

def logic_6973(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'defection_threshold', 'direct')

def logic_6974(agents, world):
    _agent_apply(world, agents, 'oxygen', 'defection_threshold', 'direct')

def logic_6975(agents, world):
    _agent_apply(world, agents, 'co2', 'defection_threshold', 'direct')

def logic_6976(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'defection_threshold', 'direct')

def logic_6977(agents, world):
    _agent_apply(world, agents, 'ice', 'defection_threshold', 'direct')

def logic_6978(agents, world):
    _agent_apply(world, agents, 'evaporation', 'defection_threshold', 'direct')

def logic_6979(agents, world):
    _agent_apply(world, agents, 'detritus', 'defection_threshold', 'direct')

def logic_6980(agents, world):
    _agent_apply(world, agents, 'methane', 'defection_threshold', 'direct')

def logic_6981(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'defection_threshold', 'direct')

def logic_6982(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'defection_threshold', 'direct')

def logic_6983(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'defection_threshold', 'direct')

def logic_6984(agents, world):
    _agent_apply(world, agents, 'erosion', 'defection_threshold', 'direct')

def logic_6985(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'defection_threshold', 'direct')

def logic_6986(agents, world):
    _agent_apply(world, agents, 'root_density', 'defection_threshold', 'direct')

def logic_6987(agents, world):
    _agent_apply(world, agents, 'wetland', 'defection_threshold', 'direct')

def logic_6988(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'defection_threshold', 'direct')

def logic_6989(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'defection_threshold', 'direct')

def logic_6990(agents, world):
    _agent_apply(world, agents, 'ash', 'defection_threshold', 'direct')

def logic_6991(agents, world):
    _agent_apply(world, agents, 'snowpack', 'defection_threshold', 'direct')

def logic_6992(agents, world):
    _agent_apply(world, agents, 'groundwater', 'defection_threshold', 'direct')

def logic_6993(agents, world):
    _agent_apply(world, agents, 'sediment', 'defection_threshold', 'direct')

def logic_6994(agents, world):
    _agent_apply(world, agents, 'salinity', 'defection_threshold', 'direct')

def logic_6995(agents, world):
    _agent_apply(world, agents, 'algae', 'defection_threshold', 'direct')

def logic_6996(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'defection_threshold', 'direct')

def logic_6997(agents, world):
    _agent_apply(world, agents, 'deadwood', 'defection_threshold', 'direct')

def logic_6998(agents, world):
    _agent_apply(world, agents, 'pollinators', 'defection_threshold', 'direct')

def logic_6999(agents, world):
    _agent_apply(world, agents, 'flowers', 'defection_threshold', 'direct')

def logic_7000(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'defection_threshold', 'direct')

def logic_7001(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'defection_threshold', 'direct')

def logic_7002(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'defection_threshold', 'direct')

def logic_7003(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'defection_threshold', 'direct')

def logic_7004(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'defection_threshold', 'direct')

def logic_7005(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'defection_threshold', 'direct')

def logic_7006(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'defection_threshold', 'direct')

def logic_7007(agents, world):
    _agent_apply(world, agents, 'hydration', 'defection_threshold', 'direct')

def logic_7008(agents, world):
    _agent_apply(world, agents, 'thirst', 'defection_threshold', 'direct')

def logic_7009(agents, world):
    _agent_apply(world, agents, 'hunger', 'defection_threshold', 'direct')

def logic_7010(agents, world):
    _agent_apply(world, agents, 'health', 'defection_threshold', 'direct')

def logic_7011(agents, world):
    _agent_apply(world, agents, 'stress', 'defection_threshold', 'direct')

def logic_7012(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'defection_threshold', 'direct')

def logic_7013(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'defection_threshold', 'direct')

def logic_7014(agents, world):
    _agent_apply(world, agents, 'social_need', 'defection_threshold', 'direct')

def logic_7015(agents, world):
    _agent_apply(world, agents, 'cooperation', 'defection_threshold', 'direct')

def logic_7016(agents, world):
    _agent_apply(world, agents, 'defection', 'defection_threshold', 'direct')

def logic_7017(agents, world):
    _agent_apply(world, agents, 'trust', 'defection_threshold', 'direct')

def logic_7018(agents, world):
    _agent_apply(world, agents, 'reputation', 'defection_threshold', 'direct')

def logic_7019(agents, world):
    _agent_apply(world, agents, 'help_received', 'defection_threshold', 'direct')

def logic_7020(agents, world):
    _agent_apply(world, agents, 'help_given', 'defection_threshold', 'direct')

def logic_7021(agents, world):
    _agent_apply(world, agents, 'local_density', 'defection_threshold', 'direct')

def logic_7022(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'defection_threshold', 'direct')

def logic_7023(agents, world):
    _agent_apply(world, agents, 'survival_score', 'defection_threshold', 'direct')

def logic_7024(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'defection_threshold', 'direct')

def logic_7025(agents, world):
    _agent_apply(world, agents, 'payoff', 'defection_threshold', 'direct')

def logic_7026(agents, world):
    _agent_apply(world, agents, 'temperature', 'oxygen_need', 'direct')

def logic_7027(agents, world):
    _agent_apply(world, agents, 'surface_water', 'oxygen_need', 'direct')

def logic_7028(agents, world):
    _agent_apply(world, agents, 'humidity', 'oxygen_need', 'direct')

def logic_7029(agents, world):
    _agent_apply(world, agents, 'cloud', 'oxygen_need', 'direct')

def logic_7030(agents, world):
    _agent_apply(world, agents, 'rain', 'oxygen_need', 'direct')

def logic_7031(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'oxygen_need', 'direct')

def logic_7032(agents, world):
    _agent_apply(world, agents, 'runoff', 'oxygen_need', 'direct')

def logic_7033(agents, world):
    _agent_apply(world, agents, 'wind_x', 'oxygen_need', 'direct')

def logic_7034(agents, world):
    _agent_apply(world, agents, 'wind_y', 'oxygen_need', 'direct')

def logic_7035(agents, world):
    _agent_apply(world, agents, 'vegetation', 'oxygen_need', 'direct')

def logic_7036(agents, world):
    _agent_apply(world, agents, 'biomass', 'oxygen_need', 'direct')

def logic_7037(agents, world):
    _agent_apply(world, agents, 'herbivore', 'oxygen_need', 'direct')

def logic_7038(agents, world):
    _agent_apply(world, agents, 'predator', 'oxygen_need', 'direct')

def logic_7039(agents, world):
    _agent_apply(world, agents, 'carrion', 'oxygen_need', 'direct')

def logic_7040(agents, world):
    _agent_apply(world, agents, 'nutrients', 'oxygen_need', 'direct')

def logic_7041(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'oxygen_need', 'direct')

def logic_7042(agents, world):
    _agent_apply(world, agents, 'oxygen', 'oxygen_need', 'direct')

def logic_7043(agents, world):
    _agent_apply(world, agents, 'co2', 'oxygen_need', 'direct')

def logic_7044(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'oxygen_need', 'direct')

def logic_7045(agents, world):
    _agent_apply(world, agents, 'ice', 'oxygen_need', 'direct')

def logic_7046(agents, world):
    _agent_apply(world, agents, 'evaporation', 'oxygen_need', 'direct')

def logic_7047(agents, world):
    _agent_apply(world, agents, 'detritus', 'oxygen_need', 'direct')

def logic_7048(agents, world):
    _agent_apply(world, agents, 'methane', 'oxygen_need', 'direct')

def logic_7049(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'oxygen_need', 'direct')

def logic_7050(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'oxygen_need', 'direct')

def logic_7051(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'oxygen_need', 'direct')

def logic_7052(agents, world):
    _agent_apply(world, agents, 'erosion', 'oxygen_need', 'direct')

def logic_7053(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'oxygen_need', 'direct')

def logic_7054(agents, world):
    _agent_apply(world, agents, 'root_density', 'oxygen_need', 'direct')

def logic_7055(agents, world):
    _agent_apply(world, agents, 'wetland', 'oxygen_need', 'direct')

def logic_7056(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'oxygen_need', 'direct')

def logic_7057(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'oxygen_need', 'direct')

def logic_7058(agents, world):
    _agent_apply(world, agents, 'ash', 'oxygen_need', 'direct')

def logic_7059(agents, world):
    _agent_apply(world, agents, 'snowpack', 'oxygen_need', 'direct')

def logic_7060(agents, world):
    _agent_apply(world, agents, 'groundwater', 'oxygen_need', 'direct')

def logic_7061(agents, world):
    _agent_apply(world, agents, 'sediment', 'oxygen_need', 'direct')

def logic_7062(agents, world):
    _agent_apply(world, agents, 'salinity', 'oxygen_need', 'direct')

def logic_7063(agents, world):
    _agent_apply(world, agents, 'algae', 'oxygen_need', 'direct')

def logic_7064(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'oxygen_need', 'direct')

def logic_7065(agents, world):
    _agent_apply(world, agents, 'deadwood', 'oxygen_need', 'direct')

def logic_7066(agents, world):
    _agent_apply(world, agents, 'pollinators', 'oxygen_need', 'direct')

def logic_7067(agents, world):
    _agent_apply(world, agents, 'flowers', 'oxygen_need', 'direct')

def logic_7068(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'oxygen_need', 'direct')

def logic_7069(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'oxygen_need', 'direct')

def logic_7070(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'oxygen_need', 'direct')

def logic_7071(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'oxygen_need', 'direct')

def logic_7072(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'oxygen_need', 'direct')

def logic_7073(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'oxygen_need', 'direct')

def logic_7074(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'oxygen_need', 'direct')

def logic_7075(agents, world):
    _agent_apply(world, agents, 'hydration', 'oxygen_need', 'direct')

def logic_7076(agents, world):
    _agent_apply(world, agents, 'thirst', 'oxygen_need', 'direct')

def logic_7077(agents, world):
    _agent_apply(world, agents, 'hunger', 'oxygen_need', 'direct')

def logic_7078(agents, world):
    _agent_apply(world, agents, 'health', 'oxygen_need', 'direct')

def logic_7079(agents, world):
    _agent_apply(world, agents, 'stress', 'oxygen_need', 'direct')

def logic_7080(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'oxygen_need', 'direct')

def logic_7081(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'oxygen_need', 'direct')

def logic_7082(agents, world):
    _agent_apply(world, agents, 'social_need', 'oxygen_need', 'direct')

def logic_7083(agents, world):
    _agent_apply(world, agents, 'cooperation', 'oxygen_need', 'direct')

def logic_7084(agents, world):
    _agent_apply(world, agents, 'defection', 'oxygen_need', 'direct')

def logic_7085(agents, world):
    _agent_apply(world, agents, 'trust', 'oxygen_need', 'direct')

def logic_7086(agents, world):
    _agent_apply(world, agents, 'reputation', 'oxygen_need', 'direct')

def logic_7087(agents, world):
    _agent_apply(world, agents, 'help_received', 'oxygen_need', 'direct')

def logic_7088(agents, world):
    _agent_apply(world, agents, 'help_given', 'oxygen_need', 'direct')

def logic_7089(agents, world):
    _agent_apply(world, agents, 'local_density', 'oxygen_need', 'direct')

def logic_7090(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'oxygen_need', 'direct')

def logic_7091(agents, world):
    _agent_apply(world, agents, 'survival_score', 'oxygen_need', 'direct')

def logic_7092(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'oxygen_need', 'direct')

def logic_7093(agents, world):
    _agent_apply(world, agents, 'payoff', 'oxygen_need', 'direct')

def logic_7094(agents, world):
    _agent_apply(world, agents, 'temperature', 'shelter_need', 'direct')

def logic_7095(agents, world):
    _agent_apply(world, agents, 'surface_water', 'shelter_need', 'direct')

def logic_7096(agents, world):
    _agent_apply(world, agents, 'humidity', 'shelter_need', 'direct')

def logic_7097(agents, world):
    _agent_apply(world, agents, 'cloud', 'shelter_need', 'direct')

def logic_7098(agents, world):
    _agent_apply(world, agents, 'rain', 'shelter_need', 'direct')

def logic_7099(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'shelter_need', 'direct')

def logic_7100(agents, world):
    _agent_apply(world, agents, 'runoff', 'shelter_need', 'direct')

def logic_7101(agents, world):
    _agent_apply(world, agents, 'wind_x', 'shelter_need', 'direct')

def logic_7102(agents, world):
    _agent_apply(world, agents, 'wind_y', 'shelter_need', 'direct')

def logic_7103(agents, world):
    _agent_apply(world, agents, 'vegetation', 'shelter_need', 'direct')

def logic_7104(agents, world):
    _agent_apply(world, agents, 'biomass', 'shelter_need', 'direct')

def logic_7105(agents, world):
    _agent_apply(world, agents, 'herbivore', 'shelter_need', 'direct')

def logic_7106(agents, world):
    _agent_apply(world, agents, 'predator', 'shelter_need', 'direct')

def logic_7107(agents, world):
    _agent_apply(world, agents, 'carrion', 'shelter_need', 'direct')

def logic_7108(agents, world):
    _agent_apply(world, agents, 'nutrients', 'shelter_need', 'direct')

def logic_7109(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'shelter_need', 'direct')

def logic_7110(agents, world):
    _agent_apply(world, agents, 'oxygen', 'shelter_need', 'direct')

def logic_7111(agents, world):
    _agent_apply(world, agents, 'co2', 'shelter_need', 'direct')

def logic_7112(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'shelter_need', 'direct')

def logic_7113(agents, world):
    _agent_apply(world, agents, 'ice', 'shelter_need', 'direct')

def logic_7114(agents, world):
    _agent_apply(world, agents, 'evaporation', 'shelter_need', 'direct')

def logic_7115(agents, world):
    _agent_apply(world, agents, 'detritus', 'shelter_need', 'direct')

def logic_7116(agents, world):
    _agent_apply(world, agents, 'methane', 'shelter_need', 'direct')

def logic_7117(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'shelter_need', 'direct')

def logic_7118(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'shelter_need', 'direct')

def logic_7119(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'shelter_need', 'direct')

def logic_7120(agents, world):
    _agent_apply(world, agents, 'erosion', 'shelter_need', 'direct')

def logic_7121(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'shelter_need', 'direct')

def logic_7122(agents, world):
    _agent_apply(world, agents, 'root_density', 'shelter_need', 'direct')

def logic_7123(agents, world):
    _agent_apply(world, agents, 'wetland', 'shelter_need', 'direct')

def logic_7124(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'shelter_need', 'direct')

def logic_7125(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'shelter_need', 'direct')

def logic_7126(agents, world):
    _agent_apply(world, agents, 'ash', 'shelter_need', 'direct')

def logic_7127(agents, world):
    _agent_apply(world, agents, 'snowpack', 'shelter_need', 'direct')

def logic_7128(agents, world):
    _agent_apply(world, agents, 'groundwater', 'shelter_need', 'direct')

def logic_7129(agents, world):
    _agent_apply(world, agents, 'sediment', 'shelter_need', 'direct')

def logic_7130(agents, world):
    _agent_apply(world, agents, 'salinity', 'shelter_need', 'direct')

def logic_7131(agents, world):
    _agent_apply(world, agents, 'algae', 'shelter_need', 'direct')

def logic_7132(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'shelter_need', 'direct')

def logic_7133(agents, world):
    _agent_apply(world, agents, 'deadwood', 'shelter_need', 'direct')

def logic_7134(agents, world):
    _agent_apply(world, agents, 'pollinators', 'shelter_need', 'direct')

def logic_7135(agents, world):
    _agent_apply(world, agents, 'flowers', 'shelter_need', 'direct')

def logic_7136(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'shelter_need', 'direct')

def logic_7137(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'shelter_need', 'direct')

def logic_7138(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'shelter_need', 'direct')

def logic_7139(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'shelter_need', 'direct')

def logic_7140(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'shelter_need', 'direct')

def logic_7141(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'shelter_need', 'direct')

def logic_7142(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'shelter_need', 'direct')

def logic_7143(agents, world):
    _agent_apply(world, agents, 'hydration', 'shelter_need', 'direct')

def logic_7144(agents, world):
    _agent_apply(world, agents, 'thirst', 'shelter_need', 'direct')

def logic_7145(agents, world):
    _agent_apply(world, agents, 'hunger', 'shelter_need', 'direct')

def logic_7146(agents, world):
    _agent_apply(world, agents, 'health', 'shelter_need', 'direct')

def logic_7147(agents, world):
    _agent_apply(world, agents, 'stress', 'shelter_need', 'direct')

def logic_7148(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'shelter_need', 'direct')

def logic_7149(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'shelter_need', 'direct')

def logic_7150(agents, world):
    _agent_apply(world, agents, 'social_need', 'shelter_need', 'direct')

def logic_7151(agents, world):
    _agent_apply(world, agents, 'cooperation', 'shelter_need', 'direct')

def logic_7152(agents, world):
    _agent_apply(world, agents, 'defection', 'shelter_need', 'direct')

def logic_7153(agents, world):
    _agent_apply(world, agents, 'trust', 'shelter_need', 'direct')

def logic_7154(agents, world):
    _agent_apply(world, agents, 'reputation', 'shelter_need', 'direct')

def logic_7155(agents, world):
    _agent_apply(world, agents, 'help_received', 'shelter_need', 'direct')

def logic_7156(agents, world):
    _agent_apply(world, agents, 'help_given', 'shelter_need', 'direct')

def logic_7157(agents, world):
    _agent_apply(world, agents, 'local_density', 'shelter_need', 'direct')

def logic_7158(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'shelter_need', 'direct')

def logic_7159(agents, world):
    _agent_apply(world, agents, 'survival_score', 'shelter_need', 'direct')

def logic_7160(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'shelter_need', 'direct')

def logic_7161(agents, world):
    _agent_apply(world, agents, 'payoff', 'shelter_need', 'direct')

def logic_7162(agents, world):
    _agent_apply(world, agents, 'temperature', 'fire_fear', 'direct')

def logic_7163(agents, world):
    _agent_apply(world, agents, 'surface_water', 'fire_fear', 'direct')

def logic_7164(agents, world):
    _agent_apply(world, agents, 'humidity', 'fire_fear', 'direct')

def logic_7165(agents, world):
    _agent_apply(world, agents, 'cloud', 'fire_fear', 'direct')

def logic_7166(agents, world):
    _agent_apply(world, agents, 'rain', 'fire_fear', 'direct')

def logic_7167(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'fire_fear', 'direct')

def logic_7168(agents, world):
    _agent_apply(world, agents, 'runoff', 'fire_fear', 'direct')

def logic_7169(agents, world):
    _agent_apply(world, agents, 'wind_x', 'fire_fear', 'direct')

def logic_7170(agents, world):
    _agent_apply(world, agents, 'wind_y', 'fire_fear', 'direct')

def logic_7171(agents, world):
    _agent_apply(world, agents, 'vegetation', 'fire_fear', 'direct')

def logic_7172(agents, world):
    _agent_apply(world, agents, 'biomass', 'fire_fear', 'direct')

def logic_7173(agents, world):
    _agent_apply(world, agents, 'herbivore', 'fire_fear', 'direct')

def logic_7174(agents, world):
    _agent_apply(world, agents, 'predator', 'fire_fear', 'direct')

def logic_7175(agents, world):
    _agent_apply(world, agents, 'carrion', 'fire_fear', 'direct')

def logic_7176(agents, world):
    _agent_apply(world, agents, 'nutrients', 'fire_fear', 'direct')

def logic_7177(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'fire_fear', 'direct')

def logic_7178(agents, world):
    _agent_apply(world, agents, 'oxygen', 'fire_fear', 'direct')

def logic_7179(agents, world):
    _agent_apply(world, agents, 'co2', 'fire_fear', 'direct')

def logic_7180(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'fire_fear', 'direct')

def logic_7181(agents, world):
    _agent_apply(world, agents, 'ice', 'fire_fear', 'direct')

def logic_7182(agents, world):
    _agent_apply(world, agents, 'evaporation', 'fire_fear', 'direct')

def logic_7183(agents, world):
    _agent_apply(world, agents, 'detritus', 'fire_fear', 'direct')

def logic_7184(agents, world):
    _agent_apply(world, agents, 'methane', 'fire_fear', 'direct')

def logic_7185(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'fire_fear', 'direct')

def logic_7186(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'fire_fear', 'direct')

def logic_7187(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'fire_fear', 'direct')

def logic_7188(agents, world):
    _agent_apply(world, agents, 'erosion', 'fire_fear', 'direct')

def logic_7189(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'fire_fear', 'direct')

def logic_7190(agents, world):
    _agent_apply(world, agents, 'root_density', 'fire_fear', 'direct')

def logic_7191(agents, world):
    _agent_apply(world, agents, 'wetland', 'fire_fear', 'direct')

def logic_7192(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'fire_fear', 'direct')

def logic_7193(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'fire_fear', 'direct')

def logic_7194(agents, world):
    _agent_apply(world, agents, 'ash', 'fire_fear', 'direct')

def logic_7195(agents, world):
    _agent_apply(world, agents, 'snowpack', 'fire_fear', 'direct')

def logic_7196(agents, world):
    _agent_apply(world, agents, 'groundwater', 'fire_fear', 'direct')

def logic_7197(agents, world):
    _agent_apply(world, agents, 'sediment', 'fire_fear', 'direct')

def logic_7198(agents, world):
    _agent_apply(world, agents, 'salinity', 'fire_fear', 'direct')

def logic_7199(agents, world):
    _agent_apply(world, agents, 'algae', 'fire_fear', 'direct')

def logic_7200(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'fire_fear', 'direct')

def logic_7201(agents, world):
    _agent_apply(world, agents, 'deadwood', 'fire_fear', 'direct')

def logic_7202(agents, world):
    _agent_apply(world, agents, 'pollinators', 'fire_fear', 'direct')

def logic_7203(agents, world):
    _agent_apply(world, agents, 'flowers', 'fire_fear', 'direct')

def logic_7204(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'fire_fear', 'direct')

def logic_7205(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'fire_fear', 'direct')

def logic_7206(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'fire_fear', 'direct')

def logic_7207(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'fire_fear', 'direct')

def logic_7208(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'fire_fear', 'direct')

def logic_7209(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'fire_fear', 'direct')

def logic_7210(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'fire_fear', 'direct')

def logic_7211(agents, world):
    _agent_apply(world, agents, 'hydration', 'fire_fear', 'direct')

def logic_7212(agents, world):
    _agent_apply(world, agents, 'thirst', 'fire_fear', 'direct')

def logic_7213(agents, world):
    _agent_apply(world, agents, 'hunger', 'fire_fear', 'direct')

def logic_7214(agents, world):
    _agent_apply(world, agents, 'health', 'fire_fear', 'direct')

def logic_7215(agents, world):
    _agent_apply(world, agents, 'stress', 'fire_fear', 'direct')

def logic_7216(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'fire_fear', 'direct')

def logic_7217(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'fire_fear', 'direct')

def logic_7218(agents, world):
    _agent_apply(world, agents, 'social_need', 'fire_fear', 'direct')

def logic_7219(agents, world):
    _agent_apply(world, agents, 'cooperation', 'fire_fear', 'direct')

def logic_7220(agents, world):
    _agent_apply(world, agents, 'defection', 'fire_fear', 'direct')

def logic_7221(agents, world):
    _agent_apply(world, agents, 'trust', 'fire_fear', 'direct')

def logic_7222(agents, world):
    _agent_apply(world, agents, 'reputation', 'fire_fear', 'direct')

def logic_7223(agents, world):
    _agent_apply(world, agents, 'help_received', 'fire_fear', 'direct')

def logic_7224(agents, world):
    _agent_apply(world, agents, 'help_given', 'fire_fear', 'direct')

def logic_7225(agents, world):
    _agent_apply(world, agents, 'local_density', 'fire_fear', 'direct')

def logic_7226(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'fire_fear', 'direct')

def logic_7227(agents, world):
    _agent_apply(world, agents, 'survival_score', 'fire_fear', 'direct')

def logic_7228(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'fire_fear', 'direct')

def logic_7229(agents, world):
    _agent_apply(world, agents, 'payoff', 'fire_fear', 'direct')

def logic_7230(agents, world):
    _agent_apply(world, agents, 'temperature', 'resource_competition', 'direct')

def logic_7231(agents, world):
    _agent_apply(world, agents, 'surface_water', 'resource_competition', 'direct')

def logic_7232(agents, world):
    _agent_apply(world, agents, 'humidity', 'resource_competition', 'direct')

def logic_7233(agents, world):
    _agent_apply(world, agents, 'cloud', 'resource_competition', 'direct')

def logic_7234(agents, world):
    _agent_apply(world, agents, 'rain', 'resource_competition', 'direct')

def logic_7235(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'resource_competition', 'direct')

def logic_7236(agents, world):
    _agent_apply(world, agents, 'runoff', 'resource_competition', 'direct')

def logic_7237(agents, world):
    _agent_apply(world, agents, 'wind_x', 'resource_competition', 'direct')

def logic_7238(agents, world):
    _agent_apply(world, agents, 'wind_y', 'resource_competition', 'direct')

def logic_7239(agents, world):
    _agent_apply(world, agents, 'vegetation', 'resource_competition', 'direct')

def logic_7240(agents, world):
    _agent_apply(world, agents, 'biomass', 'resource_competition', 'direct')

def logic_7241(agents, world):
    _agent_apply(world, agents, 'herbivore', 'resource_competition', 'direct')

def logic_7242(agents, world):
    _agent_apply(world, agents, 'predator', 'resource_competition', 'direct')

def logic_7243(agents, world):
    _agent_apply(world, agents, 'carrion', 'resource_competition', 'direct')

def logic_7244(agents, world):
    _agent_apply(world, agents, 'nutrients', 'resource_competition', 'direct')

def logic_7245(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'resource_competition', 'direct')

def logic_7246(agents, world):
    _agent_apply(world, agents, 'oxygen', 'resource_competition', 'direct')

def logic_7247(agents, world):
    _agent_apply(world, agents, 'co2', 'resource_competition', 'direct')

def logic_7248(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'resource_competition', 'direct')

def logic_7249(agents, world):
    _agent_apply(world, agents, 'ice', 'resource_competition', 'direct')

def logic_7250(agents, world):
    _agent_apply(world, agents, 'evaporation', 'resource_competition', 'direct')

def logic_7251(agents, world):
    _agent_apply(world, agents, 'detritus', 'resource_competition', 'direct')

def logic_7252(agents, world):
    _agent_apply(world, agents, 'methane', 'resource_competition', 'direct')

def logic_7253(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'resource_competition', 'direct')

def logic_7254(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'resource_competition', 'direct')

def logic_7255(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'resource_competition', 'direct')

def logic_7256(agents, world):
    _agent_apply(world, agents, 'erosion', 'resource_competition', 'direct')

def logic_7257(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'resource_competition', 'direct')

def logic_7258(agents, world):
    _agent_apply(world, agents, 'root_density', 'resource_competition', 'direct')

def logic_7259(agents, world):
    _agent_apply(world, agents, 'wetland', 'resource_competition', 'direct')

def logic_7260(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'resource_competition', 'direct')

def logic_7261(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'resource_competition', 'direct')

def logic_7262(agents, world):
    _agent_apply(world, agents, 'ash', 'resource_competition', 'direct')

def logic_7263(agents, world):
    _agent_apply(world, agents, 'snowpack', 'resource_competition', 'direct')

def logic_7264(agents, world):
    _agent_apply(world, agents, 'groundwater', 'resource_competition', 'direct')

def logic_7265(agents, world):
    _agent_apply(world, agents, 'sediment', 'resource_competition', 'direct')

def logic_7266(agents, world):
    _agent_apply(world, agents, 'salinity', 'resource_competition', 'direct')

def logic_7267(agents, world):
    _agent_apply(world, agents, 'algae', 'resource_competition', 'direct')

def logic_7268(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'resource_competition', 'direct')

def logic_7269(agents, world):
    _agent_apply(world, agents, 'deadwood', 'resource_competition', 'direct')

def logic_7270(agents, world):
    _agent_apply(world, agents, 'pollinators', 'resource_competition', 'direct')

def logic_7271(agents, world):
    _agent_apply(world, agents, 'flowers', 'resource_competition', 'direct')

def logic_7272(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'resource_competition', 'direct')

def logic_7273(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'resource_competition', 'direct')

def logic_7274(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'resource_competition', 'direct')

def logic_7275(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'resource_competition', 'direct')

def logic_7276(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'resource_competition', 'direct')

def logic_7277(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'resource_competition', 'direct')

def logic_7278(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'resource_competition', 'direct')

def logic_7279(agents, world):
    _agent_apply(world, agents, 'hydration', 'resource_competition', 'direct')

def logic_7280(agents, world):
    _agent_apply(world, agents, 'thirst', 'resource_competition', 'direct')

def logic_7281(agents, world):
    _agent_apply(world, agents, 'hunger', 'resource_competition', 'direct')

def logic_7282(agents, world):
    _agent_apply(world, agents, 'health', 'resource_competition', 'direct')

def logic_7283(agents, world):
    _agent_apply(world, agents, 'stress', 'resource_competition', 'direct')

def logic_7284(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'resource_competition', 'direct')

def logic_7285(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'resource_competition', 'direct')

def logic_7286(agents, world):
    _agent_apply(world, agents, 'social_need', 'resource_competition', 'direct')

def logic_7287(agents, world):
    _agent_apply(world, agents, 'cooperation', 'resource_competition', 'direct')

def logic_7288(agents, world):
    _agent_apply(world, agents, 'defection', 'resource_competition', 'direct')

def logic_7289(agents, world):
    _agent_apply(world, agents, 'trust', 'resource_competition', 'direct')

def logic_7290(agents, world):
    _agent_apply(world, agents, 'reputation', 'resource_competition', 'direct')

def logic_7291(agents, world):
    _agent_apply(world, agents, 'help_received', 'resource_competition', 'direct')

def logic_7292(agents, world):
    _agent_apply(world, agents, 'help_given', 'resource_competition', 'direct')

def logic_7293(agents, world):
    _agent_apply(world, agents, 'local_density', 'resource_competition', 'direct')

def logic_7294(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'resource_competition', 'direct')

def logic_7295(agents, world):
    _agent_apply(world, agents, 'survival_score', 'resource_competition', 'direct')

def logic_7296(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'resource_competition', 'direct')

def logic_7297(agents, world):
    _agent_apply(world, agents, 'payoff', 'resource_competition', 'direct')

def logic_7298(agents, world):
    _agent_apply(world, agents, 'temperature', 'vegetation_expectation', 'direct')

def logic_7299(agents, world):
    _agent_apply(world, agents, 'surface_water', 'vegetation_expectation', 'direct')

def logic_7300(agents, world):
    _agent_apply(world, agents, 'humidity', 'vegetation_expectation', 'direct')

def logic_7301(agents, world):
    _agent_apply(world, agents, 'cloud', 'vegetation_expectation', 'direct')

def logic_7302(agents, world):
    _agent_apply(world, agents, 'rain', 'vegetation_expectation', 'direct')

def logic_7303(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'vegetation_expectation', 'direct')

def logic_7304(agents, world):
    _agent_apply(world, agents, 'runoff', 'vegetation_expectation', 'direct')

def logic_7305(agents, world):
    _agent_apply(world, agents, 'wind_x', 'vegetation_expectation', 'direct')

def logic_7306(agents, world):
    _agent_apply(world, agents, 'wind_y', 'vegetation_expectation', 'direct')

def logic_7307(agents, world):
    _agent_apply(world, agents, 'vegetation', 'vegetation_expectation', 'direct')

def logic_7308(agents, world):
    _agent_apply(world, agents, 'biomass', 'vegetation_expectation', 'direct')

def logic_7309(agents, world):
    _agent_apply(world, agents, 'herbivore', 'vegetation_expectation', 'direct')

def logic_7310(agents, world):
    _agent_apply(world, agents, 'predator', 'vegetation_expectation', 'direct')

def logic_7311(agents, world):
    _agent_apply(world, agents, 'carrion', 'vegetation_expectation', 'direct')

def logic_7312(agents, world):
    _agent_apply(world, agents, 'nutrients', 'vegetation_expectation', 'direct')

def logic_7313(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'vegetation_expectation', 'direct')

def logic_7314(agents, world):
    _agent_apply(world, agents, 'oxygen', 'vegetation_expectation', 'direct')

def logic_7315(agents, world):
    _agent_apply(world, agents, 'co2', 'vegetation_expectation', 'direct')

def logic_7316(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'vegetation_expectation', 'direct')

def logic_7317(agents, world):
    _agent_apply(world, agents, 'ice', 'vegetation_expectation', 'direct')

def logic_7318(agents, world):
    _agent_apply(world, agents, 'evaporation', 'vegetation_expectation', 'direct')

def logic_7319(agents, world):
    _agent_apply(world, agents, 'detritus', 'vegetation_expectation', 'direct')

def logic_7320(agents, world):
    _agent_apply(world, agents, 'methane', 'vegetation_expectation', 'direct')

def logic_7321(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'vegetation_expectation', 'direct')

def logic_7322(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'vegetation_expectation', 'direct')

def logic_7323(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'vegetation_expectation', 'direct')

def logic_7324(agents, world):
    _agent_apply(world, agents, 'erosion', 'vegetation_expectation', 'direct')

def logic_7325(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'vegetation_expectation', 'direct')

def logic_7326(agents, world):
    _agent_apply(world, agents, 'root_density', 'vegetation_expectation', 'direct')

def logic_7327(agents, world):
    _agent_apply(world, agents, 'wetland', 'vegetation_expectation', 'direct')

def logic_7328(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'vegetation_expectation', 'direct')

def logic_7329(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'vegetation_expectation', 'direct')

def logic_7330(agents, world):
    _agent_apply(world, agents, 'ash', 'vegetation_expectation', 'direct')

def logic_7331(agents, world):
    _agent_apply(world, agents, 'snowpack', 'vegetation_expectation', 'direct')

def logic_7332(agents, world):
    _agent_apply(world, agents, 'groundwater', 'vegetation_expectation', 'direct')

def logic_7333(agents, world):
    _agent_apply(world, agents, 'sediment', 'vegetation_expectation', 'direct')

def logic_7334(agents, world):
    _agent_apply(world, agents, 'salinity', 'vegetation_expectation', 'direct')

def logic_7335(agents, world):
    _agent_apply(world, agents, 'algae', 'vegetation_expectation', 'direct')

def logic_7336(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'vegetation_expectation', 'direct')

def logic_7337(agents, world):
    _agent_apply(world, agents, 'deadwood', 'vegetation_expectation', 'direct')

def logic_7338(agents, world):
    _agent_apply(world, agents, 'pollinators', 'vegetation_expectation', 'direct')

def logic_7339(agents, world):
    _agent_apply(world, agents, 'flowers', 'vegetation_expectation', 'direct')

def logic_7340(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'vegetation_expectation', 'direct')

def logic_7341(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'vegetation_expectation', 'direct')

def logic_7342(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'vegetation_expectation', 'direct')

def logic_7343(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'vegetation_expectation', 'direct')

def logic_7344(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'vegetation_expectation', 'direct')

def logic_7345(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'vegetation_expectation', 'direct')

def logic_7346(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'vegetation_expectation', 'direct')

def logic_7347(agents, world):
    _agent_apply(world, agents, 'hydration', 'vegetation_expectation', 'direct')

def logic_7348(agents, world):
    _agent_apply(world, agents, 'thirst', 'vegetation_expectation', 'direct')

def logic_7349(agents, world):
    _agent_apply(world, agents, 'hunger', 'vegetation_expectation', 'direct')

def logic_7350(agents, world):
    _agent_apply(world, agents, 'health', 'vegetation_expectation', 'direct')

def logic_7351(agents, world):
    _agent_apply(world, agents, 'stress', 'vegetation_expectation', 'direct')

def logic_7352(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'vegetation_expectation', 'direct')

def logic_7353(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'vegetation_expectation', 'direct')

def logic_7354(agents, world):
    _agent_apply(world, agents, 'social_need', 'vegetation_expectation', 'direct')

def logic_7355(agents, world):
    _agent_apply(world, agents, 'cooperation', 'vegetation_expectation', 'direct')

def logic_7356(agents, world):
    _agent_apply(world, agents, 'defection', 'vegetation_expectation', 'direct')

def logic_7357(agents, world):
    _agent_apply(world, agents, 'trust', 'vegetation_expectation', 'direct')

def logic_7358(agents, world):
    _agent_apply(world, agents, 'reputation', 'vegetation_expectation', 'direct')

def logic_7359(agents, world):
    _agent_apply(world, agents, 'help_received', 'vegetation_expectation', 'direct')

def logic_7360(agents, world):
    _agent_apply(world, agents, 'help_given', 'vegetation_expectation', 'direct')

def logic_7361(agents, world):
    _agent_apply(world, agents, 'local_density', 'vegetation_expectation', 'direct')

def logic_7362(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'vegetation_expectation', 'direct')

def logic_7363(agents, world):
    _agent_apply(world, agents, 'survival_score', 'vegetation_expectation', 'direct')

def logic_7364(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'vegetation_expectation', 'direct')

def logic_7365(agents, world):
    _agent_apply(world, agents, 'payoff', 'vegetation_expectation', 'direct')

def logic_7366(agents, world):
    _agent_apply(world, agents, 'temperature', 'stress', 'direct')

def logic_7367(agents, world):
    _agent_apply(world, agents, 'surface_water', 'stress', 'direct')

def logic_7368(agents, world):
    _agent_apply(world, agents, 'humidity', 'stress', 'direct')

def logic_7369(agents, world):
    _agent_apply(world, agents, 'cloud', 'stress', 'direct')

def logic_7370(agents, world):
    _agent_apply(world, agents, 'rain', 'stress', 'direct')

def logic_7371(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'stress', 'direct')

def logic_7372(agents, world):
    _agent_apply(world, agents, 'runoff', 'stress', 'direct')

def logic_7373(agents, world):
    _agent_apply(world, agents, 'wind_x', 'stress', 'direct')

def logic_7374(agents, world):
    _agent_apply(world, agents, 'wind_y', 'stress', 'direct')

def logic_7375(agents, world):
    _agent_apply(world, agents, 'vegetation', 'stress', 'direct')

def logic_7376(agents, world):
    _agent_apply(world, agents, 'biomass', 'stress', 'direct')

def logic_7377(agents, world):
    _agent_apply(world, agents, 'herbivore', 'stress', 'direct')

def logic_7378(agents, world):
    _agent_apply(world, agents, 'predator', 'stress', 'direct')

def logic_7379(agents, world):
    _agent_apply(world, agents, 'carrion', 'stress', 'direct')

def logic_7380(agents, world):
    _agent_apply(world, agents, 'nutrients', 'stress', 'direct')

def logic_7381(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'stress', 'direct')

def logic_7382(agents, world):
    _agent_apply(world, agents, 'oxygen', 'stress', 'direct')

def logic_7383(agents, world):
    _agent_apply(world, agents, 'co2', 'stress', 'direct')

def logic_7384(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'stress', 'direct')

def logic_7385(agents, world):
    _agent_apply(world, agents, 'ice', 'stress', 'direct')

def logic_7386(agents, world):
    _agent_apply(world, agents, 'evaporation', 'stress', 'direct')

def logic_7387(agents, world):
    _agent_apply(world, agents, 'detritus', 'stress', 'direct')

def logic_7388(agents, world):
    _agent_apply(world, agents, 'methane', 'stress', 'direct')

def logic_7389(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'stress', 'direct')

def logic_7390(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'stress', 'direct')

def logic_7391(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'stress', 'direct')

def logic_7392(agents, world):
    _agent_apply(world, agents, 'erosion', 'stress', 'direct')

def logic_7393(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'stress', 'direct')

def logic_7394(agents, world):
    _agent_apply(world, agents, 'root_density', 'stress', 'direct')

def logic_7395(agents, world):
    _agent_apply(world, agents, 'wetland', 'stress', 'direct')

def logic_7396(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'stress', 'direct')

def logic_7397(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'stress', 'direct')

def logic_7398(agents, world):
    _agent_apply(world, agents, 'ash', 'stress', 'direct')

def logic_7399(agents, world):
    _agent_apply(world, agents, 'snowpack', 'stress', 'direct')

def logic_7400(agents, world):
    _agent_apply(world, agents, 'groundwater', 'stress', 'direct')

def logic_7401(agents, world):
    _agent_apply(world, agents, 'sediment', 'stress', 'direct')

def logic_7402(agents, world):
    _agent_apply(world, agents, 'salinity', 'stress', 'direct')

def logic_7403(agents, world):
    _agent_apply(world, agents, 'algae', 'stress', 'direct')

def logic_7404(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'stress', 'direct')

def logic_7405(agents, world):
    _agent_apply(world, agents, 'deadwood', 'stress', 'direct')

def logic_7406(agents, world):
    _agent_apply(world, agents, 'pollinators', 'stress', 'direct')

def logic_7407(agents, world):
    _agent_apply(world, agents, 'flowers', 'stress', 'direct')

def logic_7408(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'stress', 'direct')

def logic_7409(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'stress', 'direct')

def logic_7410(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'stress', 'direct')

def logic_7411(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'stress', 'direct')

def logic_7412(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'stress', 'direct')

def logic_7413(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'stress', 'direct')

def logic_7414(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'stress', 'direct')

def logic_7415(agents, world):
    _agent_apply(world, agents, 'hydration', 'stress', 'direct')

def logic_7416(agents, world):
    _agent_apply(world, agents, 'thirst', 'stress', 'direct')

def logic_7417(agents, world):
    _agent_apply(world, agents, 'hunger', 'stress', 'direct')

def logic_7418(agents, world):
    _agent_apply(world, agents, 'health', 'stress', 'direct')

def logic_7419(agents, world):
    _agent_apply(world, agents, 'stress', 'stress', 'direct')

def logic_7420(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'stress', 'direct')

def logic_7421(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'stress', 'direct')

def logic_7422(agents, world):
    _agent_apply(world, agents, 'social_need', 'stress', 'direct')

def logic_7423(agents, world):
    _agent_apply(world, agents, 'cooperation', 'stress', 'direct')

def logic_7424(agents, world):
    _agent_apply(world, agents, 'defection', 'stress', 'direct')

def logic_7425(agents, world):
    _agent_apply(world, agents, 'trust', 'stress', 'direct')

def logic_7426(agents, world):
    _agent_apply(world, agents, 'reputation', 'stress', 'direct')

def logic_7427(agents, world):
    _agent_apply(world, agents, 'help_received', 'stress', 'direct')

def logic_7428(agents, world):
    _agent_apply(world, agents, 'help_given', 'stress', 'direct')

def logic_7429(agents, world):
    _agent_apply(world, agents, 'local_density', 'stress', 'direct')

def logic_7430(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'stress', 'direct')

def logic_7431(agents, world):
    _agent_apply(world, agents, 'survival_score', 'stress', 'direct')

def logic_7432(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'stress', 'direct')

def logic_7433(agents, world):
    _agent_apply(world, agents, 'payoff', 'stress', 'direct')

def logic_7434(agents, world):
    _agent_apply(world, agents, 'temperature', 'social_need', 'direct')

def logic_7435(agents, world):
    _agent_apply(world, agents, 'surface_water', 'social_need', 'direct')

def logic_7436(agents, world):
    _agent_apply(world, agents, 'humidity', 'social_need', 'direct')

def logic_7437(agents, world):
    _agent_apply(world, agents, 'cloud', 'social_need', 'direct')

def logic_7438(agents, world):
    _agent_apply(world, agents, 'rain', 'social_need', 'direct')

def logic_7439(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'social_need', 'direct')

def logic_7440(agents, world):
    _agent_apply(world, agents, 'runoff', 'social_need', 'direct')

def logic_7441(agents, world):
    _agent_apply(world, agents, 'wind_x', 'social_need', 'direct')

def logic_7442(agents, world):
    _agent_apply(world, agents, 'wind_y', 'social_need', 'direct')

def logic_7443(agents, world):
    _agent_apply(world, agents, 'vegetation', 'social_need', 'direct')

def logic_7444(agents, world):
    _agent_apply(world, agents, 'biomass', 'social_need', 'direct')

def logic_7445(agents, world):
    _agent_apply(world, agents, 'herbivore', 'social_need', 'direct')

def logic_7446(agents, world):
    _agent_apply(world, agents, 'predator', 'social_need', 'direct')

def logic_7447(agents, world):
    _agent_apply(world, agents, 'carrion', 'social_need', 'direct')

def logic_7448(agents, world):
    _agent_apply(world, agents, 'nutrients', 'social_need', 'direct')

def logic_7449(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'social_need', 'direct')

def logic_7450(agents, world):
    _agent_apply(world, agents, 'oxygen', 'social_need', 'direct')

def logic_7451(agents, world):
    _agent_apply(world, agents, 'co2', 'social_need', 'direct')

def logic_7452(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'social_need', 'direct')

def logic_7453(agents, world):
    _agent_apply(world, agents, 'ice', 'social_need', 'direct')

def logic_7454(agents, world):
    _agent_apply(world, agents, 'evaporation', 'social_need', 'direct')

def logic_7455(agents, world):
    _agent_apply(world, agents, 'detritus', 'social_need', 'direct')

def logic_7456(agents, world):
    _agent_apply(world, agents, 'methane', 'social_need', 'direct')

def logic_7457(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'social_need', 'direct')

def logic_7458(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'social_need', 'direct')

def logic_7459(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'social_need', 'direct')

def logic_7460(agents, world):
    _agent_apply(world, agents, 'erosion', 'social_need', 'direct')

def logic_7461(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'social_need', 'direct')

def logic_7462(agents, world):
    _agent_apply(world, agents, 'root_density', 'social_need', 'direct')

def logic_7463(agents, world):
    _agent_apply(world, agents, 'wetland', 'social_need', 'direct')

def logic_7464(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'social_need', 'direct')

def logic_7465(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'social_need', 'direct')

def logic_7466(agents, world):
    _agent_apply(world, agents, 'ash', 'social_need', 'direct')

def logic_7467(agents, world):
    _agent_apply(world, agents, 'snowpack', 'social_need', 'direct')

def logic_7468(agents, world):
    _agent_apply(world, agents, 'groundwater', 'social_need', 'direct')

def logic_7469(agents, world):
    _agent_apply(world, agents, 'sediment', 'social_need', 'direct')

def logic_7470(agents, world):
    _agent_apply(world, agents, 'salinity', 'social_need', 'direct')

def logic_7471(agents, world):
    _agent_apply(world, agents, 'algae', 'social_need', 'direct')

def logic_7472(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'social_need', 'direct')

def logic_7473(agents, world):
    _agent_apply(world, agents, 'deadwood', 'social_need', 'direct')

def logic_7474(agents, world):
    _agent_apply(world, agents, 'pollinators', 'social_need', 'direct')

def logic_7475(agents, world):
    _agent_apply(world, agents, 'flowers', 'social_need', 'direct')

def logic_7476(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'social_need', 'direct')

def logic_7477(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'social_need', 'direct')

def logic_7478(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'social_need', 'direct')

def logic_7479(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'social_need', 'direct')

def logic_7480(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'social_need', 'direct')

def logic_7481(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'social_need', 'direct')

def logic_7482(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'social_need', 'direct')

def logic_7483(agents, world):
    _agent_apply(world, agents, 'hydration', 'social_need', 'direct')

def logic_7484(agents, world):
    _agent_apply(world, agents, 'thirst', 'social_need', 'direct')

def logic_7485(agents, world):
    _agent_apply(world, agents, 'hunger', 'social_need', 'direct')

def logic_7486(agents, world):
    _agent_apply(world, agents, 'health', 'social_need', 'direct')

def logic_7487(agents, world):
    _agent_apply(world, agents, 'stress', 'social_need', 'direct')

def logic_7488(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'social_need', 'direct')

def logic_7489(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'social_need', 'direct')

def logic_7490(agents, world):
    _agent_apply(world, agents, 'social_need', 'social_need', 'direct')

def logic_7491(agents, world):
    _agent_apply(world, agents, 'cooperation', 'social_need', 'direct')

def logic_7492(agents, world):
    _agent_apply(world, agents, 'defection', 'social_need', 'direct')

def logic_7493(agents, world):
    _agent_apply(world, agents, 'trust', 'social_need', 'direct')

def logic_7494(agents, world):
    _agent_apply(world, agents, 'reputation', 'social_need', 'direct')

def logic_7495(agents, world):
    _agent_apply(world, agents, 'help_received', 'social_need', 'direct')

def logic_7496(agents, world):
    _agent_apply(world, agents, 'help_given', 'social_need', 'direct')

def logic_7497(agents, world):
    _agent_apply(world, agents, 'local_density', 'social_need', 'direct')

def logic_7498(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'social_need', 'direct')

def logic_7499(agents, world):
    _agent_apply(world, agents, 'survival_score', 'social_need', 'direct')

def logic_7500(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'social_need', 'direct')

def logic_7501(agents, world):
    _agent_apply(world, agents, 'payoff', 'social_need', 'direct')

def logic_7502(agents, world):
    _agent_apply(world, agents, 'temperature', 'neighbor_energy_gap', 'direct')

def logic_7503(agents, world):
    _agent_apply(world, agents, 'surface_water', 'neighbor_energy_gap', 'direct')

def logic_7504(agents, world):
    _agent_apply(world, agents, 'humidity', 'neighbor_energy_gap', 'direct')

def logic_7505(agents, world):
    _agent_apply(world, agents, 'cloud', 'neighbor_energy_gap', 'direct')

def logic_7506(agents, world):
    _agent_apply(world, agents, 'rain', 'neighbor_energy_gap', 'direct')

def logic_7507(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'neighbor_energy_gap', 'direct')

def logic_7508(agents, world):
    _agent_apply(world, agents, 'runoff', 'neighbor_energy_gap', 'direct')

def logic_7509(agents, world):
    _agent_apply(world, agents, 'wind_x', 'neighbor_energy_gap', 'direct')

def logic_7510(agents, world):
    _agent_apply(world, agents, 'wind_y', 'neighbor_energy_gap', 'direct')

def logic_7511(agents, world):
    _agent_apply(world, agents, 'vegetation', 'neighbor_energy_gap', 'direct')

def logic_7512(agents, world):
    _agent_apply(world, agents, 'biomass', 'neighbor_energy_gap', 'direct')

def logic_7513(agents, world):
    _agent_apply(world, agents, 'herbivore', 'neighbor_energy_gap', 'direct')

def logic_7514(agents, world):
    _agent_apply(world, agents, 'predator', 'neighbor_energy_gap', 'direct')

def logic_7515(agents, world):
    _agent_apply(world, agents, 'carrion', 'neighbor_energy_gap', 'direct')

def logic_7516(agents, world):
    _agent_apply(world, agents, 'nutrients', 'neighbor_energy_gap', 'direct')

def logic_7517(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'neighbor_energy_gap', 'direct')

def logic_7518(agents, world):
    _agent_apply(world, agents, 'oxygen', 'neighbor_energy_gap', 'direct')

def logic_7519(agents, world):
    _agent_apply(world, agents, 'co2', 'neighbor_energy_gap', 'direct')

def logic_7520(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'neighbor_energy_gap', 'direct')

def logic_7521(agents, world):
    _agent_apply(world, agents, 'ice', 'neighbor_energy_gap', 'direct')

def logic_7522(agents, world):
    _agent_apply(world, agents, 'evaporation', 'neighbor_energy_gap', 'direct')

def logic_7523(agents, world):
    _agent_apply(world, agents, 'detritus', 'neighbor_energy_gap', 'direct')

def logic_7524(agents, world):
    _agent_apply(world, agents, 'methane', 'neighbor_energy_gap', 'direct')

def logic_7525(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'neighbor_energy_gap', 'direct')

def logic_7526(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'neighbor_energy_gap', 'direct')

def logic_7527(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'neighbor_energy_gap', 'direct')

def logic_7528(agents, world):
    _agent_apply(world, agents, 'erosion', 'neighbor_energy_gap', 'direct')

def logic_7529(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'neighbor_energy_gap', 'direct')

def logic_7530(agents, world):
    _agent_apply(world, agents, 'root_density', 'neighbor_energy_gap', 'direct')

def logic_7531(agents, world):
    _agent_apply(world, agents, 'wetland', 'neighbor_energy_gap', 'direct')

def logic_7532(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'neighbor_energy_gap', 'direct')

def logic_7533(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'neighbor_energy_gap', 'direct')

def logic_7534(agents, world):
    _agent_apply(world, agents, 'ash', 'neighbor_energy_gap', 'direct')

def logic_7535(agents, world):
    _agent_apply(world, agents, 'snowpack', 'neighbor_energy_gap', 'direct')

def logic_7536(agents, world):
    _agent_apply(world, agents, 'groundwater', 'neighbor_energy_gap', 'direct')

def logic_7537(agents, world):
    _agent_apply(world, agents, 'sediment', 'neighbor_energy_gap', 'direct')

def logic_7538(agents, world):
    _agent_apply(world, agents, 'salinity', 'neighbor_energy_gap', 'direct')

def logic_7539(agents, world):
    _agent_apply(world, agents, 'algae', 'neighbor_energy_gap', 'direct')

def logic_7540(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'neighbor_energy_gap', 'direct')

def logic_7541(agents, world):
    _agent_apply(world, agents, 'deadwood', 'neighbor_energy_gap', 'direct')

def logic_7542(agents, world):
    _agent_apply(world, agents, 'pollinators', 'neighbor_energy_gap', 'direct')

def logic_7543(agents, world):
    _agent_apply(world, agents, 'flowers', 'neighbor_energy_gap', 'direct')

def logic_7544(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'neighbor_energy_gap', 'direct')

def logic_7545(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'neighbor_energy_gap', 'direct')

def logic_7546(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'neighbor_energy_gap', 'direct')

def logic_7547(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'neighbor_energy_gap', 'direct')

def logic_7548(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'neighbor_energy_gap', 'direct')

def logic_7549(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'neighbor_energy_gap', 'direct')

def logic_7550(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'neighbor_energy_gap', 'direct')

def logic_7551(agents, world):
    _agent_apply(world, agents, 'hydration', 'neighbor_energy_gap', 'direct')

def logic_7552(agents, world):
    _agent_apply(world, agents, 'thirst', 'neighbor_energy_gap', 'direct')

def logic_7553(agents, world):
    _agent_apply(world, agents, 'hunger', 'neighbor_energy_gap', 'direct')

def logic_7554(agents, world):
    _agent_apply(world, agents, 'health', 'neighbor_energy_gap', 'direct')

def logic_7555(agents, world):
    _agent_apply(world, agents, 'stress', 'neighbor_energy_gap', 'direct')

def logic_7556(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'neighbor_energy_gap', 'direct')

def logic_7557(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'neighbor_energy_gap', 'direct')

def logic_7558(agents, world):
    _agent_apply(world, agents, 'social_need', 'neighbor_energy_gap', 'direct')

def logic_7559(agents, world):
    _agent_apply(world, agents, 'cooperation', 'neighbor_energy_gap', 'direct')

def logic_7560(agents, world):
    _agent_apply(world, agents, 'defection', 'neighbor_energy_gap', 'direct')

def logic_7561(agents, world):
    _agent_apply(world, agents, 'trust', 'neighbor_energy_gap', 'direct')

def logic_7562(agents, world):
    _agent_apply(world, agents, 'reputation', 'neighbor_energy_gap', 'direct')

def logic_7563(agents, world):
    _agent_apply(world, agents, 'help_received', 'neighbor_energy_gap', 'direct')

def logic_7564(agents, world):
    _agent_apply(world, agents, 'help_given', 'neighbor_energy_gap', 'direct')

def logic_7565(agents, world):
    _agent_apply(world, agents, 'local_density', 'neighbor_energy_gap', 'direct')

def logic_7566(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'neighbor_energy_gap', 'direct')

def logic_7567(agents, world):
    _agent_apply(world, agents, 'survival_score', 'neighbor_energy_gap', 'direct')

def logic_7568(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'neighbor_energy_gap', 'direct')

def logic_7569(agents, world):
    _agent_apply(world, agents, 'payoff', 'neighbor_energy_gap', 'direct')

def logic_7570(agents, world):
    _agent_apply(world, agents, 'temperature', 'neighbor_health_gap', 'direct')

def logic_7571(agents, world):
    _agent_apply(world, agents, 'surface_water', 'neighbor_health_gap', 'direct')

def logic_7572(agents, world):
    _agent_apply(world, agents, 'humidity', 'neighbor_health_gap', 'direct')

def logic_7573(agents, world):
    _agent_apply(world, agents, 'cloud', 'neighbor_health_gap', 'direct')

def logic_7574(agents, world):
    _agent_apply(world, agents, 'rain', 'neighbor_health_gap', 'direct')

def logic_7575(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'neighbor_health_gap', 'direct')

def logic_7576(agents, world):
    _agent_apply(world, agents, 'runoff', 'neighbor_health_gap', 'direct')

def logic_7577(agents, world):
    _agent_apply(world, agents, 'wind_x', 'neighbor_health_gap', 'direct')

def logic_7578(agents, world):
    _agent_apply(world, agents, 'wind_y', 'neighbor_health_gap', 'direct')

def logic_7579(agents, world):
    _agent_apply(world, agents, 'vegetation', 'neighbor_health_gap', 'direct')

def logic_7580(agents, world):
    _agent_apply(world, agents, 'biomass', 'neighbor_health_gap', 'direct')

def logic_7581(agents, world):
    _agent_apply(world, agents, 'herbivore', 'neighbor_health_gap', 'direct')

def logic_7582(agents, world):
    _agent_apply(world, agents, 'predator', 'neighbor_health_gap', 'direct')

def logic_7583(agents, world):
    _agent_apply(world, agents, 'carrion', 'neighbor_health_gap', 'direct')

def logic_7584(agents, world):
    _agent_apply(world, agents, 'nutrients', 'neighbor_health_gap', 'direct')

def logic_7585(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'neighbor_health_gap', 'direct')

def logic_7586(agents, world):
    _agent_apply(world, agents, 'oxygen', 'neighbor_health_gap', 'direct')

def logic_7587(agents, world):
    _agent_apply(world, agents, 'co2', 'neighbor_health_gap', 'direct')

def logic_7588(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'neighbor_health_gap', 'direct')

def logic_7589(agents, world):
    _agent_apply(world, agents, 'ice', 'neighbor_health_gap', 'direct')

def logic_7590(agents, world):
    _agent_apply(world, agents, 'evaporation', 'neighbor_health_gap', 'direct')

def logic_7591(agents, world):
    _agent_apply(world, agents, 'detritus', 'neighbor_health_gap', 'direct')

def logic_7592(agents, world):
    _agent_apply(world, agents, 'methane', 'neighbor_health_gap', 'direct')

def logic_7593(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'neighbor_health_gap', 'direct')

def logic_7594(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'neighbor_health_gap', 'direct')

def logic_7595(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'neighbor_health_gap', 'direct')

def logic_7596(agents, world):
    _agent_apply(world, agents, 'erosion', 'neighbor_health_gap', 'direct')

def logic_7597(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'neighbor_health_gap', 'direct')

def logic_7598(agents, world):
    _agent_apply(world, agents, 'root_density', 'neighbor_health_gap', 'direct')

def logic_7599(agents, world):
    _agent_apply(world, agents, 'wetland', 'neighbor_health_gap', 'direct')

def logic_7600(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'neighbor_health_gap', 'direct')

def logic_7601(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'neighbor_health_gap', 'direct')

def logic_7602(agents, world):
    _agent_apply(world, agents, 'ash', 'neighbor_health_gap', 'direct')

def logic_7603(agents, world):
    _agent_apply(world, agents, 'snowpack', 'neighbor_health_gap', 'direct')

def logic_7604(agents, world):
    _agent_apply(world, agents, 'groundwater', 'neighbor_health_gap', 'direct')

def logic_7605(agents, world):
    _agent_apply(world, agents, 'sediment', 'neighbor_health_gap', 'direct')

def logic_7606(agents, world):
    _agent_apply(world, agents, 'salinity', 'neighbor_health_gap', 'direct')

def logic_7607(agents, world):
    _agent_apply(world, agents, 'algae', 'neighbor_health_gap', 'direct')

def logic_7608(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'neighbor_health_gap', 'direct')

def logic_7609(agents, world):
    _agent_apply(world, agents, 'deadwood', 'neighbor_health_gap', 'direct')

def logic_7610(agents, world):
    _agent_apply(world, agents, 'pollinators', 'neighbor_health_gap', 'direct')

def logic_7611(agents, world):
    _agent_apply(world, agents, 'flowers', 'neighbor_health_gap', 'direct')

def logic_7612(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'neighbor_health_gap', 'direct')

def logic_7613(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'neighbor_health_gap', 'direct')

def logic_7614(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'neighbor_health_gap', 'direct')

def logic_7615(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'neighbor_health_gap', 'direct')

def logic_7616(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'neighbor_health_gap', 'direct')

def logic_7617(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'neighbor_health_gap', 'direct')

def logic_7618(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'neighbor_health_gap', 'direct')

def logic_7619(agents, world):
    _agent_apply(world, agents, 'hydration', 'neighbor_health_gap', 'direct')

def logic_7620(agents, world):
    _agent_apply(world, agents, 'thirst', 'neighbor_health_gap', 'direct')

def logic_7621(agents, world):
    _agent_apply(world, agents, 'hunger', 'neighbor_health_gap', 'direct')

def logic_7622(agents, world):
    _agent_apply(world, agents, 'health', 'neighbor_health_gap', 'direct')

def logic_7623(agents, world):
    _agent_apply(world, agents, 'stress', 'neighbor_health_gap', 'direct')

def logic_7624(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'neighbor_health_gap', 'direct')

def logic_7625(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'neighbor_health_gap', 'direct')

def logic_7626(agents, world):
    _agent_apply(world, agents, 'social_need', 'neighbor_health_gap', 'direct')

def logic_7627(agents, world):
    _agent_apply(world, agents, 'cooperation', 'neighbor_health_gap', 'direct')

def logic_7628(agents, world):
    _agent_apply(world, agents, 'defection', 'neighbor_health_gap', 'direct')

def logic_7629(agents, world):
    _agent_apply(world, agents, 'trust', 'neighbor_health_gap', 'direct')

def logic_7630(agents, world):
    _agent_apply(world, agents, 'reputation', 'neighbor_health_gap', 'direct')

def logic_7631(agents, world):
    _agent_apply(world, agents, 'help_received', 'neighbor_health_gap', 'direct')

def logic_7632(agents, world):
    _agent_apply(world, agents, 'help_given', 'neighbor_health_gap', 'direct')

def logic_7633(agents, world):
    _agent_apply(world, agents, 'local_density', 'neighbor_health_gap', 'direct')

def logic_7634(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'neighbor_health_gap', 'direct')

def logic_7635(agents, world):
    _agent_apply(world, agents, 'survival_score', 'neighbor_health_gap', 'direct')

def logic_7636(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'neighbor_health_gap', 'direct')

def logic_7637(agents, world):
    _agent_apply(world, agents, 'payoff', 'neighbor_health_gap', 'direct')

def logic_7638(agents, world):
    _agent_apply(world, agents, 'temperature', 'betrayal_memory', 'direct')

def logic_7639(agents, world):
    _agent_apply(world, agents, 'surface_water', 'betrayal_memory', 'direct')

def logic_7640(agents, world):
    _agent_apply(world, agents, 'humidity', 'betrayal_memory', 'direct')

def logic_7641(agents, world):
    _agent_apply(world, agents, 'cloud', 'betrayal_memory', 'direct')

def logic_7642(agents, world):
    _agent_apply(world, agents, 'rain', 'betrayal_memory', 'direct')

def logic_7643(agents, world):
    _agent_apply(world, agents, 'soil_moisture', 'betrayal_memory', 'direct')

def logic_7644(agents, world):
    _agent_apply(world, agents, 'runoff', 'betrayal_memory', 'direct')

def logic_7645(agents, world):
    _agent_apply(world, agents, 'wind_x', 'betrayal_memory', 'direct')

def logic_7646(agents, world):
    _agent_apply(world, agents, 'wind_y', 'betrayal_memory', 'direct')

def logic_7647(agents, world):
    _agent_apply(world, agents, 'vegetation', 'betrayal_memory', 'direct')

def logic_7648(agents, world):
    _agent_apply(world, agents, 'biomass', 'betrayal_memory', 'direct')

def logic_7649(agents, world):
    _agent_apply(world, agents, 'herbivore', 'betrayal_memory', 'direct')

def logic_7650(agents, world):
    _agent_apply(world, agents, 'predator', 'betrayal_memory', 'direct')

def logic_7651(agents, world):
    _agent_apply(world, agents, 'carrion', 'betrayal_memory', 'direct')

def logic_7652(agents, world):
    _agent_apply(world, agents, 'nutrients', 'betrayal_memory', 'direct')

def logic_7653(agents, world):
    _agent_apply(world, agents, 'decomposition_rate', 'betrayal_memory', 'direct')

def logic_7654(agents, world):
    _agent_apply(world, agents, 'oxygen', 'betrayal_memory', 'direct')

def logic_7655(agents, world):
    _agent_apply(world, agents, 'co2', 'betrayal_memory', 'direct')

def logic_7656(agents, world):
    _agent_apply(world, agents, 'photosynthesis_factor', 'betrayal_memory', 'direct')

def logic_7657(agents, world):
    _agent_apply(world, agents, 'ice', 'betrayal_memory', 'direct')

def logic_7658(agents, world):
    _agent_apply(world, agents, 'evaporation', 'betrayal_memory', 'direct')

def logic_7659(agents, world):
    _agent_apply(world, agents, 'detritus', 'betrayal_memory', 'direct')

def logic_7660(agents, world):
    _agent_apply(world, agents, 'methane', 'betrayal_memory', 'direct')

def logic_7661(agents, world):
    _agent_apply(world, agents, 'pathogen_load', 'betrayal_memory', 'direct')

def logic_7662(agents, world):
    _agent_apply(world, agents, 'biodiversity', 'betrayal_memory', 'direct')

def logic_7663(agents, world):
    _agent_apply(world, agents, 'habitat_stress', 'betrayal_memory', 'direct')

def logic_7664(agents, world):
    _agent_apply(world, agents, 'erosion', 'betrayal_memory', 'direct')

def logic_7665(agents, world):
    _agent_apply(world, agents, 'soil_depth', 'betrayal_memory', 'direct')

def logic_7666(agents, world):
    _agent_apply(world, agents, 'root_density', 'betrayal_memory', 'direct')

def logic_7667(agents, world):
    _agent_apply(world, agents, 'wetland', 'betrayal_memory', 'direct')

def logic_7668(agents, world):
    _agent_apply(world, agents, 'carbon_storage', 'betrayal_memory', 'direct')

def logic_7669(agents, world):
    _agent_apply(world, agents, 'fire_risk', 'betrayal_memory', 'direct')

def logic_7670(agents, world):
    _agent_apply(world, agents, 'ash', 'betrayal_memory', 'direct')

def logic_7671(agents, world):
    _agent_apply(world, agents, 'snowpack', 'betrayal_memory', 'direct')

def logic_7672(agents, world):
    _agent_apply(world, agents, 'groundwater', 'betrayal_memory', 'direct')

def logic_7673(agents, world):
    _agent_apply(world, agents, 'sediment', 'betrayal_memory', 'direct')

def logic_7674(agents, world):
    _agent_apply(world, agents, 'salinity', 'betrayal_memory', 'direct')

def logic_7675(agents, world):
    _agent_apply(world, agents, 'algae', 'betrayal_memory', 'direct')

def logic_7676(agents, world):
    _agent_apply(world, agents, 'organic_matter', 'betrayal_memory', 'direct')

def logic_7677(agents, world):
    _agent_apply(world, agents, 'deadwood', 'betrayal_memory', 'direct')

def logic_7678(agents, world):
    _agent_apply(world, agents, 'pollinators', 'betrayal_memory', 'direct')

def logic_7679(agents, world):
    _agent_apply(world, agents, 'flowers', 'betrayal_memory', 'direct')

def logic_7680(agents, world):
    _agent_apply(world, agents, 'seed_bank', 'betrayal_memory', 'direct')

def logic_7681(agents, world):
    _agent_apply(world, agents, 'soil_carbon', 'betrayal_memory', 'direct')

def logic_7682(agents, world):
    _agent_apply(world, agents, 'surface_ice', 'betrayal_memory', 'direct')

def logic_7683(agents, world):
    _agent_apply(world, agents, 'resource_scarcity', 'betrayal_memory', 'direct')

def logic_7684(agents, world):
    _agent_apply(world, agents, 'resource_abundance', 'betrayal_memory', 'direct')

def logic_7685(agents, world):
    _agent_apply(world, agents, 'energy_surplus', 'betrayal_memory', 'direct')

def logic_7686(agents, world):
    _agent_apply(world, agents, 'ticks_since_food', 'betrayal_memory', 'direct')

def logic_7687(agents, world):
    _agent_apply(world, agents, 'hydration', 'betrayal_memory', 'direct')

def logic_7688(agents, world):
    _agent_apply(world, agents, 'thirst', 'betrayal_memory', 'direct')

def logic_7689(agents, world):
    _agent_apply(world, agents, 'hunger', 'betrayal_memory', 'direct')

def logic_7690(agents, world):
    _agent_apply(world, agents, 'health', 'betrayal_memory', 'direct')

def logic_7691(agents, world):
    _agent_apply(world, agents, 'stress', 'betrayal_memory', 'direct')

def logic_7692(agents, world):
    _agent_apply(world, agents, 'risk_tolerance', 'betrayal_memory', 'direct')

def logic_7693(agents, world):
    _agent_apply(world, agents, 'competition_pressure', 'betrayal_memory', 'direct')

def logic_7694(agents, world):
    _agent_apply(world, agents, 'social_need', 'betrayal_memory', 'direct')

def logic_7695(agents, world):
    _agent_apply(world, agents, 'cooperation', 'betrayal_memory', 'direct')

def logic_7696(agents, world):
    _agent_apply(world, agents, 'defection', 'betrayal_memory', 'direct')

def logic_7697(agents, world):
    _agent_apply(world, agents, 'trust', 'betrayal_memory', 'direct')

def logic_7698(agents, world):
    _agent_apply(world, agents, 'reputation', 'betrayal_memory', 'direct')

def logic_7699(agents, world):
    _agent_apply(world, agents, 'help_received', 'betrayal_memory', 'direct')

def logic_7700(agents, world):
    _agent_apply(world, agents, 'help_given', 'betrayal_memory', 'direct')

def logic_7701(agents, world):
    _agent_apply(world, agents, 'local_density', 'betrayal_memory', 'direct')

def logic_7702(agents, world):
    _agent_apply(world, agents, 'strategy_score', 'betrayal_memory', 'direct')

def logic_7703(agents, world):
    _agent_apply(world, agents, 'survival_score', 'betrayal_memory', 'direct')

def logic_7704(agents, world):
    _agent_apply(world, agents, 'fitness_score', 'betrayal_memory', 'direct')

def logic_7705(agents, world):
    _agent_apply(world, agents, 'payoff', 'betrayal_memory', 'direct')
