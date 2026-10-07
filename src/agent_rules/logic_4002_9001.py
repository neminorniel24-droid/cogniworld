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
