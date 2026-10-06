import torch

_RATE = 0.012

def _local(world, agents, name):
    x = agents.pos[:,0].long()
    y = agents.pos[:,1].long()
    field = getattr(world, name)
    return field[y, x].to(dtype=agents.energy.dtype).clamp(0.0, 1.0)

def _a(agents, name):
    return getattr(agents, name)

def _update(agents, target, desired):
    x = _a(agents, target)
    desired = torch.nan_to_num(desired).clamp(0.0, 1.0)
    setattr(agents, target, torch.nan_to_num(x + _RATE * (desired - x)).clamp(0.0, 1.0))

def _desired(agents, world, source, target, mode):
    s = _local(world, agents, source)
    t = _a(agents, target).clamp(0.0, 1.0)
    if mode == "direct": return s
    if mode == "inverse": return 1.0 - s
    if mode == "threshold": return (s > 0.5).to(s.dtype)
    if mode == "strong": return s * s
    if mode == "limited": return torch.sqrt(s.clamp_min(0.0))
    if mode == "pulse": return (4.0 * s * (1.0-s)).clamp(0.0,1.0)
    if mode == "feedback": return s * t
    if mode == "counterpressure": return 1.0 - s * t
    if mode == "capacity": return s * _a(agents, "resource_abundance").clamp(0.0,1.0)
    if mode == "reserve": return s * _a(agents, "energy_surplus").clamp(0.0,1.0)
    if mode == "scarcity": return (1.0-s) * _a(agents, "hunger").clamp(0.0,1.0)
    if mode == "stress": return s * _a(agents, "stress").clamp(0.0,1.0)
    if mode == "recovery": return s * _a(agents, "health").clamp(0.0,1.0)
    if mode == "persistence": return s * _a(agents, "memory_update").clamp(0.0,1.0)
    raise ValueError(mode)

def logic_3002(agents, world):
    # surface_water -> hydration; direct coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'direct'))

def logic_3003(agents, world):
    # surface_water -> hydration; inverse coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'inverse'))

def logic_3004(agents, world):
    # surface_water -> hydration; threshold coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'threshold'))

def logic_3005(agents, world):
    # surface_water -> hydration; strong coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'strong'))

def logic_3006(agents, world):
    # surface_water -> hydration; limited coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'limited'))

def logic_3007(agents, world):
    # surface_water -> hydration; pulse coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'pulse'))

def logic_3008(agents, world):
    # surface_water -> hydration; feedback coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'feedback'))

def logic_3009(agents, world):
    # surface_water -> hydration; counterpressure coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'counterpressure'))

def logic_3010(agents, world):
    # surface_water -> hydration; capacity coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'capacity'))

def logic_3011(agents, world):
    # surface_water -> hydration; reserve coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'reserve'))

def logic_3012(agents, world):
    # surface_water -> hydration; scarcity coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'scarcity'))

def logic_3013(agents, world):
    # surface_water -> hydration; stress coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'stress'))

def logic_3014(agents, world):
    # surface_water -> hydration; recovery coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'recovery'))

def logic_3015(agents, world):
    # surface_water -> hydration; persistence coupling.
    _update(agents, 'hydration', _desired(agents, world, 'surface_water', 'hydration', 'persistence'))

def logic_3016(agents, world):
    # surface_water -> thirst; direct coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'direct'))

def logic_3017(agents, world):
    # surface_water -> thirst; inverse coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'inverse'))

def logic_3018(agents, world):
    # surface_water -> thirst; threshold coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'threshold'))

def logic_3019(agents, world):
    # surface_water -> thirst; strong coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'strong'))

def logic_3020(agents, world):
    # surface_water -> thirst; limited coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'limited'))

def logic_3021(agents, world):
    # surface_water -> thirst; pulse coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'pulse'))

def logic_3022(agents, world):
    # surface_water -> thirst; feedback coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'feedback'))

def logic_3023(agents, world):
    # surface_water -> thirst; counterpressure coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'counterpressure'))

def logic_3024(agents, world):
    # surface_water -> thirst; capacity coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'capacity'))

def logic_3025(agents, world):
    # surface_water -> thirst; reserve coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'reserve'))

def logic_3026(agents, world):
    # surface_water -> thirst; scarcity coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'scarcity'))

def logic_3027(agents, world):
    # surface_water -> thirst; stress coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'stress'))

def logic_3028(agents, world):
    # surface_water -> thirst; recovery coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'recovery'))

def logic_3029(agents, world):
    # surface_water -> thirst; persistence coupling.
    _update(agents, 'thirst', _desired(agents, world, 'surface_water', 'thirst', 'persistence'))

def logic_3030(agents, world):
    # surface_water -> hunger; direct coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'direct'))

def logic_3031(agents, world):
    # surface_water -> hunger; inverse coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'inverse'))

def logic_3032(agents, world):
    # surface_water -> hunger; threshold coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'threshold'))

def logic_3033(agents, world):
    # surface_water -> hunger; strong coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'strong'))

def logic_3034(agents, world):
    # surface_water -> hunger; limited coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'limited'))

def logic_3035(agents, world):
    # surface_water -> hunger; pulse coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'pulse'))

def logic_3036(agents, world):
    # surface_water -> hunger; feedback coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'feedback'))

def logic_3037(agents, world):
    # surface_water -> hunger; counterpressure coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'counterpressure'))

def logic_3038(agents, world):
    # surface_water -> hunger; capacity coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'capacity'))

def logic_3039(agents, world):
    # surface_water -> hunger; reserve coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'reserve'))

def logic_3040(agents, world):
    # surface_water -> hunger; scarcity coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'scarcity'))

def logic_3041(agents, world):
    # surface_water -> hunger; stress coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'stress'))

def logic_3042(agents, world):
    # surface_water -> hunger; recovery coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'recovery'))

def logic_3043(agents, world):
    # surface_water -> hunger; persistence coupling.
    _update(agents, 'hunger', _desired(agents, world, 'surface_water', 'hunger', 'persistence'))

def logic_3044(agents, world):
    # surface_water -> health; direct coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'direct'))

def logic_3045(agents, world):
    # surface_water -> health; inverse coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'inverse'))

def logic_3046(agents, world):
    # surface_water -> health; threshold coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'threshold'))

def logic_3047(agents, world):
    # surface_water -> health; strong coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'strong'))

def logic_3048(agents, world):
    # surface_water -> health; limited coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'limited'))

def logic_3049(agents, world):
    # surface_water -> health; pulse coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'pulse'))

def logic_3050(agents, world):
    # surface_water -> health; feedback coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'feedback'))

def logic_3051(agents, world):
    # surface_water -> health; counterpressure coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'counterpressure'))

def logic_3052(agents, world):
    # surface_water -> health; capacity coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'capacity'))

def logic_3053(agents, world):
    # surface_water -> health; reserve coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'reserve'))

def logic_3054(agents, world):
    # surface_water -> health; scarcity coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'scarcity'))

def logic_3055(agents, world):
    # surface_water -> health; stress coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'stress'))

def logic_3056(agents, world):
    # surface_water -> health; recovery coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'recovery'))

def logic_3057(agents, world):
    # surface_water -> health; persistence coupling.
    _update(agents, 'health', _desired(agents, world, 'surface_water', 'health', 'persistence'))

def logic_3058(agents, world):
    # surface_water -> thermal_stress; direct coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'direct'))

def logic_3059(agents, world):
    # surface_water -> thermal_stress; inverse coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'inverse'))

def logic_3060(agents, world):
    # surface_water -> thermal_stress; threshold coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'threshold'))

def logic_3061(agents, world):
    # surface_water -> thermal_stress; strong coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'strong'))

def logic_3062(agents, world):
    # surface_water -> thermal_stress; limited coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'limited'))

def logic_3063(agents, world):
    # surface_water -> thermal_stress; pulse coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'pulse'))

def logic_3064(agents, world):
    # surface_water -> thermal_stress; feedback coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'feedback'))

def logic_3065(agents, world):
    # surface_water -> thermal_stress; counterpressure coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'counterpressure'))

def logic_3066(agents, world):
    # surface_water -> thermal_stress; capacity coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'capacity'))

def logic_3067(agents, world):
    # surface_water -> thermal_stress; reserve coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'reserve'))

def logic_3068(agents, world):
    # surface_water -> thermal_stress; scarcity coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'scarcity'))

def logic_3069(agents, world):
    # surface_water -> thermal_stress; stress coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'stress'))

def logic_3070(agents, world):
    # surface_water -> thermal_stress; recovery coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'recovery'))

def logic_3071(agents, world):
    # surface_water -> thermal_stress; persistence coupling.
    _update(agents, 'thermal_stress', _desired(agents, world, 'surface_water', 'thermal_stress', 'persistence'))

def logic_3072(agents, world):
    # surface_water -> dehydration; direct coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'direct'))

def logic_3073(agents, world):
    # surface_water -> dehydration; inverse coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'inverse'))

def logic_3074(agents, world):
    # surface_water -> dehydration; threshold coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'threshold'))

def logic_3075(agents, world):
    # surface_water -> dehydration; strong coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'strong'))

def logic_3076(agents, world):
    # surface_water -> dehydration; limited coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'limited'))

def logic_3077(agents, world):
    # surface_water -> dehydration; pulse coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'pulse'))

def logic_3078(agents, world):
    # surface_water -> dehydration; feedback coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'feedback'))

def logic_3079(agents, world):
    # surface_water -> dehydration; counterpressure coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'counterpressure'))

def logic_3080(agents, world):
    # surface_water -> dehydration; capacity coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'capacity'))

def logic_3081(agents, world):
    # surface_water -> dehydration; reserve coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'reserve'))

def logic_3082(agents, world):
    # surface_water -> dehydration; scarcity coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'scarcity'))

def logic_3083(agents, world):
    # surface_water -> dehydration; stress coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'stress'))

def logic_3084(agents, world):
    # surface_water -> dehydration; recovery coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'recovery'))

def logic_3085(agents, world):
    # surface_water -> dehydration; persistence coupling.
    _update(agents, 'dehydration', _desired(agents, world, 'surface_water', 'dehydration', 'persistence'))

def logic_3086(agents, world):
    # surface_water -> pathogen_risk; direct coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'direct'))

def logic_3087(agents, world):
    # surface_water -> pathogen_risk; inverse coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'inverse'))

def logic_3088(agents, world):
    # surface_water -> pathogen_risk; threshold coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'threshold'))

def logic_3089(agents, world):
    # surface_water -> pathogen_risk; strong coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'strong'))

def logic_3090(agents, world):
    # surface_water -> pathogen_risk; limited coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'limited'))

def logic_3091(agents, world):
    # surface_water -> pathogen_risk; pulse coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'pulse'))

def logic_3092(agents, world):
    # surface_water -> pathogen_risk; feedback coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'feedback'))

def logic_3093(agents, world):
    # surface_water -> pathogen_risk; counterpressure coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'counterpressure'))

def logic_3094(agents, world):
    # surface_water -> pathogen_risk; capacity coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'capacity'))

def logic_3095(agents, world):
    # surface_water -> pathogen_risk; reserve coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'reserve'))

def logic_3096(agents, world):
    # surface_water -> pathogen_risk; scarcity coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'scarcity'))

def logic_3097(agents, world):
    # surface_water -> pathogen_risk; stress coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'stress'))

def logic_3098(agents, world):
    # surface_water -> pathogen_risk; recovery coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'recovery'))

def logic_3099(agents, world):
    # surface_water -> pathogen_risk; persistence coupling.
    _update(agents, 'pathogen_risk', _desired(agents, world, 'surface_water', 'pathogen_risk', 'persistence'))

def logic_3100(agents, world):
    # surface_water -> infection_risk; direct coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'direct'))

def logic_3101(agents, world):
    # surface_water -> infection_risk; inverse coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'inverse'))

def logic_3102(agents, world):
    # surface_water -> infection_risk; threshold coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'threshold'))

def logic_3103(agents, world):
    # surface_water -> infection_risk; strong coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'strong'))

def logic_3104(agents, world):
    # surface_water -> infection_risk; limited coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'limited'))

def logic_3105(agents, world):
    # surface_water -> infection_risk; pulse coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'pulse'))

def logic_3106(agents, world):
    # surface_water -> infection_risk; feedback coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'feedback'))

def logic_3107(agents, world):
    # surface_water -> infection_risk; counterpressure coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'counterpressure'))

def logic_3108(agents, world):
    # surface_water -> infection_risk; capacity coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'capacity'))

def logic_3109(agents, world):
    # surface_water -> infection_risk; reserve coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'reserve'))

def logic_3110(agents, world):
    # surface_water -> infection_risk; scarcity coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'scarcity'))

def logic_3111(agents, world):
    # surface_water -> infection_risk; stress coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'stress'))

def logic_3112(agents, world):
    # surface_water -> infection_risk; recovery coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'recovery'))

def logic_3113(agents, world):
    # surface_water -> infection_risk; persistence coupling.
    _update(agents, 'infection_risk', _desired(agents, world, 'surface_water', 'infection_risk', 'persistence'))

def logic_3114(agents, world):
    # surface_water -> alertness; direct coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'direct'))

def logic_3115(agents, world):
    # surface_water -> alertness; inverse coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'inverse'))

def logic_3116(agents, world):
    # surface_water -> alertness; threshold coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'threshold'))

def logic_3117(agents, world):
    # surface_water -> alertness; strong coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'strong'))

def logic_3118(agents, world):
    # surface_water -> alertness; limited coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'limited'))

def logic_3119(agents, world):
    # surface_water -> alertness; pulse coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'pulse'))

def logic_3120(agents, world):
    # surface_water -> alertness; feedback coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'feedback'))

def logic_3121(agents, world):
    # surface_water -> alertness; counterpressure coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'counterpressure'))

def logic_3122(agents, world):
    # surface_water -> alertness; capacity coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'capacity'))

def logic_3123(agents, world):
    # surface_water -> alertness; reserve coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'reserve'))

def logic_3124(agents, world):
    # surface_water -> alertness; scarcity coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'scarcity'))

def logic_3125(agents, world):
    # surface_water -> alertness; stress coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'stress'))

def logic_3126(agents, world):
    # surface_water -> alertness; recovery coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'recovery'))

def logic_3127(agents, world):
    # surface_water -> alertness; persistence coupling.
    _update(agents, 'alertness', _desired(agents, world, 'surface_water', 'alertness', 'persistence'))

def logic_3128(agents, world):
    # surface_water -> fear; direct coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'direct'))

def logic_3129(agents, world):
    # surface_water -> fear; inverse coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'inverse'))

def logic_3130(agents, world):
    # surface_water -> fear; threshold coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'threshold'))

def logic_3131(agents, world):
    # surface_water -> fear; strong coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'strong'))

def logic_3132(agents, world):
    # surface_water -> fear; limited coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'limited'))

def logic_3133(agents, world):
    # surface_water -> fear; pulse coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'pulse'))

def logic_3134(agents, world):
    # surface_water -> fear; feedback coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'feedback'))

def logic_3135(agents, world):
    # surface_water -> fear; counterpressure coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'counterpressure'))

def logic_3136(agents, world):
    # surface_water -> fear; capacity coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'capacity'))

def logic_3137(agents, world):
    # surface_water -> fear; reserve coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'reserve'))

def logic_3138(agents, world):
    # surface_water -> fear; scarcity coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'scarcity'))

def logic_3139(agents, world):
    # surface_water -> fear; stress coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'stress'))

def logic_3140(agents, world):
    # surface_water -> fear; recovery coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'recovery'))

def logic_3141(agents, world):
    # surface_water -> fear; persistence coupling.
    _update(agents, 'fear', _desired(agents, world, 'surface_water', 'fear', 'persistence'))

def logic_3142(agents, world):
    # surface_water -> recovery; direct coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'direct'))

def logic_3143(agents, world):
    # surface_water -> recovery; inverse coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'inverse'))

def logic_3144(agents, world):
    # surface_water -> recovery; threshold coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'threshold'))

def logic_3145(agents, world):
    # surface_water -> recovery; strong coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'strong'))

def logic_3146(agents, world):
    # surface_water -> recovery; limited coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'limited'))

def logic_3147(agents, world):
    # surface_water -> recovery; pulse coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'pulse'))

def logic_3148(agents, world):
    # surface_water -> recovery; feedback coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'feedback'))

def logic_3149(agents, world):
    # surface_water -> recovery; counterpressure coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'counterpressure'))

def logic_3150(agents, world):
    # surface_water -> recovery; capacity coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'capacity'))

def logic_3151(agents, world):
    # surface_water -> recovery; reserve coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'reserve'))

def logic_3152(agents, world):
    # surface_water -> recovery; scarcity coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'scarcity'))

def logic_3153(agents, world):
    # surface_water -> recovery; stress coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'stress'))
