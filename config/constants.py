import numpy as np

options_air_temp = [
    {"label": "TA1", "value": "TA1"},
    {"label": "TA2", "value": "TA2"},
    {"label": "TA3", "value": "TA3"},
    {"label": "TA4", "value": "TA4"},
    {"label": "TA1_max", "value": "TA1_max"},
    {"label": "TA1_min", "value": "TA1_min"},
    {"label": "TA2_max", "value": "TA2_max"},
    {"label": "TA2_min", "value": "TA2_min"},
    {"label": "TA2m", "value": "TA2m"},
    {"label": "TA5", "value": "TA5"},
    {"label": "TS1", "value": "TS1"},
    {"label": "TS2", "value": "TS2"},
    {"label": "TS3", "value": "TS3"},
    {"label": "TS4", "value": "TS4"},
    {"label": "TS5", "value": "TS5"},
    {"label": "TS6", "value": "TS6"},
    {"label": "TS7", "value": "TS7"},
    {"label": "TS8", "value": "TS8"},
    {"label": "TS9", "value": "TS9"},
    {"label": "TS10", "value": "TS10"},
    {"label": "Tsurf1", "value": "Tsurf1"},
    {"label": "Tsurf2", "value": "Tsurf2"},
]

options_radiation = [
    {"label": "ISWR", "value": "ISWR"},
    {"label": "ISWR_max", "value": "ISWR_max"},
    {"label": "ISWR_std", "value": "ISWR_std"},
    {"label": "OSWR", "value": "OSWR"},
    {"label": "NR", "value": "NR"},
    {"label": "NR_max", "value": "NR_max"},
    {"label": "NR_std", "value": "NR_std"},
    {"label": "IUVR", "value": "IUVR"},
    {"label": "ILWR", "value": "ILWR"}
]

options_wind_speed = [
    {"label": "VW1", "value": "VW1"},
    {"label": "VW1_max", "value": "VW1_max"},
    {"label": "VW1_stdev", "value": "VW1_stdev"},
    {"label": "VW2", "value": "VW2"},
    {"label": "VW2_max", "value": "VW2_max"},
    {"label": "VW2_stdev", "value": "VW2_stdev"},
    {"label": "VW10m", "value": "VW10m"}
]

options_wind_direction = [
    {"label": "DW1", "value": "DW1"},
    {"label": "DW2", "value": "DW2"}
]

options_humidity = [
    {"label": "RH1", "value": "RH1"},
    {"label": "RH2", "value": "RH2"},
    {"label": "RH2m", "value": "RH2m"}
]

options_pressure = [
    {"label": "P", "value": "P"},
]


options_all = [
    {"label": "ISWR (W/m^2)", "value": "ISWR"},
    {"label": "ISWR_max (W/m^2)", "value": "ISWR_max"},
    {"label": "ISWR_std (W/m^2)", "value": "ISWR_std"},
    {"label": "OSWR (W/m^2)", "value": "OSWR"},
    {"label": "NR (W/m^2)", "value": "NR"},
    {"label": "NR_max (W/m^2)", "value": "NR_max"},
    {"label": "NR_std (W/m^2)", "value": "NR_std"},
    {"label": "TA1 (°C)", "value": "TA1"},
    {"label": "TA1_max (°C)", "value": "TA1_max"},
    {"label": "TA1_min (°C)", "value": "TA1_min"},
    {"label": "TA2 (°C)", "value": "TA2"},
    {"label": "TA2_max (°C)", "value": "TA2_max"},
    {"label": "TA2_min (°C)", "value": "TA2_min"},
    {"label": "TA3 (°C)", "value": "TA3"},
    {"label": "TA4 (°C)", "value": "TA4"},
    {"label": "RH1 (%/100)", "value": "RH1"},
    {"label": "RH2 (%/100)", "value": "RH2"},
    {"label": "VW1 (m/s)", "value": "VW1"},
    {"label": "VW1_max (m/s)", "value": "VW1_max"},
    {"label": "VW1_stdev (m/s)", "value": "VW1_stdev"},
    {"label": "VW2 (m/s)", "value": "VW2"},
    {"label": "VW2_max (m/s)", "value": "VW2_max"},
    {"label": "VW2_stdev(m/s)", "value": "VW2_stdev"},
    {"label": "DW1 (°)", "value": "DW1"},
    {"label": "DW2 (°)", "value": "DW2"},
    {"label": "P (mbar)", "value": "P"},
    {"label": "HS1 (m)", "value": "HS1"},
    {"label": "HS2 (m)", "value": "HS2"},
    {"label": "HW1 (m)", "value": "HW1"},
    {"label": "HW2 (m)", "value": "HW2"},
    {"label": "V (V)", "value": "V"},
    {"label": "TA5 (°C)", "value": "TA5"},
    {"label": "TS1 (°C)", "value": "TS1"},
    {"label": "TS2 (°C)", "value": "TS2"},
    {"label": "TS3 (°C)", "value": "TS3"},
    {"label": "TS4 (°C)", "value": "TS4"},
    {"label": "TS5 (°C)", "value": "TS5"},
    {"label": "TS6 (°C)", "value": "TS6"},
    {"label": "TS7 (°C)", "value": "TS7"},
    {"label": "TS8 (°C)", "value": "TS8"},
    {"label": "TS9 (°C)", "value": "TS9"},
    {"label": "TS10 (°C)", "value": "TS10"},
    {"label": "Tsurf1 (°C)", "value": "Tsurf1"},
    {"label": "Tsurf2 (°C)", "value": "Tsurf2"},
    {"label": "IUVR (W/m^2)", "value": "IUVR"},
    {"label": "ILWR (W/m^2)", "value": "ILWR"},
    {"label": "SHF (W/m^2)", "value": "SHF"},
    {"label": "LHF (W/m^2)", "value": "LHF"},
    {"label": "TA2m (°C)", "value": "TA2m"},
    {"label": "RH2m (%/100)", "value": "RH2m"},
    {"label": "VW10m (m/s)", "value": "VW10m"},
    {"label": "SZA (°)", "value": "SZA"},
    {"label": "SAA (°)", "value": "SAA"},
    {"label": "SH1 (g/kg)", "value": "SH1"},
    {"label": "SH2 (g/kg)", "value": "SH2"},
    {"label": "Alb (-)", "value": "alb"},
]

station_list = [
    dict(name="Swiss Camp 10m", lat=69.555560, lon=-49.374720),  # lon=-49.364720
    dict(name="Swiss Camp", lat=69.555560, lon=-49.364720),
    dict(name="Crawford Point 1", lat=69.874170, lon=-47.024170),
    dict(name="NASA-U", lat=73.840720, lon=-49.526530),
    dict(name="GITS", lat=77.137810, lon=-61.041130),
    dict(name="Humboldt", lat=78.528330, lon=-56.842330),
    dict(name="Summit", lat=72.579720, lon=-38.504540),
    dict(name="Tunu-N", lat=78.018750, lon=-33.966830),
    dict(name="DYE2", lat=66.481970, lon=-46.290780),
    dict(name="JAR1", lat=69.493330, lon=-49.714170),
    dict(name="Saddle", lat=65.999890, lon=-44.502560),
    dict(name="South Dome", lat=63.148890, lon=-44.817500),
    dict(name="NASA-E", lat=75.002280, lon=-29.983750),
    dict(name="CP2", lat=69.913333, lon=-46.854722),
    dict(name="NGRIP", lat=75.099750, lon=-42.332560),
    dict(name="NASA-SE", lat=66.477940, lon=-42.495060),
    dict(name="KAR", lat=69.699420, lon=-33.000580),
    dict(name="JAR2", lat=69.420000, lon=-50.057500),
    dict(name="KULU", lat=65.758450, lon=-39.601770),
    dict(name="JAR3", lat=69.394440, lon=-50.310000),
    dict(name="Aurora", lat=67.135830, lon=-47.292220),
    dict(name="Petermann Glacier", lat=80.683610, lon=-60.293050),
    dict(name="Petermann ELA", lat=80.099250, lon=-58.149690),
    dict(name="NEEM", lat=77.441280, lon=-51.099940),
    dict(name="E-GRIP", lat=75.626780, lon=-35.980060),
    dict(name="LAR1", lat=-68.14111, lon=-63.95194),
    dict(name="LAR2", lat=-67.57638, lon=-63.25750),
    dict(name="LAR3", lat=-67.03166, lon=-62.65027)
]

years = np.arange(1990, 2023)

raster_tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
