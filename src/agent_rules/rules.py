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
def logic_306(agents,world):
 v=_local(world,agents,'groundwater');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_307(agents,world):
 v=_local(world,agents,'groundwater');agents.thirst=_delta(agents.thirst,v*0.001)
def logic_308(agents,world):
 v=_local(world,agents,'groundwater');agents.migration_drive=_delta(agents.migration_drive,v*0.001)
def logic_309(agents,world):
 v=_local(world,agents,'soil_moisture');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_310(agents,world):
 v=_local(world,agents,'soil_moisture');agents.hunger=_delta(agents.hunger,v*0.001)
def logic_311(agents,world):
 v=_local(world,agents,'soil_moisture');agents.reproduction_drive=_delta(agents.reproduction_drive,v*0.001)
def logic_312(agents,world):
 v=_local(world,agents,'rain');agents.hydration=_delta(agents.hydration,v*0.001)
def logic_313(agents,world):
 v=_local(world,agents,'rain');agents.health=_delta(agents.health,v*0.001)
