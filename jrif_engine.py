# ==============================================================================
# Jyotish Risk Intelligence Framework (JRIF™) - Computational Engine v2.0
# Author: Prasad Vijay Chittal (PRAVICHIT)
# ORCID: 0009-0007-3554-6942
# License: CC BY-NC-SA 4.0
# ==============================================================================

import swisseph as swe
import datetime
import pandas as pd
import numpy as np

# Set Sidereal Zodiac to Lahiri Ayanamsha (Chitrapaksha)
swe.set_sid_mode(swe.SIDM_LAHIRI)

PLANETS = {
    'Sun': swe.SUN,
    'Moon': swe.MOON,
    'Mars': swe.MARS,
    'Jupiter': swe.JUPITER,
    'Saturn': swe.SATURN,
    'Rahu': swe.MEAN_NODE
}

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

VARUNA_MANDALA = ["Ardra", "Ashlesha", "Jyeshtha", "Shatabhisha", "Purva Bhadrapada", "Revati"]
VAYU_MANDALA = ["Swati", "Punarvasu", "Uttara Phalguni", "Hasta"]
WATER_SIGNS = [3, 7, 11] # Cancer, Scorpio, Pisces

KURMA_CHAKRA = {
    "Center (Gangetic Basin / MP)": ["Krittika", "Rohini", "Mrigashira"],
    "East (Bihar, Bengal, Assam Catchment)": ["Ardra", "Punarvasu", "Pushya"],
    "South-East (Odisha, AP Coastal Delta)": ["Ashlesha", "Magha", "Purva Phalguni"],
    "South (Deccan, Tamil Nadu, Sri Lanka)": ["Uttara Phalguni", "Hasta", "Chitra"],
    "South-West (Konkan, Malabar, SW Coast)": ["Swati", "Vishakha", "Anuradha"],
    "West (Gujarat, Saurashtra, Sindh, Thar)": ["Jyeshtha", "Mula", "Purva Ashadha"],
    "North-West (Punjab, Afghan-Pak Border)": ["Uttara Ashadha", "Shravana", "Dhanishta"],
    "North (Kashmir, Himachal, Indus Valley)": ["Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada"],
    "North-East (Nepal, Sikkim, Himalayan Arc)": ["Revati", "Ashwini", "Bharani"]
}

def get_sidereal_data(jd, pid):
    flags = swe.FLG_SWIEPH | swe.FLG_SPEED | swe.FLG_SIDEREAL
    res, _ = swe.calc_ut(jd, pid, flags)
    res_trop, _ = swe.calc_ut(jd, pid, swe.FLG_SWIEPH)
    return res[0], res[3], res_trop[0]

def is_gandanta(lon):
    cusps = [0.0, 120.0, 240.0]
    for c in cusps:
        diff = abs((lon - c + 180) % 360 - 180)
        if diff <= 3.2:
            return True
    return False

def get_active_regions(planet_positions):
    activated = set()
    for p in ['Saturn', 'Mars', 'Rahu']:
        nak_idx = int(planet_positions[p] / (360.0 / 27.0)) % 27
        nak_name = NAKSHATRAS[nak_idx]
        for region, stars in KURMA_CHAKRA.items():
            if nak_name in stars:
                activated.add(region.split(" (")[0])
    return list(activated)

def compute_jri_epoch(date_obj):
    year, month, day = date_obj.year, date_obj.month, date_obj.day
    jd = swe.julday(year, month, day, 12.0)
    
    pos, spd, trop = {}, {}, {}
    for name, pid in PLANETS.items():
        p_lon, p_spd, p_trop = get_sidereal_data(jd, pid)
        pos[name] = p_lon
        spd[name] = p_spd
        trop[name] = p_trop
        
    pos['Ketu'] = (pos['Rahu'] + 180.0) % 360.0
    spd['Ketu'] = spd['Rahu']
    
    score = 1.0
    hazard_weights = {'Hydrological': 0.0, 'Seismic': 0.0, 'Atmospheric': 0.0}
    triggers = []
    
    # 1. Stambhana & Retrogression
    for p in ['Saturn', 'Jupiter', 'Mars']:
        if abs(spd[p]) <= 0.05:
            score += 2.5
            hazard_weights['Seismic'] += 2.0
            triggers.append(f"{p} Station")
        elif spd[p] < 0:
            p_sign = int(pos[p] / 30)
            if p_sign in WATER_SIGNS:
                score += 1.2
                hazard_weights['Hydrological'] += 1.5
                triggers.append(f"{p} Ret. in Water")
                
    # 2. Saturn Debilitation (Aries)
    if int(pos['Saturn'] / 30) == 0:
        score += 1.5
        hazard_weights['Seismic'] += 1.5
        triggers.append("Saturn in Aries (Neecha)")

    # 3. Gandanta Ingress
    if is_gandanta(pos['Moon']):
        score += 1.5
        hazard_weights['Hydrological'] += 1.0
        triggers.append("Moon Gandanta")
    if is_gandanta(pos['Mars']):
        score += 2.0
        hazard_weights['Seismic'] += 2.0
        triggers.append("Mars Gandanta")

    # 4. Mandala Activations
    for p in ['Saturn', 'Rahu', 'Mars']:
        nak_name = NAKSHATRAS[int(pos[p] / (360.0 / 27.0)) % 27]
        if nak_name in VARUNA_MANDALA:
            score += 1.0
            hazard_weights['Hydrological'] += 1.5
            triggers.append(f"{p} in Varuna ({nak_name})")
        if nak_name in VAYU_MANDALA:
            score += 1.0
            hazard_weights['Atmospheric'] += 2.0
            triggers.append(f"{p} in Vayu ({nak_name})")

    # 5. Aspect Squares & Oppositions
    ang_sm = abs((pos['Saturn'] - pos['Mars'] + 180) % 360 - 180)
    if abs(ang_sm - 180) <= 3.5:
        score += 2.5
        hazard_weights['Seismic'] += 2.5
        triggers.append("Saturn-Mars Opposition")
    elif abs(ang_sm - 90) <= 3.5:
        score += 2.0
        hazard_weights['Seismic'] += 2.0
        hazard_weights['Atmospheric'] += 1.5
        triggers.append("Saturn-Mars Square (90°)")

    final_score = min(10.0, round(score, 1))
    primary_hazard = max(hazard_weights, key=hazard_weights.get) if max(hazard_weights.values()) > 0 else "General"
    active_geo = get_active_regions(pos)
    
    tier = "🔴 Critical" if final_score >= 8.0 else ("🟠 Watch" if final_score >= 6.0 else ("🟡 Advisory" if final_score >= 4.0 else "🟢 Normal"))
    
    return {
        'Date': date_obj.strftime('%Y-%m-%d'),
        'JRI Score': final_score,
        'Alert Tier': tier,
        'Hazard Type': primary_hazard,
        'Active Sectors': " | ".join(active_geo),
        'Triggers': ", ".join(triggers) if triggers else "None"
    }

if __name__ == "__main__":
    print("JRIF™ Engine v2.0 initialized. Ready for evaluation.")
  
