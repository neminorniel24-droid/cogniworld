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

def logic_2055(world):
    # organic matter builds soil carbon; strong coupling.
    _couple(world,'organic_matter','soil_carbon',1.35,'positive')

def logic_2056(world):
    # organic matter builds soil carbon; threshold coupling.
    _couple(world,'organic_matter','soil_carbon',1.0,'threshold')

def logic_2057(world):
    # organic matter builds soil carbon; pulse coupling.
    _couple(world,'organic_matter','soil_carbon',1.0,'pulse')

def logic_2058(world):
    # organic matter builds soil carbon; feedback coupling.
    _couple(world,'organic_matter','soil_carbon',0.8,'positive')

def logic_2059(world):
    # organic matter builds soil carbon; counterpressure coupling.
    _couple(world,'organic_matter','soil_carbon',0.8,'negative')

def logic_2060(world):
    # organic matter builds soil carbon; capacity coupling.
    _couple(world,'organic_matter','soil_carbon',0.5,'positive')

def logic_2061(world):
    # organic matter builds soil carbon; reserve coupling.
    _couple(world,'organic_matter','soil_carbon',0.9,'positive')

def logic_2062(world):
    # soil carbon retains nutrients; direct coupling.
    _couple(world,'soil_carbon','nutrients',1.0,'positive')

def logic_2063(world):
    # soil carbon retains nutrients; inverse coupling.
    _couple(world,'soil_carbon','nutrients',1.0,'negative')

def logic_2064(world):
    # soil carbon retains nutrients; limited coupling.
    _couple(world,'soil_carbon','nutrients',0.65,'positive')

def logic_2065(world):
    # soil carbon retains nutrients; strong coupling.
    _couple(world,'soil_carbon','nutrients',1.35,'positive')

def logic_2066(world):
    # soil carbon retains nutrients; threshold coupling.
    _couple(world,'soil_carbon','nutrients',1.0,'threshold')

def logic_2067(world):
    # soil carbon retains nutrients; pulse coupling.
    _couple(world,'soil_carbon','nutrients',1.0,'pulse')

def logic_2068(world):
    # soil carbon retains nutrients; feedback coupling.
    _couple(world,'soil_carbon','nutrients',0.8,'positive')

def logic_2069(world):
    # soil carbon retains nutrients; counterpressure coupling.
    _couple(world,'soil_carbon','nutrients',0.8,'negative')

def logic_2070(world):
    # soil carbon retains nutrients; capacity coupling.
    _couple(world,'soil_carbon','nutrients',0.5,'positive')

def logic_2071(world):
    # soil carbon retains nutrients; reserve coupling.
    _couple(world,'soil_carbon','nutrients',0.9,'positive')

def logic_2072(world):
    # nutrients support plant growth; direct coupling.
    _couple(world,'nutrients','vegetation',1.0,'positive')

def logic_2073(world):
    # nutrients support plant growth; inverse coupling.
    _couple(world,'nutrients','vegetation',1.0,'negative')

def logic_2074(world):
    # nutrients support plant growth; limited coupling.
    _couple(world,'nutrients','vegetation',0.65,'positive')

def logic_2075(world):
    # nutrients support plant growth; strong coupling.
    _couple(world,'nutrients','vegetation',1.35,'positive')

def logic_2076(world):
    # nutrients support plant growth; threshold coupling.
    _couple(world,'nutrients','vegetation',1.0,'threshold')

def logic_2077(world):
    # nutrients support plant growth; pulse coupling.
    _couple(world,'nutrients','vegetation',1.0,'pulse')

def logic_2078(world):
    # nutrients support plant growth; feedback coupling.
    _couple(world,'nutrients','vegetation',0.8,'positive')

def logic_2079(world):
    # nutrients support plant growth; counterpressure coupling.
    _couple(world,'nutrients','vegetation',0.8,'negative')

def logic_2080(world):
    # nutrients support plant growth; capacity coupling.
    _couple(world,'nutrients','vegetation',0.5,'positive')

def logic_2081(world):
    # nutrients support plant growth; reserve coupling.
    _couple(world,'nutrients','vegetation',0.9,'positive')

def logic_2082(world):
    # heat increases evaporation; direct coupling.
    _couple(world,'temperature','evaporation',1.0,'positive')

def logic_2083(world):
    # heat increases evaporation; inverse coupling.
    _couple(world,'temperature','evaporation',1.0,'negative')

def logic_2084(world):
    # heat increases evaporation; limited coupling.
    _couple(world,'temperature','evaporation',0.65,'positive')

def logic_2085(world):
    # heat increases evaporation; strong coupling.
    _couple(world,'temperature','evaporation',1.35,'positive')

def logic_2086(world):
    # heat increases evaporation; threshold coupling.
    _couple(world,'temperature','evaporation',1.0,'threshold')

def logic_2087(world):
    # heat increases evaporation; pulse coupling.
    _couple(world,'temperature','evaporation',1.0,'pulse')

def logic_2088(world):
    # heat increases evaporation; feedback coupling.
    _couple(world,'temperature','evaporation',0.8,'positive')

def logic_2089(world):
    # heat increases evaporation; counterpressure coupling.
    _couple(world,'temperature','evaporation',0.8,'negative')

def logic_2090(world):
    # heat increases evaporation; capacity coupling.
    _couple(world,'temperature','evaporation',0.5,'positive')

def logic_2091(world):
    # heat increases evaporation; reserve coupling.
    _couple(world,'temperature','evaporation',0.9,'positive')

def logic_2092(world):
    # humidity suppresses evaporation; direct coupling.
    _couple(world,'humidity','evaporation',1.0,'positive')

def logic_2093(world):
    # humidity suppresses evaporation; inverse coupling.
    _couple(world,'humidity','evaporation',1.0,'negative')

def logic_2094(world):
    # humidity suppresses evaporation; limited coupling.
    _couple(world,'humidity','evaporation',0.65,'positive')

def logic_2095(world):
    # humidity suppresses evaporation; strong coupling.
    _couple(world,'humidity','evaporation',1.35,'positive')

def logic_2096(world):
    # humidity suppresses evaporation; threshold coupling.
    _couple(world,'humidity','evaporation',1.0,'threshold')

def logic_2097(world):
    # humidity suppresses evaporation; pulse coupling.
    _couple(world,'humidity','evaporation',1.0,'pulse')

def logic_2098(world):
    # humidity suppresses evaporation; feedback coupling.
    _couple(world,'humidity','evaporation',0.8,'positive')

def logic_2099(world):
    # humidity suppresses evaporation; counterpressure coupling.
    _couple(world,'humidity','evaporation',0.8,'negative')

def logic_2100(world):
    # humidity suppresses evaporation; capacity coupling.
    _couple(world,'humidity','evaporation',0.5,'positive')

def logic_2101(world):
    # humidity suppresses evaporation; reserve coupling.
    _couple(world,'humidity','evaporation',0.9,'positive')

def logic_2102(world):
    # wind increases evaporative loss; direct coupling.
    _couple(world,'wind_x','evaporation',1.0,'positive')

def logic_2103(world):
    # wind increases evaporative loss; inverse coupling.
    _couple(world,'wind_x','evaporation',1.0,'negative')

def logic_2104(world):
    # wind increases evaporative loss; limited coupling.
    _couple(world,'wind_x','evaporation',0.65,'positive')

def logic_2105(world):
    # wind increases evaporative loss; strong coupling.
    _couple(world,'wind_x','evaporation',1.35,'positive')

def logic_2106(world):
    # wind increases evaporative loss; threshold coupling.
    _couple(world,'wind_x','evaporation',1.0,'threshold')

def logic_2107(world):
    # wind increases evaporative loss; pulse coupling.
    _couple(world,'wind_x','evaporation',1.0,'pulse')

def logic_2108(world):
    # wind increases evaporative loss; feedback coupling.
    _couple(world,'wind_x','evaporation',0.8,'positive')

def logic_2109(world):
    # wind increases evaporative loss; counterpressure coupling.
    _couple(world,'wind_x','evaporation',0.8,'negative')

def logic_2110(world):
    # wind increases evaporative loss; capacity coupling.
    _couple(world,'wind_x','evaporation',0.5,'positive')

def logic_2111(world):
    # wind increases evaporative loss; reserve coupling.
    _couple(world,'wind_x','evaporation',0.9,'positive')

def logic_2112(world):
    # open water adds humidity; direct coupling.
    _couple(world,'surface_water','humidity',1.0,'positive')

def logic_2113(world):
    # open water adds humidity; inverse coupling.
    _couple(world,'surface_water','humidity',1.0,'negative')

def logic_2114(world):
    # open water adds humidity; limited coupling.
    _couple(world,'surface_water','humidity',0.65,'positive')

def logic_2115(world):
    # open water adds humidity; strong coupling.
    _couple(world,'surface_water','humidity',1.35,'positive')

def logic_2116(world):
    # open water adds humidity; threshold coupling.
    _couple(world,'surface_water','humidity',1.0,'threshold')

def logic_2117(world):
    # open water adds humidity; pulse coupling.
    _couple(world,'surface_water','humidity',1.0,'pulse')

def logic_2118(world):
    # open water adds humidity; feedback coupling.
    _couple(world,'surface_water','humidity',0.8,'positive')

def logic_2119(world):
    # open water adds humidity; counterpressure coupling.
    _couple(world,'surface_water','humidity',0.8,'negative')

def logic_2120(world):
    # open water adds humidity; capacity coupling.
    _couple(world,'surface_water','humidity',0.5,'positive')

def logic_2121(world):
    # open water adds humidity; reserve coupling.
    _couple(world,'surface_water','humidity',0.9,'positive')

def logic_2122(world):
    # surface water recharges groundwater; direct coupling.
    _couple(world,'surface_water','groundwater',1.0,'positive')

def logic_2123(world):
    # surface water recharges groundwater; inverse coupling.
    _couple(world,'surface_water','groundwater',1.0,'negative')

def logic_2124(world):
    # surface water recharges groundwater; limited coupling.
    _couple(world,'surface_water','groundwater',0.65,'positive')

def logic_2125(world):
    # surface water recharges groundwater; strong coupling.
    _couple(world,'surface_water','groundwater',1.35,'positive')

def logic_2126(world):
    # surface water recharges groundwater; threshold coupling.
    _couple(world,'surface_water','groundwater',1.0,'threshold')

def logic_2127(world):
    # surface water recharges groundwater; pulse coupling.
    _couple(world,'surface_water','groundwater',1.0,'pulse')

def logic_2128(world):
    # surface water recharges groundwater; feedback coupling.
    _couple(world,'surface_water','groundwater',0.8,'positive')

def logic_2129(world):
    # surface water recharges groundwater; counterpressure coupling.
    _couple(world,'surface_water','groundwater',0.8,'negative')

def logic_2130(world):
    # surface water recharges groundwater; capacity coupling.
    _couple(world,'surface_water','groundwater',0.5,'positive')

def logic_2131(world):
    # surface water recharges groundwater; reserve coupling.
    _couple(world,'surface_water','groundwater',0.9,'positive')

def logic_2132(world):
    # groundwater sustains surface water; direct coupling.
    _couple(world,'groundwater','surface_water',1.0,'positive')

def logic_2133(world):
    # groundwater sustains surface water; inverse coupling.
    _couple(world,'groundwater','surface_water',1.0,'negative')

def logic_2134(world):
    # groundwater sustains surface water; limited coupling.
    _couple(world,'groundwater','surface_water',0.65,'positive')

def logic_2135(world):
    # groundwater sustains surface water; strong coupling.
    _couple(world,'groundwater','surface_water',1.35,'positive')

def logic_2136(world):
    # groundwater sustains surface water; threshold coupling.
    _couple(world,'groundwater','surface_water',1.0,'threshold')

def logic_2137(world):
    # groundwater sustains surface water; pulse coupling.
    _couple(world,'groundwater','surface_water',1.0,'pulse')

def logic_2138(world):
    # groundwater sustains surface water; feedback coupling.
    _couple(world,'groundwater','surface_water',0.8,'positive')

def logic_2139(world):
    # groundwater sustains surface water; counterpressure coupling.
    _couple(world,'groundwater','surface_water',0.8,'negative')

def logic_2140(world):
    # groundwater sustains surface water; capacity coupling.
    _couple(world,'groundwater','surface_water',0.5,'positive')

def logic_2141(world):
    # groundwater sustains surface water; reserve coupling.
    _couple(world,'groundwater','surface_water',0.9,'positive')

def logic_2142(world):
    # rainfall recharges groundwater; direct coupling.
    _couple(world,'rain','groundwater',1.0,'positive')

def logic_2143(world):
    # rainfall recharges groundwater; inverse coupling.
    _couple(world,'rain','groundwater',1.0,'negative')

def logic_2144(world):
    # rainfall recharges groundwater; limited coupling.
    _couple(world,'rain','groundwater',0.65,'positive')

def logic_2145(world):
    # rainfall recharges groundwater; strong coupling.
    _couple(world,'rain','groundwater',1.35,'positive')

def logic_2146(world):
    # rainfall recharges groundwater; threshold coupling.
    _couple(world,'rain','groundwater',1.0,'threshold')

def logic_2147(world):
    # rainfall recharges groundwater; pulse coupling.
    _couple(world,'rain','groundwater',1.0,'pulse')

def logic_2148(world):
    # rainfall recharges groundwater; feedback coupling.
    _couple(world,'rain','groundwater',0.8,'positive')

def logic_2149(world):
    # rainfall recharges groundwater; counterpressure coupling.
    _couple(world,'rain','groundwater',0.8,'negative')

def logic_2150(world):
    # rainfall recharges groundwater; capacity coupling.
    _couple(world,'rain','groundwater',0.5,'positive')

def logic_2151(world):
    # rainfall recharges groundwater; reserve coupling.
    _couple(world,'rain','groundwater',0.9,'positive')

def logic_2152(world):
    # snowmelt feeds groundwater; direct coupling.
    _couple(world,'snowpack','groundwater',1.0,'positive')

def logic_2153(world):
    # snowmelt feeds groundwater; inverse coupling.
    _couple(world,'snowpack','groundwater',1.0,'negative')

def logic_2154(world):
    # snowmelt feeds groundwater; limited coupling.
    _couple(world,'snowpack','groundwater',0.65,'positive')

def logic_2155(world):
    # snowmelt feeds groundwater; strong coupling.
    _couple(world,'snowpack','groundwater',1.35,'positive')

def logic_2156(world):
    # snowmelt feeds groundwater; threshold coupling.
    _couple(world,'snowpack','groundwater',1.0,'threshold')

def logic_2157(world):
    # snowmelt feeds groundwater; pulse coupling.
    _couple(world,'snowpack','groundwater',1.0,'pulse')

def logic_2158(world):
    # snowmelt feeds groundwater; feedback coupling.
    _couple(world,'snowpack','groundwater',0.8,'positive')

def logic_2159(world):
    # snowmelt feeds groundwater; counterpressure coupling.
    _couple(world,'snowpack','groundwater',0.8,'negative')

def logic_2160(world):
    # snowmelt feeds groundwater; capacity coupling.
    _couple(world,'snowpack','groundwater',0.5,'positive')

def logic_2161(world):
    # snowmelt feeds groundwater; reserve coupling.
    _couple(world,'snowpack','groundwater',0.9,'positive')

def logic_2162(world):
    # heat reduces snowpack; direct coupling.
    _couple(world,'temperature','snowpack',1.0,'positive')

def logic_2163(world):
    # heat reduces snowpack; inverse coupling.
    _couple(world,'temperature','snowpack',1.0,'negative')

def logic_2164(world):
    # heat reduces snowpack; limited coupling.
    _couple(world,'temperature','snowpack',0.65,'positive')

def logic_2165(world):
    # heat reduces snowpack; strong coupling.
    _couple(world,'temperature','snowpack',1.35,'positive')

def logic_2166(world):
    # heat reduces snowpack; threshold coupling.
    _couple(world,'temperature','snowpack',1.0,'threshold')

def logic_2167(world):
    # heat reduces snowpack; pulse coupling.
    _couple(world,'temperature','snowpack',1.0,'pulse')

def logic_2168(world):
    # heat reduces snowpack; feedback coupling.
    _couple(world,'temperature','snowpack',0.8,'positive')

def logic_2169(world):
    # heat reduces snowpack; counterpressure coupling.
    _couple(world,'temperature','snowpack',0.8,'negative')

def logic_2170(world):
    # heat reduces snowpack; capacity coupling.
    _couple(world,'temperature','snowpack',0.5,'positive')

def logic_2171(world):
    # heat reduces snowpack; reserve coupling.
    _couple(world,'temperature','snowpack',0.9,'positive')

def logic_2172(world):
    # heat reduces ice; direct coupling.
    _couple(world,'temperature','ice',1.0,'positive')

def logic_2173(world):
    # heat reduces ice; inverse coupling.
    _couple(world,'temperature','ice',1.0,'negative')

def logic_2174(world):
    # heat reduces ice; limited coupling.
    _couple(world,'temperature','ice',0.65,'positive')

def logic_2175(world):
    # heat reduces ice; strong coupling.
    _couple(world,'temperature','ice',1.35,'positive')

def logic_2176(world):
    # heat reduces ice; threshold coupling.
    _couple(world,'temperature','ice',1.0,'threshold')

def logic_2177(world):
    # heat reduces ice; pulse coupling.
    _couple(world,'temperature','ice',1.0,'pulse')

def logic_2178(world):
    # heat reduces ice; feedback coupling.
    _couple(world,'temperature','ice',0.8,'positive')

def logic_2179(world):
    # heat reduces ice; counterpressure coupling.
    _couple(world,'temperature','ice',0.8,'negative')

def logic_2180(world):
    # heat reduces ice; capacity coupling.
    _couple(world,'temperature','ice',0.5,'positive')

def logic_2181(world):
    # heat reduces ice; reserve coupling.
    _couple(world,'temperature','ice',0.9,'positive')

def logic_2182(world):
    # fire increases ash; direct coupling.
    _couple(world,'fire_risk','ash',1.0,'positive')

def logic_2183(world):
    # fire increases ash; inverse coupling.
    _couple(world,'fire_risk','ash',1.0,'negative')

def logic_2184(world):
    # fire increases ash; limited coupling.
    _couple(world,'fire_risk','ash',0.65,'positive')

def logic_2185(world):
    # fire increases ash; strong coupling.
    _couple(world,'fire_risk','ash',1.35,'positive')

def logic_2186(world):
    # fire increases ash; threshold coupling.
    _couple(world,'fire_risk','ash',1.0,'threshold')

def logic_2187(world):
    # fire increases ash; pulse coupling.
    _couple(world,'fire_risk','ash',1.0,'pulse')

def logic_2188(world):
    # fire increases ash; feedback coupling.
    _couple(world,'fire_risk','ash',0.8,'positive')
