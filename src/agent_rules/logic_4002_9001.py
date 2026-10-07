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
