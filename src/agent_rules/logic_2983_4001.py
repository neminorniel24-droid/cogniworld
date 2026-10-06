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

def logic_3154(agents, world):
    # surface_water -> recovery; recovery coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'recovery'))

def logic_3155(agents, world):
    # surface_water -> recovery; persistence coupling.
    _update(agents, 'recovery', _desired(agents, world, 'surface_water', 'recovery', 'persistence'))

def logic_3156(agents, world):
    # surface_water -> metabolic_cost; direct coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'direct'))

def logic_3157(agents, world):
    # surface_water -> metabolic_cost; inverse coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'inverse'))

def logic_3158(agents, world):
    # surface_water -> metabolic_cost; threshold coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'threshold'))

def logic_3159(agents, world):
    # surface_water -> metabolic_cost; strong coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'strong'))

def logic_3160(agents, world):
    # surface_water -> metabolic_cost; limited coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'limited'))

def logic_3161(agents, world):
    # surface_water -> metabolic_cost; pulse coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'pulse'))

def logic_3162(agents, world):
    # surface_water -> metabolic_cost; feedback coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'feedback'))

def logic_3163(agents, world):
    # surface_water -> metabolic_cost; counterpressure coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'counterpressure'))

def logic_3164(agents, world):
    # surface_water -> metabolic_cost; capacity coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'capacity'))

def logic_3165(agents, world):
    # surface_water -> metabolic_cost; reserve coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'reserve'))

def logic_3166(agents, world):
    # surface_water -> metabolic_cost; scarcity coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'scarcity'))

def logic_3167(agents, world):
    # surface_water -> metabolic_cost; stress coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'stress'))

def logic_3168(agents, world):
    # surface_water -> metabolic_cost; recovery coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'recovery'))

def logic_3169(agents, world):
    # surface_water -> metabolic_cost; persistence coupling.
    _update(agents, 'metabolic_cost', _desired(agents, world, 'surface_water', 'metabolic_cost', 'persistence'))

def logic_3170(agents, world):
    # surface_water -> reproduction_drive; direct coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'direct'))

def logic_3171(agents, world):
    # surface_water -> reproduction_drive; inverse coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'inverse'))

def logic_3172(agents, world):
    # surface_water -> reproduction_drive; threshold coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'threshold'))

def logic_3173(agents, world):
    # surface_water -> reproduction_drive; strong coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'strong'))

def logic_3174(agents, world):
    # surface_water -> reproduction_drive; limited coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'limited'))

def logic_3175(agents, world):
    # surface_water -> reproduction_drive; pulse coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'pulse'))

def logic_3176(agents, world):
    # surface_water -> reproduction_drive; feedback coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'feedback'))

def logic_3177(agents, world):
    # surface_water -> reproduction_drive; counterpressure coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'counterpressure'))

def logic_3178(agents, world):
    # surface_water -> reproduction_drive; capacity coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'capacity'))

def logic_3179(agents, world):
    # surface_water -> reproduction_drive; reserve coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'reserve'))

def logic_3180(agents, world):
    # surface_water -> reproduction_drive; scarcity coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'scarcity'))

def logic_3181(agents, world):
    # surface_water -> reproduction_drive; stress coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'stress'))

def logic_3182(agents, world):
    # surface_water -> reproduction_drive; recovery coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'recovery'))

def logic_3183(agents, world):
    # surface_water -> reproduction_drive; persistence coupling.
    _update(agents, 'reproduction_drive', _desired(agents, world, 'surface_water', 'reproduction_drive', 'persistence'))

def logic_3184(agents, world):
    # surface_water -> migration_drive; direct coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'direct'))

def logic_3185(agents, world):
    # surface_water -> migration_drive; inverse coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'inverse'))

def logic_3186(agents, world):
    # surface_water -> migration_drive; threshold coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'threshold'))

def logic_3187(agents, world):
    # surface_water -> migration_drive; strong coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'strong'))

def logic_3188(agents, world):
    # surface_water -> migration_drive; limited coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'limited'))

def logic_3189(agents, world):
    # surface_water -> migration_drive; pulse coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'pulse'))

def logic_3190(agents, world):
    # surface_water -> migration_drive; feedback coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'feedback'))

def logic_3191(agents, world):
    # surface_water -> migration_drive; counterpressure coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'counterpressure'))

def logic_3192(agents, world):
    # surface_water -> migration_drive; capacity coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'capacity'))

def logic_3193(agents, world):
    # surface_water -> migration_drive; reserve coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'reserve'))

def logic_3194(agents, world):
    # surface_water -> migration_drive; scarcity coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'scarcity'))

def logic_3195(agents, world):
    # surface_water -> migration_drive; stress coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'stress'))

def logic_3196(agents, world):
    # surface_water -> migration_drive; recovery coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'recovery'))

def logic_3197(agents, world):
    # surface_water -> migration_drive; persistence coupling.
    _update(agents, 'migration_drive', _desired(agents, world, 'surface_water', 'migration_drive', 'persistence'))

def logic_3198(agents, world):
    # surface_water -> exploration_drive; direct coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'direct'))

def logic_3199(agents, world):
    # surface_water -> exploration_drive; inverse coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'inverse'))

def logic_3200(agents, world):
    # surface_water -> exploration_drive; threshold coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'threshold'))

def logic_3201(agents, world):
    # surface_water -> exploration_drive; strong coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'strong'))

def logic_3202(agents, world):
    # surface_water -> exploration_drive; limited coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'limited'))

def logic_3203(agents, world):
    # surface_water -> exploration_drive; pulse coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'pulse'))

def logic_3204(agents, world):
    # surface_water -> exploration_drive; feedback coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'feedback'))

def logic_3205(agents, world):
    # surface_water -> exploration_drive; counterpressure coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'counterpressure'))

def logic_3206(agents, world):
    # surface_water -> exploration_drive; capacity coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'capacity'))

def logic_3207(agents, world):
    # surface_water -> exploration_drive; reserve coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'reserve'))

def logic_3208(agents, world):
    # surface_water -> exploration_drive; scarcity coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'scarcity'))

def logic_3209(agents, world):
    # surface_water -> exploration_drive; stress coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'stress'))

def logic_3210(agents, world):
    # surface_water -> exploration_drive; recovery coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'recovery'))

def logic_3211(agents, world):
    # surface_water -> exploration_drive; persistence coupling.
    _update(agents, 'exploration_drive', _desired(agents, world, 'surface_water', 'exploration_drive', 'persistence'))

def logic_3212(agents, world):
    # surface_water -> food_access; direct coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'direct'))

def logic_3213(agents, world):
    # surface_water -> food_access; inverse coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'inverse'))

def logic_3214(agents, world):
    # surface_water -> food_access; threshold coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'threshold'))

def logic_3215(agents, world):
    # surface_water -> food_access; strong coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'strong'))

def logic_3216(agents, world):
    # surface_water -> food_access; limited coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'limited'))

def logic_3217(agents, world):
    # surface_water -> food_access; pulse coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'pulse'))

def logic_3218(agents, world):
    # surface_water -> food_access; feedback coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'feedback'))

def logic_3219(agents, world):
    # surface_water -> food_access; counterpressure coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'counterpressure'))

def logic_3220(agents, world):
    # surface_water -> food_access; capacity coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'capacity'))

def logic_3221(agents, world):
    # surface_water -> food_access; reserve coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'reserve'))

def logic_3222(agents, world):
    # surface_water -> food_access; scarcity coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'scarcity'))

def logic_3223(agents, world):
    # surface_water -> food_access; stress coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'stress'))

def logic_3224(agents, world):
    # surface_water -> food_access; recovery coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'recovery'))

def logic_3225(agents, world):
    # surface_water -> food_access; persistence coupling.
    _update(agents, 'food_access', _desired(agents, world, 'surface_water', 'food_access', 'persistence'))

def logic_3226(agents, world):
    # surface_water -> wealth; direct coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'direct'))

def logic_3227(agents, world):
    # surface_water -> wealth; inverse coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'inverse'))

def logic_3228(agents, world):
    # surface_water -> wealth; threshold coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'threshold'))

def logic_3229(agents, world):
    # surface_water -> wealth; strong coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'strong'))

def logic_3230(agents, world):
    # surface_water -> wealth; limited coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'limited'))

def logic_3231(agents, world):
    # surface_water -> wealth; pulse coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'pulse'))

def logic_3232(agents, world):
    # surface_water -> wealth; feedback coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'feedback'))

def logic_3233(agents, world):
    # surface_water -> wealth; counterpressure coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'counterpressure'))

def logic_3234(agents, world):
    # surface_water -> wealth; capacity coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'capacity'))

def logic_3235(agents, world):
    # surface_water -> wealth; reserve coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'reserve'))

def logic_3236(agents, world):
    # surface_water -> wealth; scarcity coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'scarcity'))

def logic_3237(agents, world):
    # surface_water -> wealth; stress coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'stress'))

def logic_3238(agents, world):
    # surface_water -> wealth; recovery coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'recovery'))

def logic_3239(agents, world):
    # surface_water -> wealth; persistence coupling.
    _update(agents, 'wealth', _desired(agents, world, 'surface_water', 'wealth', 'persistence'))

def logic_3240(agents, world):
    # surface_water -> stability; direct coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'direct'))

def logic_3241(agents, world):
    # surface_water -> stability; inverse coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'inverse'))

def logic_3242(agents, world):
    # surface_water -> stability; threshold coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'threshold'))

def logic_3243(agents, world):
    # surface_water -> stability; strong coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'strong'))

def logic_3244(agents, world):
    # surface_water -> stability; limited coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'limited'))

def logic_3245(agents, world):
    # surface_water -> stability; pulse coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'pulse'))

def logic_3246(agents, world):
    # surface_water -> stability; feedback coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'feedback'))

def logic_3247(agents, world):
    # surface_water -> stability; counterpressure coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'counterpressure'))

def logic_3248(agents, world):
    # surface_water -> stability; capacity coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'capacity'))

def logic_3249(agents, world):
    # surface_water -> stability; reserve coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'reserve'))

def logic_3250(agents, world):
    # surface_water -> stability; scarcity coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'scarcity'))

def logic_3251(agents, world):
    # surface_water -> stability; stress coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'stress'))

def logic_3252(agents, world):
    # surface_water -> stability; recovery coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'recovery'))

def logic_3253(agents, world):
    # surface_water -> stability; persistence coupling.
    _update(agents, 'stability', _desired(agents, world, 'surface_water', 'stability', 'persistence'))

def logic_3254(agents, world):
    # surface_water -> habitat_stress; direct coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'direct'))

def logic_3255(agents, world):
    # surface_water -> habitat_stress; inverse coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'inverse'))

def logic_3256(agents, world):
    # surface_water -> habitat_stress; threshold coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'threshold'))

def logic_3257(agents, world):
    # surface_water -> habitat_stress; strong coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'strong'))

def logic_3258(agents, world):
    # surface_water -> habitat_stress; limited coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'limited'))

def logic_3259(agents, world):
    # surface_water -> habitat_stress; pulse coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'pulse'))

def logic_3260(agents, world):
    # surface_water -> habitat_stress; feedback coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'feedback'))

def logic_3261(agents, world):
    # surface_water -> habitat_stress; counterpressure coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'counterpressure'))

def logic_3262(agents, world):
    # surface_water -> habitat_stress; capacity coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'capacity'))

def logic_3263(agents, world):
    # surface_water -> habitat_stress; reserve coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'reserve'))

def logic_3264(agents, world):
    # surface_water -> habitat_stress; scarcity coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'scarcity'))

def logic_3265(agents, world):
    # surface_water -> habitat_stress; stress coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'stress'))

def logic_3266(agents, world):
    # surface_water -> habitat_stress; recovery coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'recovery'))

def logic_3267(agents, world):
    # surface_water -> habitat_stress; persistence coupling.
    _update(agents, 'habitat_stress', _desired(agents, world, 'surface_water', 'habitat_stress', 'persistence'))

def logic_3268(agents, world):
    # surface_water -> social_tolerance; direct coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'direct'))

def logic_3269(agents, world):
    # surface_water -> social_tolerance; inverse coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'inverse'))

def logic_3270(agents, world):
    # surface_water -> social_tolerance; threshold coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'threshold'))

def logic_3271(agents, world):
    # surface_water -> social_tolerance; strong coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'strong'))

def logic_3272(agents, world):
    # surface_water -> social_tolerance; limited coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'limited'))

def logic_3273(agents, world):
    # surface_water -> social_tolerance; pulse coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'pulse'))

def logic_3274(agents, world):
    # surface_water -> social_tolerance; feedback coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'feedback'))

def logic_3275(agents, world):
    # surface_water -> social_tolerance; counterpressure coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'counterpressure'))

def logic_3276(agents, world):
    # surface_water -> social_tolerance; capacity coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'capacity'))

def logic_3277(agents, world):
    # surface_water -> social_tolerance; reserve coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'reserve'))

def logic_3278(agents, world):
    # surface_water -> social_tolerance; scarcity coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'scarcity'))

def logic_3279(agents, world):
    # surface_water -> social_tolerance; stress coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'stress'))

def logic_3280(agents, world):
    # surface_water -> social_tolerance; recovery coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'recovery'))

def logic_3281(agents, world):
    # surface_water -> social_tolerance; persistence coupling.
    _update(agents, 'social_tolerance', _desired(agents, world, 'surface_water', 'social_tolerance', 'persistence'))

def logic_3282(agents, world):
    # surface_water -> reputation; direct coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'direct'))

def logic_3283(agents, world):
    # surface_water -> reputation; inverse coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'inverse'))

def logic_3284(agents, world):
    # surface_water -> reputation; threshold coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'threshold'))

def logic_3285(agents, world):
    # surface_water -> reputation; strong coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'strong'))

def logic_3286(agents, world):
    # surface_water -> reputation; limited coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'limited'))

def logic_3287(agents, world):
    # surface_water -> reputation; pulse coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'pulse'))

def logic_3288(agents, world):
    # surface_water -> reputation; feedback coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'feedback'))

def logic_3289(agents, world):
    # surface_water -> reputation; counterpressure coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'counterpressure'))

def logic_3290(agents, world):
    # surface_water -> reputation; capacity coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'capacity'))

def logic_3291(agents, world):
    # surface_water -> reputation; reserve coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'reserve'))

def logic_3292(agents, world):
    # surface_water -> reputation; scarcity coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'scarcity'))

def logic_3293(agents, world):
    # surface_water -> reputation; stress coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'stress'))

def logic_3294(agents, world):
    # surface_water -> reputation; recovery coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'recovery'))

def logic_3295(agents, world):
    # surface_water -> reputation; persistence coupling.
    _update(agents, 'reputation', _desired(agents, world, 'surface_water', 'reputation', 'persistence'))

def logic_3296(agents, world):
    # surface_water -> trust; direct coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'direct'))

def logic_3297(agents, world):
    # surface_water -> trust; inverse coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'inverse'))

def logic_3298(agents, world):
    # surface_water -> trust; threshold coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'threshold'))

def logic_3299(agents, world):
    # surface_water -> trust; strong coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'strong'))

def logic_3300(agents, world):
    # surface_water -> trust; limited coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'limited'))

def logic_3301(agents, world):
    # surface_water -> trust; pulse coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'pulse'))

def logic_3302(agents, world):
    # surface_water -> trust; feedback coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'feedback'))

def logic_3303(agents, world):
    # surface_water -> trust; counterpressure coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'counterpressure'))

def logic_3304(agents, world):
    # surface_water -> trust; capacity coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'capacity'))

def logic_3305(agents, world):
    # surface_water -> trust; reserve coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'reserve'))

def logic_3306(agents, world):
    # surface_water -> trust; scarcity coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'scarcity'))

def logic_3307(agents, world):
    # surface_water -> trust; stress coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'stress'))

def logic_3308(agents, world):
    # surface_water -> trust; recovery coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'recovery'))

def logic_3309(agents, world):
    # surface_water -> trust; persistence coupling.
    _update(agents, 'trust', _desired(agents, world, 'surface_water', 'trust', 'persistence'))

def logic_3310(agents, world):
    # surface_water -> cooperation; direct coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'direct'))

def logic_3311(agents, world):
    # surface_water -> cooperation; inverse coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'inverse'))

def logic_3312(agents, world):
    # surface_water -> cooperation; threshold coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'threshold'))

def logic_3313(agents, world):
    # surface_water -> cooperation; strong coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'strong'))

def logic_3314(agents, world):
    # surface_water -> cooperation; limited coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'limited'))

def logic_3315(agents, world):
    # surface_water -> cooperation; pulse coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'pulse'))

def logic_3316(agents, world):
    # surface_water -> cooperation; feedback coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'feedback'))

def logic_3317(agents, world):
    # surface_water -> cooperation; counterpressure coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'counterpressure'))

def logic_3318(agents, world):
    # surface_water -> cooperation; capacity coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'capacity'))

def logic_3319(agents, world):
    # surface_water -> cooperation; reserve coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'reserve'))

def logic_3320(agents, world):
    # surface_water -> cooperation; scarcity coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'scarcity'))

def logic_3321(agents, world):
    # surface_water -> cooperation; stress coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'stress'))

def logic_3322(agents, world):
    # surface_water -> cooperation; recovery coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'recovery'))

def logic_3323(agents, world):
    # surface_water -> cooperation; persistence coupling.
    _update(agents, 'cooperation', _desired(agents, world, 'surface_water', 'cooperation', 'persistence'))

def logic_3324(agents, world):
    # surface_water -> defection; direct coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'direct'))

def logic_3325(agents, world):
    # surface_water -> defection; inverse coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'inverse'))

def logic_3326(agents, world):
    # surface_water -> defection; threshold coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'threshold'))

def logic_3327(agents, world):
    # surface_water -> defection; strong coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'strong'))

def logic_3328(agents, world):
    # surface_water -> defection; limited coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'limited'))

def logic_3329(agents, world):
    # surface_water -> defection; pulse coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'pulse'))

def logic_3330(agents, world):
    # surface_water -> defection; feedback coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'feedback'))

def logic_3331(agents, world):
    # surface_water -> defection; counterpressure coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'counterpressure'))

def logic_3332(agents, world):
    # surface_water -> defection; capacity coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'capacity'))

def logic_3333(agents, world):
    # surface_water -> defection; reserve coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'reserve'))

def logic_3334(agents, world):
    # surface_water -> defection; scarcity coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'scarcity'))

def logic_3335(agents, world):
    # surface_water -> defection; stress coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'stress'))

def logic_3336(agents, world):
    # surface_water -> defection; recovery coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'recovery'))

def logic_3337(agents, world):
    # surface_water -> defection; persistence coupling.
    _update(agents, 'defection', _desired(agents, world, 'surface_water', 'defection', 'persistence'))

def logic_3338(agents, world):
    # surface_water -> aggression; direct coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'direct'))

def logic_3339(agents, world):
    # surface_water -> aggression; inverse coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'inverse'))

def logic_3340(agents, world):
    # surface_water -> aggression; threshold coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'threshold'))

def logic_3341(agents, world):
    # surface_water -> aggression; strong coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'strong'))

def logic_3342(agents, world):
    # surface_water -> aggression; limited coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'limited'))

def logic_3343(agents, world):
    # surface_water -> aggression; pulse coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'pulse'))

def logic_3344(agents, world):
    # surface_water -> aggression; feedback coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'feedback'))

def logic_3345(agents, world):
    # surface_water -> aggression; counterpressure coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'counterpressure'))

def logic_3346(agents, world):
    # surface_water -> aggression; capacity coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'capacity'))

def logic_3347(agents, world):
    # surface_water -> aggression; reserve coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'reserve'))

def logic_3348(agents, world):
    # surface_water -> aggression; scarcity coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'scarcity'))

def logic_3349(agents, world):
    # surface_water -> aggression; stress coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'stress'))

def logic_3350(agents, world):
    # surface_water -> aggression; recovery coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'recovery'))

def logic_3351(agents, world):
    # surface_water -> aggression; persistence coupling.
    _update(agents, 'aggression', _desired(agents, world, 'surface_water', 'aggression', 'persistence'))

def logic_3352(agents, world):
    # surface_water -> conflict_pressure; direct coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'direct'))

def logic_3353(agents, world):
    # surface_water -> conflict_pressure; inverse coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'inverse'))

def logic_3354(agents, world):
    # surface_water -> conflict_pressure; threshold coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'threshold'))

def logic_3355(agents, world):
    # surface_water -> conflict_pressure; strong coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'strong'))

def logic_3356(agents, world):
    # surface_water -> conflict_pressure; limited coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'limited'))

def logic_3357(agents, world):
    # surface_water -> conflict_pressure; pulse coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'pulse'))

def logic_3358(agents, world):
    # surface_water -> conflict_pressure; feedback coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'feedback'))

def logic_3359(agents, world):
    # surface_water -> conflict_pressure; counterpressure coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'counterpressure'))

def logic_3360(agents, world):
    # surface_water -> conflict_pressure; capacity coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'capacity'))

def logic_3361(agents, world):
    # surface_water -> conflict_pressure; reserve coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'reserve'))

def logic_3362(agents, world):
    # surface_water -> conflict_pressure; scarcity coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'scarcity'))

def logic_3363(agents, world):
    # surface_water -> conflict_pressure; stress coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'stress'))

def logic_3364(agents, world):
    # surface_water -> conflict_pressure; recovery coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'recovery'))

def logic_3365(agents, world):
    # surface_water -> conflict_pressure; persistence coupling.
    _update(agents, 'conflict_pressure', _desired(agents, world, 'surface_water', 'conflict_pressure', 'persistence'))

def logic_3366(agents, world):
    # surface_water -> competition_pressure; direct coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'direct'))

def logic_3367(agents, world):
    # surface_water -> competition_pressure; inverse coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'inverse'))

def logic_3368(agents, world):
    # surface_water -> competition_pressure; threshold coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'threshold'))

def logic_3369(agents, world):
    # surface_water -> competition_pressure; strong coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'strong'))

def logic_3370(agents, world):
    # surface_water -> competition_pressure; limited coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'limited'))

def logic_3371(agents, world):
    # surface_water -> competition_pressure; pulse coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'pulse'))

def logic_3372(agents, world):
    # surface_water -> competition_pressure; feedback coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'feedback'))

def logic_3373(agents, world):
    # surface_water -> competition_pressure; counterpressure coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'counterpressure'))

def logic_3374(agents, world):
    # surface_water -> competition_pressure; capacity coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'capacity'))

def logic_3375(agents, world):
    # surface_water -> competition_pressure; reserve coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'reserve'))

def logic_3376(agents, world):
    # surface_water -> competition_pressure; scarcity coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'scarcity'))

def logic_3377(agents, world):
    # surface_water -> competition_pressure; stress coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'stress'))

def logic_3378(agents, world):
    # surface_water -> competition_pressure; recovery coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'recovery'))

def logic_3379(agents, world):
    # surface_water -> competition_pressure; persistence coupling.
    _update(agents, 'competition_pressure', _desired(agents, world, 'surface_water', 'competition_pressure', 'persistence'))

def logic_3380(agents, world):
    # surface_water -> territoriality; direct coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'direct'))

def logic_3381(agents, world):
    # surface_water -> territoriality; inverse coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'inverse'))

def logic_3382(agents, world):
    # surface_water -> territoriality; threshold coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'threshold'))

def logic_3383(agents, world):
    # surface_water -> territoriality; strong coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'strong'))

def logic_3384(agents, world):
    # surface_water -> territoriality; limited coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'limited'))

def logic_3385(agents, world):
    # surface_water -> territoriality; pulse coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'pulse'))

def logic_3386(agents, world):
    # surface_water -> territoriality; feedback coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'feedback'))

def logic_3387(agents, world):
    # surface_water -> territoriality; counterpressure coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'counterpressure'))

def logic_3388(agents, world):
    # surface_water -> territoriality; capacity coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'capacity'))

def logic_3389(agents, world):
    # surface_water -> territoriality; reserve coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'reserve'))

def logic_3390(agents, world):
    # surface_water -> territoriality; scarcity coupling.
    _update(agents, 'territoriality', _desired(agents, world, 'surface_water', 'territoriality', 'scarcity'))
