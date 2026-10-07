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

def logic_10356(world):
    _world_apply(world, 'wind_y', 'cloud', 'gap')

def logic_10357(world):
    _world_apply(world, 'wind_y', 'rain', 'direct')

def logic_10358(world):
    _world_apply(world, 'wind_y', 'soil_moisture', 'square')

def logic_10359(world):
    _world_apply(world, 'wind_y', 'runoff', 'pulse')

def logic_10360(world):
    _world_apply(world, 'wind_y', 'wind_x', 'saturation')

def logic_10361(world):
    _world_apply(world, 'wind_y', 'vegetation', 'direct')

def logic_10362(world):
    _world_apply(world, 'wind_y', 'biomass', 'square')

def logic_10363(world):
    _world_apply(world, 'wind_y', 'herbivore', 'pulse')

def logic_10364(world):
    _world_apply(world, 'wind_y', 'predator', 'saturation')

def logic_10365(world):
    _world_apply(world, 'wind_y', 'carrion', 'gap')

def logic_10366(world):
    _world_apply(world, 'wind_y', 'nutrients', 'direct')

def logic_10367(world):
    _world_apply(world, 'wind_y', 'decomposition_rate', 'square')

def logic_10368(world):
    _world_apply(world, 'wind_y', 'oxygen', 'pulse')

def logic_10369(world):
    _world_apply(world, 'wind_y', 'co2', 'gap')

def logic_10370(world):
    _world_apply(world, 'wind_y', 'photosynthesis_factor', 'direct')

def logic_10371(world):
    _world_apply(world, 'wind_y', 'ice', 'square')

def logic_10372(world):
    _world_apply(world, 'wind_y', 'evaporation', 'pulse')

def logic_10373(world):
    _world_apply(world, 'wind_y', 'detritus', 'saturation')

def logic_10374(world):
    _world_apply(world, 'wind_y', 'methane', 'gap')

def logic_10375(world):
    _world_apply(world, 'wind_y', 'pathogen_load', 'direct')

def logic_10376(world):
    _world_apply(world, 'wind_y', 'biodiversity', 'square')

def logic_10377(world):
    _world_apply(world, 'wind_y', 'habitat_stress', 'saturation')

def logic_10378(world):
    _world_apply(world, 'wind_y', 'erosion', 'gap')

def logic_10379(world):
    _world_apply(world, 'wind_y', 'soil_depth', 'direct')

def logic_10380(world):
    _world_apply(world, 'wind_y', 'root_density', 'square')

def logic_10381(world):
    _world_apply(world, 'wind_y', 'wetland', 'pulse')

def logic_10382(world):
    _world_apply(world, 'wind_y', 'carbon_storage', 'saturation')

def logic_10383(world):
    _world_apply(world, 'wind_y', 'fire_risk', 'gap')

def logic_10384(world):
    _world_apply(world, 'wind_y', 'ash', 'direct')

def logic_10385(world):
    _world_apply(world, 'wind_y', 'snowpack', 'pulse')

def logic_10386(world):
    _world_apply(world, 'wind_y', 'groundwater', 'saturation')

def logic_10387(world):
    _world_apply(world, 'wind_y', 'sediment', 'gap')

def logic_10388(world):
    _world_apply(world, 'wind_y', 'salinity', 'direct')

def logic_10389(world):
    _world_apply(world, 'wind_y', 'algae', 'square')

def logic_10390(world):
    _world_apply(world, 'wind_y', 'organic_matter', 'pulse')

def logic_10391(world):
    _world_apply(world, 'wind_y', 'deadwood', 'saturation')

def logic_10392(world):
    _world_apply(world, 'wind_y', 'pollinators', 'gap')

def logic_10393(world):
    _world_apply(world, 'wind_y', 'flowers', 'square')

def logic_10394(world):
    _world_apply(world, 'wind_y', 'seed_bank', 'pulse')

def logic_10395(world):
    _world_apply(world, 'wind_y', 'soil_carbon', 'saturation')

def logic_10396(world):
    _world_apply(world, 'wind_y', 'surface_ice', 'gap')

def logic_10397(world):
    _world_apply(world, 'vegetation', 'temperature', 'direct')

def logic_10398(world):
    _world_apply(world, 'vegetation', 'surface_water', 'square')

def logic_10399(world):
    _world_apply(world, 'vegetation', 'humidity', 'pulse')

def logic_10400(world):
    _world_apply(world, 'vegetation', 'cloud', 'saturation')

def logic_10401(world):
    _world_apply(world, 'vegetation', 'rain', 'direct')

def logic_10402(world):
    _world_apply(world, 'vegetation', 'soil_moisture', 'square')

def logic_10403(world):
    _world_apply(world, 'vegetation', 'runoff', 'pulse')

def logic_10404(world):
    _world_apply(world, 'vegetation', 'wind_x', 'saturation')

def logic_10405(world):
    _world_apply(world, 'vegetation', 'wind_y', 'gap')

def logic_10406(world):
    _world_apply(world, 'vegetation', 'biomass', 'direct')

def logic_10407(world):
    _world_apply(world, 'vegetation', 'herbivore', 'square')

def logic_10408(world):
    _world_apply(world, 'vegetation', 'predator', 'pulse')

def logic_10409(world):
    _world_apply(world, 'vegetation', 'carrion', 'gap')

def logic_10410(world):
    _world_apply(world, 'vegetation', 'nutrients', 'direct')

def logic_10411(world):
    _world_apply(world, 'vegetation', 'decomposition_rate', 'square')

def logic_10412(world):
    _world_apply(world, 'vegetation', 'oxygen', 'pulse')

def logic_10413(world):
    _world_apply(world, 'vegetation', 'co2', 'saturation')

def logic_10414(world):
    _world_apply(world, 'vegetation', 'photosynthesis_factor', 'gap')

def logic_10415(world):
    _world_apply(world, 'vegetation', 'ice', 'direct')

def logic_10416(world):
    _world_apply(world, 'vegetation', 'evaporation', 'square')

def logic_10417(world):
    _world_apply(world, 'vegetation', 'detritus', 'saturation')

def logic_10418(world):
    _world_apply(world, 'vegetation', 'methane', 'gap')

def logic_10419(world):
    _world_apply(world, 'vegetation', 'pathogen_load', 'direct')

def logic_10420(world):
    _world_apply(world, 'vegetation', 'biodiversity', 'square')

def logic_10421(world):
    _world_apply(world, 'vegetation', 'habitat_stress', 'pulse')

def logic_10422(world):
    _world_apply(world, 'vegetation', 'erosion', 'saturation')

def logic_10423(world):
    _world_apply(world, 'vegetation', 'soil_depth', 'gap')

def logic_10424(world):
    _world_apply(world, 'vegetation', 'root_density', 'direct')

def logic_10425(world):
    _world_apply(world, 'vegetation', 'wetland', 'pulse')

def logic_10426(world):
    _world_apply(world, 'vegetation', 'carbon_storage', 'saturation')

def logic_10427(world):
    _world_apply(world, 'vegetation', 'fire_risk', 'gap')

def logic_10428(world):
    _world_apply(world, 'vegetation', 'ash', 'direct')

def logic_10429(world):
    _world_apply(world, 'vegetation', 'snowpack', 'square')

def logic_10430(world):
    _world_apply(world, 'vegetation', 'groundwater', 'pulse')

def logic_10431(world):
    _world_apply(world, 'vegetation', 'sediment', 'saturation')

def logic_10432(world):
    _world_apply(world, 'vegetation', 'salinity', 'gap')

def logic_10433(world):
    _world_apply(world, 'vegetation', 'algae', 'square')

def logic_10434(world):
    _world_apply(world, 'vegetation', 'organic_matter', 'pulse')

def logic_10435(world):
    _world_apply(world, 'vegetation', 'deadwood', 'saturation')

def logic_10436(world):
    _world_apply(world, 'vegetation', 'pollinators', 'gap')

def logic_10437(world):
    _world_apply(world, 'vegetation', 'flowers', 'direct')

def logic_10438(world):
    _world_apply(world, 'vegetation', 'seed_bank', 'square')

def logic_10439(world):
    _world_apply(world, 'vegetation', 'soil_carbon', 'pulse')

def logic_10440(world):
    _world_apply(world, 'vegetation', 'surface_ice', 'saturation')

def logic_10441(world):
    _world_apply(world, 'biomass', 'temperature', 'direct')

def logic_10442(world):
    _world_apply(world, 'biomass', 'surface_water', 'square')

def logic_10443(world):
    _world_apply(world, 'biomass', 'humidity', 'pulse')

def logic_10444(world):
    _world_apply(world, 'biomass', 'cloud', 'saturation')

def logic_10445(world):
    _world_apply(world, 'biomass', 'rain', 'gap')

def logic_10446(world):
    _world_apply(world, 'biomass', 'soil_moisture', 'direct')

def logic_10447(world):
    _world_apply(world, 'biomass', 'runoff', 'square')

def logic_10448(world):
    _world_apply(world, 'biomass', 'wind_x', 'pulse')

def logic_10449(world):
    _world_apply(world, 'biomass', 'wind_y', 'gap')

def logic_10450(world):
    _world_apply(world, 'biomass', 'vegetation', 'direct')

def logic_10451(world):
    _world_apply(world, 'biomass', 'herbivore', 'square')

def logic_10452(world):
    _world_apply(world, 'biomass', 'predator', 'pulse')

def logic_10453(world):
    _world_apply(world, 'biomass', 'carrion', 'saturation')

def logic_10454(world):
    _world_apply(world, 'biomass', 'nutrients', 'gap')

def logic_10455(world):
    _world_apply(world, 'biomass', 'decomposition_rate', 'direct')

def logic_10456(world):
    _world_apply(world, 'biomass', 'oxygen', 'square')

def logic_10457(world):
    _world_apply(world, 'biomass', 'co2', 'saturation')

def logic_10458(world):
    _world_apply(world, 'biomass', 'photosynthesis_factor', 'gap')

def logic_10459(world):
    _world_apply(world, 'biomass', 'ice', 'direct')

def logic_10460(world):
    _world_apply(world, 'biomass', 'evaporation', 'square')

def logic_10461(world):
    _world_apply(world, 'biomass', 'detritus', 'pulse')

def logic_10462(world):
    _world_apply(world, 'biomass', 'methane', 'saturation')

def logic_10463(world):
    _world_apply(world, 'biomass', 'pathogen_load', 'gap')

def logic_10464(world):
    _world_apply(world, 'biomass', 'biodiversity', 'direct')

def logic_10465(world):
    _world_apply(world, 'biomass', 'habitat_stress', 'pulse')

def logic_10466(world):
    _world_apply(world, 'biomass', 'erosion', 'saturation')

def logic_10467(world):
    _world_apply(world, 'biomass', 'soil_depth', 'gap')

def logic_10468(world):
    _world_apply(world, 'biomass', 'root_density', 'direct')

def logic_10469(world):
    _world_apply(world, 'biomass', 'wetland', 'square')

def logic_10470(world):
    _world_apply(world, 'biomass', 'carbon_storage', 'pulse')

def logic_10471(world):
    _world_apply(world, 'biomass', 'fire_risk', 'saturation')

def logic_10472(world):
    _world_apply(world, 'biomass', 'ash', 'gap')

def logic_10473(world):
    _world_apply(world, 'biomass', 'snowpack', 'square')

def logic_10474(world):
    _world_apply(world, 'biomass', 'groundwater', 'pulse')

def logic_10475(world):
    _world_apply(world, 'biomass', 'sediment', 'saturation')

def logic_10476(world):
    _world_apply(world, 'biomass', 'salinity', 'gap')

def logic_10477(world):
    _world_apply(world, 'biomass', 'algae', 'direct')

def logic_10478(world):
    _world_apply(world, 'biomass', 'organic_matter', 'square')

def logic_10479(world):
    _world_apply(world, 'biomass', 'deadwood', 'pulse')

def logic_10480(world):
    _world_apply(world, 'biomass', 'pollinators', 'saturation')

def logic_10481(world):
    _world_apply(world, 'biomass', 'flowers', 'direct')

def logic_10482(world):
    _world_apply(world, 'biomass', 'seed_bank', 'square')

def logic_10483(world):
    _world_apply(world, 'biomass', 'soil_carbon', 'pulse')

def logic_10484(world):
    _world_apply(world, 'biomass', 'surface_ice', 'saturation')

def logic_10485(world):
    _world_apply(world, 'herbivore', 'temperature', 'gap')

def logic_10486(world):
    _world_apply(world, 'herbivore', 'surface_water', 'direct')

def logic_10487(world):
    _world_apply(world, 'herbivore', 'humidity', 'square')

def logic_10488(world):
    _world_apply(world, 'herbivore', 'cloud', 'pulse')

def logic_10489(world):
    _world_apply(world, 'herbivore', 'rain', 'gap')

def logic_10490(world):
    _world_apply(world, 'herbivore', 'soil_moisture', 'direct')

def logic_10491(world):
    _world_apply(world, 'herbivore', 'runoff', 'square')

def logic_10492(world):
    _world_apply(world, 'herbivore', 'wind_x', 'pulse')

def logic_10493(world):
    _world_apply(world, 'herbivore', 'wind_y', 'saturation')

def logic_10494(world):
    _world_apply(world, 'herbivore', 'vegetation', 'gap')

def logic_10495(world):
    _world_apply(world, 'herbivore', 'biomass', 'direct')

def logic_10496(world):
    _world_apply(world, 'herbivore', 'predator', 'square')

def logic_10497(world):
    _world_apply(world, 'herbivore', 'carrion', 'saturation')

def logic_10498(world):
    _world_apply(world, 'herbivore', 'nutrients', 'gap')

def logic_10499(world):
    _world_apply(world, 'herbivore', 'decomposition_rate', 'direct')

def logic_10500(world):
    _world_apply(world, 'herbivore', 'oxygen', 'square')

def logic_10501(world):
    _world_apply(world, 'herbivore', 'co2', 'pulse')

def logic_10502(world):
    _world_apply(world, 'herbivore', 'photosynthesis_factor', 'saturation')

def logic_10503(world):
    _world_apply(world, 'herbivore', 'ice', 'gap')

def logic_10504(world):
    _world_apply(world, 'herbivore', 'evaporation', 'direct')

def logic_10505(world):
    _world_apply(world, 'herbivore', 'detritus', 'pulse')

def logic_10506(world):
    _world_apply(world, 'herbivore', 'methane', 'saturation')

def logic_10507(world):
    _world_apply(world, 'herbivore', 'pathogen_load', 'gap')

def logic_10508(world):
    _world_apply(world, 'herbivore', 'biodiversity', 'direct')

def logic_10509(world):
    _world_apply(world, 'herbivore', 'habitat_stress', 'square')

def logic_10510(world):
    _world_apply(world, 'herbivore', 'erosion', 'pulse')

def logic_10511(world):
    _world_apply(world, 'herbivore', 'soil_depth', 'saturation')

def logic_10512(world):
    _world_apply(world, 'herbivore', 'root_density', 'gap')

def logic_10513(world):
    _world_apply(world, 'herbivore', 'wetland', 'square')

def logic_10514(world):
    _world_apply(world, 'herbivore', 'carbon_storage', 'pulse')

def logic_10515(world):
    _world_apply(world, 'herbivore', 'fire_risk', 'saturation')

def logic_10516(world):
    _world_apply(world, 'herbivore', 'ash', 'gap')

def logic_10517(world):
    _world_apply(world, 'herbivore', 'snowpack', 'direct')

def logic_10518(world):
    _world_apply(world, 'herbivore', 'groundwater', 'square')

def logic_10519(world):
    _world_apply(world, 'herbivore', 'sediment', 'pulse')

def logic_10520(world):
    _world_apply(world, 'herbivore', 'salinity', 'saturation')

def logic_10521(world):
    _world_apply(world, 'herbivore', 'algae', 'direct')

def logic_10522(world):
    _world_apply(world, 'herbivore', 'organic_matter', 'square')

def logic_10523(world):
    _world_apply(world, 'herbivore', 'deadwood', 'pulse')

def logic_10524(world):
    _world_apply(world, 'herbivore', 'pollinators', 'saturation')

def logic_10525(world):
    _world_apply(world, 'herbivore', 'flowers', 'gap')

def logic_10526(world):
    _world_apply(world, 'herbivore', 'seed_bank', 'direct')

def logic_10527(world):
    _world_apply(world, 'herbivore', 'soil_carbon', 'square')

def logic_10528(world):
    _world_apply(world, 'herbivore', 'surface_ice', 'pulse')

def logic_10529(world):
    _world_apply(world, 'predator', 'temperature', 'gap')

def logic_10530(world):
    _world_apply(world, 'predator', 'surface_water', 'direct')

def logic_10531(world):
    _world_apply(world, 'predator', 'humidity', 'square')

def logic_10532(world):
    _world_apply(world, 'predator', 'cloud', 'pulse')

def logic_10533(world):
    _world_apply(world, 'predator', 'rain', 'saturation')

def logic_10534(world):
    _world_apply(world, 'predator', 'soil_moisture', 'gap')

def logic_10535(world):
    _world_apply(world, 'predator', 'runoff', 'direct')

def logic_10536(world):
    _world_apply(world, 'predator', 'wind_x', 'square')

def logic_10537(world):
    _world_apply(world, 'predator', 'wind_y', 'saturation')

def logic_10538(world):
    _world_apply(world, 'predator', 'vegetation', 'gap')

def logic_10539(world):
    _world_apply(world, 'predator', 'biomass', 'direct')

def logic_10540(world):
    _world_apply(world, 'predator', 'herbivore', 'square')

def logic_10541(world):
    _world_apply(world, 'predator', 'carrion', 'pulse')

def logic_10542(world):
    _world_apply(world, 'predator', 'nutrients', 'saturation')

def logic_10543(world):
    _world_apply(world, 'predator', 'decomposition_rate', 'gap')

def logic_10544(world):
    _world_apply(world, 'predator', 'oxygen', 'direct')

def logic_10545(world):
    _world_apply(world, 'predator', 'co2', 'pulse')

def logic_10546(world):
    _world_apply(world, 'predator', 'photosynthesis_factor', 'saturation')

def logic_10547(world):
    _world_apply(world, 'predator', 'ice', 'gap')

def logic_10548(world):
    _world_apply(world, 'predator', 'evaporation', 'direct')

def logic_10549(world):
    _world_apply(world, 'predator', 'detritus', 'square')

def logic_10550(world):
    _world_apply(world, 'predator', 'methane', 'pulse')

def logic_10551(world):
    _world_apply(world, 'predator', 'pathogen_load', 'saturation')

def logic_10552(world):
    _world_apply(world, 'predator', 'biodiversity', 'gap')

def logic_10553(world):
    _world_apply(world, 'predator', 'habitat_stress', 'square')

def logic_10554(world):
    _world_apply(world, 'predator', 'erosion', 'pulse')

def logic_10555(world):
    _world_apply(world, 'predator', 'soil_depth', 'saturation')

def logic_10556(world):
    _world_apply(world, 'predator', 'root_density', 'gap')

def logic_10557(world):
    _world_apply(world, 'predator', 'wetland', 'direct')

def logic_10558(world):
    _world_apply(world, 'predator', 'carbon_storage', 'square')

def logic_10559(world):
    _world_apply(world, 'predator', 'fire_risk', 'pulse')

def logic_10560(world):
    _world_apply(world, 'predator', 'ash', 'saturation')

def logic_10561(world):
    _world_apply(world, 'predator', 'snowpack', 'direct')

def logic_10562(world):
    _world_apply(world, 'predator', 'groundwater', 'square')

def logic_10563(world):
    _world_apply(world, 'predator', 'sediment', 'pulse')

def logic_10564(world):
    _world_apply(world, 'predator', 'salinity', 'saturation')

def logic_10565(world):
    _world_apply(world, 'predator', 'algae', 'gap')

def logic_10566(world):
    _world_apply(world, 'predator', 'organic_matter', 'direct')

def logic_10567(world):
    _world_apply(world, 'predator', 'deadwood', 'square')

def logic_10568(world):
    _world_apply(world, 'predator', 'pollinators', 'pulse')

def logic_10569(world):
    _world_apply(world, 'predator', 'flowers', 'gap')

def logic_10570(world):
    _world_apply(world, 'predator', 'seed_bank', 'direct')

def logic_10571(world):
    _world_apply(world, 'predator', 'soil_carbon', 'square')

def logic_10572(world):
    _world_apply(world, 'predator', 'surface_ice', 'pulse')

def logic_10573(world):
    _world_apply(world, 'carrion', 'temperature', 'saturation')

def logic_10574(world):
    _world_apply(world, 'carrion', 'surface_water', 'gap')

def logic_10575(world):
    _world_apply(world, 'carrion', 'humidity', 'direct')

def logic_10576(world):
    _world_apply(world, 'carrion', 'cloud', 'square')

def logic_10577(world):
    _world_apply(world, 'carrion', 'rain', 'saturation')

def logic_10578(world):
    _world_apply(world, 'carrion', 'soil_moisture', 'gap')

def logic_10579(world):
    _world_apply(world, 'carrion', 'runoff', 'direct')

def logic_10580(world):
    _world_apply(world, 'carrion', 'wind_x', 'square')

def logic_10581(world):
    _world_apply(world, 'carrion', 'wind_y', 'pulse')

def logic_10582(world):
    _world_apply(world, 'carrion', 'vegetation', 'saturation')

def logic_10583(world):
    _world_apply(world, 'carrion', 'biomass', 'gap')

def logic_10584(world):
    _world_apply(world, 'carrion', 'herbivore', 'direct')

def logic_10585(world):
    _world_apply(world, 'carrion', 'predator', 'pulse')

def logic_10586(world):
    _world_apply(world, 'carrion', 'nutrients', 'saturation')

def logic_10587(world):
    _world_apply(world, 'carrion', 'decomposition_rate', 'gap')

def logic_10588(world):
    _world_apply(world, 'carrion', 'oxygen', 'direct')

def logic_10589(world):
    _world_apply(world, 'carrion', 'co2', 'square')

def logic_10590(world):
    _world_apply(world, 'carrion', 'photosynthesis_factor', 'pulse')

def logic_10591(world):
    _world_apply(world, 'carrion', 'ice', 'saturation')

def logic_10592(world):
    _world_apply(world, 'carrion', 'evaporation', 'gap')

def logic_10593(world):
    _world_apply(world, 'carrion', 'detritus', 'square')

def logic_10594(world):
    _world_apply(world, 'carrion', 'methane', 'pulse')

def logic_10595(world):
    _world_apply(world, 'carrion', 'pathogen_load', 'saturation')

def logic_10596(world):
    _world_apply(world, 'carrion', 'biodiversity', 'gap')

def logic_10597(world):
    _world_apply(world, 'carrion', 'habitat_stress', 'direct')

def logic_10598(world):
    _world_apply(world, 'carrion', 'erosion', 'square')

def logic_10599(world):
    _world_apply(world, 'carrion', 'soil_depth', 'pulse')

def logic_10600(world):
    _world_apply(world, 'carrion', 'root_density', 'saturation')

def logic_10601(world):
    _world_apply(world, 'carrion', 'wetland', 'direct')

def logic_10602(world):
    _world_apply(world, 'carrion', 'carbon_storage', 'square')

def logic_10603(world):
    _world_apply(world, 'carrion', 'fire_risk', 'pulse')

def logic_10604(world):
    _world_apply(world, 'carrion', 'ash', 'saturation')

def logic_10605(world):
    _world_apply(world, 'carrion', 'snowpack', 'gap')

def logic_10606(world):
    _world_apply(world, 'carrion', 'groundwater', 'direct')

def logic_10607(world):
    _world_apply(world, 'carrion', 'sediment', 'square')

def logic_10608(world):
    _world_apply(world, 'carrion', 'salinity', 'pulse')

def logic_10609(world):
    _world_apply(world, 'carrion', 'algae', 'gap')

def logic_10610(world):
    _world_apply(world, 'carrion', 'organic_matter', 'direct')

def logic_10611(world):
    _world_apply(world, 'carrion', 'deadwood', 'square')

def logic_10612(world):
    _world_apply(world, 'carrion', 'pollinators', 'pulse')

def logic_10613(world):
    _world_apply(world, 'carrion', 'flowers', 'saturation')

def logic_10614(world):
    _world_apply(world, 'carrion', 'seed_bank', 'gap')

def logic_10615(world):
    _world_apply(world, 'carrion', 'soil_carbon', 'direct')

def logic_10616(world):
    _world_apply(world, 'carrion', 'surface_ice', 'square')

def logic_10617(world):
    _world_apply(world, 'nutrients', 'temperature', 'saturation')

def logic_10618(world):
    _world_apply(world, 'nutrients', 'surface_water', 'gap')

def logic_10619(world):
    _world_apply(world, 'nutrients', 'humidity', 'direct')

def logic_10620(world):
    _world_apply(world, 'nutrients', 'cloud', 'square')

def logic_10621(world):
    _world_apply(world, 'nutrients', 'rain', 'pulse')

def logic_10622(world):
    _world_apply(world, 'nutrients', 'soil_moisture', 'saturation')

def logic_10623(world):
    _world_apply(world, 'nutrients', 'runoff', 'gap')

def logic_10624(world):
    _world_apply(world, 'nutrients', 'wind_x', 'direct')

def logic_10625(world):
    _world_apply(world, 'nutrients', 'wind_y', 'pulse')

def logic_10626(world):
    _world_apply(world, 'nutrients', 'vegetation', 'saturation')

def logic_10627(world):
    _world_apply(world, 'nutrients', 'biomass', 'gap')

def logic_10628(world):
    _world_apply(world, 'nutrients', 'herbivore', 'direct')

def logic_10629(world):
    _world_apply(world, 'nutrients', 'predator', 'square')

def logic_10630(world):
    _world_apply(world, 'nutrients', 'carrion', 'pulse')

def logic_10631(world):
    _world_apply(world, 'nutrients', 'decomposition_rate', 'saturation')

def logic_10632(world):
    _world_apply(world, 'nutrients', 'oxygen', 'gap')

def logic_10633(world):
    _world_apply(world, 'nutrients', 'co2', 'square')

def logic_10634(world):
    _world_apply(world, 'nutrients', 'photosynthesis_factor', 'pulse')

def logic_10635(world):
    _world_apply(world, 'nutrients', 'ice', 'saturation')

def logic_10636(world):
    _world_apply(world, 'nutrients', 'evaporation', 'gap')

def logic_10637(world):
    _world_apply(world, 'nutrients', 'detritus', 'direct')

def logic_10638(world):
    _world_apply(world, 'nutrients', 'methane', 'square')

def logic_10639(world):
    _world_apply(world, 'nutrients', 'pathogen_load', 'pulse')

def logic_10640(world):
    _world_apply(world, 'nutrients', 'biodiversity', 'saturation')

def logic_10641(world):
    _world_apply(world, 'nutrients', 'habitat_stress', 'direct')

def logic_10642(world):
    _world_apply(world, 'nutrients', 'erosion', 'square')

def logic_10643(world):
    _world_apply(world, 'nutrients', 'soil_depth', 'pulse')

def logic_10644(world):
    _world_apply(world, 'nutrients', 'root_density', 'saturation')

def logic_10645(world):
    _world_apply(world, 'nutrients', 'wetland', 'gap')

def logic_10646(world):
    _world_apply(world, 'nutrients', 'carbon_storage', 'direct')

def logic_10647(world):
    _world_apply(world, 'nutrients', 'fire_risk', 'square')

def logic_10648(world):
    _world_apply(world, 'nutrients', 'ash', 'pulse')

def logic_10649(world):
    _world_apply(world, 'nutrients', 'snowpack', 'gap')

def logic_10650(world):
    _world_apply(world, 'nutrients', 'groundwater', 'direct')

def logic_10651(world):
    _world_apply(world, 'nutrients', 'sediment', 'square')

def logic_10652(world):
    _world_apply(world, 'nutrients', 'salinity', 'pulse')

def logic_10653(world):
    _world_apply(world, 'nutrients', 'algae', 'saturation')

def logic_10654(world):
    _world_apply(world, 'nutrients', 'organic_matter', 'gap')

def logic_10655(world):
    _world_apply(world, 'nutrients', 'deadwood', 'direct')

def logic_10656(world):
    _world_apply(world, 'nutrients', 'pollinators', 'square')

def logic_10657(world):
    _world_apply(world, 'nutrients', 'flowers', 'saturation')

def logic_10658(world):
    _world_apply(world, 'nutrients', 'seed_bank', 'gap')

def logic_10659(world):
    _world_apply(world, 'nutrients', 'soil_carbon', 'direct')

def logic_10660(world):
    _world_apply(world, 'nutrients', 'surface_ice', 'square')

def logic_10661(world):
    _world_apply(world, 'decomposition_rate', 'temperature', 'pulse')

def logic_10662(world):
    _world_apply(world, 'decomposition_rate', 'surface_water', 'saturation')

def logic_10663(world):
    _world_apply(world, 'decomposition_rate', 'humidity', 'gap')

def logic_10664(world):
    _world_apply(world, 'decomposition_rate', 'cloud', 'direct')

def logic_10665(world):
    _world_apply(world, 'decomposition_rate', 'rain', 'pulse')

def logic_10666(world):
    _world_apply(world, 'decomposition_rate', 'soil_moisture', 'saturation')

def logic_10667(world):
    _world_apply(world, 'decomposition_rate', 'runoff', 'gap')

def logic_10668(world):
    _world_apply(world, 'decomposition_rate', 'wind_x', 'direct')

def logic_10669(world):
    _world_apply(world, 'decomposition_rate', 'wind_y', 'square')

def logic_10670(world):
    _world_apply(world, 'decomposition_rate', 'vegetation', 'pulse')

def logic_10671(world):
    _world_apply(world, 'decomposition_rate', 'biomass', 'saturation')

def logic_10672(world):
    _world_apply(world, 'decomposition_rate', 'herbivore', 'gap')

def logic_10673(world):
    _world_apply(world, 'decomposition_rate', 'predator', 'square')

def logic_10674(world):
    _world_apply(world, 'decomposition_rate', 'carrion', 'pulse')

def logic_10675(world):
    _world_apply(world, 'decomposition_rate', 'nutrients', 'saturation')

def logic_10676(world):
    _world_apply(world, 'decomposition_rate', 'oxygen', 'gap')

def logic_10677(world):
    _world_apply(world, 'decomposition_rate', 'co2', 'direct')

def logic_10678(world):
    _world_apply(world, 'decomposition_rate', 'photosynthesis_factor', 'square')

def logic_10679(world):
    _world_apply(world, 'decomposition_rate', 'ice', 'pulse')

def logic_10680(world):
    _world_apply(world, 'decomposition_rate', 'evaporation', 'saturation')

def logic_10681(world):
    _world_apply(world, 'decomposition_rate', 'detritus', 'direct')

def logic_10682(world):
    _world_apply(world, 'decomposition_rate', 'methane', 'square')

def logic_10683(world):
    _world_apply(world, 'decomposition_rate', 'pathogen_load', 'pulse')

def logic_10684(world):
    _world_apply(world, 'decomposition_rate', 'biodiversity', 'saturation')

def logic_10685(world):
    _world_apply(world, 'decomposition_rate', 'habitat_stress', 'gap')

def logic_10686(world):
    _world_apply(world, 'decomposition_rate', 'erosion', 'direct')

def logic_10687(world):
    _world_apply(world, 'decomposition_rate', 'soil_depth', 'square')

def logic_10688(world):
    _world_apply(world, 'decomposition_rate', 'root_density', 'pulse')

def logic_10689(world):
    _world_apply(world, 'decomposition_rate', 'wetland', 'gap')

def logic_10690(world):
    _world_apply(world, 'decomposition_rate', 'carbon_storage', 'direct')

def logic_10691(world):
    _world_apply(world, 'decomposition_rate', 'fire_risk', 'square')

def logic_10692(world):
    _world_apply(world, 'decomposition_rate', 'ash', 'pulse')

def logic_10693(world):
    _world_apply(world, 'decomposition_rate', 'snowpack', 'saturation')

def logic_10694(world):
    _world_apply(world, 'decomposition_rate', 'groundwater', 'gap')

def logic_10695(world):
    _world_apply(world, 'decomposition_rate', 'sediment', 'direct')

def logic_10696(world):
    _world_apply(world, 'decomposition_rate', 'salinity', 'square')

def logic_10697(world):
    _world_apply(world, 'decomposition_rate', 'algae', 'saturation')

def logic_10698(world):
    _world_apply(world, 'decomposition_rate', 'organic_matter', 'gap')

def logic_10699(world):
    _world_apply(world, 'decomposition_rate', 'deadwood', 'direct')

def logic_10700(world):
    _world_apply(world, 'decomposition_rate', 'pollinators', 'square')

def logic_10701(world):
    _world_apply(world, 'decomposition_rate', 'flowers', 'pulse')

def logic_10702(world):
    _world_apply(world, 'decomposition_rate', 'seed_bank', 'saturation')

def logic_10703(world):
    _world_apply(world, 'decomposition_rate', 'soil_carbon', 'gap')

def logic_10704(world):
    _world_apply(world, 'decomposition_rate', 'surface_ice', 'direct')

def logic_10705(world):
    _world_apply(world, 'oxygen', 'temperature', 'pulse')

def logic_10706(world):
    _world_apply(world, 'oxygen', 'surface_water', 'saturation')

def logic_10707(world):
    _world_apply(world, 'oxygen', 'humidity', 'gap')

def logic_10708(world):
    _world_apply(world, 'oxygen', 'cloud', 'direct')

def logic_10709(world):
    _world_apply(world, 'oxygen', 'rain', 'square')

def logic_10710(world):
    _world_apply(world, 'oxygen', 'soil_moisture', 'pulse')

def logic_10711(world):
    _world_apply(world, 'oxygen', 'runoff', 'saturation')

def logic_10712(world):
    _world_apply(world, 'oxygen', 'wind_x', 'gap')

def logic_10713(world):
    _world_apply(world, 'oxygen', 'wind_y', 'square')

def logic_10714(world):
    _world_apply(world, 'oxygen', 'vegetation', 'pulse')

def logic_10715(world):
    _world_apply(world, 'oxygen', 'biomass', 'saturation')

def logic_10716(world):
    _world_apply(world, 'oxygen', 'herbivore', 'gap')

def logic_10717(world):
    _world_apply(world, 'oxygen', 'predator', 'direct')

def logic_10718(world):
    _world_apply(world, 'oxygen', 'carrion', 'square')

def logic_10719(world):
    _world_apply(world, 'oxygen', 'nutrients', 'pulse')

def logic_10720(world):
    _world_apply(world, 'oxygen', 'decomposition_rate', 'saturation')

def logic_10721(world):
    _world_apply(world, 'oxygen', 'co2', 'direct')

def logic_10722(world):
    _world_apply(world, 'oxygen', 'photosynthesis_factor', 'square')

def logic_10723(world):
    _world_apply(world, 'oxygen', 'ice', 'pulse')

def logic_10724(world):
    _world_apply(world, 'oxygen', 'evaporation', 'saturation')

def logic_10725(world):
    _world_apply(world, 'oxygen', 'detritus', 'gap')

def logic_10726(world):
    _world_apply(world, 'oxygen', 'methane', 'direct')

def logic_10727(world):
    _world_apply(world, 'oxygen', 'pathogen_load', 'square')

def logic_10728(world):
    _world_apply(world, 'oxygen', 'biodiversity', 'pulse')

def logic_10729(world):
    _world_apply(world, 'oxygen', 'habitat_stress', 'gap')

def logic_10730(world):
    _world_apply(world, 'oxygen', 'erosion', 'direct')

def logic_10731(world):
    _world_apply(world, 'oxygen', 'soil_depth', 'square')

def logic_10732(world):
    _world_apply(world, 'oxygen', 'root_density', 'pulse')

def logic_10733(world):
    _world_apply(world, 'oxygen', 'wetland', 'saturation')

def logic_10734(world):
    _world_apply(world, 'oxygen', 'carbon_storage', 'gap')

def logic_10735(world):
    _world_apply(world, 'oxygen', 'fire_risk', 'direct')

def logic_10736(world):
    _world_apply(world, 'oxygen', 'ash', 'square')

def logic_10737(world):
    _world_apply(world, 'oxygen', 'snowpack', 'saturation')

def logic_10738(world):
    _world_apply(world, 'oxygen', 'groundwater', 'gap')

def logic_10739(world):
    _world_apply(world, 'oxygen', 'sediment', 'direct')

def logic_10740(world):
    _world_apply(world, 'oxygen', 'salinity', 'square')

def logic_10741(world):
    _world_apply(world, 'oxygen', 'algae', 'pulse')

def logic_10742(world):
    _world_apply(world, 'oxygen', 'organic_matter', 'saturation')

def logic_10743(world):
    _world_apply(world, 'oxygen', 'deadwood', 'gap')

def logic_10744(world):
    _world_apply(world, 'oxygen', 'pollinators', 'direct')

def logic_10745(world):
    _world_apply(world, 'oxygen', 'flowers', 'pulse')

def logic_10746(world):
    _world_apply(world, 'oxygen', 'seed_bank', 'saturation')

def logic_10747(world):
    _world_apply(world, 'oxygen', 'soil_carbon', 'gap')

def logic_10748(world):
    _world_apply(world, 'oxygen', 'surface_ice', 'direct')

def logic_10749(world):
    _world_apply(world, 'co2', 'temperature', 'square')

def logic_10750(world):
    _world_apply(world, 'co2', 'surface_water', 'pulse')

def logic_10751(world):
    _world_apply(world, 'co2', 'humidity', 'saturation')

def logic_10752(world):
    _world_apply(world, 'co2', 'cloud', 'gap')

def logic_10753(world):
    _world_apply(world, 'co2', 'rain', 'square')

def logic_10754(world):
    _world_apply(world, 'co2', 'soil_moisture', 'pulse')

def logic_10755(world):
    _world_apply(world, 'co2', 'runoff', 'saturation')

def logic_10756(world):
    _world_apply(world, 'co2', 'wind_x', 'gap')

def logic_10757(world):
    _world_apply(world, 'co2', 'wind_y', 'direct')

def logic_10758(world):
    _world_apply(world, 'co2', 'vegetation', 'square')

def logic_10759(world):
    _world_apply(world, 'co2', 'biomass', 'pulse')

def logic_10760(world):
    _world_apply(world, 'co2', 'herbivore', 'saturation')

def logic_10761(world):
    _world_apply(world, 'co2', 'predator', 'direct')

def logic_10762(world):
    _world_apply(world, 'co2', 'carrion', 'square')

def logic_10763(world):
    _world_apply(world, 'co2', 'nutrients', 'pulse')

def logic_10764(world):
    _world_apply(world, 'co2', 'decomposition_rate', 'saturation')

def logic_10765(world):
    _world_apply(world, 'co2', 'oxygen', 'gap')

def logic_10766(world):
    _world_apply(world, 'co2', 'photosynthesis_factor', 'direct')

def logic_10767(world):
    _world_apply(world, 'co2', 'ice', 'square')

def logic_10768(world):
    _world_apply(world, 'co2', 'evaporation', 'pulse')

def logic_10769(world):
    _world_apply(world, 'co2', 'detritus', 'gap')

def logic_10770(world):
    _world_apply(world, 'co2', 'methane', 'direct')

def logic_10771(world):
    _world_apply(world, 'co2', 'pathogen_load', 'square')

def logic_10772(world):
    _world_apply(world, 'co2', 'biodiversity', 'pulse')

def logic_10773(world):
    _world_apply(world, 'co2', 'habitat_stress', 'saturation')

def logic_10774(world):
    _world_apply(world, 'co2', 'erosion', 'gap')

def logic_10775(world):
    _world_apply(world, 'co2', 'soil_depth', 'direct')

def logic_10776(world):
    _world_apply(world, 'co2', 'root_density', 'square')

def logic_10777(world):
    _world_apply(world, 'co2', 'wetland', 'saturation')

def logic_10778(world):
    _world_apply(world, 'co2', 'carbon_storage', 'gap')

def logic_10779(world):
    _world_apply(world, 'co2', 'fire_risk', 'direct')

def logic_10780(world):
    _world_apply(world, 'co2', 'ash', 'square')

def logic_10781(world):
    _world_apply(world, 'co2', 'snowpack', 'pulse')

def logic_10782(world):
    _world_apply(world, 'co2', 'groundwater', 'saturation')

def logic_10783(world):
    _world_apply(world, 'co2', 'sediment', 'gap')

def logic_10784(world):
    _world_apply(world, 'co2', 'salinity', 'direct')

def logic_10785(world):
    _world_apply(world, 'co2', 'algae', 'pulse')

def logic_10786(world):
    _world_apply(world, 'co2', 'organic_matter', 'saturation')

def logic_10787(world):
    _world_apply(world, 'co2', 'deadwood', 'gap')

def logic_10788(world):
    _world_apply(world, 'co2', 'pollinators', 'direct')

def logic_10789(world):
    _world_apply(world, 'co2', 'flowers', 'square')

def logic_10790(world):
    _world_apply(world, 'co2', 'seed_bank', 'pulse')

def logic_10791(world):
    _world_apply(world, 'co2', 'soil_carbon', 'saturation')

def logic_10792(world):
    _world_apply(world, 'co2', 'surface_ice', 'gap')

def logic_10793(world):
    _world_apply(world, 'photosynthesis_factor', 'temperature', 'square')

def logic_10794(world):
    _world_apply(world, 'photosynthesis_factor', 'surface_water', 'pulse')

def logic_10795(world):
    _world_apply(world, 'photosynthesis_factor', 'humidity', 'saturation')

def logic_10796(world):
    _world_apply(world, 'photosynthesis_factor', 'cloud', 'gap')

def logic_10797(world):
    _world_apply(world, 'photosynthesis_factor', 'rain', 'direct')

def logic_10798(world):
    _world_apply(world, 'photosynthesis_factor', 'soil_moisture', 'square')

def logic_10799(world):
    _world_apply(world, 'photosynthesis_factor', 'runoff', 'pulse')

def logic_10800(world):
    _world_apply(world, 'photosynthesis_factor', 'wind_x', 'saturation')

def logic_10801(world):
    _world_apply(world, 'photosynthesis_factor', 'wind_y', 'direct')

def logic_10802(world):
    _world_apply(world, 'photosynthesis_factor', 'vegetation', 'square')

def logic_10803(world):
    _world_apply(world, 'photosynthesis_factor', 'biomass', 'pulse')

def logic_10804(world):
    _world_apply(world, 'photosynthesis_factor', 'herbivore', 'saturation')

def logic_10805(world):
    _world_apply(world, 'photosynthesis_factor', 'predator', 'gap')

def logic_10806(world):
    _world_apply(world, 'photosynthesis_factor', 'carrion', 'direct')

def logic_10807(world):
    _world_apply(world, 'photosynthesis_factor', 'nutrients', 'square')

def logic_10808(world):
    _world_apply(world, 'photosynthesis_factor', 'decomposition_rate', 'pulse')

def logic_10809(world):
    _world_apply(world, 'photosynthesis_factor', 'oxygen', 'gap')

def logic_10810(world):
    _world_apply(world, 'photosynthesis_factor', 'co2', 'direct')

def logic_10811(world):
    _world_apply(world, 'photosynthesis_factor', 'ice', 'square')

def logic_10812(world):
    _world_apply(world, 'photosynthesis_factor', 'evaporation', 'pulse')

def logic_10813(world):
    _world_apply(world, 'photosynthesis_factor', 'detritus', 'saturation')

def logic_10814(world):
    _world_apply(world, 'photosynthesis_factor', 'methane', 'gap')

def logic_10815(world):
    _world_apply(world, 'photosynthesis_factor', 'pathogen_load', 'direct')

def logic_10816(world):
    _world_apply(world, 'photosynthesis_factor', 'biodiversity', 'square')

def logic_10817(world):
    _world_apply(world, 'photosynthesis_factor', 'habitat_stress', 'saturation')

def logic_10818(world):
    _world_apply(world, 'photosynthesis_factor', 'erosion', 'gap')

def logic_10819(world):
    _world_apply(world, 'photosynthesis_factor', 'soil_depth', 'direct')

def logic_10820(world):
    _world_apply(world, 'photosynthesis_factor', 'root_density', 'square')

def logic_10821(world):
    _world_apply(world, 'photosynthesis_factor', 'wetland', 'pulse')

def logic_10822(world):
    _world_apply(world, 'photosynthesis_factor', 'carbon_storage', 'saturation')

def logic_10823(world):
    _world_apply(world, 'photosynthesis_factor', 'fire_risk', 'gap')

def logic_10824(world):
    _world_apply(world, 'photosynthesis_factor', 'ash', 'direct')

def logic_10825(world):
    _world_apply(world, 'photosynthesis_factor', 'snowpack', 'pulse')

def logic_10826(world):
    _world_apply(world, 'photosynthesis_factor', 'groundwater', 'saturation')

def logic_10827(world):
    _world_apply(world, 'photosynthesis_factor', 'sediment', 'gap')

def logic_10828(world):
    _world_apply(world, 'photosynthesis_factor', 'salinity', 'direct')

def logic_10829(world):
    _world_apply(world, 'photosynthesis_factor', 'algae', 'square')

def logic_10830(world):
    _world_apply(world, 'photosynthesis_factor', 'organic_matter', 'pulse')

def logic_10831(world):
    _world_apply(world, 'photosynthesis_factor', 'deadwood', 'saturation')

def logic_10832(world):
    _world_apply(world, 'photosynthesis_factor', 'pollinators', 'gap')

def logic_10833(world):
    _world_apply(world, 'photosynthesis_factor', 'flowers', 'square')

def logic_10834(world):
    _world_apply(world, 'photosynthesis_factor', 'seed_bank', 'pulse')

def logic_10835(world):
    _world_apply(world, 'photosynthesis_factor', 'soil_carbon', 'saturation')

def logic_10836(world):
    _world_apply(world, 'photosynthesis_factor', 'surface_ice', 'gap')

def logic_10837(world):
    _world_apply(world, 'ice', 'temperature', 'direct')

def logic_10838(world):
    _world_apply(world, 'ice', 'surface_water', 'square')

def logic_10839(world):
    _world_apply(world, 'ice', 'humidity', 'pulse')

def logic_10840(world):
    _world_apply(world, 'ice', 'cloud', 'saturation')

def logic_10841(world):
    _world_apply(world, 'ice', 'rain', 'direct')

def logic_10842(world):
    _world_apply(world, 'ice', 'soil_moisture', 'square')

def logic_10843(world):
    _world_apply(world, 'ice', 'runoff', 'pulse')

def logic_10844(world):
    _world_apply(world, 'ice', 'wind_x', 'saturation')

def logic_10845(world):
    _world_apply(world, 'ice', 'wind_y', 'gap')

def logic_10846(world):
    _world_apply(world, 'ice', 'vegetation', 'direct')

def logic_10847(world):
    _world_apply(world, 'ice', 'biomass', 'square')

def logic_10848(world):
    _world_apply(world, 'ice', 'herbivore', 'pulse')

def logic_10849(world):
    _world_apply(world, 'ice', 'predator', 'gap')

def logic_10850(world):
    _world_apply(world, 'ice', 'carrion', 'direct')

def logic_10851(world):
    _world_apply(world, 'ice', 'nutrients', 'square')

def logic_10852(world):
    _world_apply(world, 'ice', 'decomposition_rate', 'pulse')

def logic_10853(world):
    _world_apply(world, 'ice', 'oxygen', 'saturation')

def logic_10854(world):
    _world_apply(world, 'ice', 'co2', 'gap')

def logic_10855(world):
    _world_apply(world, 'ice', 'photosynthesis_factor', 'direct')

def logic_10856(world):
    _world_apply(world, 'ice', 'evaporation', 'square')

def logic_10857(world):
    _world_apply(world, 'ice', 'detritus', 'saturation')

def logic_10858(world):
    _world_apply(world, 'ice', 'methane', 'gap')

def logic_10859(world):
    _world_apply(world, 'ice', 'pathogen_load', 'direct')

def logic_10860(world):
    _world_apply(world, 'ice', 'biodiversity', 'square')

def logic_10861(world):
    _world_apply(world, 'ice', 'habitat_stress', 'pulse')

def logic_10862(world):
    _world_apply(world, 'ice', 'erosion', 'saturation')

def logic_10863(world):
    _world_apply(world, 'ice', 'soil_depth', 'gap')

def logic_10864(world):
    _world_apply(world, 'ice', 'root_density', 'direct')

def logic_10865(world):
    _world_apply(world, 'ice', 'wetland', 'pulse')

def logic_10866(world):
    _world_apply(world, 'ice', 'carbon_storage', 'saturation')

def logic_10867(world):
    _world_apply(world, 'ice', 'fire_risk', 'gap')

def logic_10868(world):
    _world_apply(world, 'ice', 'ash', 'direct')

def logic_10869(world):
    _world_apply(world, 'ice', 'snowpack', 'square')

def logic_10870(world):
    _world_apply(world, 'ice', 'groundwater', 'pulse')

def logic_10871(world):
    _world_apply(world, 'ice', 'sediment', 'saturation')

def logic_10872(world):
    _world_apply(world, 'ice', 'salinity', 'gap')

def logic_10873(world):
    _world_apply(world, 'ice', 'algae', 'square')

def logic_10874(world):
    _world_apply(world, 'ice', 'organic_matter', 'pulse')

def logic_10875(world):
    _world_apply(world, 'ice', 'deadwood', 'saturation')

def logic_10876(world):
    _world_apply(world, 'ice', 'pollinators', 'gap')

def logic_10877(world):
    _world_apply(world, 'ice', 'flowers', 'direct')

def logic_10878(world):
    _world_apply(world, 'ice', 'seed_bank', 'square')

def logic_10879(world):
    _world_apply(world, 'ice', 'soil_carbon', 'pulse')

def logic_10880(world):
    _world_apply(world, 'ice', 'surface_ice', 'saturation')

def logic_10881(world):
    _world_apply(world, 'evaporation', 'temperature', 'direct')

def logic_10882(world):
    _world_apply(world, 'evaporation', 'surface_water', 'square')

def logic_10883(world):
    _world_apply(world, 'evaporation', 'humidity', 'pulse')

def logic_10884(world):
    _world_apply(world, 'evaporation', 'cloud', 'saturation')

def logic_10885(world):
    _world_apply(world, 'evaporation', 'rain', 'gap')

def logic_10886(world):
    _world_apply(world, 'evaporation', 'soil_moisture', 'direct')

def logic_10887(world):
    _world_apply(world, 'evaporation', 'runoff', 'square')

def logic_10888(world):
    _world_apply(world, 'evaporation', 'wind_x', 'pulse')

def logic_10889(world):
    _world_apply(world, 'evaporation', 'wind_y', 'gap')

def logic_10890(world):
    _world_apply(world, 'evaporation', 'vegetation', 'direct')

def logic_10891(world):
    _world_apply(world, 'evaporation', 'biomass', 'square')

def logic_10892(world):
    _world_apply(world, 'evaporation', 'herbivore', 'pulse')

def logic_10893(world):
    _world_apply(world, 'evaporation', 'predator', 'saturation')

def logic_10894(world):
    _world_apply(world, 'evaporation', 'carrion', 'gap')

def logic_10895(world):
    _world_apply(world, 'evaporation', 'nutrients', 'direct')

def logic_10896(world):
    _world_apply(world, 'evaporation', 'decomposition_rate', 'square')

def logic_10897(world):
    _world_apply(world, 'evaporation', 'oxygen', 'saturation')

def logic_10898(world):
    _world_apply(world, 'evaporation', 'co2', 'gap')

def logic_10899(world):
    _world_apply(world, 'evaporation', 'photosynthesis_factor', 'direct')

def logic_10900(world):
    _world_apply(world, 'evaporation', 'ice', 'square')

def logic_10901(world):
    _world_apply(world, 'evaporation', 'detritus', 'pulse')

def logic_10902(world):
    _world_apply(world, 'evaporation', 'methane', 'saturation')

def logic_10903(world):
    _world_apply(world, 'evaporation', 'pathogen_load', 'gap')

def logic_10904(world):
    _world_apply(world, 'evaporation', 'biodiversity', 'direct')

def logic_10905(world):
    _world_apply(world, 'evaporation', 'habitat_stress', 'pulse')

def logic_10906(world):
    _world_apply(world, 'evaporation', 'erosion', 'saturation')

def logic_10907(world):
    _world_apply(world, 'evaporation', 'soil_depth', 'gap')

def logic_10908(world):
    _world_apply(world, 'evaporation', 'root_density', 'direct')

def logic_10909(world):
    _world_apply(world, 'evaporation', 'wetland', 'square')

def logic_10910(world):
    _world_apply(world, 'evaporation', 'carbon_storage', 'pulse')

def logic_10911(world):
    _world_apply(world, 'evaporation', 'fire_risk', 'saturation')

def logic_10912(world):
    _world_apply(world, 'evaporation', 'ash', 'gap')

def logic_10913(world):
    _world_apply(world, 'evaporation', 'snowpack', 'square')

def logic_10914(world):
    _world_apply(world, 'evaporation', 'groundwater', 'pulse')

def logic_10915(world):
    _world_apply(world, 'evaporation', 'sediment', 'saturation')

def logic_10916(world):
    _world_apply(world, 'evaporation', 'salinity', 'gap')

def logic_10917(world):
    _world_apply(world, 'evaporation', 'algae', 'direct')

def logic_10918(world):
    _world_apply(world, 'evaporation', 'organic_matter', 'square')

def logic_10919(world):
    _world_apply(world, 'evaporation', 'deadwood', 'pulse')

def logic_10920(world):
    _world_apply(world, 'evaporation', 'pollinators', 'saturation')

def logic_10921(world):
    _world_apply(world, 'evaporation', 'flowers', 'direct')

def logic_10922(world):
    _world_apply(world, 'evaporation', 'seed_bank', 'square')

def logic_10923(world):
    _world_apply(world, 'evaporation', 'soil_carbon', 'pulse')

def logic_10924(world):
    _world_apply(world, 'evaporation', 'surface_ice', 'saturation')

def logic_10925(world):
    _world_apply(world, 'detritus', 'temperature', 'gap')

def logic_10926(world):
    _world_apply(world, 'detritus', 'surface_water', 'direct')

def logic_10927(world):
    _world_apply(world, 'detritus', 'humidity', 'square')

def logic_10928(world):
    _world_apply(world, 'detritus', 'cloud', 'pulse')

def logic_10929(world):
    _world_apply(world, 'detritus', 'rain', 'gap')

def logic_10930(world):
    _world_apply(world, 'detritus', 'soil_moisture', 'direct')

def logic_10931(world):
    _world_apply(world, 'detritus', 'runoff', 'square')

def logic_10932(world):
    _world_apply(world, 'detritus', 'wind_x', 'pulse')

def logic_10933(world):
    _world_apply(world, 'detritus', 'wind_y', 'saturation')

def logic_10934(world):
    _world_apply(world, 'detritus', 'vegetation', 'gap')

def logic_10935(world):
    _world_apply(world, 'detritus', 'biomass', 'direct')

def logic_10936(world):
    _world_apply(world, 'detritus', 'herbivore', 'square')

def logic_10937(world):
    _world_apply(world, 'detritus', 'predator', 'saturation')

def logic_10938(world):
    _world_apply(world, 'detritus', 'carrion', 'gap')

def logic_10939(world):
    _world_apply(world, 'detritus', 'nutrients', 'direct')

def logic_10940(world):
    _world_apply(world, 'detritus', 'decomposition_rate', 'square')

def logic_10941(world):
    _world_apply(world, 'detritus', 'oxygen', 'pulse')

def logic_10942(world):
    _world_apply(world, 'detritus', 'co2', 'saturation')

def logic_10943(world):
    _world_apply(world, 'detritus', 'photosynthesis_factor', 'gap')

def logic_10944(world):
    _world_apply(world, 'detritus', 'ice', 'direct')

def logic_10945(world):
    _world_apply(world, 'detritus', 'evaporation', 'pulse')

def logic_10946(world):
    _world_apply(world, 'detritus', 'methane', 'saturation')

def logic_10947(world):
    _world_apply(world, 'detritus', 'pathogen_load', 'gap')

def logic_10948(world):
    _world_apply(world, 'detritus', 'biodiversity', 'direct')

def logic_10949(world):
    _world_apply(world, 'detritus', 'habitat_stress', 'square')

def logic_10950(world):
    _world_apply(world, 'detritus', 'erosion', 'pulse')

def logic_10951(world):
    _world_apply(world, 'detritus', 'soil_depth', 'saturation')

def logic_10952(world):
    _world_apply(world, 'detritus', 'root_density', 'gap')

def logic_10953(world):
    _world_apply(world, 'detritus', 'wetland', 'square')

def logic_10954(world):
    _world_apply(world, 'detritus', 'carbon_storage', 'pulse')

def logic_10955(world):
    _world_apply(world, 'detritus', 'fire_risk', 'saturation')

def logic_10956(world):
    _world_apply(world, 'detritus', 'ash', 'gap')

def logic_10957(world):
    _world_apply(world, 'detritus', 'snowpack', 'direct')

def logic_10958(world):
    _world_apply(world, 'detritus', 'groundwater', 'square')

def logic_10959(world):
    _world_apply(world, 'detritus', 'sediment', 'pulse')

def logic_10960(world):
    _world_apply(world, 'detritus', 'salinity', 'saturation')

def logic_10961(world):
    _world_apply(world, 'detritus', 'algae', 'direct')

def logic_10962(world):
    _world_apply(world, 'detritus', 'organic_matter', 'square')

def logic_10963(world):
    _world_apply(world, 'detritus', 'deadwood', 'pulse')

def logic_10964(world):
    _world_apply(world, 'detritus', 'pollinators', 'saturation')

def logic_10965(world):
    _world_apply(world, 'detritus', 'flowers', 'gap')

def logic_10966(world):
    _world_apply(world, 'detritus', 'seed_bank', 'direct')

def logic_10967(world):
    _world_apply(world, 'detritus', 'soil_carbon', 'square')

def logic_10968(world):
    _world_apply(world, 'detritus', 'surface_ice', 'pulse')

def logic_10969(world):
    _world_apply(world, 'methane', 'temperature', 'gap')

def logic_10970(world):
    _world_apply(world, 'methane', 'surface_water', 'direct')

def logic_10971(world):
    _world_apply(world, 'methane', 'humidity', 'square')

def logic_10972(world):
    _world_apply(world, 'methane', 'cloud', 'pulse')

def logic_10973(world):
    _world_apply(world, 'methane', 'rain', 'saturation')

def logic_10974(world):
    _world_apply(world, 'methane', 'soil_moisture', 'gap')

def logic_10975(world):
    _world_apply(world, 'methane', 'runoff', 'direct')

def logic_10976(world):
    _world_apply(world, 'methane', 'wind_x', 'square')

def logic_10977(world):
    _world_apply(world, 'methane', 'wind_y', 'saturation')

def logic_10978(world):
    _world_apply(world, 'methane', 'vegetation', 'gap')

def logic_10979(world):
    _world_apply(world, 'methane', 'biomass', 'direct')

def logic_10980(world):
    _world_apply(world, 'methane', 'herbivore', 'square')

def logic_10981(world):
    _world_apply(world, 'methane', 'predator', 'pulse')

def logic_10982(world):
    _world_apply(world, 'methane', 'carrion', 'saturation')

def logic_10983(world):
    _world_apply(world, 'methane', 'nutrients', 'gap')

def logic_10984(world):
    _world_apply(world, 'methane', 'decomposition_rate', 'direct')

def logic_10985(world):
    _world_apply(world, 'methane', 'oxygen', 'pulse')

def logic_10986(world):
    _world_apply(world, 'methane', 'co2', 'saturation')

def logic_10987(world):
    _world_apply(world, 'methane', 'photosynthesis_factor', 'gap')

def logic_10988(world):
    _world_apply(world, 'methane', 'ice', 'direct')

def logic_10989(world):
    _world_apply(world, 'methane', 'evaporation', 'square')

def logic_10990(world):
    _world_apply(world, 'methane', 'detritus', 'pulse')

def logic_10991(world):
    _world_apply(world, 'methane', 'pathogen_load', 'saturation')

def logic_10992(world):
    _world_apply(world, 'methane', 'biodiversity', 'gap')

def logic_10993(world):
    _world_apply(world, 'methane', 'habitat_stress', 'square')

def logic_10994(world):
    _world_apply(world, 'methane', 'erosion', 'pulse')

def logic_10995(world):
    _world_apply(world, 'methane', 'soil_depth', 'saturation')

def logic_10996(world):
    _world_apply(world, 'methane', 'root_density', 'gap')

def logic_10997(world):
    _world_apply(world, 'methane', 'wetland', 'direct')

def logic_10998(world):
    _world_apply(world, 'methane', 'carbon_storage', 'square')

def logic_10999(world):
    _world_apply(world, 'methane', 'fire_risk', 'pulse')

def logic_11000(world):
    _world_apply(world, 'methane', 'ash', 'saturation')

def logic_11001(world):
    _world_apply(world, 'methane', 'snowpack', 'direct')

def logic_11002(world):
    _world_apply(world, 'methane', 'groundwater', 'square')

def logic_11003(world):
    _world_apply(world, 'methane', 'sediment', 'pulse')

def logic_11004(world):
    _world_apply(world, 'methane', 'salinity', 'saturation')

def logic_11005(world):
    _world_apply(world, 'methane', 'algae', 'gap')

def logic_11006(world):
    _world_apply(world, 'methane', 'organic_matter', 'direct')

def logic_11007(world):
    _world_apply(world, 'methane', 'deadwood', 'square')

def logic_11008(world):
    _world_apply(world, 'methane', 'pollinators', 'pulse')

def logic_11009(world):
    _world_apply(world, 'methane', 'flowers', 'gap')

def logic_11010(world):
    _world_apply(world, 'methane', 'seed_bank', 'direct')

def logic_11011(world):
    _world_apply(world, 'methane', 'soil_carbon', 'square')

def logic_11012(world):
    _world_apply(world, 'methane', 'surface_ice', 'pulse')

def logic_11013(world):
    _world_apply(world, 'pathogen_load', 'temperature', 'saturation')

def logic_11014(world):
    _world_apply(world, 'pathogen_load', 'surface_water', 'gap')

def logic_11015(world):
    _world_apply(world, 'pathogen_load', 'humidity', 'direct')

def logic_11016(world):
    _world_apply(world, 'pathogen_load', 'cloud', 'square')

def logic_11017(world):
    _world_apply(world, 'pathogen_load', 'rain', 'saturation')

def logic_11018(world):
    _world_apply(world, 'pathogen_load', 'soil_moisture', 'gap')

def logic_11019(world):
    _world_apply(world, 'pathogen_load', 'runoff', 'direct')

def logic_11020(world):
    _world_apply(world, 'pathogen_load', 'wind_x', 'square')

def logic_11021(world):
    _world_apply(world, 'pathogen_load', 'wind_y', 'pulse')

def logic_11022(world):
    _world_apply(world, 'pathogen_load', 'vegetation', 'saturation')

def logic_11023(world):
    _world_apply(world, 'pathogen_load', 'biomass', 'gap')

def logic_11024(world):
    _world_apply(world, 'pathogen_load', 'herbivore', 'direct')

def logic_11025(world):
    _world_apply(world, 'pathogen_load', 'predator', 'pulse')

def logic_11026(world):
    _world_apply(world, 'pathogen_load', 'carrion', 'saturation')

def logic_11027(world):
    _world_apply(world, 'pathogen_load', 'nutrients', 'gap')

def logic_11028(world):
    _world_apply(world, 'pathogen_load', 'decomposition_rate', 'direct')

def logic_11029(world):
    _world_apply(world, 'pathogen_load', 'oxygen', 'square')

def logic_11030(world):
    _world_apply(world, 'pathogen_load', 'co2', 'pulse')

def logic_11031(world):
    _world_apply(world, 'pathogen_load', 'photosynthesis_factor', 'saturation')

def logic_11032(world):
    _world_apply(world, 'pathogen_load', 'ice', 'gap')

def logic_11033(world):
    _world_apply(world, 'pathogen_load', 'evaporation', 'square')

def logic_11034(world):
    _world_apply(world, 'pathogen_load', 'detritus', 'pulse')

def logic_11035(world):
    _world_apply(world, 'pathogen_load', 'methane', 'saturation')

def logic_11036(world):
    _world_apply(world, 'pathogen_load', 'biodiversity', 'gap')

def logic_11037(world):
    _world_apply(world, 'pathogen_load', 'habitat_stress', 'direct')

def logic_11038(world):
    _world_apply(world, 'pathogen_load', 'erosion', 'square')

def logic_11039(world):
    _world_apply(world, 'pathogen_load', 'soil_depth', 'pulse')

def logic_11040(world):
    _world_apply(world, 'pathogen_load', 'root_density', 'saturation')

def logic_11041(world):
    _world_apply(world, 'pathogen_load', 'wetland', 'direct')

def logic_11042(world):
    _world_apply(world, 'pathogen_load', 'carbon_storage', 'square')

def logic_11043(world):
    _world_apply(world, 'pathogen_load', 'fire_risk', 'pulse')

def logic_11044(world):
    _world_apply(world, 'pathogen_load', 'ash', 'saturation')

def logic_11045(world):
    _world_apply(world, 'pathogen_load', 'snowpack', 'gap')

def logic_11046(world):
    _world_apply(world, 'pathogen_load', 'groundwater', 'direct')

def logic_11047(world):
    _world_apply(world, 'pathogen_load', 'sediment', 'square')

def logic_11048(world):
    _world_apply(world, 'pathogen_load', 'salinity', 'pulse')

def logic_11049(world):
    _world_apply(world, 'pathogen_load', 'algae', 'gap')

def logic_11050(world):
    _world_apply(world, 'pathogen_load', 'organic_matter', 'direct')

def logic_11051(world):
    _world_apply(world, 'pathogen_load', 'deadwood', 'square')

def logic_11052(world):
    _world_apply(world, 'pathogen_load', 'pollinators', 'pulse')

def logic_11053(world):
    _world_apply(world, 'pathogen_load', 'flowers', 'saturation')

def logic_11054(world):
    _world_apply(world, 'pathogen_load', 'seed_bank', 'gap')

def logic_11055(world):
    _world_apply(world, 'pathogen_load', 'soil_carbon', 'direct')

def logic_11056(world):
    _world_apply(world, 'pathogen_load', 'surface_ice', 'square')

def logic_11057(world):
    _world_apply(world, 'biodiversity', 'temperature', 'saturation')

def logic_11058(world):
    _world_apply(world, 'biodiversity', 'surface_water', 'gap')

def logic_11059(world):
    _world_apply(world, 'biodiversity', 'humidity', 'direct')

def logic_11060(world):
    _world_apply(world, 'biodiversity', 'cloud', 'square')

def logic_11061(world):
    _world_apply(world, 'biodiversity', 'rain', 'pulse')

def logic_11062(world):
    _world_apply(world, 'biodiversity', 'soil_moisture', 'saturation')

def logic_11063(world):
    _world_apply(world, 'biodiversity', 'runoff', 'gap')

def logic_11064(world):
    _world_apply(world, 'biodiversity', 'wind_x', 'direct')

def logic_11065(world):
    _world_apply(world, 'biodiversity', 'wind_y', 'pulse')

def logic_11066(world):
    _world_apply(world, 'biodiversity', 'vegetation', 'saturation')

def logic_11067(world):
    _world_apply(world, 'biodiversity', 'biomass', 'gap')

def logic_11068(world):
    _world_apply(world, 'biodiversity', 'herbivore', 'direct')

def logic_11069(world):
    _world_apply(world, 'biodiversity', 'predator', 'square')

def logic_11070(world):
    _world_apply(world, 'biodiversity', 'carrion', 'pulse')

def logic_11071(world):
    _world_apply(world, 'biodiversity', 'nutrients', 'saturation')

def logic_11072(world):
    _world_apply(world, 'biodiversity', 'decomposition_rate', 'gap')

def logic_11073(world):
    _world_apply(world, 'biodiversity', 'oxygen', 'square')

def logic_11074(world):
    _world_apply(world, 'biodiversity', 'co2', 'pulse')

def logic_11075(world):
    _world_apply(world, 'biodiversity', 'photosynthesis_factor', 'saturation')

def logic_11076(world):
    _world_apply(world, 'biodiversity', 'ice', 'gap')

def logic_11077(world):
    _world_apply(world, 'biodiversity', 'evaporation', 'direct')

def logic_11078(world):
    _world_apply(world, 'biodiversity', 'detritus', 'square')

def logic_11079(world):
    _world_apply(world, 'biodiversity', 'methane', 'pulse')

def logic_11080(world):
    _world_apply(world, 'biodiversity', 'pathogen_load', 'saturation')

def logic_11081(world):
    _world_apply(world, 'biodiversity', 'habitat_stress', 'direct')

def logic_11082(world):
    _world_apply(world, 'biodiversity', 'erosion', 'square')

def logic_11083(world):
    _world_apply(world, 'biodiversity', 'soil_depth', 'pulse')

def logic_11084(world):
    _world_apply(world, 'biodiversity', 'root_density', 'saturation')

def logic_11085(world):
    _world_apply(world, 'biodiversity', 'wetland', 'gap')

def logic_11086(world):
    _world_apply(world, 'biodiversity', 'carbon_storage', 'direct')

def logic_11087(world):
    _world_apply(world, 'biodiversity', 'fire_risk', 'square')

def logic_11088(world):
    _world_apply(world, 'biodiversity', 'ash', 'pulse')

def logic_11089(world):
    _world_apply(world, 'biodiversity', 'snowpack', 'gap')

def logic_11090(world):
    _world_apply(world, 'biodiversity', 'groundwater', 'direct')

def logic_11091(world):
    _world_apply(world, 'biodiversity', 'sediment', 'square')

def logic_11092(world):
    _world_apply(world, 'biodiversity', 'salinity', 'pulse')

def logic_11093(world):
    _world_apply(world, 'biodiversity', 'algae', 'saturation')

def logic_11094(world):
    _world_apply(world, 'biodiversity', 'organic_matter', 'gap')

def logic_11095(world):
    _world_apply(world, 'biodiversity', 'deadwood', 'direct')

def logic_11096(world):
    _world_apply(world, 'biodiversity', 'pollinators', 'square')

def logic_11097(world):
    _world_apply(world, 'biodiversity', 'flowers', 'saturation')

def logic_11098(world):
    _world_apply(world, 'biodiversity', 'seed_bank', 'gap')

def logic_11099(world):
    _world_apply(world, 'biodiversity', 'soil_carbon', 'direct')

def logic_11100(world):
    _world_apply(world, 'biodiversity', 'surface_ice', 'square')

def logic_11101(world):
    _world_apply(world, 'habitat_stress', 'temperature', 'pulse')

def logic_11102(world):
    _world_apply(world, 'habitat_stress', 'surface_water', 'saturation')

def logic_11103(world):
    _world_apply(world, 'habitat_stress', 'humidity', 'gap')

def logic_11104(world):
    _world_apply(world, 'habitat_stress', 'cloud', 'direct')

def logic_11105(world):
    _world_apply(world, 'habitat_stress', 'rain', 'pulse')

def logic_11106(world):
    _world_apply(world, 'habitat_stress', 'soil_moisture', 'saturation')

def logic_11107(world):
    _world_apply(world, 'habitat_stress', 'runoff', 'gap')

def logic_11108(world):
    _world_apply(world, 'habitat_stress', 'wind_x', 'direct')

def logic_11109(world):
    _world_apply(world, 'habitat_stress', 'wind_y', 'square')

def logic_11110(world):
    _world_apply(world, 'habitat_stress', 'vegetation', 'pulse')

def logic_11111(world):
    _world_apply(world, 'habitat_stress', 'biomass', 'saturation')

def logic_11112(world):
    _world_apply(world, 'habitat_stress', 'herbivore', 'gap')

def logic_11113(world):
    _world_apply(world, 'habitat_stress', 'predator', 'square')

def logic_11114(world):
    _world_apply(world, 'habitat_stress', 'carrion', 'pulse')

def logic_11115(world):
    _world_apply(world, 'habitat_stress', 'nutrients', 'saturation')

def logic_11116(world):
    _world_apply(world, 'habitat_stress', 'decomposition_rate', 'gap')

def logic_11117(world):
    _world_apply(world, 'habitat_stress', 'oxygen', 'direct')

def logic_11118(world):
    _world_apply(world, 'habitat_stress', 'co2', 'square')

def logic_11119(world):
    _world_apply(world, 'habitat_stress', 'photosynthesis_factor', 'pulse')

def logic_11120(world):
    _world_apply(world, 'habitat_stress', 'ice', 'saturation')

def logic_11121(world):
    _world_apply(world, 'habitat_stress', 'evaporation', 'direct')

def logic_11122(world):
    _world_apply(world, 'habitat_stress', 'detritus', 'square')

def logic_11123(world):
    _world_apply(world, 'habitat_stress', 'methane', 'pulse')

def logic_11124(world):
    _world_apply(world, 'habitat_stress', 'pathogen_load', 'saturation')

def logic_11125(world):
    _world_apply(world, 'habitat_stress', 'biodiversity', 'gap')

def logic_11126(world):
    _world_apply(world, 'habitat_stress', 'erosion', 'direct')

def logic_11127(world):
    _world_apply(world, 'habitat_stress', 'soil_depth', 'square')

def logic_11128(world):
    _world_apply(world, 'habitat_stress', 'root_density', 'pulse')

def logic_11129(world):
    _world_apply(world, 'habitat_stress', 'wetland', 'gap')

def logic_11130(world):
    _world_apply(world, 'habitat_stress', 'carbon_storage', 'direct')

def logic_11131(world):
    _world_apply(world, 'habitat_stress', 'fire_risk', 'square')

def logic_11132(world):
    _world_apply(world, 'habitat_stress', 'ash', 'pulse')

def logic_11133(world):
    _world_apply(world, 'habitat_stress', 'snowpack', 'saturation')

def logic_11134(world):
    _world_apply(world, 'habitat_stress', 'groundwater', 'gap')

def logic_11135(world):
    _world_apply(world, 'habitat_stress', 'sediment', 'direct')

def logic_11136(world):
    _world_apply(world, 'habitat_stress', 'salinity', 'square')

def logic_11137(world):
    _world_apply(world, 'habitat_stress', 'algae', 'saturation')

def logic_11138(world):
    _world_apply(world, 'habitat_stress', 'organic_matter', 'gap')

def logic_11139(world):
    _world_apply(world, 'habitat_stress', 'deadwood', 'direct')

def logic_11140(world):
    _world_apply(world, 'habitat_stress', 'pollinators', 'square')

def logic_11141(world):
    _world_apply(world, 'habitat_stress', 'flowers', 'pulse')

def logic_11142(world):
    _world_apply(world, 'habitat_stress', 'seed_bank', 'saturation')

def logic_11143(world):
    _world_apply(world, 'habitat_stress', 'soil_carbon', 'gap')

def logic_11144(world):
    _world_apply(world, 'habitat_stress', 'surface_ice', 'direct')

def logic_11145(world):
    _world_apply(world, 'erosion', 'temperature', 'pulse')

def logic_11146(world):
    _world_apply(world, 'erosion', 'surface_water', 'saturation')

def logic_11147(world):
    _world_apply(world, 'erosion', 'humidity', 'gap')

def logic_11148(world):
    _world_apply(world, 'erosion', 'cloud', 'direct')

def logic_11149(world):
    _world_apply(world, 'erosion', 'rain', 'square')

def logic_11150(world):
    _world_apply(world, 'erosion', 'soil_moisture', 'pulse')

def logic_11151(world):
    _world_apply(world, 'erosion', 'runoff', 'saturation')

def logic_11152(world):
    _world_apply(world, 'erosion', 'wind_x', 'gap')

def logic_11153(world):
    _world_apply(world, 'erosion', 'wind_y', 'square')

def logic_11154(world):
    _world_apply(world, 'erosion', 'vegetation', 'pulse')

def logic_11155(world):
    _world_apply(world, 'erosion', 'biomass', 'saturation')

def logic_11156(world):
    _world_apply(world, 'erosion', 'herbivore', 'gap')

def logic_11157(world):
    _world_apply(world, 'erosion', 'predator', 'direct')

def logic_11158(world):
    _world_apply(world, 'erosion', 'carrion', 'square')

def logic_11159(world):
    _world_apply(world, 'erosion', 'nutrients', 'pulse')

def logic_11160(world):
    _world_apply(world, 'erosion', 'decomposition_rate', 'saturation')

def logic_11161(world):
    _world_apply(world, 'erosion', 'oxygen', 'direct')

def logic_11162(world):
    _world_apply(world, 'erosion', 'co2', 'square')

def logic_11163(world):
    _world_apply(world, 'erosion', 'photosynthesis_factor', 'pulse')

def logic_11164(world):
    _world_apply(world, 'erosion', 'ice', 'saturation')

def logic_11165(world):
    _world_apply(world, 'erosion', 'evaporation', 'gap')

def logic_11166(world):
    _world_apply(world, 'erosion', 'detritus', 'direct')

def logic_11167(world):
    _world_apply(world, 'erosion', 'methane', 'square')

def logic_11168(world):
    _world_apply(world, 'erosion', 'pathogen_load', 'pulse')

def logic_11169(world):
    _world_apply(world, 'erosion', 'biodiversity', 'gap')

def logic_11170(world):
    _world_apply(world, 'erosion', 'habitat_stress', 'direct')

def logic_11171(world):
    _world_apply(world, 'erosion', 'soil_depth', 'square')

def logic_11172(world):
    _world_apply(world, 'erosion', 'root_density', 'pulse')

def logic_11173(world):
    _world_apply(world, 'erosion', 'wetland', 'saturation')

def logic_11174(world):
    _world_apply(world, 'erosion', 'carbon_storage', 'gap')

def logic_11175(world):
    _world_apply(world, 'erosion', 'fire_risk', 'direct')

def logic_11176(world):
    _world_apply(world, 'erosion', 'ash', 'square')

def logic_11177(world):
    _world_apply(world, 'erosion', 'snowpack', 'saturation')

def logic_11178(world):
    _world_apply(world, 'erosion', 'groundwater', 'gap')

def logic_11179(world):
    _world_apply(world, 'erosion', 'sediment', 'direct')

def logic_11180(world):
    _world_apply(world, 'erosion', 'salinity', 'square')

def logic_11181(world):
    _world_apply(world, 'erosion', 'algae', 'pulse')

def logic_11182(world):
    _world_apply(world, 'erosion', 'organic_matter', 'saturation')

def logic_11183(world):
    _world_apply(world, 'erosion', 'deadwood', 'gap')

def logic_11184(world):
    _world_apply(world, 'erosion', 'pollinators', 'direct')

def logic_11185(world):
    _world_apply(world, 'erosion', 'flowers', 'pulse')

def logic_11186(world):
    _world_apply(world, 'erosion', 'seed_bank', 'saturation')

def logic_11187(world):
    _world_apply(world, 'erosion', 'soil_carbon', 'gap')

def logic_11188(world):
    _world_apply(world, 'erosion', 'surface_ice', 'direct')

def logic_11189(world):
    _world_apply(world, 'soil_depth', 'temperature', 'square')

def logic_11190(world):
    _world_apply(world, 'soil_depth', 'surface_water', 'pulse')

def logic_11191(world):
    _world_apply(world, 'soil_depth', 'humidity', 'saturation')

def logic_11192(world):
    _world_apply(world, 'soil_depth', 'cloud', 'gap')

def logic_11193(world):
    _world_apply(world, 'soil_depth', 'rain', 'square')

def logic_11194(world):
    _world_apply(world, 'soil_depth', 'soil_moisture', 'pulse')

def logic_11195(world):
    _world_apply(world, 'soil_depth', 'runoff', 'saturation')

def logic_11196(world):
    _world_apply(world, 'soil_depth', 'wind_x', 'gap')

def logic_11197(world):
    _world_apply(world, 'soil_depth', 'wind_y', 'direct')

def logic_11198(world):
    _world_apply(world, 'soil_depth', 'vegetation', 'square')

def logic_11199(world):
    _world_apply(world, 'soil_depth', 'biomass', 'pulse')

def logic_11200(world):
    _world_apply(world, 'soil_depth', 'herbivore', 'saturation')

def logic_11201(world):
    _world_apply(world, 'soil_depth', 'predator', 'direct')

def logic_11202(world):
    _world_apply(world, 'soil_depth', 'carrion', 'square')

def logic_11203(world):
    _world_apply(world, 'soil_depth', 'nutrients', 'pulse')

def logic_11204(world):
    _world_apply(world, 'soil_depth', 'decomposition_rate', 'saturation')

def logic_11205(world):
    _world_apply(world, 'soil_depth', 'oxygen', 'gap')

def logic_11206(world):
    _world_apply(world, 'soil_depth', 'co2', 'direct')

def logic_11207(world):
    _world_apply(world, 'soil_depth', 'photosynthesis_factor', 'square')

def logic_11208(world):
    _world_apply(world, 'soil_depth', 'ice', 'pulse')

def logic_11209(world):
    _world_apply(world, 'soil_depth', 'evaporation', 'gap')

def logic_11210(world):
    _world_apply(world, 'soil_depth', 'detritus', 'direct')

def logic_11211(world):
    _world_apply(world, 'soil_depth', 'methane', 'square')

def logic_11212(world):
    _world_apply(world, 'soil_depth', 'pathogen_load', 'pulse')

def logic_11213(world):
    _world_apply(world, 'soil_depth', 'biodiversity', 'saturation')

def logic_11214(world):
    _world_apply(world, 'soil_depth', 'habitat_stress', 'gap')

def logic_11215(world):
    _world_apply(world, 'soil_depth', 'erosion', 'direct')

def logic_11216(world):
    _world_apply(world, 'soil_depth', 'root_density', 'square')

def logic_11217(world):
    _world_apply(world, 'soil_depth', 'wetland', 'saturation')

def logic_11218(world):
    _world_apply(world, 'soil_depth', 'carbon_storage', 'gap')

def logic_11219(world):
    _world_apply(world, 'soil_depth', 'fire_risk', 'direct')

def logic_11220(world):
    _world_apply(world, 'soil_depth', 'ash', 'square')

def logic_11221(world):
    _world_apply(world, 'soil_depth', 'snowpack', 'pulse')

def logic_11222(world):
    _world_apply(world, 'soil_depth', 'groundwater', 'saturation')

def logic_11223(world):
    _world_apply(world, 'soil_depth', 'sediment', 'gap')

def logic_11224(world):
    _world_apply(world, 'soil_depth', 'salinity', 'direct')

def logic_11225(world):
    _world_apply(world, 'soil_depth', 'algae', 'pulse')

def logic_11226(world):
    _world_apply(world, 'soil_depth', 'organic_matter', 'saturation')

def logic_11227(world):
    _world_apply(world, 'soil_depth', 'deadwood', 'gap')

def logic_11228(world):
    _world_apply(world, 'soil_depth', 'pollinators', 'direct')

def logic_11229(world):
    _world_apply(world, 'soil_depth', 'flowers', 'square')

def logic_11230(world):
    _world_apply(world, 'soil_depth', 'seed_bank', 'pulse')

def logic_11231(world):
    _world_apply(world, 'soil_depth', 'soil_carbon', 'saturation')

def logic_11232(world):
    _world_apply(world, 'soil_depth', 'surface_ice', 'gap')

def logic_11233(world):
    _world_apply(world, 'root_density', 'temperature', 'square')

def logic_11234(world):
    _world_apply(world, 'root_density', 'surface_water', 'pulse')

def logic_11235(world):
    _world_apply(world, 'root_density', 'humidity', 'saturation')

def logic_11236(world):
    _world_apply(world, 'root_density', 'cloud', 'gap')

def logic_11237(world):
    _world_apply(world, 'root_density', 'rain', 'direct')

def logic_11238(world):
    _world_apply(world, 'root_density', 'soil_moisture', 'square')

def logic_11239(world):
    _world_apply(world, 'root_density', 'runoff', 'pulse')

def logic_11240(world):
    _world_apply(world, 'root_density', 'wind_x', 'saturation')

def logic_11241(world):
    _world_apply(world, 'root_density', 'wind_y', 'direct')

def logic_11242(world):
    _world_apply(world, 'root_density', 'vegetation', 'square')

def logic_11243(world):
    _world_apply(world, 'root_density', 'biomass', 'pulse')

def logic_11244(world):
    _world_apply(world, 'root_density', 'herbivore', 'saturation')

def logic_11245(world):
    _world_apply(world, 'root_density', 'predator', 'gap')

def logic_11246(world):
    _world_apply(world, 'root_density', 'carrion', 'direct')

def logic_11247(world):
    _world_apply(world, 'root_density', 'nutrients', 'square')

def logic_11248(world):
    _world_apply(world, 'root_density', 'decomposition_rate', 'pulse')

def logic_11249(world):
    _world_apply(world, 'root_density', 'oxygen', 'gap')

def logic_11250(world):
    _world_apply(world, 'root_density', 'co2', 'direct')

def logic_11251(world):
    _world_apply(world, 'root_density', 'photosynthesis_factor', 'square')

def logic_11252(world):
    _world_apply(world, 'root_density', 'ice', 'pulse')

def logic_11253(world):
    _world_apply(world, 'root_density', 'evaporation', 'saturation')

def logic_11254(world):
    _world_apply(world, 'root_density', 'detritus', 'gap')

def logic_11255(world):
    _world_apply(world, 'root_density', 'methane', 'direct')

def logic_11256(world):
    _world_apply(world, 'root_density', 'pathogen_load', 'square')

def logic_11257(world):
    _world_apply(world, 'root_density', 'biodiversity', 'saturation')

def logic_11258(world):
    _world_apply(world, 'root_density', 'habitat_stress', 'gap')

def logic_11259(world):
    _world_apply(world, 'root_density', 'erosion', 'direct')

def logic_11260(world):
    _world_apply(world, 'root_density', 'soil_depth', 'square')

def logic_11261(world):
    _world_apply(world, 'root_density', 'wetland', 'pulse')

def logic_11262(world):
    _world_apply(world, 'root_density', 'carbon_storage', 'saturation')

def logic_11263(world):
    _world_apply(world, 'root_density', 'fire_risk', 'gap')

def logic_11264(world):
    _world_apply(world, 'root_density', 'ash', 'direct')

def logic_11265(world):
    _world_apply(world, 'root_density', 'snowpack', 'pulse')

def logic_11266(world):
    _world_apply(world, 'root_density', 'groundwater', 'saturation')

def logic_11267(world):
    _world_apply(world, 'root_density', 'sediment', 'gap')

def logic_11268(world):
    _world_apply(world, 'root_density', 'salinity', 'direct')

def logic_11269(world):
    _world_apply(world, 'root_density', 'algae', 'square')

def logic_11270(world):
    _world_apply(world, 'root_density', 'organic_matter', 'pulse')

def logic_11271(world):
    _world_apply(world, 'root_density', 'deadwood', 'saturation')

def logic_11272(world):
    _world_apply(world, 'root_density', 'pollinators', 'gap')

def logic_11273(world):
    _world_apply(world, 'root_density', 'flowers', 'square')

def logic_11274(world):
    _world_apply(world, 'root_density', 'seed_bank', 'pulse')

def logic_11275(world):
    _world_apply(world, 'root_density', 'soil_carbon', 'saturation')

def logic_11276(world):
    _world_apply(world, 'root_density', 'surface_ice', 'gap')

def logic_11277(world):
    _world_apply(world, 'wetland', 'temperature', 'direct')

def logic_11278(world):
    _world_apply(world, 'wetland', 'surface_water', 'square')

def logic_11279(world):
    _world_apply(world, 'wetland', 'humidity', 'pulse')

def logic_11280(world):
    _world_apply(world, 'wetland', 'cloud', 'saturation')

def logic_11281(world):
    _world_apply(world, 'wetland', 'rain', 'direct')

def logic_11282(world):
    _world_apply(world, 'wetland', 'soil_moisture', 'square')

def logic_11283(world):
    _world_apply(world, 'wetland', 'runoff', 'pulse')

def logic_11284(world):
    _world_apply(world, 'wetland', 'wind_x', 'saturation')

def logic_11285(world):
    _world_apply(world, 'wetland', 'wind_y', 'gap')

def logic_11286(world):
    _world_apply(world, 'wetland', 'vegetation', 'direct')

def logic_11287(world):
    _world_apply(world, 'wetland', 'biomass', 'square')

def logic_11288(world):
    _world_apply(world, 'wetland', 'herbivore', 'pulse')

def logic_11289(world):
    _world_apply(world, 'wetland', 'predator', 'gap')

def logic_11290(world):
    _world_apply(world, 'wetland', 'carrion', 'direct')

def logic_11291(world):
    _world_apply(world, 'wetland', 'nutrients', 'square')

def logic_11292(world):
    _world_apply(world, 'wetland', 'decomposition_rate', 'pulse')

def logic_11293(world):
    _world_apply(world, 'wetland', 'oxygen', 'saturation')

def logic_11294(world):
    _world_apply(world, 'wetland', 'co2', 'gap')

def logic_11295(world):
    _world_apply(world, 'wetland', 'photosynthesis_factor', 'direct')

def logic_11296(world):
    _world_apply(world, 'wetland', 'ice', 'square')

def logic_11297(world):
    _world_apply(world, 'wetland', 'evaporation', 'saturation')

def logic_11298(world):
    _world_apply(world, 'wetland', 'detritus', 'gap')

def logic_11299(world):
    _world_apply(world, 'wetland', 'methane', 'direct')

def logic_11300(world):
    _world_apply(world, 'wetland', 'pathogen_load', 'square')

def logic_11301(world):
    _world_apply(world, 'wetland', 'biodiversity', 'pulse')

def logic_11302(world):
    _world_apply(world, 'wetland', 'habitat_stress', 'saturation')

def logic_11303(world):
    _world_apply(world, 'wetland', 'erosion', 'gap')

def logic_11304(world):
    _world_apply(world, 'wetland', 'soil_depth', 'direct')

def logic_11305(world):
    _world_apply(world, 'wetland', 'root_density', 'pulse')

def logic_11306(world):
    _world_apply(world, 'wetland', 'carbon_storage', 'saturation')

def logic_11307(world):
    _world_apply(world, 'wetland', 'fire_risk', 'gap')

def logic_11308(world):
    _world_apply(world, 'wetland', 'ash', 'direct')

def logic_11309(world):
    _world_apply(world, 'wetland', 'snowpack', 'square')

def logic_11310(world):
    _world_apply(world, 'wetland', 'groundwater', 'pulse')

def logic_11311(world):
    _world_apply(world, 'wetland', 'sediment', 'saturation')

def logic_11312(world):
    _world_apply(world, 'wetland', 'salinity', 'gap')

def logic_11313(world):
    _world_apply(world, 'wetland', 'algae', 'square')

def logic_11314(world):
    _world_apply(world, 'wetland', 'organic_matter', 'pulse')

def logic_11315(world):
    _world_apply(world, 'wetland', 'deadwood', 'saturation')

def logic_11316(world):
    _world_apply(world, 'wetland', 'pollinators', 'gap')

def logic_11317(world):
    _world_apply(world, 'wetland', 'flowers', 'direct')

def logic_11318(world):
    _world_apply(world, 'wetland', 'seed_bank', 'square')

def logic_11319(world):
    _world_apply(world, 'wetland', 'soil_carbon', 'pulse')

def logic_11320(world):
    _world_apply(world, 'wetland', 'surface_ice', 'saturation')

def logic_11321(world):
    _world_apply(world, 'carbon_storage', 'temperature', 'direct')

def logic_11322(world):
    _world_apply(world, 'carbon_storage', 'surface_water', 'square')

def logic_11323(world):
    _world_apply(world, 'carbon_storage', 'humidity', 'pulse')

def logic_11324(world):
    _world_apply(world, 'carbon_storage', 'cloud', 'saturation')

def logic_11325(world):
    _world_apply(world, 'carbon_storage', 'rain', 'gap')

def logic_11326(world):
    _world_apply(world, 'carbon_storage', 'soil_moisture', 'direct')

def logic_11327(world):
    _world_apply(world, 'carbon_storage', 'runoff', 'square')

def logic_11328(world):
    _world_apply(world, 'carbon_storage', 'wind_x', 'pulse')

def logic_11329(world):
    _world_apply(world, 'carbon_storage', 'wind_y', 'gap')

def logic_11330(world):
    _world_apply(world, 'carbon_storage', 'vegetation', 'direct')

def logic_11331(world):
    _world_apply(world, 'carbon_storage', 'biomass', 'square')

def logic_11332(world):
    _world_apply(world, 'carbon_storage', 'herbivore', 'pulse')

def logic_11333(world):
    _world_apply(world, 'carbon_storage', 'predator', 'saturation')

def logic_11334(world):
    _world_apply(world, 'carbon_storage', 'carrion', 'gap')

def logic_11335(world):
    _world_apply(world, 'carbon_storage', 'nutrients', 'direct')

def logic_11336(world):
    _world_apply(world, 'carbon_storage', 'decomposition_rate', 'square')

def logic_11337(world):
    _world_apply(world, 'carbon_storage', 'oxygen', 'saturation')

def logic_11338(world):
    _world_apply(world, 'carbon_storage', 'co2', 'gap')

def logic_11339(world):
    _world_apply(world, 'carbon_storage', 'photosynthesis_factor', 'direct')

def logic_11340(world):
    _world_apply(world, 'carbon_storage', 'ice', 'square')

def logic_11341(world):
    _world_apply(world, 'carbon_storage', 'evaporation', 'pulse')

def logic_11342(world):
    _world_apply(world, 'carbon_storage', 'detritus', 'saturation')

def logic_11343(world):
    _world_apply(world, 'carbon_storage', 'methane', 'gap')

def logic_11344(world):
    _world_apply(world, 'carbon_storage', 'pathogen_load', 'direct')

def logic_11345(world):
    _world_apply(world, 'carbon_storage', 'biodiversity', 'pulse')

def logic_11346(world):
    _world_apply(world, 'carbon_storage', 'habitat_stress', 'saturation')

def logic_11347(world):
    _world_apply(world, 'carbon_storage', 'erosion', 'gap')

def logic_11348(world):
    _world_apply(world, 'carbon_storage', 'soil_depth', 'direct')

def logic_11349(world):
    _world_apply(world, 'carbon_storage', 'root_density', 'square')

def logic_11350(world):
    _world_apply(world, 'carbon_storage', 'wetland', 'pulse')

def logic_11351(world):
    _world_apply(world, 'carbon_storage', 'fire_risk', 'saturation')

def logic_11352(world):
    _world_apply(world, 'carbon_storage', 'ash', 'gap')

def logic_11353(world):
    _world_apply(world, 'carbon_storage', 'snowpack', 'square')

def logic_11354(world):
    _world_apply(world, 'carbon_storage', 'groundwater', 'pulse')

def logic_11355(world):
    _world_apply(world, 'carbon_storage', 'sediment', 'saturation')

def logic_11356(world):
    _world_apply(world, 'carbon_storage', 'salinity', 'gap')

def logic_11357(world):
    _world_apply(world, 'carbon_storage', 'algae', 'direct')

def logic_11358(world):
    _world_apply(world, 'carbon_storage', 'organic_matter', 'square')

def logic_11359(world):
    _world_apply(world, 'carbon_storage', 'deadwood', 'pulse')

def logic_11360(world):
    _world_apply(world, 'carbon_storage', 'pollinators', 'saturation')

def logic_11361(world):
    _world_apply(world, 'carbon_storage', 'flowers', 'direct')

def logic_11362(world):
    _world_apply(world, 'carbon_storage', 'seed_bank', 'square')

def logic_11363(world):
    _world_apply(world, 'carbon_storage', 'soil_carbon', 'pulse')

def logic_11364(world):
    _world_apply(world, 'carbon_storage', 'surface_ice', 'saturation')

def logic_11365(world):
    _world_apply(world, 'fire_risk', 'temperature', 'gap')

def logic_11366(world):
    _world_apply(world, 'fire_risk', 'surface_water', 'direct')

def logic_11367(world):
    _world_apply(world, 'fire_risk', 'humidity', 'square')

def logic_11368(world):
    _world_apply(world, 'fire_risk', 'cloud', 'pulse')

def logic_11369(world):
    _world_apply(world, 'fire_risk', 'rain', 'gap')

def logic_11370(world):
    _world_apply(world, 'fire_risk', 'soil_moisture', 'direct')

def logic_11371(world):
    _world_apply(world, 'fire_risk', 'runoff', 'square')

def logic_11372(world):
    _world_apply(world, 'fire_risk', 'wind_x', 'pulse')

def logic_11373(world):
    _world_apply(world, 'fire_risk', 'wind_y', 'saturation')

def logic_11374(world):
    _world_apply(world, 'fire_risk', 'vegetation', 'gap')

def logic_11375(world):
    _world_apply(world, 'fire_risk', 'biomass', 'direct')

def logic_11376(world):
    _world_apply(world, 'fire_risk', 'herbivore', 'square')

def logic_11377(world):
    _world_apply(world, 'fire_risk', 'predator', 'saturation')

def logic_11378(world):
    _world_apply(world, 'fire_risk', 'carrion', 'gap')

def logic_11379(world):
    _world_apply(world, 'fire_risk', 'nutrients', 'direct')

def logic_11380(world):
    _world_apply(world, 'fire_risk', 'decomposition_rate', 'square')

def logic_11381(world):
    _world_apply(world, 'fire_risk', 'oxygen', 'pulse')

def logic_11382(world):
    _world_apply(world, 'fire_risk', 'co2', 'saturation')

def logic_11383(world):
    _world_apply(world, 'fire_risk', 'photosynthesis_factor', 'gap')

def logic_11384(world):
    _world_apply(world, 'fire_risk', 'ice', 'direct')

def logic_11385(world):
    _world_apply(world, 'fire_risk', 'evaporation', 'pulse')

def logic_11386(world):
    _world_apply(world, 'fire_risk', 'detritus', 'saturation')

def logic_11387(world):
    _world_apply(world, 'fire_risk', 'methane', 'gap')

def logic_11388(world):
    _world_apply(world, 'fire_risk', 'pathogen_load', 'direct')

def logic_11389(world):
    _world_apply(world, 'fire_risk', 'biodiversity', 'square')

def logic_11390(world):
    _world_apply(world, 'fire_risk', 'habitat_stress', 'pulse')

def logic_11391(world):
    _world_apply(world, 'fire_risk', 'erosion', 'saturation')

def logic_11392(world):
    _world_apply(world, 'fire_risk', 'soil_depth', 'gap')

def logic_11393(world):
    _world_apply(world, 'fire_risk', 'root_density', 'square')

def logic_11394(world):
    _world_apply(world, 'fire_risk', 'wetland', 'pulse')

def logic_11395(world):
    _world_apply(world, 'fire_risk', 'carbon_storage', 'saturation')

def logic_11396(world):
    _world_apply(world, 'fire_risk', 'ash', 'gap')

def logic_11397(world):
    _world_apply(world, 'fire_risk', 'snowpack', 'direct')

def logic_11398(world):
    _world_apply(world, 'fire_risk', 'groundwater', 'square')

def logic_11399(world):
    _world_apply(world, 'fire_risk', 'sediment', 'pulse')

def logic_11400(world):
    _world_apply(world, 'fire_risk', 'salinity', 'saturation')

def logic_11401(world):
    _world_apply(world, 'fire_risk', 'algae', 'direct')

def logic_11402(world):
    _world_apply(world, 'fire_risk', 'organic_matter', 'square')

def logic_11403(world):
    _world_apply(world, 'fire_risk', 'deadwood', 'pulse')

def logic_11404(world):
    _world_apply(world, 'fire_risk', 'pollinators', 'saturation')

def logic_11405(world):
    _world_apply(world, 'fire_risk', 'flowers', 'gap')

def logic_11406(world):
    _world_apply(world, 'fire_risk', 'seed_bank', 'direct')

def logic_11407(world):
    _world_apply(world, 'fire_risk', 'soil_carbon', 'square')

def logic_11408(world):
    _world_apply(world, 'fire_risk', 'surface_ice', 'pulse')

def logic_11409(world):
    _world_apply(world, 'ash', 'temperature', 'gap')

def logic_11410(world):
    _world_apply(world, 'ash', 'surface_water', 'direct')

def logic_11411(world):
    _world_apply(world, 'ash', 'humidity', 'square')

def logic_11412(world):
    _world_apply(world, 'ash', 'cloud', 'pulse')

def logic_11413(world):
    _world_apply(world, 'ash', 'rain', 'saturation')

def logic_11414(world):
    _world_apply(world, 'ash', 'soil_moisture', 'gap')

def logic_11415(world):
    _world_apply(world, 'ash', 'runoff', 'direct')

def logic_11416(world):
    _world_apply(world, 'ash', 'wind_x', 'square')

def logic_11417(world):
    _world_apply(world, 'ash', 'wind_y', 'saturation')

def logic_11418(world):
    _world_apply(world, 'ash', 'vegetation', 'gap')

def logic_11419(world):
    _world_apply(world, 'ash', 'biomass', 'direct')

def logic_11420(world):
    _world_apply(world, 'ash', 'herbivore', 'square')

def logic_11421(world):
    _world_apply(world, 'ash', 'predator', 'pulse')

def logic_11422(world):
    _world_apply(world, 'ash', 'carrion', 'saturation')

def logic_11423(world):
    _world_apply(world, 'ash', 'nutrients', 'gap')

def logic_11424(world):
    _world_apply(world, 'ash', 'decomposition_rate', 'direct')

def logic_11425(world):
    _world_apply(world, 'ash', 'oxygen', 'pulse')

def logic_11426(world):
    _world_apply(world, 'ash', 'co2', 'saturation')

def logic_11427(world):
    _world_apply(world, 'ash', 'photosynthesis_factor', 'gap')

def logic_11428(world):
    _world_apply(world, 'ash', 'ice', 'direct')

def logic_11429(world):
    _world_apply(world, 'ash', 'evaporation', 'square')

def logic_11430(world):
    _world_apply(world, 'ash', 'detritus', 'pulse')

def logic_11431(world):
    _world_apply(world, 'ash', 'methane', 'saturation')

def logic_11432(world):
    _world_apply(world, 'ash', 'pathogen_load', 'gap')

def logic_11433(world):
    _world_apply(world, 'ash', 'biodiversity', 'square')

def logic_11434(world):
    _world_apply(world, 'ash', 'habitat_stress', 'pulse')

def logic_11435(world):
    _world_apply(world, 'ash', 'erosion', 'saturation')

def logic_11436(world):
    _world_apply(world, 'ash', 'soil_depth', 'gap')

def logic_11437(world):
    _world_apply(world, 'ash', 'root_density', 'direct')

def logic_11438(world):
    _world_apply(world, 'ash', 'wetland', 'square')

def logic_11439(world):
    _world_apply(world, 'ash', 'carbon_storage', 'pulse')

def logic_11440(world):
    _world_apply(world, 'ash', 'fire_risk', 'saturation')

def logic_11441(world):
    _world_apply(world, 'ash', 'snowpack', 'direct')

def logic_11442(world):
    _world_apply(world, 'ash', 'groundwater', 'square')

def logic_11443(world):
    _world_apply(world, 'ash', 'sediment', 'pulse')

def logic_11444(world):
    _world_apply(world, 'ash', 'salinity', 'saturation')

def logic_11445(world):
    _world_apply(world, 'ash', 'algae', 'gap')

def logic_11446(world):
    _world_apply(world, 'ash', 'organic_matter', 'direct')

def logic_11447(world):
    _world_apply(world, 'ash', 'deadwood', 'square')

def logic_11448(world):
    _world_apply(world, 'ash', 'pollinators', 'pulse')

def logic_11449(world):
    _world_apply(world, 'ash', 'flowers', 'gap')

def logic_11450(world):
    _world_apply(world, 'ash', 'seed_bank', 'direct')

def logic_11451(world):
    _world_apply(world, 'ash', 'soil_carbon', 'square')

def logic_11452(world):
    _world_apply(world, 'ash', 'surface_ice', 'pulse')

def logic_11453(world):
    _world_apply(world, 'snowpack', 'temperature', 'saturation')

def logic_11454(world):
    _world_apply(world, 'snowpack', 'surface_water', 'gap')

def logic_11455(world):
    _world_apply(world, 'snowpack', 'humidity', 'direct')

def logic_11456(world):
    _world_apply(world, 'snowpack', 'cloud', 'square')

def logic_11457(world):
    _world_apply(world, 'snowpack', 'rain', 'saturation')

def logic_11458(world):
    _world_apply(world, 'snowpack', 'soil_moisture', 'gap')

def logic_11459(world):
    _world_apply(world, 'snowpack', 'runoff', 'direct')

def logic_11460(world):
    _world_apply(world, 'snowpack', 'wind_x', 'square')

def logic_11461(world):
    _world_apply(world, 'snowpack', 'wind_y', 'pulse')

def logic_11462(world):
    _world_apply(world, 'snowpack', 'vegetation', 'saturation')

def logic_11463(world):
    _world_apply(world, 'snowpack', 'biomass', 'gap')

def logic_11464(world):
    _world_apply(world, 'snowpack', 'herbivore', 'direct')

def logic_11465(world):
    _world_apply(world, 'snowpack', 'predator', 'pulse')

def logic_11466(world):
    _world_apply(world, 'snowpack', 'carrion', 'saturation')

def logic_11467(world):
    _world_apply(world, 'snowpack', 'nutrients', 'gap')

def logic_11468(world):
    _world_apply(world, 'snowpack', 'decomposition_rate', 'direct')

def logic_11469(world):
    _world_apply(world, 'snowpack', 'oxygen', 'square')

def logic_11470(world):
    _world_apply(world, 'snowpack', 'co2', 'pulse')

def logic_11471(world):
    _world_apply(world, 'snowpack', 'photosynthesis_factor', 'saturation')

def logic_11472(world):
    _world_apply(world, 'snowpack', 'ice', 'gap')

def logic_11473(world):
    _world_apply(world, 'snowpack', 'evaporation', 'square')

def logic_11474(world):
    _world_apply(world, 'snowpack', 'detritus', 'pulse')

def logic_11475(world):
    _world_apply(world, 'snowpack', 'methane', 'saturation')

def logic_11476(world):
    _world_apply(world, 'snowpack', 'pathogen_load', 'gap')

def logic_11477(world):
    _world_apply(world, 'snowpack', 'biodiversity', 'direct')

def logic_11478(world):
    _world_apply(world, 'snowpack', 'habitat_stress', 'square')

def logic_11479(world):
    _world_apply(world, 'snowpack', 'erosion', 'pulse')

def logic_11480(world):
    _world_apply(world, 'snowpack', 'soil_depth', 'saturation')

def logic_11481(world):
    _world_apply(world, 'snowpack', 'root_density', 'direct')

def logic_11482(world):
    _world_apply(world, 'snowpack', 'wetland', 'square')

def logic_11483(world):
    _world_apply(world, 'snowpack', 'carbon_storage', 'pulse')

def logic_11484(world):
    _world_apply(world, 'snowpack', 'fire_risk', 'saturation')

def logic_11485(world):
    _world_apply(world, 'snowpack', 'ash', 'gap')

def logic_11486(world):
    _world_apply(world, 'snowpack', 'groundwater', 'direct')

def logic_11487(world):
    _world_apply(world, 'snowpack', 'sediment', 'square')

def logic_11488(world):
    _world_apply(world, 'snowpack', 'salinity', 'pulse')

def logic_11489(world):
    _world_apply(world, 'snowpack', 'algae', 'gap')

def logic_11490(world):
    _world_apply(world, 'snowpack', 'organic_matter', 'direct')

def logic_11491(world):
    _world_apply(world, 'snowpack', 'deadwood', 'square')

def logic_11492(world):
    _world_apply(world, 'snowpack', 'pollinators', 'pulse')

def logic_11493(world):
    _world_apply(world, 'snowpack', 'flowers', 'saturation')

def logic_11494(world):
    _world_apply(world, 'snowpack', 'seed_bank', 'gap')

def logic_11495(world):
    _world_apply(world, 'snowpack', 'soil_carbon', 'direct')

def logic_11496(world):
    _world_apply(world, 'snowpack', 'surface_ice', 'square')

def logic_11497(world):
    _world_apply(world, 'groundwater', 'temperature', 'saturation')

def logic_11498(world):
    _world_apply(world, 'groundwater', 'surface_water', 'gap')

def logic_11499(world):
    _world_apply(world, 'groundwater', 'humidity', 'direct')

def logic_11500(world):
    _world_apply(world, 'groundwater', 'cloud', 'square')

def logic_11501(world):
    _world_apply(world, 'groundwater', 'rain', 'pulse')

def logic_11502(world):
    _world_apply(world, 'groundwater', 'soil_moisture', 'saturation')

def logic_11503(world):
    _world_apply(world, 'groundwater', 'runoff', 'gap')

def logic_11504(world):
    _world_apply(world, 'groundwater', 'wind_x', 'direct')

def logic_11505(world):
    _world_apply(world, 'groundwater', 'wind_y', 'pulse')

def logic_11506(world):
    _world_apply(world, 'groundwater', 'vegetation', 'saturation')

def logic_11507(world):
    _world_apply(world, 'groundwater', 'biomass', 'gap')

def logic_11508(world):
    _world_apply(world, 'groundwater', 'herbivore', 'direct')

def logic_11509(world):
    _world_apply(world, 'groundwater', 'predator', 'square')

def logic_11510(world):
    _world_apply(world, 'groundwater', 'carrion', 'pulse')

def logic_11511(world):
    _world_apply(world, 'groundwater', 'nutrients', 'saturation')

def logic_11512(world):
    _world_apply(world, 'groundwater', 'decomposition_rate', 'gap')

def logic_11513(world):
    _world_apply(world, 'groundwater', 'oxygen', 'square')

def logic_11514(world):
    _world_apply(world, 'groundwater', 'co2', 'pulse')

def logic_11515(world):
    _world_apply(world, 'groundwater', 'photosynthesis_factor', 'saturation')

def logic_11516(world):
    _world_apply(world, 'groundwater', 'ice', 'gap')

def logic_11517(world):
    _world_apply(world, 'groundwater', 'evaporation', 'direct')

def logic_11518(world):
    _world_apply(world, 'groundwater', 'detritus', 'square')

def logic_11519(world):
    _world_apply(world, 'groundwater', 'methane', 'pulse')

def logic_11520(world):
    _world_apply(world, 'groundwater', 'pathogen_load', 'saturation')

def logic_11521(world):
    _world_apply(world, 'groundwater', 'biodiversity', 'direct')

def logic_11522(world):
    _world_apply(world, 'groundwater', 'habitat_stress', 'square')

def logic_11523(world):
    _world_apply(world, 'groundwater', 'erosion', 'pulse')

def logic_11524(world):
    _world_apply(world, 'groundwater', 'soil_depth', 'saturation')

def logic_11525(world):
    _world_apply(world, 'groundwater', 'root_density', 'gap')

def logic_11526(world):
    _world_apply(world, 'groundwater', 'wetland', 'direct')

def logic_11527(world):
    _world_apply(world, 'groundwater', 'carbon_storage', 'square')

def logic_11528(world):
    _world_apply(world, 'groundwater', 'fire_risk', 'pulse')

def logic_11529(world):
    _world_apply(world, 'groundwater', 'ash', 'gap')

def logic_11530(world):
    _world_apply(world, 'groundwater', 'snowpack', 'direct')

def logic_11531(world):
    _world_apply(world, 'groundwater', 'sediment', 'square')

def logic_11532(world):
    _world_apply(world, 'groundwater', 'salinity', 'pulse')

def logic_11533(world):
    _world_apply(world, 'groundwater', 'algae', 'saturation')

def logic_11534(world):
    _world_apply(world, 'groundwater', 'organic_matter', 'gap')

def logic_11535(world):
    _world_apply(world, 'groundwater', 'deadwood', 'direct')

def logic_11536(world):
    _world_apply(world, 'groundwater', 'pollinators', 'square')

def logic_11537(world):
    _world_apply(world, 'groundwater', 'flowers', 'saturation')

def logic_11538(world):
    _world_apply(world, 'groundwater', 'seed_bank', 'gap')

def logic_11539(world):
    _world_apply(world, 'groundwater', 'soil_carbon', 'direct')

def logic_11540(world):
    _world_apply(world, 'groundwater', 'surface_ice', 'square')

def logic_11541(world):
    _world_apply(world, 'sediment', 'temperature', 'pulse')

def logic_11542(world):
    _world_apply(world, 'sediment', 'surface_water', 'saturation')

def logic_11543(world):
    _world_apply(world, 'sediment', 'humidity', 'gap')

def logic_11544(world):
    _world_apply(world, 'sediment', 'cloud', 'direct')

def logic_11545(world):
    _world_apply(world, 'sediment', 'rain', 'pulse')

def logic_11546(world):
    _world_apply(world, 'sediment', 'soil_moisture', 'saturation')

def logic_11547(world):
    _world_apply(world, 'sediment', 'runoff', 'gap')

def logic_11548(world):
    _world_apply(world, 'sediment', 'wind_x', 'direct')

def logic_11549(world):
    _world_apply(world, 'sediment', 'wind_y', 'square')

def logic_11550(world):
    _world_apply(world, 'sediment', 'vegetation', 'pulse')

def logic_11551(world):
    _world_apply(world, 'sediment', 'biomass', 'saturation')

def logic_11552(world):
    _world_apply(world, 'sediment', 'herbivore', 'gap')

def logic_11553(world):
    _world_apply(world, 'sediment', 'predator', 'square')

def logic_11554(world):
    _world_apply(world, 'sediment', 'carrion', 'pulse')

def logic_11555(world):
    _world_apply(world, 'sediment', 'nutrients', 'saturation')

def logic_11556(world):
    _world_apply(world, 'sediment', 'decomposition_rate', 'gap')

def logic_11557(world):
    _world_apply(world, 'sediment', 'oxygen', 'direct')

def logic_11558(world):
    _world_apply(world, 'sediment', 'co2', 'square')

def logic_11559(world):
    _world_apply(world, 'sediment', 'photosynthesis_factor', 'pulse')

def logic_11560(world):
    _world_apply(world, 'sediment', 'ice', 'saturation')

def logic_11561(world):
    _world_apply(world, 'sediment', 'evaporation', 'direct')

def logic_11562(world):
    _world_apply(world, 'sediment', 'detritus', 'square')

def logic_11563(world):
    _world_apply(world, 'sediment', 'methane', 'pulse')

def logic_11564(world):
    _world_apply(world, 'sediment', 'pathogen_load', 'saturation')

def logic_11565(world):
    _world_apply(world, 'sediment', 'biodiversity', 'gap')

def logic_11566(world):
    _world_apply(world, 'sediment', 'habitat_stress', 'direct')

def logic_11567(world):
    _world_apply(world, 'sediment', 'erosion', 'square')

def logic_11568(world):
    _world_apply(world, 'sediment', 'soil_depth', 'pulse')

def logic_11569(world):
    _world_apply(world, 'sediment', 'root_density', 'gap')

def logic_11570(world):
    _world_apply(world, 'sediment', 'wetland', 'direct')

def logic_11571(world):
    _world_apply(world, 'sediment', 'carbon_storage', 'square')

def logic_11572(world):
    _world_apply(world, 'sediment', 'fire_risk', 'pulse')

def logic_11573(world):
    _world_apply(world, 'sediment', 'ash', 'saturation')

def logic_11574(world):
    _world_apply(world, 'sediment', 'snowpack', 'gap')

def logic_11575(world):
    _world_apply(world, 'sediment', 'groundwater', 'direct')

def logic_11576(world):
    _world_apply(world, 'sediment', 'salinity', 'square')

def logic_11577(world):
    _world_apply(world, 'sediment', 'algae', 'saturation')

def logic_11578(world):
    _world_apply(world, 'sediment', 'organic_matter', 'gap')

def logic_11579(world):
    _world_apply(world, 'sediment', 'deadwood', 'direct')

def logic_11580(world):
    _world_apply(world, 'sediment', 'pollinators', 'square')

def logic_11581(world):
    _world_apply(world, 'sediment', 'flowers', 'pulse')

def logic_11582(world):
    _world_apply(world, 'sediment', 'seed_bank', 'saturation')

def logic_11583(world):
    _world_apply(world, 'sediment', 'soil_carbon', 'gap')

def logic_11584(world):
    _world_apply(world, 'sediment', 'surface_ice', 'direct')

def logic_11585(world):
    _world_apply(world, 'salinity', 'temperature', 'pulse')

def logic_11586(world):
    _world_apply(world, 'salinity', 'surface_water', 'saturation')

def logic_11587(world):
    _world_apply(world, 'salinity', 'humidity', 'gap')

def logic_11588(world):
    _world_apply(world, 'salinity', 'cloud', 'direct')

def logic_11589(world):
    _world_apply(world, 'salinity', 'rain', 'square')

def logic_11590(world):
    _world_apply(world, 'salinity', 'soil_moisture', 'pulse')

def logic_11591(world):
    _world_apply(world, 'salinity', 'runoff', 'saturation')

def logic_11592(world):
    _world_apply(world, 'salinity', 'wind_x', 'gap')

def logic_11593(world):
    _world_apply(world, 'salinity', 'wind_y', 'square')

def logic_11594(world):
    _world_apply(world, 'salinity', 'vegetation', 'pulse')

def logic_11595(world):
    _world_apply(world, 'salinity', 'biomass', 'saturation')

def logic_11596(world):
    _world_apply(world, 'salinity', 'herbivore', 'gap')

def logic_11597(world):
    _world_apply(world, 'salinity', 'predator', 'direct')

def logic_11598(world):
    _world_apply(world, 'salinity', 'carrion', 'square')

def logic_11599(world):
    _world_apply(world, 'salinity', 'nutrients', 'pulse')

def logic_11600(world):
    _world_apply(world, 'salinity', 'decomposition_rate', 'saturation')

def logic_11601(world):
    _world_apply(world, 'salinity', 'oxygen', 'direct')

def logic_11602(world):
    _world_apply(world, 'salinity', 'co2', 'square')

def logic_11603(world):
    _world_apply(world, 'salinity', 'photosynthesis_factor', 'pulse')
