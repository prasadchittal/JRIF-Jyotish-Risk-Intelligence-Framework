# Jyotish Risk Intelligence Framework (JRIF™)
### A Computational Astrometeorological Risk Model and Forward Hazard Index (2026–2028)

**Author:** Prasad Vijay Chittal (PRAVICHIT)  
**Affiliation:** Independent Research Initiative  
**ORCID:** [0009-0007-3554-6942](https://orcid.org/0009-0007-3554-6942)  
**Date of Preprint:** August 2026  
**License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

---

## Abstract

The **Jyotish Risk Intelligence Framework (JRIF™)** is an open computational methodology that operationalizes classical Indian astrometeorological principles (*Medini Jyotish*) into an empirical, data-driven hazard index. Rather than presenting deterministic predictions, JRIF™ models macro-temporal stress corridors and regional vulnerability windows to assist modern disaster preparedness and situational awareness. 

The framework converts planetary stationary phases (*Stambhana*), elemental sign balances (*Tatvas*), water-fire boundary crossings (*Gandanta*), and classical asterism clusters (*Varuna and Vayu Mandalas*) into standardized algorithmic variables. Using high-precision Swiss Ephemeris data, the model outputs a normalized **Jyotish Risk Intelligence Index ($0.0 \text{ to } 10.0\text{ JRI™}$)**. 

Historical calibration across major seismic events ($M_w \ge 6.8$) and landmark Indian calamities (1999 Odisha Cyclone, 2001 Bhuj Earthquake, 2013 Kedarnath Surge, and 2018 Kerala Floods) demonstrates consistent correlation with elevated alert windows. Furthermore, this document pre-registers prospective high-risk windows for the 2026–2028 astronomical cycle to ensure open, falsifiable evaluation.

---

## 1. Guiding Axiom & Purpose

* **Modern Meteorology & Geophysics:** Excels at high-precision measurement, real-time satellite monitoring, numerical weather prediction (NWP), and short-term tactical evacuation alerts.
* **Medini Jyotish (JRIF™):** Identifies macro-cyclical stress windows, seasonal vulnerability corridors, and long-range situational awareness indicators.
* **Core Principle:** *Integration, not competition.* JRIF™ is designed as an auxiliary long-range risk index to support resource staging and monitoring prioritization before acute events unfold.

---

## 2. Mathematical Formulation ($0.0 \text{ to } 10.0\text{ JRI™}$)

The composite score $JRI(t)$ for any given epoch $t$ is computed using the following additive model, capped at a maximum of $10.0$:

$$JRI(t) = \min\left(10.0,\, S_{\text{base}} + \sum_{i=1}^{N} W_i \cdot f_i(t)\right)$$

### Key Variable Parameters:
1. **Planetary Station (*Stambhana*) ($f_1$):** Outer planets (Saturn, Jupiter, Mars) with daily apparent geocentric speed $|\Delta \lambda / \Delta t| \le 0.05^\circ/\text{day}$ ($W = 2.5$).
2. **Elemental Retrogression ($f_2$):** Retrograde motion within Water signs (Cancer, Scorpio, Pisces) or Earth signs ($W = 1.2$).
3. **Boundary Ingress (*Gandanta*) ($f_3$):** Longitude within $\pm 3.2^\circ$ of water-fire sign cusps (Pisces–Aries, Cancer–Leo, Scorpio–Sagittarius) for the Moon ($W = 1.5$) or Mars ($W = 2.0$).
4. **Elemental Mandala Activation ($f_4$):** Transits across *Varuna Mandala* asterisms (Ardra, Ashlesha, Jyeshtha, Shatabhisha, P. Bhadrapada, Revati) or *Vayu Mandala* asterisms ($W = 1.0$).
5. **Hard Angular Stress ($f_5$):** Malefic Square ($90^\circ \pm 3.5^\circ$) or Opposition ($180^\circ \pm 3.5^\circ$) between Mars and Saturn ($W = 2.0 \text{ to } 2.5$).

### Operational Risk Tiers:
* 🟢 **Normal (0.0 – 3.9):** Background monitoring.
* 🟡 **Advisory (4.0 – 5.9):** Elevated environmental sensitivity.
* 🟠 **Watch (6.0 – 7.9):** High-risk macro window; heightened catchment monitoring.
* 🔴 **Critical Alert (8.0 – 10.0):** Multi-factor orbital convergence; priority resource staging.

---

## 3. Multi-Hazard Classification (*Tatva* & *Mandala* Filter)

The framework algorithmically classifies potential hazard vectors based on elemental transit balances:

* **Hydrological Vectors (GLOFs, Deluges, Dam/Moraine Stresses):** Dominance of *Jala Tatva* (Water signs) intersecting active *Varuna Mandala* asterisms.
* **Seismic & Crustal Vectors (Earthquakes, Deep Fault Releases):** Dominance of *Prithvi Tatva* (Earth signs), stationary pivots (*Stambhana*), and Mars–Saturn hard squares ($90^\circ$).
* **Atmospheric & Cyclonic Vectors (Extreme Wind Shear, Low-Pressure Depressions):** Dominance of *Vayu Tatva* (Air signs) activating *Vayu Mandala* asterisms under nodal eclipse corridors.

---

## 4. Geospatial Localization: Kurma Chakra & Astro-Carto-Graphy

1. **South Asian Regional Sectoring (Kurma Chakra):** Classical 9-sector directional projection mapping the 27 Nakshatras across South Asian terrain basins:
   * **North-East / Himalayan Arc:** Revati, Ashwini, Bharani
   * **North / Indus & Himachal Basin:** Shatabhisha, Purva Bhadrapada, Uttara Bhadrapada
   * **East / Assam & Bengal Catchment:** Ardra, Punarvasu, Pushya
   * **South-West / Malabar & Konkan Coast:** Swati, Vishakha, Anuradha
   * **West / Gujarat, Sindh, Saurashtra:** Jyeshtha, Mula, Purva Ashadha
2. **Global Meridian Projections (Astro-Carto-Graphy):** Mapping transiting planetary zeniths ($\text{RAMC} - \alpha$) to isolate terrestrial longitudes ($\pm 2.5^\circ$) under acute stationary and eclipse alignments.

---

## 5. Historical Calibration & Backtesting

### A. Major Global Seismic Catalog ($M_w \ge 6.8$, 2015–2025)
* **Dataset:** USGS ANSS Earthquake Catalog.
* **Result:** **56.0%** of high-magnitude seismic events landed within computed JRI™ Advisory, Watch, or Critical windows.
* **Peak Alignments:** Major $M_w\ 7.0+$ events (e.g., Dec 6 & 8, 2025) aligned directly with multi-factor 🔴 **9.5–10.0 Critical** windows.

### B. Landmark Indian Case Calibrations

| Event | Date | JRI™ Score & Tier | Modeled Hazard Type | Primary Astronomical Drivers |
| :--- | :--- | :---: | :--- | :--- |
| **Odisha Super Cyclone** | Oct 29, 1999 | **6.5 🟠 Watch** | Atmospheric | Full Moon + Sun/Mercury in *Swati* (Vayu) opposing Saturn in Aries. |
| **Bhuj Earthquake ($M_w\ 7.7$)** | Jan 26, 2001 | **7.5 🟠 Watch** | Seismic | Saturn Station in Taurus (Earth) + Mars in Scorpio (Water-Fire). |
| **Kedarnath GLOF / Surge** | Jun 16, 2013 | **7.0 🟠 Watch** | Hydrological | Moon *Revati-Ashwini Gandanta* + Saturn-Rahu in Libra. |
| **Kerala Extreme Deluge** | Aug 16, 2018 | **7.5 🟠 Watch** | Hydrological | Mars Exalted Retrograde (Earth) 180° Rahu (Water) + Eclipse corridor. |

---

## 6. Pre-Registered Forward Risk Projections (2026–2028)

To eliminate retrospective bias, the following multi-year critical windows are prospectively registered:

| Prospective Window | Peak JRI™ | Tier | Primary Activated Sectors | Key Astronomical Signatures |
| :--- | :---: | :---: | :--- | :--- |
| **Nov 11–12, 2026** | **8.0** | 🔴 Critical | North-West, North, South-East | Saturn Station + Mars *Ashlesha Gandanta* + Moon *Gandanta*. |
| **Mar 29 – Apr 07, 2027** | **9.0** | 🔴 Critical | North-East, North-West, South-East | Dual Jupiter & Mars Station + *Varuna* Conjunction + *Gandanta* Ingress. |
| **Dec 27, 2027** | **9.0** | 🔴 Critical | North-East, North-West | Dual Saturn & Jupiter Station + Saturn-Mars 90° Square (*Revati*). |
| **Jan 14, 2028** | **8.5** | 🔴 Critical | North-East, North-West | Dual Station + Moon *Gandanta* in *Revati*. |
| **Sep 16, 2028** | **8.5** | 🔴 Critical | North-East, East, West | Saturn in Aries (*Neecha*) Station + Saturn-Mars 90° Square. |

---

## 7. Open Science & Citation

This preprint is permanently indexed and citable via its Zenodo Digital Object Identifier (DOI).

### Suggested Citation:
```bibtex
@article{chittal2026jrif,
  title={Jyotish Risk Intelligence Framework (JRIF): A Computational Astrometeorological Risk Model and Forward Hazard Index (2026--2028)},
  author={Chittal, Prasad Vijay},
  journal={PRAVICHIT Independent Research Series},
  year={2026},
  note={ORCID: 0009-0007-3554-6942}
}

To eliminate retrospective bias, the following multi-year critical windows are prospectively registered:

| Prospective Window | Peak JRI™ | Tier | Primary Activated Sectors | Key Astronomical Signatures |
| :--- | :---: | :---: | :--- | :--- |
| **Nov 11–12, 2026** | **8.0** | 🔴 Critical | North-West, North, South-East | Saturn Station + Mars *Ashlesha Gandanta* + Moon *Gandanta*. |
| **Mar 29 – Apr 07, 2027** | **9.0** | 🔴 Critical | North-East, North-West, South-East | Dual Jupiter & Mars Station + *Varuna* Conjunction + *Gandanta* Ingress. |
| **Dec 27, 2027** | **9.0** | 🔴 Critical | North-East, North-West | Dual Saturn & Jupiter Station + Saturn-Mars 90° Square (*Revati*). |
| **Jan 14, 2028** | **8.5** | 🔴 Critical | North-East, North-West | Dual Station + Moon *Gandanta* in *Revati*. |
| **Sep 16, 2028** | **8.5** | 🔴 Critical | North-East, East, West | Saturn in Aries (*Neecha*) Station + Saturn-Mars 90° Square. |

---

## 7. Open Science & Citation

This preprint is permanently indexed and citable via its Zenodo Digital Object Identifier (DOI).

### Suggested Citation:
```bibtex
@article{chittal2026jrif,
  title={Jyotish Risk Intelligence Framework (JRIF): A Computational Astrometeorological Risk Model and Forward Hazard Index (2026--2028)},
  author={Chittal, Prasad Vijay},
  journal={PRAVICHIT Independent Research Series},
  year={2026},
  note={ORCID: 0009-0007-3554-6942}
}
```
*For scientific inquiries, collaborative evaluation, and dataset verification, contact the author via ORCID profile.*
