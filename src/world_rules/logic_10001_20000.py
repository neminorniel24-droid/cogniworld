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

def logic_11604(world):
    _world_apply(world, 'salinity', 'ice', 'saturation')

def logic_11605(world):
    _world_apply(world, 'salinity', 'evaporation', 'gap')

def logic_11606(world):
    _world_apply(world, 'salinity', 'detritus', 'direct')

def logic_11607(world):
    _world_apply(world, 'salinity', 'methane', 'square')

def logic_11608(world):
    _world_apply(world, 'salinity', 'pathogen_load', 'pulse')

def logic_11609(world):
    _world_apply(world, 'salinity', 'biodiversity', 'gap')

def logic_11610(world):
    _world_apply(world, 'salinity', 'habitat_stress', 'direct')

def logic_11611(world):
    _world_apply(world, 'salinity', 'erosion', 'square')

def logic_11612(world):
    _world_apply(world, 'salinity', 'soil_depth', 'pulse')

def logic_11613(world):
    _world_apply(world, 'salinity', 'root_density', 'saturation')

def logic_11614(world):
    _world_apply(world, 'salinity', 'wetland', 'gap')

def logic_11615(world):
    _world_apply(world, 'salinity', 'carbon_storage', 'direct')

def logic_11616(world):
    _world_apply(world, 'salinity', 'fire_risk', 'square')

def logic_11617(world):
    _world_apply(world, 'salinity', 'ash', 'saturation')

def logic_11618(world):
    _world_apply(world, 'salinity', 'snowpack', 'gap')

def logic_11619(world):
    _world_apply(world, 'salinity', 'groundwater', 'direct')

def logic_11620(world):
    _world_apply(world, 'salinity', 'sediment', 'square')

def logic_11621(world):
    _world_apply(world, 'salinity', 'algae', 'pulse')

def logic_11622(world):
    _world_apply(world, 'salinity', 'organic_matter', 'saturation')

def logic_11623(world):
    _world_apply(world, 'salinity', 'deadwood', 'gap')

def logic_11624(world):
    _world_apply(world, 'salinity', 'pollinators', 'direct')

def logic_11625(world):
    _world_apply(world, 'salinity', 'flowers', 'pulse')

def logic_11626(world):
    _world_apply(world, 'salinity', 'seed_bank', 'saturation')

def logic_11627(world):
    _world_apply(world, 'salinity', 'soil_carbon', 'gap')

def logic_11628(world):
    _world_apply(world, 'salinity', 'surface_ice', 'direct')

def logic_11629(world):
    _world_apply(world, 'algae', 'temperature', 'square')

def logic_11630(world):
    _world_apply(world, 'algae', 'surface_water', 'pulse')

def logic_11631(world):
    _world_apply(world, 'algae', 'humidity', 'saturation')

def logic_11632(world):
    _world_apply(world, 'algae', 'cloud', 'gap')

def logic_11633(world):
    _world_apply(world, 'algae', 'rain', 'square')

def logic_11634(world):
    _world_apply(world, 'algae', 'soil_moisture', 'pulse')

def logic_11635(world):
    _world_apply(world, 'algae', 'runoff', 'saturation')

def logic_11636(world):
    _world_apply(world, 'algae', 'wind_x', 'gap')

def logic_11637(world):
    _world_apply(world, 'algae', 'wind_y', 'direct')

def logic_11638(world):
    _world_apply(world, 'algae', 'vegetation', 'square')

def logic_11639(world):
    _world_apply(world, 'algae', 'biomass', 'pulse')

def logic_11640(world):
    _world_apply(world, 'algae', 'herbivore', 'saturation')

def logic_11641(world):
    _world_apply(world, 'algae', 'predator', 'direct')

def logic_11642(world):
    _world_apply(world, 'algae', 'carrion', 'square')

def logic_11643(world):
    _world_apply(world, 'algae', 'nutrients', 'pulse')

def logic_11644(world):
    _world_apply(world, 'algae', 'decomposition_rate', 'saturation')

def logic_11645(world):
    _world_apply(world, 'algae', 'oxygen', 'gap')

def logic_11646(world):
    _world_apply(world, 'algae', 'co2', 'direct')

def logic_11647(world):
    _world_apply(world, 'algae', 'photosynthesis_factor', 'square')

def logic_11648(world):
    _world_apply(world, 'algae', 'ice', 'pulse')

def logic_11649(world):
    _world_apply(world, 'algae', 'evaporation', 'gap')

def logic_11650(world):
    _world_apply(world, 'algae', 'detritus', 'direct')

def logic_11651(world):
    _world_apply(world, 'algae', 'methane', 'square')

def logic_11652(world):
    _world_apply(world, 'algae', 'pathogen_load', 'pulse')

def logic_11653(world):
    _world_apply(world, 'algae', 'biodiversity', 'saturation')

def logic_11654(world):
    _world_apply(world, 'algae', 'habitat_stress', 'gap')

def logic_11655(world):
    _world_apply(world, 'algae', 'erosion', 'direct')

def logic_11656(world):
    _world_apply(world, 'algae', 'soil_depth', 'square')

def logic_11657(world):
    _world_apply(world, 'algae', 'root_density', 'saturation')

def logic_11658(world):
    _world_apply(world, 'algae', 'wetland', 'gap')

def logic_11659(world):
    _world_apply(world, 'algae', 'carbon_storage', 'direct')

def logic_11660(world):
    _world_apply(world, 'algae', 'fire_risk', 'square')

def logic_11661(world):
    _world_apply(world, 'algae', 'ash', 'pulse')

def logic_11662(world):
    _world_apply(world, 'algae', 'snowpack', 'saturation')

def logic_11663(world):
    _world_apply(world, 'algae', 'groundwater', 'gap')

def logic_11664(world):
    _world_apply(world, 'algae', 'sediment', 'direct')

def logic_11665(world):
    _world_apply(world, 'algae', 'salinity', 'pulse')

def logic_11666(world):
    _world_apply(world, 'algae', 'organic_matter', 'saturation')

def logic_11667(world):
    _world_apply(world, 'algae', 'deadwood', 'gap')

def logic_11668(world):
    _world_apply(world, 'algae', 'pollinators', 'direct')

def logic_11669(world):
    _world_apply(world, 'algae', 'flowers', 'square')

def logic_11670(world):
    _world_apply(world, 'algae', 'seed_bank', 'pulse')

def logic_11671(world):
    _world_apply(world, 'algae', 'soil_carbon', 'saturation')

def logic_11672(world):
    _world_apply(world, 'algae', 'surface_ice', 'gap')

def logic_11673(world):
    _world_apply(world, 'organic_matter', 'temperature', 'square')

def logic_11674(world):
    _world_apply(world, 'organic_matter', 'surface_water', 'pulse')

def logic_11675(world):
    _world_apply(world, 'organic_matter', 'humidity', 'saturation')

def logic_11676(world):
    _world_apply(world, 'organic_matter', 'cloud', 'gap')

def logic_11677(world):
    _world_apply(world, 'organic_matter', 'rain', 'direct')

def logic_11678(world):
    _world_apply(world, 'organic_matter', 'soil_moisture', 'square')

def logic_11679(world):
    _world_apply(world, 'organic_matter', 'runoff', 'pulse')

def logic_11680(world):
    _world_apply(world, 'organic_matter', 'wind_x', 'saturation')

def logic_11681(world):
    _world_apply(world, 'organic_matter', 'wind_y', 'direct')

def logic_11682(world):
    _world_apply(world, 'organic_matter', 'vegetation', 'square')

def logic_11683(world):
    _world_apply(world, 'organic_matter', 'biomass', 'pulse')

def logic_11684(world):
    _world_apply(world, 'organic_matter', 'herbivore', 'saturation')

def logic_11685(world):
    _world_apply(world, 'organic_matter', 'predator', 'gap')

def logic_11686(world):
    _world_apply(world, 'organic_matter', 'carrion', 'direct')

def logic_11687(world):
    _world_apply(world, 'organic_matter', 'nutrients', 'square')

def logic_11688(world):
    _world_apply(world, 'organic_matter', 'decomposition_rate', 'pulse')

def logic_11689(world):
    _world_apply(world, 'organic_matter', 'oxygen', 'gap')

def logic_11690(world):
    _world_apply(world, 'organic_matter', 'co2', 'direct')

def logic_11691(world):
    _world_apply(world, 'organic_matter', 'photosynthesis_factor', 'square')

def logic_11692(world):
    _world_apply(world, 'organic_matter', 'ice', 'pulse')

def logic_11693(world):
    _world_apply(world, 'organic_matter', 'evaporation', 'saturation')

def logic_11694(world):
    _world_apply(world, 'organic_matter', 'detritus', 'gap')

def logic_11695(world):
    _world_apply(world, 'organic_matter', 'methane', 'direct')

def logic_11696(world):
    _world_apply(world, 'organic_matter', 'pathogen_load', 'square')

def logic_11697(world):
    _world_apply(world, 'organic_matter', 'biodiversity', 'saturation')

def logic_11698(world):
    _world_apply(world, 'organic_matter', 'habitat_stress', 'gap')

def logic_11699(world):
    _world_apply(world, 'organic_matter', 'erosion', 'direct')

def logic_11700(world):
    _world_apply(world, 'organic_matter', 'soil_depth', 'square')

def logic_11701(world):
    _world_apply(world, 'organic_matter', 'root_density', 'pulse')

def logic_11702(world):
    _world_apply(world, 'organic_matter', 'wetland', 'saturation')

def logic_11703(world):
    _world_apply(world, 'organic_matter', 'carbon_storage', 'gap')

def logic_11704(world):
    _world_apply(world, 'organic_matter', 'fire_risk', 'direct')

def logic_11705(world):
    _world_apply(world, 'organic_matter', 'ash', 'pulse')

def logic_11706(world):
    _world_apply(world, 'organic_matter', 'snowpack', 'saturation')

def logic_11707(world):
    _world_apply(world, 'organic_matter', 'groundwater', 'gap')

def logic_11708(world):
    _world_apply(world, 'organic_matter', 'sediment', 'direct')

def logic_11709(world):
    _world_apply(world, 'organic_matter', 'salinity', 'square')

def logic_11710(world):
    _world_apply(world, 'organic_matter', 'algae', 'pulse')

def logic_11711(world):
    _world_apply(world, 'organic_matter', 'deadwood', 'saturation')

def logic_11712(world):
    _world_apply(world, 'organic_matter', 'pollinators', 'gap')

def logic_11713(world):
    _world_apply(world, 'organic_matter', 'flowers', 'square')

def logic_11714(world):
    _world_apply(world, 'organic_matter', 'seed_bank', 'pulse')

def logic_11715(world):
    _world_apply(world, 'organic_matter', 'soil_carbon', 'saturation')

def logic_11716(world):
    _world_apply(world, 'organic_matter', 'surface_ice', 'gap')

def logic_11717(world):
    _world_apply(world, 'deadwood', 'temperature', 'direct')

def logic_11718(world):
    _world_apply(world, 'deadwood', 'surface_water', 'square')

def logic_11719(world):
    _world_apply(world, 'deadwood', 'humidity', 'pulse')

def logic_11720(world):
    _world_apply(world, 'deadwood', 'cloud', 'saturation')

def logic_11721(world):
    _world_apply(world, 'deadwood', 'rain', 'direct')

def logic_11722(world):
    _world_apply(world, 'deadwood', 'soil_moisture', 'square')

def logic_11723(world):
    _world_apply(world, 'deadwood', 'runoff', 'pulse')

def logic_11724(world):
    _world_apply(world, 'deadwood', 'wind_x', 'saturation')

def logic_11725(world):
    _world_apply(world, 'deadwood', 'wind_y', 'gap')

def logic_11726(world):
    _world_apply(world, 'deadwood', 'vegetation', 'direct')

def logic_11727(world):
    _world_apply(world, 'deadwood', 'biomass', 'square')

def logic_11728(world):
    _world_apply(world, 'deadwood', 'herbivore', 'pulse')

def logic_11729(world):
    _world_apply(world, 'deadwood', 'predator', 'gap')

def logic_11730(world):
    _world_apply(world, 'deadwood', 'carrion', 'direct')

def logic_11731(world):
    _world_apply(world, 'deadwood', 'nutrients', 'square')

def logic_11732(world):
    _world_apply(world, 'deadwood', 'decomposition_rate', 'pulse')

def logic_11733(world):
    _world_apply(world, 'deadwood', 'oxygen', 'saturation')

def logic_11734(world):
    _world_apply(world, 'deadwood', 'co2', 'gap')

def logic_11735(world):
    _world_apply(world, 'deadwood', 'photosynthesis_factor', 'direct')

def logic_11736(world):
    _world_apply(world, 'deadwood', 'ice', 'square')

def logic_11737(world):
    _world_apply(world, 'deadwood', 'evaporation', 'saturation')

def logic_11738(world):
    _world_apply(world, 'deadwood', 'detritus', 'gap')

def logic_11739(world):
    _world_apply(world, 'deadwood', 'methane', 'direct')

def logic_11740(world):
    _world_apply(world, 'deadwood', 'pathogen_load', 'square')

def logic_11741(world):
    _world_apply(world, 'deadwood', 'biodiversity', 'pulse')

def logic_11742(world):
    _world_apply(world, 'deadwood', 'habitat_stress', 'saturation')

def logic_11743(world):
    _world_apply(world, 'deadwood', 'erosion', 'gap')

def logic_11744(world):
    _world_apply(world, 'deadwood', 'soil_depth', 'direct')

def logic_11745(world):
    _world_apply(world, 'deadwood', 'root_density', 'pulse')

def logic_11746(world):
    _world_apply(world, 'deadwood', 'wetland', 'saturation')

def logic_11747(world):
    _world_apply(world, 'deadwood', 'carbon_storage', 'gap')

def logic_11748(world):
    _world_apply(world, 'deadwood', 'fire_risk', 'direct')

def logic_11749(world):
    _world_apply(world, 'deadwood', 'ash', 'square')

def logic_11750(world):
    _world_apply(world, 'deadwood', 'snowpack', 'pulse')

def logic_11751(world):
    _world_apply(world, 'deadwood', 'groundwater', 'saturation')

def logic_11752(world):
    _world_apply(world, 'deadwood', 'sediment', 'gap')

def logic_11753(world):
    _world_apply(world, 'deadwood', 'salinity', 'square')

def logic_11754(world):
    _world_apply(world, 'deadwood', 'algae', 'pulse')

def logic_11755(world):
    _world_apply(world, 'deadwood', 'organic_matter', 'saturation')

def logic_11756(world):
    _world_apply(world, 'deadwood', 'pollinators', 'gap')

def logic_11757(world):
    _world_apply(world, 'deadwood', 'flowers', 'direct')

def logic_11758(world):
    _world_apply(world, 'deadwood', 'seed_bank', 'square')

def logic_11759(world):
    _world_apply(world, 'deadwood', 'soil_carbon', 'pulse')

def logic_11760(world):
    _world_apply(world, 'deadwood', 'surface_ice', 'saturation')

def logic_11761(world):
    _world_apply(world, 'pollinators', 'temperature', 'direct')

def logic_11762(world):
    _world_apply(world, 'pollinators', 'surface_water', 'square')

def logic_11763(world):
    _world_apply(world, 'pollinators', 'humidity', 'pulse')

def logic_11764(world):
    _world_apply(world, 'pollinators', 'cloud', 'saturation')

def logic_11765(world):
    _world_apply(world, 'pollinators', 'rain', 'gap')

def logic_11766(world):
    _world_apply(world, 'pollinators', 'soil_moisture', 'direct')

def logic_11767(world):
    _world_apply(world, 'pollinators', 'runoff', 'square')

def logic_11768(world):
    _world_apply(world, 'pollinators', 'wind_x', 'pulse')

def logic_11769(world):
    _world_apply(world, 'pollinators', 'wind_y', 'gap')

def logic_11770(world):
    _world_apply(world, 'pollinators', 'vegetation', 'direct')

def logic_11771(world):
    _world_apply(world, 'pollinators', 'biomass', 'square')

def logic_11772(world):
    _world_apply(world, 'pollinators', 'herbivore', 'pulse')

def logic_11773(world):
    _world_apply(world, 'pollinators', 'predator', 'saturation')

def logic_11774(world):
    _world_apply(world, 'pollinators', 'carrion', 'gap')

def logic_11775(world):
    _world_apply(world, 'pollinators', 'nutrients', 'direct')

def logic_11776(world):
    _world_apply(world, 'pollinators', 'decomposition_rate', 'square')

def logic_11777(world):
    _world_apply(world, 'pollinators', 'oxygen', 'saturation')

def logic_11778(world):
    _world_apply(world, 'pollinators', 'co2', 'gap')

def logic_11779(world):
    _world_apply(world, 'pollinators', 'photosynthesis_factor', 'direct')

def logic_11780(world):
    _world_apply(world, 'pollinators', 'ice', 'square')

def logic_11781(world):
    _world_apply(world, 'pollinators', 'evaporation', 'pulse')

def logic_11782(world):
    _world_apply(world, 'pollinators', 'detritus', 'saturation')

def logic_11783(world):
    _world_apply(world, 'pollinators', 'methane', 'gap')

def logic_11784(world):
    _world_apply(world, 'pollinators', 'pathogen_load', 'direct')

def logic_11785(world):
    _world_apply(world, 'pollinators', 'biodiversity', 'pulse')

def logic_11786(world):
    _world_apply(world, 'pollinators', 'habitat_stress', 'saturation')

def logic_11787(world):
    _world_apply(world, 'pollinators', 'erosion', 'gap')

def logic_11788(world):
    _world_apply(world, 'pollinators', 'soil_depth', 'direct')

def logic_11789(world):
    _world_apply(world, 'pollinators', 'root_density', 'square')

def logic_11790(world):
    _world_apply(world, 'pollinators', 'wetland', 'pulse')

def logic_11791(world):
    _world_apply(world, 'pollinators', 'carbon_storage', 'saturation')

def logic_11792(world):
    _world_apply(world, 'pollinators', 'fire_risk', 'gap')

def logic_11793(world):
    _world_apply(world, 'pollinators', 'ash', 'square')

def logic_11794(world):
    _world_apply(world, 'pollinators', 'snowpack', 'pulse')

def logic_11795(world):
    _world_apply(world, 'pollinators', 'groundwater', 'saturation')

def logic_11796(world):
    _world_apply(world, 'pollinators', 'sediment', 'gap')

def logic_11797(world):
    _world_apply(world, 'pollinators', 'salinity', 'direct')

def logic_11798(world):
    _world_apply(world, 'pollinators', 'algae', 'square')

def logic_11799(world):
    _world_apply(world, 'pollinators', 'organic_matter', 'pulse')

def logic_11800(world):
    _world_apply(world, 'pollinators', 'deadwood', 'saturation')

def logic_11801(world):
    _world_apply(world, 'pollinators', 'flowers', 'direct')

def logic_11802(world):
    _world_apply(world, 'pollinators', 'seed_bank', 'square')

def logic_11803(world):
    _world_apply(world, 'pollinators', 'soil_carbon', 'pulse')

def logic_11804(world):
    _world_apply(world, 'pollinators', 'surface_ice', 'saturation')

def logic_11805(world):
    _world_apply(world, 'flowers', 'temperature', 'gap')

def logic_11806(world):
    _world_apply(world, 'flowers', 'surface_water', 'direct')

def logic_11807(world):
    _world_apply(world, 'flowers', 'humidity', 'square')

def logic_11808(world):
    _world_apply(world, 'flowers', 'cloud', 'pulse')

def logic_11809(world):
    _world_apply(world, 'flowers', 'rain', 'gap')

def logic_11810(world):
    _world_apply(world, 'flowers', 'soil_moisture', 'direct')

def logic_11811(world):
    _world_apply(world, 'flowers', 'runoff', 'square')

def logic_11812(world):
    _world_apply(world, 'flowers', 'wind_x', 'pulse')

def logic_11813(world):
    _world_apply(world, 'flowers', 'wind_y', 'saturation')

def logic_11814(world):
    _world_apply(world, 'flowers', 'vegetation', 'gap')

def logic_11815(world):
    _world_apply(world, 'flowers', 'biomass', 'direct')

def logic_11816(world):
    _world_apply(world, 'flowers', 'herbivore', 'square')

def logic_11817(world):
    _world_apply(world, 'flowers', 'predator', 'saturation')

def logic_11818(world):
    _world_apply(world, 'flowers', 'carrion', 'gap')

def logic_11819(world):
    _world_apply(world, 'flowers', 'nutrients', 'direct')

def logic_11820(world):
    _world_apply(world, 'flowers', 'decomposition_rate', 'square')

def logic_11821(world):
    _world_apply(world, 'flowers', 'oxygen', 'pulse')

def logic_11822(world):
    _world_apply(world, 'flowers', 'co2', 'saturation')

def logic_11823(world):
    _world_apply(world, 'flowers', 'photosynthesis_factor', 'gap')

def logic_11824(world):
    _world_apply(world, 'flowers', 'ice', 'direct')

def logic_11825(world):
    _world_apply(world, 'flowers', 'evaporation', 'pulse')

def logic_11826(world):
    _world_apply(world, 'flowers', 'detritus', 'saturation')

def logic_11827(world):
    _world_apply(world, 'flowers', 'methane', 'gap')

def logic_11828(world):
    _world_apply(world, 'flowers', 'pathogen_load', 'direct')

def logic_11829(world):
    _world_apply(world, 'flowers', 'biodiversity', 'square')

def logic_11830(world):
    _world_apply(world, 'flowers', 'habitat_stress', 'pulse')

def logic_11831(world):
    _world_apply(world, 'flowers', 'erosion', 'saturation')

def logic_11832(world):
    _world_apply(world, 'flowers', 'soil_depth', 'gap')

def logic_11833(world):
    _world_apply(world, 'flowers', 'root_density', 'square')

def logic_11834(world):
    _world_apply(world, 'flowers', 'wetland', 'pulse')

def logic_11835(world):
    _world_apply(world, 'flowers', 'carbon_storage', 'saturation')

def logic_11836(world):
    _world_apply(world, 'flowers', 'fire_risk', 'gap')

def logic_11837(world):
    _world_apply(world, 'flowers', 'ash', 'direct')

def logic_11838(world):
    _world_apply(world, 'flowers', 'snowpack', 'square')

def logic_11839(world):
    _world_apply(world, 'flowers', 'groundwater', 'pulse')

def logic_11840(world):
    _world_apply(world, 'flowers', 'sediment', 'saturation')

def logic_11841(world):
    _world_apply(world, 'flowers', 'salinity', 'direct')

def logic_11842(world):
    _world_apply(world, 'flowers', 'algae', 'square')

def logic_11843(world):
    _world_apply(world, 'flowers', 'organic_matter', 'pulse')

def logic_11844(world):
    _world_apply(world, 'flowers', 'deadwood', 'saturation')

def logic_11845(world):
    _world_apply(world, 'flowers', 'pollinators', 'gap')

def logic_11846(world):
    _world_apply(world, 'flowers', 'seed_bank', 'direct')

def logic_11847(world):
    _world_apply(world, 'flowers', 'soil_carbon', 'square')

def logic_11848(world):
    _world_apply(world, 'flowers', 'surface_ice', 'pulse')

def logic_11849(world):
    _world_apply(world, 'seed_bank', 'temperature', 'gap')

def logic_11850(world):
    _world_apply(world, 'seed_bank', 'surface_water', 'direct')

def logic_11851(world):
    _world_apply(world, 'seed_bank', 'humidity', 'square')

def logic_11852(world):
    _world_apply(world, 'seed_bank', 'cloud', 'pulse')

def logic_11853(world):
    _world_apply(world, 'seed_bank', 'rain', 'saturation')

def logic_11854(world):
    _world_apply(world, 'seed_bank', 'soil_moisture', 'gap')

def logic_11855(world):
    _world_apply(world, 'seed_bank', 'runoff', 'direct')

def logic_11856(world):
    _world_apply(world, 'seed_bank', 'wind_x', 'square')

def logic_11857(world):
    _world_apply(world, 'seed_bank', 'wind_y', 'saturation')

def logic_11858(world):
    _world_apply(world, 'seed_bank', 'vegetation', 'gap')

def logic_11859(world):
    _world_apply(world, 'seed_bank', 'biomass', 'direct')

def logic_11860(world):
    _world_apply(world, 'seed_bank', 'herbivore', 'square')

def logic_11861(world):
    _world_apply(world, 'seed_bank', 'predator', 'pulse')

def logic_11862(world):
    _world_apply(world, 'seed_bank', 'carrion', 'saturation')

def logic_11863(world):
    _world_apply(world, 'seed_bank', 'nutrients', 'gap')

def logic_11864(world):
    _world_apply(world, 'seed_bank', 'decomposition_rate', 'direct')

def logic_11865(world):
    _world_apply(world, 'seed_bank', 'oxygen', 'pulse')

def logic_11866(world):
    _world_apply(world, 'seed_bank', 'co2', 'saturation')

def logic_11867(world):
    _world_apply(world, 'seed_bank', 'photosynthesis_factor', 'gap')

def logic_11868(world):
    _world_apply(world, 'seed_bank', 'ice', 'direct')

def logic_11869(world):
    _world_apply(world, 'seed_bank', 'evaporation', 'square')

def logic_11870(world):
    _world_apply(world, 'seed_bank', 'detritus', 'pulse')

def logic_11871(world):
    _world_apply(world, 'seed_bank', 'methane', 'saturation')

def logic_11872(world):
    _world_apply(world, 'seed_bank', 'pathogen_load', 'gap')

def logic_11873(world):
    _world_apply(world, 'seed_bank', 'biodiversity', 'square')

def logic_11874(world):
    _world_apply(world, 'seed_bank', 'habitat_stress', 'pulse')

def logic_11875(world):
    _world_apply(world, 'seed_bank', 'erosion', 'saturation')

def logic_11876(world):
    _world_apply(world, 'seed_bank', 'soil_depth', 'gap')

def logic_11877(world):
    _world_apply(world, 'seed_bank', 'root_density', 'direct')

def logic_11878(world):
    _world_apply(world, 'seed_bank', 'wetland', 'square')

def logic_11879(world):
    _world_apply(world, 'seed_bank', 'carbon_storage', 'pulse')

def logic_11880(world):
    _world_apply(world, 'seed_bank', 'fire_risk', 'saturation')

def logic_11881(world):
    _world_apply(world, 'seed_bank', 'ash', 'direct')

def logic_11882(world):
    _world_apply(world, 'seed_bank', 'snowpack', 'square')

def logic_11883(world):
    _world_apply(world, 'seed_bank', 'groundwater', 'pulse')

def logic_11884(world):
    _world_apply(world, 'seed_bank', 'sediment', 'saturation')

def logic_11885(world):
    _world_apply(world, 'seed_bank', 'salinity', 'gap')

def logic_11886(world):
    _world_apply(world, 'seed_bank', 'algae', 'direct')

def logic_11887(world):
    _world_apply(world, 'seed_bank', 'organic_matter', 'square')

def logic_11888(world):
    _world_apply(world, 'seed_bank', 'deadwood', 'pulse')

def logic_11889(world):
    _world_apply(world, 'seed_bank', 'pollinators', 'gap')

def logic_11890(world):
    _world_apply(world, 'seed_bank', 'flowers', 'direct')

def logic_11891(world):
    _world_apply(world, 'seed_bank', 'soil_carbon', 'square')

def logic_11892(world):
    _world_apply(world, 'seed_bank', 'surface_ice', 'pulse')

def logic_11893(world):
    _world_apply(world, 'soil_carbon', 'temperature', 'saturation')

def logic_11894(world):
    _world_apply(world, 'soil_carbon', 'surface_water', 'gap')

def logic_11895(world):
    _world_apply(world, 'soil_carbon', 'humidity', 'direct')

def logic_11896(world):
    _world_apply(world, 'soil_carbon', 'cloud', 'square')

def logic_11897(world):
    _world_apply(world, 'soil_carbon', 'rain', 'saturation')

def logic_11898(world):
    _world_apply(world, 'soil_carbon', 'soil_moisture', 'gap')

def logic_11899(world):
    _world_apply(world, 'soil_carbon', 'runoff', 'direct')

def logic_11900(world):
    _world_apply(world, 'soil_carbon', 'wind_x', 'square')

def logic_11901(world):
    _world_apply(world, 'soil_carbon', 'wind_y', 'pulse')

def logic_11902(world):
    _world_apply(world, 'soil_carbon', 'vegetation', 'saturation')

def logic_11903(world):
    _world_apply(world, 'soil_carbon', 'biomass', 'gap')

def logic_11904(world):
    _world_apply(world, 'soil_carbon', 'herbivore', 'direct')

def logic_11905(world):
    _world_apply(world, 'soil_carbon', 'predator', 'pulse')

def logic_11906(world):
    _world_apply(world, 'soil_carbon', 'carrion', 'saturation')

def logic_11907(world):
    _world_apply(world, 'soil_carbon', 'nutrients', 'gap')

def logic_11908(world):
    _world_apply(world, 'soil_carbon', 'decomposition_rate', 'direct')

def logic_11909(world):
    _world_apply(world, 'soil_carbon', 'oxygen', 'square')

def logic_11910(world):
    _world_apply(world, 'soil_carbon', 'co2', 'pulse')

def logic_11911(world):
    _world_apply(world, 'soil_carbon', 'photosynthesis_factor', 'saturation')

def logic_11912(world):
    _world_apply(world, 'soil_carbon', 'ice', 'gap')

def logic_11913(world):
    _world_apply(world, 'soil_carbon', 'evaporation', 'square')

def logic_11914(world):
    _world_apply(world, 'soil_carbon', 'detritus', 'pulse')

def logic_11915(world):
    _world_apply(world, 'soil_carbon', 'methane', 'saturation')

def logic_11916(world):
    _world_apply(world, 'soil_carbon', 'pathogen_load', 'gap')

def logic_11917(world):
    _world_apply(world, 'soil_carbon', 'biodiversity', 'direct')

def logic_11918(world):
    _world_apply(world, 'soil_carbon', 'habitat_stress', 'square')

def logic_11919(world):
    _world_apply(world, 'soil_carbon', 'erosion', 'pulse')

def logic_11920(world):
    _world_apply(world, 'soil_carbon', 'soil_depth', 'saturation')

def logic_11921(world):
    _world_apply(world, 'soil_carbon', 'root_density', 'direct')

def logic_11922(world):
    _world_apply(world, 'soil_carbon', 'wetland', 'square')

def logic_11923(world):
    _world_apply(world, 'soil_carbon', 'carbon_storage', 'pulse')

def logic_11924(world):
    _world_apply(world, 'soil_carbon', 'fire_risk', 'saturation')

def logic_11925(world):
    _world_apply(world, 'soil_carbon', 'ash', 'gap')

def logic_11926(world):
    _world_apply(world, 'soil_carbon', 'snowpack', 'direct')

def logic_11927(world):
    _world_apply(world, 'soil_carbon', 'groundwater', 'square')

def logic_11928(world):
    _world_apply(world, 'soil_carbon', 'sediment', 'pulse')

def logic_11929(world):
    _world_apply(world, 'soil_carbon', 'salinity', 'gap')

def logic_11930(world):
    _world_apply(world, 'soil_carbon', 'algae', 'direct')

def logic_11931(world):
    _world_apply(world, 'soil_carbon', 'organic_matter', 'square')

def logic_11932(world):
    _world_apply(world, 'soil_carbon', 'deadwood', 'pulse')

def logic_11933(world):
    _world_apply(world, 'soil_carbon', 'pollinators', 'saturation')

def logic_11934(world):
    _world_apply(world, 'soil_carbon', 'flowers', 'gap')

def logic_11935(world):
    _world_apply(world, 'soil_carbon', 'seed_bank', 'direct')

def logic_11936(world):
    _world_apply(world, 'soil_carbon', 'surface_ice', 'square')

def logic_11937(world):
    _world_apply(world, 'surface_ice', 'temperature', 'saturation')

def logic_11938(world):
    _world_apply(world, 'surface_ice', 'surface_water', 'gap')

def logic_11939(world):
    _world_apply(world, 'surface_ice', 'humidity', 'direct')

def logic_11940(world):
    _world_apply(world, 'surface_ice', 'cloud', 'square')

def logic_11941(world):
    _world_apply(world, 'surface_ice', 'rain', 'pulse')

def logic_11942(world):
    _world_apply(world, 'surface_ice', 'soil_moisture', 'saturation')

def logic_11943(world):
    _world_apply(world, 'surface_ice', 'runoff', 'gap')

def logic_11944(world):
    _world_apply(world, 'surface_ice', 'wind_x', 'direct')

def logic_11945(world):
    _world_apply(world, 'surface_ice', 'wind_y', 'pulse')

def logic_11946(world):
    _world_apply(world, 'surface_ice', 'vegetation', 'saturation')

def logic_11947(world):
    _world_apply(world, 'surface_ice', 'biomass', 'gap')

def logic_11948(world):
    _world_apply(world, 'surface_ice', 'herbivore', 'direct')

def logic_11949(world):
    _world_apply(world, 'surface_ice', 'predator', 'square')

def logic_11950(world):
    _world_apply(world, 'surface_ice', 'carrion', 'pulse')

def logic_11951(world):
    _world_apply(world, 'surface_ice', 'nutrients', 'saturation')

def logic_11952(world):
    _world_apply(world, 'surface_ice', 'decomposition_rate', 'gap')

def logic_11953(world):
    _world_apply(world, 'surface_ice', 'oxygen', 'square')

def logic_11954(world):
    _world_apply(world, 'surface_ice', 'co2', 'pulse')

def logic_11955(world):
    _world_apply(world, 'surface_ice', 'photosynthesis_factor', 'saturation')

def logic_11956(world):
    _world_apply(world, 'surface_ice', 'ice', 'gap')

def logic_11957(world):
    _world_apply(world, 'surface_ice', 'evaporation', 'direct')

def logic_11958(world):
    _world_apply(world, 'surface_ice', 'detritus', 'square')

def logic_11959(world):
    _world_apply(world, 'surface_ice', 'methane', 'pulse')

def logic_11960(world):
    _world_apply(world, 'surface_ice', 'pathogen_load', 'saturation')

def logic_11961(world):
    _world_apply(world, 'surface_ice', 'biodiversity', 'direct')

def logic_11962(world):
    _world_apply(world, 'surface_ice', 'habitat_stress', 'square')

def logic_11963(world):
    _world_apply(world, 'surface_ice', 'erosion', 'pulse')

def logic_11964(world):
    _world_apply(world, 'surface_ice', 'soil_depth', 'saturation')

def logic_11965(world):
    _world_apply(world, 'surface_ice', 'root_density', 'gap')

def logic_11966(world):
    _world_apply(world, 'surface_ice', 'wetland', 'direct')

def logic_11967(world):
    _world_apply(world, 'surface_ice', 'carbon_storage', 'square')

def logic_11968(world):
    _world_apply(world, 'surface_ice', 'fire_risk', 'pulse')

def logic_11969(world):
    _world_apply(world, 'surface_ice', 'ash', 'gap')

def logic_11970(world):
    _world_apply(world, 'surface_ice', 'snowpack', 'direct')

def logic_11971(world):
    _world_apply(world, 'surface_ice', 'groundwater', 'square')

def logic_11972(world):
    _world_apply(world, 'surface_ice', 'sediment', 'pulse')

def logic_11973(world):
    _world_apply(world, 'surface_ice', 'salinity', 'saturation')

def logic_11974(world):
    _world_apply(world, 'surface_ice', 'algae', 'gap')

def logic_11975(world):
    _world_apply(world, 'surface_ice', 'organic_matter', 'direct')

def logic_11976(world):
    _world_apply(world, 'surface_ice', 'deadwood', 'square')

def logic_11977(world):
    _world_apply(world, 'surface_ice', 'pollinators', 'saturation')

def logic_11978(world):
    _world_apply(world, 'surface_ice', 'flowers', 'gap')

def logic_11979(world):
    _world_apply(world, 'surface_ice', 'seed_bank', 'direct')

def logic_11980(world):
    _world_apply(world, 'surface_ice', 'soil_carbon', 'square')

def logic_11981(world):
    _world_apply(world, 'temperature', 'surface_water', 'pulse')

def logic_11982(world):
    _world_apply(world, 'temperature', 'humidity', 'saturation')

def logic_11983(world):
    _world_apply(world, 'temperature', 'cloud', 'gap')

def logic_11984(world):
    _world_apply(world, 'temperature', 'rain', 'direct')

def logic_11985(world):
    _world_apply(world, 'temperature', 'soil_moisture', 'pulse')

def logic_11986(world):
    _world_apply(world, 'temperature', 'runoff', 'saturation')

def logic_11987(world):
    _world_apply(world, 'temperature', 'wind_x', 'gap')

def logic_11988(world):
    _world_apply(world, 'temperature', 'wind_y', 'direct')

def logic_11989(world):
    _world_apply(world, 'temperature', 'vegetation', 'square')

def logic_11990(world):
    _world_apply(world, 'temperature', 'biomass', 'pulse')

def logic_11991(world):
    _world_apply(world, 'temperature', 'herbivore', 'saturation')

def logic_11992(world):
    _world_apply(world, 'temperature', 'predator', 'gap')

def logic_11993(world):
    _world_apply(world, 'temperature', 'carrion', 'square')

def logic_11994(world):
    _world_apply(world, 'temperature', 'nutrients', 'pulse')

def logic_11995(world):
    _world_apply(world, 'temperature', 'decomposition_rate', 'saturation')

def logic_11996(world):
    _world_apply(world, 'temperature', 'oxygen', 'gap')

def logic_11997(world):
    _world_apply(world, 'temperature', 'co2', 'direct')

def logic_11998(world):
    _world_apply(world, 'temperature', 'photosynthesis_factor', 'square')

def logic_11999(world):
    _world_apply(world, 'temperature', 'ice', 'pulse')

def logic_12000(world):
    _world_apply(world, 'temperature', 'evaporation', 'saturation')

def logic_12001(world):
    _world_apply(world, 'temperature', 'detritus', 'direct')

def logic_12002(world):
    _world_apply(world, 'temperature', 'methane', 'square')

def logic_12003(world):
    _world_apply(world, 'temperature', 'pathogen_load', 'pulse')

def logic_12004(world):
    _world_apply(world, 'temperature', 'biodiversity', 'saturation')

def logic_12005(world):
    _world_apply(world, 'temperature', 'habitat_stress', 'gap')

def logic_12006(world):
    _world_apply(world, 'temperature', 'erosion', 'direct')

def logic_12007(world):
    _world_apply(world, 'temperature', 'soil_depth', 'square')

def logic_12008(world):
    _world_apply(world, 'temperature', 'root_density', 'pulse')

def logic_12009(world):
    _world_apply(world, 'temperature', 'wetland', 'gap')

def logic_12010(world):
    _world_apply(world, 'temperature', 'carbon_storage', 'direct')

def logic_12011(world):
    _world_apply(world, 'temperature', 'fire_risk', 'square')

def logic_12012(world):
    _world_apply(world, 'temperature', 'ash', 'pulse')

def logic_12013(world):
    _world_apply(world, 'temperature', 'snowpack', 'saturation')

def logic_12014(world):
    _world_apply(world, 'temperature', 'groundwater', 'gap')

def logic_12015(world):
    _world_apply(world, 'temperature', 'sediment', 'direct')

def logic_12016(world):
    _world_apply(world, 'temperature', 'salinity', 'square')

def logic_12017(world):
    _world_apply(world, 'temperature', 'algae', 'saturation')

def logic_12018(world):
    _world_apply(world, 'temperature', 'organic_matter', 'gap')

def logic_12019(world):
    _world_apply(world, 'temperature', 'deadwood', 'direct')

def logic_12020(world):
    _world_apply(world, 'temperature', 'pollinators', 'square')

def logic_12021(world):
    _world_apply(world, 'temperature', 'flowers', 'pulse')

def logic_12022(world):
    _world_apply(world, 'temperature', 'seed_bank', 'saturation')

def logic_12023(world):
    _world_apply(world, 'temperature', 'soil_carbon', 'gap')

def logic_12024(world):
    _world_apply(world, 'temperature', 'surface_ice', 'direct')

def logic_12025(world):
    _world_apply(world, 'surface_water', 'temperature', 'pulse')

def logic_12026(world):
    _world_apply(world, 'surface_water', 'humidity', 'saturation')

def logic_12027(world):
    _world_apply(world, 'surface_water', 'cloud', 'gap')

def logic_12028(world):
    _world_apply(world, 'surface_water', 'rain', 'direct')

def logic_12029(world):
    _world_apply(world, 'surface_water', 'soil_moisture', 'square')

def logic_12030(world):
    _world_apply(world, 'surface_water', 'runoff', 'pulse')

def logic_12031(world):
    _world_apply(world, 'surface_water', 'wind_x', 'saturation')

def logic_12032(world):
    _world_apply(world, 'surface_water', 'wind_y', 'gap')

def logic_12033(world):
    _world_apply(world, 'surface_water', 'vegetation', 'square')

def logic_12034(world):
    _world_apply(world, 'surface_water', 'biomass', 'pulse')

def logic_12035(world):
    _world_apply(world, 'surface_water', 'herbivore', 'saturation')

def logic_12036(world):
    _world_apply(world, 'surface_water', 'predator', 'gap')

def logic_12037(world):
    _world_apply(world, 'surface_water', 'carrion', 'direct')

def logic_12038(world):
    _world_apply(world, 'surface_water', 'nutrients', 'square')

def logic_12039(world):
    _world_apply(world, 'surface_water', 'decomposition_rate', 'pulse')

def logic_12040(world):
    _world_apply(world, 'surface_water', 'oxygen', 'saturation')

def logic_12041(world):
    _world_apply(world, 'surface_water', 'co2', 'direct')

def logic_12042(world):
    _world_apply(world, 'surface_water', 'photosynthesis_factor', 'square')

def logic_12043(world):
    _world_apply(world, 'surface_water', 'ice', 'pulse')

def logic_12044(world):
    _world_apply(world, 'surface_water', 'evaporation', 'saturation')

def logic_12045(world):
    _world_apply(world, 'surface_water', 'detritus', 'gap')

def logic_12046(world):
    _world_apply(world, 'surface_water', 'methane', 'direct')

def logic_12047(world):
    _world_apply(world, 'surface_water', 'pathogen_load', 'square')

def logic_12048(world):
    _world_apply(world, 'surface_water', 'biodiversity', 'pulse')

def logic_12049(world):
    _world_apply(world, 'surface_water', 'habitat_stress', 'gap')

def logic_12050(world):
    _world_apply(world, 'surface_water', 'erosion', 'direct')

def logic_12051(world):
    _world_apply(world, 'surface_water', 'soil_depth', 'square')

def logic_12052(world):
    _world_apply(world, 'surface_water', 'root_density', 'pulse')

def logic_12053(world):
    _world_apply(world, 'surface_water', 'wetland', 'saturation')

def logic_12054(world):
    _world_apply(world, 'surface_water', 'carbon_storage', 'gap')

def logic_12055(world):
    _world_apply(world, 'surface_water', 'fire_risk', 'direct')

def logic_12056(world):
    _world_apply(world, 'surface_water', 'ash', 'square')

def logic_12057(world):
    _world_apply(world, 'surface_water', 'snowpack', 'saturation')

def logic_12058(world):
    _world_apply(world, 'surface_water', 'groundwater', 'gap')

def logic_12059(world):
    _world_apply(world, 'surface_water', 'sediment', 'direct')

def logic_12060(world):
    _world_apply(world, 'surface_water', 'salinity', 'square')

def logic_12061(world):
    _world_apply(world, 'surface_water', 'algae', 'pulse')

def logic_12062(world):
    _world_apply(world, 'surface_water', 'organic_matter', 'saturation')

def logic_12063(world):
    _world_apply(world, 'surface_water', 'deadwood', 'gap')

def logic_12064(world):
    _world_apply(world, 'surface_water', 'pollinators', 'direct')

def logic_12065(world):
    _world_apply(world, 'surface_water', 'flowers', 'pulse')

def logic_12066(world):
    _world_apply(world, 'surface_water', 'seed_bank', 'saturation')

def logic_12067(world):
    _world_apply(world, 'surface_water', 'soil_carbon', 'gap')

def logic_12068(world):
    _world_apply(world, 'surface_water', 'surface_ice', 'direct')

def logic_12069(world):
    _world_apply(world, 'humidity', 'temperature', 'square')

def logic_12070(world):
    _world_apply(world, 'humidity', 'surface_water', 'pulse')

def logic_12071(world):
    _world_apply(world, 'humidity', 'cloud', 'saturation')

def logic_12072(world):
    _world_apply(world, 'humidity', 'rain', 'gap')

def logic_12073(world):
    _world_apply(world, 'humidity', 'soil_moisture', 'square')

def logic_12074(world):
    _world_apply(world, 'humidity', 'runoff', 'pulse')

def logic_12075(world):
    _world_apply(world, 'humidity', 'wind_x', 'saturation')

def logic_12076(world):
    _world_apply(world, 'humidity', 'wind_y', 'gap')

def logic_12077(world):
    _world_apply(world, 'humidity', 'vegetation', 'direct')

def logic_12078(world):
    _world_apply(world, 'humidity', 'biomass', 'square')

def logic_12079(world):
    _world_apply(world, 'humidity', 'herbivore', 'pulse')

def logic_12080(world):
    _world_apply(world, 'humidity', 'predator', 'saturation')

def logic_12081(world):
    _world_apply(world, 'humidity', 'carrion', 'direct')

def logic_12082(world):
    _world_apply(world, 'humidity', 'nutrients', 'square')

def logic_12083(world):
    _world_apply(world, 'humidity', 'decomposition_rate', 'pulse')

def logic_12084(world):
    _world_apply(world, 'humidity', 'oxygen', 'saturation')

def logic_12085(world):
    _world_apply(world, 'humidity', 'co2', 'gap')

def logic_12086(world):
    _world_apply(world, 'humidity', 'photosynthesis_factor', 'direct')

def logic_12087(world):
    _world_apply(world, 'humidity', 'ice', 'square')

def logic_12088(world):
    _world_apply(world, 'humidity', 'evaporation', 'pulse')

def logic_12089(world):
    _world_apply(world, 'humidity', 'detritus', 'gap')

def logic_12090(world):
    _world_apply(world, 'humidity', 'methane', 'direct')

def logic_12091(world):
    _world_apply(world, 'humidity', 'pathogen_load', 'square')

def logic_12092(world):
    _world_apply(world, 'humidity', 'biodiversity', 'pulse')

def logic_12093(world):
    _world_apply(world, 'humidity', 'habitat_stress', 'saturation')

def logic_12094(world):
    _world_apply(world, 'humidity', 'erosion', 'gap')

def logic_12095(world):
    _world_apply(world, 'humidity', 'soil_depth', 'direct')

def logic_12096(world):
    _world_apply(world, 'humidity', 'root_density', 'square')

def logic_12097(world):
    _world_apply(world, 'humidity', 'wetland', 'saturation')

def logic_12098(world):
    _world_apply(world, 'humidity', 'carbon_storage', 'gap')

def logic_12099(world):
    _world_apply(world, 'humidity', 'fire_risk', 'direct')

def logic_12100(world):
    _world_apply(world, 'humidity', 'ash', 'square')

def logic_12101(world):
    _world_apply(world, 'humidity', 'snowpack', 'pulse')

def logic_12102(world):
    _world_apply(world, 'humidity', 'groundwater', 'saturation')

def logic_12103(world):
    _world_apply(world, 'humidity', 'sediment', 'gap')

def logic_12104(world):
    _world_apply(world, 'humidity', 'salinity', 'direct')

def logic_12105(world):
    _world_apply(world, 'humidity', 'algae', 'pulse')

def logic_12106(world):
    _world_apply(world, 'humidity', 'organic_matter', 'saturation')

def logic_12107(world):
    _world_apply(world, 'humidity', 'deadwood', 'gap')

def logic_12108(world):
    _world_apply(world, 'humidity', 'pollinators', 'direct')

def logic_12109(world):
    _world_apply(world, 'humidity', 'flowers', 'square')

def logic_12110(world):
    _world_apply(world, 'humidity', 'seed_bank', 'pulse')

def logic_12111(world):
    _world_apply(world, 'humidity', 'soil_carbon', 'saturation')

def logic_12112(world):
    _world_apply(world, 'humidity', 'surface_ice', 'gap')

def logic_12113(world):
    _world_apply(world, 'cloud', 'temperature', 'square')

def logic_12114(world):
    _world_apply(world, 'cloud', 'surface_water', 'pulse')

def logic_12115(world):
    _world_apply(world, 'cloud', 'humidity', 'saturation')

def logic_12116(world):
    _world_apply(world, 'cloud', 'rain', 'gap')

def logic_12117(world):
    _world_apply(world, 'cloud', 'soil_moisture', 'direct')

def logic_12118(world):
    _world_apply(world, 'cloud', 'runoff', 'square')

def logic_12119(world):
    _world_apply(world, 'cloud', 'wind_x', 'pulse')

def logic_12120(world):
    _world_apply(world, 'cloud', 'wind_y', 'saturation')

def logic_12121(world):
    _world_apply(world, 'cloud', 'vegetation', 'direct')

def logic_12122(world):
    _world_apply(world, 'cloud', 'biomass', 'square')

def logic_12123(world):
    _world_apply(world, 'cloud', 'herbivore', 'pulse')

def logic_12124(world):
    _world_apply(world, 'cloud', 'predator', 'saturation')

def logic_12125(world):
    _world_apply(world, 'cloud', 'carrion', 'gap')

def logic_12126(world):
    _world_apply(world, 'cloud', 'nutrients', 'direct')

def logic_12127(world):
    _world_apply(world, 'cloud', 'decomposition_rate', 'square')

def logic_12128(world):
    _world_apply(world, 'cloud', 'oxygen', 'pulse')

def logic_12129(world):
    _world_apply(world, 'cloud', 'co2', 'gap')

def logic_12130(world):
    _world_apply(world, 'cloud', 'photosynthesis_factor', 'direct')

def logic_12131(world):
    _world_apply(world, 'cloud', 'ice', 'square')

def logic_12132(world):
    _world_apply(world, 'cloud', 'evaporation', 'pulse')

def logic_12133(world):
    _world_apply(world, 'cloud', 'detritus', 'saturation')

def logic_12134(world):
    _world_apply(world, 'cloud', 'methane', 'gap')

def logic_12135(world):
    _world_apply(world, 'cloud', 'pathogen_load', 'direct')

def logic_12136(world):
    _world_apply(world, 'cloud', 'biodiversity', 'square')

def logic_12137(world):
    _world_apply(world, 'cloud', 'habitat_stress', 'saturation')

def logic_12138(world):
    _world_apply(world, 'cloud', 'erosion', 'gap')

def logic_12139(world):
    _world_apply(world, 'cloud', 'soil_depth', 'direct')

def logic_12140(world):
    _world_apply(world, 'cloud', 'root_density', 'square')

def logic_12141(world):
    _world_apply(world, 'cloud', 'wetland', 'pulse')

def logic_12142(world):
    _world_apply(world, 'cloud', 'carbon_storage', 'saturation')

def logic_12143(world):
    _world_apply(world, 'cloud', 'fire_risk', 'gap')

def logic_12144(world):
    _world_apply(world, 'cloud', 'ash', 'direct')

def logic_12145(world):
    _world_apply(world, 'cloud', 'snowpack', 'pulse')

def logic_12146(world):
    _world_apply(world, 'cloud', 'groundwater', 'saturation')

def logic_12147(world):
    _world_apply(world, 'cloud', 'sediment', 'gap')

def logic_12148(world):
    _world_apply(world, 'cloud', 'salinity', 'direct')

def logic_12149(world):
    _world_apply(world, 'cloud', 'algae', 'square')

def logic_12150(world):
    _world_apply(world, 'cloud', 'organic_matter', 'pulse')

def logic_12151(world):
    _world_apply(world, 'cloud', 'deadwood', 'saturation')

def logic_12152(world):
    _world_apply(world, 'cloud', 'pollinators', 'gap')

def logic_12153(world):
    _world_apply(world, 'cloud', 'flowers', 'square')

def logic_12154(world):
    _world_apply(world, 'cloud', 'seed_bank', 'pulse')

def logic_12155(world):
    _world_apply(world, 'cloud', 'soil_carbon', 'saturation')

def logic_12156(world):
    _world_apply(world, 'cloud', 'surface_ice', 'gap')

def logic_12157(world):
    _world_apply(world, 'rain', 'temperature', 'direct')

def logic_12158(world):
    _world_apply(world, 'rain', 'surface_water', 'square')

def logic_12159(world):
    _world_apply(world, 'rain', 'humidity', 'pulse')

def logic_12160(world):
    _world_apply(world, 'rain', 'cloud', 'saturation')

def logic_12161(world):
    _world_apply(world, 'rain', 'soil_moisture', 'direct')

def logic_12162(world):
    _world_apply(world, 'rain', 'runoff', 'square')

def logic_12163(world):
    _world_apply(world, 'rain', 'wind_x', 'pulse')

def logic_12164(world):
    _world_apply(world, 'rain', 'wind_y', 'saturation')

def logic_12165(world):
    _world_apply(world, 'rain', 'vegetation', 'gap')

def logic_12166(world):
    _world_apply(world, 'rain', 'biomass', 'direct')

def logic_12167(world):
    _world_apply(world, 'rain', 'herbivore', 'square')

def logic_12168(world):
    _world_apply(world, 'rain', 'predator', 'pulse')

def logic_12169(world):
    _world_apply(world, 'rain', 'carrion', 'gap')

def logic_12170(world):
    _world_apply(world, 'rain', 'nutrients', 'direct')

def logic_12171(world):
    _world_apply(world, 'rain', 'decomposition_rate', 'square')

def logic_12172(world):
    _world_apply(world, 'rain', 'oxygen', 'pulse')

def logic_12173(world):
    _world_apply(world, 'rain', 'co2', 'saturation')

def logic_12174(world):
    _world_apply(world, 'rain', 'photosynthesis_factor', 'gap')

def logic_12175(world):
    _world_apply(world, 'rain', 'ice', 'direct')

def logic_12176(world):
    _world_apply(world, 'rain', 'evaporation', 'square')

def logic_12177(world):
    _world_apply(world, 'rain', 'detritus', 'saturation')

def logic_12178(world):
    _world_apply(world, 'rain', 'methane', 'gap')

def logic_12179(world):
    _world_apply(world, 'rain', 'pathogen_load', 'direct')

def logic_12180(world):
    _world_apply(world, 'rain', 'biodiversity', 'square')

def logic_12181(world):
    _world_apply(world, 'rain', 'habitat_stress', 'pulse')

def logic_12182(world):
    _world_apply(world, 'rain', 'erosion', 'saturation')

def logic_12183(world):
    _world_apply(world, 'rain', 'soil_depth', 'gap')

def logic_12184(world):
    _world_apply(world, 'rain', 'root_density', 'direct')

def logic_12185(world):
    _world_apply(world, 'rain', 'wetland', 'pulse')

def logic_12186(world):
    _world_apply(world, 'rain', 'carbon_storage', 'saturation')

def logic_12187(world):
    _world_apply(world, 'rain', 'fire_risk', 'gap')

def logic_12188(world):
    _world_apply(world, 'rain', 'ash', 'direct')

def logic_12189(world):
    _world_apply(world, 'rain', 'snowpack', 'square')

def logic_12190(world):
    _world_apply(world, 'rain', 'groundwater', 'pulse')

def logic_12191(world):
    _world_apply(world, 'rain', 'sediment', 'saturation')

def logic_12192(world):
    _world_apply(world, 'rain', 'salinity', 'gap')

def logic_12193(world):
    _world_apply(world, 'rain', 'algae', 'square')

def logic_12194(world):
    _world_apply(world, 'rain', 'organic_matter', 'pulse')

def logic_12195(world):
    _world_apply(world, 'rain', 'deadwood', 'saturation')

def logic_12196(world):
    _world_apply(world, 'rain', 'pollinators', 'gap')

def logic_12197(world):
    _world_apply(world, 'rain', 'flowers', 'direct')

def logic_12198(world):
    _world_apply(world, 'rain', 'seed_bank', 'square')

def logic_12199(world):
    _world_apply(world, 'rain', 'soil_carbon', 'pulse')

def logic_12200(world):
    _world_apply(world, 'rain', 'surface_ice', 'saturation')

def logic_12201(world):
    _world_apply(world, 'soil_moisture', 'temperature', 'direct')

def logic_12202(world):
    _world_apply(world, 'soil_moisture', 'surface_water', 'square')

def logic_12203(world):
    _world_apply(world, 'soil_moisture', 'humidity', 'pulse')

def logic_12204(world):
    _world_apply(world, 'soil_moisture', 'cloud', 'saturation')

def logic_12205(world):
    _world_apply(world, 'soil_moisture', 'rain', 'gap')

def logic_12206(world):
    _world_apply(world, 'soil_moisture', 'runoff', 'direct')

def logic_12207(world):
    _world_apply(world, 'soil_moisture', 'wind_x', 'square')

def logic_12208(world):
    _world_apply(world, 'soil_moisture', 'wind_y', 'pulse')

def logic_12209(world):
    _world_apply(world, 'soil_moisture', 'vegetation', 'gap')

def logic_12210(world):
    _world_apply(world, 'soil_moisture', 'biomass', 'direct')

def logic_12211(world):
    _world_apply(world, 'soil_moisture', 'herbivore', 'square')

def logic_12212(world):
    _world_apply(world, 'soil_moisture', 'predator', 'pulse')

def logic_12213(world):
    _world_apply(world, 'soil_moisture', 'carrion', 'saturation')

def logic_12214(world):
    _world_apply(world, 'soil_moisture', 'nutrients', 'gap')

def logic_12215(world):
    _world_apply(world, 'soil_moisture', 'decomposition_rate', 'direct')

def logic_12216(world):
    _world_apply(world, 'soil_moisture', 'oxygen', 'square')

def logic_12217(world):
    _world_apply(world, 'soil_moisture', 'co2', 'saturation')

def logic_12218(world):
    _world_apply(world, 'soil_moisture', 'photosynthesis_factor', 'gap')

def logic_12219(world):
    _world_apply(world, 'soil_moisture', 'ice', 'direct')

def logic_12220(world):
    _world_apply(world, 'soil_moisture', 'evaporation', 'square')

def logic_12221(world):
    _world_apply(world, 'soil_moisture', 'detritus', 'pulse')

def logic_12222(world):
    _world_apply(world, 'soil_moisture', 'methane', 'saturation')

def logic_12223(world):
    _world_apply(world, 'soil_moisture', 'pathogen_load', 'gap')

def logic_12224(world):
    _world_apply(world, 'soil_moisture', 'biodiversity', 'direct')

def logic_12225(world):
    _world_apply(world, 'soil_moisture', 'habitat_stress', 'pulse')

def logic_12226(world):
    _world_apply(world, 'soil_moisture', 'erosion', 'saturation')

def logic_12227(world):
    _world_apply(world, 'soil_moisture', 'soil_depth', 'gap')

def logic_12228(world):
    _world_apply(world, 'soil_moisture', 'root_density', 'direct')

def logic_12229(world):
    _world_apply(world, 'soil_moisture', 'wetland', 'square')

def logic_12230(world):
    _world_apply(world, 'soil_moisture', 'carbon_storage', 'pulse')

def logic_12231(world):
    _world_apply(world, 'soil_moisture', 'fire_risk', 'saturation')

def logic_12232(world):
    _world_apply(world, 'soil_moisture', 'ash', 'gap')

def logic_12233(world):
    _world_apply(world, 'soil_moisture', 'snowpack', 'square')

def logic_12234(world):
    _world_apply(world, 'soil_moisture', 'groundwater', 'pulse')

def logic_12235(world):
    _world_apply(world, 'soil_moisture', 'sediment', 'saturation')

def logic_12236(world):
    _world_apply(world, 'soil_moisture', 'salinity', 'gap')

def logic_12237(world):
    _world_apply(world, 'soil_moisture', 'algae', 'direct')

def logic_12238(world):
    _world_apply(world, 'soil_moisture', 'organic_matter', 'square')

def logic_12239(world):
    _world_apply(world, 'soil_moisture', 'deadwood', 'pulse')

def logic_12240(world):
    _world_apply(world, 'soil_moisture', 'pollinators', 'saturation')

def logic_12241(world):
    _world_apply(world, 'soil_moisture', 'flowers', 'direct')

def logic_12242(world):
    _world_apply(world, 'soil_moisture', 'seed_bank', 'square')

def logic_12243(world):
    _world_apply(world, 'soil_moisture', 'soil_carbon', 'pulse')

def logic_12244(world):
    _world_apply(world, 'soil_moisture', 'surface_ice', 'saturation')

def logic_12245(world):
    _world_apply(world, 'runoff', 'temperature', 'gap')

def logic_12246(world):
    _world_apply(world, 'runoff', 'surface_water', 'direct')

def logic_12247(world):
    _world_apply(world, 'runoff', 'humidity', 'square')

def logic_12248(world):
    _world_apply(world, 'runoff', 'cloud', 'pulse')

def logic_12249(world):
    _world_apply(world, 'runoff', 'rain', 'gap')

def logic_12250(world):
    _world_apply(world, 'runoff', 'soil_moisture', 'direct')

def logic_12251(world):
    _world_apply(world, 'runoff', 'wind_x', 'square')

def logic_12252(world):
    _world_apply(world, 'runoff', 'wind_y', 'pulse')

def logic_12253(world):
    _world_apply(world, 'runoff', 'vegetation', 'saturation')

def logic_12254(world):
    _world_apply(world, 'runoff', 'biomass', 'gap')

def logic_12255(world):
    _world_apply(world, 'runoff', 'herbivore', 'direct')

def logic_12256(world):
    _world_apply(world, 'runoff', 'predator', 'square')

def logic_12257(world):
    _world_apply(world, 'runoff', 'carrion', 'saturation')

def logic_12258(world):
    _world_apply(world, 'runoff', 'nutrients', 'gap')

def logic_12259(world):
    _world_apply(world, 'runoff', 'decomposition_rate', 'direct')

def logic_12260(world):
    _world_apply(world, 'runoff', 'oxygen', 'square')

def logic_12261(world):
    _world_apply(world, 'runoff', 'co2', 'pulse')

def logic_12262(world):
    _world_apply(world, 'runoff', 'photosynthesis_factor', 'saturation')

def logic_12263(world):
    _world_apply(world, 'runoff', 'ice', 'gap')

def logic_12264(world):
    _world_apply(world, 'runoff', 'evaporation', 'direct')

def logic_12265(world):
    _world_apply(world, 'runoff', 'detritus', 'pulse')

def logic_12266(world):
    _world_apply(world, 'runoff', 'methane', 'saturation')

def logic_12267(world):
    _world_apply(world, 'runoff', 'pathogen_load', 'gap')

def logic_12268(world):
    _world_apply(world, 'runoff', 'biodiversity', 'direct')

def logic_12269(world):
    _world_apply(world, 'runoff', 'habitat_stress', 'square')

def logic_12270(world):
    _world_apply(world, 'runoff', 'erosion', 'pulse')

def logic_12271(world):
    _world_apply(world, 'runoff', 'soil_depth', 'saturation')

def logic_12272(world):
    _world_apply(world, 'runoff', 'root_density', 'gap')

def logic_12273(world):
    _world_apply(world, 'runoff', 'wetland', 'square')

def logic_12274(world):
    _world_apply(world, 'runoff', 'carbon_storage', 'pulse')

def logic_12275(world):
    _world_apply(world, 'runoff', 'fire_risk', 'saturation')

def logic_12276(world):
    _world_apply(world, 'runoff', 'ash', 'gap')

def logic_12277(world):
    _world_apply(world, 'runoff', 'snowpack', 'direct')

def logic_12278(world):
    _world_apply(world, 'runoff', 'groundwater', 'square')

def logic_12279(world):
    _world_apply(world, 'runoff', 'sediment', 'pulse')

def logic_12280(world):
    _world_apply(world, 'runoff', 'salinity', 'saturation')

def logic_12281(world):
    _world_apply(world, 'runoff', 'algae', 'direct')

def logic_12282(world):
    _world_apply(world, 'runoff', 'organic_matter', 'square')

def logic_12283(world):
    _world_apply(world, 'runoff', 'deadwood', 'pulse')

def logic_12284(world):
    _world_apply(world, 'runoff', 'pollinators', 'saturation')

def logic_12285(world):
    _world_apply(world, 'runoff', 'flowers', 'gap')

def logic_12286(world):
    _world_apply(world, 'runoff', 'seed_bank', 'direct')

def logic_12287(world):
    _world_apply(world, 'runoff', 'soil_carbon', 'square')

def logic_12288(world):
    _world_apply(world, 'runoff', 'surface_ice', 'pulse')

def logic_12289(world):
    _world_apply(world, 'wind_x', 'temperature', 'gap')

def logic_12290(world):
    _world_apply(world, 'wind_x', 'surface_water', 'direct')

def logic_12291(world):
    _world_apply(world, 'wind_x', 'humidity', 'square')

def logic_12292(world):
    _world_apply(world, 'wind_x', 'cloud', 'pulse')

def logic_12293(world):
    _world_apply(world, 'wind_x', 'rain', 'saturation')

def logic_12294(world):
    _world_apply(world, 'wind_x', 'soil_moisture', 'gap')

def logic_12295(world):
    _world_apply(world, 'wind_x', 'runoff', 'direct')

def logic_12296(world):
    _world_apply(world, 'wind_x', 'wind_y', 'square')

def logic_12297(world):
    _world_apply(world, 'wind_x', 'vegetation', 'saturation')

def logic_12298(world):
    _world_apply(world, 'wind_x', 'biomass', 'gap')

def logic_12299(world):
    _world_apply(world, 'wind_x', 'herbivore', 'direct')

def logic_12300(world):
    _world_apply(world, 'wind_x', 'predator', 'square')

def logic_12301(world):
    _world_apply(world, 'wind_x', 'carrion', 'pulse')

def logic_12302(world):
    _world_apply(world, 'wind_x', 'nutrients', 'saturation')

def logic_12303(world):
    _world_apply(world, 'wind_x', 'decomposition_rate', 'gap')

def logic_12304(world):
    _world_apply(world, 'wind_x', 'oxygen', 'direct')

def logic_12305(world):
    _world_apply(world, 'wind_x', 'co2', 'pulse')

def logic_12306(world):
    _world_apply(world, 'wind_x', 'photosynthesis_factor', 'saturation')

def logic_12307(world):
    _world_apply(world, 'wind_x', 'ice', 'gap')

def logic_12308(world):
    _world_apply(world, 'wind_x', 'evaporation', 'direct')

def logic_12309(world):
    _world_apply(world, 'wind_x', 'detritus', 'square')

def logic_12310(world):
    _world_apply(world, 'wind_x', 'methane', 'pulse')

def logic_12311(world):
    _world_apply(world, 'wind_x', 'pathogen_load', 'saturation')

def logic_12312(world):
    _world_apply(world, 'wind_x', 'biodiversity', 'gap')

def logic_12313(world):
    _world_apply(world, 'wind_x', 'habitat_stress', 'square')

def logic_12314(world):
    _world_apply(world, 'wind_x', 'erosion', 'pulse')

def logic_12315(world):
    _world_apply(world, 'wind_x', 'soil_depth', 'saturation')

def logic_12316(world):
    _world_apply(world, 'wind_x', 'root_density', 'gap')

def logic_12317(world):
    _world_apply(world, 'wind_x', 'wetland', 'direct')

def logic_12318(world):
    _world_apply(world, 'wind_x', 'carbon_storage', 'square')

def logic_12319(world):
    _world_apply(world, 'wind_x', 'fire_risk', 'pulse')

def logic_12320(world):
    _world_apply(world, 'wind_x', 'ash', 'saturation')

def logic_12321(world):
    _world_apply(world, 'wind_x', 'snowpack', 'direct')

def logic_12322(world):
    _world_apply(world, 'wind_x', 'groundwater', 'square')

def logic_12323(world):
    _world_apply(world, 'wind_x', 'sediment', 'pulse')

def logic_12324(world):
    _world_apply(world, 'wind_x', 'salinity', 'saturation')

def logic_12325(world):
    _world_apply(world, 'wind_x', 'algae', 'gap')

def logic_12326(world):
    _world_apply(world, 'wind_x', 'organic_matter', 'direct')

def logic_12327(world):
    _world_apply(world, 'wind_x', 'deadwood', 'square')

def logic_12328(world):
    _world_apply(world, 'wind_x', 'pollinators', 'pulse')

def logic_12329(world):
    _world_apply(world, 'wind_x', 'flowers', 'gap')

def logic_12330(world):
    _world_apply(world, 'wind_x', 'seed_bank', 'direct')

def logic_12331(world):
    _world_apply(world, 'wind_x', 'soil_carbon', 'square')

def logic_12332(world):
    _world_apply(world, 'wind_x', 'surface_ice', 'pulse')

def logic_12333(world):
    _world_apply(world, 'wind_y', 'temperature', 'saturation')

def logic_12334(world):
    _world_apply(world, 'wind_y', 'surface_water', 'gap')

def logic_12335(world):
    _world_apply(world, 'wind_y', 'humidity', 'direct')

def logic_12336(world):
    _world_apply(world, 'wind_y', 'cloud', 'square')

def logic_12337(world):
    _world_apply(world, 'wind_y', 'rain', 'saturation')

def logic_12338(world):
    _world_apply(world, 'wind_y', 'soil_moisture', 'gap')

def logic_12339(world):
    _world_apply(world, 'wind_y', 'runoff', 'direct')

def logic_12340(world):
    _world_apply(world, 'wind_y', 'wind_x', 'square')

def logic_12341(world):
    _world_apply(world, 'wind_y', 'vegetation', 'pulse')

def logic_12342(world):
    _world_apply(world, 'wind_y', 'biomass', 'saturation')

def logic_12343(world):
    _world_apply(world, 'wind_y', 'herbivore', 'gap')

def logic_12344(world):
    _world_apply(world, 'wind_y', 'predator', 'direct')

def logic_12345(world):
    _world_apply(world, 'wind_y', 'carrion', 'pulse')

def logic_12346(world):
    _world_apply(world, 'wind_y', 'nutrients', 'saturation')

def logic_12347(world):
    _world_apply(world, 'wind_y', 'decomposition_rate', 'gap')

def logic_12348(world):
    _world_apply(world, 'wind_y', 'oxygen', 'direct')

def logic_12349(world):
    _world_apply(world, 'wind_y', 'co2', 'square')

def logic_12350(world):
    _world_apply(world, 'wind_y', 'photosynthesis_factor', 'pulse')

def logic_12351(world):
    _world_apply(world, 'wind_y', 'ice', 'saturation')

def logic_12352(world):
    _world_apply(world, 'wind_y', 'evaporation', 'gap')

def logic_12353(world):
    _world_apply(world, 'wind_y', 'detritus', 'square')

def logic_12354(world):
    _world_apply(world, 'wind_y', 'methane', 'pulse')

def logic_12355(world):
    _world_apply(world, 'wind_y', 'pathogen_load', 'saturation')

def logic_12356(world):
    _world_apply(world, 'wind_y', 'biodiversity', 'gap')

def logic_12357(world):
    _world_apply(world, 'wind_y', 'habitat_stress', 'direct')

def logic_12358(world):
    _world_apply(world, 'wind_y', 'erosion', 'square')

def logic_12359(world):
    _world_apply(world, 'wind_y', 'soil_depth', 'pulse')

def logic_12360(world):
    _world_apply(world, 'wind_y', 'root_density', 'saturation')

def logic_12361(world):
    _world_apply(world, 'wind_y', 'wetland', 'direct')

def logic_12362(world):
    _world_apply(world, 'wind_y', 'carbon_storage', 'square')

def logic_12363(world):
    _world_apply(world, 'wind_y', 'fire_risk', 'pulse')

def logic_12364(world):
    _world_apply(world, 'wind_y', 'ash', 'saturation')

def logic_12365(world):
    _world_apply(world, 'wind_y', 'snowpack', 'gap')

def logic_12366(world):
    _world_apply(world, 'wind_y', 'groundwater', 'direct')

def logic_12367(world):
    _world_apply(world, 'wind_y', 'sediment', 'square')

def logic_12368(world):
    _world_apply(world, 'wind_y', 'salinity', 'pulse')

def logic_12369(world):
    _world_apply(world, 'wind_y', 'algae', 'gap')

def logic_12370(world):
    _world_apply(world, 'wind_y', 'organic_matter', 'direct')

def logic_12371(world):
    _world_apply(world, 'wind_y', 'deadwood', 'square')

def logic_12372(world):
    _world_apply(world, 'wind_y', 'pollinators', 'pulse')

def logic_12373(world):
    _world_apply(world, 'wind_y', 'flowers', 'saturation')

def logic_12374(world):
    _world_apply(world, 'wind_y', 'seed_bank', 'gap')

def logic_12375(world):
    _world_apply(world, 'wind_y', 'soil_carbon', 'direct')

def logic_12376(world):
    _world_apply(world, 'wind_y', 'surface_ice', 'square')

def logic_12377(world):
    _world_apply(world, 'vegetation', 'temperature', 'saturation')

def logic_12378(world):
    _world_apply(world, 'vegetation', 'surface_water', 'gap')

def logic_12379(world):
    _world_apply(world, 'vegetation', 'humidity', 'direct')

def logic_12380(world):
    _world_apply(world, 'vegetation', 'cloud', 'square')

def logic_12381(world):
    _world_apply(world, 'vegetation', 'rain', 'pulse')

def logic_12382(world):
    _world_apply(world, 'vegetation', 'soil_moisture', 'saturation')

def logic_12383(world):
    _world_apply(world, 'vegetation', 'runoff', 'gap')

def logic_12384(world):
    _world_apply(world, 'vegetation', 'wind_x', 'direct')

def logic_12385(world):
    _world_apply(world, 'vegetation', 'wind_y', 'pulse')

def logic_12386(world):
    _world_apply(world, 'vegetation', 'biomass', 'saturation')

def logic_12387(world):
    _world_apply(world, 'vegetation', 'herbivore', 'gap')

def logic_12388(world):
    _world_apply(world, 'vegetation', 'predator', 'direct')

def logic_12389(world):
    _world_apply(world, 'vegetation', 'carrion', 'square')

def logic_12390(world):
    _world_apply(world, 'vegetation', 'nutrients', 'pulse')

def logic_12391(world):
    _world_apply(world, 'vegetation', 'decomposition_rate', 'saturation')

def logic_12392(world):
    _world_apply(world, 'vegetation', 'oxygen', 'gap')

def logic_12393(world):
    _world_apply(world, 'vegetation', 'co2', 'square')

def logic_12394(world):
    _world_apply(world, 'vegetation', 'photosynthesis_factor', 'pulse')

def logic_12395(world):
    _world_apply(world, 'vegetation', 'ice', 'saturation')

def logic_12396(world):
    _world_apply(world, 'vegetation', 'evaporation', 'gap')

def logic_12397(world):
    _world_apply(world, 'vegetation', 'detritus', 'direct')

def logic_12398(world):
    _world_apply(world, 'vegetation', 'methane', 'square')

def logic_12399(world):
    _world_apply(world, 'vegetation', 'pathogen_load', 'pulse')

def logic_12400(world):
    _world_apply(world, 'vegetation', 'biodiversity', 'saturation')

def logic_12401(world):
    _world_apply(world, 'vegetation', 'habitat_stress', 'direct')

def logic_12402(world):
    _world_apply(world, 'vegetation', 'erosion', 'square')

def logic_12403(world):
    _world_apply(world, 'vegetation', 'soil_depth', 'pulse')

def logic_12404(world):
    _world_apply(world, 'vegetation', 'root_density', 'saturation')

def logic_12405(world):
    _world_apply(world, 'vegetation', 'wetland', 'gap')

def logic_12406(world):
    _world_apply(world, 'vegetation', 'carbon_storage', 'direct')

def logic_12407(world):
    _world_apply(world, 'vegetation', 'fire_risk', 'square')

def logic_12408(world):
    _world_apply(world, 'vegetation', 'ash', 'pulse')

def logic_12409(world):
    _world_apply(world, 'vegetation', 'snowpack', 'gap')

def logic_12410(world):
    _world_apply(world, 'vegetation', 'groundwater', 'direct')

def logic_12411(world):
    _world_apply(world, 'vegetation', 'sediment', 'square')

def logic_12412(world):
    _world_apply(world, 'vegetation', 'salinity', 'pulse')

def logic_12413(world):
    _world_apply(world, 'vegetation', 'algae', 'saturation')

def logic_12414(world):
    _world_apply(world, 'vegetation', 'organic_matter', 'gap')

def logic_12415(world):
    _world_apply(world, 'vegetation', 'deadwood', 'direct')

def logic_12416(world):
    _world_apply(world, 'vegetation', 'pollinators', 'square')

def logic_12417(world):
    _world_apply(world, 'vegetation', 'flowers', 'saturation')

def logic_12418(world):
    _world_apply(world, 'vegetation', 'seed_bank', 'gap')

def logic_12419(world):
    _world_apply(world, 'vegetation', 'soil_carbon', 'direct')

def logic_12420(world):
    _world_apply(world, 'vegetation', 'surface_ice', 'square')

def logic_12421(world):
    _world_apply(world, 'biomass', 'temperature', 'pulse')

def logic_12422(world):
    _world_apply(world, 'biomass', 'surface_water', 'saturation')

def logic_12423(world):
    _world_apply(world, 'biomass', 'humidity', 'gap')

def logic_12424(world):
    _world_apply(world, 'biomass', 'cloud', 'direct')

def logic_12425(world):
    _world_apply(world, 'biomass', 'rain', 'pulse')

def logic_12426(world):
    _world_apply(world, 'biomass', 'soil_moisture', 'saturation')

def logic_12427(world):
    _world_apply(world, 'biomass', 'runoff', 'gap')

def logic_12428(world):
    _world_apply(world, 'biomass', 'wind_x', 'direct')

def logic_12429(world):
    _world_apply(world, 'biomass', 'wind_y', 'square')

def logic_12430(world):
    _world_apply(world, 'biomass', 'vegetation', 'pulse')

def logic_12431(world):
    _world_apply(world, 'biomass', 'herbivore', 'saturation')

def logic_12432(world):
    _world_apply(world, 'biomass', 'predator', 'gap')

def logic_12433(world):
    _world_apply(world, 'biomass', 'carrion', 'square')

def logic_12434(world):
    _world_apply(world, 'biomass', 'nutrients', 'pulse')

def logic_12435(world):
    _world_apply(world, 'biomass', 'decomposition_rate', 'saturation')

def logic_12436(world):
    _world_apply(world, 'biomass', 'oxygen', 'gap')

def logic_12437(world):
    _world_apply(world, 'biomass', 'co2', 'direct')

def logic_12438(world):
    _world_apply(world, 'biomass', 'photosynthesis_factor', 'square')

def logic_12439(world):
    _world_apply(world, 'biomass', 'ice', 'pulse')

def logic_12440(world):
    _world_apply(world, 'biomass', 'evaporation', 'saturation')

def logic_12441(world):
    _world_apply(world, 'biomass', 'detritus', 'direct')

def logic_12442(world):
    _world_apply(world, 'biomass', 'methane', 'square')

def logic_12443(world):
    _world_apply(world, 'biomass', 'pathogen_load', 'pulse')

def logic_12444(world):
    _world_apply(world, 'biomass', 'biodiversity', 'saturation')

def logic_12445(world):
    _world_apply(world, 'biomass', 'habitat_stress', 'gap')

def logic_12446(world):
    _world_apply(world, 'biomass', 'erosion', 'direct')

def logic_12447(world):
    _world_apply(world, 'biomass', 'soil_depth', 'square')

def logic_12448(world):
    _world_apply(world, 'biomass', 'root_density', 'pulse')

def logic_12449(world):
    _world_apply(world, 'biomass', 'wetland', 'gap')

def logic_12450(world):
    _world_apply(world, 'biomass', 'carbon_storage', 'direct')

def logic_12451(world):
    _world_apply(world, 'biomass', 'fire_risk', 'square')

def logic_12452(world):
    _world_apply(world, 'biomass', 'ash', 'pulse')

def logic_12453(world):
    _world_apply(world, 'biomass', 'snowpack', 'saturation')

def logic_12454(world):
    _world_apply(world, 'biomass', 'groundwater', 'gap')

def logic_12455(world):
    _world_apply(world, 'biomass', 'sediment', 'direct')

def logic_12456(world):
    _world_apply(world, 'biomass', 'salinity', 'square')

def logic_12457(world):
    _world_apply(world, 'biomass', 'algae', 'saturation')

def logic_12458(world):
    _world_apply(world, 'biomass', 'organic_matter', 'gap')

def logic_12459(world):
    _world_apply(world, 'biomass', 'deadwood', 'direct')

def logic_12460(world):
    _world_apply(world, 'biomass', 'pollinators', 'square')

def logic_12461(world):
    _world_apply(world, 'biomass', 'flowers', 'pulse')

def logic_12462(world):
    _world_apply(world, 'biomass', 'seed_bank', 'saturation')

def logic_12463(world):
    _world_apply(world, 'biomass', 'soil_carbon', 'gap')

def logic_12464(world):
    _world_apply(world, 'biomass', 'surface_ice', 'direct')

def logic_12465(world):
    _world_apply(world, 'herbivore', 'temperature', 'pulse')

def logic_12466(world):
    _world_apply(world, 'herbivore', 'surface_water', 'saturation')

def logic_12467(world):
    _world_apply(world, 'herbivore', 'humidity', 'gap')

def logic_12468(world):
    _world_apply(world, 'herbivore', 'cloud', 'direct')

def logic_12469(world):
    _world_apply(world, 'herbivore', 'rain', 'square')

def logic_12470(world):
    _world_apply(world, 'herbivore', 'soil_moisture', 'pulse')

def logic_12471(world):
    _world_apply(world, 'herbivore', 'runoff', 'saturation')

def logic_12472(world):
    _world_apply(world, 'herbivore', 'wind_x', 'gap')

def logic_12473(world):
    _world_apply(world, 'herbivore', 'wind_y', 'square')

def logic_12474(world):
    _world_apply(world, 'herbivore', 'vegetation', 'pulse')

def logic_12475(world):
    _world_apply(world, 'herbivore', 'biomass', 'saturation')

def logic_12476(world):
    _world_apply(world, 'herbivore', 'predator', 'gap')

def logic_12477(world):
    _world_apply(world, 'herbivore', 'carrion', 'direct')

def logic_12478(world):
    _world_apply(world, 'herbivore', 'nutrients', 'square')

def logic_12479(world):
    _world_apply(world, 'herbivore', 'decomposition_rate', 'pulse')

def logic_12480(world):
    _world_apply(world, 'herbivore', 'oxygen', 'saturation')

def logic_12481(world):
    _world_apply(world, 'herbivore', 'co2', 'direct')

def logic_12482(world):
    _world_apply(world, 'herbivore', 'photosynthesis_factor', 'square')

def logic_12483(world):
    _world_apply(world, 'herbivore', 'ice', 'pulse')

def logic_12484(world):
    _world_apply(world, 'herbivore', 'evaporation', 'saturation')

def logic_12485(world):
    _world_apply(world, 'herbivore', 'detritus', 'gap')

def logic_12486(world):
    _world_apply(world, 'herbivore', 'methane', 'direct')

def logic_12487(world):
    _world_apply(world, 'herbivore', 'pathogen_load', 'square')

def logic_12488(world):
    _world_apply(world, 'herbivore', 'biodiversity', 'pulse')

def logic_12489(world):
    _world_apply(world, 'herbivore', 'habitat_stress', 'gap')

def logic_12490(world):
    _world_apply(world, 'herbivore', 'erosion', 'direct')

def logic_12491(world):
    _world_apply(world, 'herbivore', 'soil_depth', 'square')

def logic_12492(world):
    _world_apply(world, 'herbivore', 'root_density', 'pulse')

def logic_12493(world):
    _world_apply(world, 'herbivore', 'wetland', 'saturation')

def logic_12494(world):
    _world_apply(world, 'herbivore', 'carbon_storage', 'gap')

def logic_12495(world):
    _world_apply(world, 'herbivore', 'fire_risk', 'direct')

def logic_12496(world):
    _world_apply(world, 'herbivore', 'ash', 'square')

def logic_12497(world):
    _world_apply(world, 'herbivore', 'snowpack', 'saturation')

def logic_12498(world):
    _world_apply(world, 'herbivore', 'groundwater', 'gap')

def logic_12499(world):
    _world_apply(world, 'herbivore', 'sediment', 'direct')

def logic_12500(world):
    _world_apply(world, 'herbivore', 'salinity', 'square')

def logic_12501(world):
    _world_apply(world, 'herbivore', 'algae', 'pulse')

def logic_12502(world):
    _world_apply(world, 'herbivore', 'organic_matter', 'saturation')

def logic_12503(world):
    _world_apply(world, 'herbivore', 'deadwood', 'gap')

def logic_12504(world):
    _world_apply(world, 'herbivore', 'pollinators', 'direct')

def logic_12505(world):
    _world_apply(world, 'herbivore', 'flowers', 'pulse')

def logic_12506(world):
    _world_apply(world, 'herbivore', 'seed_bank', 'saturation')

def logic_12507(world):
    _world_apply(world, 'herbivore', 'soil_carbon', 'gap')

def logic_12508(world):
    _world_apply(world, 'herbivore', 'surface_ice', 'direct')

def logic_12509(world):
    _world_apply(world, 'predator', 'temperature', 'square')

def logic_12510(world):
    _world_apply(world, 'predator', 'surface_water', 'pulse')

def logic_12511(world):
    _world_apply(world, 'predator', 'humidity', 'saturation')

def logic_12512(world):
    _world_apply(world, 'predator', 'cloud', 'gap')

def logic_12513(world):
    _world_apply(world, 'predator', 'rain', 'square')

def logic_12514(world):
    _world_apply(world, 'predator', 'soil_moisture', 'pulse')

def logic_12515(world):
    _world_apply(world, 'predator', 'runoff', 'saturation')

def logic_12516(world):
    _world_apply(world, 'predator', 'wind_x', 'gap')

def logic_12517(world):
    _world_apply(world, 'predator', 'wind_y', 'direct')

def logic_12518(world):
    _world_apply(world, 'predator', 'vegetation', 'square')

def logic_12519(world):
    _world_apply(world, 'predator', 'biomass', 'pulse')

def logic_12520(world):
    _world_apply(world, 'predator', 'herbivore', 'saturation')

def logic_12521(world):
    _world_apply(world, 'predator', 'carrion', 'direct')

def logic_12522(world):
    _world_apply(world, 'predator', 'nutrients', 'square')

def logic_12523(world):
    _world_apply(world, 'predator', 'decomposition_rate', 'pulse')

def logic_12524(world):
    _world_apply(world, 'predator', 'oxygen', 'saturation')

def logic_12525(world):
    _world_apply(world, 'predator', 'co2', 'gap')

def logic_12526(world):
    _world_apply(world, 'predator', 'photosynthesis_factor', 'direct')

def logic_12527(world):
    _world_apply(world, 'predator', 'ice', 'square')

def logic_12528(world):
    _world_apply(world, 'predator', 'evaporation', 'pulse')

def logic_12529(world):
    _world_apply(world, 'predator', 'detritus', 'gap')

def logic_12530(world):
    _world_apply(world, 'predator', 'methane', 'direct')

def logic_12531(world):
    _world_apply(world, 'predator', 'pathogen_load', 'square')

def logic_12532(world):
    _world_apply(world, 'predator', 'biodiversity', 'pulse')

def logic_12533(world):
    _world_apply(world, 'predator', 'habitat_stress', 'saturation')

def logic_12534(world):
    _world_apply(world, 'predator', 'erosion', 'gap')

def logic_12535(world):
    _world_apply(world, 'predator', 'soil_depth', 'direct')

def logic_12536(world):
    _world_apply(world, 'predator', 'root_density', 'square')

def logic_12537(world):
    _world_apply(world, 'predator', 'wetland', 'saturation')

def logic_12538(world):
    _world_apply(world, 'predator', 'carbon_storage', 'gap')

def logic_12539(world):
    _world_apply(world, 'predator', 'fire_risk', 'direct')

def logic_12540(world):
    _world_apply(world, 'predator', 'ash', 'square')

def logic_12541(world):
    _world_apply(world, 'predator', 'snowpack', 'pulse')

def logic_12542(world):
    _world_apply(world, 'predator', 'groundwater', 'saturation')

def logic_12543(world):
    _world_apply(world, 'predator', 'sediment', 'gap')

def logic_12544(world):
    _world_apply(world, 'predator', 'salinity', 'direct')

def logic_12545(world):
    _world_apply(world, 'predator', 'algae', 'pulse')

def logic_12546(world):
    _world_apply(world, 'predator', 'organic_matter', 'saturation')

def logic_12547(world):
    _world_apply(world, 'predator', 'deadwood', 'gap')

def logic_12548(world):
    _world_apply(world, 'predator', 'pollinators', 'direct')

def logic_12549(world):
    _world_apply(world, 'predator', 'flowers', 'square')

def logic_12550(world):
    _world_apply(world, 'predator', 'seed_bank', 'pulse')

def logic_12551(world):
    _world_apply(world, 'predator', 'soil_carbon', 'saturation')

def logic_12552(world):
    _world_apply(world, 'predator', 'surface_ice', 'gap')

def logic_12553(world):
    _world_apply(world, 'carrion', 'temperature', 'square')

def logic_12554(world):
    _world_apply(world, 'carrion', 'surface_water', 'pulse')

def logic_12555(world):
    _world_apply(world, 'carrion', 'humidity', 'saturation')

def logic_12556(world):
    _world_apply(world, 'carrion', 'cloud', 'gap')

def logic_12557(world):
    _world_apply(world, 'carrion', 'rain', 'direct')

def logic_12558(world):
    _world_apply(world, 'carrion', 'soil_moisture', 'square')

def logic_12559(world):
    _world_apply(world, 'carrion', 'runoff', 'pulse')

def logic_12560(world):
    _world_apply(world, 'carrion', 'wind_x', 'saturation')

def logic_12561(world):
    _world_apply(world, 'carrion', 'wind_y', 'direct')

def logic_12562(world):
    _world_apply(world, 'carrion', 'vegetation', 'square')

def logic_12563(world):
    _world_apply(world, 'carrion', 'biomass', 'pulse')

def logic_12564(world):
    _world_apply(world, 'carrion', 'herbivore', 'saturation')

def logic_12565(world):
    _world_apply(world, 'carrion', 'predator', 'gap')

def logic_12566(world):
    _world_apply(world, 'carrion', 'nutrients', 'direct')

def logic_12567(world):
    _world_apply(world, 'carrion', 'decomposition_rate', 'square')

def logic_12568(world):
    _world_apply(world, 'carrion', 'oxygen', 'pulse')

def logic_12569(world):
    _world_apply(world, 'carrion', 'co2', 'gap')

def logic_12570(world):
    _world_apply(world, 'carrion', 'photosynthesis_factor', 'direct')

def logic_12571(world):
    _world_apply(world, 'carrion', 'ice', 'square')

def logic_12572(world):
    _world_apply(world, 'carrion', 'evaporation', 'pulse')

def logic_12573(world):
    _world_apply(world, 'carrion', 'detritus', 'saturation')

def logic_12574(world):
    _world_apply(world, 'carrion', 'methane', 'gap')

def logic_12575(world):
    _world_apply(world, 'carrion', 'pathogen_load', 'direct')

def logic_12576(world):
    _world_apply(world, 'carrion', 'biodiversity', 'square')

def logic_12577(world):
    _world_apply(world, 'carrion', 'habitat_stress', 'saturation')

def logic_12578(world):
    _world_apply(world, 'carrion', 'erosion', 'gap')

def logic_12579(world):
    _world_apply(world, 'carrion', 'soil_depth', 'direct')

def logic_12580(world):
    _world_apply(world, 'carrion', 'root_density', 'square')

def logic_12581(world):
    _world_apply(world, 'carrion', 'wetland', 'pulse')

def logic_12582(world):
    _world_apply(world, 'carrion', 'carbon_storage', 'saturation')

def logic_12583(world):
    _world_apply(world, 'carrion', 'fire_risk', 'gap')

def logic_12584(world):
    _world_apply(world, 'carrion', 'ash', 'direct')

def logic_12585(world):
    _world_apply(world, 'carrion', 'snowpack', 'pulse')

def logic_12586(world):
    _world_apply(world, 'carrion', 'groundwater', 'saturation')

def logic_12587(world):
    _world_apply(world, 'carrion', 'sediment', 'gap')

def logic_12588(world):
    _world_apply(world, 'carrion', 'salinity', 'direct')

def logic_12589(world):
    _world_apply(world, 'carrion', 'algae', 'square')

def logic_12590(world):
    _world_apply(world, 'carrion', 'organic_matter', 'pulse')

def logic_12591(world):
    _world_apply(world, 'carrion', 'deadwood', 'saturation')

def logic_12592(world):
    _world_apply(world, 'carrion', 'pollinators', 'gap')

def logic_12593(world):
    _world_apply(world, 'carrion', 'flowers', 'square')

def logic_12594(world):
    _world_apply(world, 'carrion', 'seed_bank', 'pulse')

def logic_12595(world):
    _world_apply(world, 'carrion', 'soil_carbon', 'saturation')

def logic_12596(world):
    _world_apply(world, 'carrion', 'surface_ice', 'gap')

def logic_12597(world):
    _world_apply(world, 'nutrients', 'temperature', 'direct')

def logic_12598(world):
    _world_apply(world, 'nutrients', 'surface_water', 'square')

def logic_12599(world):
    _world_apply(world, 'nutrients', 'humidity', 'pulse')

def logic_12600(world):
    _world_apply(world, 'nutrients', 'cloud', 'saturation')

def logic_12601(world):
    _world_apply(world, 'nutrients', 'rain', 'direct')

def logic_12602(world):
    _world_apply(world, 'nutrients', 'soil_moisture', 'square')

def logic_12603(world):
    _world_apply(world, 'nutrients', 'runoff', 'pulse')

def logic_12604(world):
    _world_apply(world, 'nutrients', 'wind_x', 'saturation')

def logic_12605(world):
    _world_apply(world, 'nutrients', 'wind_y', 'gap')

def logic_12606(world):
    _world_apply(world, 'nutrients', 'vegetation', 'direct')

def logic_12607(world):
    _world_apply(world, 'nutrients', 'biomass', 'square')

def logic_12608(world):
    _world_apply(world, 'nutrients', 'herbivore', 'pulse')

def logic_12609(world):
    _world_apply(world, 'nutrients', 'predator', 'gap')

def logic_12610(world):
    _world_apply(world, 'nutrients', 'carrion', 'direct')

def logic_12611(world):
    _world_apply(world, 'nutrients', 'decomposition_rate', 'square')

def logic_12612(world):
    _world_apply(world, 'nutrients', 'oxygen', 'pulse')

def logic_12613(world):
    _world_apply(world, 'nutrients', 'co2', 'saturation')

def logic_12614(world):
    _world_apply(world, 'nutrients', 'photosynthesis_factor', 'gap')

def logic_12615(world):
    _world_apply(world, 'nutrients', 'ice', 'direct')

def logic_12616(world):
    _world_apply(world, 'nutrients', 'evaporation', 'square')

def logic_12617(world):
    _world_apply(world, 'nutrients', 'detritus', 'saturation')

def logic_12618(world):
    _world_apply(world, 'nutrients', 'methane', 'gap')

def logic_12619(world):
    _world_apply(world, 'nutrients', 'pathogen_load', 'direct')

def logic_12620(world):
    _world_apply(world, 'nutrients', 'biodiversity', 'square')

def logic_12621(world):
    _world_apply(world, 'nutrients', 'habitat_stress', 'pulse')

def logic_12622(world):
    _world_apply(world, 'nutrients', 'erosion', 'saturation')

def logic_12623(world):
    _world_apply(world, 'nutrients', 'soil_depth', 'gap')

def logic_12624(world):
    _world_apply(world, 'nutrients', 'root_density', 'direct')

def logic_12625(world):
    _world_apply(world, 'nutrients', 'wetland', 'pulse')

def logic_12626(world):
    _world_apply(world, 'nutrients', 'carbon_storage', 'saturation')

def logic_12627(world):
    _world_apply(world, 'nutrients', 'fire_risk', 'gap')

def logic_12628(world):
    _world_apply(world, 'nutrients', 'ash', 'direct')

def logic_12629(world):
    _world_apply(world, 'nutrients', 'snowpack', 'square')

def logic_12630(world):
    _world_apply(world, 'nutrients', 'groundwater', 'pulse')

def logic_12631(world):
    _world_apply(world, 'nutrients', 'sediment', 'saturation')

def logic_12632(world):
    _world_apply(world, 'nutrients', 'salinity', 'gap')

def logic_12633(world):
    _world_apply(world, 'nutrients', 'algae', 'square')

def logic_12634(world):
    _world_apply(world, 'nutrients', 'organic_matter', 'pulse')

def logic_12635(world):
    _world_apply(world, 'nutrients', 'deadwood', 'saturation')

def logic_12636(world):
    _world_apply(world, 'nutrients', 'pollinators', 'gap')

def logic_12637(world):
    _world_apply(world, 'nutrients', 'flowers', 'direct')

def logic_12638(world):
    _world_apply(world, 'nutrients', 'seed_bank', 'square')

def logic_12639(world):
    _world_apply(world, 'nutrients', 'soil_carbon', 'pulse')

def logic_12640(world):
    _world_apply(world, 'nutrients', 'surface_ice', 'saturation')

def logic_12641(world):
    _world_apply(world, 'decomposition_rate', 'temperature', 'direct')

def logic_12642(world):
    _world_apply(world, 'decomposition_rate', 'surface_water', 'square')

def logic_12643(world):
    _world_apply(world, 'decomposition_rate', 'humidity', 'pulse')

def logic_12644(world):
    _world_apply(world, 'decomposition_rate', 'cloud', 'saturation')

def logic_12645(world):
    _world_apply(world, 'decomposition_rate', 'rain', 'gap')

def logic_12646(world):
    _world_apply(world, 'decomposition_rate', 'soil_moisture', 'direct')

def logic_12647(world):
    _world_apply(world, 'decomposition_rate', 'runoff', 'square')

def logic_12648(world):
    _world_apply(world, 'decomposition_rate', 'wind_x', 'pulse')

def logic_12649(world):
    _world_apply(world, 'decomposition_rate', 'wind_y', 'gap')

def logic_12650(world):
    _world_apply(world, 'decomposition_rate', 'vegetation', 'direct')

def logic_12651(world):
    _world_apply(world, 'decomposition_rate', 'biomass', 'square')

def logic_12652(world):
    _world_apply(world, 'decomposition_rate', 'herbivore', 'pulse')

def logic_12653(world):
    _world_apply(world, 'decomposition_rate', 'predator', 'saturation')

def logic_12654(world):
    _world_apply(world, 'decomposition_rate', 'carrion', 'gap')

def logic_12655(world):
    _world_apply(world, 'decomposition_rate', 'nutrients', 'direct')

def logic_12656(world):
    _world_apply(world, 'decomposition_rate', 'oxygen', 'square')

def logic_12657(world):
    _world_apply(world, 'decomposition_rate', 'co2', 'saturation')

def logic_12658(world):
    _world_apply(world, 'decomposition_rate', 'photosynthesis_factor', 'gap')

def logic_12659(world):
    _world_apply(world, 'decomposition_rate', 'ice', 'direct')

def logic_12660(world):
    _world_apply(world, 'decomposition_rate', 'evaporation', 'square')

def logic_12661(world):
    _world_apply(world, 'decomposition_rate', 'detritus', 'pulse')

def logic_12662(world):
    _world_apply(world, 'decomposition_rate', 'methane', 'saturation')

def logic_12663(world):
    _world_apply(world, 'decomposition_rate', 'pathogen_load', 'gap')

def logic_12664(world):
    _world_apply(world, 'decomposition_rate', 'biodiversity', 'direct')

def logic_12665(world):
    _world_apply(world, 'decomposition_rate', 'habitat_stress', 'pulse')

def logic_12666(world):
    _world_apply(world, 'decomposition_rate', 'erosion', 'saturation')

def logic_12667(world):
    _world_apply(world, 'decomposition_rate', 'soil_depth', 'gap')

def logic_12668(world):
    _world_apply(world, 'decomposition_rate', 'root_density', 'direct')

def logic_12669(world):
    _world_apply(world, 'decomposition_rate', 'wetland', 'square')

def logic_12670(world):
    _world_apply(world, 'decomposition_rate', 'carbon_storage', 'pulse')

def logic_12671(world):
    _world_apply(world, 'decomposition_rate', 'fire_risk', 'saturation')

def logic_12672(world):
    _world_apply(world, 'decomposition_rate', 'ash', 'gap')

def logic_12673(world):
    _world_apply(world, 'decomposition_rate', 'snowpack', 'square')

def logic_12674(world):
    _world_apply(world, 'decomposition_rate', 'groundwater', 'pulse')

def logic_12675(world):
    _world_apply(world, 'decomposition_rate', 'sediment', 'saturation')

def logic_12676(world):
    _world_apply(world, 'decomposition_rate', 'salinity', 'gap')

def logic_12677(world):
    _world_apply(world, 'decomposition_rate', 'algae', 'direct')

def logic_12678(world):
    _world_apply(world, 'decomposition_rate', 'organic_matter', 'square')

def logic_12679(world):
    _world_apply(world, 'decomposition_rate', 'deadwood', 'pulse')

def logic_12680(world):
    _world_apply(world, 'decomposition_rate', 'pollinators', 'saturation')

def logic_12681(world):
    _world_apply(world, 'decomposition_rate', 'flowers', 'direct')

def logic_12682(world):
    _world_apply(world, 'decomposition_rate', 'seed_bank', 'square')

def logic_12683(world):
    _world_apply(world, 'decomposition_rate', 'soil_carbon', 'pulse')

def logic_12684(world):
    _world_apply(world, 'decomposition_rate', 'surface_ice', 'saturation')

def logic_12685(world):
    _world_apply(world, 'oxygen', 'temperature', 'gap')

def logic_12686(world):
    _world_apply(world, 'oxygen', 'surface_water', 'direct')

def logic_12687(world):
    _world_apply(world, 'oxygen', 'humidity', 'square')

def logic_12688(world):
    _world_apply(world, 'oxygen', 'cloud', 'pulse')

def logic_12689(world):
    _world_apply(world, 'oxygen', 'rain', 'gap')

def logic_12690(world):
    _world_apply(world, 'oxygen', 'soil_moisture', 'direct')

def logic_12691(world):
    _world_apply(world, 'oxygen', 'runoff', 'square')

def logic_12692(world):
    _world_apply(world, 'oxygen', 'wind_x', 'pulse')

def logic_12693(world):
    _world_apply(world, 'oxygen', 'wind_y', 'saturation')

def logic_12694(world):
    _world_apply(world, 'oxygen', 'vegetation', 'gap')

def logic_12695(world):
    _world_apply(world, 'oxygen', 'biomass', 'direct')

def logic_12696(world):
    _world_apply(world, 'oxygen', 'herbivore', 'square')

def logic_12697(world):
    _world_apply(world, 'oxygen', 'predator', 'saturation')

def logic_12698(world):
    _world_apply(world, 'oxygen', 'carrion', 'gap')

def logic_12699(world):
    _world_apply(world, 'oxygen', 'nutrients', 'direct')

def logic_12700(world):
    _world_apply(world, 'oxygen', 'decomposition_rate', 'square')

def logic_12701(world):
    _world_apply(world, 'oxygen', 'co2', 'pulse')

def logic_12702(world):
    _world_apply(world, 'oxygen', 'photosynthesis_factor', 'saturation')

def logic_12703(world):
    _world_apply(world, 'oxygen', 'ice', 'gap')

def logic_12704(world):
    _world_apply(world, 'oxygen', 'evaporation', 'direct')

def logic_12705(world):
    _world_apply(world, 'oxygen', 'detritus', 'pulse')

def logic_12706(world):
    _world_apply(world, 'oxygen', 'methane', 'saturation')

def logic_12707(world):
    _world_apply(world, 'oxygen', 'pathogen_load', 'gap')

def logic_12708(world):
    _world_apply(world, 'oxygen', 'biodiversity', 'direct')

def logic_12709(world):
    _world_apply(world, 'oxygen', 'habitat_stress', 'square')

def logic_12710(world):
    _world_apply(world, 'oxygen', 'erosion', 'pulse')

def logic_12711(world):
    _world_apply(world, 'oxygen', 'soil_depth', 'saturation')

def logic_12712(world):
    _world_apply(world, 'oxygen', 'root_density', 'gap')

def logic_12713(world):
    _world_apply(world, 'oxygen', 'wetland', 'square')

def logic_12714(world):
    _world_apply(world, 'oxygen', 'carbon_storage', 'pulse')

def logic_12715(world):
    _world_apply(world, 'oxygen', 'fire_risk', 'saturation')

def logic_12716(world):
    _world_apply(world, 'oxygen', 'ash', 'gap')

def logic_12717(world):
    _world_apply(world, 'oxygen', 'snowpack', 'direct')

def logic_12718(world):
    _world_apply(world, 'oxygen', 'groundwater', 'square')

def logic_12719(world):
    _world_apply(world, 'oxygen', 'sediment', 'pulse')

def logic_12720(world):
    _world_apply(world, 'oxygen', 'salinity', 'saturation')

def logic_12721(world):
    _world_apply(world, 'oxygen', 'algae', 'direct')

def logic_12722(world):
    _world_apply(world, 'oxygen', 'organic_matter', 'square')

def logic_12723(world):
    _world_apply(world, 'oxygen', 'deadwood', 'pulse')

def logic_12724(world):
    _world_apply(world, 'oxygen', 'pollinators', 'saturation')

def logic_12725(world):
    _world_apply(world, 'oxygen', 'flowers', 'gap')

def logic_12726(world):
    _world_apply(world, 'oxygen', 'seed_bank', 'direct')

def logic_12727(world):
    _world_apply(world, 'oxygen', 'soil_carbon', 'square')

def logic_12728(world):
    _world_apply(world, 'oxygen', 'surface_ice', 'pulse')

def logic_12729(world):
    _world_apply(world, 'co2', 'temperature', 'gap')

def logic_12730(world):
    _world_apply(world, 'co2', 'surface_water', 'direct')

def logic_12731(world):
    _world_apply(world, 'co2', 'humidity', 'square')

def logic_12732(world):
    _world_apply(world, 'co2', 'cloud', 'pulse')

def logic_12733(world):
    _world_apply(world, 'co2', 'rain', 'saturation')

def logic_12734(world):
    _world_apply(world, 'co2', 'soil_moisture', 'gap')

def logic_12735(world):
    _world_apply(world, 'co2', 'runoff', 'direct')

def logic_12736(world):
    _world_apply(world, 'co2', 'wind_x', 'square')

def logic_12737(world):
    _world_apply(world, 'co2', 'wind_y', 'saturation')

def logic_12738(world):
    _world_apply(world, 'co2', 'vegetation', 'gap')

def logic_12739(world):
    _world_apply(world, 'co2', 'biomass', 'direct')

def logic_12740(world):
    _world_apply(world, 'co2', 'herbivore', 'square')

def logic_12741(world):
    _world_apply(world, 'co2', 'predator', 'pulse')

def logic_12742(world):
    _world_apply(world, 'co2', 'carrion', 'saturation')

def logic_12743(world):
    _world_apply(world, 'co2', 'nutrients', 'gap')

def logic_12744(world):
    _world_apply(world, 'co2', 'decomposition_rate', 'direct')

def logic_12745(world):
    _world_apply(world, 'co2', 'oxygen', 'pulse')

def logic_12746(world):
    _world_apply(world, 'co2', 'photosynthesis_factor', 'saturation')

def logic_12747(world):
    _world_apply(world, 'co2', 'ice', 'gap')

def logic_12748(world):
    _world_apply(world, 'co2', 'evaporation', 'direct')

def logic_12749(world):
    _world_apply(world, 'co2', 'detritus', 'square')

def logic_12750(world):
    _world_apply(world, 'co2', 'methane', 'pulse')

def logic_12751(world):
    _world_apply(world, 'co2', 'pathogen_load', 'saturation')

def logic_12752(world):
    _world_apply(world, 'co2', 'biodiversity', 'gap')

def logic_12753(world):
    _world_apply(world, 'co2', 'habitat_stress', 'square')

def logic_12754(world):
    _world_apply(world, 'co2', 'erosion', 'pulse')

def logic_12755(world):
    _world_apply(world, 'co2', 'soil_depth', 'saturation')

def logic_12756(world):
    _world_apply(world, 'co2', 'root_density', 'gap')

def logic_12757(world):
    _world_apply(world, 'co2', 'wetland', 'direct')

def logic_12758(world):
    _world_apply(world, 'co2', 'carbon_storage', 'square')

def logic_12759(world):
    _world_apply(world, 'co2', 'fire_risk', 'pulse')

def logic_12760(world):
    _world_apply(world, 'co2', 'ash', 'saturation')

def logic_12761(world):
    _world_apply(world, 'co2', 'snowpack', 'direct')

def logic_12762(world):
    _world_apply(world, 'co2', 'groundwater', 'square')

def logic_12763(world):
    _world_apply(world, 'co2', 'sediment', 'pulse')

def logic_12764(world):
    _world_apply(world, 'co2', 'salinity', 'saturation')

def logic_12765(world):
    _world_apply(world, 'co2', 'algae', 'gap')

def logic_12766(world):
    _world_apply(world, 'co2', 'organic_matter', 'direct')

def logic_12767(world):
    _world_apply(world, 'co2', 'deadwood', 'square')

def logic_12768(world):
    _world_apply(world, 'co2', 'pollinators', 'pulse')

def logic_12769(world):
    _world_apply(world, 'co2', 'flowers', 'gap')

def logic_12770(world):
    _world_apply(world, 'co2', 'seed_bank', 'direct')

def logic_12771(world):
    _world_apply(world, 'co2', 'soil_carbon', 'square')

def logic_12772(world):
    _world_apply(world, 'co2', 'surface_ice', 'pulse')

def logic_12773(world):
    _world_apply(world, 'photosynthesis_factor', 'temperature', 'saturation')

def logic_12774(world):
    _world_apply(world, 'photosynthesis_factor', 'surface_water', 'gap')

def logic_12775(world):
    _world_apply(world, 'photosynthesis_factor', 'humidity', 'direct')

def logic_12776(world):
    _world_apply(world, 'photosynthesis_factor', 'cloud', 'square')

def logic_12777(world):
    _world_apply(world, 'photosynthesis_factor', 'rain', 'saturation')

def logic_12778(world):
    _world_apply(world, 'photosynthesis_factor', 'soil_moisture', 'gap')

def logic_12779(world):
    _world_apply(world, 'photosynthesis_factor', 'runoff', 'direct')

def logic_12780(world):
    _world_apply(world, 'photosynthesis_factor', 'wind_x', 'square')

def logic_12781(world):
    _world_apply(world, 'photosynthesis_factor', 'wind_y', 'pulse')

def logic_12782(world):
    _world_apply(world, 'photosynthesis_factor', 'vegetation', 'saturation')

def logic_12783(world):
    _world_apply(world, 'photosynthesis_factor', 'biomass', 'gap')

def logic_12784(world):
    _world_apply(world, 'photosynthesis_factor', 'herbivore', 'direct')

def logic_12785(world):
    _world_apply(world, 'photosynthesis_factor', 'predator', 'pulse')

def logic_12786(world):
    _world_apply(world, 'photosynthesis_factor', 'carrion', 'saturation')

def logic_12787(world):
    _world_apply(world, 'photosynthesis_factor', 'nutrients', 'gap')

def logic_12788(world):
    _world_apply(world, 'photosynthesis_factor', 'decomposition_rate', 'direct')

def logic_12789(world):
    _world_apply(world, 'photosynthesis_factor', 'oxygen', 'square')

def logic_12790(world):
    _world_apply(world, 'photosynthesis_factor', 'co2', 'pulse')

def logic_12791(world):
    _world_apply(world, 'photosynthesis_factor', 'ice', 'saturation')

def logic_12792(world):
    _world_apply(world, 'photosynthesis_factor', 'evaporation', 'gap')

def logic_12793(world):
    _world_apply(world, 'photosynthesis_factor', 'detritus', 'square')

def logic_12794(world):
    _world_apply(world, 'photosynthesis_factor', 'methane', 'pulse')

def logic_12795(world):
    _world_apply(world, 'photosynthesis_factor', 'pathogen_load', 'saturation')

def logic_12796(world):
    _world_apply(world, 'photosynthesis_factor', 'biodiversity', 'gap')

def logic_12797(world):
    _world_apply(world, 'photosynthesis_factor', 'habitat_stress', 'direct')

def logic_12798(world):
    _world_apply(world, 'photosynthesis_factor', 'erosion', 'square')

def logic_12799(world):
    _world_apply(world, 'photosynthesis_factor', 'soil_depth', 'pulse')

def logic_12800(world):
    _world_apply(world, 'photosynthesis_factor', 'root_density', 'saturation')

def logic_12801(world):
    _world_apply(world, 'photosynthesis_factor', 'wetland', 'direct')

def logic_12802(world):
    _world_apply(world, 'photosynthesis_factor', 'carbon_storage', 'square')

def logic_12803(world):
    _world_apply(world, 'photosynthesis_factor', 'fire_risk', 'pulse')

def logic_12804(world):
    _world_apply(world, 'photosynthesis_factor', 'ash', 'saturation')

def logic_12805(world):
    _world_apply(world, 'photosynthesis_factor', 'snowpack', 'gap')

def logic_12806(world):
    _world_apply(world, 'photosynthesis_factor', 'groundwater', 'direct')

def logic_12807(world):
    _world_apply(world, 'photosynthesis_factor', 'sediment', 'square')

def logic_12808(world):
    _world_apply(world, 'photosynthesis_factor', 'salinity', 'pulse')

def logic_12809(world):
    _world_apply(world, 'photosynthesis_factor', 'algae', 'gap')

def logic_12810(world):
    _world_apply(world, 'photosynthesis_factor', 'organic_matter', 'direct')

def logic_12811(world):
    _world_apply(world, 'photosynthesis_factor', 'deadwood', 'square')

def logic_12812(world):
    _world_apply(world, 'photosynthesis_factor', 'pollinators', 'pulse')

def logic_12813(world):
    _world_apply(world, 'photosynthesis_factor', 'flowers', 'saturation')

def logic_12814(world):
    _world_apply(world, 'photosynthesis_factor', 'seed_bank', 'gap')

def logic_12815(world):
    _world_apply(world, 'photosynthesis_factor', 'soil_carbon', 'direct')

def logic_12816(world):
    _world_apply(world, 'photosynthesis_factor', 'surface_ice', 'square')

def logic_12817(world):
    _world_apply(world, 'ice', 'temperature', 'saturation')

def logic_12818(world):
    _world_apply(world, 'ice', 'surface_water', 'gap')

def logic_12819(world):
    _world_apply(world, 'ice', 'humidity', 'direct')

def logic_12820(world):
    _world_apply(world, 'ice', 'cloud', 'square')

def logic_12821(world):
    _world_apply(world, 'ice', 'rain', 'pulse')

def logic_12822(world):
    _world_apply(world, 'ice', 'soil_moisture', 'saturation')

def logic_12823(world):
    _world_apply(world, 'ice', 'runoff', 'gap')

def logic_12824(world):
    _world_apply(world, 'ice', 'wind_x', 'direct')

def logic_12825(world):
    _world_apply(world, 'ice', 'wind_y', 'pulse')

def logic_12826(world):
    _world_apply(world, 'ice', 'vegetation', 'saturation')

def logic_12827(world):
    _world_apply(world, 'ice', 'biomass', 'gap')

def logic_12828(world):
    _world_apply(world, 'ice', 'herbivore', 'direct')

def logic_12829(world):
    _world_apply(world, 'ice', 'predator', 'square')

def logic_12830(world):
    _world_apply(world, 'ice', 'carrion', 'pulse')

def logic_12831(world):
    _world_apply(world, 'ice', 'nutrients', 'saturation')

def logic_12832(world):
    _world_apply(world, 'ice', 'decomposition_rate', 'gap')

def logic_12833(world):
    _world_apply(world, 'ice', 'oxygen', 'square')

def logic_12834(world):
    _world_apply(world, 'ice', 'co2', 'pulse')

def logic_12835(world):
    _world_apply(world, 'ice', 'photosynthesis_factor', 'saturation')

def logic_12836(world):
    _world_apply(world, 'ice', 'evaporation', 'gap')

def logic_12837(world):
    _world_apply(world, 'ice', 'detritus', 'direct')

def logic_12838(world):
    _world_apply(world, 'ice', 'methane', 'square')

def logic_12839(world):
    _world_apply(world, 'ice', 'pathogen_load', 'pulse')

def logic_12840(world):
    _world_apply(world, 'ice', 'biodiversity', 'saturation')

def logic_12841(world):
    _world_apply(world, 'ice', 'habitat_stress', 'direct')

def logic_12842(world):
    _world_apply(world, 'ice', 'erosion', 'square')

def logic_12843(world):
    _world_apply(world, 'ice', 'soil_depth', 'pulse')

def logic_12844(world):
    _world_apply(world, 'ice', 'root_density', 'saturation')

def logic_12845(world):
    _world_apply(world, 'ice', 'wetland', 'gap')

def logic_12846(world):
    _world_apply(world, 'ice', 'carbon_storage', 'direct')

def logic_12847(world):
    _world_apply(world, 'ice', 'fire_risk', 'square')

def logic_12848(world):
    _world_apply(world, 'ice', 'ash', 'pulse')

def logic_12849(world):
    _world_apply(world, 'ice', 'snowpack', 'gap')

def logic_12850(world):
    _world_apply(world, 'ice', 'groundwater', 'direct')

def logic_12851(world):
    _world_apply(world, 'ice', 'sediment', 'square')

def logic_12852(world):
    _world_apply(world, 'ice', 'salinity', 'pulse')

def logic_12853(world):
    _world_apply(world, 'ice', 'algae', 'saturation')

def logic_12854(world):
    _world_apply(world, 'ice', 'organic_matter', 'gap')

def logic_12855(world):
    _world_apply(world, 'ice', 'deadwood', 'direct')

def logic_12856(world):
    _world_apply(world, 'ice', 'pollinators', 'square')

def logic_12857(world):
    _world_apply(world, 'ice', 'flowers', 'saturation')

def logic_12858(world):
    _world_apply(world, 'ice', 'seed_bank', 'gap')

def logic_12859(world):
    _world_apply(world, 'ice', 'soil_carbon', 'direct')

def logic_12860(world):
    _world_apply(world, 'ice', 'surface_ice', 'square')

def logic_12861(world):
    _world_apply(world, 'evaporation', 'temperature', 'pulse')

def logic_12862(world):
    _world_apply(world, 'evaporation', 'surface_water', 'saturation')

def logic_12863(world):
    _world_apply(world, 'evaporation', 'humidity', 'gap')

def logic_12864(world):
    _world_apply(world, 'evaporation', 'cloud', 'direct')

def logic_12865(world):
    _world_apply(world, 'evaporation', 'rain', 'pulse')

def logic_12866(world):
    _world_apply(world, 'evaporation', 'soil_moisture', 'saturation')

def logic_12867(world):
    _world_apply(world, 'evaporation', 'runoff', 'gap')

def logic_12868(world):
    _world_apply(world, 'evaporation', 'wind_x', 'direct')

def logic_12869(world):
    _world_apply(world, 'evaporation', 'wind_y', 'square')

def logic_12870(world):
    _world_apply(world, 'evaporation', 'vegetation', 'pulse')

def logic_12871(world):
    _world_apply(world, 'evaporation', 'biomass', 'saturation')

def logic_12872(world):
    _world_apply(world, 'evaporation', 'herbivore', 'gap')

def logic_12873(world):
    _world_apply(world, 'evaporation', 'predator', 'square')

def logic_12874(world):
    _world_apply(world, 'evaporation', 'carrion', 'pulse')

def logic_12875(world):
    _world_apply(world, 'evaporation', 'nutrients', 'saturation')

def logic_12876(world):
    _world_apply(world, 'evaporation', 'decomposition_rate', 'gap')

def logic_12877(world):
    _world_apply(world, 'evaporation', 'oxygen', 'direct')

def logic_12878(world):
    _world_apply(world, 'evaporation', 'co2', 'square')

def logic_12879(world):
    _world_apply(world, 'evaporation', 'photosynthesis_factor', 'pulse')

def logic_12880(world):
    _world_apply(world, 'evaporation', 'ice', 'saturation')

def logic_12881(world):
    _world_apply(world, 'evaporation', 'detritus', 'direct')

def logic_12882(world):
    _world_apply(world, 'evaporation', 'methane', 'square')

def logic_12883(world):
    _world_apply(world, 'evaporation', 'pathogen_load', 'pulse')

def logic_12884(world):
    _world_apply(world, 'evaporation', 'biodiversity', 'saturation')

def logic_12885(world):
    _world_apply(world, 'evaporation', 'habitat_stress', 'gap')

def logic_12886(world):
    _world_apply(world, 'evaporation', 'erosion', 'direct')

def logic_12887(world):
    _world_apply(world, 'evaporation', 'soil_depth', 'square')

def logic_12888(world):
    _world_apply(world, 'evaporation', 'root_density', 'pulse')

def logic_12889(world):
    _world_apply(world, 'evaporation', 'wetland', 'gap')

def logic_12890(world):
    _world_apply(world, 'evaporation', 'carbon_storage', 'direct')

def logic_12891(world):
    _world_apply(world, 'evaporation', 'fire_risk', 'square')

def logic_12892(world):
    _world_apply(world, 'evaporation', 'ash', 'pulse')

def logic_12893(world):
    _world_apply(world, 'evaporation', 'snowpack', 'saturation')

def logic_12894(world):
    _world_apply(world, 'evaporation', 'groundwater', 'gap')

def logic_12895(world):
    _world_apply(world, 'evaporation', 'sediment', 'direct')

def logic_12896(world):
    _world_apply(world, 'evaporation', 'salinity', 'square')

def logic_12897(world):
    _world_apply(world, 'evaporation', 'algae', 'saturation')

def logic_12898(world):
    _world_apply(world, 'evaporation', 'organic_matter', 'gap')

def logic_12899(world):
    _world_apply(world, 'evaporation', 'deadwood', 'direct')

def logic_12900(world):
    _world_apply(world, 'evaporation', 'pollinators', 'square')

def logic_12901(world):
    _world_apply(world, 'evaporation', 'flowers', 'pulse')

def logic_12902(world):
    _world_apply(world, 'evaporation', 'seed_bank', 'saturation')

def logic_12903(world):
    _world_apply(world, 'evaporation', 'soil_carbon', 'gap')

def logic_12904(world):
    _world_apply(world, 'evaporation', 'surface_ice', 'direct')

def logic_12905(world):
    _world_apply(world, 'detritus', 'temperature', 'pulse')

def logic_12906(world):
    _world_apply(world, 'detritus', 'surface_water', 'saturation')

def logic_12907(world):
    _world_apply(world, 'detritus', 'humidity', 'gap')

def logic_12908(world):
    _world_apply(world, 'detritus', 'cloud', 'direct')

def logic_12909(world):
    _world_apply(world, 'detritus', 'rain', 'square')

def logic_12910(world):
    _world_apply(world, 'detritus', 'soil_moisture', 'pulse')

def logic_12911(world):
    _world_apply(world, 'detritus', 'runoff', 'saturation')

def logic_12912(world):
    _world_apply(world, 'detritus', 'wind_x', 'gap')

def logic_12913(world):
    _world_apply(world, 'detritus', 'wind_y', 'square')

def logic_12914(world):
    _world_apply(world, 'detritus', 'vegetation', 'pulse')

def logic_12915(world):
    _world_apply(world, 'detritus', 'biomass', 'saturation')

def logic_12916(world):
    _world_apply(world, 'detritus', 'herbivore', 'gap')

def logic_12917(world):
    _world_apply(world, 'detritus', 'predator', 'direct')

def logic_12918(world):
    _world_apply(world, 'detritus', 'carrion', 'square')

def logic_12919(world):
    _world_apply(world, 'detritus', 'nutrients', 'pulse')

def logic_12920(world):
    _world_apply(world, 'detritus', 'decomposition_rate', 'saturation')

def logic_12921(world):
    _world_apply(world, 'detritus', 'oxygen', 'direct')

def logic_12922(world):
    _world_apply(world, 'detritus', 'co2', 'square')

def logic_12923(world):
    _world_apply(world, 'detritus', 'photosynthesis_factor', 'pulse')

def logic_12924(world):
    _world_apply(world, 'detritus', 'ice', 'saturation')

def logic_12925(world):
    _world_apply(world, 'detritus', 'evaporation', 'gap')

def logic_12926(world):
    _world_apply(world, 'detritus', 'methane', 'direct')

def logic_12927(world):
    _world_apply(world, 'detritus', 'pathogen_load', 'square')

def logic_12928(world):
    _world_apply(world, 'detritus', 'biodiversity', 'pulse')

def logic_12929(world):
    _world_apply(world, 'detritus', 'habitat_stress', 'gap')

def logic_12930(world):
    _world_apply(world, 'detritus', 'erosion', 'direct')

def logic_12931(world):
    _world_apply(world, 'detritus', 'soil_depth', 'square')

def logic_12932(world):
    _world_apply(world, 'detritus', 'root_density', 'pulse')

def logic_12933(world):
    _world_apply(world, 'detritus', 'wetland', 'saturation')

def logic_12934(world):
    _world_apply(world, 'detritus', 'carbon_storage', 'gap')

def logic_12935(world):
    _world_apply(world, 'detritus', 'fire_risk', 'direct')

def logic_12936(world):
    _world_apply(world, 'detritus', 'ash', 'square')

def logic_12937(world):
    _world_apply(world, 'detritus', 'snowpack', 'saturation')

def logic_12938(world):
    _world_apply(world, 'detritus', 'groundwater', 'gap')

def logic_12939(world):
    _world_apply(world, 'detritus', 'sediment', 'direct')

def logic_12940(world):
    _world_apply(world, 'detritus', 'salinity', 'square')

def logic_12941(world):
    _world_apply(world, 'detritus', 'algae', 'pulse')

def logic_12942(world):
    _world_apply(world, 'detritus', 'organic_matter', 'saturation')

def logic_12943(world):
    _world_apply(world, 'detritus', 'deadwood', 'gap')

def logic_12944(world):
    _world_apply(world, 'detritus', 'pollinators', 'direct')

def logic_12945(world):
    _world_apply(world, 'detritus', 'flowers', 'pulse')

def logic_12946(world):
    _world_apply(world, 'detritus', 'seed_bank', 'saturation')

def logic_12947(world):
    _world_apply(world, 'detritus', 'soil_carbon', 'gap')

def logic_12948(world):
    _world_apply(world, 'detritus', 'surface_ice', 'direct')

def logic_12949(world):
    _world_apply(world, 'methane', 'temperature', 'square')

def logic_12950(world):
    _world_apply(world, 'methane', 'surface_water', 'pulse')

def logic_12951(world):
    _world_apply(world, 'methane', 'humidity', 'saturation')

def logic_12952(world):
    _world_apply(world, 'methane', 'cloud', 'gap')

def logic_12953(world):
    _world_apply(world, 'methane', 'rain', 'square')

def logic_12954(world):
    _world_apply(world, 'methane', 'soil_moisture', 'pulse')

def logic_12955(world):
    _world_apply(world, 'methane', 'runoff', 'saturation')

def logic_12956(world):
    _world_apply(world, 'methane', 'wind_x', 'gap')

def logic_12957(world):
    _world_apply(world, 'methane', 'wind_y', 'direct')

def logic_12958(world):
    _world_apply(world, 'methane', 'vegetation', 'square')

def logic_12959(world):
    _world_apply(world, 'methane', 'biomass', 'pulse')

def logic_12960(world):
    _world_apply(world, 'methane', 'herbivore', 'saturation')

def logic_12961(world):
    _world_apply(world, 'methane', 'predator', 'direct')

def logic_12962(world):
    _world_apply(world, 'methane', 'carrion', 'square')

def logic_12963(world):
    _world_apply(world, 'methane', 'nutrients', 'pulse')

def logic_12964(world):
    _world_apply(world, 'methane', 'decomposition_rate', 'saturation')

def logic_12965(world):
    _world_apply(world, 'methane', 'oxygen', 'gap')

def logic_12966(world):
    _world_apply(world, 'methane', 'co2', 'direct')

def logic_12967(world):
    _world_apply(world, 'methane', 'photosynthesis_factor', 'square')

def logic_12968(world):
    _world_apply(world, 'methane', 'ice', 'pulse')

def logic_12969(world):
    _world_apply(world, 'methane', 'evaporation', 'gap')

def logic_12970(world):
    _world_apply(world, 'methane', 'detritus', 'direct')

def logic_12971(world):
    _world_apply(world, 'methane', 'pathogen_load', 'square')

def logic_12972(world):
    _world_apply(world, 'methane', 'biodiversity', 'pulse')

def logic_12973(world):
    _world_apply(world, 'methane', 'habitat_stress', 'saturation')

def logic_12974(world):
    _world_apply(world, 'methane', 'erosion', 'gap')

def logic_12975(world):
    _world_apply(world, 'methane', 'soil_depth', 'direct')

def logic_12976(world):
    _world_apply(world, 'methane', 'root_density', 'square')

def logic_12977(world):
    _world_apply(world, 'methane', 'wetland', 'saturation')

def logic_12978(world):
    _world_apply(world, 'methane', 'carbon_storage', 'gap')

def logic_12979(world):
    _world_apply(world, 'methane', 'fire_risk', 'direct')

def logic_12980(world):
    _world_apply(world, 'methane', 'ash', 'square')

def logic_12981(world):
    _world_apply(world, 'methane', 'snowpack', 'pulse')

def logic_12982(world):
    _world_apply(world, 'methane', 'groundwater', 'saturation')

def logic_12983(world):
    _world_apply(world, 'methane', 'sediment', 'gap')

def logic_12984(world):
    _world_apply(world, 'methane', 'salinity', 'direct')

def logic_12985(world):
    _world_apply(world, 'methane', 'algae', 'pulse')

def logic_12986(world):
    _world_apply(world, 'methane', 'organic_matter', 'saturation')

def logic_12987(world):
    _world_apply(world, 'methane', 'deadwood', 'gap')

def logic_12988(world):
    _world_apply(world, 'methane', 'pollinators', 'direct')

def logic_12989(world):
    _world_apply(world, 'methane', 'flowers', 'square')

def logic_12990(world):
    _world_apply(world, 'methane', 'seed_bank', 'pulse')

def logic_12991(world):
    _world_apply(world, 'methane', 'soil_carbon', 'saturation')

def logic_12992(world):
    _world_apply(world, 'methane', 'surface_ice', 'gap')

def logic_12993(world):
    _world_apply(world, 'pathogen_load', 'temperature', 'square')

def logic_12994(world):
    _world_apply(world, 'pathogen_load', 'surface_water', 'pulse')

def logic_12995(world):
    _world_apply(world, 'pathogen_load', 'humidity', 'saturation')

def logic_12996(world):
    _world_apply(world, 'pathogen_load', 'cloud', 'gap')

def logic_12997(world):
    _world_apply(world, 'pathogen_load', 'rain', 'direct')

def logic_12998(world):
    _world_apply(world, 'pathogen_load', 'soil_moisture', 'square')

def logic_12999(world):
    _world_apply(world, 'pathogen_load', 'runoff', 'pulse')

def logic_13000(world):
    _world_apply(world, 'pathogen_load', 'wind_x', 'saturation')

def logic_13001(world):
    _world_apply(world, 'pathogen_load', 'wind_y', 'direct')

def logic_13002(world):
    _world_apply(world, 'pathogen_load', 'vegetation', 'square')

def logic_13003(world):
    _world_apply(world, 'pathogen_load', 'biomass', 'pulse')

def logic_13004(world):
    _world_apply(world, 'pathogen_load', 'herbivore', 'saturation')

def logic_13005(world):
    _world_apply(world, 'pathogen_load', 'predator', 'gap')

def logic_13006(world):
    _world_apply(world, 'pathogen_load', 'carrion', 'direct')

def logic_13007(world):
    _world_apply(world, 'pathogen_load', 'nutrients', 'square')

def logic_13008(world):
    _world_apply(world, 'pathogen_load', 'decomposition_rate', 'pulse')

def logic_13009(world):
    _world_apply(world, 'pathogen_load', 'oxygen', 'gap')

def logic_13010(world):
    _world_apply(world, 'pathogen_load', 'co2', 'direct')

def logic_13011(world):
    _world_apply(world, 'pathogen_load', 'photosynthesis_factor', 'square')

def logic_13012(world):
    _world_apply(world, 'pathogen_load', 'ice', 'pulse')

def logic_13013(world):
    _world_apply(world, 'pathogen_load', 'evaporation', 'saturation')

def logic_13014(world):
    _world_apply(world, 'pathogen_load', 'detritus', 'gap')

def logic_13015(world):
    _world_apply(world, 'pathogen_load', 'methane', 'direct')

def logic_13016(world):
    _world_apply(world, 'pathogen_load', 'biodiversity', 'square')

def logic_13017(world):
    _world_apply(world, 'pathogen_load', 'habitat_stress', 'saturation')

def logic_13018(world):
    _world_apply(world, 'pathogen_load', 'erosion', 'gap')

def logic_13019(world):
    _world_apply(world, 'pathogen_load', 'soil_depth', 'direct')

def logic_13020(world):
    _world_apply(world, 'pathogen_load', 'root_density', 'square')

def logic_13021(world):
    _world_apply(world, 'pathogen_load', 'wetland', 'pulse')

def logic_13022(world):
    _world_apply(world, 'pathogen_load', 'carbon_storage', 'saturation')

def logic_13023(world):
    _world_apply(world, 'pathogen_load', 'fire_risk', 'gap')

def logic_13024(world):
    _world_apply(world, 'pathogen_load', 'ash', 'direct')

def logic_13025(world):
    _world_apply(world, 'pathogen_load', 'snowpack', 'pulse')

def logic_13026(world):
    _world_apply(world, 'pathogen_load', 'groundwater', 'saturation')

def logic_13027(world):
    _world_apply(world, 'pathogen_load', 'sediment', 'gap')

def logic_13028(world):
    _world_apply(world, 'pathogen_load', 'salinity', 'direct')

def logic_13029(world):
    _world_apply(world, 'pathogen_load', 'algae', 'square')

def logic_13030(world):
    _world_apply(world, 'pathogen_load', 'organic_matter', 'pulse')

def logic_13031(world):
    _world_apply(world, 'pathogen_load', 'deadwood', 'saturation')

def logic_13032(world):
    _world_apply(world, 'pathogen_load', 'pollinators', 'gap')

def logic_13033(world):
    _world_apply(world, 'pathogen_load', 'flowers', 'square')

def logic_13034(world):
    _world_apply(world, 'pathogen_load', 'seed_bank', 'pulse')

def logic_13035(world):
    _world_apply(world, 'pathogen_load', 'soil_carbon', 'saturation')

def logic_13036(world):
    _world_apply(world, 'pathogen_load', 'surface_ice', 'gap')

def logic_13037(world):
    _world_apply(world, 'biodiversity', 'temperature', 'direct')

def logic_13038(world):
    _world_apply(world, 'biodiversity', 'surface_water', 'square')

def logic_13039(world):
    _world_apply(world, 'biodiversity', 'humidity', 'pulse')

def logic_13040(world):
    _world_apply(world, 'biodiversity', 'cloud', 'saturation')

def logic_13041(world):
    _world_apply(world, 'biodiversity', 'rain', 'direct')

def logic_13042(world):
    _world_apply(world, 'biodiversity', 'soil_moisture', 'square')

def logic_13043(world):
    _world_apply(world, 'biodiversity', 'runoff', 'pulse')

def logic_13044(world):
    _world_apply(world, 'biodiversity', 'wind_x', 'saturation')

def logic_13045(world):
    _world_apply(world, 'biodiversity', 'wind_y', 'gap')

def logic_13046(world):
    _world_apply(world, 'biodiversity', 'vegetation', 'direct')

def logic_13047(world):
    _world_apply(world, 'biodiversity', 'biomass', 'square')

def logic_13048(world):
    _world_apply(world, 'biodiversity', 'herbivore', 'pulse')

def logic_13049(world):
    _world_apply(world, 'biodiversity', 'predator', 'gap')

def logic_13050(world):
    _world_apply(world, 'biodiversity', 'carrion', 'direct')

def logic_13051(world):
    _world_apply(world, 'biodiversity', 'nutrients', 'square')

def logic_13052(world):
    _world_apply(world, 'biodiversity', 'decomposition_rate', 'pulse')

def logic_13053(world):
    _world_apply(world, 'biodiversity', 'oxygen', 'saturation')

def logic_13054(world):
    _world_apply(world, 'biodiversity', 'co2', 'gap')

def logic_13055(world):
    _world_apply(world, 'biodiversity', 'photosynthesis_factor', 'direct')

def logic_13056(world):
    _world_apply(world, 'biodiversity', 'ice', 'square')

def logic_13057(world):
    _world_apply(world, 'biodiversity', 'evaporation', 'saturation')

def logic_13058(world):
    _world_apply(world, 'biodiversity', 'detritus', 'gap')

def logic_13059(world):
    _world_apply(world, 'biodiversity', 'methane', 'direct')

def logic_13060(world):
    _world_apply(world, 'biodiversity', 'pathogen_load', 'square')

def logic_13061(world):
    _world_apply(world, 'biodiversity', 'habitat_stress', 'pulse')

def logic_13062(world):
    _world_apply(world, 'biodiversity', 'erosion', 'saturation')

def logic_13063(world):
    _world_apply(world, 'biodiversity', 'soil_depth', 'gap')

def logic_13064(world):
    _world_apply(world, 'biodiversity', 'root_density', 'direct')

def logic_13065(world):
    _world_apply(world, 'biodiversity', 'wetland', 'pulse')

def logic_13066(world):
    _world_apply(world, 'biodiversity', 'carbon_storage', 'saturation')

def logic_13067(world):
    _world_apply(world, 'biodiversity', 'fire_risk', 'gap')

def logic_13068(world):
    _world_apply(world, 'biodiversity', 'ash', 'direct')

def logic_13069(world):
    _world_apply(world, 'biodiversity', 'snowpack', 'square')

def logic_13070(world):
    _world_apply(world, 'biodiversity', 'groundwater', 'pulse')

def logic_13071(world):
    _world_apply(world, 'biodiversity', 'sediment', 'saturation')

def logic_13072(world):
    _world_apply(world, 'biodiversity', 'salinity', 'gap')

def logic_13073(world):
    _world_apply(world, 'biodiversity', 'algae', 'square')

def logic_13074(world):
    _world_apply(world, 'biodiversity', 'organic_matter', 'pulse')

def logic_13075(world):
    _world_apply(world, 'biodiversity', 'deadwood', 'saturation')

def logic_13076(world):
    _world_apply(world, 'biodiversity', 'pollinators', 'gap')

def logic_13077(world):
    _world_apply(world, 'biodiversity', 'flowers', 'direct')

def logic_13078(world):
    _world_apply(world, 'biodiversity', 'seed_bank', 'square')

def logic_13079(world):
    _world_apply(world, 'biodiversity', 'soil_carbon', 'pulse')

def logic_13080(world):
    _world_apply(world, 'biodiversity', 'surface_ice', 'saturation')

def logic_13081(world):
    _world_apply(world, 'habitat_stress', 'temperature', 'direct')

def logic_13082(world):
    _world_apply(world, 'habitat_stress', 'surface_water', 'square')

def logic_13083(world):
    _world_apply(world, 'habitat_stress', 'humidity', 'pulse')

def logic_13084(world):
    _world_apply(world, 'habitat_stress', 'cloud', 'saturation')

def logic_13085(world):
    _world_apply(world, 'habitat_stress', 'rain', 'gap')

def logic_13086(world):
    _world_apply(world, 'habitat_stress', 'soil_moisture', 'direct')

def logic_13087(world):
    _world_apply(world, 'habitat_stress', 'runoff', 'square')

def logic_13088(world):
    _world_apply(world, 'habitat_stress', 'wind_x', 'pulse')

def logic_13089(world):
    _world_apply(world, 'habitat_stress', 'wind_y', 'gap')

def logic_13090(world):
    _world_apply(world, 'habitat_stress', 'vegetation', 'direct')

def logic_13091(world):
    _world_apply(world, 'habitat_stress', 'biomass', 'square')

def logic_13092(world):
    _world_apply(world, 'habitat_stress', 'herbivore', 'pulse')

def logic_13093(world):
    _world_apply(world, 'habitat_stress', 'predator', 'saturation')

def logic_13094(world):
    _world_apply(world, 'habitat_stress', 'carrion', 'gap')

def logic_13095(world):
    _world_apply(world, 'habitat_stress', 'nutrients', 'direct')

def logic_13096(world):
    _world_apply(world, 'habitat_stress', 'decomposition_rate', 'square')

def logic_13097(world):
    _world_apply(world, 'habitat_stress', 'oxygen', 'saturation')

def logic_13098(world):
    _world_apply(world, 'habitat_stress', 'co2', 'gap')

def logic_13099(world):
    _world_apply(world, 'habitat_stress', 'photosynthesis_factor', 'direct')

def logic_13100(world):
    _world_apply(world, 'habitat_stress', 'ice', 'square')

def logic_13101(world):
    _world_apply(world, 'habitat_stress', 'evaporation', 'pulse')

def logic_13102(world):
    _world_apply(world, 'habitat_stress', 'detritus', 'saturation')

def logic_13103(world):
    _world_apply(world, 'habitat_stress', 'methane', 'gap')

def logic_13104(world):
    _world_apply(world, 'habitat_stress', 'pathogen_load', 'direct')

def logic_13105(world):
    _world_apply(world, 'habitat_stress', 'biodiversity', 'pulse')

def logic_13106(world):
    _world_apply(world, 'habitat_stress', 'erosion', 'saturation')

def logic_13107(world):
    _world_apply(world, 'habitat_stress', 'soil_depth', 'gap')

def logic_13108(world):
    _world_apply(world, 'habitat_stress', 'root_density', 'direct')

def logic_13109(world):
    _world_apply(world, 'habitat_stress', 'wetland', 'square')

def logic_13110(world):
    _world_apply(world, 'habitat_stress', 'carbon_storage', 'pulse')

def logic_13111(world):
    _world_apply(world, 'habitat_stress', 'fire_risk', 'saturation')

def logic_13112(world):
    _world_apply(world, 'habitat_stress', 'ash', 'gap')

def logic_13113(world):
    _world_apply(world, 'habitat_stress', 'snowpack', 'square')

def logic_13114(world):
    _world_apply(world, 'habitat_stress', 'groundwater', 'pulse')

def logic_13115(world):
    _world_apply(world, 'habitat_stress', 'sediment', 'saturation')

def logic_13116(world):
    _world_apply(world, 'habitat_stress', 'salinity', 'gap')

def logic_13117(world):
    _world_apply(world, 'habitat_stress', 'algae', 'direct')

def logic_13118(world):
    _world_apply(world, 'habitat_stress', 'organic_matter', 'square')

def logic_13119(world):
    _world_apply(world, 'habitat_stress', 'deadwood', 'pulse')

def logic_13120(world):
    _world_apply(world, 'habitat_stress', 'pollinators', 'saturation')

def logic_13121(world):
    _world_apply(world, 'habitat_stress', 'flowers', 'direct')

def logic_13122(world):
    _world_apply(world, 'habitat_stress', 'seed_bank', 'square')

def logic_13123(world):
    _world_apply(world, 'habitat_stress', 'soil_carbon', 'pulse')

def logic_13124(world):
    _world_apply(world, 'habitat_stress', 'surface_ice', 'saturation')

def logic_13125(world):
    _world_apply(world, 'erosion', 'temperature', 'gap')

def logic_13126(world):
    _world_apply(world, 'erosion', 'surface_water', 'direct')

def logic_13127(world):
    _world_apply(world, 'erosion', 'humidity', 'square')

def logic_13128(world):
    _world_apply(world, 'erosion', 'cloud', 'pulse')

def logic_13129(world):
    _world_apply(world, 'erosion', 'rain', 'gap')

def logic_13130(world):
    _world_apply(world, 'erosion', 'soil_moisture', 'direct')

def logic_13131(world):
    _world_apply(world, 'erosion', 'runoff', 'square')

def logic_13132(world):
    _world_apply(world, 'erosion', 'wind_x', 'pulse')

def logic_13133(world):
    _world_apply(world, 'erosion', 'wind_y', 'saturation')

def logic_13134(world):
    _world_apply(world, 'erosion', 'vegetation', 'gap')

def logic_13135(world):
    _world_apply(world, 'erosion', 'biomass', 'direct')

def logic_13136(world):
    _world_apply(world, 'erosion', 'herbivore', 'square')

def logic_13137(world):
    _world_apply(world, 'erosion', 'predator', 'saturation')

def logic_13138(world):
    _world_apply(world, 'erosion', 'carrion', 'gap')

def logic_13139(world):
    _world_apply(world, 'erosion', 'nutrients', 'direct')

def logic_13140(world):
    _world_apply(world, 'erosion', 'decomposition_rate', 'square')

def logic_13141(world):
    _world_apply(world, 'erosion', 'oxygen', 'pulse')

def logic_13142(world):
    _world_apply(world, 'erosion', 'co2', 'saturation')

def logic_13143(world):
    _world_apply(world, 'erosion', 'photosynthesis_factor', 'gap')

def logic_13144(world):
    _world_apply(world, 'erosion', 'ice', 'direct')

def logic_13145(world):
    _world_apply(world, 'erosion', 'evaporation', 'pulse')

def logic_13146(world):
    _world_apply(world, 'erosion', 'detritus', 'saturation')

def logic_13147(world):
    _world_apply(world, 'erosion', 'methane', 'gap')

def logic_13148(world):
    _world_apply(world, 'erosion', 'pathogen_load', 'direct')

def logic_13149(world):
    _world_apply(world, 'erosion', 'biodiversity', 'square')

def logic_13150(world):
    _world_apply(world, 'erosion', 'habitat_stress', 'pulse')

def logic_13151(world):
    _world_apply(world, 'erosion', 'soil_depth', 'saturation')

def logic_13152(world):
    _world_apply(world, 'erosion', 'root_density', 'gap')

def logic_13153(world):
    _world_apply(world, 'erosion', 'wetland', 'square')

def logic_13154(world):
    _world_apply(world, 'erosion', 'carbon_storage', 'pulse')

def logic_13155(world):
    _world_apply(world, 'erosion', 'fire_risk', 'saturation')

def logic_13156(world):
    _world_apply(world, 'erosion', 'ash', 'gap')

def logic_13157(world):
    _world_apply(world, 'erosion', 'snowpack', 'direct')

def logic_13158(world):
    _world_apply(world, 'erosion', 'groundwater', 'square')

def logic_13159(world):
    _world_apply(world, 'erosion', 'sediment', 'pulse')

def logic_13160(world):
    _world_apply(world, 'erosion', 'salinity', 'saturation')

def logic_13161(world):
    _world_apply(world, 'erosion', 'algae', 'direct')

def logic_13162(world):
    _world_apply(world, 'erosion', 'organic_matter', 'square')

def logic_13163(world):
    _world_apply(world, 'erosion', 'deadwood', 'pulse')

def logic_13164(world):
    _world_apply(world, 'erosion', 'pollinators', 'saturation')

def logic_13165(world):
    _world_apply(world, 'erosion', 'flowers', 'gap')

def logic_13166(world):
    _world_apply(world, 'erosion', 'seed_bank', 'direct')

def logic_13167(world):
    _world_apply(world, 'erosion', 'soil_carbon', 'square')

def logic_13168(world):
    _world_apply(world, 'erosion', 'surface_ice', 'pulse')

def logic_13169(world):
    _world_apply(world, 'soil_depth', 'temperature', 'gap')

def logic_13170(world):
    _world_apply(world, 'soil_depth', 'surface_water', 'direct')

def logic_13171(world):
    _world_apply(world, 'soil_depth', 'humidity', 'square')

def logic_13172(world):
    _world_apply(world, 'soil_depth', 'cloud', 'pulse')

def logic_13173(world):
    _world_apply(world, 'soil_depth', 'rain', 'saturation')

def logic_13174(world):
    _world_apply(world, 'soil_depth', 'soil_moisture', 'gap')

def logic_13175(world):
    _world_apply(world, 'soil_depth', 'runoff', 'direct')

def logic_13176(world):
    _world_apply(world, 'soil_depth', 'wind_x', 'square')

def logic_13177(world):
    _world_apply(world, 'soil_depth', 'wind_y', 'saturation')

def logic_13178(world):
    _world_apply(world, 'soil_depth', 'vegetation', 'gap')

def logic_13179(world):
    _world_apply(world, 'soil_depth', 'biomass', 'direct')

def logic_13180(world):
    _world_apply(world, 'soil_depth', 'herbivore', 'square')

def logic_13181(world):
    _world_apply(world, 'soil_depth', 'predator', 'pulse')

def logic_13182(world):
    _world_apply(world, 'soil_depth', 'carrion', 'saturation')

def logic_13183(world):
    _world_apply(world, 'soil_depth', 'nutrients', 'gap')

def logic_13184(world):
    _world_apply(world, 'soil_depth', 'decomposition_rate', 'direct')

def logic_13185(world):
    _world_apply(world, 'soil_depth', 'oxygen', 'pulse')

def logic_13186(world):
    _world_apply(world, 'soil_depth', 'co2', 'saturation')

def logic_13187(world):
    _world_apply(world, 'soil_depth', 'photosynthesis_factor', 'gap')

def logic_13188(world):
    _world_apply(world, 'soil_depth', 'ice', 'direct')

def logic_13189(world):
    _world_apply(world, 'soil_depth', 'evaporation', 'square')

def logic_13190(world):
    _world_apply(world, 'soil_depth', 'detritus', 'pulse')

def logic_13191(world):
    _world_apply(world, 'soil_depth', 'methane', 'saturation')

def logic_13192(world):
    _world_apply(world, 'soil_depth', 'pathogen_load', 'gap')

def logic_13193(world):
    _world_apply(world, 'soil_depth', 'biodiversity', 'square')

def logic_13194(world):
    _world_apply(world, 'soil_depth', 'habitat_stress', 'pulse')

def logic_13195(world):
    _world_apply(world, 'soil_depth', 'erosion', 'saturation')

def logic_13196(world):
    _world_apply(world, 'soil_depth', 'root_density', 'gap')

def logic_13197(world):
    _world_apply(world, 'soil_depth', 'wetland', 'direct')

def logic_13198(world):
    _world_apply(world, 'soil_depth', 'carbon_storage', 'square')

def logic_13199(world):
    _world_apply(world, 'soil_depth', 'fire_risk', 'pulse')

def logic_13200(world):
    _world_apply(world, 'soil_depth', 'ash', 'saturation')

def logic_13201(world):
    _world_apply(world, 'soil_depth', 'snowpack', 'direct')

def logic_13202(world):
    _world_apply(world, 'soil_depth', 'groundwater', 'square')

def logic_13203(world):
    _world_apply(world, 'soil_depth', 'sediment', 'pulse')

def logic_13204(world):
    _world_apply(world, 'soil_depth', 'salinity', 'saturation')

def logic_13205(world):
    _world_apply(world, 'soil_depth', 'algae', 'gap')

def logic_13206(world):
    _world_apply(world, 'soil_depth', 'organic_matter', 'direct')

def logic_13207(world):
    _world_apply(world, 'soil_depth', 'deadwood', 'square')

def logic_13208(world):
    _world_apply(world, 'soil_depth', 'pollinators', 'pulse')

def logic_13209(world):
    _world_apply(world, 'soil_depth', 'flowers', 'gap')

def logic_13210(world):
    _world_apply(world, 'soil_depth', 'seed_bank', 'direct')

def logic_13211(world):
    _world_apply(world, 'soil_depth', 'soil_carbon', 'square')

def logic_13212(world):
    _world_apply(world, 'soil_depth', 'surface_ice', 'pulse')

def logic_13213(world):
    _world_apply(world, 'root_density', 'temperature', 'saturation')

def logic_13214(world):
    _world_apply(world, 'root_density', 'surface_water', 'gap')

def logic_13215(world):
    _world_apply(world, 'root_density', 'humidity', 'direct')

def logic_13216(world):
    _world_apply(world, 'root_density', 'cloud', 'square')

def logic_13217(world):
    _world_apply(world, 'root_density', 'rain', 'saturation')

def logic_13218(world):
    _world_apply(world, 'root_density', 'soil_moisture', 'gap')

def logic_13219(world):
    _world_apply(world, 'root_density', 'runoff', 'direct')

def logic_13220(world):
    _world_apply(world, 'root_density', 'wind_x', 'square')

def logic_13221(world):
    _world_apply(world, 'root_density', 'wind_y', 'pulse')

def logic_13222(world):
    _world_apply(world, 'root_density', 'vegetation', 'saturation')

def logic_13223(world):
    _world_apply(world, 'root_density', 'biomass', 'gap')

def logic_13224(world):
    _world_apply(world, 'root_density', 'herbivore', 'direct')

def logic_13225(world):
    _world_apply(world, 'root_density', 'predator', 'pulse')

def logic_13226(world):
    _world_apply(world, 'root_density', 'carrion', 'saturation')

def logic_13227(world):
    _world_apply(world, 'root_density', 'nutrients', 'gap')

def logic_13228(world):
    _world_apply(world, 'root_density', 'decomposition_rate', 'direct')

def logic_13229(world):
    _world_apply(world, 'root_density', 'oxygen', 'square')

def logic_13230(world):
    _world_apply(world, 'root_density', 'co2', 'pulse')

def logic_13231(world):
    _world_apply(world, 'root_density', 'photosynthesis_factor', 'saturation')

def logic_13232(world):
    _world_apply(world, 'root_density', 'ice', 'gap')

def logic_13233(world):
    _world_apply(world, 'root_density', 'evaporation', 'square')

def logic_13234(world):
    _world_apply(world, 'root_density', 'detritus', 'pulse')

def logic_13235(world):
    _world_apply(world, 'root_density', 'methane', 'saturation')

def logic_13236(world):
    _world_apply(world, 'root_density', 'pathogen_load', 'gap')

def logic_13237(world):
    _world_apply(world, 'root_density', 'biodiversity', 'direct')

def logic_13238(world):
    _world_apply(world, 'root_density', 'habitat_stress', 'square')

def logic_13239(world):
    _world_apply(world, 'root_density', 'erosion', 'pulse')

def logic_13240(world):
    _world_apply(world, 'root_density', 'soil_depth', 'saturation')

def logic_13241(world):
    _world_apply(world, 'root_density', 'wetland', 'direct')

def logic_13242(world):
    _world_apply(world, 'root_density', 'carbon_storage', 'square')

def logic_13243(world):
    _world_apply(world, 'root_density', 'fire_risk', 'pulse')

def logic_13244(world):
    _world_apply(world, 'root_density', 'ash', 'saturation')

def logic_13245(world):
    _world_apply(world, 'root_density', 'snowpack', 'gap')

def logic_13246(world):
    _world_apply(world, 'root_density', 'groundwater', 'direct')

def logic_13247(world):
    _world_apply(world, 'root_density', 'sediment', 'square')

def logic_13248(world):
    _world_apply(world, 'root_density', 'salinity', 'pulse')

def logic_13249(world):
    _world_apply(world, 'root_density', 'algae', 'gap')

def logic_13250(world):
    _world_apply(world, 'root_density', 'organic_matter', 'direct')

def logic_13251(world):
    _world_apply(world, 'root_density', 'deadwood', 'square')

def logic_13252(world):
    _world_apply(world, 'root_density', 'pollinators', 'pulse')

def logic_13253(world):
    _world_apply(world, 'root_density', 'flowers', 'saturation')

def logic_13254(world):
    _world_apply(world, 'root_density', 'seed_bank', 'gap')

def logic_13255(world):
    _world_apply(world, 'root_density', 'soil_carbon', 'direct')

def logic_13256(world):
    _world_apply(world, 'root_density', 'surface_ice', 'square')

def logic_13257(world):
    _world_apply(world, 'wetland', 'temperature', 'saturation')

def logic_13258(world):
    _world_apply(world, 'wetland', 'surface_water', 'gap')

def logic_13259(world):
    _world_apply(world, 'wetland', 'humidity', 'direct')

def logic_13260(world):
    _world_apply(world, 'wetland', 'cloud', 'square')

def logic_13261(world):
    _world_apply(world, 'wetland', 'rain', 'pulse')

def logic_13262(world):
    _world_apply(world, 'wetland', 'soil_moisture', 'saturation')

def logic_13263(world):
    _world_apply(world, 'wetland', 'runoff', 'gap')

def logic_13264(world):
    _world_apply(world, 'wetland', 'wind_x', 'direct')

def logic_13265(world):
    _world_apply(world, 'wetland', 'wind_y', 'pulse')

def logic_13266(world):
    _world_apply(world, 'wetland', 'vegetation', 'saturation')

def logic_13267(world):
    _world_apply(world, 'wetland', 'biomass', 'gap')

def logic_13268(world):
    _world_apply(world, 'wetland', 'herbivore', 'direct')

def logic_13269(world):
    _world_apply(world, 'wetland', 'predator', 'square')

def logic_13270(world):
    _world_apply(world, 'wetland', 'carrion', 'pulse')

def logic_13271(world):
    _world_apply(world, 'wetland', 'nutrients', 'saturation')

def logic_13272(world):
    _world_apply(world, 'wetland', 'decomposition_rate', 'gap')

def logic_13273(world):
    _world_apply(world, 'wetland', 'oxygen', 'square')

def logic_13274(world):
    _world_apply(world, 'wetland', 'co2', 'pulse')

def logic_13275(world):
    _world_apply(world, 'wetland', 'photosynthesis_factor', 'saturation')

def logic_13276(world):
    _world_apply(world, 'wetland', 'ice', 'gap')

def logic_13277(world):
    _world_apply(world, 'wetland', 'evaporation', 'direct')

def logic_13278(world):
    _world_apply(world, 'wetland', 'detritus', 'square')

def logic_13279(world):
    _world_apply(world, 'wetland', 'methane', 'pulse')

def logic_13280(world):
    _world_apply(world, 'wetland', 'pathogen_load', 'saturation')

def logic_13281(world):
    _world_apply(world, 'wetland', 'biodiversity', 'direct')

def logic_13282(world):
    _world_apply(world, 'wetland', 'habitat_stress', 'square')

def logic_13283(world):
    _world_apply(world, 'wetland', 'erosion', 'pulse')

def logic_13284(world):
    _world_apply(world, 'wetland', 'soil_depth', 'saturation')

def logic_13285(world):
    _world_apply(world, 'wetland', 'root_density', 'gap')

def logic_13286(world):
    _world_apply(world, 'wetland', 'carbon_storage', 'direct')

def logic_13287(world):
    _world_apply(world, 'wetland', 'fire_risk', 'square')

def logic_13288(world):
    _world_apply(world, 'wetland', 'ash', 'pulse')

def logic_13289(world):
    _world_apply(world, 'wetland', 'snowpack', 'gap')

def logic_13290(world):
    _world_apply(world, 'wetland', 'groundwater', 'direct')

def logic_13291(world):
    _world_apply(world, 'wetland', 'sediment', 'square')

def logic_13292(world):
    _world_apply(world, 'wetland', 'salinity', 'pulse')

def logic_13293(world):
    _world_apply(world, 'wetland', 'algae', 'saturation')

def logic_13294(world):
    _world_apply(world, 'wetland', 'organic_matter', 'gap')

def logic_13295(world):
    _world_apply(world, 'wetland', 'deadwood', 'direct')

def logic_13296(world):
    _world_apply(world, 'wetland', 'pollinators', 'square')

def logic_13297(world):
    _world_apply(world, 'wetland', 'flowers', 'saturation')

def logic_13298(world):
    _world_apply(world, 'wetland', 'seed_bank', 'gap')

def logic_13299(world):
    _world_apply(world, 'wetland', 'soil_carbon', 'direct')

def logic_13300(world):
    _world_apply(world, 'wetland', 'surface_ice', 'square')

def logic_13301(world):
    _world_apply(world, 'carbon_storage', 'temperature', 'pulse')

def logic_13302(world):
    _world_apply(world, 'carbon_storage', 'surface_water', 'saturation')

def logic_13303(world):
    _world_apply(world, 'carbon_storage', 'humidity', 'gap')

def logic_13304(world):
    _world_apply(world, 'carbon_storage', 'cloud', 'direct')

def logic_13305(world):
    _world_apply(world, 'carbon_storage', 'rain', 'pulse')

def logic_13306(world):
    _world_apply(world, 'carbon_storage', 'soil_moisture', 'saturation')

def logic_13307(world):
    _world_apply(world, 'carbon_storage', 'runoff', 'gap')

def logic_13308(world):
    _world_apply(world, 'carbon_storage', 'wind_x', 'direct')

def logic_13309(world):
    _world_apply(world, 'carbon_storage', 'wind_y', 'square')

def logic_13310(world):
    _world_apply(world, 'carbon_storage', 'vegetation', 'pulse')

def logic_13311(world):
    _world_apply(world, 'carbon_storage', 'biomass', 'saturation')

def logic_13312(world):
    _world_apply(world, 'carbon_storage', 'herbivore', 'gap')

def logic_13313(world):
    _world_apply(world, 'carbon_storage', 'predator', 'square')

def logic_13314(world):
    _world_apply(world, 'carbon_storage', 'carrion', 'pulse')

def logic_13315(world):
    _world_apply(world, 'carbon_storage', 'nutrients', 'saturation')

def logic_13316(world):
    _world_apply(world, 'carbon_storage', 'decomposition_rate', 'gap')

def logic_13317(world):
    _world_apply(world, 'carbon_storage', 'oxygen', 'direct')

def logic_13318(world):
    _world_apply(world, 'carbon_storage', 'co2', 'square')

def logic_13319(world):
    _world_apply(world, 'carbon_storage', 'photosynthesis_factor', 'pulse')

def logic_13320(world):
    _world_apply(world, 'carbon_storage', 'ice', 'saturation')

def logic_13321(world):
    _world_apply(world, 'carbon_storage', 'evaporation', 'direct')

def logic_13322(world):
    _world_apply(world, 'carbon_storage', 'detritus', 'square')

def logic_13323(world):
    _world_apply(world, 'carbon_storage', 'methane', 'pulse')

def logic_13324(world):
    _world_apply(world, 'carbon_storage', 'pathogen_load', 'saturation')

def logic_13325(world):
    _world_apply(world, 'carbon_storage', 'biodiversity', 'gap')

def logic_13326(world):
    _world_apply(world, 'carbon_storage', 'habitat_stress', 'direct')

def logic_13327(world):
    _world_apply(world, 'carbon_storage', 'erosion', 'square')

def logic_13328(world):
    _world_apply(world, 'carbon_storage', 'soil_depth', 'pulse')

def logic_13329(world):
    _world_apply(world, 'carbon_storage', 'root_density', 'gap')

def logic_13330(world):
    _world_apply(world, 'carbon_storage', 'wetland', 'direct')

def logic_13331(world):
    _world_apply(world, 'carbon_storage', 'fire_risk', 'square')

def logic_13332(world):
    _world_apply(world, 'carbon_storage', 'ash', 'pulse')

def logic_13333(world):
    _world_apply(world, 'carbon_storage', 'snowpack', 'saturation')

def logic_13334(world):
    _world_apply(world, 'carbon_storage', 'groundwater', 'gap')

def logic_13335(world):
    _world_apply(world, 'carbon_storage', 'sediment', 'direct')

def logic_13336(world):
    _world_apply(world, 'carbon_storage', 'salinity', 'square')

def logic_13337(world):
    _world_apply(world, 'carbon_storage', 'algae', 'saturation')

def logic_13338(world):
    _world_apply(world, 'carbon_storage', 'organic_matter', 'gap')

def logic_13339(world):
    _world_apply(world, 'carbon_storage', 'deadwood', 'direct')

def logic_13340(world):
    _world_apply(world, 'carbon_storage', 'pollinators', 'square')

def logic_13341(world):
    _world_apply(world, 'carbon_storage', 'flowers', 'pulse')

def logic_13342(world):
    _world_apply(world, 'carbon_storage', 'seed_bank', 'saturation')

def logic_13343(world):
    _world_apply(world, 'carbon_storage', 'soil_carbon', 'gap')

def logic_13344(world):
    _world_apply(world, 'carbon_storage', 'surface_ice', 'direct')

def logic_13345(world):
    _world_apply(world, 'fire_risk', 'temperature', 'pulse')

def logic_13346(world):
    _world_apply(world, 'fire_risk', 'surface_water', 'saturation')

def logic_13347(world):
    _world_apply(world, 'fire_risk', 'humidity', 'gap')

def logic_13348(world):
    _world_apply(world, 'fire_risk', 'cloud', 'direct')

def logic_13349(world):
    _world_apply(world, 'fire_risk', 'rain', 'square')

def logic_13350(world):
    _world_apply(world, 'fire_risk', 'soil_moisture', 'pulse')

def logic_13351(world):
    _world_apply(world, 'fire_risk', 'runoff', 'saturation')

def logic_13352(world):
    _world_apply(world, 'fire_risk', 'wind_x', 'gap')

def logic_13353(world):
    _world_apply(world, 'fire_risk', 'wind_y', 'square')

def logic_13354(world):
    _world_apply(world, 'fire_risk', 'vegetation', 'pulse')

def logic_13355(world):
    _world_apply(world, 'fire_risk', 'biomass', 'saturation')

def logic_13356(world):
    _world_apply(world, 'fire_risk', 'herbivore', 'gap')

def logic_13357(world):
    _world_apply(world, 'fire_risk', 'predator', 'direct')

def logic_13358(world):
    _world_apply(world, 'fire_risk', 'carrion', 'square')

def logic_13359(world):
    _world_apply(world, 'fire_risk', 'nutrients', 'pulse')

def logic_13360(world):
    _world_apply(world, 'fire_risk', 'decomposition_rate', 'saturation')

def logic_13361(world):
    _world_apply(world, 'fire_risk', 'oxygen', 'direct')

def logic_13362(world):
    _world_apply(world, 'fire_risk', 'co2', 'square')

def logic_13363(world):
    _world_apply(world, 'fire_risk', 'photosynthesis_factor', 'pulse')

def logic_13364(world):
    _world_apply(world, 'fire_risk', 'ice', 'saturation')

def logic_13365(world):
    _world_apply(world, 'fire_risk', 'evaporation', 'gap')

def logic_13366(world):
    _world_apply(world, 'fire_risk', 'detritus', 'direct')

def logic_13367(world):
    _world_apply(world, 'fire_risk', 'methane', 'square')

def logic_13368(world):
    _world_apply(world, 'fire_risk', 'pathogen_load', 'pulse')

def logic_13369(world):
    _world_apply(world, 'fire_risk', 'biodiversity', 'gap')

def logic_13370(world):
    _world_apply(world, 'fire_risk', 'habitat_stress', 'direct')

def logic_13371(world):
    _world_apply(world, 'fire_risk', 'erosion', 'square')

def logic_13372(world):
    _world_apply(world, 'fire_risk', 'soil_depth', 'pulse')

def logic_13373(world):
    _world_apply(world, 'fire_risk', 'root_density', 'saturation')

def logic_13374(world):
    _world_apply(world, 'fire_risk', 'wetland', 'gap')

def logic_13375(world):
    _world_apply(world, 'fire_risk', 'carbon_storage', 'direct')

def logic_13376(world):
    _world_apply(world, 'fire_risk', 'ash', 'square')

def logic_13377(world):
    _world_apply(world, 'fire_risk', 'snowpack', 'saturation')

def logic_13378(world):
    _world_apply(world, 'fire_risk', 'groundwater', 'gap')

def logic_13379(world):
    _world_apply(world, 'fire_risk', 'sediment', 'direct')

def logic_13380(world):
    _world_apply(world, 'fire_risk', 'salinity', 'square')

def logic_13381(world):
    _world_apply(world, 'fire_risk', 'algae', 'pulse')

def logic_13382(world):
    _world_apply(world, 'fire_risk', 'organic_matter', 'saturation')

def logic_13383(world):
    _world_apply(world, 'fire_risk', 'deadwood', 'gap')

def logic_13384(world):
    _world_apply(world, 'fire_risk', 'pollinators', 'direct')

def logic_13385(world):
    _world_apply(world, 'fire_risk', 'flowers', 'pulse')

def logic_13386(world):
    _world_apply(world, 'fire_risk', 'seed_bank', 'saturation')

def logic_13387(world):
    _world_apply(world, 'fire_risk', 'soil_carbon', 'gap')

def logic_13388(world):
    _world_apply(world, 'fire_risk', 'surface_ice', 'direct')

def logic_13389(world):
    _world_apply(world, 'ash', 'temperature', 'square')

def logic_13390(world):
    _world_apply(world, 'ash', 'surface_water', 'pulse')

def logic_13391(world):
    _world_apply(world, 'ash', 'humidity', 'saturation')

def logic_13392(world):
    _world_apply(world, 'ash', 'cloud', 'gap')

def logic_13393(world):
    _world_apply(world, 'ash', 'rain', 'square')

def logic_13394(world):
    _world_apply(world, 'ash', 'soil_moisture', 'pulse')

def logic_13395(world):
    _world_apply(world, 'ash', 'runoff', 'saturation')

def logic_13396(world):
    _world_apply(world, 'ash', 'wind_x', 'gap')

def logic_13397(world):
    _world_apply(world, 'ash', 'wind_y', 'direct')

def logic_13398(world):
    _world_apply(world, 'ash', 'vegetation', 'square')

def logic_13399(world):
    _world_apply(world, 'ash', 'biomass', 'pulse')

def logic_13400(world):
    _world_apply(world, 'ash', 'herbivore', 'saturation')

def logic_13401(world):
    _world_apply(world, 'ash', 'predator', 'direct')

def logic_13402(world):
    _world_apply(world, 'ash', 'carrion', 'square')

def logic_13403(world):
    _world_apply(world, 'ash', 'nutrients', 'pulse')

def logic_13404(world):
    _world_apply(world, 'ash', 'decomposition_rate', 'saturation')

def logic_13405(world):
    _world_apply(world, 'ash', 'oxygen', 'gap')

def logic_13406(world):
    _world_apply(world, 'ash', 'co2', 'direct')

def logic_13407(world):
    _world_apply(world, 'ash', 'photosynthesis_factor', 'square')

def logic_13408(world):
    _world_apply(world, 'ash', 'ice', 'pulse')

def logic_13409(world):
    _world_apply(world, 'ash', 'evaporation', 'gap')

def logic_13410(world):
    _world_apply(world, 'ash', 'detritus', 'direct')

def logic_13411(world):
    _world_apply(world, 'ash', 'methane', 'square')

def logic_13412(world):
    _world_apply(world, 'ash', 'pathogen_load', 'pulse')

def logic_13413(world):
    _world_apply(world, 'ash', 'biodiversity', 'saturation')

def logic_13414(world):
    _world_apply(world, 'ash', 'habitat_stress', 'gap')

def logic_13415(world):
    _world_apply(world, 'ash', 'erosion', 'direct')

def logic_13416(world):
    _world_apply(world, 'ash', 'soil_depth', 'square')

def logic_13417(world):
    _world_apply(world, 'ash', 'root_density', 'saturation')

def logic_13418(world):
    _world_apply(world, 'ash', 'wetland', 'gap')

def logic_13419(world):
    _world_apply(world, 'ash', 'carbon_storage', 'direct')

def logic_13420(world):
    _world_apply(world, 'ash', 'fire_risk', 'square')

def logic_13421(world):
    _world_apply(world, 'ash', 'snowpack', 'pulse')

def logic_13422(world):
    _world_apply(world, 'ash', 'groundwater', 'saturation')

def logic_13423(world):
    _world_apply(world, 'ash', 'sediment', 'gap')

def logic_13424(world):
    _world_apply(world, 'ash', 'salinity', 'direct')

def logic_13425(world):
    _world_apply(world, 'ash', 'algae', 'pulse')

def logic_13426(world):
    _world_apply(world, 'ash', 'organic_matter', 'saturation')

def logic_13427(world):
    _world_apply(world, 'ash', 'deadwood', 'gap')

def logic_13428(world):
    _world_apply(world, 'ash', 'pollinators', 'direct')

def logic_13429(world):
    _world_apply(world, 'ash', 'flowers', 'square')

def logic_13430(world):
    _world_apply(world, 'ash', 'seed_bank', 'pulse')

def logic_13431(world):
    _world_apply(world, 'ash', 'soil_carbon', 'saturation')

def logic_13432(world):
    _world_apply(world, 'ash', 'surface_ice', 'gap')

def logic_13433(world):
    _world_apply(world, 'snowpack', 'temperature', 'square')

def logic_13434(world):
    _world_apply(world, 'snowpack', 'surface_water', 'pulse')

def logic_13435(world):
    _world_apply(world, 'snowpack', 'humidity', 'saturation')

def logic_13436(world):
    _world_apply(world, 'snowpack', 'cloud', 'gap')

def logic_13437(world):
    _world_apply(world, 'snowpack', 'rain', 'direct')

def logic_13438(world):
    _world_apply(world, 'snowpack', 'soil_moisture', 'square')

def logic_13439(world):
    _world_apply(world, 'snowpack', 'runoff', 'pulse')

def logic_13440(world):
    _world_apply(world, 'snowpack', 'wind_x', 'saturation')

def logic_13441(world):
    _world_apply(world, 'snowpack', 'wind_y', 'direct')

def logic_13442(world):
    _world_apply(world, 'snowpack', 'vegetation', 'square')

def logic_13443(world):
    _world_apply(world, 'snowpack', 'biomass', 'pulse')

def logic_13444(world):
    _world_apply(world, 'snowpack', 'herbivore', 'saturation')

def logic_13445(world):
    _world_apply(world, 'snowpack', 'predator', 'gap')

def logic_13446(world):
    _world_apply(world, 'snowpack', 'carrion', 'direct')

def logic_13447(world):
    _world_apply(world, 'snowpack', 'nutrients', 'square')

def logic_13448(world):
    _world_apply(world, 'snowpack', 'decomposition_rate', 'pulse')

def logic_13449(world):
    _world_apply(world, 'snowpack', 'oxygen', 'gap')

def logic_13450(world):
    _world_apply(world, 'snowpack', 'co2', 'direct')

def logic_13451(world):
    _world_apply(world, 'snowpack', 'photosynthesis_factor', 'square')

def logic_13452(world):
    _world_apply(world, 'snowpack', 'ice', 'pulse')

def logic_13453(world):
    _world_apply(world, 'snowpack', 'evaporation', 'saturation')

def logic_13454(world):
    _world_apply(world, 'snowpack', 'detritus', 'gap')

def logic_13455(world):
    _world_apply(world, 'snowpack', 'methane', 'direct')

def logic_13456(world):
    _world_apply(world, 'snowpack', 'pathogen_load', 'square')

def logic_13457(world):
    _world_apply(world, 'snowpack', 'biodiversity', 'saturation')

def logic_13458(world):
    _world_apply(world, 'snowpack', 'habitat_stress', 'gap')

def logic_13459(world):
    _world_apply(world, 'snowpack', 'erosion', 'direct')

def logic_13460(world):
    _world_apply(world, 'snowpack', 'soil_depth', 'square')

def logic_13461(world):
    _world_apply(world, 'snowpack', 'root_density', 'pulse')

def logic_13462(world):
    _world_apply(world, 'snowpack', 'wetland', 'saturation')

def logic_13463(world):
    _world_apply(world, 'snowpack', 'carbon_storage', 'gap')

def logic_13464(world):
    _world_apply(world, 'snowpack', 'fire_risk', 'direct')

def logic_13465(world):
    _world_apply(world, 'snowpack', 'ash', 'pulse')

def logic_13466(world):
    _world_apply(world, 'snowpack', 'groundwater', 'saturation')

def logic_13467(world):
    _world_apply(world, 'snowpack', 'sediment', 'gap')

def logic_13468(world):
    _world_apply(world, 'snowpack', 'salinity', 'direct')

def logic_13469(world):
    _world_apply(world, 'snowpack', 'algae', 'square')

def logic_13470(world):
    _world_apply(world, 'snowpack', 'organic_matter', 'pulse')

def logic_13471(world):
    _world_apply(world, 'snowpack', 'deadwood', 'saturation')

def logic_13472(world):
    _world_apply(world, 'snowpack', 'pollinators', 'gap')

def logic_13473(world):
    _world_apply(world, 'snowpack', 'flowers', 'square')

def logic_13474(world):
    _world_apply(world, 'snowpack', 'seed_bank', 'pulse')

def logic_13475(world):
    _world_apply(world, 'snowpack', 'soil_carbon', 'saturation')

def logic_13476(world):
    _world_apply(world, 'snowpack', 'surface_ice', 'gap')

def logic_13477(world):
    _world_apply(world, 'groundwater', 'temperature', 'direct')

def logic_13478(world):
    _world_apply(world, 'groundwater', 'surface_water', 'square')

def logic_13479(world):
    _world_apply(world, 'groundwater', 'humidity', 'pulse')

def logic_13480(world):
    _world_apply(world, 'groundwater', 'cloud', 'saturation')

def logic_13481(world):
    _world_apply(world, 'groundwater', 'rain', 'direct')

def logic_13482(world):
    _world_apply(world, 'groundwater', 'soil_moisture', 'square')

def logic_13483(world):
    _world_apply(world, 'groundwater', 'runoff', 'pulse')

def logic_13484(world):
    _world_apply(world, 'groundwater', 'wind_x', 'saturation')

def logic_13485(world):
    _world_apply(world, 'groundwater', 'wind_y', 'gap')

def logic_13486(world):
    _world_apply(world, 'groundwater', 'vegetation', 'direct')

def logic_13487(world):
    _world_apply(world, 'groundwater', 'biomass', 'square')

def logic_13488(world):
    _world_apply(world, 'groundwater', 'herbivore', 'pulse')

def logic_13489(world):
    _world_apply(world, 'groundwater', 'predator', 'gap')

def logic_13490(world):
    _world_apply(world, 'groundwater', 'carrion', 'direct')

def logic_13491(world):
    _world_apply(world, 'groundwater', 'nutrients', 'square')

def logic_13492(world):
    _world_apply(world, 'groundwater', 'decomposition_rate', 'pulse')

def logic_13493(world):
    _world_apply(world, 'groundwater', 'oxygen', 'saturation')

def logic_13494(world):
    _world_apply(world, 'groundwater', 'co2', 'gap')

def logic_13495(world):
    _world_apply(world, 'groundwater', 'photosynthesis_factor', 'direct')

def logic_13496(world):
    _world_apply(world, 'groundwater', 'ice', 'square')

def logic_13497(world):
    _world_apply(world, 'groundwater', 'evaporation', 'saturation')

def logic_13498(world):
    _world_apply(world, 'groundwater', 'detritus', 'gap')

def logic_13499(world):
    _world_apply(world, 'groundwater', 'methane', 'direct')

def logic_13500(world):
    _world_apply(world, 'groundwater', 'pathogen_load', 'square')

def logic_13501(world):
    _world_apply(world, 'groundwater', 'biodiversity', 'pulse')

def logic_13502(world):
    _world_apply(world, 'groundwater', 'habitat_stress', 'saturation')

def logic_13503(world):
    _world_apply(world, 'groundwater', 'erosion', 'gap')

def logic_13504(world):
    _world_apply(world, 'groundwater', 'soil_depth', 'direct')

def logic_13505(world):
    _world_apply(world, 'groundwater', 'root_density', 'pulse')

def logic_13506(world):
    _world_apply(world, 'groundwater', 'wetland', 'saturation')

def logic_13507(world):
    _world_apply(world, 'groundwater', 'carbon_storage', 'gap')

def logic_13508(world):
    _world_apply(world, 'groundwater', 'fire_risk', 'direct')

def logic_13509(world):
    _world_apply(world, 'groundwater', 'ash', 'square')

def logic_13510(world):
    _world_apply(world, 'groundwater', 'snowpack', 'pulse')

def logic_13511(world):
    _world_apply(world, 'groundwater', 'sediment', 'saturation')

def logic_13512(world):
    _world_apply(world, 'groundwater', 'salinity', 'gap')

def logic_13513(world):
    _world_apply(world, 'groundwater', 'algae', 'square')

def logic_13514(world):
    _world_apply(world, 'groundwater', 'organic_matter', 'pulse')

def logic_13515(world):
    _world_apply(world, 'groundwater', 'deadwood', 'saturation')

def logic_13516(world):
    _world_apply(world, 'groundwater', 'pollinators', 'gap')

def logic_13517(world):
    _world_apply(world, 'groundwater', 'flowers', 'direct')

def logic_13518(world):
    _world_apply(world, 'groundwater', 'seed_bank', 'square')

def logic_13519(world):
    _world_apply(world, 'groundwater', 'soil_carbon', 'pulse')

def logic_13520(world):
    _world_apply(world, 'groundwater', 'surface_ice', 'saturation')

def logic_13521(world):
    _world_apply(world, 'sediment', 'temperature', 'direct')

def logic_13522(world):
    _world_apply(world, 'sediment', 'surface_water', 'square')

def logic_13523(world):
    _world_apply(world, 'sediment', 'humidity', 'pulse')

def logic_13524(world):
    _world_apply(world, 'sediment', 'cloud', 'saturation')

def logic_13525(world):
    _world_apply(world, 'sediment', 'rain', 'gap')

def logic_13526(world):
    _world_apply(world, 'sediment', 'soil_moisture', 'direct')

def logic_13527(world):
    _world_apply(world, 'sediment', 'runoff', 'square')

def logic_13528(world):
    _world_apply(world, 'sediment', 'wind_x', 'pulse')

def logic_13529(world):
    _world_apply(world, 'sediment', 'wind_y', 'gap')

def logic_13530(world):
    _world_apply(world, 'sediment', 'vegetation', 'direct')

def logic_13531(world):
    _world_apply(world, 'sediment', 'biomass', 'square')

def logic_13532(world):
    _world_apply(world, 'sediment', 'herbivore', 'pulse')

def logic_13533(world):
    _world_apply(world, 'sediment', 'predator', 'saturation')

def logic_13534(world):
    _world_apply(world, 'sediment', 'carrion', 'gap')

def logic_13535(world):
    _world_apply(world, 'sediment', 'nutrients', 'direct')

def logic_13536(world):
    _world_apply(world, 'sediment', 'decomposition_rate', 'square')

def logic_13537(world):
    _world_apply(world, 'sediment', 'oxygen', 'saturation')

def logic_13538(world):
    _world_apply(world, 'sediment', 'co2', 'gap')

def logic_13539(world):
    _world_apply(world, 'sediment', 'photosynthesis_factor', 'direct')

def logic_13540(world):
    _world_apply(world, 'sediment', 'ice', 'square')

def logic_13541(world):
    _world_apply(world, 'sediment', 'evaporation', 'pulse')

def logic_13542(world):
    _world_apply(world, 'sediment', 'detritus', 'saturation')

def logic_13543(world):
    _world_apply(world, 'sediment', 'methane', 'gap')

def logic_13544(world):
    _world_apply(world, 'sediment', 'pathogen_load', 'direct')

def logic_13545(world):
    _world_apply(world, 'sediment', 'biodiversity', 'pulse')

def logic_13546(world):
    _world_apply(world, 'sediment', 'habitat_stress', 'saturation')

def logic_13547(world):
    _world_apply(world, 'sediment', 'erosion', 'gap')

def logic_13548(world):
    _world_apply(world, 'sediment', 'soil_depth', 'direct')

def logic_13549(world):
    _world_apply(world, 'sediment', 'root_density', 'square')

def logic_13550(world):
    _world_apply(world, 'sediment', 'wetland', 'pulse')

def logic_13551(world):
    _world_apply(world, 'sediment', 'carbon_storage', 'saturation')

def logic_13552(world):
    _world_apply(world, 'sediment', 'fire_risk', 'gap')

def logic_13553(world):
    _world_apply(world, 'sediment', 'ash', 'square')

def logic_13554(world):
    _world_apply(world, 'sediment', 'snowpack', 'pulse')

def logic_13555(world):
    _world_apply(world, 'sediment', 'groundwater', 'saturation')

def logic_13556(world):
    _world_apply(world, 'sediment', 'salinity', 'gap')

def logic_13557(world):
    _world_apply(world, 'sediment', 'algae', 'direct')

def logic_13558(world):
    _world_apply(world, 'sediment', 'organic_matter', 'square')

def logic_13559(world):
    _world_apply(world, 'sediment', 'deadwood', 'pulse')

def logic_13560(world):
    _world_apply(world, 'sediment', 'pollinators', 'saturation')

def logic_13561(world):
    _world_apply(world, 'sediment', 'flowers', 'direct')

def logic_13562(world):
    _world_apply(world, 'sediment', 'seed_bank', 'square')

def logic_13563(world):
    _world_apply(world, 'sediment', 'soil_carbon', 'pulse')

def logic_13564(world):
    _world_apply(world, 'sediment', 'surface_ice', 'saturation')

def logic_13565(world):
    _world_apply(world, 'salinity', 'temperature', 'gap')

def logic_13566(world):
    _world_apply(world, 'salinity', 'surface_water', 'direct')

def logic_13567(world):
    _world_apply(world, 'salinity', 'humidity', 'square')

def logic_13568(world):
    _world_apply(world, 'salinity', 'cloud', 'pulse')

def logic_13569(world):
    _world_apply(world, 'salinity', 'rain', 'gap')

def logic_13570(world):
    _world_apply(world, 'salinity', 'soil_moisture', 'direct')

def logic_13571(world):
    _world_apply(world, 'salinity', 'runoff', 'square')

def logic_13572(world):
    _world_apply(world, 'salinity', 'wind_x', 'pulse')

def logic_13573(world):
    _world_apply(world, 'salinity', 'wind_y', 'saturation')

def logic_13574(world):
    _world_apply(world, 'salinity', 'vegetation', 'gap')

def logic_13575(world):
    _world_apply(world, 'salinity', 'biomass', 'direct')

def logic_13576(world):
    _world_apply(world, 'salinity', 'herbivore', 'square')

def logic_13577(world):
    _world_apply(world, 'salinity', 'predator', 'saturation')

def logic_13578(world):
    _world_apply(world, 'salinity', 'carrion', 'gap')

def logic_13579(world):
    _world_apply(world, 'salinity', 'nutrients', 'direct')

def logic_13580(world):
    _world_apply(world, 'salinity', 'decomposition_rate', 'square')

def logic_13581(world):
    _world_apply(world, 'salinity', 'oxygen', 'pulse')

def logic_13582(world):
    _world_apply(world, 'salinity', 'co2', 'saturation')

def logic_13583(world):
    _world_apply(world, 'salinity', 'photosynthesis_factor', 'gap')

def logic_13584(world):
    _world_apply(world, 'salinity', 'ice', 'direct')

def logic_13585(world):
    _world_apply(world, 'salinity', 'evaporation', 'pulse')

def logic_13586(world):
    _world_apply(world, 'salinity', 'detritus', 'saturation')

def logic_13587(world):
    _world_apply(world, 'salinity', 'methane', 'gap')

def logic_13588(world):
    _world_apply(world, 'salinity', 'pathogen_load', 'direct')

def logic_13589(world):
    _world_apply(world, 'salinity', 'biodiversity', 'square')

def logic_13590(world):
    _world_apply(world, 'salinity', 'habitat_stress', 'pulse')

def logic_13591(world):
    _world_apply(world, 'salinity', 'erosion', 'saturation')

def logic_13592(world):
    _world_apply(world, 'salinity', 'soil_depth', 'gap')

def logic_13593(world):
    _world_apply(world, 'salinity', 'root_density', 'square')

def logic_13594(world):
    _world_apply(world, 'salinity', 'wetland', 'pulse')

def logic_13595(world):
    _world_apply(world, 'salinity', 'carbon_storage', 'saturation')

def logic_13596(world):
    _world_apply(world, 'salinity', 'fire_risk', 'gap')

def logic_13597(world):
    _world_apply(world, 'salinity', 'ash', 'direct')

def logic_13598(world):
    _world_apply(world, 'salinity', 'snowpack', 'square')

def logic_13599(world):
    _world_apply(world, 'salinity', 'groundwater', 'pulse')

def logic_13600(world):
    _world_apply(world, 'salinity', 'sediment', 'saturation')

def logic_13601(world):
    _world_apply(world, 'salinity', 'algae', 'direct')

def logic_13602(world):
    _world_apply(world, 'salinity', 'organic_matter', 'square')

def logic_13603(world):
    _world_apply(world, 'salinity', 'deadwood', 'pulse')

def logic_13604(world):
    _world_apply(world, 'salinity', 'pollinators', 'saturation')

def logic_13605(world):
    _world_apply(world, 'salinity', 'flowers', 'gap')

def logic_13606(world):
    _world_apply(world, 'salinity', 'seed_bank', 'direct')

def logic_13607(world):
    _world_apply(world, 'salinity', 'soil_carbon', 'square')

def logic_13608(world):
    _world_apply(world, 'salinity', 'surface_ice', 'pulse')

def logic_13609(world):
    _world_apply(world, 'algae', 'temperature', 'gap')

def logic_13610(world):
    _world_apply(world, 'algae', 'surface_water', 'direct')

def logic_13611(world):
    _world_apply(world, 'algae', 'humidity', 'square')

def logic_13612(world):
    _world_apply(world, 'algae', 'cloud', 'pulse')

def logic_13613(world):
    _world_apply(world, 'algae', 'rain', 'saturation')

def logic_13614(world):
    _world_apply(world, 'algae', 'soil_moisture', 'gap')

def logic_13615(world):
    _world_apply(world, 'algae', 'runoff', 'direct')

def logic_13616(world):
    _world_apply(world, 'algae', 'wind_x', 'square')

def logic_13617(world):
    _world_apply(world, 'algae', 'wind_y', 'saturation')

def logic_13618(world):
    _world_apply(world, 'algae', 'vegetation', 'gap')

def logic_13619(world):
    _world_apply(world, 'algae', 'biomass', 'direct')

def logic_13620(world):
    _world_apply(world, 'algae', 'herbivore', 'square')

def logic_13621(world):
    _world_apply(world, 'algae', 'predator', 'pulse')

def logic_13622(world):
    _world_apply(world, 'algae', 'carrion', 'saturation')

def logic_13623(world):
    _world_apply(world, 'algae', 'nutrients', 'gap')

def logic_13624(world):
    _world_apply(world, 'algae', 'decomposition_rate', 'direct')

def logic_13625(world):
    _world_apply(world, 'algae', 'oxygen', 'pulse')

def logic_13626(world):
    _world_apply(world, 'algae', 'co2', 'saturation')

def logic_13627(world):
    _world_apply(world, 'algae', 'photosynthesis_factor', 'gap')

def logic_13628(world):
    _world_apply(world, 'algae', 'ice', 'direct')

def logic_13629(world):
    _world_apply(world, 'algae', 'evaporation', 'square')

def logic_13630(world):
    _world_apply(world, 'algae', 'detritus', 'pulse')

def logic_13631(world):
    _world_apply(world, 'algae', 'methane', 'saturation')

def logic_13632(world):
    _world_apply(world, 'algae', 'pathogen_load', 'gap')

def logic_13633(world):
    _world_apply(world, 'algae', 'biodiversity', 'square')

def logic_13634(world):
    _world_apply(world, 'algae', 'habitat_stress', 'pulse')

def logic_13635(world):
    _world_apply(world, 'algae', 'erosion', 'saturation')

def logic_13636(world):
    _world_apply(world, 'algae', 'soil_depth', 'gap')

def logic_13637(world):
    _world_apply(world, 'algae', 'root_density', 'direct')

def logic_13638(world):
    _world_apply(world, 'algae', 'wetland', 'square')

def logic_13639(world):
    _world_apply(world, 'algae', 'carbon_storage', 'pulse')

def logic_13640(world):
    _world_apply(world, 'algae', 'fire_risk', 'saturation')

def logic_13641(world):
    _world_apply(world, 'algae', 'ash', 'direct')

def logic_13642(world):
    _world_apply(world, 'algae', 'snowpack', 'square')

def logic_13643(world):
    _world_apply(world, 'algae', 'groundwater', 'pulse')

def logic_13644(world):
    _world_apply(world, 'algae', 'sediment', 'saturation')

def logic_13645(world):
    _world_apply(world, 'algae', 'salinity', 'gap')

def logic_13646(world):
    _world_apply(world, 'algae', 'organic_matter', 'direct')

def logic_13647(world):
    _world_apply(world, 'algae', 'deadwood', 'square')

def logic_13648(world):
    _world_apply(world, 'algae', 'pollinators', 'pulse')

def logic_13649(world):
    _world_apply(world, 'algae', 'flowers', 'gap')

def logic_13650(world):
    _world_apply(world, 'algae', 'seed_bank', 'direct')

def logic_13651(world):
    _world_apply(world, 'algae', 'soil_carbon', 'square')

def logic_13652(world):
    _world_apply(world, 'algae', 'surface_ice', 'pulse')

def logic_13653(world):
    _world_apply(world, 'organic_matter', 'temperature', 'saturation')

def logic_13654(world):
    _world_apply(world, 'organic_matter', 'surface_water', 'gap')

def logic_13655(world):
    _world_apply(world, 'organic_matter', 'humidity', 'direct')

def logic_13656(world):
    _world_apply(world, 'organic_matter', 'cloud', 'square')

def logic_13657(world):
    _world_apply(world, 'organic_matter', 'rain', 'saturation')

def logic_13658(world):
    _world_apply(world, 'organic_matter', 'soil_moisture', 'gap')

def logic_13659(world):
    _world_apply(world, 'organic_matter', 'runoff', 'direct')

def logic_13660(world):
    _world_apply(world, 'organic_matter', 'wind_x', 'square')

def logic_13661(world):
    _world_apply(world, 'organic_matter', 'wind_y', 'pulse')

def logic_13662(world):
    _world_apply(world, 'organic_matter', 'vegetation', 'saturation')

def logic_13663(world):
    _world_apply(world, 'organic_matter', 'biomass', 'gap')

def logic_13664(world):
    _world_apply(world, 'organic_matter', 'herbivore', 'direct')

def logic_13665(world):
    _world_apply(world, 'organic_matter', 'predator', 'pulse')

def logic_13666(world):
    _world_apply(world, 'organic_matter', 'carrion', 'saturation')

def logic_13667(world):
    _world_apply(world, 'organic_matter', 'nutrients', 'gap')

def logic_13668(world):
    _world_apply(world, 'organic_matter', 'decomposition_rate', 'direct')

def logic_13669(world):
    _world_apply(world, 'organic_matter', 'oxygen', 'square')

def logic_13670(world):
    _world_apply(world, 'organic_matter', 'co2', 'pulse')

def logic_13671(world):
    _world_apply(world, 'organic_matter', 'photosynthesis_factor', 'saturation')

def logic_13672(world):
    _world_apply(world, 'organic_matter', 'ice', 'gap')

def logic_13673(world):
    _world_apply(world, 'organic_matter', 'evaporation', 'square')

def logic_13674(world):
    _world_apply(world, 'organic_matter', 'detritus', 'pulse')

def logic_13675(world):
    _world_apply(world, 'organic_matter', 'methane', 'saturation')

def logic_13676(world):
    _world_apply(world, 'organic_matter', 'pathogen_load', 'gap')

def logic_13677(world):
    _world_apply(world, 'organic_matter', 'biodiversity', 'direct')

def logic_13678(world):
    _world_apply(world, 'organic_matter', 'habitat_stress', 'square')

def logic_13679(world):
    _world_apply(world, 'organic_matter', 'erosion', 'pulse')

def logic_13680(world):
    _world_apply(world, 'organic_matter', 'soil_depth', 'saturation')

def logic_13681(world):
    _world_apply(world, 'organic_matter', 'root_density', 'direct')

def logic_13682(world):
    _world_apply(world, 'organic_matter', 'wetland', 'square')

def logic_13683(world):
    _world_apply(world, 'organic_matter', 'carbon_storage', 'pulse')

def logic_13684(world):
    _world_apply(world, 'organic_matter', 'fire_risk', 'saturation')

def logic_13685(world):
    _world_apply(world, 'organic_matter', 'ash', 'gap')

def logic_13686(world):
    _world_apply(world, 'organic_matter', 'snowpack', 'direct')

def logic_13687(world):
    _world_apply(world, 'organic_matter', 'groundwater', 'square')

def logic_13688(world):
    _world_apply(world, 'organic_matter', 'sediment', 'pulse')

def logic_13689(world):
    _world_apply(world, 'organic_matter', 'salinity', 'gap')

def logic_13690(world):
    _world_apply(world, 'organic_matter', 'algae', 'direct')

def logic_13691(world):
    _world_apply(world, 'organic_matter', 'deadwood', 'square')

def logic_13692(world):
    _world_apply(world, 'organic_matter', 'pollinators', 'pulse')

def logic_13693(world):
    _world_apply(world, 'organic_matter', 'flowers', 'saturation')

def logic_13694(world):
    _world_apply(world, 'organic_matter', 'seed_bank', 'gap')

def logic_13695(world):
    _world_apply(world, 'organic_matter', 'soil_carbon', 'direct')

def logic_13696(world):
    _world_apply(world, 'organic_matter', 'surface_ice', 'square')

def logic_13697(world):
    _world_apply(world, 'deadwood', 'temperature', 'saturation')

def logic_13698(world):
    _world_apply(world, 'deadwood', 'surface_water', 'gap')

def logic_13699(world):
    _world_apply(world, 'deadwood', 'humidity', 'direct')

def logic_13700(world):
    _world_apply(world, 'deadwood', 'cloud', 'square')

def logic_13701(world):
    _world_apply(world, 'deadwood', 'rain', 'pulse')

def logic_13702(world):
    _world_apply(world, 'deadwood', 'soil_moisture', 'saturation')

def logic_13703(world):
    _world_apply(world, 'deadwood', 'runoff', 'gap')

def logic_13704(world):
    _world_apply(world, 'deadwood', 'wind_x', 'direct')

def logic_13705(world):
    _world_apply(world, 'deadwood', 'wind_y', 'pulse')

def logic_13706(world):
    _world_apply(world, 'deadwood', 'vegetation', 'saturation')

def logic_13707(world):
    _world_apply(world, 'deadwood', 'biomass', 'gap')

def logic_13708(world):
    _world_apply(world, 'deadwood', 'herbivore', 'direct')

def logic_13709(world):
    _world_apply(world, 'deadwood', 'predator', 'square')

def logic_13710(world):
    _world_apply(world, 'deadwood', 'carrion', 'pulse')

def logic_13711(world):
    _world_apply(world, 'deadwood', 'nutrients', 'saturation')

def logic_13712(world):
    _world_apply(world, 'deadwood', 'decomposition_rate', 'gap')

def logic_13713(world):
    _world_apply(world, 'deadwood', 'oxygen', 'square')

def logic_13714(world):
    _world_apply(world, 'deadwood', 'co2', 'pulse')

def logic_13715(world):
    _world_apply(world, 'deadwood', 'photosynthesis_factor', 'saturation')

def logic_13716(world):
    _world_apply(world, 'deadwood', 'ice', 'gap')

def logic_13717(world):
    _world_apply(world, 'deadwood', 'evaporation', 'direct')

def logic_13718(world):
    _world_apply(world, 'deadwood', 'detritus', 'square')

def logic_13719(world):
    _world_apply(world, 'deadwood', 'methane', 'pulse')

def logic_13720(world):
    _world_apply(world, 'deadwood', 'pathogen_load', 'saturation')

def logic_13721(world):
    _world_apply(world, 'deadwood', 'biodiversity', 'direct')

def logic_13722(world):
    _world_apply(world, 'deadwood', 'habitat_stress', 'square')

def logic_13723(world):
    _world_apply(world, 'deadwood', 'erosion', 'pulse')

def logic_13724(world):
    _world_apply(world, 'deadwood', 'soil_depth', 'saturation')

def logic_13725(world):
    _world_apply(world, 'deadwood', 'root_density', 'gap')

def logic_13726(world):
    _world_apply(world, 'deadwood', 'wetland', 'direct')

def logic_13727(world):
    _world_apply(world, 'deadwood', 'carbon_storage', 'square')

def logic_13728(world):
    _world_apply(world, 'deadwood', 'fire_risk', 'pulse')

def logic_13729(world):
    _world_apply(world, 'deadwood', 'ash', 'gap')

def logic_13730(world):
    _world_apply(world, 'deadwood', 'snowpack', 'direct')

def logic_13731(world):
    _world_apply(world, 'deadwood', 'groundwater', 'square')

def logic_13732(world):
    _world_apply(world, 'deadwood', 'sediment', 'pulse')

def logic_13733(world):
    _world_apply(world, 'deadwood', 'salinity', 'saturation')

def logic_13734(world):
    _world_apply(world, 'deadwood', 'algae', 'gap')

def logic_13735(world):
    _world_apply(world, 'deadwood', 'organic_matter', 'direct')

def logic_13736(world):
    _world_apply(world, 'deadwood', 'pollinators', 'square')

def logic_13737(world):
    _world_apply(world, 'deadwood', 'flowers', 'saturation')

def logic_13738(world):
    _world_apply(world, 'deadwood', 'seed_bank', 'gap')

def logic_13739(world):
    _world_apply(world, 'deadwood', 'soil_carbon', 'direct')

def logic_13740(world):
    _world_apply(world, 'deadwood', 'surface_ice', 'square')

def logic_13741(world):
    _world_apply(world, 'pollinators', 'temperature', 'pulse')

def logic_13742(world):
    _world_apply(world, 'pollinators', 'surface_water', 'saturation')

def logic_13743(world):
    _world_apply(world, 'pollinators', 'humidity', 'gap')

def logic_13744(world):
    _world_apply(world, 'pollinators', 'cloud', 'direct')

def logic_13745(world):
    _world_apply(world, 'pollinators', 'rain', 'pulse')

def logic_13746(world):
    _world_apply(world, 'pollinators', 'soil_moisture', 'saturation')

def logic_13747(world):
    _world_apply(world, 'pollinators', 'runoff', 'gap')

def logic_13748(world):
    _world_apply(world, 'pollinators', 'wind_x', 'direct')

def logic_13749(world):
    _world_apply(world, 'pollinators', 'wind_y', 'square')

def logic_13750(world):
    _world_apply(world, 'pollinators', 'vegetation', 'pulse')

def logic_13751(world):
    _world_apply(world, 'pollinators', 'biomass', 'saturation')

def logic_13752(world):
    _world_apply(world, 'pollinators', 'herbivore', 'gap')

def logic_13753(world):
    _world_apply(world, 'pollinators', 'predator', 'square')

def logic_13754(world):
    _world_apply(world, 'pollinators', 'carrion', 'pulse')

def logic_13755(world):
    _world_apply(world, 'pollinators', 'nutrients', 'saturation')

def logic_13756(world):
    _world_apply(world, 'pollinators', 'decomposition_rate', 'gap')

def logic_13757(world):
    _world_apply(world, 'pollinators', 'oxygen', 'direct')

def logic_13758(world):
    _world_apply(world, 'pollinators', 'co2', 'square')

def logic_13759(world):
    _world_apply(world, 'pollinators', 'photosynthesis_factor', 'pulse')

def logic_13760(world):
    _world_apply(world, 'pollinators', 'ice', 'saturation')

def logic_13761(world):
    _world_apply(world, 'pollinators', 'evaporation', 'direct')

def logic_13762(world):
    _world_apply(world, 'pollinators', 'detritus', 'square')

def logic_13763(world):
    _world_apply(world, 'pollinators', 'methane', 'pulse')

def logic_13764(world):
    _world_apply(world, 'pollinators', 'pathogen_load', 'saturation')

def logic_13765(world):
    _world_apply(world, 'pollinators', 'biodiversity', 'gap')

def logic_13766(world):
    _world_apply(world, 'pollinators', 'habitat_stress', 'direct')

def logic_13767(world):
    _world_apply(world, 'pollinators', 'erosion', 'square')

def logic_13768(world):
    _world_apply(world, 'pollinators', 'soil_depth', 'pulse')

def logic_13769(world):
    _world_apply(world, 'pollinators', 'root_density', 'gap')

def logic_13770(world):
    _world_apply(world, 'pollinators', 'wetland', 'direct')

def logic_13771(world):
    _world_apply(world, 'pollinators', 'carbon_storage', 'square')

def logic_13772(world):
    _world_apply(world, 'pollinators', 'fire_risk', 'pulse')

def logic_13773(world):
    _world_apply(world, 'pollinators', 'ash', 'saturation')

def logic_13774(world):
    _world_apply(world, 'pollinators', 'snowpack', 'gap')

def logic_13775(world):
    _world_apply(world, 'pollinators', 'groundwater', 'direct')

def logic_13776(world):
    _world_apply(world, 'pollinators', 'sediment', 'square')

def logic_13777(world):
    _world_apply(world, 'pollinators', 'salinity', 'saturation')

def logic_13778(world):
    _world_apply(world, 'pollinators', 'algae', 'gap')

def logic_13779(world):
    _world_apply(world, 'pollinators', 'organic_matter', 'direct')

def logic_13780(world):
    _world_apply(world, 'pollinators', 'deadwood', 'square')

def logic_13781(world):
    _world_apply(world, 'pollinators', 'flowers', 'pulse')

def logic_13782(world):
    _world_apply(world, 'pollinators', 'seed_bank', 'saturation')

def logic_13783(world):
    _world_apply(world, 'pollinators', 'soil_carbon', 'gap')

def logic_13784(world):
    _world_apply(world, 'pollinators', 'surface_ice', 'direct')

def logic_13785(world):
    _world_apply(world, 'flowers', 'temperature', 'pulse')

def logic_13786(world):
    _world_apply(world, 'flowers', 'surface_water', 'saturation')

def logic_13787(world):
    _world_apply(world, 'flowers', 'humidity', 'gap')

def logic_13788(world):
    _world_apply(world, 'flowers', 'cloud', 'direct')

def logic_13789(world):
    _world_apply(world, 'flowers', 'rain', 'square')

def logic_13790(world):
    _world_apply(world, 'flowers', 'soil_moisture', 'pulse')

def logic_13791(world):
    _world_apply(world, 'flowers', 'runoff', 'saturation')

def logic_13792(world):
    _world_apply(world, 'flowers', 'wind_x', 'gap')

def logic_13793(world):
    _world_apply(world, 'flowers', 'wind_y', 'square')

def logic_13794(world):
    _world_apply(world, 'flowers', 'vegetation', 'pulse')

def logic_13795(world):
    _world_apply(world, 'flowers', 'biomass', 'saturation')

def logic_13796(world):
    _world_apply(world, 'flowers', 'herbivore', 'gap')

def logic_13797(world):
    _world_apply(world, 'flowers', 'predator', 'direct')

def logic_13798(world):
    _world_apply(world, 'flowers', 'carrion', 'square')

def logic_13799(world):
    _world_apply(world, 'flowers', 'nutrients', 'pulse')

def logic_13800(world):
    _world_apply(world, 'flowers', 'decomposition_rate', 'saturation')

def logic_13801(world):
    _world_apply(world, 'flowers', 'oxygen', 'direct')

def logic_13802(world):
    _world_apply(world, 'flowers', 'co2', 'square')

def logic_13803(world):
    _world_apply(world, 'flowers', 'photosynthesis_factor', 'pulse')

def logic_13804(world):
    _world_apply(world, 'flowers', 'ice', 'saturation')

def logic_13805(world):
    _world_apply(world, 'flowers', 'evaporation', 'gap')

def logic_13806(world):
    _world_apply(world, 'flowers', 'detritus', 'direct')

def logic_13807(world):
    _world_apply(world, 'flowers', 'methane', 'square')

def logic_13808(world):
    _world_apply(world, 'flowers', 'pathogen_load', 'pulse')

def logic_13809(world):
    _world_apply(world, 'flowers', 'biodiversity', 'gap')

def logic_13810(world):
    _world_apply(world, 'flowers', 'habitat_stress', 'direct')

def logic_13811(world):
    _world_apply(world, 'flowers', 'erosion', 'square')

def logic_13812(world):
    _world_apply(world, 'flowers', 'soil_depth', 'pulse')

def logic_13813(world):
    _world_apply(world, 'flowers', 'root_density', 'saturation')

def logic_13814(world):
    _world_apply(world, 'flowers', 'wetland', 'gap')

def logic_13815(world):
    _world_apply(world, 'flowers', 'carbon_storage', 'direct')

def logic_13816(world):
    _world_apply(world, 'flowers', 'fire_risk', 'square')

def logic_13817(world):
    _world_apply(world, 'flowers', 'ash', 'saturation')

def logic_13818(world):
    _world_apply(world, 'flowers', 'snowpack', 'gap')

def logic_13819(world):
    _world_apply(world, 'flowers', 'groundwater', 'direct')

def logic_13820(world):
    _world_apply(world, 'flowers', 'sediment', 'square')

def logic_13821(world):
    _world_apply(world, 'flowers', 'salinity', 'pulse')

def logic_13822(world):
    _world_apply(world, 'flowers', 'algae', 'saturation')

def logic_13823(world):
    _world_apply(world, 'flowers', 'organic_matter', 'gap')

def logic_13824(world):
    _world_apply(world, 'flowers', 'deadwood', 'direct')

def logic_13825(world):
    _world_apply(world, 'flowers', 'pollinators', 'pulse')

def logic_13826(world):
    _world_apply(world, 'flowers', 'seed_bank', 'saturation')

def logic_13827(world):
    _world_apply(world, 'flowers', 'soil_carbon', 'gap')

def logic_13828(world):
    _world_apply(world, 'flowers', 'surface_ice', 'direct')

def logic_13829(world):
    _world_apply(world, 'seed_bank', 'temperature', 'square')

def logic_13830(world):
    _world_apply(world, 'seed_bank', 'surface_water', 'pulse')

def logic_13831(world):
    _world_apply(world, 'seed_bank', 'humidity', 'saturation')

def logic_13832(world):
    _world_apply(world, 'seed_bank', 'cloud', 'gap')

def logic_13833(world):
    _world_apply(world, 'seed_bank', 'rain', 'square')

def logic_13834(world):
    _world_apply(world, 'seed_bank', 'soil_moisture', 'pulse')

def logic_13835(world):
    _world_apply(world, 'seed_bank', 'runoff', 'saturation')

def logic_13836(world):
    _world_apply(world, 'seed_bank', 'wind_x', 'gap')

def logic_13837(world):
    _world_apply(world, 'seed_bank', 'wind_y', 'direct')

def logic_13838(world):
    _world_apply(world, 'seed_bank', 'vegetation', 'square')

def logic_13839(world):
    _world_apply(world, 'seed_bank', 'biomass', 'pulse')

def logic_13840(world):
    _world_apply(world, 'seed_bank', 'herbivore', 'saturation')

def logic_13841(world):
    _world_apply(world, 'seed_bank', 'predator', 'direct')

def logic_13842(world):
    _world_apply(world, 'seed_bank', 'carrion', 'square')

def logic_13843(world):
    _world_apply(world, 'seed_bank', 'nutrients', 'pulse')

def logic_13844(world):
    _world_apply(world, 'seed_bank', 'decomposition_rate', 'saturation')

def logic_13845(world):
    _world_apply(world, 'seed_bank', 'oxygen', 'gap')

def logic_13846(world):
    _world_apply(world, 'seed_bank', 'co2', 'direct')

def logic_13847(world):
    _world_apply(world, 'seed_bank', 'photosynthesis_factor', 'square')

def logic_13848(world):
    _world_apply(world, 'seed_bank', 'ice', 'pulse')

def logic_13849(world):
    _world_apply(world, 'seed_bank', 'evaporation', 'gap')

def logic_13850(world):
    _world_apply(world, 'seed_bank', 'detritus', 'direct')

def logic_13851(world):
    _world_apply(world, 'seed_bank', 'methane', 'square')

def logic_13852(world):
    _world_apply(world, 'seed_bank', 'pathogen_load', 'pulse')

def logic_13853(world):
    _world_apply(world, 'seed_bank', 'biodiversity', 'saturation')

def logic_13854(world):
    _world_apply(world, 'seed_bank', 'habitat_stress', 'gap')

def logic_13855(world):
    _world_apply(world, 'seed_bank', 'erosion', 'direct')

def logic_13856(world):
    _world_apply(world, 'seed_bank', 'soil_depth', 'square')

def logic_13857(world):
    _world_apply(world, 'seed_bank', 'root_density', 'saturation')

def logic_13858(world):
    _world_apply(world, 'seed_bank', 'wetland', 'gap')

def logic_13859(world):
    _world_apply(world, 'seed_bank', 'carbon_storage', 'direct')

def logic_13860(world):
    _world_apply(world, 'seed_bank', 'fire_risk', 'square')

def logic_13861(world):
    _world_apply(world, 'seed_bank', 'ash', 'pulse')

def logic_13862(world):
    _world_apply(world, 'seed_bank', 'snowpack', 'saturation')

def logic_13863(world):
    _world_apply(world, 'seed_bank', 'groundwater', 'gap')

def logic_13864(world):
    _world_apply(world, 'seed_bank', 'sediment', 'direct')

def logic_13865(world):
    _world_apply(world, 'seed_bank', 'salinity', 'pulse')

def logic_13866(world):
    _world_apply(world, 'seed_bank', 'algae', 'saturation')

def logic_13867(world):
    _world_apply(world, 'seed_bank', 'organic_matter', 'gap')

def logic_13868(world):
    _world_apply(world, 'seed_bank', 'deadwood', 'direct')

def logic_13869(world):
    _world_apply(world, 'seed_bank', 'pollinators', 'square')

def logic_13870(world):
    _world_apply(world, 'seed_bank', 'flowers', 'pulse')

def logic_13871(world):
    _world_apply(world, 'seed_bank', 'soil_carbon', 'saturation')

def logic_13872(world):
    _world_apply(world, 'seed_bank', 'surface_ice', 'gap')

def logic_13873(world):
    _world_apply(world, 'soil_carbon', 'temperature', 'square')

def logic_13874(world):
    _world_apply(world, 'soil_carbon', 'surface_water', 'pulse')

def logic_13875(world):
    _world_apply(world, 'soil_carbon', 'humidity', 'saturation')

def logic_13876(world):
    _world_apply(world, 'soil_carbon', 'cloud', 'gap')

def logic_13877(world):
    _world_apply(world, 'soil_carbon', 'rain', 'direct')

def logic_13878(world):
    _world_apply(world, 'soil_carbon', 'soil_moisture', 'square')

def logic_13879(world):
    _world_apply(world, 'soil_carbon', 'runoff', 'pulse')

def logic_13880(world):
    _world_apply(world, 'soil_carbon', 'wind_x', 'saturation')

def logic_13881(world):
    _world_apply(world, 'soil_carbon', 'wind_y', 'direct')

def logic_13882(world):
    _world_apply(world, 'soil_carbon', 'vegetation', 'square')

def logic_13883(world):
    _world_apply(world, 'soil_carbon', 'biomass', 'pulse')

def logic_13884(world):
    _world_apply(world, 'soil_carbon', 'herbivore', 'saturation')

def logic_13885(world):
    _world_apply(world, 'soil_carbon', 'predator', 'gap')

def logic_13886(world):
    _world_apply(world, 'soil_carbon', 'carrion', 'direct')

def logic_13887(world):
    _world_apply(world, 'soil_carbon', 'nutrients', 'square')

def logic_13888(world):
    _world_apply(world, 'soil_carbon', 'decomposition_rate', 'pulse')

def logic_13889(world):
    _world_apply(world, 'soil_carbon', 'oxygen', 'gap')

def logic_13890(world):
    _world_apply(world, 'soil_carbon', 'co2', 'direct')

def logic_13891(world):
    _world_apply(world, 'soil_carbon', 'photosynthesis_factor', 'square')

def logic_13892(world):
    _world_apply(world, 'soil_carbon', 'ice', 'pulse')

def logic_13893(world):
    _world_apply(world, 'soil_carbon', 'evaporation', 'saturation')

def logic_13894(world):
    _world_apply(world, 'soil_carbon', 'detritus', 'gap')

def logic_13895(world):
    _world_apply(world, 'soil_carbon', 'methane', 'direct')

def logic_13896(world):
    _world_apply(world, 'soil_carbon', 'pathogen_load', 'square')

def logic_13897(world):
    _world_apply(world, 'soil_carbon', 'biodiversity', 'saturation')

def logic_13898(world):
    _world_apply(world, 'soil_carbon', 'habitat_stress', 'gap')

def logic_13899(world):
    _world_apply(world, 'soil_carbon', 'erosion', 'direct')

def logic_13900(world):
    _world_apply(world, 'soil_carbon', 'soil_depth', 'square')

def logic_13901(world):
    _world_apply(world, 'soil_carbon', 'root_density', 'pulse')

def logic_13902(world):
    _world_apply(world, 'soil_carbon', 'wetland', 'saturation')

def logic_13903(world):
    _world_apply(world, 'soil_carbon', 'carbon_storage', 'gap')

def logic_13904(world):
    _world_apply(world, 'soil_carbon', 'fire_risk', 'direct')

def logic_13905(world):
    _world_apply(world, 'soil_carbon', 'ash', 'pulse')

def logic_13906(world):
    _world_apply(world, 'soil_carbon', 'snowpack', 'saturation')

def logic_13907(world):
    _world_apply(world, 'soil_carbon', 'groundwater', 'gap')

def logic_13908(world):
    _world_apply(world, 'soil_carbon', 'sediment', 'direct')

def logic_13909(world):
    _world_apply(world, 'soil_carbon', 'salinity', 'square')

def logic_13910(world):
    _world_apply(world, 'soil_carbon', 'algae', 'pulse')

def logic_13911(world):
    _world_apply(world, 'soil_carbon', 'organic_matter', 'saturation')

def logic_13912(world):
    _world_apply(world, 'soil_carbon', 'deadwood', 'gap')

def logic_13913(world):
    _world_apply(world, 'soil_carbon', 'pollinators', 'square')

def logic_13914(world):
    _world_apply(world, 'soil_carbon', 'flowers', 'pulse')

def logic_13915(world):
    _world_apply(world, 'soil_carbon', 'seed_bank', 'saturation')

def logic_13916(world):
    _world_apply(world, 'soil_carbon', 'surface_ice', 'gap')

def logic_13917(world):
    _world_apply(world, 'surface_ice', 'temperature', 'direct')

def logic_13918(world):
    _world_apply(world, 'surface_ice', 'surface_water', 'square')

def logic_13919(world):
    _world_apply(world, 'surface_ice', 'humidity', 'pulse')

def logic_13920(world):
    _world_apply(world, 'surface_ice', 'cloud', 'saturation')

def logic_13921(world):
    _world_apply(world, 'surface_ice', 'rain', 'direct')

def logic_13922(world):
    _world_apply(world, 'surface_ice', 'soil_moisture', 'square')

def logic_13923(world):
    _world_apply(world, 'surface_ice', 'runoff', 'pulse')

def logic_13924(world):
    _world_apply(world, 'surface_ice', 'wind_x', 'saturation')

def logic_13925(world):
    _world_apply(world, 'surface_ice', 'wind_y', 'gap')

def logic_13926(world):
    _world_apply(world, 'surface_ice', 'vegetation', 'direct')

def logic_13927(world):
    _world_apply(world, 'surface_ice', 'biomass', 'square')

def logic_13928(world):
    _world_apply(world, 'surface_ice', 'herbivore', 'pulse')

def logic_13929(world):
    _world_apply(world, 'surface_ice', 'predator', 'gap')

def logic_13930(world):
    _world_apply(world, 'surface_ice', 'carrion', 'direct')

def logic_13931(world):
    _world_apply(world, 'surface_ice', 'nutrients', 'square')

def logic_13932(world):
    _world_apply(world, 'surface_ice', 'decomposition_rate', 'pulse')

def logic_13933(world):
    _world_apply(world, 'surface_ice', 'oxygen', 'saturation')

def logic_13934(world):
    _world_apply(world, 'surface_ice', 'co2', 'gap')

def logic_13935(world):
    _world_apply(world, 'surface_ice', 'photosynthesis_factor', 'direct')

def logic_13936(world):
    _world_apply(world, 'surface_ice', 'ice', 'square')

def logic_13937(world):
    _world_apply(world, 'surface_ice', 'evaporation', 'saturation')

def logic_13938(world):
    _world_apply(world, 'surface_ice', 'detritus', 'gap')

def logic_13939(world):
    _world_apply(world, 'surface_ice', 'methane', 'direct')

def logic_13940(world):
    _world_apply(world, 'surface_ice', 'pathogen_load', 'square')

def logic_13941(world):
    _world_apply(world, 'surface_ice', 'biodiversity', 'pulse')

def logic_13942(world):
    _world_apply(world, 'surface_ice', 'habitat_stress', 'saturation')

def logic_13943(world):
    _world_apply(world, 'surface_ice', 'erosion', 'gap')

def logic_13944(world):
    _world_apply(world, 'surface_ice', 'soil_depth', 'direct')

def logic_13945(world):
    _world_apply(world, 'surface_ice', 'root_density', 'pulse')

def logic_13946(world):
    _world_apply(world, 'surface_ice', 'wetland', 'saturation')

def logic_13947(world):
    _world_apply(world, 'surface_ice', 'carbon_storage', 'gap')

def logic_13948(world):
    _world_apply(world, 'surface_ice', 'fire_risk', 'direct')

def logic_13949(world):
    _world_apply(world, 'surface_ice', 'ash', 'square')

def logic_13950(world):
    _world_apply(world, 'surface_ice', 'snowpack', 'pulse')

def logic_13951(world):
    _world_apply(world, 'surface_ice', 'groundwater', 'saturation')

def logic_13952(world):
    _world_apply(world, 'surface_ice', 'sediment', 'gap')

def logic_13953(world):
    _world_apply(world, 'surface_ice', 'salinity', 'square')

def logic_13954(world):
    _world_apply(world, 'surface_ice', 'algae', 'pulse')

def logic_13955(world):
    _world_apply(world, 'surface_ice', 'organic_matter', 'saturation')

def logic_13956(world):
    _world_apply(world, 'surface_ice', 'deadwood', 'gap')

def logic_13957(world):
    _world_apply(world, 'surface_ice', 'pollinators', 'direct')

def logic_13958(world):
    _world_apply(world, 'surface_ice', 'flowers', 'square')

def logic_13959(world):
    _world_apply(world, 'surface_ice', 'seed_bank', 'pulse')

def logic_13960(world):
    _world_apply(world, 'surface_ice', 'soil_carbon', 'saturation')

def logic_13961(world):
    _world_apply(world, 'temperature', 'surface_water', 'direct')

def logic_13962(world):
    _world_apply(world, 'temperature', 'humidity', 'square')

def logic_13963(world):
    _world_apply(world, 'temperature', 'cloud', 'pulse')

def logic_13964(world):
    _world_apply(world, 'temperature', 'rain', 'saturation')

def logic_13965(world):
    _world_apply(world, 'temperature', 'soil_moisture', 'gap')

def logic_13966(world):
    _world_apply(world, 'temperature', 'runoff', 'direct')

def logic_13967(world):
    _world_apply(world, 'temperature', 'wind_x', 'square')

def logic_13968(world):
    _world_apply(world, 'temperature', 'wind_y', 'pulse')

def logic_13969(world):
    _world_apply(world, 'temperature', 'vegetation', 'gap')

def logic_13970(world):
    _world_apply(world, 'temperature', 'biomass', 'direct')

def logic_13971(world):
    _world_apply(world, 'temperature', 'herbivore', 'square')

def logic_13972(world):
    _world_apply(world, 'temperature', 'predator', 'pulse')

def logic_13973(world):
    _world_apply(world, 'temperature', 'carrion', 'saturation')

def logic_13974(world):
    _world_apply(world, 'temperature', 'nutrients', 'gap')

def logic_13975(world):
    _world_apply(world, 'temperature', 'decomposition_rate', 'direct')

def logic_13976(world):
    _world_apply(world, 'temperature', 'oxygen', 'square')

def logic_13977(world):
    _world_apply(world, 'temperature', 'co2', 'saturation')

def logic_13978(world):
    _world_apply(world, 'temperature', 'photosynthesis_factor', 'gap')

def logic_13979(world):
    _world_apply(world, 'temperature', 'ice', 'direct')

def logic_13980(world):
    _world_apply(world, 'temperature', 'evaporation', 'square')

def logic_13981(world):
    _world_apply(world, 'temperature', 'detritus', 'pulse')

def logic_13982(world):
    _world_apply(world, 'temperature', 'methane', 'saturation')

def logic_13983(world):
    _world_apply(world, 'temperature', 'pathogen_load', 'gap')

def logic_13984(world):
    _world_apply(world, 'temperature', 'biodiversity', 'direct')

def logic_13985(world):
    _world_apply(world, 'temperature', 'habitat_stress', 'pulse')

def logic_13986(world):
    _world_apply(world, 'temperature', 'erosion', 'saturation')

def logic_13987(world):
    _world_apply(world, 'temperature', 'soil_depth', 'gap')

def logic_13988(world):
    _world_apply(world, 'temperature', 'root_density', 'direct')

def logic_13989(world):
    _world_apply(world, 'temperature', 'wetland', 'square')

def logic_13990(world):
    _world_apply(world, 'temperature', 'carbon_storage', 'pulse')

def logic_13991(world):
    _world_apply(world, 'temperature', 'fire_risk', 'saturation')

def logic_13992(world):
    _world_apply(world, 'temperature', 'ash', 'gap')

def logic_13993(world):
    _world_apply(world, 'temperature', 'snowpack', 'square')

def logic_13994(world):
    _world_apply(world, 'temperature', 'groundwater', 'pulse')

def logic_13995(world):
    _world_apply(world, 'temperature', 'sediment', 'saturation')

def logic_13996(world):
    _world_apply(world, 'temperature', 'salinity', 'gap')

def logic_13997(world):
    _world_apply(world, 'temperature', 'algae', 'direct')

def logic_13998(world):
    _world_apply(world, 'temperature', 'organic_matter', 'square')

def logic_13999(world):
    _world_apply(world, 'temperature', 'deadwood', 'pulse')

def logic_14000(world):
    _world_apply(world, 'temperature', 'pollinators', 'saturation')

def logic_14001(world):
    _world_apply(world, 'temperature', 'flowers', 'direct')

def logic_14002(world):
    _world_apply(world, 'temperature', 'seed_bank', 'square')

def logic_14003(world):
    _world_apply(world, 'temperature', 'soil_carbon', 'pulse')

def logic_14004(world):
    _world_apply(world, 'temperature', 'surface_ice', 'saturation')

def logic_14005(world):
    _world_apply(world, 'surface_water', 'temperature', 'gap')

def logic_14006(world):
    _world_apply(world, 'surface_water', 'humidity', 'direct')

def logic_14007(world):
    _world_apply(world, 'surface_water', 'cloud', 'square')

def logic_14008(world):
    _world_apply(world, 'surface_water', 'rain', 'pulse')

def logic_14009(world):
    _world_apply(world, 'surface_water', 'soil_moisture', 'gap')

def logic_14010(world):
    _world_apply(world, 'surface_water', 'runoff', 'direct')

def logic_14011(world):
    _world_apply(world, 'surface_water', 'wind_x', 'square')

def logic_14012(world):
    _world_apply(world, 'surface_water', 'wind_y', 'pulse')

def logic_14013(world):
    _world_apply(world, 'surface_water', 'vegetation', 'saturation')

def logic_14014(world):
    _world_apply(world, 'surface_water', 'biomass', 'gap')

def logic_14015(world):
    _world_apply(world, 'surface_water', 'herbivore', 'direct')

def logic_14016(world):
    _world_apply(world, 'surface_water', 'predator', 'square')

def logic_14017(world):
    _world_apply(world, 'surface_water', 'carrion', 'saturation')

def logic_14018(world):
    _world_apply(world, 'surface_water', 'nutrients', 'gap')

def logic_14019(world):
    _world_apply(world, 'surface_water', 'decomposition_rate', 'direct')

def logic_14020(world):
    _world_apply(world, 'surface_water', 'oxygen', 'square')

def logic_14021(world):
    _world_apply(world, 'surface_water', 'co2', 'pulse')

def logic_14022(world):
    _world_apply(world, 'surface_water', 'photosynthesis_factor', 'saturation')

def logic_14023(world):
    _world_apply(world, 'surface_water', 'ice', 'gap')

def logic_14024(world):
    _world_apply(world, 'surface_water', 'evaporation', 'direct')

def logic_14025(world):
    _world_apply(world, 'surface_water', 'detritus', 'pulse')

def logic_14026(world):
    _world_apply(world, 'surface_water', 'methane', 'saturation')

def logic_14027(world):
    _world_apply(world, 'surface_water', 'pathogen_load', 'gap')

def logic_14028(world):
    _world_apply(world, 'surface_water', 'biodiversity', 'direct')

def logic_14029(world):
    _world_apply(world, 'surface_water', 'habitat_stress', 'square')

def logic_14030(world):
    _world_apply(world, 'surface_water', 'erosion', 'pulse')

def logic_14031(world):
    _world_apply(world, 'surface_water', 'soil_depth', 'saturation')

def logic_14032(world):
    _world_apply(world, 'surface_water', 'root_density', 'gap')

def logic_14033(world):
    _world_apply(world, 'surface_water', 'wetland', 'square')

def logic_14034(world):
    _world_apply(world, 'surface_water', 'carbon_storage', 'pulse')

def logic_14035(world):
    _world_apply(world, 'surface_water', 'fire_risk', 'saturation')

def logic_14036(world):
    _world_apply(world, 'surface_water', 'ash', 'gap')

def logic_14037(world):
    _world_apply(world, 'surface_water', 'snowpack', 'direct')

def logic_14038(world):
    _world_apply(world, 'surface_water', 'groundwater', 'square')

def logic_14039(world):
    _world_apply(world, 'surface_water', 'sediment', 'pulse')

def logic_14040(world):
    _world_apply(world, 'surface_water', 'salinity', 'saturation')

def logic_14041(world):
    _world_apply(world, 'surface_water', 'algae', 'direct')

def logic_14042(world):
    _world_apply(world, 'surface_water', 'organic_matter', 'square')

def logic_14043(world):
    _world_apply(world, 'surface_water', 'deadwood', 'pulse')

def logic_14044(world):
    _world_apply(world, 'surface_water', 'pollinators', 'saturation')

def logic_14045(world):
    _world_apply(world, 'surface_water', 'flowers', 'gap')

def logic_14046(world):
    _world_apply(world, 'surface_water', 'seed_bank', 'direct')

def logic_14047(world):
    _world_apply(world, 'surface_water', 'soil_carbon', 'square')

def logic_14048(world):
    _world_apply(world, 'surface_water', 'surface_ice', 'pulse')

def logic_14049(world):
    _world_apply(world, 'humidity', 'temperature', 'gap')

def logic_14050(world):
    _world_apply(world, 'humidity', 'surface_water', 'direct')

def logic_14051(world):
    _world_apply(world, 'humidity', 'cloud', 'square')

def logic_14052(world):
    _world_apply(world, 'humidity', 'rain', 'pulse')

def logic_14053(world):
    _world_apply(world, 'humidity', 'soil_moisture', 'saturation')

def logic_14054(world):
    _world_apply(world, 'humidity', 'runoff', 'gap')

def logic_14055(world):
    _world_apply(world, 'humidity', 'wind_x', 'direct')

def logic_14056(world):
    _world_apply(world, 'humidity', 'wind_y', 'square')

def logic_14057(world):
    _world_apply(world, 'humidity', 'vegetation', 'saturation')

def logic_14058(world):
    _world_apply(world, 'humidity', 'biomass', 'gap')

def logic_14059(world):
    _world_apply(world, 'humidity', 'herbivore', 'direct')

def logic_14060(world):
    _world_apply(world, 'humidity', 'predator', 'square')

def logic_14061(world):
    _world_apply(world, 'humidity', 'carrion', 'pulse')

def logic_14062(world):
    _world_apply(world, 'humidity', 'nutrients', 'saturation')

def logic_14063(world):
    _world_apply(world, 'humidity', 'decomposition_rate', 'gap')

def logic_14064(world):
    _world_apply(world, 'humidity', 'oxygen', 'direct')

def logic_14065(world):
    _world_apply(world, 'humidity', 'co2', 'pulse')

def logic_14066(world):
    _world_apply(world, 'humidity', 'photosynthesis_factor', 'saturation')

def logic_14067(world):
    _world_apply(world, 'humidity', 'ice', 'gap')

def logic_14068(world):
    _world_apply(world, 'humidity', 'evaporation', 'direct')

def logic_14069(world):
    _world_apply(world, 'humidity', 'detritus', 'square')

def logic_14070(world):
    _world_apply(world, 'humidity', 'methane', 'pulse')

def logic_14071(world):
    _world_apply(world, 'humidity', 'pathogen_load', 'saturation')

def logic_14072(world):
    _world_apply(world, 'humidity', 'biodiversity', 'gap')

def logic_14073(world):
    _world_apply(world, 'humidity', 'habitat_stress', 'square')

def logic_14074(world):
    _world_apply(world, 'humidity', 'erosion', 'pulse')

def logic_14075(world):
    _world_apply(world, 'humidity', 'soil_depth', 'saturation')

def logic_14076(world):
    _world_apply(world, 'humidity', 'root_density', 'gap')

def logic_14077(world):
    _world_apply(world, 'humidity', 'wetland', 'direct')

def logic_14078(world):
    _world_apply(world, 'humidity', 'carbon_storage', 'square')

def logic_14079(world):
    _world_apply(world, 'humidity', 'fire_risk', 'pulse')

def logic_14080(world):
    _world_apply(world, 'humidity', 'ash', 'saturation')

def logic_14081(world):
    _world_apply(world, 'humidity', 'snowpack', 'direct')

def logic_14082(world):
    _world_apply(world, 'humidity', 'groundwater', 'square')

def logic_14083(world):
    _world_apply(world, 'humidity', 'sediment', 'pulse')

def logic_14084(world):
    _world_apply(world, 'humidity', 'salinity', 'saturation')

def logic_14085(world):
    _world_apply(world, 'humidity', 'algae', 'gap')

def logic_14086(world):
    _world_apply(world, 'humidity', 'organic_matter', 'direct')

def logic_14087(world):
    _world_apply(world, 'humidity', 'deadwood', 'square')

def logic_14088(world):
    _world_apply(world, 'humidity', 'pollinators', 'pulse')

def logic_14089(world):
    _world_apply(world, 'humidity', 'flowers', 'gap')

def logic_14090(world):
    _world_apply(world, 'humidity', 'seed_bank', 'direct')

def logic_14091(world):
    _world_apply(world, 'humidity', 'soil_carbon', 'square')

def logic_14092(world):
    _world_apply(world, 'humidity', 'surface_ice', 'pulse')

def logic_14093(world):
    _world_apply(world, 'cloud', 'temperature', 'saturation')

def logic_14094(world):
    _world_apply(world, 'cloud', 'surface_water', 'gap')

def logic_14095(world):
    _world_apply(world, 'cloud', 'humidity', 'direct')

def logic_14096(world):
    _world_apply(world, 'cloud', 'rain', 'square')

def logic_14097(world):
    _world_apply(world, 'cloud', 'soil_moisture', 'saturation')

def logic_14098(world):
    _world_apply(world, 'cloud', 'runoff', 'gap')

def logic_14099(world):
    _world_apply(world, 'cloud', 'wind_x', 'direct')

def logic_14100(world):
    _world_apply(world, 'cloud', 'wind_y', 'square')

def logic_14101(world):
    _world_apply(world, 'cloud', 'vegetation', 'pulse')

def logic_14102(world):
    _world_apply(world, 'cloud', 'biomass', 'saturation')

def logic_14103(world):
    _world_apply(world, 'cloud', 'herbivore', 'gap')

def logic_14104(world):
    _world_apply(world, 'cloud', 'predator', 'direct')

def logic_14105(world):
    _world_apply(world, 'cloud', 'carrion', 'pulse')

def logic_14106(world):
    _world_apply(world, 'cloud', 'nutrients', 'saturation')

def logic_14107(world):
    _world_apply(world, 'cloud', 'decomposition_rate', 'gap')

def logic_14108(world):
    _world_apply(world, 'cloud', 'oxygen', 'direct')

def logic_14109(world):
    _world_apply(world, 'cloud', 'co2', 'square')

def logic_14110(world):
    _world_apply(world, 'cloud', 'photosynthesis_factor', 'pulse')

def logic_14111(world):
    _world_apply(world, 'cloud', 'ice', 'saturation')

def logic_14112(world):
    _world_apply(world, 'cloud', 'evaporation', 'gap')

def logic_14113(world):
    _world_apply(world, 'cloud', 'detritus', 'square')

def logic_14114(world):
    _world_apply(world, 'cloud', 'methane', 'pulse')

def logic_14115(world):
    _world_apply(world, 'cloud', 'pathogen_load', 'saturation')

def logic_14116(world):
    _world_apply(world, 'cloud', 'biodiversity', 'gap')

def logic_14117(world):
    _world_apply(world, 'cloud', 'habitat_stress', 'direct')

def logic_14118(world):
    _world_apply(world, 'cloud', 'erosion', 'square')

def logic_14119(world):
    _world_apply(world, 'cloud', 'soil_depth', 'pulse')

def logic_14120(world):
    _world_apply(world, 'cloud', 'root_density', 'saturation')

def logic_14121(world):
    _world_apply(world, 'cloud', 'wetland', 'direct')

def logic_14122(world):
    _world_apply(world, 'cloud', 'carbon_storage', 'square')

def logic_14123(world):
    _world_apply(world, 'cloud', 'fire_risk', 'pulse')

def logic_14124(world):
    _world_apply(world, 'cloud', 'ash', 'saturation')

def logic_14125(world):
    _world_apply(world, 'cloud', 'snowpack', 'gap')

def logic_14126(world):
    _world_apply(world, 'cloud', 'groundwater', 'direct')

def logic_14127(world):
    _world_apply(world, 'cloud', 'sediment', 'square')

def logic_14128(world):
    _world_apply(world, 'cloud', 'salinity', 'pulse')

def logic_14129(world):
    _world_apply(world, 'cloud', 'algae', 'gap')

def logic_14130(world):
    _world_apply(world, 'cloud', 'organic_matter', 'direct')

def logic_14131(world):
    _world_apply(world, 'cloud', 'deadwood', 'square')

def logic_14132(world):
    _world_apply(world, 'cloud', 'pollinators', 'pulse')

def logic_14133(world):
    _world_apply(world, 'cloud', 'flowers', 'saturation')

def logic_14134(world):
    _world_apply(world, 'cloud', 'seed_bank', 'gap')

def logic_14135(world):
    _world_apply(world, 'cloud', 'soil_carbon', 'direct')

def logic_14136(world):
    _world_apply(world, 'cloud', 'surface_ice', 'square')

def logic_14137(world):
    _world_apply(world, 'rain', 'temperature', 'saturation')

def logic_14138(world):
    _world_apply(world, 'rain', 'surface_water', 'gap')

def logic_14139(world):
    _world_apply(world, 'rain', 'humidity', 'direct')

def logic_14140(world):
    _world_apply(world, 'rain', 'cloud', 'square')

def logic_14141(world):
    _world_apply(world, 'rain', 'soil_moisture', 'pulse')

def logic_14142(world):
    _world_apply(world, 'rain', 'runoff', 'saturation')

def logic_14143(world):
    _world_apply(world, 'rain', 'wind_x', 'gap')

def logic_14144(world):
    _world_apply(world, 'rain', 'wind_y', 'direct')

def logic_14145(world):
    _world_apply(world, 'rain', 'vegetation', 'pulse')

def logic_14146(world):
    _world_apply(world, 'rain', 'biomass', 'saturation')

def logic_14147(world):
    _world_apply(world, 'rain', 'herbivore', 'gap')

def logic_14148(world):
    _world_apply(world, 'rain', 'predator', 'direct')

def logic_14149(world):
    _world_apply(world, 'rain', 'carrion', 'square')

def logic_14150(world):
    _world_apply(world, 'rain', 'nutrients', 'pulse')

def logic_14151(world):
    _world_apply(world, 'rain', 'decomposition_rate', 'saturation')

def logic_14152(world):
    _world_apply(world, 'rain', 'oxygen', 'gap')

def logic_14153(world):
    _world_apply(world, 'rain', 'co2', 'square')

def logic_14154(world):
    _world_apply(world, 'rain', 'photosynthesis_factor', 'pulse')

def logic_14155(world):
    _world_apply(world, 'rain', 'ice', 'saturation')

def logic_14156(world):
    _world_apply(world, 'rain', 'evaporation', 'gap')

def logic_14157(world):
    _world_apply(world, 'rain', 'detritus', 'direct')

def logic_14158(world):
    _world_apply(world, 'rain', 'methane', 'square')

def logic_14159(world):
    _world_apply(world, 'rain', 'pathogen_load', 'pulse')

def logic_14160(world):
    _world_apply(world, 'rain', 'biodiversity', 'saturation')

def logic_14161(world):
    _world_apply(world, 'rain', 'habitat_stress', 'direct')

def logic_14162(world):
    _world_apply(world, 'rain', 'erosion', 'square')

def logic_14163(world):
    _world_apply(world, 'rain', 'soil_depth', 'pulse')

def logic_14164(world):
    _world_apply(world, 'rain', 'root_density', 'saturation')

def logic_14165(world):
    _world_apply(world, 'rain', 'wetland', 'gap')

def logic_14166(world):
    _world_apply(world, 'rain', 'carbon_storage', 'direct')

def logic_14167(world):
    _world_apply(world, 'rain', 'fire_risk', 'square')

def logic_14168(world):
    _world_apply(world, 'rain', 'ash', 'pulse')

def logic_14169(world):
    _world_apply(world, 'rain', 'snowpack', 'gap')

def logic_14170(world):
    _world_apply(world, 'rain', 'groundwater', 'direct')

def logic_14171(world):
    _world_apply(world, 'rain', 'sediment', 'square')

def logic_14172(world):
    _world_apply(world, 'rain', 'salinity', 'pulse')

def logic_14173(world):
    _world_apply(world, 'rain', 'algae', 'saturation')

def logic_14174(world):
    _world_apply(world, 'rain', 'organic_matter', 'gap')

def logic_14175(world):
    _world_apply(world, 'rain', 'deadwood', 'direct')

def logic_14176(world):
    _world_apply(world, 'rain', 'pollinators', 'square')

def logic_14177(world):
    _world_apply(world, 'rain', 'flowers', 'saturation')

def logic_14178(world):
    _world_apply(world, 'rain', 'seed_bank', 'gap')

def logic_14179(world):
    _world_apply(world, 'rain', 'soil_carbon', 'direct')

def logic_14180(world):
    _world_apply(world, 'rain', 'surface_ice', 'square')

def logic_14181(world):
    _world_apply(world, 'soil_moisture', 'temperature', 'pulse')

def logic_14182(world):
    _world_apply(world, 'soil_moisture', 'surface_water', 'saturation')

def logic_14183(world):
    _world_apply(world, 'soil_moisture', 'humidity', 'gap')

def logic_14184(world):
    _world_apply(world, 'soil_moisture', 'cloud', 'direct')

def logic_14185(world):
    _world_apply(world, 'soil_moisture', 'rain', 'pulse')

def logic_14186(world):
    _world_apply(world, 'soil_moisture', 'runoff', 'saturation')

def logic_14187(world):
    _world_apply(world, 'soil_moisture', 'wind_x', 'gap')

def logic_14188(world):
    _world_apply(world, 'soil_moisture', 'wind_y', 'direct')

def logic_14189(world):
    _world_apply(world, 'soil_moisture', 'vegetation', 'square')

def logic_14190(world):
    _world_apply(world, 'soil_moisture', 'biomass', 'pulse')

def logic_14191(world):
    _world_apply(world, 'soil_moisture', 'herbivore', 'saturation')

def logic_14192(world):
    _world_apply(world, 'soil_moisture', 'predator', 'gap')

def logic_14193(world):
    _world_apply(world, 'soil_moisture', 'carrion', 'square')

def logic_14194(world):
    _world_apply(world, 'soil_moisture', 'nutrients', 'pulse')

def logic_14195(world):
    _world_apply(world, 'soil_moisture', 'decomposition_rate', 'saturation')

def logic_14196(world):
    _world_apply(world, 'soil_moisture', 'oxygen', 'gap')

def logic_14197(world):
    _world_apply(world, 'soil_moisture', 'co2', 'direct')

def logic_14198(world):
    _world_apply(world, 'soil_moisture', 'photosynthesis_factor', 'square')

def logic_14199(world):
    _world_apply(world, 'soil_moisture', 'ice', 'pulse')

def logic_14200(world):
    _world_apply(world, 'soil_moisture', 'evaporation', 'saturation')

def logic_14201(world):
    _world_apply(world, 'soil_moisture', 'detritus', 'direct')

def logic_14202(world):
    _world_apply(world, 'soil_moisture', 'methane', 'square')

def logic_14203(world):
    _world_apply(world, 'soil_moisture', 'pathogen_load', 'pulse')

def logic_14204(world):
    _world_apply(world, 'soil_moisture', 'biodiversity', 'saturation')

def logic_14205(world):
    _world_apply(world, 'soil_moisture', 'habitat_stress', 'gap')

def logic_14206(world):
    _world_apply(world, 'soil_moisture', 'erosion', 'direct')

def logic_14207(world):
    _world_apply(world, 'soil_moisture', 'soil_depth', 'square')

def logic_14208(world):
    _world_apply(world, 'soil_moisture', 'root_density', 'pulse')

def logic_14209(world):
    _world_apply(world, 'soil_moisture', 'wetland', 'gap')

def logic_14210(world):
    _world_apply(world, 'soil_moisture', 'carbon_storage', 'direct')

def logic_14211(world):
    _world_apply(world, 'soil_moisture', 'fire_risk', 'square')

def logic_14212(world):
    _world_apply(world, 'soil_moisture', 'ash', 'pulse')

def logic_14213(world):
    _world_apply(world, 'soil_moisture', 'snowpack', 'saturation')

def logic_14214(world):
    _world_apply(world, 'soil_moisture', 'groundwater', 'gap')

def logic_14215(world):
    _world_apply(world, 'soil_moisture', 'sediment', 'direct')

def logic_14216(world):
    _world_apply(world, 'soil_moisture', 'salinity', 'square')

def logic_14217(world):
    _world_apply(world, 'soil_moisture', 'algae', 'saturation')

def logic_14218(world):
    _world_apply(world, 'soil_moisture', 'organic_matter', 'gap')

def logic_14219(world):
    _world_apply(world, 'soil_moisture', 'deadwood', 'direct')

def logic_14220(world):
    _world_apply(world, 'soil_moisture', 'pollinators', 'square')

def logic_14221(world):
    _world_apply(world, 'soil_moisture', 'flowers', 'pulse')

def logic_14222(world):
    _world_apply(world, 'soil_moisture', 'seed_bank', 'saturation')

def logic_14223(world):
    _world_apply(world, 'soil_moisture', 'soil_carbon', 'gap')

def logic_14224(world):
    _world_apply(world, 'soil_moisture', 'surface_ice', 'direct')

def logic_14225(world):
    _world_apply(world, 'runoff', 'temperature', 'pulse')

def logic_14226(world):
    _world_apply(world, 'runoff', 'surface_water', 'saturation')

def logic_14227(world):
    _world_apply(world, 'runoff', 'humidity', 'gap')

def logic_14228(world):
    _world_apply(world, 'runoff', 'cloud', 'direct')

def logic_14229(world):
    _world_apply(world, 'runoff', 'rain', 'square')

def logic_14230(world):
    _world_apply(world, 'runoff', 'soil_moisture', 'pulse')

def logic_14231(world):
    _world_apply(world, 'runoff', 'wind_x', 'saturation')

def logic_14232(world):
    _world_apply(world, 'runoff', 'wind_y', 'gap')

def logic_14233(world):
    _world_apply(world, 'runoff', 'vegetation', 'square')

def logic_14234(world):
    _world_apply(world, 'runoff', 'biomass', 'pulse')

def logic_14235(world):
    _world_apply(world, 'runoff', 'herbivore', 'saturation')

def logic_14236(world):
    _world_apply(world, 'runoff', 'predator', 'gap')

def logic_14237(world):
    _world_apply(world, 'runoff', 'carrion', 'direct')

def logic_14238(world):
    _world_apply(world, 'runoff', 'nutrients', 'square')

def logic_14239(world):
    _world_apply(world, 'runoff', 'decomposition_rate', 'pulse')

def logic_14240(world):
    _world_apply(world, 'runoff', 'oxygen', 'saturation')

def logic_14241(world):
    _world_apply(world, 'runoff', 'co2', 'direct')

def logic_14242(world):
    _world_apply(world, 'runoff', 'photosynthesis_factor', 'square')

def logic_14243(world):
    _world_apply(world, 'runoff', 'ice', 'pulse')

def logic_14244(world):
    _world_apply(world, 'runoff', 'evaporation', 'saturation')

def logic_14245(world):
    _world_apply(world, 'runoff', 'detritus', 'gap')

def logic_14246(world):
    _world_apply(world, 'runoff', 'methane', 'direct')

def logic_14247(world):
    _world_apply(world, 'runoff', 'pathogen_load', 'square')

def logic_14248(world):
    _world_apply(world, 'runoff', 'biodiversity', 'pulse')

def logic_14249(world):
    _world_apply(world, 'runoff', 'habitat_stress', 'gap')

def logic_14250(world):
    _world_apply(world, 'runoff', 'erosion', 'direct')

def logic_14251(world):
    _world_apply(world, 'runoff', 'soil_depth', 'square')

def logic_14252(world):
    _world_apply(world, 'runoff', 'root_density', 'pulse')

def logic_14253(world):
    _world_apply(world, 'runoff', 'wetland', 'saturation')

def logic_14254(world):
    _world_apply(world, 'runoff', 'carbon_storage', 'gap')

def logic_14255(world):
    _world_apply(world, 'runoff', 'fire_risk', 'direct')

def logic_14256(world):
    _world_apply(world, 'runoff', 'ash', 'square')

def logic_14257(world):
    _world_apply(world, 'runoff', 'snowpack', 'saturation')

def logic_14258(world):
    _world_apply(world, 'runoff', 'groundwater', 'gap')

def logic_14259(world):
    _world_apply(world, 'runoff', 'sediment', 'direct')

def logic_14260(world):
    _world_apply(world, 'runoff', 'salinity', 'square')

def logic_14261(world):
    _world_apply(world, 'runoff', 'algae', 'pulse')

def logic_14262(world):
    _world_apply(world, 'runoff', 'organic_matter', 'saturation')

def logic_14263(world):
    _world_apply(world, 'runoff', 'deadwood', 'gap')

def logic_14264(world):
    _world_apply(world, 'runoff', 'pollinators', 'direct')

def logic_14265(world):
    _world_apply(world, 'runoff', 'flowers', 'pulse')

def logic_14266(world):
    _world_apply(world, 'runoff', 'seed_bank', 'saturation')

def logic_14267(world):
    _world_apply(world, 'runoff', 'soil_carbon', 'gap')

def logic_14268(world):
    _world_apply(world, 'runoff', 'surface_ice', 'direct')

def logic_14269(world):
    _world_apply(world, 'wind_x', 'temperature', 'square')

def logic_14270(world):
    _world_apply(world, 'wind_x', 'surface_water', 'pulse')

def logic_14271(world):
    _world_apply(world, 'wind_x', 'humidity', 'saturation')

def logic_14272(world):
    _world_apply(world, 'wind_x', 'cloud', 'gap')

def logic_14273(world):
    _world_apply(world, 'wind_x', 'rain', 'square')

def logic_14274(world):
    _world_apply(world, 'wind_x', 'soil_moisture', 'pulse')

def logic_14275(world):
    _world_apply(world, 'wind_x', 'runoff', 'saturation')

def logic_14276(world):
    _world_apply(world, 'wind_x', 'wind_y', 'gap')

def logic_14277(world):
    _world_apply(world, 'wind_x', 'vegetation', 'direct')

def logic_14278(world):
    _world_apply(world, 'wind_x', 'biomass', 'square')

def logic_14279(world):
    _world_apply(world, 'wind_x', 'herbivore', 'pulse')

def logic_14280(world):
    _world_apply(world, 'wind_x', 'predator', 'saturation')

def logic_14281(world):
    _world_apply(world, 'wind_x', 'carrion', 'direct')

def logic_14282(world):
    _world_apply(world, 'wind_x', 'nutrients', 'square')

def logic_14283(world):
    _world_apply(world, 'wind_x', 'decomposition_rate', 'pulse')

def logic_14284(world):
    _world_apply(world, 'wind_x', 'oxygen', 'saturation')

def logic_14285(world):
    _world_apply(world, 'wind_x', 'co2', 'gap')

def logic_14286(world):
    _world_apply(world, 'wind_x', 'photosynthesis_factor', 'direct')

def logic_14287(world):
    _world_apply(world, 'wind_x', 'ice', 'square')

def logic_14288(world):
    _world_apply(world, 'wind_x', 'evaporation', 'pulse')

def logic_14289(world):
    _world_apply(world, 'wind_x', 'detritus', 'gap')

def logic_14290(world):
    _world_apply(world, 'wind_x', 'methane', 'direct')

def logic_14291(world):
    _world_apply(world, 'wind_x', 'pathogen_load', 'square')

def logic_14292(world):
    _world_apply(world, 'wind_x', 'biodiversity', 'pulse')

def logic_14293(world):
    _world_apply(world, 'wind_x', 'habitat_stress', 'saturation')

def logic_14294(world):
    _world_apply(world, 'wind_x', 'erosion', 'gap')

def logic_14295(world):
    _world_apply(world, 'wind_x', 'soil_depth', 'direct')

def logic_14296(world):
    _world_apply(world, 'wind_x', 'root_density', 'square')

def logic_14297(world):
    _world_apply(world, 'wind_x', 'wetland', 'saturation')

def logic_14298(world):
    _world_apply(world, 'wind_x', 'carbon_storage', 'gap')

def logic_14299(world):
    _world_apply(world, 'wind_x', 'fire_risk', 'direct')

def logic_14300(world):
    _world_apply(world, 'wind_x', 'ash', 'square')

def logic_14301(world):
    _world_apply(world, 'wind_x', 'snowpack', 'pulse')

def logic_14302(world):
    _world_apply(world, 'wind_x', 'groundwater', 'saturation')

def logic_14303(world):
    _world_apply(world, 'wind_x', 'sediment', 'gap')

def logic_14304(world):
    _world_apply(world, 'wind_x', 'salinity', 'direct')

def logic_14305(world):
    _world_apply(world, 'wind_x', 'algae', 'pulse')

def logic_14306(world):
    _world_apply(world, 'wind_x', 'organic_matter', 'saturation')

def logic_14307(world):
    _world_apply(world, 'wind_x', 'deadwood', 'gap')

def logic_14308(world):
    _world_apply(world, 'wind_x', 'pollinators', 'direct')

def logic_14309(world):
    _world_apply(world, 'wind_x', 'flowers', 'square')

def logic_14310(world):
    _world_apply(world, 'wind_x', 'seed_bank', 'pulse')

def logic_14311(world):
    _world_apply(world, 'wind_x', 'soil_carbon', 'saturation')

def logic_14312(world):
    _world_apply(world, 'wind_x', 'surface_ice', 'gap')

def logic_14313(world):
    _world_apply(world, 'wind_y', 'temperature', 'square')

def logic_14314(world):
    _world_apply(world, 'wind_y', 'surface_water', 'pulse')

def logic_14315(world):
    _world_apply(world, 'wind_y', 'humidity', 'saturation')

def logic_14316(world):
    _world_apply(world, 'wind_y', 'cloud', 'gap')

def logic_14317(world):
    _world_apply(world, 'wind_y', 'rain', 'direct')

def logic_14318(world):
    _world_apply(world, 'wind_y', 'soil_moisture', 'square')

def logic_14319(world):
    _world_apply(world, 'wind_y', 'runoff', 'pulse')

def logic_14320(world):
    _world_apply(world, 'wind_y', 'wind_x', 'saturation')

def logic_14321(world):
    _world_apply(world, 'wind_y', 'vegetation', 'direct')

def logic_14322(world):
    _world_apply(world, 'wind_y', 'biomass', 'square')

def logic_14323(world):
    _world_apply(world, 'wind_y', 'herbivore', 'pulse')

def logic_14324(world):
    _world_apply(world, 'wind_y', 'predator', 'saturation')

def logic_14325(world):
    _world_apply(world, 'wind_y', 'carrion', 'gap')

def logic_14326(world):
    _world_apply(world, 'wind_y', 'nutrients', 'direct')

def logic_14327(world):
    _world_apply(world, 'wind_y', 'decomposition_rate', 'square')

def logic_14328(world):
    _world_apply(world, 'wind_y', 'oxygen', 'pulse')

def logic_14329(world):
    _world_apply(world, 'wind_y', 'co2', 'gap')

def logic_14330(world):
    _world_apply(world, 'wind_y', 'photosynthesis_factor', 'direct')

def logic_14331(world):
    _world_apply(world, 'wind_y', 'ice', 'square')

def logic_14332(world):
    _world_apply(world, 'wind_y', 'evaporation', 'pulse')

def logic_14333(world):
    _world_apply(world, 'wind_y', 'detritus', 'saturation')

def logic_14334(world):
    _world_apply(world, 'wind_y', 'methane', 'gap')

def logic_14335(world):
    _world_apply(world, 'wind_y', 'pathogen_load', 'direct')

def logic_14336(world):
    _world_apply(world, 'wind_y', 'biodiversity', 'square')

def logic_14337(world):
    _world_apply(world, 'wind_y', 'habitat_stress', 'saturation')

def logic_14338(world):
    _world_apply(world, 'wind_y', 'erosion', 'gap')

def logic_14339(world):
    _world_apply(world, 'wind_y', 'soil_depth', 'direct')

def logic_14340(world):
    _world_apply(world, 'wind_y', 'root_density', 'square')

def logic_14341(world):
    _world_apply(world, 'wind_y', 'wetland', 'pulse')

def logic_14342(world):
    _world_apply(world, 'wind_y', 'carbon_storage', 'saturation')

def logic_14343(world):
    _world_apply(world, 'wind_y', 'fire_risk', 'gap')

def logic_14344(world):
    _world_apply(world, 'wind_y', 'ash', 'direct')

def logic_14345(world):
    _world_apply(world, 'wind_y', 'snowpack', 'pulse')

def logic_14346(world):
    _world_apply(world, 'wind_y', 'groundwater', 'saturation')

def logic_14347(world):
    _world_apply(world, 'wind_y', 'sediment', 'gap')

def logic_14348(world):
    _world_apply(world, 'wind_y', 'salinity', 'direct')

def logic_14349(world):
    _world_apply(world, 'wind_y', 'algae', 'square')

def logic_14350(world):
    _world_apply(world, 'wind_y', 'organic_matter', 'pulse')

def logic_14351(world):
    _world_apply(world, 'wind_y', 'deadwood', 'saturation')

def logic_14352(world):
    _world_apply(world, 'wind_y', 'pollinators', 'gap')

def logic_14353(world):
    _world_apply(world, 'wind_y', 'flowers', 'square')

def logic_14354(world):
    _world_apply(world, 'wind_y', 'seed_bank', 'pulse')

def logic_14355(world):
    _world_apply(world, 'wind_y', 'soil_carbon', 'saturation')

def logic_14356(world):
    _world_apply(world, 'wind_y', 'surface_ice', 'gap')

def logic_14357(world):
    _world_apply(world, 'vegetation', 'temperature', 'direct')

def logic_14358(world):
    _world_apply(world, 'vegetation', 'surface_water', 'square')

def logic_14359(world):
    _world_apply(world, 'vegetation', 'humidity', 'pulse')

def logic_14360(world):
    _world_apply(world, 'vegetation', 'cloud', 'saturation')

def logic_14361(world):
    _world_apply(world, 'vegetation', 'rain', 'direct')

def logic_14362(world):
    _world_apply(world, 'vegetation', 'soil_moisture', 'square')

def logic_14363(world):
    _world_apply(world, 'vegetation', 'runoff', 'pulse')

def logic_14364(world):
    _world_apply(world, 'vegetation', 'wind_x', 'saturation')

def logic_14365(world):
    _world_apply(world, 'vegetation', 'wind_y', 'gap')

def logic_14366(world):
    _world_apply(world, 'vegetation', 'biomass', 'direct')

def logic_14367(world):
    _world_apply(world, 'vegetation', 'herbivore', 'square')

def logic_14368(world):
    _world_apply(world, 'vegetation', 'predator', 'pulse')

def logic_14369(world):
    _world_apply(world, 'vegetation', 'carrion', 'gap')

def logic_14370(world):
    _world_apply(world, 'vegetation', 'nutrients', 'direct')

def logic_14371(world):
    _world_apply(world, 'vegetation', 'decomposition_rate', 'square')

def logic_14372(world):
    _world_apply(world, 'vegetation', 'oxygen', 'pulse')

def logic_14373(world):
    _world_apply(world, 'vegetation', 'co2', 'saturation')

def logic_14374(world):
    _world_apply(world, 'vegetation', 'photosynthesis_factor', 'gap')

def logic_14375(world):
    _world_apply(world, 'vegetation', 'ice', 'direct')

def logic_14376(world):
    _world_apply(world, 'vegetation', 'evaporation', 'square')

def logic_14377(world):
    _world_apply(world, 'vegetation', 'detritus', 'saturation')

def logic_14378(world):
    _world_apply(world, 'vegetation', 'methane', 'gap')

def logic_14379(world):
    _world_apply(world, 'vegetation', 'pathogen_load', 'direct')

def logic_14380(world):
    _world_apply(world, 'vegetation', 'biodiversity', 'square')

def logic_14381(world):
    _world_apply(world, 'vegetation', 'habitat_stress', 'pulse')

def logic_14382(world):
    _world_apply(world, 'vegetation', 'erosion', 'saturation')

def logic_14383(world):
    _world_apply(world, 'vegetation', 'soil_depth', 'gap')

def logic_14384(world):
    _world_apply(world, 'vegetation', 'root_density', 'direct')

def logic_14385(world):
    _world_apply(world, 'vegetation', 'wetland', 'pulse')

def logic_14386(world):
    _world_apply(world, 'vegetation', 'carbon_storage', 'saturation')

def logic_14387(world):
    _world_apply(world, 'vegetation', 'fire_risk', 'gap')

def logic_14388(world):
    _world_apply(world, 'vegetation', 'ash', 'direct')

def logic_14389(world):
    _world_apply(world, 'vegetation', 'snowpack', 'square')

def logic_14390(world):
    _world_apply(world, 'vegetation', 'groundwater', 'pulse')

def logic_14391(world):
    _world_apply(world, 'vegetation', 'sediment', 'saturation')

def logic_14392(world):
    _world_apply(world, 'vegetation', 'salinity', 'gap')

def logic_14393(world):
    _world_apply(world, 'vegetation', 'algae', 'square')

def logic_14394(world):
    _world_apply(world, 'vegetation', 'organic_matter', 'pulse')

def logic_14395(world):
    _world_apply(world, 'vegetation', 'deadwood', 'saturation')

def logic_14396(world):
    _world_apply(world, 'vegetation', 'pollinators', 'gap')

def logic_14397(world):
    _world_apply(world, 'vegetation', 'flowers', 'direct')

def logic_14398(world):
    _world_apply(world, 'vegetation', 'seed_bank', 'square')

def logic_14399(world):
    _world_apply(world, 'vegetation', 'soil_carbon', 'pulse')

def logic_14400(world):
    _world_apply(world, 'vegetation', 'surface_ice', 'saturation')

def logic_14401(world):
    _world_apply(world, 'biomass', 'temperature', 'direct')

def logic_14402(world):
    _world_apply(world, 'biomass', 'surface_water', 'square')

def logic_14403(world):
    _world_apply(world, 'biomass', 'humidity', 'pulse')

def logic_14404(world):
    _world_apply(world, 'biomass', 'cloud', 'saturation')

def logic_14405(world):
    _world_apply(world, 'biomass', 'rain', 'gap')

def logic_14406(world):
    _world_apply(world, 'biomass', 'soil_moisture', 'direct')

def logic_14407(world):
    _world_apply(world, 'biomass', 'runoff', 'square')

def logic_14408(world):
    _world_apply(world, 'biomass', 'wind_x', 'pulse')

def logic_14409(world):
    _world_apply(world, 'biomass', 'wind_y', 'gap')

def logic_14410(world):
    _world_apply(world, 'biomass', 'vegetation', 'direct')

def logic_14411(world):
    _world_apply(world, 'biomass', 'herbivore', 'square')

def logic_14412(world):
    _world_apply(world, 'biomass', 'predator', 'pulse')

def logic_14413(world):
    _world_apply(world, 'biomass', 'carrion', 'saturation')

def logic_14414(world):
    _world_apply(world, 'biomass', 'nutrients', 'gap')

def logic_14415(world):
    _world_apply(world, 'biomass', 'decomposition_rate', 'direct')

def logic_14416(world):
    _world_apply(world, 'biomass', 'oxygen', 'square')

def logic_14417(world):
    _world_apply(world, 'biomass', 'co2', 'saturation')

def logic_14418(world):
    _world_apply(world, 'biomass', 'photosynthesis_factor', 'gap')

def logic_14419(world):
    _world_apply(world, 'biomass', 'ice', 'direct')

def logic_14420(world):
    _world_apply(world, 'biomass', 'evaporation', 'square')

def logic_14421(world):
    _world_apply(world, 'biomass', 'detritus', 'pulse')

def logic_14422(world):
    _world_apply(world, 'biomass', 'methane', 'saturation')

def logic_14423(world):
    _world_apply(world, 'biomass', 'pathogen_load', 'gap')

def logic_14424(world):
    _world_apply(world, 'biomass', 'biodiversity', 'direct')

def logic_14425(world):
    _world_apply(world, 'biomass', 'habitat_stress', 'pulse')

def logic_14426(world):
    _world_apply(world, 'biomass', 'erosion', 'saturation')

def logic_14427(world):
    _world_apply(world, 'biomass', 'soil_depth', 'gap')

def logic_14428(world):
    _world_apply(world, 'biomass', 'root_density', 'direct')

def logic_14429(world):
    _world_apply(world, 'biomass', 'wetland', 'square')

def logic_14430(world):
    _world_apply(world, 'biomass', 'carbon_storage', 'pulse')

def logic_14431(world):
    _world_apply(world, 'biomass', 'fire_risk', 'saturation')

def logic_14432(world):
    _world_apply(world, 'biomass', 'ash', 'gap')

def logic_14433(world):
    _world_apply(world, 'biomass', 'snowpack', 'square')

def logic_14434(world):
    _world_apply(world, 'biomass', 'groundwater', 'pulse')

def logic_14435(world):
    _world_apply(world, 'biomass', 'sediment', 'saturation')

def logic_14436(world):
    _world_apply(world, 'biomass', 'salinity', 'gap')

def logic_14437(world):
    _world_apply(world, 'biomass', 'algae', 'direct')

def logic_14438(world):
    _world_apply(world, 'biomass', 'organic_matter', 'square')

def logic_14439(world):
    _world_apply(world, 'biomass', 'deadwood', 'pulse')

def logic_14440(world):
    _world_apply(world, 'biomass', 'pollinators', 'saturation')

def logic_14441(world):
    _world_apply(world, 'biomass', 'flowers', 'direct')

def logic_14442(world):
    _world_apply(world, 'biomass', 'seed_bank', 'square')

def logic_14443(world):
    _world_apply(world, 'biomass', 'soil_carbon', 'pulse')

def logic_14444(world):
    _world_apply(world, 'biomass', 'surface_ice', 'saturation')

def logic_14445(world):
    _world_apply(world, 'herbivore', 'temperature', 'gap')

def logic_14446(world):
    _world_apply(world, 'herbivore', 'surface_water', 'direct')

def logic_14447(world):
    _world_apply(world, 'herbivore', 'humidity', 'square')

def logic_14448(world):
    _world_apply(world, 'herbivore', 'cloud', 'pulse')

def logic_14449(world):
    _world_apply(world, 'herbivore', 'rain', 'gap')

def logic_14450(world):
    _world_apply(world, 'herbivore', 'soil_moisture', 'direct')

def logic_14451(world):
    _world_apply(world, 'herbivore', 'runoff', 'square')

def logic_14452(world):
    _world_apply(world, 'herbivore', 'wind_x', 'pulse')

def logic_14453(world):
    _world_apply(world, 'herbivore', 'wind_y', 'saturation')

def logic_14454(world):
    _world_apply(world, 'herbivore', 'vegetation', 'gap')

def logic_14455(world):
    _world_apply(world, 'herbivore', 'biomass', 'direct')

def logic_14456(world):
    _world_apply(world, 'herbivore', 'predator', 'square')

def logic_14457(world):
    _world_apply(world, 'herbivore', 'carrion', 'saturation')

def logic_14458(world):
    _world_apply(world, 'herbivore', 'nutrients', 'gap')

def logic_14459(world):
    _world_apply(world, 'herbivore', 'decomposition_rate', 'direct')

def logic_14460(world):
    _world_apply(world, 'herbivore', 'oxygen', 'square')

def logic_14461(world):
    _world_apply(world, 'herbivore', 'co2', 'pulse')

def logic_14462(world):
    _world_apply(world, 'herbivore', 'photosynthesis_factor', 'saturation')

def logic_14463(world):
    _world_apply(world, 'herbivore', 'ice', 'gap')

def logic_14464(world):
    _world_apply(world, 'herbivore', 'evaporation', 'direct')

def logic_14465(world):
    _world_apply(world, 'herbivore', 'detritus', 'pulse')

def logic_14466(world):
    _world_apply(world, 'herbivore', 'methane', 'saturation')

def logic_14467(world):
    _world_apply(world, 'herbivore', 'pathogen_load', 'gap')

def logic_14468(world):
    _world_apply(world, 'herbivore', 'biodiversity', 'direct')

def logic_14469(world):
    _world_apply(world, 'herbivore', 'habitat_stress', 'square')

def logic_14470(world):
    _world_apply(world, 'herbivore', 'erosion', 'pulse')

def logic_14471(world):
    _world_apply(world, 'herbivore', 'soil_depth', 'saturation')

def logic_14472(world):
    _world_apply(world, 'herbivore', 'root_density', 'gap')

def logic_14473(world):
    _world_apply(world, 'herbivore', 'wetland', 'square')

def logic_14474(world):
    _world_apply(world, 'herbivore', 'carbon_storage', 'pulse')

def logic_14475(world):
    _world_apply(world, 'herbivore', 'fire_risk', 'saturation')

def logic_14476(world):
    _world_apply(world, 'herbivore', 'ash', 'gap')

def logic_14477(world):
    _world_apply(world, 'herbivore', 'snowpack', 'direct')

def logic_14478(world):
    _world_apply(world, 'herbivore', 'groundwater', 'square')

def logic_14479(world):
    _world_apply(world, 'herbivore', 'sediment', 'pulse')

def logic_14480(world):
    _world_apply(world, 'herbivore', 'salinity', 'saturation')

def logic_14481(world):
    _world_apply(world, 'herbivore', 'algae', 'direct')

def logic_14482(world):
    _world_apply(world, 'herbivore', 'organic_matter', 'square')

def logic_14483(world):
    _world_apply(world, 'herbivore', 'deadwood', 'pulse')

def logic_14484(world):
    _world_apply(world, 'herbivore', 'pollinators', 'saturation')

def logic_14485(world):
    _world_apply(world, 'herbivore', 'flowers', 'gap')

def logic_14486(world):
    _world_apply(world, 'herbivore', 'seed_bank', 'direct')

def logic_14487(world):
    _world_apply(world, 'herbivore', 'soil_carbon', 'square')

def logic_14488(world):
    _world_apply(world, 'herbivore', 'surface_ice', 'pulse')

def logic_14489(world):
    _world_apply(world, 'predator', 'temperature', 'gap')

def logic_14490(world):
    _world_apply(world, 'predator', 'surface_water', 'direct')

def logic_14491(world):
    _world_apply(world, 'predator', 'humidity', 'square')

def logic_14492(world):
    _world_apply(world, 'predator', 'cloud', 'pulse')

def logic_14493(world):
    _world_apply(world, 'predator', 'rain', 'saturation')

def logic_14494(world):
    _world_apply(world, 'predator', 'soil_moisture', 'gap')

def logic_14495(world):
    _world_apply(world, 'predator', 'runoff', 'direct')

def logic_14496(world):
    _world_apply(world, 'predator', 'wind_x', 'square')

def logic_14497(world):
    _world_apply(world, 'predator', 'wind_y', 'saturation')

def logic_14498(world):
    _world_apply(world, 'predator', 'vegetation', 'gap')

def logic_14499(world):
    _world_apply(world, 'predator', 'biomass', 'direct')

def logic_14500(world):
    _world_apply(world, 'predator', 'herbivore', 'square')

def logic_14501(world):
    _world_apply(world, 'predator', 'carrion', 'pulse')

def logic_14502(world):
    _world_apply(world, 'predator', 'nutrients', 'saturation')

def logic_14503(world):
    _world_apply(world, 'predator', 'decomposition_rate', 'gap')

def logic_14504(world):
    _world_apply(world, 'predator', 'oxygen', 'direct')

def logic_14505(world):
    _world_apply(world, 'predator', 'co2', 'pulse')

def logic_14506(world):
    _world_apply(world, 'predator', 'photosynthesis_factor', 'saturation')

def logic_14507(world):
    _world_apply(world, 'predator', 'ice', 'gap')

def logic_14508(world):
    _world_apply(world, 'predator', 'evaporation', 'direct')

def logic_14509(world):
    _world_apply(world, 'predator', 'detritus', 'square')

def logic_14510(world):
    _world_apply(world, 'predator', 'methane', 'pulse')

def logic_14511(world):
    _world_apply(world, 'predator', 'pathogen_load', 'saturation')

def logic_14512(world):
    _world_apply(world, 'predator', 'biodiversity', 'gap')

def logic_14513(world):
    _world_apply(world, 'predator', 'habitat_stress', 'square')

def logic_14514(world):
    _world_apply(world, 'predator', 'erosion', 'pulse')

def logic_14515(world):
    _world_apply(world, 'predator', 'soil_depth', 'saturation')

def logic_14516(world):
    _world_apply(world, 'predator', 'root_density', 'gap')

def logic_14517(world):
    _world_apply(world, 'predator', 'wetland', 'direct')

def logic_14518(world):
    _world_apply(world, 'predator', 'carbon_storage', 'square')

def logic_14519(world):
    _world_apply(world, 'predator', 'fire_risk', 'pulse')

def logic_14520(world):
    _world_apply(world, 'predator', 'ash', 'saturation')

def logic_14521(world):
    _world_apply(world, 'predator', 'snowpack', 'direct')

def logic_14522(world):
    _world_apply(world, 'predator', 'groundwater', 'square')

def logic_14523(world):
    _world_apply(world, 'predator', 'sediment', 'pulse')

def logic_14524(world):
    _world_apply(world, 'predator', 'salinity', 'saturation')

def logic_14525(world):
    _world_apply(world, 'predator', 'algae', 'gap')

def logic_14526(world):
    _world_apply(world, 'predator', 'organic_matter', 'direct')

def logic_14527(world):
    _world_apply(world, 'predator', 'deadwood', 'square')

def logic_14528(world):
    _world_apply(world, 'predator', 'pollinators', 'pulse')

def logic_14529(world):
    _world_apply(world, 'predator', 'flowers', 'gap')

def logic_14530(world):
    _world_apply(world, 'predator', 'seed_bank', 'direct')

def logic_14531(world):
    _world_apply(world, 'predator', 'soil_carbon', 'square')

def logic_14532(world):
    _world_apply(world, 'predator', 'surface_ice', 'pulse')

def logic_14533(world):
    _world_apply(world, 'carrion', 'temperature', 'saturation')

def logic_14534(world):
    _world_apply(world, 'carrion', 'surface_water', 'gap')

def logic_14535(world):
    _world_apply(world, 'carrion', 'humidity', 'direct')

def logic_14536(world):
    _world_apply(world, 'carrion', 'cloud', 'square')

def logic_14537(world):
    _world_apply(world, 'carrion', 'rain', 'saturation')

def logic_14538(world):
    _world_apply(world, 'carrion', 'soil_moisture', 'gap')

def logic_14539(world):
    _world_apply(world, 'carrion', 'runoff', 'direct')

def logic_14540(world):
    _world_apply(world, 'carrion', 'wind_x', 'square')

def logic_14541(world):
    _world_apply(world, 'carrion', 'wind_y', 'pulse')

def logic_14542(world):
    _world_apply(world, 'carrion', 'vegetation', 'saturation')

def logic_14543(world):
    _world_apply(world, 'carrion', 'biomass', 'gap')

def logic_14544(world):
    _world_apply(world, 'carrion', 'herbivore', 'direct')

def logic_14545(world):
    _world_apply(world, 'carrion', 'predator', 'pulse')

def logic_14546(world):
    _world_apply(world, 'carrion', 'nutrients', 'saturation')

def logic_14547(world):
    _world_apply(world, 'carrion', 'decomposition_rate', 'gap')

def logic_14548(world):
    _world_apply(world, 'carrion', 'oxygen', 'direct')

def logic_14549(world):
    _world_apply(world, 'carrion', 'co2', 'square')

def logic_14550(world):
    _world_apply(world, 'carrion', 'photosynthesis_factor', 'pulse')

def logic_14551(world):
    _world_apply(world, 'carrion', 'ice', 'saturation')

def logic_14552(world):
    _world_apply(world, 'carrion', 'evaporation', 'gap')

def logic_14553(world):
    _world_apply(world, 'carrion', 'detritus', 'square')

def logic_14554(world):
    _world_apply(world, 'carrion', 'methane', 'pulse')

def logic_14555(world):
    _world_apply(world, 'carrion', 'pathogen_load', 'saturation')

def logic_14556(world):
    _world_apply(world, 'carrion', 'biodiversity', 'gap')

def logic_14557(world):
    _world_apply(world, 'carrion', 'habitat_stress', 'direct')

def logic_14558(world):
    _world_apply(world, 'carrion', 'erosion', 'square')

def logic_14559(world):
    _world_apply(world, 'carrion', 'soil_depth', 'pulse')

def logic_14560(world):
    _world_apply(world, 'carrion', 'root_density', 'saturation')

def logic_14561(world):
    _world_apply(world, 'carrion', 'wetland', 'direct')

def logic_14562(world):
    _world_apply(world, 'carrion', 'carbon_storage', 'square')

def logic_14563(world):
    _world_apply(world, 'carrion', 'fire_risk', 'pulse')

def logic_14564(world):
    _world_apply(world, 'carrion', 'ash', 'saturation')

def logic_14565(world):
    _world_apply(world, 'carrion', 'snowpack', 'gap')

def logic_14566(world):
    _world_apply(world, 'carrion', 'groundwater', 'direct')

def logic_14567(world):
    _world_apply(world, 'carrion', 'sediment', 'square')

def logic_14568(world):
    _world_apply(world, 'carrion', 'salinity', 'pulse')

def logic_14569(world):
    _world_apply(world, 'carrion', 'algae', 'gap')

def logic_14570(world):
    _world_apply(world, 'carrion', 'organic_matter', 'direct')

def logic_14571(world):
    _world_apply(world, 'carrion', 'deadwood', 'square')

def logic_14572(world):
    _world_apply(world, 'carrion', 'pollinators', 'pulse')

def logic_14573(world):
    _world_apply(world, 'carrion', 'flowers', 'saturation')

def logic_14574(world):
    _world_apply(world, 'carrion', 'seed_bank', 'gap')

def logic_14575(world):
    _world_apply(world, 'carrion', 'soil_carbon', 'direct')

def logic_14576(world):
    _world_apply(world, 'carrion', 'surface_ice', 'square')

def logic_14577(world):
    _world_apply(world, 'nutrients', 'temperature', 'saturation')

def logic_14578(world):
    _world_apply(world, 'nutrients', 'surface_water', 'gap')

def logic_14579(world):
    _world_apply(world, 'nutrients', 'humidity', 'direct')

def logic_14580(world):
    _world_apply(world, 'nutrients', 'cloud', 'square')

def logic_14581(world):
    _world_apply(world, 'nutrients', 'rain', 'pulse')

def logic_14582(world):
    _world_apply(world, 'nutrients', 'soil_moisture', 'saturation')

def logic_14583(world):
    _world_apply(world, 'nutrients', 'runoff', 'gap')

def logic_14584(world):
    _world_apply(world, 'nutrients', 'wind_x', 'direct')

def logic_14585(world):
    _world_apply(world, 'nutrients', 'wind_y', 'pulse')

def logic_14586(world):
    _world_apply(world, 'nutrients', 'vegetation', 'saturation')

def logic_14587(world):
    _world_apply(world, 'nutrients', 'biomass', 'gap')

def logic_14588(world):
    _world_apply(world, 'nutrients', 'herbivore', 'direct')

def logic_14589(world):
    _world_apply(world, 'nutrients', 'predator', 'square')

def logic_14590(world):
    _world_apply(world, 'nutrients', 'carrion', 'pulse')

def logic_14591(world):
    _world_apply(world, 'nutrients', 'decomposition_rate', 'saturation')

def logic_14592(world):
    _world_apply(world, 'nutrients', 'oxygen', 'gap')

def logic_14593(world):
    _world_apply(world, 'nutrients', 'co2', 'square')

def logic_14594(world):
    _world_apply(world, 'nutrients', 'photosynthesis_factor', 'pulse')

def logic_14595(world):
    _world_apply(world, 'nutrients', 'ice', 'saturation')

def logic_14596(world):
    _world_apply(world, 'nutrients', 'evaporation', 'gap')

def logic_14597(world):
    _world_apply(world, 'nutrients', 'detritus', 'direct')

def logic_14598(world):
    _world_apply(world, 'nutrients', 'methane', 'square')

def logic_14599(world):
    _world_apply(world, 'nutrients', 'pathogen_load', 'pulse')

def logic_14600(world):
    _world_apply(world, 'nutrients', 'biodiversity', 'saturation')

def logic_14601(world):
    _world_apply(world, 'nutrients', 'habitat_stress', 'direct')

def logic_14602(world):
    _world_apply(world, 'nutrients', 'erosion', 'square')

def logic_14603(world):
    _world_apply(world, 'nutrients', 'soil_depth', 'pulse')

def logic_14604(world):
    _world_apply(world, 'nutrients', 'root_density', 'saturation')

def logic_14605(world):
    _world_apply(world, 'nutrients', 'wetland', 'gap')

def logic_14606(world):
    _world_apply(world, 'nutrients', 'carbon_storage', 'direct')

def logic_14607(world):
    _world_apply(world, 'nutrients', 'fire_risk', 'square')

def logic_14608(world):
    _world_apply(world, 'nutrients', 'ash', 'pulse')

def logic_14609(world):
    _world_apply(world, 'nutrients', 'snowpack', 'gap')

def logic_14610(world):
    _world_apply(world, 'nutrients', 'groundwater', 'direct')

def logic_14611(world):
    _world_apply(world, 'nutrients', 'sediment', 'square')

def logic_14612(world):
    _world_apply(world, 'nutrients', 'salinity', 'pulse')

def logic_14613(world):
    _world_apply(world, 'nutrients', 'algae', 'saturation')

def logic_14614(world):
    _world_apply(world, 'nutrients', 'organic_matter', 'gap')

def logic_14615(world):
    _world_apply(world, 'nutrients', 'deadwood', 'direct')

def logic_14616(world):
    _world_apply(world, 'nutrients', 'pollinators', 'square')

def logic_14617(world):
    _world_apply(world, 'nutrients', 'flowers', 'saturation')

def logic_14618(world):
    _world_apply(world, 'nutrients', 'seed_bank', 'gap')

def logic_14619(world):
    _world_apply(world, 'nutrients', 'soil_carbon', 'direct')

def logic_14620(world):
    _world_apply(world, 'nutrients', 'surface_ice', 'square')

def logic_14621(world):
    _world_apply(world, 'decomposition_rate', 'temperature', 'pulse')

def logic_14622(world):
    _world_apply(world, 'decomposition_rate', 'surface_water', 'saturation')

def logic_14623(world):
    _world_apply(world, 'decomposition_rate', 'humidity', 'gap')

def logic_14624(world):
    _world_apply(world, 'decomposition_rate', 'cloud', 'direct')

def logic_14625(world):
    _world_apply(world, 'decomposition_rate', 'rain', 'pulse')

def logic_14626(world):
    _world_apply(world, 'decomposition_rate', 'soil_moisture', 'saturation')

def logic_14627(world):
    _world_apply(world, 'decomposition_rate', 'runoff', 'gap')

def logic_14628(world):
    _world_apply(world, 'decomposition_rate', 'wind_x', 'direct')

def logic_14629(world):
    _world_apply(world, 'decomposition_rate', 'wind_y', 'square')

def logic_14630(world):
    _world_apply(world, 'decomposition_rate', 'vegetation', 'pulse')

def logic_14631(world):
    _world_apply(world, 'decomposition_rate', 'biomass', 'saturation')

def logic_14632(world):
    _world_apply(world, 'decomposition_rate', 'herbivore', 'gap')

def logic_14633(world):
    _world_apply(world, 'decomposition_rate', 'predator', 'square')

def logic_14634(world):
    _world_apply(world, 'decomposition_rate', 'carrion', 'pulse')

def logic_14635(world):
    _world_apply(world, 'decomposition_rate', 'nutrients', 'saturation')

def logic_14636(world):
    _world_apply(world, 'decomposition_rate', 'oxygen', 'gap')

def logic_14637(world):
    _world_apply(world, 'decomposition_rate', 'co2', 'direct')

def logic_14638(world):
    _world_apply(world, 'decomposition_rate', 'photosynthesis_factor', 'square')

def logic_14639(world):
    _world_apply(world, 'decomposition_rate', 'ice', 'pulse')

def logic_14640(world):
    _world_apply(world, 'decomposition_rate', 'evaporation', 'saturation')

def logic_14641(world):
    _world_apply(world, 'decomposition_rate', 'detritus', 'direct')

def logic_14642(world):
    _world_apply(world, 'decomposition_rate', 'methane', 'square')

def logic_14643(world):
    _world_apply(world, 'decomposition_rate', 'pathogen_load', 'pulse')

def logic_14644(world):
    _world_apply(world, 'decomposition_rate', 'biodiversity', 'saturation')

def logic_14645(world):
    _world_apply(world, 'decomposition_rate', 'habitat_stress', 'gap')

def logic_14646(world):
    _world_apply(world, 'decomposition_rate', 'erosion', 'direct')

def logic_14647(world):
    _world_apply(world, 'decomposition_rate', 'soil_depth', 'square')

def logic_14648(world):
    _world_apply(world, 'decomposition_rate', 'root_density', 'pulse')

def logic_14649(world):
    _world_apply(world, 'decomposition_rate', 'wetland', 'gap')

def logic_14650(world):
    _world_apply(world, 'decomposition_rate', 'carbon_storage', 'direct')

def logic_14651(world):
    _world_apply(world, 'decomposition_rate', 'fire_risk', 'square')

def logic_14652(world):
    _world_apply(world, 'decomposition_rate', 'ash', 'pulse')

def logic_14653(world):
    _world_apply(world, 'decomposition_rate', 'snowpack', 'saturation')

def logic_14654(world):
    _world_apply(world, 'decomposition_rate', 'groundwater', 'gap')

def logic_14655(world):
    _world_apply(world, 'decomposition_rate', 'sediment', 'direct')

def logic_14656(world):
    _world_apply(world, 'decomposition_rate', 'salinity', 'square')

def logic_14657(world):
    _world_apply(world, 'decomposition_rate', 'algae', 'saturation')

def logic_14658(world):
    _world_apply(world, 'decomposition_rate', 'organic_matter', 'gap')

def logic_14659(world):
    _world_apply(world, 'decomposition_rate', 'deadwood', 'direct')

def logic_14660(world):
    _world_apply(world, 'decomposition_rate', 'pollinators', 'square')

def logic_14661(world):
    _world_apply(world, 'decomposition_rate', 'flowers', 'pulse')

def logic_14662(world):
    _world_apply(world, 'decomposition_rate', 'seed_bank', 'saturation')

def logic_14663(world):
    _world_apply(world, 'decomposition_rate', 'soil_carbon', 'gap')

def logic_14664(world):
    _world_apply(world, 'decomposition_rate', 'surface_ice', 'direct')

def logic_14665(world):
    _world_apply(world, 'oxygen', 'temperature', 'pulse')

def logic_14666(world):
    _world_apply(world, 'oxygen', 'surface_water', 'saturation')

def logic_14667(world):
    _world_apply(world, 'oxygen', 'humidity', 'gap')

def logic_14668(world):
    _world_apply(world, 'oxygen', 'cloud', 'direct')

def logic_14669(world):
    _world_apply(world, 'oxygen', 'rain', 'square')

def logic_14670(world):
    _world_apply(world, 'oxygen', 'soil_moisture', 'pulse')

def logic_14671(world):
    _world_apply(world, 'oxygen', 'runoff', 'saturation')

def logic_14672(world):
    _world_apply(world, 'oxygen', 'wind_x', 'gap')

def logic_14673(world):
    _world_apply(world, 'oxygen', 'wind_y', 'square')

def logic_14674(world):
    _world_apply(world, 'oxygen', 'vegetation', 'pulse')

def logic_14675(world):
    _world_apply(world, 'oxygen', 'biomass', 'saturation')

def logic_14676(world):
    _world_apply(world, 'oxygen', 'herbivore', 'gap')

def logic_14677(world):
    _world_apply(world, 'oxygen', 'predator', 'direct')

def logic_14678(world):
    _world_apply(world, 'oxygen', 'carrion', 'square')

def logic_14679(world):
    _world_apply(world, 'oxygen', 'nutrients', 'pulse')

def logic_14680(world):
    _world_apply(world, 'oxygen', 'decomposition_rate', 'saturation')

def logic_14681(world):
    _world_apply(world, 'oxygen', 'co2', 'direct')

def logic_14682(world):
    _world_apply(world, 'oxygen', 'photosynthesis_factor', 'square')

def logic_14683(world):
    _world_apply(world, 'oxygen', 'ice', 'pulse')

def logic_14684(world):
    _world_apply(world, 'oxygen', 'evaporation', 'saturation')

def logic_14685(world):
    _world_apply(world, 'oxygen', 'detritus', 'gap')

def logic_14686(world):
    _world_apply(world, 'oxygen', 'methane', 'direct')

def logic_14687(world):
    _world_apply(world, 'oxygen', 'pathogen_load', 'square')

def logic_14688(world):
    _world_apply(world, 'oxygen', 'biodiversity', 'pulse')

def logic_14689(world):
    _world_apply(world, 'oxygen', 'habitat_stress', 'gap')

def logic_14690(world):
    _world_apply(world, 'oxygen', 'erosion', 'direct')

def logic_14691(world):
    _world_apply(world, 'oxygen', 'soil_depth', 'square')

def logic_14692(world):
    _world_apply(world, 'oxygen', 'root_density', 'pulse')

def logic_14693(world):
    _world_apply(world, 'oxygen', 'wetland', 'saturation')

def logic_14694(world):
    _world_apply(world, 'oxygen', 'carbon_storage', 'gap')

def logic_14695(world):
    _world_apply(world, 'oxygen', 'fire_risk', 'direct')

def logic_14696(world):
    _world_apply(world, 'oxygen', 'ash', 'square')

def logic_14697(world):
    _world_apply(world, 'oxygen', 'snowpack', 'saturation')

def logic_14698(world):
    _world_apply(world, 'oxygen', 'groundwater', 'gap')

def logic_14699(world):
    _world_apply(world, 'oxygen', 'sediment', 'direct')

def logic_14700(world):
    _world_apply(world, 'oxygen', 'salinity', 'square')

def logic_14701(world):
    _world_apply(world, 'oxygen', 'algae', 'pulse')

def logic_14702(world):
    _world_apply(world, 'oxygen', 'organic_matter', 'saturation')

def logic_14703(world):
    _world_apply(world, 'oxygen', 'deadwood', 'gap')

def logic_14704(world):
    _world_apply(world, 'oxygen', 'pollinators', 'direct')

def logic_14705(world):
    _world_apply(world, 'oxygen', 'flowers', 'pulse')

def logic_14706(world):
    _world_apply(world, 'oxygen', 'seed_bank', 'saturation')

def logic_14707(world):
    _world_apply(world, 'oxygen', 'soil_carbon', 'gap')

def logic_14708(world):
    _world_apply(world, 'oxygen', 'surface_ice', 'direct')

def logic_14709(world):
    _world_apply(world, 'co2', 'temperature', 'square')

def logic_14710(world):
    _world_apply(world, 'co2', 'surface_water', 'pulse')

def logic_14711(world):
    _world_apply(world, 'co2', 'humidity', 'saturation')

def logic_14712(world):
    _world_apply(world, 'co2', 'cloud', 'gap')

def logic_14713(world):
    _world_apply(world, 'co2', 'rain', 'square')

def logic_14714(world):
    _world_apply(world, 'co2', 'soil_moisture', 'pulse')

def logic_14715(world):
    _world_apply(world, 'co2', 'runoff', 'saturation')

def logic_14716(world):
    _world_apply(world, 'co2', 'wind_x', 'gap')

def logic_14717(world):
    _world_apply(world, 'co2', 'wind_y', 'direct')

def logic_14718(world):
    _world_apply(world, 'co2', 'vegetation', 'square')

def logic_14719(world):
    _world_apply(world, 'co2', 'biomass', 'pulse')

def logic_14720(world):
    _world_apply(world, 'co2', 'herbivore', 'saturation')

def logic_14721(world):
    _world_apply(world, 'co2', 'predator', 'direct')

def logic_14722(world):
    _world_apply(world, 'co2', 'carrion', 'square')

def logic_14723(world):
    _world_apply(world, 'co2', 'nutrients', 'pulse')

def logic_14724(world):
    _world_apply(world, 'co2', 'decomposition_rate', 'saturation')

def logic_14725(world):
    _world_apply(world, 'co2', 'oxygen', 'gap')

def logic_14726(world):
    _world_apply(world, 'co2', 'photosynthesis_factor', 'direct')

def logic_14727(world):
    _world_apply(world, 'co2', 'ice', 'square')

def logic_14728(world):
    _world_apply(world, 'co2', 'evaporation', 'pulse')

def logic_14729(world):
    _world_apply(world, 'co2', 'detritus', 'gap')

def logic_14730(world):
    _world_apply(world, 'co2', 'methane', 'direct')

def logic_14731(world):
    _world_apply(world, 'co2', 'pathogen_load', 'square')

def logic_14732(world):
    _world_apply(world, 'co2', 'biodiversity', 'pulse')

def logic_14733(world):
    _world_apply(world, 'co2', 'habitat_stress', 'saturation')

def logic_14734(world):
    _world_apply(world, 'co2', 'erosion', 'gap')

def logic_14735(world):
    _world_apply(world, 'co2', 'soil_depth', 'direct')

def logic_14736(world):
    _world_apply(world, 'co2', 'root_density', 'square')

def logic_14737(world):
    _world_apply(world, 'co2', 'wetland', 'saturation')

def logic_14738(world):
    _world_apply(world, 'co2', 'carbon_storage', 'gap')

def logic_14739(world):
    _world_apply(world, 'co2', 'fire_risk', 'direct')

def logic_14740(world):
    _world_apply(world, 'co2', 'ash', 'square')

def logic_14741(world):
    _world_apply(world, 'co2', 'snowpack', 'pulse')

def logic_14742(world):
    _world_apply(world, 'co2', 'groundwater', 'saturation')

def logic_14743(world):
    _world_apply(world, 'co2', 'sediment', 'gap')

def logic_14744(world):
    _world_apply(world, 'co2', 'salinity', 'direct')

def logic_14745(world):
    _world_apply(world, 'co2', 'algae', 'pulse')

def logic_14746(world):
    _world_apply(world, 'co2', 'organic_matter', 'saturation')

def logic_14747(world):
    _world_apply(world, 'co2', 'deadwood', 'gap')

def logic_14748(world):
    _world_apply(world, 'co2', 'pollinators', 'direct')

def logic_14749(world):
    _world_apply(world, 'co2', 'flowers', 'square')

def logic_14750(world):
    _world_apply(world, 'co2', 'seed_bank', 'pulse')

def logic_14751(world):
    _world_apply(world, 'co2', 'soil_carbon', 'saturation')

def logic_14752(world):
    _world_apply(world, 'co2', 'surface_ice', 'gap')

def logic_14753(world):
    _world_apply(world, 'photosynthesis_factor', 'temperature', 'square')

def logic_14754(world):
    _world_apply(world, 'photosynthesis_factor', 'surface_water', 'pulse')

def logic_14755(world):
    _world_apply(world, 'photosynthesis_factor', 'humidity', 'saturation')

def logic_14756(world):
    _world_apply(world, 'photosynthesis_factor', 'cloud', 'gap')

def logic_14757(world):
    _world_apply(world, 'photosynthesis_factor', 'rain', 'direct')

def logic_14758(world):
    _world_apply(world, 'photosynthesis_factor', 'soil_moisture', 'square')

def logic_14759(world):
    _world_apply(world, 'photosynthesis_factor', 'runoff', 'pulse')

def logic_14760(world):
    _world_apply(world, 'photosynthesis_factor', 'wind_x', 'saturation')

def logic_14761(world):
    _world_apply(world, 'photosynthesis_factor', 'wind_y', 'direct')

def logic_14762(world):
    _world_apply(world, 'photosynthesis_factor', 'vegetation', 'square')

def logic_14763(world):
    _world_apply(world, 'photosynthesis_factor', 'biomass', 'pulse')

def logic_14764(world):
    _world_apply(world, 'photosynthesis_factor', 'herbivore', 'saturation')

def logic_14765(world):
    _world_apply(world, 'photosynthesis_factor', 'predator', 'gap')

def logic_14766(world):
    _world_apply(world, 'photosynthesis_factor', 'carrion', 'direct')

def logic_14767(world):
    _world_apply(world, 'photosynthesis_factor', 'nutrients', 'square')

def logic_14768(world):
    _world_apply(world, 'photosynthesis_factor', 'decomposition_rate', 'pulse')

def logic_14769(world):
    _world_apply(world, 'photosynthesis_factor', 'oxygen', 'gap')

def logic_14770(world):
    _world_apply(world, 'photosynthesis_factor', 'co2', 'direct')

def logic_14771(world):
    _world_apply(world, 'photosynthesis_factor', 'ice', 'square')

def logic_14772(world):
    _world_apply(world, 'photosynthesis_factor', 'evaporation', 'pulse')

def logic_14773(world):
    _world_apply(world, 'photosynthesis_factor', 'detritus', 'saturation')

def logic_14774(world):
    _world_apply(world, 'photosynthesis_factor', 'methane', 'gap')

def logic_14775(world):
    _world_apply(world, 'photosynthesis_factor', 'pathogen_load', 'direct')

def logic_14776(world):
    _world_apply(world, 'photosynthesis_factor', 'biodiversity', 'square')

def logic_14777(world):
    _world_apply(world, 'photosynthesis_factor', 'habitat_stress', 'saturation')

def logic_14778(world):
    _world_apply(world, 'photosynthesis_factor', 'erosion', 'gap')

def logic_14779(world):
    _world_apply(world, 'photosynthesis_factor', 'soil_depth', 'direct')

def logic_14780(world):
    _world_apply(world, 'photosynthesis_factor', 'root_density', 'square')

def logic_14781(world):
    _world_apply(world, 'photosynthesis_factor', 'wetland', 'pulse')

def logic_14782(world):
    _world_apply(world, 'photosynthesis_factor', 'carbon_storage', 'saturation')

def logic_14783(world):
    _world_apply(world, 'photosynthesis_factor', 'fire_risk', 'gap')

def logic_14784(world):
    _world_apply(world, 'photosynthesis_factor', 'ash', 'direct')

def logic_14785(world):
    _world_apply(world, 'photosynthesis_factor', 'snowpack', 'pulse')

def logic_14786(world):
    _world_apply(world, 'photosynthesis_factor', 'groundwater', 'saturation')

def logic_14787(world):
    _world_apply(world, 'photosynthesis_factor', 'sediment', 'gap')

def logic_14788(world):
    _world_apply(world, 'photosynthesis_factor', 'salinity', 'direct')

def logic_14789(world):
    _world_apply(world, 'photosynthesis_factor', 'algae', 'square')

def logic_14790(world):
    _world_apply(world, 'photosynthesis_factor', 'organic_matter', 'pulse')

def logic_14791(world):
    _world_apply(world, 'photosynthesis_factor', 'deadwood', 'saturation')

def logic_14792(world):
    _world_apply(world, 'photosynthesis_factor', 'pollinators', 'gap')

def logic_14793(world):
    _world_apply(world, 'photosynthesis_factor', 'flowers', 'square')

def logic_14794(world):
    _world_apply(world, 'photosynthesis_factor', 'seed_bank', 'pulse')

def logic_14795(world):
    _world_apply(world, 'photosynthesis_factor', 'soil_carbon', 'saturation')

def logic_14796(world):
    _world_apply(world, 'photosynthesis_factor', 'surface_ice', 'gap')

def logic_14797(world):
    _world_apply(world, 'ice', 'temperature', 'direct')

def logic_14798(world):
    _world_apply(world, 'ice', 'surface_water', 'square')

def logic_14799(world):
    _world_apply(world, 'ice', 'humidity', 'pulse')

def logic_14800(world):
    _world_apply(world, 'ice', 'cloud', 'saturation')

def logic_14801(world):
    _world_apply(world, 'ice', 'rain', 'direct')

def logic_14802(world):
    _world_apply(world, 'ice', 'soil_moisture', 'square')

def logic_14803(world):
    _world_apply(world, 'ice', 'runoff', 'pulse')

def logic_14804(world):
    _world_apply(world, 'ice', 'wind_x', 'saturation')

def logic_14805(world):
    _world_apply(world, 'ice', 'wind_y', 'gap')

def logic_14806(world):
    _world_apply(world, 'ice', 'vegetation', 'direct')

def logic_14807(world):
    _world_apply(world, 'ice', 'biomass', 'square')

def logic_14808(world):
    _world_apply(world, 'ice', 'herbivore', 'pulse')

def logic_14809(world):
    _world_apply(world, 'ice', 'predator', 'gap')

def logic_14810(world):
    _world_apply(world, 'ice', 'carrion', 'direct')

def logic_14811(world):
    _world_apply(world, 'ice', 'nutrients', 'square')

def logic_14812(world):
    _world_apply(world, 'ice', 'decomposition_rate', 'pulse')

def logic_14813(world):
    _world_apply(world, 'ice', 'oxygen', 'saturation')

def logic_14814(world):
    _world_apply(world, 'ice', 'co2', 'gap')

def logic_14815(world):
    _world_apply(world, 'ice', 'photosynthesis_factor', 'direct')

def logic_14816(world):
    _world_apply(world, 'ice', 'evaporation', 'square')

def logic_14817(world):
    _world_apply(world, 'ice', 'detritus', 'saturation')

def logic_14818(world):
    _world_apply(world, 'ice', 'methane', 'gap')

def logic_14819(world):
    _world_apply(world, 'ice', 'pathogen_load', 'direct')

def logic_14820(world):
    _world_apply(world, 'ice', 'biodiversity', 'square')

def logic_14821(world):
    _world_apply(world, 'ice', 'habitat_stress', 'pulse')

def logic_14822(world):
    _world_apply(world, 'ice', 'erosion', 'saturation')

def logic_14823(world):
    _world_apply(world, 'ice', 'soil_depth', 'gap')

def logic_14824(world):
    _world_apply(world, 'ice', 'root_density', 'direct')

def logic_14825(world):
    _world_apply(world, 'ice', 'wetland', 'pulse')

def logic_14826(world):
    _world_apply(world, 'ice', 'carbon_storage', 'saturation')

def logic_14827(world):
    _world_apply(world, 'ice', 'fire_risk', 'gap')

def logic_14828(world):
    _world_apply(world, 'ice', 'ash', 'direct')

def logic_14829(world):
    _world_apply(world, 'ice', 'snowpack', 'square')

def logic_14830(world):
    _world_apply(world, 'ice', 'groundwater', 'pulse')

def logic_14831(world):
    _world_apply(world, 'ice', 'sediment', 'saturation')

def logic_14832(world):
    _world_apply(world, 'ice', 'salinity', 'gap')

def logic_14833(world):
    _world_apply(world, 'ice', 'algae', 'square')

def logic_14834(world):
    _world_apply(world, 'ice', 'organic_matter', 'pulse')

def logic_14835(world):
    _world_apply(world, 'ice', 'deadwood', 'saturation')

def logic_14836(world):
    _world_apply(world, 'ice', 'pollinators', 'gap')

def logic_14837(world):
    _world_apply(world, 'ice', 'flowers', 'direct')

def logic_14838(world):
    _world_apply(world, 'ice', 'seed_bank', 'square')

def logic_14839(world):
    _world_apply(world, 'ice', 'soil_carbon', 'pulse')

def logic_14840(world):
    _world_apply(world, 'ice', 'surface_ice', 'saturation')

def logic_14841(world):
    _world_apply(world, 'evaporation', 'temperature', 'direct')

def logic_14842(world):
    _world_apply(world, 'evaporation', 'surface_water', 'square')

def logic_14843(world):
    _world_apply(world, 'evaporation', 'humidity', 'pulse')

def logic_14844(world):
    _world_apply(world, 'evaporation', 'cloud', 'saturation')

def logic_14845(world):
    _world_apply(world, 'evaporation', 'rain', 'gap')

def logic_14846(world):
    _world_apply(world, 'evaporation', 'soil_moisture', 'direct')

def logic_14847(world):
    _world_apply(world, 'evaporation', 'runoff', 'square')

def logic_14848(world):
    _world_apply(world, 'evaporation', 'wind_x', 'pulse')

def logic_14849(world):
    _world_apply(world, 'evaporation', 'wind_y', 'gap')

def logic_14850(world):
    _world_apply(world, 'evaporation', 'vegetation', 'direct')

def logic_14851(world):
    _world_apply(world, 'evaporation', 'biomass', 'square')

def logic_14852(world):
    _world_apply(world, 'evaporation', 'herbivore', 'pulse')

def logic_14853(world):
    _world_apply(world, 'evaporation', 'predator', 'saturation')

def logic_14854(world):
    _world_apply(world, 'evaporation', 'carrion', 'gap')

def logic_14855(world):
    _world_apply(world, 'evaporation', 'nutrients', 'direct')

def logic_14856(world):
    _world_apply(world, 'evaporation', 'decomposition_rate', 'square')

def logic_14857(world):
    _world_apply(world, 'evaporation', 'oxygen', 'saturation')

def logic_14858(world):
    _world_apply(world, 'evaporation', 'co2', 'gap')

def logic_14859(world):
    _world_apply(world, 'evaporation', 'photosynthesis_factor', 'direct')

def logic_14860(world):
    _world_apply(world, 'evaporation', 'ice', 'square')

def logic_14861(world):
    _world_apply(world, 'evaporation', 'detritus', 'pulse')

def logic_14862(world):
    _world_apply(world, 'evaporation', 'methane', 'saturation')

def logic_14863(world):
    _world_apply(world, 'evaporation', 'pathogen_load', 'gap')

def logic_14864(world):
    _world_apply(world, 'evaporation', 'biodiversity', 'direct')

def logic_14865(world):
    _world_apply(world, 'evaporation', 'habitat_stress', 'pulse')

def logic_14866(world):
    _world_apply(world, 'evaporation', 'erosion', 'saturation')

def logic_14867(world):
    _world_apply(world, 'evaporation', 'soil_depth', 'gap')

def logic_14868(world):
    _world_apply(world, 'evaporation', 'root_density', 'direct')

def logic_14869(world):
    _world_apply(world, 'evaporation', 'wetland', 'square')

def logic_14870(world):
    _world_apply(world, 'evaporation', 'carbon_storage', 'pulse')

def logic_14871(world):
    _world_apply(world, 'evaporation', 'fire_risk', 'saturation')

def logic_14872(world):
    _world_apply(world, 'evaporation', 'ash', 'gap')

def logic_14873(world):
    _world_apply(world, 'evaporation', 'snowpack', 'square')

def logic_14874(world):
    _world_apply(world, 'evaporation', 'groundwater', 'pulse')

def logic_14875(world):
    _world_apply(world, 'evaporation', 'sediment', 'saturation')

def logic_14876(world):
    _world_apply(world, 'evaporation', 'salinity', 'gap')

def logic_14877(world):
    _world_apply(world, 'evaporation', 'algae', 'direct')

def logic_14878(world):
    _world_apply(world, 'evaporation', 'organic_matter', 'square')

def logic_14879(world):
    _world_apply(world, 'evaporation', 'deadwood', 'pulse')

def logic_14880(world):
    _world_apply(world, 'evaporation', 'pollinators', 'saturation')

def logic_14881(world):
    _world_apply(world, 'evaporation', 'flowers', 'direct')

def logic_14882(world):
    _world_apply(world, 'evaporation', 'seed_bank', 'square')

def logic_14883(world):
    _world_apply(world, 'evaporation', 'soil_carbon', 'pulse')

def logic_14884(world):
    _world_apply(world, 'evaporation', 'surface_ice', 'saturation')

def logic_14885(world):
    _world_apply(world, 'detritus', 'temperature', 'gap')

def logic_14886(world):
    _world_apply(world, 'detritus', 'surface_water', 'direct')

def logic_14887(world):
    _world_apply(world, 'detritus', 'humidity', 'square')

def logic_14888(world):
    _world_apply(world, 'detritus', 'cloud', 'pulse')

def logic_14889(world):
    _world_apply(world, 'detritus', 'rain', 'gap')

def logic_14890(world):
    _world_apply(world, 'detritus', 'soil_moisture', 'direct')

def logic_14891(world):
    _world_apply(world, 'detritus', 'runoff', 'square')

def logic_14892(world):
    _world_apply(world, 'detritus', 'wind_x', 'pulse')

def logic_14893(world):
    _world_apply(world, 'detritus', 'wind_y', 'saturation')

def logic_14894(world):
    _world_apply(world, 'detritus', 'vegetation', 'gap')

def logic_14895(world):
    _world_apply(world, 'detritus', 'biomass', 'direct')

def logic_14896(world):
    _world_apply(world, 'detritus', 'herbivore', 'square')

def logic_14897(world):
    _world_apply(world, 'detritus', 'predator', 'saturation')

def logic_14898(world):
    _world_apply(world, 'detritus', 'carrion', 'gap')

def logic_14899(world):
    _world_apply(world, 'detritus', 'nutrients', 'direct')

def logic_14900(world):
    _world_apply(world, 'detritus', 'decomposition_rate', 'square')

def logic_14901(world):
    _world_apply(world, 'detritus', 'oxygen', 'pulse')

def logic_14902(world):
    _world_apply(world, 'detritus', 'co2', 'saturation')

def logic_14903(world):
    _world_apply(world, 'detritus', 'photosynthesis_factor', 'gap')

def logic_14904(world):
    _world_apply(world, 'detritus', 'ice', 'direct')

def logic_14905(world):
    _world_apply(world, 'detritus', 'evaporation', 'pulse')

def logic_14906(world):
    _world_apply(world, 'detritus', 'methane', 'saturation')

def logic_14907(world):
    _world_apply(world, 'detritus', 'pathogen_load', 'gap')

def logic_14908(world):
    _world_apply(world, 'detritus', 'biodiversity', 'direct')

def logic_14909(world):
    _world_apply(world, 'detritus', 'habitat_stress', 'square')

def logic_14910(world):
    _world_apply(world, 'detritus', 'erosion', 'pulse')

def logic_14911(world):
    _world_apply(world, 'detritus', 'soil_depth', 'saturation')

def logic_14912(world):
    _world_apply(world, 'detritus', 'root_density', 'gap')

def logic_14913(world):
    _world_apply(world, 'detritus', 'wetland', 'square')

def logic_14914(world):
    _world_apply(world, 'detritus', 'carbon_storage', 'pulse')

def logic_14915(world):
    _world_apply(world, 'detritus', 'fire_risk', 'saturation')

def logic_14916(world):
    _world_apply(world, 'detritus', 'ash', 'gap')

def logic_14917(world):
    _world_apply(world, 'detritus', 'snowpack', 'direct')

def logic_14918(world):
    _world_apply(world, 'detritus', 'groundwater', 'square')

def logic_14919(world):
    _world_apply(world, 'detritus', 'sediment', 'pulse')

def logic_14920(world):
    _world_apply(world, 'detritus', 'salinity', 'saturation')

def logic_14921(world):
    _world_apply(world, 'detritus', 'algae', 'direct')

def logic_14922(world):
    _world_apply(world, 'detritus', 'organic_matter', 'square')

def logic_14923(world):
    _world_apply(world, 'detritus', 'deadwood', 'pulse')

def logic_14924(world):
    _world_apply(world, 'detritus', 'pollinators', 'saturation')

def logic_14925(world):
    _world_apply(world, 'detritus', 'flowers', 'gap')

def logic_14926(world):
    _world_apply(world, 'detritus', 'seed_bank', 'direct')

def logic_14927(world):
    _world_apply(world, 'detritus', 'soil_carbon', 'square')

def logic_14928(world):
    _world_apply(world, 'detritus', 'surface_ice', 'pulse')

def logic_14929(world):
    _world_apply(world, 'methane', 'temperature', 'gap')

def logic_14930(world):
    _world_apply(world, 'methane', 'surface_water', 'direct')

def logic_14931(world):
    _world_apply(world, 'methane', 'humidity', 'square')

def logic_14932(world):
    _world_apply(world, 'methane', 'cloud', 'pulse')

def logic_14933(world):
    _world_apply(world, 'methane', 'rain', 'saturation')

def logic_14934(world):
    _world_apply(world, 'methane', 'soil_moisture', 'gap')

def logic_14935(world):
    _world_apply(world, 'methane', 'runoff', 'direct')

def logic_14936(world):
    _world_apply(world, 'methane', 'wind_x', 'square')

def logic_14937(world):
    _world_apply(world, 'methane', 'wind_y', 'saturation')

def logic_14938(world):
    _world_apply(world, 'methane', 'vegetation', 'gap')

def logic_14939(world):
    _world_apply(world, 'methane', 'biomass', 'direct')

def logic_14940(world):
    _world_apply(world, 'methane', 'herbivore', 'square')

def logic_14941(world):
    _world_apply(world, 'methane', 'predator', 'pulse')

def logic_14942(world):
    _world_apply(world, 'methane', 'carrion', 'saturation')

def logic_14943(world):
    _world_apply(world, 'methane', 'nutrients', 'gap')

def logic_14944(world):
    _world_apply(world, 'methane', 'decomposition_rate', 'direct')

def logic_14945(world):
    _world_apply(world, 'methane', 'oxygen', 'pulse')

def logic_14946(world):
    _world_apply(world, 'methane', 'co2', 'saturation')

def logic_14947(world):
    _world_apply(world, 'methane', 'photosynthesis_factor', 'gap')

def logic_14948(world):
    _world_apply(world, 'methane', 'ice', 'direct')

def logic_14949(world):
    _world_apply(world, 'methane', 'evaporation', 'square')

def logic_14950(world):
    _world_apply(world, 'methane', 'detritus', 'pulse')

def logic_14951(world):
    _world_apply(world, 'methane', 'pathogen_load', 'saturation')

def logic_14952(world):
    _world_apply(world, 'methane', 'biodiversity', 'gap')

def logic_14953(world):
    _world_apply(world, 'methane', 'habitat_stress', 'square')

def logic_14954(world):
    _world_apply(world, 'methane', 'erosion', 'pulse')

def logic_14955(world):
    _world_apply(world, 'methane', 'soil_depth', 'saturation')

def logic_14956(world):
    _world_apply(world, 'methane', 'root_density', 'gap')

def logic_14957(world):
    _world_apply(world, 'methane', 'wetland', 'direct')

def logic_14958(world):
    _world_apply(world, 'methane', 'carbon_storage', 'square')

def logic_14959(world):
    _world_apply(world, 'methane', 'fire_risk', 'pulse')

def logic_14960(world):
    _world_apply(world, 'methane', 'ash', 'saturation')

def logic_14961(world):
    _world_apply(world, 'methane', 'snowpack', 'direct')

def logic_14962(world):
    _world_apply(world, 'methane', 'groundwater', 'square')

def logic_14963(world):
    _world_apply(world, 'methane', 'sediment', 'pulse')

def logic_14964(world):
    _world_apply(world, 'methane', 'salinity', 'saturation')

def logic_14965(world):
    _world_apply(world, 'methane', 'algae', 'gap')

def logic_14966(world):
    _world_apply(world, 'methane', 'organic_matter', 'direct')

def logic_14967(world):
    _world_apply(world, 'methane', 'deadwood', 'square')

def logic_14968(world):
    _world_apply(world, 'methane', 'pollinators', 'pulse')

def logic_14969(world):
    _world_apply(world, 'methane', 'flowers', 'gap')

def logic_14970(world):
    _world_apply(world, 'methane', 'seed_bank', 'direct')

def logic_14971(world):
    _world_apply(world, 'methane', 'soil_carbon', 'square')

def logic_14972(world):
    _world_apply(world, 'methane', 'surface_ice', 'pulse')

def logic_14973(world):
    _world_apply(world, 'pathogen_load', 'temperature', 'saturation')

def logic_14974(world):
    _world_apply(world, 'pathogen_load', 'surface_water', 'gap')

def logic_14975(world):
    _world_apply(world, 'pathogen_load', 'humidity', 'direct')

def logic_14976(world):
    _world_apply(world, 'pathogen_load', 'cloud', 'square')

def logic_14977(world):
    _world_apply(world, 'pathogen_load', 'rain', 'saturation')

def logic_14978(world):
    _world_apply(world, 'pathogen_load', 'soil_moisture', 'gap')

def logic_14979(world):
    _world_apply(world, 'pathogen_load', 'runoff', 'direct')

def logic_14980(world):
    _world_apply(world, 'pathogen_load', 'wind_x', 'square')

def logic_14981(world):
    _world_apply(world, 'pathogen_load', 'wind_y', 'pulse')

def logic_14982(world):
    _world_apply(world, 'pathogen_load', 'vegetation', 'saturation')

def logic_14983(world):
    _world_apply(world, 'pathogen_load', 'biomass', 'gap')

def logic_14984(world):
    _world_apply(world, 'pathogen_load', 'herbivore', 'direct')

def logic_14985(world):
    _world_apply(world, 'pathogen_load', 'predator', 'pulse')

def logic_14986(world):
    _world_apply(world, 'pathogen_load', 'carrion', 'saturation')

def logic_14987(world):
    _world_apply(world, 'pathogen_load', 'nutrients', 'gap')

def logic_14988(world):
    _world_apply(world, 'pathogen_load', 'decomposition_rate', 'direct')

def logic_14989(world):
    _world_apply(world, 'pathogen_load', 'oxygen', 'square')

def logic_14990(world):
    _world_apply(world, 'pathogen_load', 'co2', 'pulse')

def logic_14991(world):
    _world_apply(world, 'pathogen_load', 'photosynthesis_factor', 'saturation')

def logic_14992(world):
    _world_apply(world, 'pathogen_load', 'ice', 'gap')

def logic_14993(world):
    _world_apply(world, 'pathogen_load', 'evaporation', 'square')

def logic_14994(world):
    _world_apply(world, 'pathogen_load', 'detritus', 'pulse')

def logic_14995(world):
    _world_apply(world, 'pathogen_load', 'methane', 'saturation')

def logic_14996(world):
    _world_apply(world, 'pathogen_load', 'biodiversity', 'gap')

def logic_14997(world):
    _world_apply(world, 'pathogen_load', 'habitat_stress', 'direct')

def logic_14998(world):
    _world_apply(world, 'pathogen_load', 'erosion', 'square')

def logic_14999(world):
    _world_apply(world, 'pathogen_load', 'soil_depth', 'pulse')

def logic_15000(world):
    _world_apply(world, 'pathogen_load', 'root_density', 'saturation')

def logic_15001(world):
    _world_apply(world, 'pathogen_load', 'wetland', 'direct')

def logic_15002(world):
    _world_apply(world, 'pathogen_load', 'carbon_storage', 'square')

def logic_15003(world):
    _world_apply(world, 'pathogen_load', 'fire_risk', 'pulse')

def logic_15004(world):
    _world_apply(world, 'pathogen_load', 'ash', 'saturation')

def logic_15005(world):
    _world_apply(world, 'pathogen_load', 'snowpack', 'gap')

def logic_15006(world):
    _world_apply(world, 'pathogen_load', 'groundwater', 'direct')

def logic_15007(world):
    _world_apply(world, 'pathogen_load', 'sediment', 'square')

def logic_15008(world):
    _world_apply(world, 'pathogen_load', 'salinity', 'pulse')

def logic_15009(world):
    _world_apply(world, 'pathogen_load', 'algae', 'gap')

def logic_15010(world):
    _world_apply(world, 'pathogen_load', 'organic_matter', 'direct')

def logic_15011(world):
    _world_apply(world, 'pathogen_load', 'deadwood', 'square')

def logic_15012(world):
    _world_apply(world, 'pathogen_load', 'pollinators', 'pulse')

def logic_15013(world):
    _world_apply(world, 'pathogen_load', 'flowers', 'saturation')

def logic_15014(world):
    _world_apply(world, 'pathogen_load', 'seed_bank', 'gap')

def logic_15015(world):
    _world_apply(world, 'pathogen_load', 'soil_carbon', 'direct')

def logic_15016(world):
    _world_apply(world, 'pathogen_load', 'surface_ice', 'square')

def logic_15017(world):
    _world_apply(world, 'biodiversity', 'temperature', 'saturation')

def logic_15018(world):
    _world_apply(world, 'biodiversity', 'surface_water', 'gap')

def logic_15019(world):
    _world_apply(world, 'biodiversity', 'humidity', 'direct')

def logic_15020(world):
    _world_apply(world, 'biodiversity', 'cloud', 'square')

def logic_15021(world):
    _world_apply(world, 'biodiversity', 'rain', 'pulse')

def logic_15022(world):
    _world_apply(world, 'biodiversity', 'soil_moisture', 'saturation')

def logic_15023(world):
    _world_apply(world, 'biodiversity', 'runoff', 'gap')

def logic_15024(world):
    _world_apply(world, 'biodiversity', 'wind_x', 'direct')

def logic_15025(world):
    _world_apply(world, 'biodiversity', 'wind_y', 'pulse')

def logic_15026(world):
    _world_apply(world, 'biodiversity', 'vegetation', 'saturation')

def logic_15027(world):
    _world_apply(world, 'biodiversity', 'biomass', 'gap')

def logic_15028(world):
    _world_apply(world, 'biodiversity', 'herbivore', 'direct')

def logic_15029(world):
    _world_apply(world, 'biodiversity', 'predator', 'square')

def logic_15030(world):
    _world_apply(world, 'biodiversity', 'carrion', 'pulse')

def logic_15031(world):
    _world_apply(world, 'biodiversity', 'nutrients', 'saturation')

def logic_15032(world):
    _world_apply(world, 'biodiversity', 'decomposition_rate', 'gap')

def logic_15033(world):
    _world_apply(world, 'biodiversity', 'oxygen', 'square')

def logic_15034(world):
    _world_apply(world, 'biodiversity', 'co2', 'pulse')

def logic_15035(world):
    _world_apply(world, 'biodiversity', 'photosynthesis_factor', 'saturation')

def logic_15036(world):
    _world_apply(world, 'biodiversity', 'ice', 'gap')

def logic_15037(world):
    _world_apply(world, 'biodiversity', 'evaporation', 'direct')

def logic_15038(world):
    _world_apply(world, 'biodiversity', 'detritus', 'square')

def logic_15039(world):
    _world_apply(world, 'biodiversity', 'methane', 'pulse')

def logic_15040(world):
    _world_apply(world, 'biodiversity', 'pathogen_load', 'saturation')

def logic_15041(world):
    _world_apply(world, 'biodiversity', 'habitat_stress', 'direct')

def logic_15042(world):
    _world_apply(world, 'biodiversity', 'erosion', 'square')

def logic_15043(world):
    _world_apply(world, 'biodiversity', 'soil_depth', 'pulse')

def logic_15044(world):
    _world_apply(world, 'biodiversity', 'root_density', 'saturation')

def logic_15045(world):
    _world_apply(world, 'biodiversity', 'wetland', 'gap')

def logic_15046(world):
    _world_apply(world, 'biodiversity', 'carbon_storage', 'direct')

def logic_15047(world):
    _world_apply(world, 'biodiversity', 'fire_risk', 'square')

def logic_15048(world):
    _world_apply(world, 'biodiversity', 'ash', 'pulse')

def logic_15049(world):
    _world_apply(world, 'biodiversity', 'snowpack', 'gap')

def logic_15050(world):
    _world_apply(world, 'biodiversity', 'groundwater', 'direct')

def logic_15051(world):
    _world_apply(world, 'biodiversity', 'sediment', 'square')

def logic_15052(world):
    _world_apply(world, 'biodiversity', 'salinity', 'pulse')

def logic_15053(world):
    _world_apply(world, 'biodiversity', 'algae', 'saturation')

def logic_15054(world):
    _world_apply(world, 'biodiversity', 'organic_matter', 'gap')

def logic_15055(world):
    _world_apply(world, 'biodiversity', 'deadwood', 'direct')

def logic_15056(world):
    _world_apply(world, 'biodiversity', 'pollinators', 'square')

def logic_15057(world):
    _world_apply(world, 'biodiversity', 'flowers', 'saturation')

def logic_15058(world):
    _world_apply(world, 'biodiversity', 'seed_bank', 'gap')

def logic_15059(world):
    _world_apply(world, 'biodiversity', 'soil_carbon', 'direct')

def logic_15060(world):
    _world_apply(world, 'biodiversity', 'surface_ice', 'square')

def logic_15061(world):
    _world_apply(world, 'habitat_stress', 'temperature', 'pulse')

def logic_15062(world):
    _world_apply(world, 'habitat_stress', 'surface_water', 'saturation')

def logic_15063(world):
    _world_apply(world, 'habitat_stress', 'humidity', 'gap')

def logic_15064(world):
    _world_apply(world, 'habitat_stress', 'cloud', 'direct')

def logic_15065(world):
    _world_apply(world, 'habitat_stress', 'rain', 'pulse')

def logic_15066(world):
    _world_apply(world, 'habitat_stress', 'soil_moisture', 'saturation')

def logic_15067(world):
    _world_apply(world, 'habitat_stress', 'runoff', 'gap')

def logic_15068(world):
    _world_apply(world, 'habitat_stress', 'wind_x', 'direct')

def logic_15069(world):
    _world_apply(world, 'habitat_stress', 'wind_y', 'square')

def logic_15070(world):
    _world_apply(world, 'habitat_stress', 'vegetation', 'pulse')

def logic_15071(world):
    _world_apply(world, 'habitat_stress', 'biomass', 'saturation')

def logic_15072(world):
    _world_apply(world, 'habitat_stress', 'herbivore', 'gap')

def logic_15073(world):
    _world_apply(world, 'habitat_stress', 'predator', 'square')

def logic_15074(world):
    _world_apply(world, 'habitat_stress', 'carrion', 'pulse')

def logic_15075(world):
    _world_apply(world, 'habitat_stress', 'nutrients', 'saturation')

def logic_15076(world):
    _world_apply(world, 'habitat_stress', 'decomposition_rate', 'gap')

def logic_15077(world):
    _world_apply(world, 'habitat_stress', 'oxygen', 'direct')

def logic_15078(world):
    _world_apply(world, 'habitat_stress', 'co2', 'square')

def logic_15079(world):
    _world_apply(world, 'habitat_stress', 'photosynthesis_factor', 'pulse')

def logic_15080(world):
    _world_apply(world, 'habitat_stress', 'ice', 'saturation')

def logic_15081(world):
    _world_apply(world, 'habitat_stress', 'evaporation', 'direct')

def logic_15082(world):
    _world_apply(world, 'habitat_stress', 'detritus', 'square')

def logic_15083(world):
    _world_apply(world, 'habitat_stress', 'methane', 'pulse')

def logic_15084(world):
    _world_apply(world, 'habitat_stress', 'pathogen_load', 'saturation')

def logic_15085(world):
    _world_apply(world, 'habitat_stress', 'biodiversity', 'gap')

def logic_15086(world):
    _world_apply(world, 'habitat_stress', 'erosion', 'direct')

def logic_15087(world):
    _world_apply(world, 'habitat_stress', 'soil_depth', 'square')

def logic_15088(world):
    _world_apply(world, 'habitat_stress', 'root_density', 'pulse')

def logic_15089(world):
    _world_apply(world, 'habitat_stress', 'wetland', 'gap')

def logic_15090(world):
    _world_apply(world, 'habitat_stress', 'carbon_storage', 'direct')

def logic_15091(world):
    _world_apply(world, 'habitat_stress', 'fire_risk', 'square')

def logic_15092(world):
    _world_apply(world, 'habitat_stress', 'ash', 'pulse')

def logic_15093(world):
    _world_apply(world, 'habitat_stress', 'snowpack', 'saturation')

def logic_15094(world):
    _world_apply(world, 'habitat_stress', 'groundwater', 'gap')

def logic_15095(world):
    _world_apply(world, 'habitat_stress', 'sediment', 'direct')

def logic_15096(world):
    _world_apply(world, 'habitat_stress', 'salinity', 'square')

def logic_15097(world):
    _world_apply(world, 'habitat_stress', 'algae', 'saturation')

def logic_15098(world):
    _world_apply(world, 'habitat_stress', 'organic_matter', 'gap')

def logic_15099(world):
    _world_apply(world, 'habitat_stress', 'deadwood', 'direct')

def logic_15100(world):
    _world_apply(world, 'habitat_stress', 'pollinators', 'square')

def logic_15101(world):
    _world_apply(world, 'habitat_stress', 'flowers', 'pulse')

def logic_15102(world):
    _world_apply(world, 'habitat_stress', 'seed_bank', 'saturation')

def logic_15103(world):
    _world_apply(world, 'habitat_stress', 'soil_carbon', 'gap')

def logic_15104(world):
    _world_apply(world, 'habitat_stress', 'surface_ice', 'direct')

def logic_15105(world):
    _world_apply(world, 'erosion', 'temperature', 'pulse')

def logic_15106(world):
    _world_apply(world, 'erosion', 'surface_water', 'saturation')

def logic_15107(world):
    _world_apply(world, 'erosion', 'humidity', 'gap')

def logic_15108(world):
    _world_apply(world, 'erosion', 'cloud', 'direct')

def logic_15109(world):
    _world_apply(world, 'erosion', 'rain', 'square')

def logic_15110(world):
    _world_apply(world, 'erosion', 'soil_moisture', 'pulse')

def logic_15111(world):
    _world_apply(world, 'erosion', 'runoff', 'saturation')

def logic_15112(world):
    _world_apply(world, 'erosion', 'wind_x', 'gap')

def logic_15113(world):
    _world_apply(world, 'erosion', 'wind_y', 'square')

def logic_15114(world):
    _world_apply(world, 'erosion', 'vegetation', 'pulse')

def logic_15115(world):
    _world_apply(world, 'erosion', 'biomass', 'saturation')

def logic_15116(world):
    _world_apply(world, 'erosion', 'herbivore', 'gap')

def logic_15117(world):
    _world_apply(world, 'erosion', 'predator', 'direct')

def logic_15118(world):
    _world_apply(world, 'erosion', 'carrion', 'square')

def logic_15119(world):
    _world_apply(world, 'erosion', 'nutrients', 'pulse')

def logic_15120(world):
    _world_apply(world, 'erosion', 'decomposition_rate', 'saturation')

def logic_15121(world):
    _world_apply(world, 'erosion', 'oxygen', 'direct')

def logic_15122(world):
    _world_apply(world, 'erosion', 'co2', 'square')

def logic_15123(world):
    _world_apply(world, 'erosion', 'photosynthesis_factor', 'pulse')

def logic_15124(world):
    _world_apply(world, 'erosion', 'ice', 'saturation')

def logic_15125(world):
    _world_apply(world, 'erosion', 'evaporation', 'gap')

def logic_15126(world):
    _world_apply(world, 'erosion', 'detritus', 'direct')

def logic_15127(world):
    _world_apply(world, 'erosion', 'methane', 'square')

def logic_15128(world):
    _world_apply(world, 'erosion', 'pathogen_load', 'pulse')

def logic_15129(world):
    _world_apply(world, 'erosion', 'biodiversity', 'gap')

def logic_15130(world):
    _world_apply(world, 'erosion', 'habitat_stress', 'direct')

def logic_15131(world):
    _world_apply(world, 'erosion', 'soil_depth', 'square')

def logic_15132(world):
    _world_apply(world, 'erosion', 'root_density', 'pulse')

def logic_15133(world):
    _world_apply(world, 'erosion', 'wetland', 'saturation')

def logic_15134(world):
    _world_apply(world, 'erosion', 'carbon_storage', 'gap')

def logic_15135(world):
    _world_apply(world, 'erosion', 'fire_risk', 'direct')

def logic_15136(world):
    _world_apply(world, 'erosion', 'ash', 'square')

def logic_15137(world):
    _world_apply(world, 'erosion', 'snowpack', 'saturation')

def logic_15138(world):
    _world_apply(world, 'erosion', 'groundwater', 'gap')

def logic_15139(world):
    _world_apply(world, 'erosion', 'sediment', 'direct')

def logic_15140(world):
    _world_apply(world, 'erosion', 'salinity', 'square')

def logic_15141(world):
    _world_apply(world, 'erosion', 'algae', 'pulse')

def logic_15142(world):
    _world_apply(world, 'erosion', 'organic_matter', 'saturation')

def logic_15143(world):
    _world_apply(world, 'erosion', 'deadwood', 'gap')

def logic_15144(world):
    _world_apply(world, 'erosion', 'pollinators', 'direct')

def logic_15145(world):
    _world_apply(world, 'erosion', 'flowers', 'pulse')

def logic_15146(world):
    _world_apply(world, 'erosion', 'seed_bank', 'saturation')

def logic_15147(world):
    _world_apply(world, 'erosion', 'soil_carbon', 'gap')

def logic_15148(world):
    _world_apply(world, 'erosion', 'surface_ice', 'direct')

def logic_15149(world):
    _world_apply(world, 'soil_depth', 'temperature', 'square')

def logic_15150(world):
    _world_apply(world, 'soil_depth', 'surface_water', 'pulse')

def logic_15151(world):
    _world_apply(world, 'soil_depth', 'humidity', 'saturation')

def logic_15152(world):
    _world_apply(world, 'soil_depth', 'cloud', 'gap')

def logic_15153(world):
    _world_apply(world, 'soil_depth', 'rain', 'square')

def logic_15154(world):
    _world_apply(world, 'soil_depth', 'soil_moisture', 'pulse')

def logic_15155(world):
    _world_apply(world, 'soil_depth', 'runoff', 'saturation')

def logic_15156(world):
    _world_apply(world, 'soil_depth', 'wind_x', 'gap')

def logic_15157(world):
    _world_apply(world, 'soil_depth', 'wind_y', 'direct')

def logic_15158(world):
    _world_apply(world, 'soil_depth', 'vegetation', 'square')

def logic_15159(world):
    _world_apply(world, 'soil_depth', 'biomass', 'pulse')

def logic_15160(world):
    _world_apply(world, 'soil_depth', 'herbivore', 'saturation')

def logic_15161(world):
    _world_apply(world, 'soil_depth', 'predator', 'direct')

def logic_15162(world):
    _world_apply(world, 'soil_depth', 'carrion', 'square')

def logic_15163(world):
    _world_apply(world, 'soil_depth', 'nutrients', 'pulse')

def logic_15164(world):
    _world_apply(world, 'soil_depth', 'decomposition_rate', 'saturation')

def logic_15165(world):
    _world_apply(world, 'soil_depth', 'oxygen', 'gap')

def logic_15166(world):
    _world_apply(world, 'soil_depth', 'co2', 'direct')

def logic_15167(world):
    _world_apply(world, 'soil_depth', 'photosynthesis_factor', 'square')

def logic_15168(world):
    _world_apply(world, 'soil_depth', 'ice', 'pulse')

def logic_15169(world):
    _world_apply(world, 'soil_depth', 'evaporation', 'gap')

def logic_15170(world):
    _world_apply(world, 'soil_depth', 'detritus', 'direct')

def logic_15171(world):
    _world_apply(world, 'soil_depth', 'methane', 'square')

def logic_15172(world):
    _world_apply(world, 'soil_depth', 'pathogen_load', 'pulse')

def logic_15173(world):
    _world_apply(world, 'soil_depth', 'biodiversity', 'saturation')

def logic_15174(world):
    _world_apply(world, 'soil_depth', 'habitat_stress', 'gap')

def logic_15175(world):
    _world_apply(world, 'soil_depth', 'erosion', 'direct')

def logic_15176(world):
    _world_apply(world, 'soil_depth', 'root_density', 'square')

def logic_15177(world):
    _world_apply(world, 'soil_depth', 'wetland', 'saturation')

def logic_15178(world):
    _world_apply(world, 'soil_depth', 'carbon_storage', 'gap')

def logic_15179(world):
    _world_apply(world, 'soil_depth', 'fire_risk', 'direct')

def logic_15180(world):
    _world_apply(world, 'soil_depth', 'ash', 'square')

def logic_15181(world):
    _world_apply(world, 'soil_depth', 'snowpack', 'pulse')

def logic_15182(world):
    _world_apply(world, 'soil_depth', 'groundwater', 'saturation')

def logic_15183(world):
    _world_apply(world, 'soil_depth', 'sediment', 'gap')

def logic_15184(world):
    _world_apply(world, 'soil_depth', 'salinity', 'direct')

def logic_15185(world):
    _world_apply(world, 'soil_depth', 'algae', 'pulse')

def logic_15186(world):
    _world_apply(world, 'soil_depth', 'organic_matter', 'saturation')

def logic_15187(world):
    _world_apply(world, 'soil_depth', 'deadwood', 'gap')

def logic_15188(world):
    _world_apply(world, 'soil_depth', 'pollinators', 'direct')

def logic_15189(world):
    _world_apply(world, 'soil_depth', 'flowers', 'square')

def logic_15190(world):
    _world_apply(world, 'soil_depth', 'seed_bank', 'pulse')

def logic_15191(world):
    _world_apply(world, 'soil_depth', 'soil_carbon', 'saturation')

def logic_15192(world):
    _world_apply(world, 'soil_depth', 'surface_ice', 'gap')

def logic_15193(world):
    _world_apply(world, 'root_density', 'temperature', 'square')

def logic_15194(world):
    _world_apply(world, 'root_density', 'surface_water', 'pulse')

def logic_15195(world):
    _world_apply(world, 'root_density', 'humidity', 'saturation')

def logic_15196(world):
    _world_apply(world, 'root_density', 'cloud', 'gap')

def logic_15197(world):
    _world_apply(world, 'root_density', 'rain', 'direct')

def logic_15198(world):
    _world_apply(world, 'root_density', 'soil_moisture', 'square')

def logic_15199(world):
    _world_apply(world, 'root_density', 'runoff', 'pulse')

def logic_15200(world):
    _world_apply(world, 'root_density', 'wind_x', 'saturation')

def logic_15201(world):
    _world_apply(world, 'root_density', 'wind_y', 'direct')

def logic_15202(world):
    _world_apply(world, 'root_density', 'vegetation', 'square')

def logic_15203(world):
    _world_apply(world, 'root_density', 'biomass', 'pulse')

def logic_15204(world):
    _world_apply(world, 'root_density', 'herbivore', 'saturation')

def logic_15205(world):
    _world_apply(world, 'root_density', 'predator', 'gap')

def logic_15206(world):
    _world_apply(world, 'root_density', 'carrion', 'direct')

def logic_15207(world):
    _world_apply(world, 'root_density', 'nutrients', 'square')

def logic_15208(world):
    _world_apply(world, 'root_density', 'decomposition_rate', 'pulse')

def logic_15209(world):
    _world_apply(world, 'root_density', 'oxygen', 'gap')

def logic_15210(world):
    _world_apply(world, 'root_density', 'co2', 'direct')

def logic_15211(world):
    _world_apply(world, 'root_density', 'photosynthesis_factor', 'square')

def logic_15212(world):
    _world_apply(world, 'root_density', 'ice', 'pulse')

def logic_15213(world):
    _world_apply(world, 'root_density', 'evaporation', 'saturation')

def logic_15214(world):
    _world_apply(world, 'root_density', 'detritus', 'gap')

def logic_15215(world):
    _world_apply(world, 'root_density', 'methane', 'direct')

def logic_15216(world):
    _world_apply(world, 'root_density', 'pathogen_load', 'square')

def logic_15217(world):
    _world_apply(world, 'root_density', 'biodiversity', 'saturation')

def logic_15218(world):
    _world_apply(world, 'root_density', 'habitat_stress', 'gap')

def logic_15219(world):
    _world_apply(world, 'root_density', 'erosion', 'direct')

def logic_15220(world):
    _world_apply(world, 'root_density', 'soil_depth', 'square')

def logic_15221(world):
    _world_apply(world, 'root_density', 'wetland', 'pulse')

def logic_15222(world):
    _world_apply(world, 'root_density', 'carbon_storage', 'saturation')

def logic_15223(world):
    _world_apply(world, 'root_density', 'fire_risk', 'gap')

def logic_15224(world):
    _world_apply(world, 'root_density', 'ash', 'direct')

def logic_15225(world):
    _world_apply(world, 'root_density', 'snowpack', 'pulse')

def logic_15226(world):
    _world_apply(world, 'root_density', 'groundwater', 'saturation')

def logic_15227(world):
    _world_apply(world, 'root_density', 'sediment', 'gap')

def logic_15228(world):
    _world_apply(world, 'root_density', 'salinity', 'direct')

def logic_15229(world):
    _world_apply(world, 'root_density', 'algae', 'square')

def logic_15230(world):
    _world_apply(world, 'root_density', 'organic_matter', 'pulse')

def logic_15231(world):
    _world_apply(world, 'root_density', 'deadwood', 'saturation')

def logic_15232(world):
    _world_apply(world, 'root_density', 'pollinators', 'gap')

def logic_15233(world):
    _world_apply(world, 'root_density', 'flowers', 'square')

def logic_15234(world):
    _world_apply(world, 'root_density', 'seed_bank', 'pulse')

def logic_15235(world):
    _world_apply(world, 'root_density', 'soil_carbon', 'saturation')

def logic_15236(world):
    _world_apply(world, 'root_density', 'surface_ice', 'gap')

def logic_15237(world):
    _world_apply(world, 'wetland', 'temperature', 'direct')

def logic_15238(world):
    _world_apply(world, 'wetland', 'surface_water', 'square')

def logic_15239(world):
    _world_apply(world, 'wetland', 'humidity', 'pulse')

def logic_15240(world):
    _world_apply(world, 'wetland', 'cloud', 'saturation')

def logic_15241(world):
    _world_apply(world, 'wetland', 'rain', 'direct')

def logic_15242(world):
    _world_apply(world, 'wetland', 'soil_moisture', 'square')

def logic_15243(world):
    _world_apply(world, 'wetland', 'runoff', 'pulse')

def logic_15244(world):
    _world_apply(world, 'wetland', 'wind_x', 'saturation')

def logic_15245(world):
    _world_apply(world, 'wetland', 'wind_y', 'gap')

def logic_15246(world):
    _world_apply(world, 'wetland', 'vegetation', 'direct')

def logic_15247(world):
    _world_apply(world, 'wetland', 'biomass', 'square')

def logic_15248(world):
    _world_apply(world, 'wetland', 'herbivore', 'pulse')

def logic_15249(world):
    _world_apply(world, 'wetland', 'predator', 'gap')

def logic_15250(world):
    _world_apply(world, 'wetland', 'carrion', 'direct')

def logic_15251(world):
    _world_apply(world, 'wetland', 'nutrients', 'square')

def logic_15252(world):
    _world_apply(world, 'wetland', 'decomposition_rate', 'pulse')

def logic_15253(world):
    _world_apply(world, 'wetland', 'oxygen', 'saturation')

def logic_15254(world):
    _world_apply(world, 'wetland', 'co2', 'gap')

def logic_15255(world):
    _world_apply(world, 'wetland', 'photosynthesis_factor', 'direct')

def logic_15256(world):
    _world_apply(world, 'wetland', 'ice', 'square')

def logic_15257(world):
    _world_apply(world, 'wetland', 'evaporation', 'saturation')

def logic_15258(world):
    _world_apply(world, 'wetland', 'detritus', 'gap')

def logic_15259(world):
    _world_apply(world, 'wetland', 'methane', 'direct')

def logic_15260(world):
    _world_apply(world, 'wetland', 'pathogen_load', 'square')

def logic_15261(world):
    _world_apply(world, 'wetland', 'biodiversity', 'pulse')

def logic_15262(world):
    _world_apply(world, 'wetland', 'habitat_stress', 'saturation')

def logic_15263(world):
    _world_apply(world, 'wetland', 'erosion', 'gap')

def logic_15264(world):
    _world_apply(world, 'wetland', 'soil_depth', 'direct')

def logic_15265(world):
    _world_apply(world, 'wetland', 'root_density', 'pulse')

def logic_15266(world):
    _world_apply(world, 'wetland', 'carbon_storage', 'saturation')

def logic_15267(world):
    _world_apply(world, 'wetland', 'fire_risk', 'gap')

def logic_15268(world):
    _world_apply(world, 'wetland', 'ash', 'direct')

def logic_15269(world):
    _world_apply(world, 'wetland', 'snowpack', 'square')

def logic_15270(world):
    _world_apply(world, 'wetland', 'groundwater', 'pulse')

def logic_15271(world):
    _world_apply(world, 'wetland', 'sediment', 'saturation')

def logic_15272(world):
    _world_apply(world, 'wetland', 'salinity', 'gap')

def logic_15273(world):
    _world_apply(world, 'wetland', 'algae', 'square')

def logic_15274(world):
    _world_apply(world, 'wetland', 'organic_matter', 'pulse')

def logic_15275(world):
    _world_apply(world, 'wetland', 'deadwood', 'saturation')

def logic_15276(world):
    _world_apply(world, 'wetland', 'pollinators', 'gap')

def logic_15277(world):
    _world_apply(world, 'wetland', 'flowers', 'direct')

def logic_15278(world):
    _world_apply(world, 'wetland', 'seed_bank', 'square')

def logic_15279(world):
    _world_apply(world, 'wetland', 'soil_carbon', 'pulse')

def logic_15280(world):
    _world_apply(world, 'wetland', 'surface_ice', 'saturation')

def logic_15281(world):
    _world_apply(world, 'carbon_storage', 'temperature', 'direct')

def logic_15282(world):
    _world_apply(world, 'carbon_storage', 'surface_water', 'square')

def logic_15283(world):
    _world_apply(world, 'carbon_storage', 'humidity', 'pulse')

def logic_15284(world):
    _world_apply(world, 'carbon_storage', 'cloud', 'saturation')

def logic_15285(world):
    _world_apply(world, 'carbon_storage', 'rain', 'gap')

def logic_15286(world):
    _world_apply(world, 'carbon_storage', 'soil_moisture', 'direct')

def logic_15287(world):
    _world_apply(world, 'carbon_storage', 'runoff', 'square')

def logic_15288(world):
    _world_apply(world, 'carbon_storage', 'wind_x', 'pulse')

def logic_15289(world):
    _world_apply(world, 'carbon_storage', 'wind_y', 'gap')

def logic_15290(world):
    _world_apply(world, 'carbon_storage', 'vegetation', 'direct')

def logic_15291(world):
    _world_apply(world, 'carbon_storage', 'biomass', 'square')

def logic_15292(world):
    _world_apply(world, 'carbon_storage', 'herbivore', 'pulse')

def logic_15293(world):
    _world_apply(world, 'carbon_storage', 'predator', 'saturation')

def logic_15294(world):
    _world_apply(world, 'carbon_storage', 'carrion', 'gap')

def logic_15295(world):
    _world_apply(world, 'carbon_storage', 'nutrients', 'direct')

def logic_15296(world):
    _world_apply(world, 'carbon_storage', 'decomposition_rate', 'square')

def logic_15297(world):
    _world_apply(world, 'carbon_storage', 'oxygen', 'saturation')

def logic_15298(world):
    _world_apply(world, 'carbon_storage', 'co2', 'gap')

def logic_15299(world):
    _world_apply(world, 'carbon_storage', 'photosynthesis_factor', 'direct')

def logic_15300(world):
    _world_apply(world, 'carbon_storage', 'ice', 'square')

def logic_15301(world):
    _world_apply(world, 'carbon_storage', 'evaporation', 'pulse')

def logic_15302(world):
    _world_apply(world, 'carbon_storage', 'detritus', 'saturation')

def logic_15303(world):
    _world_apply(world, 'carbon_storage', 'methane', 'gap')

def logic_15304(world):
    _world_apply(world, 'carbon_storage', 'pathogen_load', 'direct')

def logic_15305(world):
    _world_apply(world, 'carbon_storage', 'biodiversity', 'pulse')

def logic_15306(world):
    _world_apply(world, 'carbon_storage', 'habitat_stress', 'saturation')

def logic_15307(world):
    _world_apply(world, 'carbon_storage', 'erosion', 'gap')

def logic_15308(world):
    _world_apply(world, 'carbon_storage', 'soil_depth', 'direct')

def logic_15309(world):
    _world_apply(world, 'carbon_storage', 'root_density', 'square')

def logic_15310(world):
    _world_apply(world, 'carbon_storage', 'wetland', 'pulse')

def logic_15311(world):
    _world_apply(world, 'carbon_storage', 'fire_risk', 'saturation')

def logic_15312(world):
    _world_apply(world, 'carbon_storage', 'ash', 'gap')

def logic_15313(world):
    _world_apply(world, 'carbon_storage', 'snowpack', 'square')

def logic_15314(world):
    _world_apply(world, 'carbon_storage', 'groundwater', 'pulse')

def logic_15315(world):
    _world_apply(world, 'carbon_storage', 'sediment', 'saturation')

def logic_15316(world):
    _world_apply(world, 'carbon_storage', 'salinity', 'gap')

def logic_15317(world):
    _world_apply(world, 'carbon_storage', 'algae', 'direct')

def logic_15318(world):
    _world_apply(world, 'carbon_storage', 'organic_matter', 'square')

def logic_15319(world):
    _world_apply(world, 'carbon_storage', 'deadwood', 'pulse')

def logic_15320(world):
    _world_apply(world, 'carbon_storage', 'pollinators', 'saturation')

def logic_15321(world):
    _world_apply(world, 'carbon_storage', 'flowers', 'direct')

def logic_15322(world):
    _world_apply(world, 'carbon_storage', 'seed_bank', 'square')

def logic_15323(world):
    _world_apply(world, 'carbon_storage', 'soil_carbon', 'pulse')

def logic_15324(world):
    _world_apply(world, 'carbon_storage', 'surface_ice', 'saturation')

def logic_15325(world):
    _world_apply(world, 'fire_risk', 'temperature', 'gap')

def logic_15326(world):
    _world_apply(world, 'fire_risk', 'surface_water', 'direct')

def logic_15327(world):
    _world_apply(world, 'fire_risk', 'humidity', 'square')

def logic_15328(world):
    _world_apply(world, 'fire_risk', 'cloud', 'pulse')

def logic_15329(world):
    _world_apply(world, 'fire_risk', 'rain', 'gap')

def logic_15330(world):
    _world_apply(world, 'fire_risk', 'soil_moisture', 'direct')

def logic_15331(world):
    _world_apply(world, 'fire_risk', 'runoff', 'square')

def logic_15332(world):
    _world_apply(world, 'fire_risk', 'wind_x', 'pulse')

def logic_15333(world):
    _world_apply(world, 'fire_risk', 'wind_y', 'saturation')

def logic_15334(world):
    _world_apply(world, 'fire_risk', 'vegetation', 'gap')

def logic_15335(world):
    _world_apply(world, 'fire_risk', 'biomass', 'direct')

def logic_15336(world):
    _world_apply(world, 'fire_risk', 'herbivore', 'square')

def logic_15337(world):
    _world_apply(world, 'fire_risk', 'predator', 'saturation')

def logic_15338(world):
    _world_apply(world, 'fire_risk', 'carrion', 'gap')

def logic_15339(world):
    _world_apply(world, 'fire_risk', 'nutrients', 'direct')

def logic_15340(world):
    _world_apply(world, 'fire_risk', 'decomposition_rate', 'square')

def logic_15341(world):
    _world_apply(world, 'fire_risk', 'oxygen', 'pulse')

def logic_15342(world):
    _world_apply(world, 'fire_risk', 'co2', 'saturation')

def logic_15343(world):
    _world_apply(world, 'fire_risk', 'photosynthesis_factor', 'gap')

def logic_15344(world):
    _world_apply(world, 'fire_risk', 'ice', 'direct')

def logic_15345(world):
    _world_apply(world, 'fire_risk', 'evaporation', 'pulse')

def logic_15346(world):
    _world_apply(world, 'fire_risk', 'detritus', 'saturation')

def logic_15347(world):
    _world_apply(world, 'fire_risk', 'methane', 'gap')

def logic_15348(world):
    _world_apply(world, 'fire_risk', 'pathogen_load', 'direct')

def logic_15349(world):
    _world_apply(world, 'fire_risk', 'biodiversity', 'square')

def logic_15350(world):
    _world_apply(world, 'fire_risk', 'habitat_stress', 'pulse')

def logic_15351(world):
    _world_apply(world, 'fire_risk', 'erosion', 'saturation')

def logic_15352(world):
    _world_apply(world, 'fire_risk', 'soil_depth', 'gap')

def logic_15353(world):
    _world_apply(world, 'fire_risk', 'root_density', 'square')

def logic_15354(world):
    _world_apply(world, 'fire_risk', 'wetland', 'pulse')

def logic_15355(world):
    _world_apply(world, 'fire_risk', 'carbon_storage', 'saturation')

def logic_15356(world):
    _world_apply(world, 'fire_risk', 'ash', 'gap')

def logic_15357(world):
    _world_apply(world, 'fire_risk', 'snowpack', 'direct')

def logic_15358(world):
    _world_apply(world, 'fire_risk', 'groundwater', 'square')

def logic_15359(world):
    _world_apply(world, 'fire_risk', 'sediment', 'pulse')

def logic_15360(world):
    _world_apply(world, 'fire_risk', 'salinity', 'saturation')

def logic_15361(world):
    _world_apply(world, 'fire_risk', 'algae', 'direct')

def logic_15362(world):
    _world_apply(world, 'fire_risk', 'organic_matter', 'square')

def logic_15363(world):
    _world_apply(world, 'fire_risk', 'deadwood', 'pulse')

def logic_15364(world):
    _world_apply(world, 'fire_risk', 'pollinators', 'saturation')

def logic_15365(world):
    _world_apply(world, 'fire_risk', 'flowers', 'gap')

def logic_15366(world):
    _world_apply(world, 'fire_risk', 'seed_bank', 'direct')

def logic_15367(world):
    _world_apply(world, 'fire_risk', 'soil_carbon', 'square')

def logic_15368(world):
    _world_apply(world, 'fire_risk', 'surface_ice', 'pulse')

def logic_15369(world):
    _world_apply(world, 'ash', 'temperature', 'gap')

def logic_15370(world):
    _world_apply(world, 'ash', 'surface_water', 'direct')

def logic_15371(world):
    _world_apply(world, 'ash', 'humidity', 'square')

def logic_15372(world):
    _world_apply(world, 'ash', 'cloud', 'pulse')

def logic_15373(world):
    _world_apply(world, 'ash', 'rain', 'saturation')

def logic_15374(world):
    _world_apply(world, 'ash', 'soil_moisture', 'gap')

def logic_15375(world):
    _world_apply(world, 'ash', 'runoff', 'direct')

def logic_15376(world):
    _world_apply(world, 'ash', 'wind_x', 'square')

def logic_15377(world):
    _world_apply(world, 'ash', 'wind_y', 'saturation')

def logic_15378(world):
    _world_apply(world, 'ash', 'vegetation', 'gap')

def logic_15379(world):
    _world_apply(world, 'ash', 'biomass', 'direct')

def logic_15380(world):
    _world_apply(world, 'ash', 'herbivore', 'square')

def logic_15381(world):
    _world_apply(world, 'ash', 'predator', 'pulse')

def logic_15382(world):
    _world_apply(world, 'ash', 'carrion', 'saturation')

def logic_15383(world):
    _world_apply(world, 'ash', 'nutrients', 'gap')

def logic_15384(world):
    _world_apply(world, 'ash', 'decomposition_rate', 'direct')

def logic_15385(world):
    _world_apply(world, 'ash', 'oxygen', 'pulse')

def logic_15386(world):
    _world_apply(world, 'ash', 'co2', 'saturation')

def logic_15387(world):
    _world_apply(world, 'ash', 'photosynthesis_factor', 'gap')

def logic_15388(world):
    _world_apply(world, 'ash', 'ice', 'direct')

def logic_15389(world):
    _world_apply(world, 'ash', 'evaporation', 'square')

def logic_15390(world):
    _world_apply(world, 'ash', 'detritus', 'pulse')

def logic_15391(world):
    _world_apply(world, 'ash', 'methane', 'saturation')

def logic_15392(world):
    _world_apply(world, 'ash', 'pathogen_load', 'gap')

def logic_15393(world):
    _world_apply(world, 'ash', 'biodiversity', 'square')

def logic_15394(world):
    _world_apply(world, 'ash', 'habitat_stress', 'pulse')

def logic_15395(world):
    _world_apply(world, 'ash', 'erosion', 'saturation')

def logic_15396(world):
    _world_apply(world, 'ash', 'soil_depth', 'gap')

def logic_15397(world):
    _world_apply(world, 'ash', 'root_density', 'direct')

def logic_15398(world):
    _world_apply(world, 'ash', 'wetland', 'square')

def logic_15399(world):
    _world_apply(world, 'ash', 'carbon_storage', 'pulse')

def logic_15400(world):
    _world_apply(world, 'ash', 'fire_risk', 'saturation')

def logic_15401(world):
    _world_apply(world, 'ash', 'snowpack', 'direct')

def logic_15402(world):
    _world_apply(world, 'ash', 'groundwater', 'square')

def logic_15403(world):
    _world_apply(world, 'ash', 'sediment', 'pulse')

def logic_15404(world):
    _world_apply(world, 'ash', 'salinity', 'saturation')

def logic_15405(world):
    _world_apply(world, 'ash', 'algae', 'gap')

def logic_15406(world):
    _world_apply(world, 'ash', 'organic_matter', 'direct')

def logic_15407(world):
    _world_apply(world, 'ash', 'deadwood', 'square')

def logic_15408(world):
    _world_apply(world, 'ash', 'pollinators', 'pulse')

def logic_15409(world):
    _world_apply(world, 'ash', 'flowers', 'gap')

def logic_15410(world):
    _world_apply(world, 'ash', 'seed_bank', 'direct')

def logic_15411(world):
    _world_apply(world, 'ash', 'soil_carbon', 'square')

def logic_15412(world):
    _world_apply(world, 'ash', 'surface_ice', 'pulse')

def logic_15413(world):
    _world_apply(world, 'snowpack', 'temperature', 'saturation')

def logic_15414(world):
    _world_apply(world, 'snowpack', 'surface_water', 'gap')

def logic_15415(world):
    _world_apply(world, 'snowpack', 'humidity', 'direct')

def logic_15416(world):
    _world_apply(world, 'snowpack', 'cloud', 'square')

def logic_15417(world):
    _world_apply(world, 'snowpack', 'rain', 'saturation')

def logic_15418(world):
    _world_apply(world, 'snowpack', 'soil_moisture', 'gap')

def logic_15419(world):
    _world_apply(world, 'snowpack', 'runoff', 'direct')

def logic_15420(world):
    _world_apply(world, 'snowpack', 'wind_x', 'square')

def logic_15421(world):
    _world_apply(world, 'snowpack', 'wind_y', 'pulse')

def logic_15422(world):
    _world_apply(world, 'snowpack', 'vegetation', 'saturation')

def logic_15423(world):
    _world_apply(world, 'snowpack', 'biomass', 'gap')

def logic_15424(world):
    _world_apply(world, 'snowpack', 'herbivore', 'direct')

def logic_15425(world):
    _world_apply(world, 'snowpack', 'predator', 'pulse')

def logic_15426(world):
    _world_apply(world, 'snowpack', 'carrion', 'saturation')

def logic_15427(world):
    _world_apply(world, 'snowpack', 'nutrients', 'gap')

def logic_15428(world):
    _world_apply(world, 'snowpack', 'decomposition_rate', 'direct')

def logic_15429(world):
    _world_apply(world, 'snowpack', 'oxygen', 'square')

def logic_15430(world):
    _world_apply(world, 'snowpack', 'co2', 'pulse')

def logic_15431(world):
    _world_apply(world, 'snowpack', 'photosynthesis_factor', 'saturation')

def logic_15432(world):
    _world_apply(world, 'snowpack', 'ice', 'gap')

def logic_15433(world):
    _world_apply(world, 'snowpack', 'evaporation', 'square')

def logic_15434(world):
    _world_apply(world, 'snowpack', 'detritus', 'pulse')

def logic_15435(world):
    _world_apply(world, 'snowpack', 'methane', 'saturation')

def logic_15436(world):
    _world_apply(world, 'snowpack', 'pathogen_load', 'gap')

def logic_15437(world):
    _world_apply(world, 'snowpack', 'biodiversity', 'direct')

def logic_15438(world):
    _world_apply(world, 'snowpack', 'habitat_stress', 'square')

def logic_15439(world):
    _world_apply(world, 'snowpack', 'erosion', 'pulse')

def logic_15440(world):
    _world_apply(world, 'snowpack', 'soil_depth', 'saturation')

def logic_15441(world):
    _world_apply(world, 'snowpack', 'root_density', 'direct')

def logic_15442(world):
    _world_apply(world, 'snowpack', 'wetland', 'square')

def logic_15443(world):
    _world_apply(world, 'snowpack', 'carbon_storage', 'pulse')

def logic_15444(world):
    _world_apply(world, 'snowpack', 'fire_risk', 'saturation')

def logic_15445(world):
    _world_apply(world, 'snowpack', 'ash', 'gap')

def logic_15446(world):
    _world_apply(world, 'snowpack', 'groundwater', 'direct')

def logic_15447(world):
    _world_apply(world, 'snowpack', 'sediment', 'square')

def logic_15448(world):
    _world_apply(world, 'snowpack', 'salinity', 'pulse')

def logic_15449(world):
    _world_apply(world, 'snowpack', 'algae', 'gap')

def logic_15450(world):
    _world_apply(world, 'snowpack', 'organic_matter', 'direct')

def logic_15451(world):
    _world_apply(world, 'snowpack', 'deadwood', 'square')

def logic_15452(world):
    _world_apply(world, 'snowpack', 'pollinators', 'pulse')

def logic_15453(world):
    _world_apply(world, 'snowpack', 'flowers', 'saturation')

def logic_15454(world):
    _world_apply(world, 'snowpack', 'seed_bank', 'gap')

def logic_15455(world):
    _world_apply(world, 'snowpack', 'soil_carbon', 'direct')

def logic_15456(world):
    _world_apply(world, 'snowpack', 'surface_ice', 'square')

def logic_15457(world):
    _world_apply(world, 'groundwater', 'temperature', 'saturation')

def logic_15458(world):
    _world_apply(world, 'groundwater', 'surface_water', 'gap')

def logic_15459(world):
    _world_apply(world, 'groundwater', 'humidity', 'direct')

def logic_15460(world):
    _world_apply(world, 'groundwater', 'cloud', 'square')

def logic_15461(world):
    _world_apply(world, 'groundwater', 'rain', 'pulse')

def logic_15462(world):
    _world_apply(world, 'groundwater', 'soil_moisture', 'saturation')

def logic_15463(world):
    _world_apply(world, 'groundwater', 'runoff', 'gap')

def logic_15464(world):
    _world_apply(world, 'groundwater', 'wind_x', 'direct')

def logic_15465(world):
    _world_apply(world, 'groundwater', 'wind_y', 'pulse')

def logic_15466(world):
    _world_apply(world, 'groundwater', 'vegetation', 'saturation')

def logic_15467(world):
    _world_apply(world, 'groundwater', 'biomass', 'gap')

def logic_15468(world):
    _world_apply(world, 'groundwater', 'herbivore', 'direct')

def logic_15469(world):
    _world_apply(world, 'groundwater', 'predator', 'square')

def logic_15470(world):
    _world_apply(world, 'groundwater', 'carrion', 'pulse')

def logic_15471(world):
    _world_apply(world, 'groundwater', 'nutrients', 'saturation')

def logic_15472(world):
    _world_apply(world, 'groundwater', 'decomposition_rate', 'gap')

def logic_15473(world):
    _world_apply(world, 'groundwater', 'oxygen', 'square')

def logic_15474(world):
    _world_apply(world, 'groundwater', 'co2', 'pulse')

def logic_15475(world):
    _world_apply(world, 'groundwater', 'photosynthesis_factor', 'saturation')

def logic_15476(world):
    _world_apply(world, 'groundwater', 'ice', 'gap')

def logic_15477(world):
    _world_apply(world, 'groundwater', 'evaporation', 'direct')

def logic_15478(world):
    _world_apply(world, 'groundwater', 'detritus', 'square')

def logic_15479(world):
    _world_apply(world, 'groundwater', 'methane', 'pulse')

def logic_15480(world):
    _world_apply(world, 'groundwater', 'pathogen_load', 'saturation')

def logic_15481(world):
    _world_apply(world, 'groundwater', 'biodiversity', 'direct')

def logic_15482(world):
    _world_apply(world, 'groundwater', 'habitat_stress', 'square')

def logic_15483(world):
    _world_apply(world, 'groundwater', 'erosion', 'pulse')

def logic_15484(world):
    _world_apply(world, 'groundwater', 'soil_depth', 'saturation')

def logic_15485(world):
    _world_apply(world, 'groundwater', 'root_density', 'gap')

def logic_15486(world):
    _world_apply(world, 'groundwater', 'wetland', 'direct')

def logic_15487(world):
    _world_apply(world, 'groundwater', 'carbon_storage', 'square')

def logic_15488(world):
    _world_apply(world, 'groundwater', 'fire_risk', 'pulse')

def logic_15489(world):
    _world_apply(world, 'groundwater', 'ash', 'gap')

def logic_15490(world):
    _world_apply(world, 'groundwater', 'snowpack', 'direct')

def logic_15491(world):
    _world_apply(world, 'groundwater', 'sediment', 'square')

def logic_15492(world):
    _world_apply(world, 'groundwater', 'salinity', 'pulse')

def logic_15493(world):
    _world_apply(world, 'groundwater', 'algae', 'saturation')

def logic_15494(world):
    _world_apply(world, 'groundwater', 'organic_matter', 'gap')

def logic_15495(world):
    _world_apply(world, 'groundwater', 'deadwood', 'direct')

def logic_15496(world):
    _world_apply(world, 'groundwater', 'pollinators', 'square')

def logic_15497(world):
    _world_apply(world, 'groundwater', 'flowers', 'saturation')

def logic_15498(world):
    _world_apply(world, 'groundwater', 'seed_bank', 'gap')

def logic_15499(world):
    _world_apply(world, 'groundwater', 'soil_carbon', 'direct')

def logic_15500(world):
    _world_apply(world, 'groundwater', 'surface_ice', 'square')

def logic_15501(world):
    _world_apply(world, 'sediment', 'temperature', 'pulse')

def logic_15502(world):
    _world_apply(world, 'sediment', 'surface_water', 'saturation')

def logic_15503(world):
    _world_apply(world, 'sediment', 'humidity', 'gap')

def logic_15504(world):
    _world_apply(world, 'sediment', 'cloud', 'direct')

def logic_15505(world):
    _world_apply(world, 'sediment', 'rain', 'pulse')

def logic_15506(world):
    _world_apply(world, 'sediment', 'soil_moisture', 'saturation')

def logic_15507(world):
    _world_apply(world, 'sediment', 'runoff', 'gap')

def logic_15508(world):
    _world_apply(world, 'sediment', 'wind_x', 'direct')

def logic_15509(world):
    _world_apply(world, 'sediment', 'wind_y', 'square')

def logic_15510(world):
    _world_apply(world, 'sediment', 'vegetation', 'pulse')

def logic_15511(world):
    _world_apply(world, 'sediment', 'biomass', 'saturation')

def logic_15512(world):
    _world_apply(world, 'sediment', 'herbivore', 'gap')

def logic_15513(world):
    _world_apply(world, 'sediment', 'predator', 'square')

def logic_15514(world):
    _world_apply(world, 'sediment', 'carrion', 'pulse')

def logic_15515(world):
    _world_apply(world, 'sediment', 'nutrients', 'saturation')

def logic_15516(world):
    _world_apply(world, 'sediment', 'decomposition_rate', 'gap')

def logic_15517(world):
    _world_apply(world, 'sediment', 'oxygen', 'direct')

def logic_15518(world):
    _world_apply(world, 'sediment', 'co2', 'square')

def logic_15519(world):
    _world_apply(world, 'sediment', 'photosynthesis_factor', 'pulse')

def logic_15520(world):
    _world_apply(world, 'sediment', 'ice', 'saturation')

def logic_15521(world):
    _world_apply(world, 'sediment', 'evaporation', 'direct')

def logic_15522(world):
    _world_apply(world, 'sediment', 'detritus', 'square')

def logic_15523(world):
    _world_apply(world, 'sediment', 'methane', 'pulse')

def logic_15524(world):
    _world_apply(world, 'sediment', 'pathogen_load', 'saturation')

def logic_15525(world):
    _world_apply(world, 'sediment', 'biodiversity', 'gap')

def logic_15526(world):
    _world_apply(world, 'sediment', 'habitat_stress', 'direct')

def logic_15527(world):
    _world_apply(world, 'sediment', 'erosion', 'square')

def logic_15528(world):
    _world_apply(world, 'sediment', 'soil_depth', 'pulse')

def logic_15529(world):
    _world_apply(world, 'sediment', 'root_density', 'gap')

def logic_15530(world):
    _world_apply(world, 'sediment', 'wetland', 'direct')

def logic_15531(world):
    _world_apply(world, 'sediment', 'carbon_storage', 'square')

def logic_15532(world):
    _world_apply(world, 'sediment', 'fire_risk', 'pulse')

def logic_15533(world):
    _world_apply(world, 'sediment', 'ash', 'saturation')

def logic_15534(world):
    _world_apply(world, 'sediment', 'snowpack', 'gap')

def logic_15535(world):
    _world_apply(world, 'sediment', 'groundwater', 'direct')

def logic_15536(world):
    _world_apply(world, 'sediment', 'salinity', 'square')

def logic_15537(world):
    _world_apply(world, 'sediment', 'algae', 'saturation')

def logic_15538(world):
    _world_apply(world, 'sediment', 'organic_matter', 'gap')

def logic_15539(world):
    _world_apply(world, 'sediment', 'deadwood', 'direct')

def logic_15540(world):
    _world_apply(world, 'sediment', 'pollinators', 'square')

def logic_15541(world):
    _world_apply(world, 'sediment', 'flowers', 'pulse')

def logic_15542(world):
    _world_apply(world, 'sediment', 'seed_bank', 'saturation')

def logic_15543(world):
    _world_apply(world, 'sediment', 'soil_carbon', 'gap')

def logic_15544(world):
    _world_apply(world, 'sediment', 'surface_ice', 'direct')

def logic_15545(world):
    _world_apply(world, 'salinity', 'temperature', 'pulse')

def logic_15546(world):
    _world_apply(world, 'salinity', 'surface_water', 'saturation')

def logic_15547(world):
    _world_apply(world, 'salinity', 'humidity', 'gap')

def logic_15548(world):
    _world_apply(world, 'salinity', 'cloud', 'direct')

def logic_15549(world):
    _world_apply(world, 'salinity', 'rain', 'square')

def logic_15550(world):
    _world_apply(world, 'salinity', 'soil_moisture', 'pulse')

def logic_15551(world):
    _world_apply(world, 'salinity', 'runoff', 'saturation')

def logic_15552(world):
    _world_apply(world, 'salinity', 'wind_x', 'gap')

def logic_15553(world):
    _world_apply(world, 'salinity', 'wind_y', 'square')

def logic_15554(world):
    _world_apply(world, 'salinity', 'vegetation', 'pulse')

def logic_15555(world):
    _world_apply(world, 'salinity', 'biomass', 'saturation')

def logic_15556(world):
    _world_apply(world, 'salinity', 'herbivore', 'gap')

def logic_15557(world):
    _world_apply(world, 'salinity', 'predator', 'direct')

def logic_15558(world):
    _world_apply(world, 'salinity', 'carrion', 'square')

def logic_15559(world):
    _world_apply(world, 'salinity', 'nutrients', 'pulse')

def logic_15560(world):
    _world_apply(world, 'salinity', 'decomposition_rate', 'saturation')

def logic_15561(world):
    _world_apply(world, 'salinity', 'oxygen', 'direct')

def logic_15562(world):
    _world_apply(world, 'salinity', 'co2', 'square')

def logic_15563(world):
    _world_apply(world, 'salinity', 'photosynthesis_factor', 'pulse')

def logic_15564(world):
    _world_apply(world, 'salinity', 'ice', 'saturation')

def logic_15565(world):
    _world_apply(world, 'salinity', 'evaporation', 'gap')

def logic_15566(world):
    _world_apply(world, 'salinity', 'detritus', 'direct')

def logic_15567(world):
    _world_apply(world, 'salinity', 'methane', 'square')

def logic_15568(world):
    _world_apply(world, 'salinity', 'pathogen_load', 'pulse')

def logic_15569(world):
    _world_apply(world, 'salinity', 'biodiversity', 'gap')

def logic_15570(world):
    _world_apply(world, 'salinity', 'habitat_stress', 'direct')

def logic_15571(world):
    _world_apply(world, 'salinity', 'erosion', 'square')

def logic_15572(world):
    _world_apply(world, 'salinity', 'soil_depth', 'pulse')

def logic_15573(world):
    _world_apply(world, 'salinity', 'root_density', 'saturation')

def logic_15574(world):
    _world_apply(world, 'salinity', 'wetland', 'gap')

def logic_15575(world):
    _world_apply(world, 'salinity', 'carbon_storage', 'direct')

def logic_15576(world):
    _world_apply(world, 'salinity', 'fire_risk', 'square')

def logic_15577(world):
    _world_apply(world, 'salinity', 'ash', 'saturation')

def logic_15578(world):
    _world_apply(world, 'salinity', 'snowpack', 'gap')

def logic_15579(world):
    _world_apply(world, 'salinity', 'groundwater', 'direct')

def logic_15580(world):
    _world_apply(world, 'salinity', 'sediment', 'square')

def logic_15581(world):
    _world_apply(world, 'salinity', 'algae', 'pulse')

def logic_15582(world):
    _world_apply(world, 'salinity', 'organic_matter', 'saturation')

def logic_15583(world):
    _world_apply(world, 'salinity', 'deadwood', 'gap')

def logic_15584(world):
    _world_apply(world, 'salinity', 'pollinators', 'direct')

def logic_15585(world):
    _world_apply(world, 'salinity', 'flowers', 'pulse')

def logic_15586(world):
    _world_apply(world, 'salinity', 'seed_bank', 'saturation')

def logic_15587(world):
    _world_apply(world, 'salinity', 'soil_carbon', 'gap')

def logic_15588(world):
    _world_apply(world, 'salinity', 'surface_ice', 'direct')

def logic_15589(world):
    _world_apply(world, 'algae', 'temperature', 'square')

def logic_15590(world):
    _world_apply(world, 'algae', 'surface_water', 'pulse')

def logic_15591(world):
    _world_apply(world, 'algae', 'humidity', 'saturation')

def logic_15592(world):
    _world_apply(world, 'algae', 'cloud', 'gap')

def logic_15593(world):
    _world_apply(world, 'algae', 'rain', 'square')

def logic_15594(world):
    _world_apply(world, 'algae', 'soil_moisture', 'pulse')

def logic_15595(world):
    _world_apply(world, 'algae', 'runoff', 'saturation')

def logic_15596(world):
    _world_apply(world, 'algae', 'wind_x', 'gap')

def logic_15597(world):
    _world_apply(world, 'algae', 'wind_y', 'direct')

def logic_15598(world):
    _world_apply(world, 'algae', 'vegetation', 'square')

def logic_15599(world):
    _world_apply(world, 'algae', 'biomass', 'pulse')

def logic_15600(world):
    _world_apply(world, 'algae', 'herbivore', 'saturation')

def logic_15601(world):
    _world_apply(world, 'algae', 'predator', 'direct')

def logic_15602(world):
    _world_apply(world, 'algae', 'carrion', 'square')

def logic_15603(world):
    _world_apply(world, 'algae', 'nutrients', 'pulse')

def logic_15604(world):
    _world_apply(world, 'algae', 'decomposition_rate', 'saturation')

def logic_15605(world):
    _world_apply(world, 'algae', 'oxygen', 'gap')

def logic_15606(world):
    _world_apply(world, 'algae', 'co2', 'direct')

def logic_15607(world):
    _world_apply(world, 'algae', 'photosynthesis_factor', 'square')

def logic_15608(world):
    _world_apply(world, 'algae', 'ice', 'pulse')

def logic_15609(world):
    _world_apply(world, 'algae', 'evaporation', 'gap')

def logic_15610(world):
    _world_apply(world, 'algae', 'detritus', 'direct')

def logic_15611(world):
    _world_apply(world, 'algae', 'methane', 'square')

def logic_15612(world):
    _world_apply(world, 'algae', 'pathogen_load', 'pulse')

def logic_15613(world):
    _world_apply(world, 'algae', 'biodiversity', 'saturation')

def logic_15614(world):
    _world_apply(world, 'algae', 'habitat_stress', 'gap')

def logic_15615(world):
    _world_apply(world, 'algae', 'erosion', 'direct')

def logic_15616(world):
    _world_apply(world, 'algae', 'soil_depth', 'square')

def logic_15617(world):
    _world_apply(world, 'algae', 'root_density', 'saturation')

def logic_15618(world):
    _world_apply(world, 'algae', 'wetland', 'gap')

def logic_15619(world):
    _world_apply(world, 'algae', 'carbon_storage', 'direct')

def logic_15620(world):
    _world_apply(world, 'algae', 'fire_risk', 'square')

def logic_15621(world):
    _world_apply(world, 'algae', 'ash', 'pulse')

def logic_15622(world):
    _world_apply(world, 'algae', 'snowpack', 'saturation')

def logic_15623(world):
    _world_apply(world, 'algae', 'groundwater', 'gap')

def logic_15624(world):
    _world_apply(world, 'algae', 'sediment', 'direct')

def logic_15625(world):
    _world_apply(world, 'algae', 'salinity', 'pulse')

def logic_15626(world):
    _world_apply(world, 'algae', 'organic_matter', 'saturation')

def logic_15627(world):
    _world_apply(world, 'algae', 'deadwood', 'gap')

def logic_15628(world):
    _world_apply(world, 'algae', 'pollinators', 'direct')

def logic_15629(world):
    _world_apply(world, 'algae', 'flowers', 'square')

def logic_15630(world):
    _world_apply(world, 'algae', 'seed_bank', 'pulse')

def logic_15631(world):
    _world_apply(world, 'algae', 'soil_carbon', 'saturation')

def logic_15632(world):
    _world_apply(world, 'algae', 'surface_ice', 'gap')

def logic_15633(world):
    _world_apply(world, 'organic_matter', 'temperature', 'square')

def logic_15634(world):
    _world_apply(world, 'organic_matter', 'surface_water', 'pulse')

def logic_15635(world):
    _world_apply(world, 'organic_matter', 'humidity', 'saturation')

def logic_15636(world):
    _world_apply(world, 'organic_matter', 'cloud', 'gap')

def logic_15637(world):
    _world_apply(world, 'organic_matter', 'rain', 'direct')

def logic_15638(world):
    _world_apply(world, 'organic_matter', 'soil_moisture', 'square')

def logic_15639(world):
    _world_apply(world, 'organic_matter', 'runoff', 'pulse')

def logic_15640(world):
    _world_apply(world, 'organic_matter', 'wind_x', 'saturation')

def logic_15641(world):
    _world_apply(world, 'organic_matter', 'wind_y', 'direct')

def logic_15642(world):
    _world_apply(world, 'organic_matter', 'vegetation', 'square')

def logic_15643(world):
    _world_apply(world, 'organic_matter', 'biomass', 'pulse')

def logic_15644(world):
    _world_apply(world, 'organic_matter', 'herbivore', 'saturation')

def logic_15645(world):
    _world_apply(world, 'organic_matter', 'predator', 'gap')

def logic_15646(world):
    _world_apply(world, 'organic_matter', 'carrion', 'direct')

def logic_15647(world):
    _world_apply(world, 'organic_matter', 'nutrients', 'square')

def logic_15648(world):
    _world_apply(world, 'organic_matter', 'decomposition_rate', 'pulse')

def logic_15649(world):
    _world_apply(world, 'organic_matter', 'oxygen', 'gap')

def logic_15650(world):
    _world_apply(world, 'organic_matter', 'co2', 'direct')

def logic_15651(world):
    _world_apply(world, 'organic_matter', 'photosynthesis_factor', 'square')

def logic_15652(world):
    _world_apply(world, 'organic_matter', 'ice', 'pulse')

def logic_15653(world):
    _world_apply(world, 'organic_matter', 'evaporation', 'saturation')

def logic_15654(world):
    _world_apply(world, 'organic_matter', 'detritus', 'gap')

def logic_15655(world):
    _world_apply(world, 'organic_matter', 'methane', 'direct')

def logic_15656(world):
    _world_apply(world, 'organic_matter', 'pathogen_load', 'square')

def logic_15657(world):
    _world_apply(world, 'organic_matter', 'biodiversity', 'saturation')

def logic_15658(world):
    _world_apply(world, 'organic_matter', 'habitat_stress', 'gap')

def logic_15659(world):
    _world_apply(world, 'organic_matter', 'erosion', 'direct')

def logic_15660(world):
    _world_apply(world, 'organic_matter', 'soil_depth', 'square')

def logic_15661(world):
    _world_apply(world, 'organic_matter', 'root_density', 'pulse')

def logic_15662(world):
    _world_apply(world, 'organic_matter', 'wetland', 'saturation')

def logic_15663(world):
    _world_apply(world, 'organic_matter', 'carbon_storage', 'gap')

def logic_15664(world):
    _world_apply(world, 'organic_matter', 'fire_risk', 'direct')

def logic_15665(world):
    _world_apply(world, 'organic_matter', 'ash', 'pulse')

def logic_15666(world):
    _world_apply(world, 'organic_matter', 'snowpack', 'saturation')

def logic_15667(world):
    _world_apply(world, 'organic_matter', 'groundwater', 'gap')

def logic_15668(world):
    _world_apply(world, 'organic_matter', 'sediment', 'direct')

def logic_15669(world):
    _world_apply(world, 'organic_matter', 'salinity', 'square')

def logic_15670(world):
    _world_apply(world, 'organic_matter', 'algae', 'pulse')

def logic_15671(world):
    _world_apply(world, 'organic_matter', 'deadwood', 'saturation')

def logic_15672(world):
    _world_apply(world, 'organic_matter', 'pollinators', 'gap')

def logic_15673(world):
    _world_apply(world, 'organic_matter', 'flowers', 'square')

def logic_15674(world):
    _world_apply(world, 'organic_matter', 'seed_bank', 'pulse')

def logic_15675(world):
    _world_apply(world, 'organic_matter', 'soil_carbon', 'saturation')

def logic_15676(world):
    _world_apply(world, 'organic_matter', 'surface_ice', 'gap')

def logic_15677(world):
    _world_apply(world, 'deadwood', 'temperature', 'direct')

def logic_15678(world):
    _world_apply(world, 'deadwood', 'surface_water', 'square')

def logic_15679(world):
    _world_apply(world, 'deadwood', 'humidity', 'pulse')

def logic_15680(world):
    _world_apply(world, 'deadwood', 'cloud', 'saturation')

def logic_15681(world):
    _world_apply(world, 'deadwood', 'rain', 'direct')

def logic_15682(world):
    _world_apply(world, 'deadwood', 'soil_moisture', 'square')

def logic_15683(world):
    _world_apply(world, 'deadwood', 'runoff', 'pulse')

def logic_15684(world):
    _world_apply(world, 'deadwood', 'wind_x', 'saturation')

def logic_15685(world):
    _world_apply(world, 'deadwood', 'wind_y', 'gap')

def logic_15686(world):
    _world_apply(world, 'deadwood', 'vegetation', 'direct')

def logic_15687(world):
    _world_apply(world, 'deadwood', 'biomass', 'square')

def logic_15688(world):
    _world_apply(world, 'deadwood', 'herbivore', 'pulse')

def logic_15689(world):
    _world_apply(world, 'deadwood', 'predator', 'gap')

def logic_15690(world):
    _world_apply(world, 'deadwood', 'carrion', 'direct')

def logic_15691(world):
    _world_apply(world, 'deadwood', 'nutrients', 'square')

def logic_15692(world):
    _world_apply(world, 'deadwood', 'decomposition_rate', 'pulse')

def logic_15693(world):
    _world_apply(world, 'deadwood', 'oxygen', 'saturation')

def logic_15694(world):
    _world_apply(world, 'deadwood', 'co2', 'gap')

def logic_15695(world):
    _world_apply(world, 'deadwood', 'photosynthesis_factor', 'direct')

def logic_15696(world):
    _world_apply(world, 'deadwood', 'ice', 'square')

def logic_15697(world):
    _world_apply(world, 'deadwood', 'evaporation', 'saturation')

def logic_15698(world):
    _world_apply(world, 'deadwood', 'detritus', 'gap')

def logic_15699(world):
    _world_apply(world, 'deadwood', 'methane', 'direct')

def logic_15700(world):
    _world_apply(world, 'deadwood', 'pathogen_load', 'square')

def logic_15701(world):
    _world_apply(world, 'deadwood', 'biodiversity', 'pulse')

def logic_15702(world):
    _world_apply(world, 'deadwood', 'habitat_stress', 'saturation')

def logic_15703(world):
    _world_apply(world, 'deadwood', 'erosion', 'gap')

def logic_15704(world):
    _world_apply(world, 'deadwood', 'soil_depth', 'direct')

def logic_15705(world):
    _world_apply(world, 'deadwood', 'root_density', 'pulse')

def logic_15706(world):
    _world_apply(world, 'deadwood', 'wetland', 'saturation')

def logic_15707(world):
    _world_apply(world, 'deadwood', 'carbon_storage', 'gap')

def logic_15708(world):
    _world_apply(world, 'deadwood', 'fire_risk', 'direct')

def logic_15709(world):
    _world_apply(world, 'deadwood', 'ash', 'square')

def logic_15710(world):
    _world_apply(world, 'deadwood', 'snowpack', 'pulse')

def logic_15711(world):
    _world_apply(world, 'deadwood', 'groundwater', 'saturation')

def logic_15712(world):
    _world_apply(world, 'deadwood', 'sediment', 'gap')

def logic_15713(world):
    _world_apply(world, 'deadwood', 'salinity', 'square')

def logic_15714(world):
    _world_apply(world, 'deadwood', 'algae', 'pulse')

def logic_15715(world):
    _world_apply(world, 'deadwood', 'organic_matter', 'saturation')

def logic_15716(world):
    _world_apply(world, 'deadwood', 'pollinators', 'gap')

def logic_15717(world):
    _world_apply(world, 'deadwood', 'flowers', 'direct')

def logic_15718(world):
    _world_apply(world, 'deadwood', 'seed_bank', 'square')

def logic_15719(world):
    _world_apply(world, 'deadwood', 'soil_carbon', 'pulse')

def logic_15720(world):
    _world_apply(world, 'deadwood', 'surface_ice', 'saturation')

def logic_15721(world):
    _world_apply(world, 'pollinators', 'temperature', 'direct')

def logic_15722(world):
    _world_apply(world, 'pollinators', 'surface_water', 'square')

def logic_15723(world):
    _world_apply(world, 'pollinators', 'humidity', 'pulse')

def logic_15724(world):
    _world_apply(world, 'pollinators', 'cloud', 'saturation')

def logic_15725(world):
    _world_apply(world, 'pollinators', 'rain', 'gap')

def logic_15726(world):
    _world_apply(world, 'pollinators', 'soil_moisture', 'direct')

def logic_15727(world):
    _world_apply(world, 'pollinators', 'runoff', 'square')

def logic_15728(world):
    _world_apply(world, 'pollinators', 'wind_x', 'pulse')

def logic_15729(world):
    _world_apply(world, 'pollinators', 'wind_y', 'gap')

def logic_15730(world):
    _world_apply(world, 'pollinators', 'vegetation', 'direct')

def logic_15731(world):
    _world_apply(world, 'pollinators', 'biomass', 'square')

def logic_15732(world):
    _world_apply(world, 'pollinators', 'herbivore', 'pulse')

def logic_15733(world):
    _world_apply(world, 'pollinators', 'predator', 'saturation')

def logic_15734(world):
    _world_apply(world, 'pollinators', 'carrion', 'gap')

def logic_15735(world):
    _world_apply(world, 'pollinators', 'nutrients', 'direct')

def logic_15736(world):
    _world_apply(world, 'pollinators', 'decomposition_rate', 'square')

def logic_15737(world):
    _world_apply(world, 'pollinators', 'oxygen', 'saturation')

def logic_15738(world):
    _world_apply(world, 'pollinators', 'co2', 'gap')

def logic_15739(world):
    _world_apply(world, 'pollinators', 'photosynthesis_factor', 'direct')

def logic_15740(world):
    _world_apply(world, 'pollinators', 'ice', 'square')

def logic_15741(world):
    _world_apply(world, 'pollinators', 'evaporation', 'pulse')

def logic_15742(world):
    _world_apply(world, 'pollinators', 'detritus', 'saturation')

def logic_15743(world):
    _world_apply(world, 'pollinators', 'methane', 'gap')

def logic_15744(world):
    _world_apply(world, 'pollinators', 'pathogen_load', 'direct')

def logic_15745(world):
    _world_apply(world, 'pollinators', 'biodiversity', 'pulse')

def logic_15746(world):
    _world_apply(world, 'pollinators', 'habitat_stress', 'saturation')

def logic_15747(world):
    _world_apply(world, 'pollinators', 'erosion', 'gap')

def logic_15748(world):
    _world_apply(world, 'pollinators', 'soil_depth', 'direct')

def logic_15749(world):
    _world_apply(world, 'pollinators', 'root_density', 'square')

def logic_15750(world):
    _world_apply(world, 'pollinators', 'wetland', 'pulse')

def logic_15751(world):
    _world_apply(world, 'pollinators', 'carbon_storage', 'saturation')

def logic_15752(world):
    _world_apply(world, 'pollinators', 'fire_risk', 'gap')

def logic_15753(world):
    _world_apply(world, 'pollinators', 'ash', 'square')

def logic_15754(world):
    _world_apply(world, 'pollinators', 'snowpack', 'pulse')

def logic_15755(world):
    _world_apply(world, 'pollinators', 'groundwater', 'saturation')

def logic_15756(world):
    _world_apply(world, 'pollinators', 'sediment', 'gap')

def logic_15757(world):
    _world_apply(world, 'pollinators', 'salinity', 'direct')

def logic_15758(world):
    _world_apply(world, 'pollinators', 'algae', 'square')

def logic_15759(world):
    _world_apply(world, 'pollinators', 'organic_matter', 'pulse')

def logic_15760(world):
    _world_apply(world, 'pollinators', 'deadwood', 'saturation')

def logic_15761(world):
    _world_apply(world, 'pollinators', 'flowers', 'direct')

def logic_15762(world):
    _world_apply(world, 'pollinators', 'seed_bank', 'square')

def logic_15763(world):
    _world_apply(world, 'pollinators', 'soil_carbon', 'pulse')

def logic_15764(world):
    _world_apply(world, 'pollinators', 'surface_ice', 'saturation')

def logic_15765(world):
    _world_apply(world, 'flowers', 'temperature', 'gap')

def logic_15766(world):
    _world_apply(world, 'flowers', 'surface_water', 'direct')

def logic_15767(world):
    _world_apply(world, 'flowers', 'humidity', 'square')

def logic_15768(world):
    _world_apply(world, 'flowers', 'cloud', 'pulse')

def logic_15769(world):
    _world_apply(world, 'flowers', 'rain', 'gap')

def logic_15770(world):
    _world_apply(world, 'flowers', 'soil_moisture', 'direct')

def logic_15771(world):
    _world_apply(world, 'flowers', 'runoff', 'square')

def logic_15772(world):
    _world_apply(world, 'flowers', 'wind_x', 'pulse')

def logic_15773(world):
    _world_apply(world, 'flowers', 'wind_y', 'saturation')

def logic_15774(world):
    _world_apply(world, 'flowers', 'vegetation', 'gap')

def logic_15775(world):
    _world_apply(world, 'flowers', 'biomass', 'direct')

def logic_15776(world):
    _world_apply(world, 'flowers', 'herbivore', 'square')

def logic_15777(world):
    _world_apply(world, 'flowers', 'predator', 'saturation')

def logic_15778(world):
    _world_apply(world, 'flowers', 'carrion', 'gap')

def logic_15779(world):
    _world_apply(world, 'flowers', 'nutrients', 'direct')

def logic_15780(world):
    _world_apply(world, 'flowers', 'decomposition_rate', 'square')

def logic_15781(world):
    _world_apply(world, 'flowers', 'oxygen', 'pulse')

def logic_15782(world):
    _world_apply(world, 'flowers', 'co2', 'saturation')

def logic_15783(world):
    _world_apply(world, 'flowers', 'photosynthesis_factor', 'gap')

def logic_15784(world):
    _world_apply(world, 'flowers', 'ice', 'direct')

def logic_15785(world):
    _world_apply(world, 'flowers', 'evaporation', 'pulse')

def logic_15786(world):
    _world_apply(world, 'flowers', 'detritus', 'saturation')

def logic_15787(world):
    _world_apply(world, 'flowers', 'methane', 'gap')

def logic_15788(world):
    _world_apply(world, 'flowers', 'pathogen_load', 'direct')

def logic_15789(world):
    _world_apply(world, 'flowers', 'biodiversity', 'square')

def logic_15790(world):
    _world_apply(world, 'flowers', 'habitat_stress', 'pulse')

def logic_15791(world):
    _world_apply(world, 'flowers', 'erosion', 'saturation')

def logic_15792(world):
    _world_apply(world, 'flowers', 'soil_depth', 'gap')

def logic_15793(world):
    _world_apply(world, 'flowers', 'root_density', 'square')

def logic_15794(world):
    _world_apply(world, 'flowers', 'wetland', 'pulse')

def logic_15795(world):
    _world_apply(world, 'flowers', 'carbon_storage', 'saturation')

def logic_15796(world):
    _world_apply(world, 'flowers', 'fire_risk', 'gap')

def logic_15797(world):
    _world_apply(world, 'flowers', 'ash', 'direct')

def logic_15798(world):
    _world_apply(world, 'flowers', 'snowpack', 'square')

def logic_15799(world):
    _world_apply(world, 'flowers', 'groundwater', 'pulse')

def logic_15800(world):
    _world_apply(world, 'flowers', 'sediment', 'saturation')

def logic_15801(world):
    _world_apply(world, 'flowers', 'salinity', 'direct')

def logic_15802(world):
    _world_apply(world, 'flowers', 'algae', 'square')

def logic_15803(world):
    _world_apply(world, 'flowers', 'organic_matter', 'pulse')

def logic_15804(world):
    _world_apply(world, 'flowers', 'deadwood', 'saturation')

def logic_15805(world):
    _world_apply(world, 'flowers', 'pollinators', 'gap')

def logic_15806(world):
    _world_apply(world, 'flowers', 'seed_bank', 'direct')

def logic_15807(world):
    _world_apply(world, 'flowers', 'soil_carbon', 'square')

def logic_15808(world):
    _world_apply(world, 'flowers', 'surface_ice', 'pulse')

def logic_15809(world):
    _world_apply(world, 'seed_bank', 'temperature', 'gap')

def logic_15810(world):
    _world_apply(world, 'seed_bank', 'surface_water', 'direct')

def logic_15811(world):
    _world_apply(world, 'seed_bank', 'humidity', 'square')

def logic_15812(world):
    _world_apply(world, 'seed_bank', 'cloud', 'pulse')

def logic_15813(world):
    _world_apply(world, 'seed_bank', 'rain', 'saturation')

def logic_15814(world):
    _world_apply(world, 'seed_bank', 'soil_moisture', 'gap')

def logic_15815(world):
    _world_apply(world, 'seed_bank', 'runoff', 'direct')

def logic_15816(world):
    _world_apply(world, 'seed_bank', 'wind_x', 'square')

def logic_15817(world):
    _world_apply(world, 'seed_bank', 'wind_y', 'saturation')

def logic_15818(world):
    _world_apply(world, 'seed_bank', 'vegetation', 'gap')

def logic_15819(world):
    _world_apply(world, 'seed_bank', 'biomass', 'direct')

def logic_15820(world):
    _world_apply(world, 'seed_bank', 'herbivore', 'square')

def logic_15821(world):
    _world_apply(world, 'seed_bank', 'predator', 'pulse')

def logic_15822(world):
    _world_apply(world, 'seed_bank', 'carrion', 'saturation')

def logic_15823(world):
    _world_apply(world, 'seed_bank', 'nutrients', 'gap')

def logic_15824(world):
    _world_apply(world, 'seed_bank', 'decomposition_rate', 'direct')

def logic_15825(world):
    _world_apply(world, 'seed_bank', 'oxygen', 'pulse')

def logic_15826(world):
    _world_apply(world, 'seed_bank', 'co2', 'saturation')

def logic_15827(world):
    _world_apply(world, 'seed_bank', 'photosynthesis_factor', 'gap')

def logic_15828(world):
    _world_apply(world, 'seed_bank', 'ice', 'direct')

def logic_15829(world):
    _world_apply(world, 'seed_bank', 'evaporation', 'square')

def logic_15830(world):
    _world_apply(world, 'seed_bank', 'detritus', 'pulse')

def logic_15831(world):
    _world_apply(world, 'seed_bank', 'methane', 'saturation')

def logic_15832(world):
    _world_apply(world, 'seed_bank', 'pathogen_load', 'gap')

def logic_15833(world):
    _world_apply(world, 'seed_bank', 'biodiversity', 'square')

def logic_15834(world):
    _world_apply(world, 'seed_bank', 'habitat_stress', 'pulse')

def logic_15835(world):
    _world_apply(world, 'seed_bank', 'erosion', 'saturation')

def logic_15836(world):
    _world_apply(world, 'seed_bank', 'soil_depth', 'gap')

def logic_15837(world):
    _world_apply(world, 'seed_bank', 'root_density', 'direct')

def logic_15838(world):
    _world_apply(world, 'seed_bank', 'wetland', 'square')

def logic_15839(world):
    _world_apply(world, 'seed_bank', 'carbon_storage', 'pulse')

def logic_15840(world):
    _world_apply(world, 'seed_bank', 'fire_risk', 'saturation')

def logic_15841(world):
    _world_apply(world, 'seed_bank', 'ash', 'direct')

def logic_15842(world):
    _world_apply(world, 'seed_bank', 'snowpack', 'square')

def logic_15843(world):
    _world_apply(world, 'seed_bank', 'groundwater', 'pulse')

def logic_15844(world):
    _world_apply(world, 'seed_bank', 'sediment', 'saturation')

def logic_15845(world):
    _world_apply(world, 'seed_bank', 'salinity', 'gap')

def logic_15846(world):
    _world_apply(world, 'seed_bank', 'algae', 'direct')

def logic_15847(world):
    _world_apply(world, 'seed_bank', 'organic_matter', 'square')

def logic_15848(world):
    _world_apply(world, 'seed_bank', 'deadwood', 'pulse')

def logic_15849(world):
    _world_apply(world, 'seed_bank', 'pollinators', 'gap')

def logic_15850(world):
    _world_apply(world, 'seed_bank', 'flowers', 'direct')

def logic_15851(world):
    _world_apply(world, 'seed_bank', 'soil_carbon', 'square')

def logic_15852(world):
    _world_apply(world, 'seed_bank', 'surface_ice', 'pulse')

def logic_15853(world):
    _world_apply(world, 'soil_carbon', 'temperature', 'saturation')

def logic_15854(world):
    _world_apply(world, 'soil_carbon', 'surface_water', 'gap')

def logic_15855(world):
    _world_apply(world, 'soil_carbon', 'humidity', 'direct')

def logic_15856(world):
    _world_apply(world, 'soil_carbon', 'cloud', 'square')

def logic_15857(world):
    _world_apply(world, 'soil_carbon', 'rain', 'saturation')

def logic_15858(world):
    _world_apply(world, 'soil_carbon', 'soil_moisture', 'gap')

def logic_15859(world):
    _world_apply(world, 'soil_carbon', 'runoff', 'direct')

def logic_15860(world):
    _world_apply(world, 'soil_carbon', 'wind_x', 'square')

def logic_15861(world):
    _world_apply(world, 'soil_carbon', 'wind_y', 'pulse')

def logic_15862(world):
    _world_apply(world, 'soil_carbon', 'vegetation', 'saturation')

def logic_15863(world):
    _world_apply(world, 'soil_carbon', 'biomass', 'gap')

def logic_15864(world):
    _world_apply(world, 'soil_carbon', 'herbivore', 'direct')

def logic_15865(world):
    _world_apply(world, 'soil_carbon', 'predator', 'pulse')

def logic_15866(world):
    _world_apply(world, 'soil_carbon', 'carrion', 'saturation')

def logic_15867(world):
    _world_apply(world, 'soil_carbon', 'nutrients', 'gap')

def logic_15868(world):
    _world_apply(world, 'soil_carbon', 'decomposition_rate', 'direct')

def logic_15869(world):
    _world_apply(world, 'soil_carbon', 'oxygen', 'square')

def logic_15870(world):
    _world_apply(world, 'soil_carbon', 'co2', 'pulse')

def logic_15871(world):
    _world_apply(world, 'soil_carbon', 'photosynthesis_factor', 'saturation')

def logic_15872(world):
    _world_apply(world, 'soil_carbon', 'ice', 'gap')

def logic_15873(world):
    _world_apply(world, 'soil_carbon', 'evaporation', 'square')

def logic_15874(world):
    _world_apply(world, 'soil_carbon', 'detritus', 'pulse')

def logic_15875(world):
    _world_apply(world, 'soil_carbon', 'methane', 'saturation')

def logic_15876(world):
    _world_apply(world, 'soil_carbon', 'pathogen_load', 'gap')

def logic_15877(world):
    _world_apply(world, 'soil_carbon', 'biodiversity', 'direct')

def logic_15878(world):
    _world_apply(world, 'soil_carbon', 'habitat_stress', 'square')

def logic_15879(world):
    _world_apply(world, 'soil_carbon', 'erosion', 'pulse')

def logic_15880(world):
    _world_apply(world, 'soil_carbon', 'soil_depth', 'saturation')

def logic_15881(world):
    _world_apply(world, 'soil_carbon', 'root_density', 'direct')

def logic_15882(world):
    _world_apply(world, 'soil_carbon', 'wetland', 'square')

def logic_15883(world):
    _world_apply(world, 'soil_carbon', 'carbon_storage', 'pulse')

def logic_15884(world):
    _world_apply(world, 'soil_carbon', 'fire_risk', 'saturation')

def logic_15885(world):
    _world_apply(world, 'soil_carbon', 'ash', 'gap')

def logic_15886(world):
    _world_apply(world, 'soil_carbon', 'snowpack', 'direct')

def logic_15887(world):
    _world_apply(world, 'soil_carbon', 'groundwater', 'square')

def logic_15888(world):
    _world_apply(world, 'soil_carbon', 'sediment', 'pulse')

def logic_15889(world):
    _world_apply(world, 'soil_carbon', 'salinity', 'gap')

def logic_15890(world):
    _world_apply(world, 'soil_carbon', 'algae', 'direct')

def logic_15891(world):
    _world_apply(world, 'soil_carbon', 'organic_matter', 'square')

def logic_15892(world):
    _world_apply(world, 'soil_carbon', 'deadwood', 'pulse')

def logic_15893(world):
    _world_apply(world, 'soil_carbon', 'pollinators', 'saturation')

def logic_15894(world):
    _world_apply(world, 'soil_carbon', 'flowers', 'gap')

def logic_15895(world):
    _world_apply(world, 'soil_carbon', 'seed_bank', 'direct')

def logic_15896(world):
    _world_apply(world, 'soil_carbon', 'surface_ice', 'square')

def logic_15897(world):
    _world_apply(world, 'surface_ice', 'temperature', 'saturation')

def logic_15898(world):
    _world_apply(world, 'surface_ice', 'surface_water', 'gap')

def logic_15899(world):
    _world_apply(world, 'surface_ice', 'humidity', 'direct')

def logic_15900(world):
    _world_apply(world, 'surface_ice', 'cloud', 'square')

def logic_15901(world):
    _world_apply(world, 'surface_ice', 'rain', 'pulse')

def logic_15902(world):
    _world_apply(world, 'surface_ice', 'soil_moisture', 'saturation')

def logic_15903(world):
    _world_apply(world, 'surface_ice', 'runoff', 'gap')

def logic_15904(world):
    _world_apply(world, 'surface_ice', 'wind_x', 'direct')

def logic_15905(world):
    _world_apply(world, 'surface_ice', 'wind_y', 'pulse')

def logic_15906(world):
    _world_apply(world, 'surface_ice', 'vegetation', 'saturation')

def logic_15907(world):
    _world_apply(world, 'surface_ice', 'biomass', 'gap')

def logic_15908(world):
    _world_apply(world, 'surface_ice', 'herbivore', 'direct')

def logic_15909(world):
    _world_apply(world, 'surface_ice', 'predator', 'square')

def logic_15910(world):
    _world_apply(world, 'surface_ice', 'carrion', 'pulse')

def logic_15911(world):
    _world_apply(world, 'surface_ice', 'nutrients', 'saturation')

def logic_15912(world):
    _world_apply(world, 'surface_ice', 'decomposition_rate', 'gap')

def logic_15913(world):
    _world_apply(world, 'surface_ice', 'oxygen', 'square')

def logic_15914(world):
    _world_apply(world, 'surface_ice', 'co2', 'pulse')

def logic_15915(world):
    _world_apply(world, 'surface_ice', 'photosynthesis_factor', 'saturation')

def logic_15916(world):
    _world_apply(world, 'surface_ice', 'ice', 'gap')

def logic_15917(world):
    _world_apply(world, 'surface_ice', 'evaporation', 'direct')

def logic_15918(world):
    _world_apply(world, 'surface_ice', 'detritus', 'square')

def logic_15919(world):
    _world_apply(world, 'surface_ice', 'methane', 'pulse')

def logic_15920(world):
    _world_apply(world, 'surface_ice', 'pathogen_load', 'saturation')

def logic_15921(world):
    _world_apply(world, 'surface_ice', 'biodiversity', 'direct')

def logic_15922(world):
    _world_apply(world, 'surface_ice', 'habitat_stress', 'square')

def logic_15923(world):
    _world_apply(world, 'surface_ice', 'erosion', 'pulse')

def logic_15924(world):
    _world_apply(world, 'surface_ice', 'soil_depth', 'saturation')

def logic_15925(world):
    _world_apply(world, 'surface_ice', 'root_density', 'gap')

def logic_15926(world):
    _world_apply(world, 'surface_ice', 'wetland', 'direct')

def logic_15927(world):
    _world_apply(world, 'surface_ice', 'carbon_storage', 'square')

def logic_15928(world):
    _world_apply(world, 'surface_ice', 'fire_risk', 'pulse')

def logic_15929(world):
    _world_apply(world, 'surface_ice', 'ash', 'gap')

def logic_15930(world):
    _world_apply(world, 'surface_ice', 'snowpack', 'direct')

def logic_15931(world):
    _world_apply(world, 'surface_ice', 'groundwater', 'square')

def logic_15932(world):
    _world_apply(world, 'surface_ice', 'sediment', 'pulse')

def logic_15933(world):
    _world_apply(world, 'surface_ice', 'salinity', 'saturation')

def logic_15934(world):
    _world_apply(world, 'surface_ice', 'algae', 'gap')

def logic_15935(world):
    _world_apply(world, 'surface_ice', 'organic_matter', 'direct')

def logic_15936(world):
    _world_apply(world, 'surface_ice', 'deadwood', 'square')

def logic_15937(world):
    _world_apply(world, 'surface_ice', 'pollinators', 'saturation')

def logic_15938(world):
    _world_apply(world, 'surface_ice', 'flowers', 'gap')

def logic_15939(world):
    _world_apply(world, 'surface_ice', 'seed_bank', 'direct')

def logic_15940(world):
    _world_apply(world, 'surface_ice', 'soil_carbon', 'square')

def logic_15941(world):
    _world_apply(world, 'temperature', 'surface_water', 'pulse')

def logic_15942(world):
    _world_apply(world, 'temperature', 'humidity', 'saturation')

def logic_15943(world):
    _world_apply(world, 'temperature', 'cloud', 'gap')

def logic_15944(world):
    _world_apply(world, 'temperature', 'rain', 'direct')

def logic_15945(world):
    _world_apply(world, 'temperature', 'soil_moisture', 'pulse')

def logic_15946(world):
    _world_apply(world, 'temperature', 'runoff', 'saturation')

def logic_15947(world):
    _world_apply(world, 'temperature', 'wind_x', 'gap')

def logic_15948(world):
    _world_apply(world, 'temperature', 'wind_y', 'direct')

def logic_15949(world):
    _world_apply(world, 'temperature', 'vegetation', 'square')

def logic_15950(world):
    _world_apply(world, 'temperature', 'biomass', 'pulse')

def logic_15951(world):
    _world_apply(world, 'temperature', 'herbivore', 'saturation')

def logic_15952(world):
    _world_apply(world, 'temperature', 'predator', 'gap')

def logic_15953(world):
    _world_apply(world, 'temperature', 'carrion', 'square')

def logic_15954(world):
    _world_apply(world, 'temperature', 'nutrients', 'pulse')

def logic_15955(world):
    _world_apply(world, 'temperature', 'decomposition_rate', 'saturation')

def logic_15956(world):
    _world_apply(world, 'temperature', 'oxygen', 'gap')

def logic_15957(world):
    _world_apply(world, 'temperature', 'co2', 'direct')

def logic_15958(world):
    _world_apply(world, 'temperature', 'photosynthesis_factor', 'square')

def logic_15959(world):
    _world_apply(world, 'temperature', 'ice', 'pulse')

def logic_15960(world):
    _world_apply(world, 'temperature', 'evaporation', 'saturation')

def logic_15961(world):
    _world_apply(world, 'temperature', 'detritus', 'direct')

def logic_15962(world):
    _world_apply(world, 'temperature', 'methane', 'square')

def logic_15963(world):
    _world_apply(world, 'temperature', 'pathogen_load', 'pulse')

def logic_15964(world):
    _world_apply(world, 'temperature', 'biodiversity', 'saturation')

def logic_15965(world):
    _world_apply(world, 'temperature', 'habitat_stress', 'gap')

def logic_15966(world):
    _world_apply(world, 'temperature', 'erosion', 'direct')

def logic_15967(world):
    _world_apply(world, 'temperature', 'soil_depth', 'square')

def logic_15968(world):
    _world_apply(world, 'temperature', 'root_density', 'pulse')

def logic_15969(world):
    _world_apply(world, 'temperature', 'wetland', 'gap')

def logic_15970(world):
    _world_apply(world, 'temperature', 'carbon_storage', 'direct')

def logic_15971(world):
    _world_apply(world, 'temperature', 'fire_risk', 'square')

def logic_15972(world):
    _world_apply(world, 'temperature', 'ash', 'pulse')

def logic_15973(world):
    _world_apply(world, 'temperature', 'snowpack', 'saturation')

def logic_15974(world):
    _world_apply(world, 'temperature', 'groundwater', 'gap')

def logic_15975(world):
    _world_apply(world, 'temperature', 'sediment', 'direct')

def logic_15976(world):
    _world_apply(world, 'temperature', 'salinity', 'square')

def logic_15977(world):
    _world_apply(world, 'temperature', 'algae', 'saturation')

def logic_15978(world):
    _world_apply(world, 'temperature', 'organic_matter', 'gap')

def logic_15979(world):
    _world_apply(world, 'temperature', 'deadwood', 'direct')

def logic_15980(world):
    _world_apply(world, 'temperature', 'pollinators', 'square')

def logic_15981(world):
    _world_apply(world, 'temperature', 'flowers', 'pulse')

def logic_15982(world):
    _world_apply(world, 'temperature', 'seed_bank', 'saturation')

def logic_15983(world):
    _world_apply(world, 'temperature', 'soil_carbon', 'gap')

def logic_15984(world):
    _world_apply(world, 'temperature', 'surface_ice', 'direct')

def logic_15985(world):
    _world_apply(world, 'surface_water', 'temperature', 'pulse')

def logic_15986(world):
    _world_apply(world, 'surface_water', 'humidity', 'saturation')

def logic_15987(world):
    _world_apply(world, 'surface_water', 'cloud', 'gap')

def logic_15988(world):
    _world_apply(world, 'surface_water', 'rain', 'direct')

def logic_15989(world):
    _world_apply(world, 'surface_water', 'soil_moisture', 'square')

def logic_15990(world):
    _world_apply(world, 'surface_water', 'runoff', 'pulse')

def logic_15991(world):
    _world_apply(world, 'surface_water', 'wind_x', 'saturation')

def logic_15992(world):
    _world_apply(world, 'surface_water', 'wind_y', 'gap')

def logic_15993(world):
    _world_apply(world, 'surface_water', 'vegetation', 'square')

def logic_15994(world):
    _world_apply(world, 'surface_water', 'biomass', 'pulse')

def logic_15995(world):
    _world_apply(world, 'surface_water', 'herbivore', 'saturation')

def logic_15996(world):
    _world_apply(world, 'surface_water', 'predator', 'gap')

def logic_15997(world):
    _world_apply(world, 'surface_water', 'carrion', 'direct')

def logic_15998(world):
    _world_apply(world, 'surface_water', 'nutrients', 'square')

def logic_15999(world):
    _world_apply(world, 'surface_water', 'decomposition_rate', 'pulse')

def logic_16000(world):
    _world_apply(world, 'surface_water', 'oxygen', 'saturation')

def logic_16001(world):
    _world_apply(world, 'surface_water', 'co2', 'direct')

def logic_16002(world):
    _world_apply(world, 'surface_water', 'photosynthesis_factor', 'square')

def logic_16003(world):
    _world_apply(world, 'surface_water', 'ice', 'pulse')

def logic_16004(world):
    _world_apply(world, 'surface_water', 'evaporation', 'saturation')

def logic_16005(world):
    _world_apply(world, 'surface_water', 'detritus', 'gap')

def logic_16006(world):
    _world_apply(world, 'surface_water', 'methane', 'direct')

def logic_16007(world):
    _world_apply(world, 'surface_water', 'pathogen_load', 'square')

def logic_16008(world):
    _world_apply(world, 'surface_water', 'biodiversity', 'pulse')

def logic_16009(world):
    _world_apply(world, 'surface_water', 'habitat_stress', 'gap')

def logic_16010(world):
    _world_apply(world, 'surface_water', 'erosion', 'direct')

def logic_16011(world):
    _world_apply(world, 'surface_water', 'soil_depth', 'square')

def logic_16012(world):
    _world_apply(world, 'surface_water', 'root_density', 'pulse')

def logic_16013(world):
    _world_apply(world, 'surface_water', 'wetland', 'saturation')

def logic_16014(world):
    _world_apply(world, 'surface_water', 'carbon_storage', 'gap')

def logic_16015(world):
    _world_apply(world, 'surface_water', 'fire_risk', 'direct')

def logic_16016(world):
    _world_apply(world, 'surface_water', 'ash', 'square')

def logic_16017(world):
    _world_apply(world, 'surface_water', 'snowpack', 'saturation')

def logic_16018(world):
    _world_apply(world, 'surface_water', 'groundwater', 'gap')

def logic_16019(world):
    _world_apply(world, 'surface_water', 'sediment', 'direct')

def logic_16020(world):
    _world_apply(world, 'surface_water', 'salinity', 'square')

def logic_16021(world):
    _world_apply(world, 'surface_water', 'algae', 'pulse')

def logic_16022(world):
    _world_apply(world, 'surface_water', 'organic_matter', 'saturation')

def logic_16023(world):
    _world_apply(world, 'surface_water', 'deadwood', 'gap')

def logic_16024(world):
    _world_apply(world, 'surface_water', 'pollinators', 'direct')

def logic_16025(world):
    _world_apply(world, 'surface_water', 'flowers', 'pulse')

def logic_16026(world):
    _world_apply(world, 'surface_water', 'seed_bank', 'saturation')

def logic_16027(world):
    _world_apply(world, 'surface_water', 'soil_carbon', 'gap')

def logic_16028(world):
    _world_apply(world, 'surface_water', 'surface_ice', 'direct')

def logic_16029(world):
    _world_apply(world, 'humidity', 'temperature', 'square')

def logic_16030(world):
    _world_apply(world, 'humidity', 'surface_water', 'pulse')

def logic_16031(world):
    _world_apply(world, 'humidity', 'cloud', 'saturation')

def logic_16032(world):
    _world_apply(world, 'humidity', 'rain', 'gap')

def logic_16033(world):
    _world_apply(world, 'humidity', 'soil_moisture', 'square')

def logic_16034(world):
    _world_apply(world, 'humidity', 'runoff', 'pulse')

def logic_16035(world):
    _world_apply(world, 'humidity', 'wind_x', 'saturation')

def logic_16036(world):
    _world_apply(world, 'humidity', 'wind_y', 'gap')

def logic_16037(world):
    _world_apply(world, 'humidity', 'vegetation', 'direct')

def logic_16038(world):
    _world_apply(world, 'humidity', 'biomass', 'square')

def logic_16039(world):
    _world_apply(world, 'humidity', 'herbivore', 'pulse')

def logic_16040(world):
    _world_apply(world, 'humidity', 'predator', 'saturation')

def logic_16041(world):
    _world_apply(world, 'humidity', 'carrion', 'direct')

def logic_16042(world):
    _world_apply(world, 'humidity', 'nutrients', 'square')

def logic_16043(world):
    _world_apply(world, 'humidity', 'decomposition_rate', 'pulse')

def logic_16044(world):
    _world_apply(world, 'humidity', 'oxygen', 'saturation')

def logic_16045(world):
    _world_apply(world, 'humidity', 'co2', 'gap')

def logic_16046(world):
    _world_apply(world, 'humidity', 'photosynthesis_factor', 'direct')

def logic_16047(world):
    _world_apply(world, 'humidity', 'ice', 'square')

def logic_16048(world):
    _world_apply(world, 'humidity', 'evaporation', 'pulse')

def logic_16049(world):
    _world_apply(world, 'humidity', 'detritus', 'gap')

def logic_16050(world):
    _world_apply(world, 'humidity', 'methane', 'direct')

def logic_16051(world):
    _world_apply(world, 'humidity', 'pathogen_load', 'square')

def logic_16052(world):
    _world_apply(world, 'humidity', 'biodiversity', 'pulse')

def logic_16053(world):
    _world_apply(world, 'humidity', 'habitat_stress', 'saturation')

def logic_16054(world):
    _world_apply(world, 'humidity', 'erosion', 'gap')

def logic_16055(world):
    _world_apply(world, 'humidity', 'soil_depth', 'direct')

def logic_16056(world):
    _world_apply(world, 'humidity', 'root_density', 'square')

def logic_16057(world):
    _world_apply(world, 'humidity', 'wetland', 'saturation')

def logic_16058(world):
    _world_apply(world, 'humidity', 'carbon_storage', 'gap')

def logic_16059(world):
    _world_apply(world, 'humidity', 'fire_risk', 'direct')

def logic_16060(world):
    _world_apply(world, 'humidity', 'ash', 'square')

def logic_16061(world):
    _world_apply(world, 'humidity', 'snowpack', 'pulse')

def logic_16062(world):
    _world_apply(world, 'humidity', 'groundwater', 'saturation')

def logic_16063(world):
    _world_apply(world, 'humidity', 'sediment', 'gap')

def logic_16064(world):
    _world_apply(world, 'humidity', 'salinity', 'direct')

def logic_16065(world):
    _world_apply(world, 'humidity', 'algae', 'pulse')

def logic_16066(world):
    _world_apply(world, 'humidity', 'organic_matter', 'saturation')

def logic_16067(world):
    _world_apply(world, 'humidity', 'deadwood', 'gap')

def logic_16068(world):
    _world_apply(world, 'humidity', 'pollinators', 'direct')

def logic_16069(world):
    _world_apply(world, 'humidity', 'flowers', 'square')

def logic_16070(world):
    _world_apply(world, 'humidity', 'seed_bank', 'pulse')

def logic_16071(world):
    _world_apply(world, 'humidity', 'soil_carbon', 'saturation')

def logic_16072(world):
    _world_apply(world, 'humidity', 'surface_ice', 'gap')

def logic_16073(world):
    _world_apply(world, 'cloud', 'temperature', 'square')

def logic_16074(world):
    _world_apply(world, 'cloud', 'surface_water', 'pulse')

def logic_16075(world):
    _world_apply(world, 'cloud', 'humidity', 'saturation')

def logic_16076(world):
    _world_apply(world, 'cloud', 'rain', 'gap')

def logic_16077(world):
    _world_apply(world, 'cloud', 'soil_moisture', 'direct')

def logic_16078(world):
    _world_apply(world, 'cloud', 'runoff', 'square')

def logic_16079(world):
    _world_apply(world, 'cloud', 'wind_x', 'pulse')

def logic_16080(world):
    _world_apply(world, 'cloud', 'wind_y', 'saturation')

def logic_16081(world):
    _world_apply(world, 'cloud', 'vegetation', 'direct')

def logic_16082(world):
    _world_apply(world, 'cloud', 'biomass', 'square')

def logic_16083(world):
    _world_apply(world, 'cloud', 'herbivore', 'pulse')

def logic_16084(world):
    _world_apply(world, 'cloud', 'predator', 'saturation')

def logic_16085(world):
    _world_apply(world, 'cloud', 'carrion', 'gap')

def logic_16086(world):
    _world_apply(world, 'cloud', 'nutrients', 'direct')

def logic_16087(world):
    _world_apply(world, 'cloud', 'decomposition_rate', 'square')

def logic_16088(world):
    _world_apply(world, 'cloud', 'oxygen', 'pulse')

def logic_16089(world):
    _world_apply(world, 'cloud', 'co2', 'gap')

def logic_16090(world):
    _world_apply(world, 'cloud', 'photosynthesis_factor', 'direct')

def logic_16091(world):
    _world_apply(world, 'cloud', 'ice', 'square')

def logic_16092(world):
    _world_apply(world, 'cloud', 'evaporation', 'pulse')

def logic_16093(world):
    _world_apply(world, 'cloud', 'detritus', 'saturation')

def logic_16094(world):
    _world_apply(world, 'cloud', 'methane', 'gap')

def logic_16095(world):
    _world_apply(world, 'cloud', 'pathogen_load', 'direct')

def logic_16096(world):
    _world_apply(world, 'cloud', 'biodiversity', 'square')

def logic_16097(world):
    _world_apply(world, 'cloud', 'habitat_stress', 'saturation')

def logic_16098(world):
    _world_apply(world, 'cloud', 'erosion', 'gap')

def logic_16099(world):
    _world_apply(world, 'cloud', 'soil_depth', 'direct')

def logic_16100(world):
    _world_apply(world, 'cloud', 'root_density', 'square')

def logic_16101(world):
    _world_apply(world, 'cloud', 'wetland', 'pulse')

def logic_16102(world):
    _world_apply(world, 'cloud', 'carbon_storage', 'saturation')

def logic_16103(world):
    _world_apply(world, 'cloud', 'fire_risk', 'gap')

def logic_16104(world):
    _world_apply(world, 'cloud', 'ash', 'direct')

def logic_16105(world):
    _world_apply(world, 'cloud', 'snowpack', 'pulse')

def logic_16106(world):
    _world_apply(world, 'cloud', 'groundwater', 'saturation')

def logic_16107(world):
    _world_apply(world, 'cloud', 'sediment', 'gap')

def logic_16108(world):
    _world_apply(world, 'cloud', 'salinity', 'direct')

def logic_16109(world):
    _world_apply(world, 'cloud', 'algae', 'square')

def logic_16110(world):
    _world_apply(world, 'cloud', 'organic_matter', 'pulse')

def logic_16111(world):
    _world_apply(world, 'cloud', 'deadwood', 'saturation')

def logic_16112(world):
    _world_apply(world, 'cloud', 'pollinators', 'gap')

def logic_16113(world):
    _world_apply(world, 'cloud', 'flowers', 'square')

def logic_16114(world):
    _world_apply(world, 'cloud', 'seed_bank', 'pulse')

def logic_16115(world):
    _world_apply(world, 'cloud', 'soil_carbon', 'saturation')

def logic_16116(world):
    _world_apply(world, 'cloud', 'surface_ice', 'gap')

def logic_16117(world):
    _world_apply(world, 'rain', 'temperature', 'direct')

def logic_16118(world):
    _world_apply(world, 'rain', 'surface_water', 'square')

def logic_16119(world):
    _world_apply(world, 'rain', 'humidity', 'pulse')

def logic_16120(world):
    _world_apply(world, 'rain', 'cloud', 'saturation')

def logic_16121(world):
    _world_apply(world, 'rain', 'soil_moisture', 'direct')

def logic_16122(world):
    _world_apply(world, 'rain', 'runoff', 'square')

def logic_16123(world):
    _world_apply(world, 'rain', 'wind_x', 'pulse')

def logic_16124(world):
    _world_apply(world, 'rain', 'wind_y', 'saturation')

def logic_16125(world):
    _world_apply(world, 'rain', 'vegetation', 'gap')

def logic_16126(world):
    _world_apply(world, 'rain', 'biomass', 'direct')

def logic_16127(world):
    _world_apply(world, 'rain', 'herbivore', 'square')

def logic_16128(world):
    _world_apply(world, 'rain', 'predator', 'pulse')

def logic_16129(world):
    _world_apply(world, 'rain', 'carrion', 'gap')

def logic_16130(world):
    _world_apply(world, 'rain', 'nutrients', 'direct')

def logic_16131(world):
    _world_apply(world, 'rain', 'decomposition_rate', 'square')

def logic_16132(world):
    _world_apply(world, 'rain', 'oxygen', 'pulse')

def logic_16133(world):
    _world_apply(world, 'rain', 'co2', 'saturation')

def logic_16134(world):
    _world_apply(world, 'rain', 'photosynthesis_factor', 'gap')

def logic_16135(world):
    _world_apply(world, 'rain', 'ice', 'direct')

def logic_16136(world):
    _world_apply(world, 'rain', 'evaporation', 'square')

def logic_16137(world):
    _world_apply(world, 'rain', 'detritus', 'saturation')

def logic_16138(world):
    _world_apply(world, 'rain', 'methane', 'gap')

def logic_16139(world):
    _world_apply(world, 'rain', 'pathogen_load', 'direct')

def logic_16140(world):
    _world_apply(world, 'rain', 'biodiversity', 'square')

def logic_16141(world):
    _world_apply(world, 'rain', 'habitat_stress', 'pulse')

def logic_16142(world):
    _world_apply(world, 'rain', 'erosion', 'saturation')

def logic_16143(world):
    _world_apply(world, 'rain', 'soil_depth', 'gap')

def logic_16144(world):
    _world_apply(world, 'rain', 'root_density', 'direct')

def logic_16145(world):
    _world_apply(world, 'rain', 'wetland', 'pulse')

def logic_16146(world):
    _world_apply(world, 'rain', 'carbon_storage', 'saturation')

def logic_16147(world):
    _world_apply(world, 'rain', 'fire_risk', 'gap')

def logic_16148(world):
    _world_apply(world, 'rain', 'ash', 'direct')

def logic_16149(world):
    _world_apply(world, 'rain', 'snowpack', 'square')

def logic_16150(world):
    _world_apply(world, 'rain', 'groundwater', 'pulse')

def logic_16151(world):
    _world_apply(world, 'rain', 'sediment', 'saturation')

def logic_16152(world):
    _world_apply(world, 'rain', 'salinity', 'gap')

def logic_16153(world):
    _world_apply(world, 'rain', 'algae', 'square')

def logic_16154(world):
    _world_apply(world, 'rain', 'organic_matter', 'pulse')

def logic_16155(world):
    _world_apply(world, 'rain', 'deadwood', 'saturation')

def logic_16156(world):
    _world_apply(world, 'rain', 'pollinators', 'gap')

def logic_16157(world):
    _world_apply(world, 'rain', 'flowers', 'direct')

def logic_16158(world):
    _world_apply(world, 'rain', 'seed_bank', 'square')

def logic_16159(world):
    _world_apply(world, 'rain', 'soil_carbon', 'pulse')

def logic_16160(world):
    _world_apply(world, 'rain', 'surface_ice', 'saturation')

def logic_16161(world):
    _world_apply(world, 'soil_moisture', 'temperature', 'direct')

def logic_16162(world):
    _world_apply(world, 'soil_moisture', 'surface_water', 'square')

def logic_16163(world):
    _world_apply(world, 'soil_moisture', 'humidity', 'pulse')

def logic_16164(world):
    _world_apply(world, 'soil_moisture', 'cloud', 'saturation')

def logic_16165(world):
    _world_apply(world, 'soil_moisture', 'rain', 'gap')

def logic_16166(world):
    _world_apply(world, 'soil_moisture', 'runoff', 'direct')

def logic_16167(world):
    _world_apply(world, 'soil_moisture', 'wind_x', 'square')

def logic_16168(world):
    _world_apply(world, 'soil_moisture', 'wind_y', 'pulse')

def logic_16169(world):
    _world_apply(world, 'soil_moisture', 'vegetation', 'gap')

def logic_16170(world):
    _world_apply(world, 'soil_moisture', 'biomass', 'direct')

def logic_16171(world):
    _world_apply(world, 'soil_moisture', 'herbivore', 'square')

def logic_16172(world):
    _world_apply(world, 'soil_moisture', 'predator', 'pulse')

def logic_16173(world):
    _world_apply(world, 'soil_moisture', 'carrion', 'saturation')

def logic_16174(world):
    _world_apply(world, 'soil_moisture', 'nutrients', 'gap')

def logic_16175(world):
    _world_apply(world, 'soil_moisture', 'decomposition_rate', 'direct')

def logic_16176(world):
    _world_apply(world, 'soil_moisture', 'oxygen', 'square')

def logic_16177(world):
    _world_apply(world, 'soil_moisture', 'co2', 'saturation')

def logic_16178(world):
    _world_apply(world, 'soil_moisture', 'photosynthesis_factor', 'gap')

def logic_16179(world):
    _world_apply(world, 'soil_moisture', 'ice', 'direct')

def logic_16180(world):
    _world_apply(world, 'soil_moisture', 'evaporation', 'square')

def logic_16181(world):
    _world_apply(world, 'soil_moisture', 'detritus', 'pulse')

def logic_16182(world):
    _world_apply(world, 'soil_moisture', 'methane', 'saturation')

def logic_16183(world):
    _world_apply(world, 'soil_moisture', 'pathogen_load', 'gap')

def logic_16184(world):
    _world_apply(world, 'soil_moisture', 'biodiversity', 'direct')

def logic_16185(world):
    _world_apply(world, 'soil_moisture', 'habitat_stress', 'pulse')

def logic_16186(world):
    _world_apply(world, 'soil_moisture', 'erosion', 'saturation')

def logic_16187(world):
    _world_apply(world, 'soil_moisture', 'soil_depth', 'gap')

def logic_16188(world):
    _world_apply(world, 'soil_moisture', 'root_density', 'direct')

def logic_16189(world):
    _world_apply(world, 'soil_moisture', 'wetland', 'square')

def logic_16190(world):
    _world_apply(world, 'soil_moisture', 'carbon_storage', 'pulse')

def logic_16191(world):
    _world_apply(world, 'soil_moisture', 'fire_risk', 'saturation')

def logic_16192(world):
    _world_apply(world, 'soil_moisture', 'ash', 'gap')

def logic_16193(world):
    _world_apply(world, 'soil_moisture', 'snowpack', 'square')

def logic_16194(world):
    _world_apply(world, 'soil_moisture', 'groundwater', 'pulse')

def logic_16195(world):
    _world_apply(world, 'soil_moisture', 'sediment', 'saturation')

def logic_16196(world):
    _world_apply(world, 'soil_moisture', 'salinity', 'gap')

def logic_16197(world):
    _world_apply(world, 'soil_moisture', 'algae', 'direct')

def logic_16198(world):
    _world_apply(world, 'soil_moisture', 'organic_matter', 'square')

def logic_16199(world):
    _world_apply(world, 'soil_moisture', 'deadwood', 'pulse')

def logic_16200(world):
    _world_apply(world, 'soil_moisture', 'pollinators', 'saturation')

def logic_16201(world):
    _world_apply(world, 'soil_moisture', 'flowers', 'direct')

def logic_16202(world):
    _world_apply(world, 'soil_moisture', 'seed_bank', 'square')

def logic_16203(world):
    _world_apply(world, 'soil_moisture', 'soil_carbon', 'pulse')

def logic_16204(world):
    _world_apply(world, 'soil_moisture', 'surface_ice', 'saturation')

def logic_16205(world):
    _world_apply(world, 'runoff', 'temperature', 'gap')

def logic_16206(world):
    _world_apply(world, 'runoff', 'surface_water', 'direct')

def logic_16207(world):
    _world_apply(world, 'runoff', 'humidity', 'square')

def logic_16208(world):
    _world_apply(world, 'runoff', 'cloud', 'pulse')

def logic_16209(world):
    _world_apply(world, 'runoff', 'rain', 'gap')

def logic_16210(world):
    _world_apply(world, 'runoff', 'soil_moisture', 'direct')

def logic_16211(world):
    _world_apply(world, 'runoff', 'wind_x', 'square')

def logic_16212(world):
    _world_apply(world, 'runoff', 'wind_y', 'pulse')

def logic_16213(world):
    _world_apply(world, 'runoff', 'vegetation', 'saturation')

def logic_16214(world):
    _world_apply(world, 'runoff', 'biomass', 'gap')

def logic_16215(world):
    _world_apply(world, 'runoff', 'herbivore', 'direct')

def logic_16216(world):
    _world_apply(world, 'runoff', 'predator', 'square')

def logic_16217(world):
    _world_apply(world, 'runoff', 'carrion', 'saturation')

def logic_16218(world):
    _world_apply(world, 'runoff', 'nutrients', 'gap')

def logic_16219(world):
    _world_apply(world, 'runoff', 'decomposition_rate', 'direct')

def logic_16220(world):
    _world_apply(world, 'runoff', 'oxygen', 'square')

def logic_16221(world):
    _world_apply(world, 'runoff', 'co2', 'pulse')

def logic_16222(world):
    _world_apply(world, 'runoff', 'photosynthesis_factor', 'saturation')

def logic_16223(world):
    _world_apply(world, 'runoff', 'ice', 'gap')

def logic_16224(world):
    _world_apply(world, 'runoff', 'evaporation', 'direct')

def logic_16225(world):
    _world_apply(world, 'runoff', 'detritus', 'pulse')

def logic_16226(world):
    _world_apply(world, 'runoff', 'methane', 'saturation')

def logic_16227(world):
    _world_apply(world, 'runoff', 'pathogen_load', 'gap')

def logic_16228(world):
    _world_apply(world, 'runoff', 'biodiversity', 'direct')

def logic_16229(world):
    _world_apply(world, 'runoff', 'habitat_stress', 'square')

def logic_16230(world):
    _world_apply(world, 'runoff', 'erosion', 'pulse')

def logic_16231(world):
    _world_apply(world, 'runoff', 'soil_depth', 'saturation')

def logic_16232(world):
    _world_apply(world, 'runoff', 'root_density', 'gap')

def logic_16233(world):
    _world_apply(world, 'runoff', 'wetland', 'square')

def logic_16234(world):
    _world_apply(world, 'runoff', 'carbon_storage', 'pulse')

def logic_16235(world):
    _world_apply(world, 'runoff', 'fire_risk', 'saturation')

def logic_16236(world):
    _world_apply(world, 'runoff', 'ash', 'gap')

def logic_16237(world):
    _world_apply(world, 'runoff', 'snowpack', 'direct')

def logic_16238(world):
    _world_apply(world, 'runoff', 'groundwater', 'square')

def logic_16239(world):
    _world_apply(world, 'runoff', 'sediment', 'pulse')

def logic_16240(world):
    _world_apply(world, 'runoff', 'salinity', 'saturation')

def logic_16241(world):
    _world_apply(world, 'runoff', 'algae', 'direct')

def logic_16242(world):
    _world_apply(world, 'runoff', 'organic_matter', 'square')

def logic_16243(world):
    _world_apply(world, 'runoff', 'deadwood', 'pulse')

def logic_16244(world):
    _world_apply(world, 'runoff', 'pollinators', 'saturation')

def logic_16245(world):
    _world_apply(world, 'runoff', 'flowers', 'gap')

def logic_16246(world):
    _world_apply(world, 'runoff', 'seed_bank', 'direct')

def logic_16247(world):
    _world_apply(world, 'runoff', 'soil_carbon', 'square')

def logic_16248(world):
    _world_apply(world, 'runoff', 'surface_ice', 'pulse')

def logic_16249(world):
    _world_apply(world, 'wind_x', 'temperature', 'gap')

def logic_16250(world):
    _world_apply(world, 'wind_x', 'surface_water', 'direct')

def logic_16251(world):
    _world_apply(world, 'wind_x', 'humidity', 'square')

def logic_16252(world):
    _world_apply(world, 'wind_x', 'cloud', 'pulse')

def logic_16253(world):
    _world_apply(world, 'wind_x', 'rain', 'saturation')

def logic_16254(world):
    _world_apply(world, 'wind_x', 'soil_moisture', 'gap')

def logic_16255(world):
    _world_apply(world, 'wind_x', 'runoff', 'direct')

def logic_16256(world):
    _world_apply(world, 'wind_x', 'wind_y', 'square')

def logic_16257(world):
    _world_apply(world, 'wind_x', 'vegetation', 'saturation')

def logic_16258(world):
    _world_apply(world, 'wind_x', 'biomass', 'gap')

def logic_16259(world):
    _world_apply(world, 'wind_x', 'herbivore', 'direct')

def logic_16260(world):
    _world_apply(world, 'wind_x', 'predator', 'square')

def logic_16261(world):
    _world_apply(world, 'wind_x', 'carrion', 'pulse')

def logic_16262(world):
    _world_apply(world, 'wind_x', 'nutrients', 'saturation')

def logic_16263(world):
    _world_apply(world, 'wind_x', 'decomposition_rate', 'gap')

def logic_16264(world):
    _world_apply(world, 'wind_x', 'oxygen', 'direct')

def logic_16265(world):
    _world_apply(world, 'wind_x', 'co2', 'pulse')

def logic_16266(world):
    _world_apply(world, 'wind_x', 'photosynthesis_factor', 'saturation')

def logic_16267(world):
    _world_apply(world, 'wind_x', 'ice', 'gap')

def logic_16268(world):
    _world_apply(world, 'wind_x', 'evaporation', 'direct')

def logic_16269(world):
    _world_apply(world, 'wind_x', 'detritus', 'square')

def logic_16270(world):
    _world_apply(world, 'wind_x', 'methane', 'pulse')

def logic_16271(world):
    _world_apply(world, 'wind_x', 'pathogen_load', 'saturation')

def logic_16272(world):
    _world_apply(world, 'wind_x', 'biodiversity', 'gap')

def logic_16273(world):
    _world_apply(world, 'wind_x', 'habitat_stress', 'square')

def logic_16274(world):
    _world_apply(world, 'wind_x', 'erosion', 'pulse')

def logic_16275(world):
    _world_apply(world, 'wind_x', 'soil_depth', 'saturation')

def logic_16276(world):
    _world_apply(world, 'wind_x', 'root_density', 'gap')

def logic_16277(world):
    _world_apply(world, 'wind_x', 'wetland', 'direct')

def logic_16278(world):
    _world_apply(world, 'wind_x', 'carbon_storage', 'square')

def logic_16279(world):
    _world_apply(world, 'wind_x', 'fire_risk', 'pulse')

def logic_16280(world):
    _world_apply(world, 'wind_x', 'ash', 'saturation')

def logic_16281(world):
    _world_apply(world, 'wind_x', 'snowpack', 'direct')

def logic_16282(world):
    _world_apply(world, 'wind_x', 'groundwater', 'square')

def logic_16283(world):
    _world_apply(world, 'wind_x', 'sediment', 'pulse')

def logic_16284(world):
    _world_apply(world, 'wind_x', 'salinity', 'saturation')

def logic_16285(world):
    _world_apply(world, 'wind_x', 'algae', 'gap')

def logic_16286(world):
    _world_apply(world, 'wind_x', 'organic_matter', 'direct')

def logic_16287(world):
    _world_apply(world, 'wind_x', 'deadwood', 'square')

def logic_16288(world):
    _world_apply(world, 'wind_x', 'pollinators', 'pulse')

def logic_16289(world):
    _world_apply(world, 'wind_x', 'flowers', 'gap')

def logic_16290(world):
    _world_apply(world, 'wind_x', 'seed_bank', 'direct')

def logic_16291(world):
    _world_apply(world, 'wind_x', 'soil_carbon', 'square')

def logic_16292(world):
    _world_apply(world, 'wind_x', 'surface_ice', 'pulse')

def logic_16293(world):
    _world_apply(world, 'wind_y', 'temperature', 'saturation')

def logic_16294(world):
    _world_apply(world, 'wind_y', 'surface_water', 'gap')

def logic_16295(world):
    _world_apply(world, 'wind_y', 'humidity', 'direct')

def logic_16296(world):
    _world_apply(world, 'wind_y', 'cloud', 'square')

def logic_16297(world):
    _world_apply(world, 'wind_y', 'rain', 'saturation')

def logic_16298(world):
    _world_apply(world, 'wind_y', 'soil_moisture', 'gap')

def logic_16299(world):
    _world_apply(world, 'wind_y', 'runoff', 'direct')

def logic_16300(world):
    _world_apply(world, 'wind_y', 'wind_x', 'square')

def logic_16301(world):
    _world_apply(world, 'wind_y', 'vegetation', 'pulse')

def logic_16302(world):
    _world_apply(world, 'wind_y', 'biomass', 'saturation')

def logic_16303(world):
    _world_apply(world, 'wind_y', 'herbivore', 'gap')

def logic_16304(world):
    _world_apply(world, 'wind_y', 'predator', 'direct')

def logic_16305(world):
    _world_apply(world, 'wind_y', 'carrion', 'pulse')

def logic_16306(world):
    _world_apply(world, 'wind_y', 'nutrients', 'saturation')

def logic_16307(world):
    _world_apply(world, 'wind_y', 'decomposition_rate', 'gap')

def logic_16308(world):
    _world_apply(world, 'wind_y', 'oxygen', 'direct')

def logic_16309(world):
    _world_apply(world, 'wind_y', 'co2', 'square')

def logic_16310(world):
    _world_apply(world, 'wind_y', 'photosynthesis_factor', 'pulse')

def logic_16311(world):
    _world_apply(world, 'wind_y', 'ice', 'saturation')

def logic_16312(world):
    _world_apply(world, 'wind_y', 'evaporation', 'gap')

def logic_16313(world):
    _world_apply(world, 'wind_y', 'detritus', 'square')

def logic_16314(world):
    _world_apply(world, 'wind_y', 'methane', 'pulse')

def logic_16315(world):
    _world_apply(world, 'wind_y', 'pathogen_load', 'saturation')

def logic_16316(world):
    _world_apply(world, 'wind_y', 'biodiversity', 'gap')

def logic_16317(world):
    _world_apply(world, 'wind_y', 'habitat_stress', 'direct')

def logic_16318(world):
    _world_apply(world, 'wind_y', 'erosion', 'square')

def logic_16319(world):
    _world_apply(world, 'wind_y', 'soil_depth', 'pulse')

def logic_16320(world):
    _world_apply(world, 'wind_y', 'root_density', 'saturation')

def logic_16321(world):
    _world_apply(world, 'wind_y', 'wetland', 'direct')

def logic_16322(world):
    _world_apply(world, 'wind_y', 'carbon_storage', 'square')

def logic_16323(world):
    _world_apply(world, 'wind_y', 'fire_risk', 'pulse')

def logic_16324(world):
    _world_apply(world, 'wind_y', 'ash', 'saturation')

def logic_16325(world):
    _world_apply(world, 'wind_y', 'snowpack', 'gap')

def logic_16326(world):
    _world_apply(world, 'wind_y', 'groundwater', 'direct')

def logic_16327(world):
    _world_apply(world, 'wind_y', 'sediment', 'square')

def logic_16328(world):
    _world_apply(world, 'wind_y', 'salinity', 'pulse')

def logic_16329(world):
    _world_apply(world, 'wind_y', 'algae', 'gap')

def logic_16330(world):
    _world_apply(world, 'wind_y', 'organic_matter', 'direct')

def logic_16331(world):
    _world_apply(world, 'wind_y', 'deadwood', 'square')

def logic_16332(world):
    _world_apply(world, 'wind_y', 'pollinators', 'pulse')

def logic_16333(world):
    _world_apply(world, 'wind_y', 'flowers', 'saturation')

def logic_16334(world):
    _world_apply(world, 'wind_y', 'seed_bank', 'gap')

def logic_16335(world):
    _world_apply(world, 'wind_y', 'soil_carbon', 'direct')

def logic_16336(world):
    _world_apply(world, 'wind_y', 'surface_ice', 'square')

def logic_16337(world):
    _world_apply(world, 'vegetation', 'temperature', 'saturation')

def logic_16338(world):
    _world_apply(world, 'vegetation', 'surface_water', 'gap')

def logic_16339(world):
    _world_apply(world, 'vegetation', 'humidity', 'direct')

def logic_16340(world):
    _world_apply(world, 'vegetation', 'cloud', 'square')

def logic_16341(world):
    _world_apply(world, 'vegetation', 'rain', 'pulse')

def logic_16342(world):
    _world_apply(world, 'vegetation', 'soil_moisture', 'saturation')

def logic_16343(world):
    _world_apply(world, 'vegetation', 'runoff', 'gap')

def logic_16344(world):
    _world_apply(world, 'vegetation', 'wind_x', 'direct')

def logic_16345(world):
    _world_apply(world, 'vegetation', 'wind_y', 'pulse')

def logic_16346(world):
    _world_apply(world, 'vegetation', 'biomass', 'saturation')

def logic_16347(world):
    _world_apply(world, 'vegetation', 'herbivore', 'gap')

def logic_16348(world):
    _world_apply(world, 'vegetation', 'predator', 'direct')

def logic_16349(world):
    _world_apply(world, 'vegetation', 'carrion', 'square')

def logic_16350(world):
    _world_apply(world, 'vegetation', 'nutrients', 'pulse')

def logic_16351(world):
    _world_apply(world, 'vegetation', 'decomposition_rate', 'saturation')

def logic_16352(world):
    _world_apply(world, 'vegetation', 'oxygen', 'gap')

def logic_16353(world):
    _world_apply(world, 'vegetation', 'co2', 'square')

def logic_16354(world):
    _world_apply(world, 'vegetation', 'photosynthesis_factor', 'pulse')

def logic_16355(world):
    _world_apply(world, 'vegetation', 'ice', 'saturation')

def logic_16356(world):
    _world_apply(world, 'vegetation', 'evaporation', 'gap')

def logic_16357(world):
    _world_apply(world, 'vegetation', 'detritus', 'direct')

def logic_16358(world):
    _world_apply(world, 'vegetation', 'methane', 'square')

def logic_16359(world):
    _world_apply(world, 'vegetation', 'pathogen_load', 'pulse')

def logic_16360(world):
    _world_apply(world, 'vegetation', 'biodiversity', 'saturation')

def logic_16361(world):
    _world_apply(world, 'vegetation', 'habitat_stress', 'direct')

def logic_16362(world):
    _world_apply(world, 'vegetation', 'erosion', 'square')

def logic_16363(world):
    _world_apply(world, 'vegetation', 'soil_depth', 'pulse')

def logic_16364(world):
    _world_apply(world, 'vegetation', 'root_density', 'saturation')

def logic_16365(world):
    _world_apply(world, 'vegetation', 'wetland', 'gap')

def logic_16366(world):
    _world_apply(world, 'vegetation', 'carbon_storage', 'direct')

def logic_16367(world):
    _world_apply(world, 'vegetation', 'fire_risk', 'square')

def logic_16368(world):
    _world_apply(world, 'vegetation', 'ash', 'pulse')

def logic_16369(world):
    _world_apply(world, 'vegetation', 'snowpack', 'gap')

def logic_16370(world):
    _world_apply(world, 'vegetation', 'groundwater', 'direct')

def logic_16371(world):
    _world_apply(world, 'vegetation', 'sediment', 'square')

def logic_16372(world):
    _world_apply(world, 'vegetation', 'salinity', 'pulse')

def logic_16373(world):
    _world_apply(world, 'vegetation', 'algae', 'saturation')

def logic_16374(world):
    _world_apply(world, 'vegetation', 'organic_matter', 'gap')

def logic_16375(world):
    _world_apply(world, 'vegetation', 'deadwood', 'direct')

def logic_16376(world):
    _world_apply(world, 'vegetation', 'pollinators', 'square')

def logic_16377(world):
    _world_apply(world, 'vegetation', 'flowers', 'saturation')

def logic_16378(world):
    _world_apply(world, 'vegetation', 'seed_bank', 'gap')

def logic_16379(world):
    _world_apply(world, 'vegetation', 'soil_carbon', 'direct')

def logic_16380(world):
    _world_apply(world, 'vegetation', 'surface_ice', 'square')

def logic_16381(world):
    _world_apply(world, 'biomass', 'temperature', 'pulse')

def logic_16382(world):
    _world_apply(world, 'biomass', 'surface_water', 'saturation')

def logic_16383(world):
    _world_apply(world, 'biomass', 'humidity', 'gap')

def logic_16384(world):
    _world_apply(world, 'biomass', 'cloud', 'direct')

def logic_16385(world):
    _world_apply(world, 'biomass', 'rain', 'pulse')

def logic_16386(world):
    _world_apply(world, 'biomass', 'soil_moisture', 'saturation')

def logic_16387(world):
    _world_apply(world, 'biomass', 'runoff', 'gap')

def logic_16388(world):
    _world_apply(world, 'biomass', 'wind_x', 'direct')

def logic_16389(world):
    _world_apply(world, 'biomass', 'wind_y', 'square')

def logic_16390(world):
    _world_apply(world, 'biomass', 'vegetation', 'pulse')

def logic_16391(world):
    _world_apply(world, 'biomass', 'herbivore', 'saturation')

def logic_16392(world):
    _world_apply(world, 'biomass', 'predator', 'gap')

def logic_16393(world):
    _world_apply(world, 'biomass', 'carrion', 'square')

def logic_16394(world):
    _world_apply(world, 'biomass', 'nutrients', 'pulse')

def logic_16395(world):
    _world_apply(world, 'biomass', 'decomposition_rate', 'saturation')

def logic_16396(world):
    _world_apply(world, 'biomass', 'oxygen', 'gap')

def logic_16397(world):
    _world_apply(world, 'biomass', 'co2', 'direct')

def logic_16398(world):
    _world_apply(world, 'biomass', 'photosynthesis_factor', 'square')

def logic_16399(world):
    _world_apply(world, 'biomass', 'ice', 'pulse')

def logic_16400(world):
    _world_apply(world, 'biomass', 'evaporation', 'saturation')

def logic_16401(world):
    _world_apply(world, 'biomass', 'detritus', 'direct')

def logic_16402(world):
    _world_apply(world, 'biomass', 'methane', 'square')

def logic_16403(world):
    _world_apply(world, 'biomass', 'pathogen_load', 'pulse')

def logic_16404(world):
    _world_apply(world, 'biomass', 'biodiversity', 'saturation')

def logic_16405(world):
    _world_apply(world, 'biomass', 'habitat_stress', 'gap')

def logic_16406(world):
    _world_apply(world, 'biomass', 'erosion', 'direct')

def logic_16407(world):
    _world_apply(world, 'biomass', 'soil_depth', 'square')

def logic_16408(world):
    _world_apply(world, 'biomass', 'root_density', 'pulse')

def logic_16409(world):
    _world_apply(world, 'biomass', 'wetland', 'gap')

def logic_16410(world):
    _world_apply(world, 'biomass', 'carbon_storage', 'direct')

def logic_16411(world):
    _world_apply(world, 'biomass', 'fire_risk', 'square')

def logic_16412(world):
    _world_apply(world, 'biomass', 'ash', 'pulse')

def logic_16413(world):
    _world_apply(world, 'biomass', 'snowpack', 'saturation')

def logic_16414(world):
    _world_apply(world, 'biomass', 'groundwater', 'gap')

def logic_16415(world):
    _world_apply(world, 'biomass', 'sediment', 'direct')

def logic_16416(world):
    _world_apply(world, 'biomass', 'salinity', 'square')

def logic_16417(world):
    _world_apply(world, 'biomass', 'algae', 'saturation')

def logic_16418(world):
    _world_apply(world, 'biomass', 'organic_matter', 'gap')

def logic_16419(world):
    _world_apply(world, 'biomass', 'deadwood', 'direct')

def logic_16420(world):
    _world_apply(world, 'biomass', 'pollinators', 'square')

def logic_16421(world):
    _world_apply(world, 'biomass', 'flowers', 'pulse')

def logic_16422(world):
    _world_apply(world, 'biomass', 'seed_bank', 'saturation')

def logic_16423(world):
    _world_apply(world, 'biomass', 'soil_carbon', 'gap')

def logic_16424(world):
    _world_apply(world, 'biomass', 'surface_ice', 'direct')

def logic_16425(world):
    _world_apply(world, 'herbivore', 'temperature', 'pulse')

def logic_16426(world):
    _world_apply(world, 'herbivore', 'surface_water', 'saturation')

def logic_16427(world):
    _world_apply(world, 'herbivore', 'humidity', 'gap')

def logic_16428(world):
    _world_apply(world, 'herbivore', 'cloud', 'direct')

def logic_16429(world):
    _world_apply(world, 'herbivore', 'rain', 'square')

def logic_16430(world):
    _world_apply(world, 'herbivore', 'soil_moisture', 'pulse')

def logic_16431(world):
    _world_apply(world, 'herbivore', 'runoff', 'saturation')

def logic_16432(world):
    _world_apply(world, 'herbivore', 'wind_x', 'gap')

def logic_16433(world):
    _world_apply(world, 'herbivore', 'wind_y', 'square')

def logic_16434(world):
    _world_apply(world, 'herbivore', 'vegetation', 'pulse')

def logic_16435(world):
    _world_apply(world, 'herbivore', 'biomass', 'saturation')

def logic_16436(world):
    _world_apply(world, 'herbivore', 'predator', 'gap')

def logic_16437(world):
    _world_apply(world, 'herbivore', 'carrion', 'direct')

def logic_16438(world):
    _world_apply(world, 'herbivore', 'nutrients', 'square')

def logic_16439(world):
    _world_apply(world, 'herbivore', 'decomposition_rate', 'pulse')

def logic_16440(world):
    _world_apply(world, 'herbivore', 'oxygen', 'saturation')

def logic_16441(world):
    _world_apply(world, 'herbivore', 'co2', 'direct')

def logic_16442(world):
    _world_apply(world, 'herbivore', 'photosynthesis_factor', 'square')

def logic_16443(world):
    _world_apply(world, 'herbivore', 'ice', 'pulse')

def logic_16444(world):
    _world_apply(world, 'herbivore', 'evaporation', 'saturation')

def logic_16445(world):
    _world_apply(world, 'herbivore', 'detritus', 'gap')

def logic_16446(world):
    _world_apply(world, 'herbivore', 'methane', 'direct')

def logic_16447(world):
    _world_apply(world, 'herbivore', 'pathogen_load', 'square')

def logic_16448(world):
    _world_apply(world, 'herbivore', 'biodiversity', 'pulse')

def logic_16449(world):
    _world_apply(world, 'herbivore', 'habitat_stress', 'gap')

def logic_16450(world):
    _world_apply(world, 'herbivore', 'erosion', 'direct')

def logic_16451(world):
    _world_apply(world, 'herbivore', 'soil_depth', 'square')

def logic_16452(world):
    _world_apply(world, 'herbivore', 'root_density', 'pulse')

def logic_16453(world):
    _world_apply(world, 'herbivore', 'wetland', 'saturation')

def logic_16454(world):
    _world_apply(world, 'herbivore', 'carbon_storage', 'gap')

def logic_16455(world):
    _world_apply(world, 'herbivore', 'fire_risk', 'direct')

def logic_16456(world):
    _world_apply(world, 'herbivore', 'ash', 'square')

def logic_16457(world):
    _world_apply(world, 'herbivore', 'snowpack', 'saturation')

def logic_16458(world):
    _world_apply(world, 'herbivore', 'groundwater', 'gap')

def logic_16459(world):
    _world_apply(world, 'herbivore', 'sediment', 'direct')

def logic_16460(world):
    _world_apply(world, 'herbivore', 'salinity', 'square')

def logic_16461(world):
    _world_apply(world, 'herbivore', 'algae', 'pulse')

def logic_16462(world):
    _world_apply(world, 'herbivore', 'organic_matter', 'saturation')

def logic_16463(world):
    _world_apply(world, 'herbivore', 'deadwood', 'gap')

def logic_16464(world):
    _world_apply(world, 'herbivore', 'pollinators', 'direct')

def logic_16465(world):
    _world_apply(world, 'herbivore', 'flowers', 'pulse')

def logic_16466(world):
    _world_apply(world, 'herbivore', 'seed_bank', 'saturation')

def logic_16467(world):
    _world_apply(world, 'herbivore', 'soil_carbon', 'gap')

def logic_16468(world):
    _world_apply(world, 'herbivore', 'surface_ice', 'direct')

def logic_16469(world):
    _world_apply(world, 'predator', 'temperature', 'square')

def logic_16470(world):
    _world_apply(world, 'predator', 'surface_water', 'pulse')

def logic_16471(world):
    _world_apply(world, 'predator', 'humidity', 'saturation')

def logic_16472(world):
    _world_apply(world, 'predator', 'cloud', 'gap')

def logic_16473(world):
    _world_apply(world, 'predator', 'rain', 'square')

def logic_16474(world):
    _world_apply(world, 'predator', 'soil_moisture', 'pulse')

def logic_16475(world):
    _world_apply(world, 'predator', 'runoff', 'saturation')

def logic_16476(world):
    _world_apply(world, 'predator', 'wind_x', 'gap')

def logic_16477(world):
    _world_apply(world, 'predator', 'wind_y', 'direct')

def logic_16478(world):
    _world_apply(world, 'predator', 'vegetation', 'square')

def logic_16479(world):
    _world_apply(world, 'predator', 'biomass', 'pulse')

def logic_16480(world):
    _world_apply(world, 'predator', 'herbivore', 'saturation')

def logic_16481(world):
    _world_apply(world, 'predator', 'carrion', 'direct')

def logic_16482(world):
    _world_apply(world, 'predator', 'nutrients', 'square')

def logic_16483(world):
    _world_apply(world, 'predator', 'decomposition_rate', 'pulse')

def logic_16484(world):
    _world_apply(world, 'predator', 'oxygen', 'saturation')

def logic_16485(world):
    _world_apply(world, 'predator', 'co2', 'gap')

def logic_16486(world):
    _world_apply(world, 'predator', 'photosynthesis_factor', 'direct')

def logic_16487(world):
    _world_apply(world, 'predator', 'ice', 'square')

def logic_16488(world):
    _world_apply(world, 'predator', 'evaporation', 'pulse')

def logic_16489(world):
    _world_apply(world, 'predator', 'detritus', 'gap')

def logic_16490(world):
    _world_apply(world, 'predator', 'methane', 'direct')

def logic_16491(world):
    _world_apply(world, 'predator', 'pathogen_load', 'square')

def logic_16492(world):
    _world_apply(world, 'predator', 'biodiversity', 'pulse')

def logic_16493(world):
    _world_apply(world, 'predator', 'habitat_stress', 'saturation')

def logic_16494(world):
    _world_apply(world, 'predator', 'erosion', 'gap')

def logic_16495(world):
    _world_apply(world, 'predator', 'soil_depth', 'direct')

def logic_16496(world):
    _world_apply(world, 'predator', 'root_density', 'square')

def logic_16497(world):
    _world_apply(world, 'predator', 'wetland', 'saturation')

def logic_16498(world):
    _world_apply(world, 'predator', 'carbon_storage', 'gap')

def logic_16499(world):
    _world_apply(world, 'predator', 'fire_risk', 'direct')

def logic_16500(world):
    _world_apply(world, 'predator', 'ash', 'square')

def logic_16501(world):
    _world_apply(world, 'predator', 'snowpack', 'pulse')

def logic_16502(world):
    _world_apply(world, 'predator', 'groundwater', 'saturation')

def logic_16503(world):
    _world_apply(world, 'predator', 'sediment', 'gap')

def logic_16504(world):
    _world_apply(world, 'predator', 'salinity', 'direct')

def logic_16505(world):
    _world_apply(world, 'predator', 'algae', 'pulse')

def logic_16506(world):
    _world_apply(world, 'predator', 'organic_matter', 'saturation')

def logic_16507(world):
    _world_apply(world, 'predator', 'deadwood', 'gap')

def logic_16508(world):
    _world_apply(world, 'predator', 'pollinators', 'direct')

def logic_16509(world):
    _world_apply(world, 'predator', 'flowers', 'square')

def logic_16510(world):
    _world_apply(world, 'predator', 'seed_bank', 'pulse')

def logic_16511(world):
    _world_apply(world, 'predator', 'soil_carbon', 'saturation')

def logic_16512(world):
    _world_apply(world, 'predator', 'surface_ice', 'gap')

def logic_16513(world):
    _world_apply(world, 'carrion', 'temperature', 'square')

def logic_16514(world):
    _world_apply(world, 'carrion', 'surface_water', 'pulse')

def logic_16515(world):
    _world_apply(world, 'carrion', 'humidity', 'saturation')

def logic_16516(world):
    _world_apply(world, 'carrion', 'cloud', 'gap')

def logic_16517(world):
    _world_apply(world, 'carrion', 'rain', 'direct')

def logic_16518(world):
    _world_apply(world, 'carrion', 'soil_moisture', 'square')

def logic_16519(world):
    _world_apply(world, 'carrion', 'runoff', 'pulse')

def logic_16520(world):
    _world_apply(world, 'carrion', 'wind_x', 'saturation')

def logic_16521(world):
    _world_apply(world, 'carrion', 'wind_y', 'direct')

def logic_16522(world):
    _world_apply(world, 'carrion', 'vegetation', 'square')
