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

def logic_2189(world):
    # fire increases ash; counterpressure coupling.
    _couple(world,'fire_risk','ash',0.8,'negative')

def logic_2190(world):
    # fire increases ash; capacity coupling.
    _couple(world,'fire_risk','ash',0.5,'positive')

def logic_2191(world):
    # fire increases ash; reserve coupling.
    _couple(world,'fire_risk','ash',0.9,'positive')

def logic_2192(world):
    # ash alters soil carbon; direct coupling.
    _couple(world,'ash','soil_carbon',1.0,'positive')

def logic_2193(world):
    # ash alters soil carbon; inverse coupling.
    _couple(world,'ash','soil_carbon',1.0,'negative')

def logic_2194(world):
    # ash alters soil carbon; limited coupling.
    _couple(world,'ash','soil_carbon',0.65,'positive')

def logic_2195(world):
    # ash alters soil carbon; strong coupling.
    _couple(world,'ash','soil_carbon',1.35,'positive')

def logic_2196(world):
    # ash alters soil carbon; threshold coupling.
    _couple(world,'ash','soil_carbon',1.0,'threshold')

def logic_2197(world):
    # ash alters soil carbon; pulse coupling.
    _couple(world,'ash','soil_carbon',1.0,'pulse')

def logic_2198(world):
    # ash alters soil carbon; feedback coupling.
    _couple(world,'ash','soil_carbon',0.8,'positive')

def logic_2199(world):
    # ash alters soil carbon; counterpressure coupling.
    _couple(world,'ash','soil_carbon',0.8,'negative')

def logic_2200(world):
    # ash alters soil carbon; capacity coupling.
    _couple(world,'ash','soil_carbon',0.5,'positive')

def logic_2201(world):
    # ash alters soil carbon; reserve coupling.
    _couple(world,'ash','soil_carbon',0.9,'positive')

def logic_2202(world):
    # fire removes deadwood; direct coupling.
    _couple(world,'fire_risk','deadwood',1.0,'positive')

def logic_2203(world):
    # fire removes deadwood; inverse coupling.
    _couple(world,'fire_risk','deadwood',1.0,'negative')

def logic_2204(world):
    # fire removes deadwood; limited coupling.
    _couple(world,'fire_risk','deadwood',0.65,'positive')

def logic_2205(world):
    # fire removes deadwood; strong coupling.
    _couple(world,'fire_risk','deadwood',1.35,'positive')

def logic_2206(world):
    # fire removes deadwood; threshold coupling.
    _couple(world,'fire_risk','deadwood',1.0,'threshold')

def logic_2207(world):
    # fire removes deadwood; pulse coupling.
    _couple(world,'fire_risk','deadwood',1.0,'pulse')

def logic_2208(world):
    # fire removes deadwood; feedback coupling.
    _couple(world,'fire_risk','deadwood',0.8,'positive')

def logic_2209(world):
    # fire removes deadwood; counterpressure coupling.
    _couple(world,'fire_risk','deadwood',0.8,'negative')

def logic_2210(world):
    # fire removes deadwood; capacity coupling.
    _couple(world,'fire_risk','deadwood',0.5,'positive')

def logic_2211(world):
    # fire removes deadwood; reserve coupling.
    _couple(world,'fire_risk','deadwood',0.9,'positive')

def logic_2212(world):
    # deadwood feeds organic matter; direct coupling.
    _couple(world,'deadwood','organic_matter',1.0,'positive')

def logic_2213(world):
    # deadwood feeds organic matter; inverse coupling.
    _couple(world,'deadwood','organic_matter',1.0,'negative')

def logic_2214(world):
    # deadwood feeds organic matter; limited coupling.
    _couple(world,'deadwood','organic_matter',0.65,'positive')

def logic_2215(world):
    # deadwood feeds organic matter; strong coupling.
    _couple(world,'deadwood','organic_matter',1.35,'positive')

def logic_2216(world):
    # deadwood feeds organic matter; threshold coupling.
    _couple(world,'deadwood','organic_matter',1.0,'threshold')

def logic_2217(world):
    # deadwood feeds organic matter; pulse coupling.
    _couple(world,'deadwood','organic_matter',1.0,'pulse')

def logic_2218(world):
    # deadwood feeds organic matter; feedback coupling.
    _couple(world,'deadwood','organic_matter',0.8,'positive')

def logic_2219(world):
    # deadwood feeds organic matter; counterpressure coupling.
    _couple(world,'deadwood','organic_matter',0.8,'negative')

def logic_2220(world):
    # deadwood feeds organic matter; capacity coupling.
    _couple(world,'deadwood','organic_matter',0.5,'positive')

def logic_2221(world):
    # deadwood feeds organic matter; reserve coupling.
    _couple(world,'deadwood','organic_matter',0.9,'positive')

def logic_2222(world):
    # decomposition releases nutrients; direct coupling.
    _couple(world,'decomposition_rate','nutrients',1.0,'positive')

def logic_2223(world):
    # decomposition releases nutrients; inverse coupling.
    _couple(world,'decomposition_rate','nutrients',1.0,'negative')

def logic_2224(world):
    # decomposition releases nutrients; limited coupling.
    _couple(world,'decomposition_rate','nutrients',0.65,'positive')

def logic_2225(world):
    # decomposition releases nutrients; strong coupling.
    _couple(world,'decomposition_rate','nutrients',1.35,'positive')

def logic_2226(world):
    # decomposition releases nutrients; threshold coupling.
    _couple(world,'decomposition_rate','nutrients',1.0,'threshold')

def logic_2227(world):
    # decomposition releases nutrients; pulse coupling.
    _couple(world,'decomposition_rate','nutrients',1.0,'pulse')

def logic_2228(world):
    # decomposition releases nutrients; feedback coupling.
    _couple(world,'decomposition_rate','nutrients',0.8,'positive')

def logic_2229(world):
    # decomposition releases nutrients; counterpressure coupling.
    _couple(world,'decomposition_rate','nutrients',0.8,'negative')

def logic_2230(world):
    # decomposition releases nutrients; capacity coupling.
    _couple(world,'decomposition_rate','nutrients',0.5,'positive')

def logic_2231(world):
    # decomposition releases nutrients; reserve coupling.
    _couple(world,'decomposition_rate','nutrients',0.9,'positive')

def logic_2232(world):
    # warmth accelerates decomposition; direct coupling.
    _couple(world,'temperature','decomposition_rate',1.0,'positive')

def logic_2233(world):
    # warmth accelerates decomposition; inverse coupling.
    _couple(world,'temperature','decomposition_rate',1.0,'negative')

def logic_2234(world):
    # warmth accelerates decomposition; limited coupling.
    _couple(world,'temperature','decomposition_rate',0.65,'positive')

def logic_2235(world):
    # warmth accelerates decomposition; strong coupling.
    _couple(world,'temperature','decomposition_rate',1.35,'positive')

def logic_2236(world):
    # warmth accelerates decomposition; threshold coupling.
    _couple(world,'temperature','decomposition_rate',1.0,'threshold')

def logic_2237(world):
    # warmth accelerates decomposition; pulse coupling.
    _couple(world,'temperature','decomposition_rate',1.0,'pulse')

def logic_2238(world):
    # warmth accelerates decomposition; feedback coupling.
    _couple(world,'temperature','decomposition_rate',0.8,'positive')

def logic_2239(world):
    # warmth accelerates decomposition; counterpressure coupling.
    _couple(world,'temperature','decomposition_rate',0.8,'negative')

def logic_2240(world):
    # warmth accelerates decomposition; capacity coupling.
    _couple(world,'temperature','decomposition_rate',0.5,'positive')

def logic_2241(world):
    # warmth accelerates decomposition; reserve coupling.
    _couple(world,'temperature','decomposition_rate',0.9,'positive')

def logic_2242(world):
    # moist soil supports decomposition; direct coupling.
    _couple(world,'soil_moisture','decomposition_rate',1.0,'positive')

def logic_2243(world):
    # moist soil supports decomposition; inverse coupling.
    _couple(world,'soil_moisture','decomposition_rate',1.0,'negative')

def logic_2244(world):
    # moist soil supports decomposition; limited coupling.
    _couple(world,'soil_moisture','decomposition_rate',0.65,'positive')

def logic_2245(world):
    # moist soil supports decomposition; strong coupling.
    _couple(world,'soil_moisture','decomposition_rate',1.35,'positive')

def logic_2246(world):
    # moist soil supports decomposition; threshold coupling.
    _couple(world,'soil_moisture','decomposition_rate',1.0,'threshold')

def logic_2247(world):
    # moist soil supports decomposition; pulse coupling.
    _couple(world,'soil_moisture','decomposition_rate',1.0,'pulse')

def logic_2248(world):
    # moist soil supports decomposition; feedback coupling.
    _couple(world,'soil_moisture','decomposition_rate',0.8,'positive')

def logic_2249(world):
    # moist soil supports decomposition; counterpressure coupling.
    _couple(world,'soil_moisture','decomposition_rate',0.8,'negative')

def logic_2250(world):
    # moist soil supports decomposition; capacity coupling.
    _couple(world,'soil_moisture','decomposition_rate',0.5,'positive')

def logic_2251(world):
    # moist soil supports decomposition; reserve coupling.
    _couple(world,'soil_moisture','decomposition_rate',0.9,'positive')

def logic_2252(world):
    # algae adds organic matter; direct coupling.
    _couple(world,'algae','organic_matter',1.0,'positive')

def logic_2253(world):
    # algae adds organic matter; inverse coupling.
    _couple(world,'algae','organic_matter',1.0,'negative')

def logic_2254(world):
    # algae adds organic matter; limited coupling.
    _couple(world,'algae','organic_matter',0.65,'positive')

def logic_2255(world):
    # algae adds organic matter; strong coupling.
    _couple(world,'algae','organic_matter',1.35,'positive')

def logic_2256(world):
    # algae adds organic matter; threshold coupling.
    _couple(world,'algae','organic_matter',1.0,'threshold')

def logic_2257(world):
    # algae adds organic matter; pulse coupling.
    _couple(world,'algae','organic_matter',1.0,'pulse')

def logic_2258(world):
    # algae adds organic matter; feedback coupling.
    _couple(world,'algae','organic_matter',0.8,'positive')

def logic_2259(world):
    # algae adds organic matter; counterpressure coupling.
    _couple(world,'algae','organic_matter',0.8,'negative')

def logic_2260(world):
    # algae adds organic matter; capacity coupling.
    _couple(world,'algae','organic_matter',0.5,'positive')

def logic_2261(world):
    # algae adds organic matter; reserve coupling.
    _couple(world,'algae','organic_matter',0.9,'positive')

def logic_2262(world):
    # vegetation produces flowers; direct coupling.
    _couple(world,'vegetation','flowers',1.0,'positive')

def logic_2263(world):
    # vegetation produces flowers; inverse coupling.
    _couple(world,'vegetation','flowers',1.0,'negative')

def logic_2264(world):
    # vegetation produces flowers; limited coupling.
    _couple(world,'vegetation','flowers',0.65,'positive')

def logic_2265(world):
    # vegetation produces flowers; strong coupling.
    _couple(world,'vegetation','flowers',1.35,'positive')

def logic_2266(world):
    # vegetation produces flowers; threshold coupling.
    _couple(world,'vegetation','flowers',1.0,'threshold')

def logic_2267(world):
    # vegetation produces flowers; pulse coupling.
    _couple(world,'vegetation','flowers',1.0,'pulse')

def logic_2268(world):
    # vegetation produces flowers; feedback coupling.
    _couple(world,'vegetation','flowers',0.8,'positive')

def logic_2269(world):
    # vegetation produces flowers; counterpressure coupling.
    _couple(world,'vegetation','flowers',0.8,'negative')

def logic_2270(world):
    # vegetation produces flowers; capacity coupling.
    _couple(world,'vegetation','flowers',0.5,'positive')

def logic_2271(world):
    # vegetation produces flowers; reserve coupling.
    _couple(world,'vegetation','flowers',0.9,'positive')

def logic_2272(world):
    # flowers support pollinators; direct coupling.
    _couple(world,'flowers','pollinators',1.0,'positive')

def logic_2273(world):
    # flowers support pollinators; inverse coupling.
    _couple(world,'flowers','pollinators',1.0,'negative')

def logic_2274(world):
    # flowers support pollinators; limited coupling.
    _couple(world,'flowers','pollinators',0.65,'positive')

def logic_2275(world):
    # flowers support pollinators; strong coupling.
    _couple(world,'flowers','pollinators',1.35,'positive')

def logic_2276(world):
    # flowers support pollinators; threshold coupling.
    _couple(world,'flowers','pollinators',1.0,'threshold')

def logic_2277(world):
    # flowers support pollinators; pulse coupling.
    _couple(world,'flowers','pollinators',1.0,'pulse')

def logic_2278(world):
    # flowers support pollinators; feedback coupling.
    _couple(world,'flowers','pollinators',0.8,'positive')

def logic_2279(world):
    # flowers support pollinators; counterpressure coupling.
    _couple(world,'flowers','pollinators',0.8,'negative')

def logic_2280(world):
    # flowers support pollinators; capacity coupling.
    _couple(world,'flowers','pollinators',0.5,'positive')

def logic_2281(world):
    # flowers support pollinators; reserve coupling.
    _couple(world,'flowers','pollinators',0.9,'positive')

def logic_2282(world):
    # pollination replenishes seed bank; direct coupling.
    _couple(world,'pollinators','seed_bank',1.0,'positive')

def logic_2283(world):
    # pollination replenishes seed bank; inverse coupling.
    _couple(world,'pollinators','seed_bank',1.0,'negative')

def logic_2284(world):
    # pollination replenishes seed bank; limited coupling.
    _couple(world,'pollinators','seed_bank',0.65,'positive')

def logic_2285(world):
    # pollination replenishes seed bank; strong coupling.
    _couple(world,'pollinators','seed_bank',1.35,'positive')

def logic_2286(world):
    # pollination replenishes seed bank; threshold coupling.
    _couple(world,'pollinators','seed_bank',1.0,'threshold')

def logic_2287(world):
    # pollination replenishes seed bank; pulse coupling.
    _couple(world,'pollinators','seed_bank',1.0,'pulse')

def logic_2288(world):
    # pollination replenishes seed bank; feedback coupling.
    _couple(world,'pollinators','seed_bank',0.8,'positive')

def logic_2289(world):
    # pollination replenishes seed bank; counterpressure coupling.
    _couple(world,'pollinators','seed_bank',0.8,'negative')

def logic_2290(world):
    # pollination replenishes seed bank; capacity coupling.
    _couple(world,'pollinators','seed_bank',0.5,'positive')

def logic_2291(world):
    # pollination replenishes seed bank; reserve coupling.
    _couple(world,'pollinators','seed_bank',0.9,'positive')

def logic_2292(world):
    # seed bank supports regeneration; direct coupling.
    _couple(world,'seed_bank','vegetation',1.0,'positive')

def logic_2293(world):
    # seed bank supports regeneration; inverse coupling.
    _couple(world,'seed_bank','vegetation',1.0,'negative')

def logic_2294(world):
    # seed bank supports regeneration; limited coupling.
    _couple(world,'seed_bank','vegetation',0.65,'positive')

def logic_2295(world):
    # seed bank supports regeneration; strong coupling.
    _couple(world,'seed_bank','vegetation',1.35,'positive')

def logic_2296(world):
    # seed bank supports regeneration; threshold coupling.
    _couple(world,'seed_bank','vegetation',1.0,'threshold')

def logic_2297(world):
    # seed bank supports regeneration; pulse coupling.
    _couple(world,'seed_bank','vegetation',1.0,'pulse')

def logic_2298(world):
    # seed bank supports regeneration; feedback coupling.
    _couple(world,'seed_bank','vegetation',0.8,'positive')

def logic_2299(world):
    # seed bank supports regeneration; counterpressure coupling.
    _couple(world,'seed_bank','vegetation',0.8,'negative')

def logic_2300(world):
    # seed bank supports regeneration; capacity coupling.
    _couple(world,'seed_bank','vegetation',0.5,'positive')

def logic_2301(world):
    # seed bank supports regeneration; reserve coupling.
    _couple(world,'seed_bank','vegetation',0.9,'positive')

def logic_2302(world):
    # vegetation relieves habitat stress; direct coupling.
    _couple(world,'vegetation','habitat_stress',1.0,'positive')

def logic_2303(world):
    # vegetation relieves habitat stress; inverse coupling.
    _couple(world,'vegetation','habitat_stress',1.0,'negative')

def logic_2304(world):
    # vegetation relieves habitat stress; limited coupling.
    _couple(world,'vegetation','habitat_stress',0.65,'positive')

def logic_2305(world):
    # vegetation relieves habitat stress; strong coupling.
    _couple(world,'vegetation','habitat_stress',1.35,'positive')

def logic_2306(world):
    # vegetation relieves habitat stress; threshold coupling.
    _couple(world,'vegetation','habitat_stress',1.0,'threshold')

def logic_2307(world):
    # vegetation relieves habitat stress; pulse coupling.
    _couple(world,'vegetation','habitat_stress',1.0,'pulse')

def logic_2308(world):
    # vegetation relieves habitat stress; feedback coupling.
    _couple(world,'vegetation','habitat_stress',0.8,'positive')

def logic_2309(world):
    # vegetation relieves habitat stress; counterpressure coupling.
    _couple(world,'vegetation','habitat_stress',0.8,'negative')

def logic_2310(world):
    # vegetation relieves habitat stress; capacity coupling.
    _couple(world,'vegetation','habitat_stress',0.5,'positive')

def logic_2311(world):
    # vegetation relieves habitat stress; reserve coupling.
    _couple(world,'vegetation','habitat_stress',0.9,'positive')

def logic_2312(world):
    # habitat stress suppresses vegetation; direct coupling.
    _couple(world,'habitat_stress','vegetation',1.0,'positive')

def logic_2313(world):
    # habitat stress suppresses vegetation; inverse coupling.
    _couple(world,'habitat_stress','vegetation',1.0,'negative')

def logic_2314(world):
    # habitat stress suppresses vegetation; limited coupling.
    _couple(world,'habitat_stress','vegetation',0.65,'positive')

def logic_2315(world):
    # habitat stress suppresses vegetation; strong coupling.
    _couple(world,'habitat_stress','vegetation',1.35,'positive')

def logic_2316(world):
    # habitat stress suppresses vegetation; threshold coupling.
    _couple(world,'habitat_stress','vegetation',1.0,'threshold')

def logic_2317(world):
    # habitat stress suppresses vegetation; pulse coupling.
    _couple(world,'habitat_stress','vegetation',1.0,'pulse')

def logic_2318(world):
    # habitat stress suppresses vegetation; feedback coupling.
    _couple(world,'habitat_stress','vegetation',0.8,'positive')

def logic_2319(world):
    # habitat stress suppresses vegetation; counterpressure coupling.
    _couple(world,'habitat_stress','vegetation',0.8,'negative')

def logic_2320(world):
    # habitat stress suppresses vegetation; capacity coupling.
    _couple(world,'habitat_stress','vegetation',0.5,'positive')

def logic_2321(world):
    # habitat stress suppresses vegetation; reserve coupling.
    _couple(world,'habitat_stress','vegetation',0.9,'positive')

def logic_2322(world):
    # erosion reduces soil depth; direct coupling.
    _couple(world,'erosion','soil_depth',1.0,'positive')

def logic_2323(world):
    # erosion reduces soil depth; inverse coupling.
    _couple(world,'erosion','soil_depth',1.0,'negative')

def logic_2324(world):
    # erosion reduces soil depth; limited coupling.
    _couple(world,'erosion','soil_depth',0.65,'positive')

def logic_2325(world):
    # erosion reduces soil depth; strong coupling.
    _couple(world,'erosion','soil_depth',1.35,'positive')

def logic_2326(world):
    # erosion reduces soil depth; threshold coupling.
    _couple(world,'erosion','soil_depth',1.0,'threshold')

def logic_2327(world):
    # erosion reduces soil depth; pulse coupling.
    _couple(world,'erosion','soil_depth',1.0,'pulse')

def logic_2328(world):
    # erosion reduces soil depth; feedback coupling.
    _couple(world,'erosion','soil_depth',0.8,'positive')

def logic_2329(world):
    # erosion reduces soil depth; counterpressure coupling.
    _couple(world,'erosion','soil_depth',0.8,'negative')

def logic_2330(world):
    # erosion reduces soil depth; capacity coupling.
    _couple(world,'erosion','soil_depth',0.5,'positive')

def logic_2331(world):
    # erosion reduces soil depth; reserve coupling.
    _couple(world,'erosion','soil_depth',0.9,'positive')

def logic_2332(world):
    # soil depth supports roots; direct coupling.
    _couple(world,'soil_depth','root_density',1.0,'positive')

def logic_2333(world):
    # soil depth supports roots; inverse coupling.
    _couple(world,'soil_depth','root_density',1.0,'negative')

def logic_2334(world):
    # soil depth supports roots; limited coupling.
    _couple(world,'soil_depth','root_density',0.65,'positive')

def logic_2335(world):
    # soil depth supports roots; strong coupling.
    _couple(world,'soil_depth','root_density',1.35,'positive')

def logic_2336(world):
    # soil depth supports roots; threshold coupling.
    _couple(world,'soil_depth','root_density',1.0,'threshold')

def logic_2337(world):
    # soil depth supports roots; pulse coupling.
    _couple(world,'soil_depth','root_density',1.0,'pulse')

def logic_2338(world):
    # soil depth supports roots; feedback coupling.
    _couple(world,'soil_depth','root_density',0.8,'positive')

def logic_2339(world):
    # soil depth supports roots; counterpressure coupling.
    _couple(world,'soil_depth','root_density',0.8,'negative')

def logic_2340(world):
    # soil depth supports roots; capacity coupling.
    _couple(world,'soil_depth','root_density',0.5,'positive')

def logic_2341(world):
    # soil depth supports roots; reserve coupling.
    _couple(world,'soil_depth','root_density',0.9,'positive')

def logic_2342(world):
    # roots improve soil water retention; direct coupling.
    _couple(world,'root_density','soil_moisture',1.0,'positive')

def logic_2343(world):
    # roots improve soil water retention; inverse coupling.
    _couple(world,'root_density','soil_moisture',1.0,'negative')

def logic_2344(world):
    # roots improve soil water retention; limited coupling.
    _couple(world,'root_density','soil_moisture',0.65,'positive')

def logic_2345(world):
    # roots improve soil water retention; strong coupling.
    _couple(world,'root_density','soil_moisture',1.35,'positive')

def logic_2346(world):
    # roots improve soil water retention; threshold coupling.
    _couple(world,'root_density','soil_moisture',1.0,'threshold')

def logic_2347(world):
    # roots improve soil water retention; pulse coupling.
    _couple(world,'root_density','soil_moisture',1.0,'pulse')

def logic_2348(world):
    # roots improve soil water retention; feedback coupling.
    _couple(world,'root_density','soil_moisture',0.8,'positive')

def logic_2349(world):
    # roots improve soil water retention; counterpressure coupling.
    _couple(world,'root_density','soil_moisture',0.8,'negative')

def logic_2350(world):
    # roots improve soil water retention; capacity coupling.
    _couple(world,'root_density','soil_moisture',0.5,'positive')

def logic_2351(world):
    # roots improve soil water retention; reserve coupling.
    _couple(world,'root_density','soil_moisture',0.9,'positive')

def logic_2352(world):
    # runoff transports sediment; direct coupling.
    _couple(world,'runoff','sediment',1.0,'positive')

def logic_2353(world):
    # runoff transports sediment; inverse coupling.
    _couple(world,'runoff','sediment',1.0,'negative')

def logic_2354(world):
    # runoff transports sediment; limited coupling.
    _couple(world,'runoff','sediment',0.65,'positive')

def logic_2355(world):
    # runoff transports sediment; strong coupling.
    _couple(world,'runoff','sediment',1.35,'positive')

def logic_2356(world):
    # runoff transports sediment; threshold coupling.
    _couple(world,'runoff','sediment',1.0,'threshold')

def logic_2357(world):
    # runoff transports sediment; pulse coupling.
    _couple(world,'runoff','sediment',1.0,'pulse')

def logic_2358(world):
    # runoff transports sediment; feedback coupling.
    _couple(world,'runoff','sediment',0.8,'positive')

def logic_2359(world):
    # runoff transports sediment; counterpressure coupling.
    _couple(world,'runoff','sediment',0.8,'negative')

def logic_2360(world):
    # runoff transports sediment; capacity coupling.
    _couple(world,'runoff','sediment',0.5,'positive')

def logic_2361(world):
    # runoff transports sediment; reserve coupling.
    _couple(world,'runoff','sediment',0.9,'positive')

def logic_2362(world):
    # sediment can rebuild soil depth; direct coupling.
    _couple(world,'sediment','soil_depth',1.0,'positive')

def logic_2363(world):
    # sediment can rebuild soil depth; inverse coupling.
    _couple(world,'sediment','soil_depth',1.0,'negative')

def logic_2364(world):
    # sediment can rebuild soil depth; limited coupling.
    _couple(world,'sediment','soil_depth',0.65,'positive')

def logic_2365(world):
    # sediment can rebuild soil depth; strong coupling.
    _couple(world,'sediment','soil_depth',1.35,'positive')

def logic_2366(world):
    # sediment can rebuild soil depth; threshold coupling.
    _couple(world,'sediment','soil_depth',1.0,'threshold')

def logic_2367(world):
    # sediment can rebuild soil depth; pulse coupling.
    _couple(world,'sediment','soil_depth',1.0,'pulse')

def logic_2368(world):
    # sediment can rebuild soil depth; feedback coupling.
    _couple(world,'sediment','soil_depth',0.8,'positive')

def logic_2369(world):
    # sediment can rebuild soil depth; counterpressure coupling.
    _couple(world,'sediment','soil_depth',0.8,'negative')

def logic_2370(world):
    # sediment can rebuild soil depth; capacity coupling.
    _couple(world,'sediment','soil_depth',0.5,'positive')

def logic_2371(world):
    # sediment can rebuild soil depth; reserve coupling.
    _couple(world,'sediment','soil_depth',0.9,'positive')

def logic_2372(world):
    # salinity stresses vegetation; direct coupling.
    _couple(world,'salinity','vegetation',1.0,'positive')

def logic_2373(world):
    # salinity stresses vegetation; inverse coupling.
    _couple(world,'salinity','vegetation',1.0,'negative')

def logic_2374(world):
    # salinity stresses vegetation; limited coupling.
    _couple(world,'salinity','vegetation',0.65,'positive')

def logic_2375(world):
    # salinity stresses vegetation; strong coupling.
    _couple(world,'salinity','vegetation',1.35,'positive')

def logic_2376(world):
    # salinity stresses vegetation; threshold coupling.
    _couple(world,'salinity','vegetation',1.0,'threshold')

def logic_2377(world):
    # salinity stresses vegetation; pulse coupling.
    _couple(world,'salinity','vegetation',1.0,'pulse')

def logic_2378(world):
    # salinity stresses vegetation; feedback coupling.
    _couple(world,'salinity','vegetation',0.8,'positive')

def logic_2379(world):
    # salinity stresses vegetation; counterpressure coupling.
    _couple(world,'salinity','vegetation',0.8,'negative')

def logic_2380(world):
    # salinity stresses vegetation; capacity coupling.
    _couple(world,'salinity','vegetation',0.5,'positive')

def logic_2381(world):
    # salinity stresses vegetation; reserve coupling.
    _couple(world,'salinity','vegetation',0.9,'positive')

def logic_2382(world):
    # wetland conditions promote methane; direct coupling.
    _couple(world,'wetland','methane',1.0,'positive')

def logic_2383(world):
    # wetland conditions promote methane; inverse coupling.
    _couple(world,'wetland','methane',1.0,'negative')

def logic_2384(world):
    # wetland conditions promote methane; limited coupling.
    _couple(world,'wetland','methane',0.65,'positive')

def logic_2385(world):
    # wetland conditions promote methane; strong coupling.
    _couple(world,'wetland','methane',1.35,'positive')

def logic_2386(world):
    # wetland conditions promote methane; threshold coupling.
    _couple(world,'wetland','methane',1.0,'threshold')

def logic_2387(world):
    # wetland conditions promote methane; pulse coupling.
    _couple(world,'wetland','methane',1.0,'pulse')

def logic_2388(world):
    # wetland conditions promote methane; feedback coupling.
    _couple(world,'wetland','methane',0.8,'positive')

def logic_2389(world):
    # wetland conditions promote methane; counterpressure coupling.
    _couple(world,'wetland','methane',0.8,'negative')

def logic_2390(world):
    # wetland conditions promote methane; capacity coupling.
    _couple(world,'wetland','methane',0.5,'positive')

def logic_2391(world):
    # wetland conditions promote methane; reserve coupling.
    _couple(world,'wetland','methane',0.9,'positive')

def logic_2392(world):
    # oxygen availability shapes decomposition; direct coupling.
    _couple(world,'oxygen','decomposition_rate',1.0,'positive')

def logic_2393(world):
    # oxygen availability shapes decomposition; inverse coupling.
    _couple(world,'oxygen','decomposition_rate',1.0,'negative')

def logic_2394(world):
    # oxygen availability shapes decomposition; limited coupling.
    _couple(world,'oxygen','decomposition_rate',0.65,'positive')

def logic_2395(world):
    # oxygen availability shapes decomposition; strong coupling.
    _couple(world,'oxygen','decomposition_rate',1.35,'positive')

def logic_2396(world):
    # oxygen availability shapes decomposition; threshold coupling.
    _couple(world,'oxygen','decomposition_rate',1.0,'threshold')

def logic_2397(world):
    # oxygen availability shapes decomposition; pulse coupling.
    _couple(world,'oxygen','decomposition_rate',1.0,'pulse')

def logic_2398(world):
    # oxygen availability shapes decomposition; feedback coupling.
    _couple(world,'oxygen','decomposition_rate',0.8,'positive')

def logic_2399(world):
    # oxygen availability shapes decomposition; counterpressure coupling.
    _couple(world,'oxygen','decomposition_rate',0.8,'negative')

def logic_2400(world):
    # oxygen availability shapes decomposition; capacity coupling.
    _couple(world,'oxygen','decomposition_rate',0.5,'positive')

def logic_2401(world):
    # oxygen availability shapes decomposition; reserve coupling.
    _couple(world,'oxygen','decomposition_rate',0.9,'positive')

def logic_2402(world):
    # CO2 supports photosynthesis; direct coupling.
    _couple(world,'co2','vegetation',1.0,'positive')

def logic_2403(world):
    # CO2 supports photosynthesis; inverse coupling.
    _couple(world,'co2','vegetation',1.0,'negative')

def logic_2404(world):
    # CO2 supports photosynthesis; limited coupling.
    _couple(world,'co2','vegetation',0.65,'positive')

def logic_2405(world):
    # CO2 supports photosynthesis; strong coupling.
    _couple(world,'co2','vegetation',1.35,'positive')

def logic_2406(world):
    # CO2 supports photosynthesis; threshold coupling.
    _couple(world,'co2','vegetation',1.0,'threshold')

def logic_2407(world):
    # CO2 supports photosynthesis; pulse coupling.
    _couple(world,'co2','vegetation',1.0,'pulse')

def logic_2408(world):
    # CO2 supports photosynthesis; feedback coupling.
    _couple(world,'co2','vegetation',0.8,'positive')

def logic_2409(world):
    # CO2 supports photosynthesis; counterpressure coupling.
    _couple(world,'co2','vegetation',0.8,'negative')

def logic_2410(world):
    # CO2 supports photosynthesis; capacity coupling.
    _couple(world,'co2','vegetation',0.5,'positive')

def logic_2411(world):
    # CO2 supports photosynthesis; reserve coupling.
    _couple(world,'co2','vegetation',0.9,'positive')

def logic_2412(world):
    # photosynthetic efficiency supports vegetation; direct coupling.
    _couple(world,'photosynthesis_factor','vegetation',1.0,'positive')

def logic_2413(world):
    # photosynthetic efficiency supports vegetation; inverse coupling.
    _couple(world,'photosynthesis_factor','vegetation',1.0,'negative')

def logic_2414(world):
    # photosynthetic efficiency supports vegetation; limited coupling.
    _couple(world,'photosynthesis_factor','vegetation',0.65,'positive')

def logic_2415(world):
    # photosynthetic efficiency supports vegetation; strong coupling.
    _couple(world,'photosynthesis_factor','vegetation',1.35,'positive')

def logic_2416(world):
    # photosynthetic efficiency supports vegetation; threshold coupling.
    _couple(world,'photosynthesis_factor','vegetation',1.0,'threshold')

def logic_2417(world):
    # photosynthetic efficiency supports vegetation; pulse coupling.
    _couple(world,'photosynthesis_factor','vegetation',1.0,'pulse')

def logic_2418(world):
    # photosynthetic efficiency supports vegetation; feedback coupling.
    _couple(world,'photosynthesis_factor','vegetation',0.8,'positive')

def logic_2419(world):
    # photosynthetic efficiency supports vegetation; counterpressure coupling.
    _couple(world,'photosynthesis_factor','vegetation',0.8,'negative')

def logic_2420(world):
    # photosynthetic efficiency supports vegetation; capacity coupling.
    _couple(world,'photosynthesis_factor','vegetation',0.5,'positive')

def logic_2421(world):
    # photosynthetic efficiency supports vegetation; reserve coupling.
    _couple(world,'photosynthesis_factor','vegetation',0.9,'positive')

def logic_2422(world):
    # cloud formation supports rainfall; direct coupling.
    _couple(world,'cloud','rain',1.0,'positive')

def logic_2423(world):
    # cloud formation supports rainfall; inverse coupling.
    _couple(world,'cloud','rain',1.0,'negative')

def logic_2424(world):
    # cloud formation supports rainfall; limited coupling.
    _couple(world,'cloud','rain',0.65,'positive')

def logic_2425(world):
    # cloud formation supports rainfall; strong coupling.
    _couple(world,'cloud','rain',1.35,'positive')

def logic_2426(world):
    # cloud formation supports rainfall; threshold coupling.
    _couple(world,'cloud','rain',1.0,'threshold')

def logic_2427(world):
    # cloud formation supports rainfall; pulse coupling.
    _couple(world,'cloud','rain',1.0,'pulse')

def logic_2428(world):
    # cloud formation supports rainfall; feedback coupling.
    _couple(world,'cloud','rain',0.8,'positive')

def logic_2429(world):
    # cloud formation supports rainfall; counterpressure coupling.
    _couple(world,'cloud','rain',0.8,'negative')

def logic_2430(world):
    # cloud formation supports rainfall; capacity coupling.
    _couple(world,'cloud','rain',0.5,'positive')

def logic_2431(world):
    # cloud formation supports rainfall; reserve coupling.
    _couple(world,'cloud','rain',0.9,'positive')

def logic_2432(world):
    # rainfall generates runoff; direct coupling.
    _couple(world,'rain','runoff',1.0,'positive')

def logic_2433(world):
    # rainfall generates runoff; inverse coupling.
    _couple(world,'rain','runoff',1.0,'negative')

def logic_2434(world):
    # rainfall generates runoff; limited coupling.
    _couple(world,'rain','runoff',0.65,'positive')

def logic_2435(world):
    # rainfall generates runoff; strong coupling.
    _couple(world,'rain','runoff',1.35,'positive')

def logic_2436(world):
    # rainfall generates runoff; threshold coupling.
    _couple(world,'rain','runoff',1.0,'threshold')

def logic_2437(world):
    # rainfall generates runoff; pulse coupling.
    _couple(world,'rain','runoff',1.0,'pulse')

def logic_2438(world):
    # rainfall generates runoff; feedback coupling.
    _couple(world,'rain','runoff',0.8,'positive')

def logic_2439(world):
    # rainfall generates runoff; counterpressure coupling.
    _couple(world,'rain','runoff',0.8,'negative')

def logic_2440(world):
    # rainfall generates runoff; capacity coupling.
    _couple(world,'rain','runoff',0.5,'positive')

def logic_2441(world):
    # rainfall generates runoff; reserve coupling.
    _couple(world,'rain','runoff',0.9,'positive')

def logic_2442(world):
    # surface ice contributes to ice cover; direct coupling.
    _couple(world,'surface_ice','ice',1.0,'positive')

def logic_2443(world):
    # surface ice contributes to ice cover; inverse coupling.
    _couple(world,'surface_ice','ice',1.0,'negative')

def logic_2444(world):
    # surface ice contributes to ice cover; limited coupling.
    _couple(world,'surface_ice','ice',0.65,'positive')

def logic_2445(world):
    # surface ice contributes to ice cover; strong coupling.
    _couple(world,'surface_ice','ice',1.35,'positive')

def logic_2446(world):
    # surface ice contributes to ice cover; threshold coupling.
    _couple(world,'surface_ice','ice',1.0,'threshold')

def logic_2447(world):
    # surface ice contributes to ice cover; pulse coupling.
    _couple(world,'surface_ice','ice',1.0,'pulse')

def logic_2448(world):
    # surface ice contributes to ice cover; feedback coupling.
    _couple(world,'surface_ice','ice',0.8,'positive')

def logic_2449(world):
    # surface ice contributes to ice cover; counterpressure coupling.
    _couple(world,'surface_ice','ice',0.8,'negative')

def logic_2450(world):
    # surface ice contributes to ice cover; capacity coupling.
    _couple(world,'surface_ice','ice',0.5,'positive')

def logic_2451(world):
    # surface ice contributes to ice cover; reserve coupling.
    _couple(world,'surface_ice','ice',0.9,'positive')

def logic_2452(world):
    # fire reduces stored carbon; direct coupling.
    _couple(world,'fire_risk','carbon_storage',1.0,'positive')

def logic_2453(world):
    # fire reduces stored carbon; inverse coupling.
    _couple(world,'fire_risk','carbon_storage',1.0,'negative')

def logic_2454(world):
    # fire reduces stored carbon; limited coupling.
    _couple(world,'fire_risk','carbon_storage',0.65,'positive')

def logic_2455(world):
    # fire reduces stored carbon; strong coupling.
    _couple(world,'fire_risk','carbon_storage',1.35,'positive')

def logic_2456(world):
    # fire reduces stored carbon; threshold coupling.
    _couple(world,'fire_risk','carbon_storage',1.0,'threshold')

def logic_2457(world):
    # fire reduces stored carbon; pulse coupling.
    _couple(world,'fire_risk','carbon_storage',1.0,'pulse')

def logic_2458(world):
    # fire reduces stored carbon; feedback coupling.
    _couple(world,'fire_risk','carbon_storage',0.8,'positive')

def logic_2459(world):
    # fire reduces stored carbon; counterpressure coupling.
    _couple(world,'fire_risk','carbon_storage',0.8,'negative')

def logic_2460(world):
    # fire reduces stored carbon; capacity coupling.
    _couple(world,'fire_risk','carbon_storage',0.5,'positive')

def logic_2461(world):
    # fire reduces stored carbon; reserve coupling.
    _couple(world,'fire_risk','carbon_storage',0.9,'positive')

def logic_2462(world):
    # vegetation stores carbon; direct coupling.
    _couple(world,'vegetation','carbon_storage',1.0,'positive')

def logic_2463(world):
    # vegetation stores carbon; inverse coupling.
    _couple(world,'vegetation','carbon_storage',1.0,'negative')

def logic_2464(world):
    # vegetation stores carbon; limited coupling.
    _couple(world,'vegetation','carbon_storage',0.65,'positive')

def logic_2465(world):
    # vegetation stores carbon; strong coupling.
    _couple(world,'vegetation','carbon_storage',1.35,'positive')

def logic_2466(world):
    # vegetation stores carbon; threshold coupling.
    _couple(world,'vegetation','carbon_storage',1.0,'threshold')

def logic_2467(world):
    # vegetation stores carbon; pulse coupling.
    _couple(world,'vegetation','carbon_storage',1.0,'pulse')

def logic_2468(world):
    # vegetation stores carbon; feedback coupling.
    _couple(world,'vegetation','carbon_storage',0.8,'positive')

def logic_2469(world):
    # vegetation stores carbon; counterpressure coupling.
    _couple(world,'vegetation','carbon_storage',0.8,'negative')

def logic_2470(world):
    # vegetation stores carbon; capacity coupling.
    _couple(world,'vegetation','carbon_storage',0.5,'positive')

def logic_2471(world):
    # vegetation stores carbon; reserve coupling.
    _couple(world,'vegetation','carbon_storage',0.9,'positive')

def logic_2472(world):
    # soil carbon stores carbon; direct coupling.
    _couple(world,'soil_carbon','carbon_storage',1.0,'positive')

def logic_2473(world):
    # soil carbon stores carbon; inverse coupling.
    _couple(world,'soil_carbon','carbon_storage',1.0,'negative')

def logic_2474(world):
    # soil carbon stores carbon; limited coupling.
    _couple(world,'soil_carbon','carbon_storage',0.65,'positive')

def logic_2475(world):
    # soil carbon stores carbon; strong coupling.
    _couple(world,'soil_carbon','carbon_storage',1.35,'positive')

def logic_2476(world):
    # soil carbon stores carbon; threshold coupling.
    _couple(world,'soil_carbon','carbon_storage',1.0,'threshold')

def logic_2477(world):
    # soil carbon stores carbon; pulse coupling.
    _couple(world,'soil_carbon','carbon_storage',1.0,'pulse')

def logic_2478(world):
    # soil carbon stores carbon; feedback coupling.
    _couple(world,'soil_carbon','carbon_storage',0.8,'positive')

def logic_2479(world):
    # soil carbon stores carbon; counterpressure coupling.
    _couple(world,'soil_carbon','carbon_storage',0.8,'negative')

def logic_2480(world):
    # soil carbon stores carbon; capacity coupling.
    _couple(world,'soil_carbon','carbon_storage',0.5,'positive')

def logic_2481(world):
    # soil carbon stores carbon; reserve coupling.
    _couple(world,'soil_carbon','carbon_storage',0.9,'positive')

def logic_2482(world):
    # snowmelt supplies surface water; direct coupling.
    _couple(world,'snowpack','surface_water',1.0,'positive')

def logic_2483(world):
    # snowmelt supplies surface water; inverse coupling.
    _couple(world,'snowpack','surface_water',1.0,'negative')

def logic_2484(world):
    # snowmelt supplies surface water; limited coupling.
    _couple(world,'snowpack','surface_water',0.65,'positive')

def logic_2485(world):
    # snowmelt supplies surface water; strong coupling.
    _couple(world,'snowpack','surface_water',1.35,'positive')

def logic_2486(world):
    # snowmelt supplies surface water; threshold coupling.
    _couple(world,'snowpack','surface_water',1.0,'threshold')

def logic_2487(world):
    # snowmelt supplies surface water; pulse coupling.
    _couple(world,'snowpack','surface_water',1.0,'pulse')

def logic_2488(world):
    # snowmelt supplies surface water; feedback coupling.
    _couple(world,'snowpack','surface_water',0.8,'positive')

def logic_2489(world):
    # snowmelt supplies surface water; counterpressure coupling.
    _couple(world,'snowpack','surface_water',0.8,'negative')

def logic_2490(world):
    # snowmelt supplies surface water; capacity coupling.
    _couple(world,'snowpack','surface_water',0.5,'positive')

def logic_2491(world):
    # snowmelt supplies surface water; reserve coupling.
    _couple(world,'snowpack','surface_water',0.9,'positive')

def logic_2492(world):
    # water availability maintains soil moisture; direct coupling.
    _couple(world,'surface_water','soil_moisture',1.0,'positive')

def logic_2493(world):
    # water availability maintains soil moisture; inverse coupling.
    _couple(world,'surface_water','soil_moisture',1.0,'negative')

def logic_2494(world):
    # water availability maintains soil moisture; limited coupling.
    _couple(world,'surface_water','soil_moisture',0.65,'positive')

def logic_2495(world):
    # water availability maintains soil moisture; strong coupling.
    _couple(world,'surface_water','soil_moisture',1.35,'positive')

def logic_2496(world):
    # water availability maintains soil moisture; threshold coupling.
    _couple(world,'surface_water','soil_moisture',1.0,'threshold')

def logic_2497(world):
    # water availability maintains soil moisture; pulse coupling.
    _couple(world,'surface_water','soil_moisture',1.0,'pulse')

def logic_2498(world):
    # water availability maintains soil moisture; feedback coupling.
    _couple(world,'surface_water','soil_moisture',0.8,'positive')

def logic_2499(world):
    # water availability maintains soil moisture; counterpressure coupling.
    _couple(world,'surface_water','soil_moisture',0.8,'negative')

def logic_2500(world):
    # water availability maintains soil moisture; capacity coupling.
    _couple(world,'surface_water','soil_moisture',0.5,'positive')
