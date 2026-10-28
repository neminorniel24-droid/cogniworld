"""Transparent illustrative reservoir-flow simulation for ecological chemistry."""
import math

def simulate_carbon_cycle(reservoirs, flows, *, steps, dt=1.0):
    """Explicit-Euler transfers preserve total amount; this is not a climate forecast."""
    if not reservoirs or any(not isinstance(k,str) or not k for k in reservoirs):
        raise ValueError("reservoirs must be a non-empty mapping of names to amounts")
    state={}
    for name,value in reservoirs.items():
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:
            raise ValueError(f"reservoir {name!r} must have a finite non-negative amount")
        state[name]=float(value)
    if isinstance(steps,bool) or not isinstance(steps,int) or steps<0: raise ValueError("steps must be a non-negative integer")
    if isinstance(dt,bool) or not isinstance(dt,(int,float)) or not math.isfinite(dt) or dt<=0: raise ValueError("dt must be finite and positive")
    parsed=[]; rates={}
    for flow in flows:
        try: source,target,rate=flow["source"],flow["target"],flow["rate"]
        except (TypeError,KeyError) as exc: raise ValueError("each flow requires source, target and rate") from exc
        if source not in state or target not in state: raise ValueError("flow endpoints must name existing reservoirs")
        if source==target: raise ValueError("self-transfers are not supported")
        if isinstance(rate,bool) or not isinstance(rate,(int,float)) or not math.isfinite(rate) or rate<0:
            raise ValueError("flow rate must be finite and non-negative")
        parsed.append((source,target,float(rate))); rates[source]=rates.get(source,0.0)+float(rate)
    if any(rate*dt>1 for rate in rates.values()):
        raise ValueError("unstable explicit step: outgoing rate * dt must be <= 1 per reservoir")
    for _ in range(steps):
        delta={name:0.0 for name in state}
        for source,target,rate in parsed:
            amount=state[source]*rate*dt; delta[source]-=amount; delta[target]+=amount
        state={name:value+delta[name] for name,value in state.items()}
        if any(value < -1e-10 for value in state.values()): raise ArithmeticError("negative reservoir generated")
        state={name:max(0.0,value) for name,value in state.items()}
    return state
