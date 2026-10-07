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
