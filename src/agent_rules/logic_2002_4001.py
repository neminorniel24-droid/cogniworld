import torch
def _local(world,agents,name):
    x,y=agents.pos[:,0],agents.pos[:,1]; f=getattr(world,name,None)
    return torch.zeros_like(agents.energy) if f is None else f[y,x].to(agents.energy.dtype)
def _adjust(agents,name,value,rate=0.0005):
    if not hasattr(agents,name): return
    cur=getattr(agents,name); setattr(agents,name,(cur+rate*(value-cur)).clamp(0.0,1.0))
def _drive(agents,world,source,target,sign=1.0):
    s=_local(world,agents,source).clamp(0.0,1.0)
    if sign<0: s=1.0-s
    _adjust(agents,target,s)
