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

def logic_2004(world):
    # rainfall replenishes accessible water; limited coupling.
    _couple(world,'rain','surface_water',0.65,'positive')

def logic_2005(world):
    # rainfall replenishes accessible water; strong coupling.
    _couple(world,'rain','surface_water',1.35,'positive')

def logic_2006(world):
    # rainfall replenishes accessible water; threshold coupling.
    _couple(world,'rain','surface_water',1.0,'threshold')

def logic_2007(world):
    # rainfall replenishes accessible water; pulse coupling.
    _couple(world,'rain','surface_water',1.0,'pulse')

def logic_2008(world):
    # rainfall replenishes accessible water; feedback coupling.
    _couple(world,'rain','surface_water',0.8,'positive')

def logic_2009(world):
    # rainfall replenishes accessible water; counterpressure coupling.
    _couple(world,'rain','surface_water',0.8,'negative')

def logic_2010(world):
    # rainfall replenishes accessible water; capacity coupling.
    _couple(world,'rain','surface_water',0.5,'positive')

def logic_2011(world):
    # rainfall replenishes accessible water; reserve coupling.
    _couple(world,'rain','surface_water',0.9,'positive')

def logic_2012(world):
    # rainfall wets soil; direct coupling.
    _couple(world,'rain','soil_moisture',1.0,'positive')

def logic_2013(world):
    # rainfall wets soil; inverse coupling.
    _couple(world,'rain','soil_moisture',1.0,'negative')

def logic_2014(world):
    # rainfall wets soil; limited coupling.
    _couple(world,'rain','soil_moisture',0.65,'positive')

def logic_2015(world):
    # rainfall wets soil; strong coupling.
    _couple(world,'rain','soil_moisture',1.35,'positive')

def logic_2016(world):
    # rainfall wets soil; threshold coupling.
    _couple(world,'rain','soil_moisture',1.0,'threshold')

def logic_2017(world):
    # rainfall wets soil; pulse coupling.
    _couple(world,'rain','soil_moisture',1.0,'pulse')

def logic_2018(world):
    # rainfall wets soil; feedback coupling.
    _couple(world,'rain','soil_moisture',0.8,'positive')
