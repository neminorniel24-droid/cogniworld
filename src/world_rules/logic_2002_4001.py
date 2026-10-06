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

def logic_2019(world):
    # rainfall wets soil; counterpressure coupling.
    _couple(world,'rain','soil_moisture',0.8,'negative')

def logic_2020(world):
    # rainfall wets soil; capacity coupling.
    _couple(world,'rain','soil_moisture',0.5,'positive')

def logic_2021(world):
    # rainfall wets soil; reserve coupling.
    _couple(world,'rain','soil_moisture',0.9,'positive')

def logic_2022(world):
    # soil moisture supports vegetation; direct coupling.
    _couple(world,'soil_moisture','vegetation',1.0,'positive')

def logic_2023(world):
    # soil moisture supports vegetation; inverse coupling.
    _couple(world,'soil_moisture','vegetation',1.0,'negative')

def logic_2024(world):
    # soil moisture supports vegetation; limited coupling.
    _couple(world,'soil_moisture','vegetation',0.65,'positive')

def logic_2025(world):
    # soil moisture supports vegetation; strong coupling.
    _couple(world,'soil_moisture','vegetation',1.35,'positive')

def logic_2026(world):
    # soil moisture supports vegetation; threshold coupling.
    _couple(world,'soil_moisture','vegetation',1.0,'threshold')

def logic_2027(world):
    # soil moisture supports vegetation; pulse coupling.
    _couple(world,'soil_moisture','vegetation',1.0,'pulse')

def logic_2028(world):
    # soil moisture supports vegetation; feedback coupling.
    _couple(world,'soil_moisture','vegetation',0.8,'positive')

def logic_2029(world):
    # soil moisture supports vegetation; counterpressure coupling.
    _couple(world,'soil_moisture','vegetation',0.8,'negative')

def logic_2030(world):
    # soil moisture supports vegetation; capacity coupling.
    _couple(world,'soil_moisture','vegetation',0.5,'positive')

def logic_2031(world):
    # soil moisture supports vegetation; reserve coupling.
    _couple(world,'soil_moisture','vegetation',0.9,'positive')

def logic_2032(world):
    # vegetation builds biomass; direct coupling.
    _couple(world,'vegetation','biomass',1.0,'positive')

def logic_2033(world):
    # vegetation builds biomass; inverse coupling.
    _couple(world,'vegetation','biomass',1.0,'negative')

def logic_2034(world):
    # vegetation builds biomass; limited coupling.
    _couple(world,'vegetation','biomass',0.65,'positive')

def logic_2035(world):
    # vegetation builds biomass; strong coupling.
    _couple(world,'vegetation','biomass',1.35,'positive')

def logic_2036(world):
    # vegetation builds biomass; threshold coupling.
    _couple(world,'vegetation','biomass',1.0,'threshold')

def logic_2037(world):
    # vegetation builds biomass; pulse coupling.
    _couple(world,'vegetation','biomass',1.0,'pulse')

def logic_2038(world):
    # vegetation builds biomass; feedback coupling.
    _couple(world,'vegetation','biomass',0.8,'positive')

def logic_2039(world):
    # vegetation builds biomass; counterpressure coupling.
    _couple(world,'vegetation','biomass',0.8,'negative')

def logic_2040(world):
    # vegetation builds biomass; capacity coupling.
    _couple(world,'vegetation','biomass',0.5,'positive')

def logic_2041(world):
    # vegetation builds biomass; reserve coupling.
    _couple(world,'vegetation','biomass',0.9,'positive')

def logic_2042(world):
    # biomass contributes organic matter; direct coupling.
    _couple(world,'biomass','organic_matter',1.0,'positive')

def logic_2043(world):
    # biomass contributes organic matter; inverse coupling.
    _couple(world,'biomass','organic_matter',1.0,'negative')

def logic_2044(world):
    # biomass contributes organic matter; limited coupling.
    _couple(world,'biomass','organic_matter',0.65,'positive')

def logic_2045(world):
    # biomass contributes organic matter; strong coupling.
    _couple(world,'biomass','organic_matter',1.35,'positive')

def logic_2046(world):
    # biomass contributes organic matter; threshold coupling.
    _couple(world,'biomass','organic_matter',1.0,'threshold')

def logic_2047(world):
    # biomass contributes organic matter; pulse coupling.
    _couple(world,'biomass','organic_matter',1.0,'pulse')

def logic_2048(world):
    # biomass contributes organic matter; feedback coupling.
    _couple(world,'biomass','organic_matter',0.8,'positive')

def logic_2049(world):
    # biomass contributes organic matter; counterpressure coupling.
    _couple(world,'biomass','organic_matter',0.8,'negative')

def logic_2050(world):
    # biomass contributes organic matter; capacity coupling.
    _couple(world,'biomass','organic_matter',0.5,'positive')

def logic_2051(world):
    # biomass contributes organic matter; reserve coupling.
    _couple(world,'biomass','organic_matter',0.9,'positive')

def logic_2052(world):
    # organic matter builds soil carbon; direct coupling.
    _couple(world,'organic_matter','soil_carbon',1.0,'positive')

def logic_2053(world):
    # organic matter builds soil carbon; inverse coupling.
    _couple(world,'organic_matter','soil_carbon',1.0,'negative')

def logic_2054(world):
    # organic matter builds soil carbon; limited coupling.
    _couple(world,'organic_matter','soil_carbon',0.65,'positive')
