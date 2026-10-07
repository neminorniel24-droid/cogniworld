import torch

RATE = 0.008


def _field(world, name):
    x = getattr(world, name, None)
    if x is None:
        return None
    return torch.nan_to_num(x).float()


def _local(world, agents, name):
    x = agents.pos[:, 0].long()
    y = agents.pos[:, 1].long()
    field = getattr(world, name, None)
    if field is None:
        return None
    return torch.nan_to_num(field[y, x]).to(dtype=agents.energy.dtype)


def _sigmoid(x):
    return torch.sigmoid(torch.nan_to_num(x))


def _mode(s, t, mode):
    if mode == "inverse": return 1 - s
    if mode == "square": return s * s
    if mode == "sqrt": return torch.sqrt(s.clamp_min(0))
    if mode == "pulse": return 4 * s * (1 - s)
    if mode == "threshold": return (s > 0.5).to(s.dtype)
    if mode == "saturation": return s / (0.25 + s)
    if mode == "reciprocal": return 1 / (1 + s)
    if mode == "gap": return torch.abs(s - t)
    if mode == "feedback": return s * t
    return s


def _world_apply(world, source, target, mode):
    s = _field(world, source)
    t = _field(world, target)
    if s is None or t is None:
        return
    s = _sigmoid(s)
    t = torch.nan_to_num(t)
    d = _mode(s, _sigmoid(t), mode)
    setattr(world, target, t + RATE * (d - t))


def _agent_source(world, agents, name):
    if hasattr(agents, name):
        return torch.nan_to_num(getattr(agents, name)).to(dtype=agents.energy.dtype)
    return _local(world, agents, name)


def _agent_apply(world, agents, source, target, mode):
    s = _agent_source(world, agents, source)
    if s is None or not hasattr(agents, target):
        return
    s = _sigmoid(s)
    raw = torch.nan_to_num(getattr(agents, target))
    t = _sigmoid(raw)
    d = _mode(s, t, mode)
    setattr(agents, target, torch.logit((t + RATE * (d - t)).clamp(1e-5, 1 - 1e-5)))

def logic_10001(world):
    _world_apply(world, 'temperature', 'surface_water', 'direct')

def logic_10002(world):
    _world_apply(world, 'temperature', 'humidity', 'square')

def logic_10003(world):
    _world_apply(world, 'temperature', 'cloud', 'pulse')

def logic_10004(world):
    _world_apply(world, 'temperature', 'rain', 'saturation')

def logic_10005(world):
    _world_apply(world, 'temperature', 'soil_moisture', 'gap')

def logic_10006(world):
    _world_apply(world, 'temperature', 'runoff', 'direct')

def logic_10007(world):
    _world_apply(world, 'temperature', 'wind_x', 'square')

def logic_10008(world):
    _world_apply(world, 'temperature', 'wind_y', 'pulse')

def logic_10009(world):
    _world_apply(world, 'temperature', 'vegetation', 'gap')

def logic_10010(world):
    _world_apply(world, 'temperature', 'biomass', 'direct')

def logic_10011(world):
    _world_apply(world, 'temperature', 'herbivore', 'square')

def logic_10012(world):
    _world_apply(world, 'temperature', 'predator', 'pulse')

def logic_10013(world):
    _world_apply(world, 'temperature', 'carrion', 'saturation')

def logic_10014(world):
    _world_apply(world, 'temperature', 'nutrients', 'gap')

def logic_10015(world):
    _world_apply(world, 'temperature', 'decomposition_rate', 'direct')

def logic_10016(world):
    _world_apply(world, 'temperature', 'oxygen', 'square')

def logic_10017(world):
    _world_apply(world, 'temperature', 'co2', 'saturation')

def logic_10018(world):
    _world_apply(world, 'temperature', 'photosynthesis_factor', 'gap')

def logic_10019(world):
    _world_apply(world, 'temperature', 'ice', 'direct')

def logic_10020(world):
    _world_apply(world, 'temperature', 'evaporation', 'square')

def logic_10021(world):
    _world_apply(world, 'temperature', 'detritus', 'pulse')

def logic_10022(world):
    _world_apply(world, 'temperature', 'methane', 'saturation')

def logic_10023(world):
    _world_apply(world, 'temperature', 'pathogen_load', 'gap')

def logic_10024(world):
    _world_apply(world, 'temperature', 'biodiversity', 'direct')

def logic_10025(world):
    _world_apply(world, 'temperature', 'habitat_stress', 'pulse')

def logic_10026(world):
    _world_apply(world, 'temperature', 'erosion', 'saturation')

def logic_10027(world):
    _world_apply(world, 'temperature', 'soil_depth', 'gap')

def logic_10028(world):
    _world_apply(world, 'temperature', 'root_density', 'direct')

def logic_10029(world):
    _world_apply(world, 'temperature', 'wetland', 'square')

def logic_10030(world):
    _world_apply(world, 'temperature', 'carbon_storage', 'pulse')

def logic_10031(world):
    _world_apply(world, 'temperature', 'fire_risk', 'saturation')

def logic_10032(world):
    _world_apply(world, 'temperature', 'ash', 'gap')

def logic_10033(world):
    _world_apply(world, 'temperature', 'snowpack', 'square')

def logic_10034(world):
    _world_apply(world, 'temperature', 'groundwater', 'pulse')

def logic_10035(world):
    _world_apply(world, 'temperature', 'sediment', 'saturation')

def logic_10036(world):
    _world_apply(world, 'temperature', 'salinity', 'gap')

def logic_10037(world):
    _world_apply(world, 'temperature', 'algae', 'direct')

def logic_10038(world):
    _world_apply(world, 'temperature', 'organic_matter', 'square')

def logic_10039(world):
    _world_apply(world, 'temperature', 'deadwood', 'pulse')

def logic_10040(world):
    _world_apply(world, 'temperature', 'pollinators', 'saturation')

def logic_10041(world):
    _world_apply(world, 'temperature', 'flowers', 'direct')

def logic_10042(world):
    _world_apply(world, 'temperature', 'seed_bank', 'square')

def logic_10043(world):
    _world_apply(world, 'temperature', 'soil_carbon', 'pulse')

def logic_10044(world):
    _world_apply(world, 'temperature', 'surface_ice', 'saturation')

def logic_10045(world):
    _world_apply(world, 'surface_water', 'temperature', 'gap')

def logic_10046(world):
    _world_apply(world, 'surface_water', 'humidity', 'direct')

def logic_10047(world):
    _world_apply(world, 'surface_water', 'cloud', 'square')

def logic_10048(world):
    _world_apply(world, 'surface_water', 'rain', 'pulse')

def logic_10049(world):
    _world_apply(world, 'surface_water', 'soil_moisture', 'gap')

def logic_10050(world):
    _world_apply(world, 'surface_water', 'runoff', 'direct')

def logic_10051(world):
    _world_apply(world, 'surface_water', 'wind_x', 'square')

def logic_10052(world):
    _world_apply(world, 'surface_water', 'wind_y', 'pulse')

def logic_10053(world):
    _world_apply(world, 'surface_water', 'vegetation', 'saturation')

def logic_10054(world):
    _world_apply(world, 'surface_water', 'biomass', 'gap')

def logic_10055(world):
    _world_apply(world, 'surface_water', 'herbivore', 'direct')

def logic_10056(world):
    _world_apply(world, 'surface_water', 'predator', 'square')

def logic_10057(world):
    _world_apply(world, 'surface_water', 'carrion', 'saturation')

def logic_10058(world):
    _world_apply(world, 'surface_water', 'nutrients', 'gap')

def logic_10059(world):
    _world_apply(world, 'surface_water', 'decomposition_rate', 'direct')

def logic_10060(world):
    _world_apply(world, 'surface_water', 'oxygen', 'square')

def logic_10061(world):
    _world_apply(world, 'surface_water', 'co2', 'pulse')

def logic_10062(world):
    _world_apply(world, 'surface_water', 'photosynthesis_factor', 'saturation')

def logic_10063(world):
    _world_apply(world, 'surface_water', 'ice', 'gap')

def logic_10064(world):
    _world_apply(world, 'surface_water', 'evaporation', 'direct')

def logic_10065(world):
    _world_apply(world, 'surface_water', 'detritus', 'pulse')

def logic_10066(world):
    _world_apply(world, 'surface_water', 'methane', 'saturation')

def logic_10067(world):
    _world_apply(world, 'surface_water', 'pathogen_load', 'gap')

def logic_10068(world):
    _world_apply(world, 'surface_water', 'biodiversity', 'direct')

def logic_10069(world):
    _world_apply(world, 'surface_water', 'habitat_stress', 'square')

def logic_10070(world):
    _world_apply(world, 'surface_water', 'erosion', 'pulse')

def logic_10071(world):
    _world_apply(world, 'surface_water', 'soil_depth', 'saturation')

def logic_10072(world):
    _world_apply(world, 'surface_water', 'root_density', 'gap')

def logic_10073(world):
    _world_apply(world, 'surface_water', 'wetland', 'square')

def logic_10074(world):
    _world_apply(world, 'surface_water', 'carbon_storage', 'pulse')

def logic_10075(world):
    _world_apply(world, 'surface_water', 'fire_risk', 'saturation')

def logic_10076(world):
    _world_apply(world, 'surface_water', 'ash', 'gap')

def logic_10077(world):
    _world_apply(world, 'surface_water', 'snowpack', 'direct')

def logic_10078(world):
    _world_apply(world, 'surface_water', 'groundwater', 'square')

def logic_10079(world):
    _world_apply(world, 'surface_water', 'sediment', 'pulse')

def logic_10080(world):
    _world_apply(world, 'surface_water', 'salinity', 'saturation')

def logic_10081(world):
    _world_apply(world, 'surface_water', 'algae', 'direct')

def logic_10082(world):
    _world_apply(world, 'surface_water', 'organic_matter', 'square')

def logic_10083(world):
    _world_apply(world, 'surface_water', 'deadwood', 'pulse')

def logic_10084(world):
    _world_apply(world, 'surface_water', 'pollinators', 'saturation')

def logic_10085(world):
    _world_apply(world, 'surface_water', 'flowers', 'gap')

def logic_10086(world):
    _world_apply(world, 'surface_water', 'seed_bank', 'direct')

def logic_10087(world):
    _world_apply(world, 'surface_water', 'soil_carbon', 'square')

def logic_10088(world):
    _world_apply(world, 'surface_water', 'surface_ice', 'pulse')

def logic_10089(world):
    _world_apply(world, 'humidity', 'temperature', 'gap')

def logic_10090(world):
    _world_apply(world, 'humidity', 'surface_water', 'direct')

def logic_10091(world):
    _world_apply(world, 'humidity', 'cloud', 'square')

def logic_10092(world):
    _world_apply(world, 'humidity', 'rain', 'pulse')

def logic_10093(world):
    _world_apply(world, 'humidity', 'soil_moisture', 'saturation')

def logic_10094(world):
    _world_apply(world, 'humidity', 'runoff', 'gap')

def logic_10095(world):
    _world_apply(world, 'humidity', 'wind_x', 'direct')

def logic_10096(world):
    _world_apply(world, 'humidity', 'wind_y', 'square')

def logic_10097(world):
    _world_apply(world, 'humidity', 'vegetation', 'saturation')

def logic_10098(world):
    _world_apply(world, 'humidity', 'biomass', 'gap')

def logic_10099(world):
    _world_apply(world, 'humidity', 'herbivore', 'direct')

def logic_10100(world):
    _world_apply(world, 'humidity', 'predator', 'square')

def logic_10101(world):
    _world_apply(world, 'humidity', 'carrion', 'pulse')

def logic_10102(world):
    _world_apply(world, 'humidity', 'nutrients', 'saturation')

def logic_10103(world):
    _world_apply(world, 'humidity', 'decomposition_rate', 'gap')

def logic_10104(world):
    _world_apply(world, 'humidity', 'oxygen', 'direct')

def logic_10105(world):
    _world_apply(world, 'humidity', 'co2', 'pulse')

def logic_10106(world):
    _world_apply(world, 'humidity', 'photosynthesis_factor', 'saturation')

def logic_10107(world):
    _world_apply(world, 'humidity', 'ice', 'gap')

def logic_10108(world):
    _world_apply(world, 'humidity', 'evaporation', 'direct')

def logic_10109(world):
    _world_apply(world, 'humidity', 'detritus', 'square')

def logic_10110(world):
    _world_apply(world, 'humidity', 'methane', 'pulse')

def logic_10111(world):
    _world_apply(world, 'humidity', 'pathogen_load', 'saturation')

def logic_10112(world):
    _world_apply(world, 'humidity', 'biodiversity', 'gap')

def logic_10113(world):
    _world_apply(world, 'humidity', 'habitat_stress', 'square')

def logic_10114(world):
    _world_apply(world, 'humidity', 'erosion', 'pulse')

def logic_10115(world):
    _world_apply(world, 'humidity', 'soil_depth', 'saturation')

def logic_10116(world):
    _world_apply(world, 'humidity', 'root_density', 'gap')
