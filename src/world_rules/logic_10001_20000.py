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

def logic_10117(world):
    _world_apply(world, 'humidity', 'wetland', 'direct')

def logic_10118(world):
    _world_apply(world, 'humidity', 'carbon_storage', 'square')

def logic_10119(world):
    _world_apply(world, 'humidity', 'fire_risk', 'pulse')

def logic_10120(world):
    _world_apply(world, 'humidity', 'ash', 'saturation')

def logic_10121(world):
    _world_apply(world, 'humidity', 'snowpack', 'direct')

def logic_10122(world):
    _world_apply(world, 'humidity', 'groundwater', 'square')

def logic_10123(world):
    _world_apply(world, 'humidity', 'sediment', 'pulse')

def logic_10124(world):
    _world_apply(world, 'humidity', 'salinity', 'saturation')

def logic_10125(world):
    _world_apply(world, 'humidity', 'algae', 'gap')

def logic_10126(world):
    _world_apply(world, 'humidity', 'organic_matter', 'direct')

def logic_10127(world):
    _world_apply(world, 'humidity', 'deadwood', 'square')

def logic_10128(world):
    _world_apply(world, 'humidity', 'pollinators', 'pulse')

def logic_10129(world):
    _world_apply(world, 'humidity', 'flowers', 'gap')

def logic_10130(world):
    _world_apply(world, 'humidity', 'seed_bank', 'direct')

def logic_10131(world):
    _world_apply(world, 'humidity', 'soil_carbon', 'square')

def logic_10132(world):
    _world_apply(world, 'humidity', 'surface_ice', 'pulse')

def logic_10133(world):
    _world_apply(world, 'cloud', 'temperature', 'saturation')

def logic_10134(world):
    _world_apply(world, 'cloud', 'surface_water', 'gap')

def logic_10135(world):
    _world_apply(world, 'cloud', 'humidity', 'direct')

def logic_10136(world):
    _world_apply(world, 'cloud', 'rain', 'square')

def logic_10137(world):
    _world_apply(world, 'cloud', 'soil_moisture', 'saturation')

def logic_10138(world):
    _world_apply(world, 'cloud', 'runoff', 'gap')

def logic_10139(world):
    _world_apply(world, 'cloud', 'wind_x', 'direct')

def logic_10140(world):
    _world_apply(world, 'cloud', 'wind_y', 'square')

def logic_10141(world):
    _world_apply(world, 'cloud', 'vegetation', 'pulse')

def logic_10142(world):
    _world_apply(world, 'cloud', 'biomass', 'saturation')

def logic_10143(world):
    _world_apply(world, 'cloud', 'herbivore', 'gap')

def logic_10144(world):
    _world_apply(world, 'cloud', 'predator', 'direct')

def logic_10145(world):
    _world_apply(world, 'cloud', 'carrion', 'pulse')

def logic_10146(world):
    _world_apply(world, 'cloud', 'nutrients', 'saturation')

def logic_10147(world):
    _world_apply(world, 'cloud', 'decomposition_rate', 'gap')

def logic_10148(world):
    _world_apply(world, 'cloud', 'oxygen', 'direct')

def logic_10149(world):
    _world_apply(world, 'cloud', 'co2', 'square')

def logic_10150(world):
    _world_apply(world, 'cloud', 'photosynthesis_factor', 'pulse')

def logic_10151(world):
    _world_apply(world, 'cloud', 'ice', 'saturation')

def logic_10152(world):
    _world_apply(world, 'cloud', 'evaporation', 'gap')

def logic_10153(world):
    _world_apply(world, 'cloud', 'detritus', 'square')

def logic_10154(world):
    _world_apply(world, 'cloud', 'methane', 'pulse')

def logic_10155(world):
    _world_apply(world, 'cloud', 'pathogen_load', 'saturation')

def logic_10156(world):
    _world_apply(world, 'cloud', 'biodiversity', 'gap')

def logic_10157(world):
    _world_apply(world, 'cloud', 'habitat_stress', 'direct')

def logic_10158(world):
    _world_apply(world, 'cloud', 'erosion', 'square')

def logic_10159(world):
    _world_apply(world, 'cloud', 'soil_depth', 'pulse')

def logic_10160(world):
    _world_apply(world, 'cloud', 'root_density', 'saturation')

def logic_10161(world):
    _world_apply(world, 'cloud', 'wetland', 'direct')

def logic_10162(world):
    _world_apply(world, 'cloud', 'carbon_storage', 'square')

def logic_10163(world):
    _world_apply(world, 'cloud', 'fire_risk', 'pulse')

def logic_10164(world):
    _world_apply(world, 'cloud', 'ash', 'saturation')

def logic_10165(world):
    _world_apply(world, 'cloud', 'snowpack', 'gap')

def logic_10166(world):
    _world_apply(world, 'cloud', 'groundwater', 'direct')

def logic_10167(world):
    _world_apply(world, 'cloud', 'sediment', 'square')

def logic_10168(world):
    _world_apply(world, 'cloud', 'salinity', 'pulse')

def logic_10169(world):
    _world_apply(world, 'cloud', 'algae', 'gap')

def logic_10170(world):
    _world_apply(world, 'cloud', 'organic_matter', 'direct')

def logic_10171(world):
    _world_apply(world, 'cloud', 'deadwood', 'square')

def logic_10172(world):
    _world_apply(world, 'cloud', 'pollinators', 'pulse')

def logic_10173(world):
    _world_apply(world, 'cloud', 'flowers', 'saturation')

def logic_10174(world):
    _world_apply(world, 'cloud', 'seed_bank', 'gap')

def logic_10175(world):
    _world_apply(world, 'cloud', 'soil_carbon', 'direct')

def logic_10176(world):
    _world_apply(world, 'cloud', 'surface_ice', 'square')

def logic_10177(world):
    _world_apply(world, 'rain', 'temperature', 'saturation')

def logic_10178(world):
    _world_apply(world, 'rain', 'surface_water', 'gap')

def logic_10179(world):
    _world_apply(world, 'rain', 'humidity', 'direct')

def logic_10180(world):
    _world_apply(world, 'rain', 'cloud', 'square')

def logic_10181(world):
    _world_apply(world, 'rain', 'soil_moisture', 'pulse')

def logic_10182(world):
    _world_apply(world, 'rain', 'runoff', 'saturation')

def logic_10183(world):
    _world_apply(world, 'rain', 'wind_x', 'gap')

def logic_10184(world):
    _world_apply(world, 'rain', 'wind_y', 'direct')

def logic_10185(world):
    _world_apply(world, 'rain', 'vegetation', 'pulse')

def logic_10186(world):
    _world_apply(world, 'rain', 'biomass', 'saturation')

def logic_10187(world):
    _world_apply(world, 'rain', 'herbivore', 'gap')

def logic_10188(world):
    _world_apply(world, 'rain', 'predator', 'direct')

def logic_10189(world):
    _world_apply(world, 'rain', 'carrion', 'square')

def logic_10190(world):
    _world_apply(world, 'rain', 'nutrients', 'pulse')

def logic_10191(world):
    _world_apply(world, 'rain', 'decomposition_rate', 'saturation')

def logic_10192(world):
    _world_apply(world, 'rain', 'oxygen', 'gap')

def logic_10193(world):
    _world_apply(world, 'rain', 'co2', 'square')

def logic_10194(world):
    _world_apply(world, 'rain', 'photosynthesis_factor', 'pulse')

def logic_10195(world):
    _world_apply(world, 'rain', 'ice', 'saturation')

def logic_10196(world):
    _world_apply(world, 'rain', 'evaporation', 'gap')

def logic_10197(world):
    _world_apply(world, 'rain', 'detritus', 'direct')

def logic_10198(world):
    _world_apply(world, 'rain', 'methane', 'square')

def logic_10199(world):
    _world_apply(world, 'rain', 'pathogen_load', 'pulse')

def logic_10200(world):
    _world_apply(world, 'rain', 'biodiversity', 'saturation')

def logic_10201(world):
    _world_apply(world, 'rain', 'habitat_stress', 'direct')

def logic_10202(world):
    _world_apply(world, 'rain', 'erosion', 'square')

def logic_10203(world):
    _world_apply(world, 'rain', 'soil_depth', 'pulse')

def logic_10204(world):
    _world_apply(world, 'rain', 'root_density', 'saturation')

def logic_10205(world):
    _world_apply(world, 'rain', 'wetland', 'gap')

def logic_10206(world):
    _world_apply(world, 'rain', 'carbon_storage', 'direct')

def logic_10207(world):
    _world_apply(world, 'rain', 'fire_risk', 'square')

def logic_10208(world):
    _world_apply(world, 'rain', 'ash', 'pulse')

def logic_10209(world):
    _world_apply(world, 'rain', 'snowpack', 'gap')

def logic_10210(world):
    _world_apply(world, 'rain', 'groundwater', 'direct')

def logic_10211(world):
    _world_apply(world, 'rain', 'sediment', 'square')

def logic_10212(world):
    _world_apply(world, 'rain', 'salinity', 'pulse')

def logic_10213(world):
    _world_apply(world, 'rain', 'algae', 'saturation')

def logic_10214(world):
    _world_apply(world, 'rain', 'organic_matter', 'gap')

def logic_10215(world):
    _world_apply(world, 'rain', 'deadwood', 'direct')

def logic_10216(world):
    _world_apply(world, 'rain', 'pollinators', 'square')

def logic_10217(world):
    _world_apply(world, 'rain', 'flowers', 'saturation')

def logic_10218(world):
    _world_apply(world, 'rain', 'seed_bank', 'gap')

def logic_10219(world):
    _world_apply(world, 'rain', 'soil_carbon', 'direct')

def logic_10220(world):
    _world_apply(world, 'rain', 'surface_ice', 'square')

def logic_10221(world):
    _world_apply(world, 'soil_moisture', 'temperature', 'pulse')

def logic_10222(world):
    _world_apply(world, 'soil_moisture', 'surface_water', 'saturation')

def logic_10223(world):
    _world_apply(world, 'soil_moisture', 'humidity', 'gap')

def logic_10224(world):
    _world_apply(world, 'soil_moisture', 'cloud', 'direct')

def logic_10225(world):
    _world_apply(world, 'soil_moisture', 'rain', 'pulse')

def logic_10226(world):
    _world_apply(world, 'soil_moisture', 'runoff', 'saturation')

def logic_10227(world):
    _world_apply(world, 'soil_moisture', 'wind_x', 'gap')

def logic_10228(world):
    _world_apply(world, 'soil_moisture', 'wind_y', 'direct')

def logic_10229(world):
    _world_apply(world, 'soil_moisture', 'vegetation', 'square')

def logic_10230(world):
    _world_apply(world, 'soil_moisture', 'biomass', 'pulse')

def logic_10231(world):
    _world_apply(world, 'soil_moisture', 'herbivore', 'saturation')

def logic_10232(world):
    _world_apply(world, 'soil_moisture', 'predator', 'gap')

def logic_10233(world):
    _world_apply(world, 'soil_moisture', 'carrion', 'square')

def logic_10234(world):
    _world_apply(world, 'soil_moisture', 'nutrients', 'pulse')

def logic_10235(world):
    _world_apply(world, 'soil_moisture', 'decomposition_rate', 'saturation')

def logic_10236(world):
    _world_apply(world, 'soil_moisture', 'oxygen', 'gap')

def logic_10237(world):
    _world_apply(world, 'soil_moisture', 'co2', 'direct')

def logic_10238(world):
    _world_apply(world, 'soil_moisture', 'photosynthesis_factor', 'square')

def logic_10239(world):
    _world_apply(world, 'soil_moisture', 'ice', 'pulse')

def logic_10240(world):
    _world_apply(world, 'soil_moisture', 'evaporation', 'saturation')

def logic_10241(world):
    _world_apply(world, 'soil_moisture', 'detritus', 'direct')

def logic_10242(world):
    _world_apply(world, 'soil_moisture', 'methane', 'square')

def logic_10243(world):
    _world_apply(world, 'soil_moisture', 'pathogen_load', 'pulse')

def logic_10244(world):
    _world_apply(world, 'soil_moisture', 'biodiversity', 'saturation')

def logic_10245(world):
    _world_apply(world, 'soil_moisture', 'habitat_stress', 'gap')

def logic_10246(world):
    _world_apply(world, 'soil_moisture', 'erosion', 'direct')

def logic_10247(world):
    _world_apply(world, 'soil_moisture', 'soil_depth', 'square')

def logic_10248(world):
    _world_apply(world, 'soil_moisture', 'root_density', 'pulse')

def logic_10249(world):
    _world_apply(world, 'soil_moisture', 'wetland', 'gap')

def logic_10250(world):
    _world_apply(world, 'soil_moisture', 'carbon_storage', 'direct')

def logic_10251(world):
    _world_apply(world, 'soil_moisture', 'fire_risk', 'square')

def logic_10252(world):
    _world_apply(world, 'soil_moisture', 'ash', 'pulse')

def logic_10253(world):
    _world_apply(world, 'soil_moisture', 'snowpack', 'saturation')

def logic_10254(world):
    _world_apply(world, 'soil_moisture', 'groundwater', 'gap')

def logic_10255(world):
    _world_apply(world, 'soil_moisture', 'sediment', 'direct')

def logic_10256(world):
    _world_apply(world, 'soil_moisture', 'salinity', 'square')

def logic_10257(world):
    _world_apply(world, 'soil_moisture', 'algae', 'saturation')

def logic_10258(world):
    _world_apply(world, 'soil_moisture', 'organic_matter', 'gap')

def logic_10259(world):
    _world_apply(world, 'soil_moisture', 'deadwood', 'direct')

def logic_10260(world):
    _world_apply(world, 'soil_moisture', 'pollinators', 'square')

def logic_10261(world):
    _world_apply(world, 'soil_moisture', 'flowers', 'pulse')

def logic_10262(world):
    _world_apply(world, 'soil_moisture', 'seed_bank', 'saturation')

def logic_10263(world):
    _world_apply(world, 'soil_moisture', 'soil_carbon', 'gap')

def logic_10264(world):
    _world_apply(world, 'soil_moisture', 'surface_ice', 'direct')

def logic_10265(world):
    _world_apply(world, 'runoff', 'temperature', 'pulse')

def logic_10266(world):
    _world_apply(world, 'runoff', 'surface_water', 'saturation')

def logic_10267(world):
    _world_apply(world, 'runoff', 'humidity', 'gap')

def logic_10268(world):
    _world_apply(world, 'runoff', 'cloud', 'direct')

def logic_10269(world):
    _world_apply(world, 'runoff', 'rain', 'square')

def logic_10270(world):
    _world_apply(world, 'runoff', 'soil_moisture', 'pulse')

def logic_10271(world):
    _world_apply(world, 'runoff', 'wind_x', 'saturation')

def logic_10272(world):
    _world_apply(world, 'runoff', 'wind_y', 'gap')

def logic_10273(world):
    _world_apply(world, 'runoff', 'vegetation', 'square')

def logic_10274(world):
    _world_apply(world, 'runoff', 'biomass', 'pulse')

def logic_10275(world):
    _world_apply(world, 'runoff', 'herbivore', 'saturation')

def logic_10276(world):
    _world_apply(world, 'runoff', 'predator', 'gap')

def logic_10277(world):
    _world_apply(world, 'runoff', 'carrion', 'direct')

def logic_10278(world):
    _world_apply(world, 'runoff', 'nutrients', 'square')

def logic_10279(world):
    _world_apply(world, 'runoff', 'decomposition_rate', 'pulse')

def logic_10280(world):
    _world_apply(world, 'runoff', 'oxygen', 'saturation')

def logic_10281(world):
    _world_apply(world, 'runoff', 'co2', 'direct')

def logic_10282(world):
    _world_apply(world, 'runoff', 'photosynthesis_factor', 'square')

def logic_10283(world):
    _world_apply(world, 'runoff', 'ice', 'pulse')

def logic_10284(world):
    _world_apply(world, 'runoff', 'evaporation', 'saturation')

def logic_10285(world):
    _world_apply(world, 'runoff', 'detritus', 'gap')

def logic_10286(world):
    _world_apply(world, 'runoff', 'methane', 'direct')

def logic_10287(world):
    _world_apply(world, 'runoff', 'pathogen_load', 'square')

def logic_10288(world):
    _world_apply(world, 'runoff', 'biodiversity', 'pulse')

def logic_10289(world):
    _world_apply(world, 'runoff', 'habitat_stress', 'gap')

def logic_10290(world):
    _world_apply(world, 'runoff', 'erosion', 'direct')

def logic_10291(world):
    _world_apply(world, 'runoff', 'soil_depth', 'square')

def logic_10292(world):
    _world_apply(world, 'runoff', 'root_density', 'pulse')

def logic_10293(world):
    _world_apply(world, 'runoff', 'wetland', 'saturation')

def logic_10294(world):
    _world_apply(world, 'runoff', 'carbon_storage', 'gap')

def logic_10295(world):
    _world_apply(world, 'runoff', 'fire_risk', 'direct')

def logic_10296(world):
    _world_apply(world, 'runoff', 'ash', 'square')

def logic_10297(world):
    _world_apply(world, 'runoff', 'snowpack', 'saturation')

def logic_10298(world):
    _world_apply(world, 'runoff', 'groundwater', 'gap')

def logic_10299(world):
    _world_apply(world, 'runoff', 'sediment', 'direct')

def logic_10300(world):
    _world_apply(world, 'runoff', 'salinity', 'square')

def logic_10301(world):
    _world_apply(world, 'runoff', 'algae', 'pulse')

def logic_10302(world):
    _world_apply(world, 'runoff', 'organic_matter', 'saturation')

def logic_10303(world):
    _world_apply(world, 'runoff', 'deadwood', 'gap')

def logic_10304(world):
    _world_apply(world, 'runoff', 'pollinators', 'direct')

def logic_10305(world):
    _world_apply(world, 'runoff', 'flowers', 'pulse')

def logic_10306(world):
    _world_apply(world, 'runoff', 'seed_bank', 'saturation')

def logic_10307(world):
    _world_apply(world, 'runoff', 'soil_carbon', 'gap')

def logic_10308(world):
    _world_apply(world, 'runoff', 'surface_ice', 'direct')

def logic_10309(world):
    _world_apply(world, 'wind_x', 'temperature', 'square')

def logic_10310(world):
    _world_apply(world, 'wind_x', 'surface_water', 'pulse')

def logic_10311(world):
    _world_apply(world, 'wind_x', 'humidity', 'saturation')

def logic_10312(world):
    _world_apply(world, 'wind_x', 'cloud', 'gap')

def logic_10313(world):
    _world_apply(world, 'wind_x', 'rain', 'square')

def logic_10314(world):
    _world_apply(world, 'wind_x', 'soil_moisture', 'pulse')

def logic_10315(world):
    _world_apply(world, 'wind_x', 'runoff', 'saturation')

def logic_10316(world):
    _world_apply(world, 'wind_x', 'wind_y', 'gap')

def logic_10317(world):
    _world_apply(world, 'wind_x', 'vegetation', 'direct')

def logic_10318(world):
    _world_apply(world, 'wind_x', 'biomass', 'square')

def logic_10319(world):
    _world_apply(world, 'wind_x', 'herbivore', 'pulse')

def logic_10320(world):
    _world_apply(world, 'wind_x', 'predator', 'saturation')

def logic_10321(world):
    _world_apply(world, 'wind_x', 'carrion', 'direct')

def logic_10322(world):
    _world_apply(world, 'wind_x', 'nutrients', 'square')

def logic_10323(world):
    _world_apply(world, 'wind_x', 'decomposition_rate', 'pulse')

def logic_10324(world):
    _world_apply(world, 'wind_x', 'oxygen', 'saturation')

def logic_10325(world):
    _world_apply(world, 'wind_x', 'co2', 'gap')

def logic_10326(world):
    _world_apply(world, 'wind_x', 'photosynthesis_factor', 'direct')

def logic_10327(world):
    _world_apply(world, 'wind_x', 'ice', 'square')

def logic_10328(world):
    _world_apply(world, 'wind_x', 'evaporation', 'pulse')

def logic_10329(world):
    _world_apply(world, 'wind_x', 'detritus', 'gap')

def logic_10330(world):
    _world_apply(world, 'wind_x', 'methane', 'direct')

def logic_10331(world):
    _world_apply(world, 'wind_x', 'pathogen_load', 'square')

def logic_10332(world):
    _world_apply(world, 'wind_x', 'biodiversity', 'pulse')

def logic_10333(world):
    _world_apply(world, 'wind_x', 'habitat_stress', 'saturation')

def logic_10334(world):
    _world_apply(world, 'wind_x', 'erosion', 'gap')

def logic_10335(world):
    _world_apply(world, 'wind_x', 'soil_depth', 'direct')

def logic_10336(world):
    _world_apply(world, 'wind_x', 'root_density', 'square')

def logic_10337(world):
    _world_apply(world, 'wind_x', 'wetland', 'saturation')

def logic_10338(world):
    _world_apply(world, 'wind_x', 'carbon_storage', 'gap')

def logic_10339(world):
    _world_apply(world, 'wind_x', 'fire_risk', 'direct')

def logic_10340(world):
    _world_apply(world, 'wind_x', 'ash', 'square')

def logic_10341(world):
    _world_apply(world, 'wind_x', 'snowpack', 'pulse')

def logic_10342(world):
    _world_apply(world, 'wind_x', 'groundwater', 'saturation')

def logic_10343(world):
    _world_apply(world, 'wind_x', 'sediment', 'gap')

def logic_10344(world):
    _world_apply(world, 'wind_x', 'salinity', 'direct')

def logic_10345(world):
    _world_apply(world, 'wind_x', 'algae', 'pulse')

def logic_10346(world):
    _world_apply(world, 'wind_x', 'organic_matter', 'saturation')

def logic_10347(world):
    _world_apply(world, 'wind_x', 'deadwood', 'gap')

def logic_10348(world):
    _world_apply(world, 'wind_x', 'pollinators', 'direct')

def logic_10349(world):
    _world_apply(world, 'wind_x', 'flowers', 'square')

def logic_10350(world):
    _world_apply(world, 'wind_x', 'seed_bank', 'pulse')

def logic_10351(world):
    _world_apply(world, 'wind_x', 'soil_carbon', 'saturation')

def logic_10352(world):
    _world_apply(world, 'wind_x', 'surface_ice', 'gap')

def logic_10353(world):
    _world_apply(world, 'wind_y', 'temperature', 'square')

def logic_10354(world):
    _world_apply(world, 'wind_y', 'surface_water', 'pulse')

def logic_10355(world):
    _world_apply(world, 'wind_y', 'humidity', 'saturation')
