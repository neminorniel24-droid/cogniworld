import torch
_RATE=0.00025
def _couple(world,source,target,gain=1.0,mode="positive"):
    s=getattr(world,source,None); t=getattr(world,target,None)
    if s is None or t is None: return
    s=s.clamp(0.0,1.0)
    if mode=="negative": desired=(1.0-s)*gain
    elif mode=="pulse": desired=(s*(1.0-s))*gain
    elif mode=="threshold": desired=(s>0.55).to(s.dtype)*gain
    else: desired=s*gain
    setattr(world,target,(t+_RATE*(desired-t)).clamp(0.0,1.0))

def logic_2002(world):
    # rainfall replenishes accessible water; direct coupling.
    _couple(world,'rain','surface_water',1.0,'positive')

def logic_2003(world):
    # rainfall replenishes accessible water; inverse coupling.
    _couple(world,'rain','surface_water',1.0,'negative')
