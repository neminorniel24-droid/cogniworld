import torch

def _local(world,agents,name):
 x,y=agents.pos[:,0],agents.pos[:,1];return getattr(world,name)[y,x]

def _delta(x,d):return torch.clamp(x+d,0,2)
def logic_303(agents,world):
 v=_local(world,agents,'surface_water');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_304(agents,world):
 v=_local(world,agents,'surface_water');agents.thirst=_delta(agents.thirst,v*0.001)
def logic_305(agents,world):
 v=_local(world,agents,'surface_water');agents.health=_delta(agents.health,v*0.001)
