Jyotish Risk Intelligence Framework (JRIF)

An Exploratory Computational Framework for Astrometeorological Risk Research (2026–2028)

""DOI" (https://zenodo.org/badge/DOI/10.5281/zenodo.22119016.svg)" (https://doi.org/10.5281/zenodo.22119016)

Author: Prasad Vijay Chittal (PRAVICHIT)
Affiliation: Independent Research Initiative
ORCID: "0009-0007-3554-6942" (https://orcid.org/0009-0007-3554-6942)
Research record: August 2026
License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

---

Abstract

The Jyotish Risk Intelligence Framework (JRIF) is an exploratory computational project investigating whether selected concepts from classical Indian astrometeorology (Medini Jyotish) can be represented as explicit, reproducible computational rules.

The framework translates selected astronomical configurations and traditional interpretive concepts—including planetary stationarity (Stambhana), elemental sign categories (Tatva), boundary transitions (Gandanta), and selected asterism groupings—into a composite Jyotish Risk Intelligence (JRI) score on a nominal 0.0–10.0 scale.

JRIF is a research hypothesis, not a validated earthquake, flood, cyclone, or other natural-hazard forecasting system. Its scoring rules and interpretations require independent verification, and its predictive performance has not been established. It is not a substitute for official meteorological, geological, seismic, hydrological, or emergency-management information.

The project aims to support transparent experimentation through documented rules, reproducible software, explicit limitations, and prospective evaluation.

1. Purpose and Research Position

JRIF investigates a computational representation of selected traditional astrometeorological concepts.

Its guiding principle is integration, not competition. The project does not claim that traditional astrometeorology supersedes modern meteorology, geophysics, seismology, satellite observation, or numerical forecasting.

Any future operational use would require evidence that the framework provides measurable, reliable information beyond appropriate baselines. Until that evidence exists, JRIF should be treated as an exploratory research framework.

Research objectives

- Translate selected traditional concepts into explicit computational rules.
- Document inputs, thresholds, scoring weights, and implementation decisions.
- Test whether independent implementations reproduce the same outputs.
- Evaluate astronomical calculations against suitable reference data.
- Establish a preregistered, forward-only evaluation of any claimed hazard association.
- Publish negative, inconclusive, and positive findings transparently.

2. Computational Framework

JRIF uses a composite index intended to represent the simultaneous activation of selected rule-based indicators.

A general additive representation is:

[
JRI(t)=\min\left(10.0,\ S_{\mathrm{base}}+
\sum_{i=1}^{N}W_i f_i(t)\right)
]

where:

- (t) is the evaluated epoch.
- (S_{\mathrm{base}}) is the baseline score, as defined by the particular engine version.
- (f_i(t)) represents an implemented rule or indicator.
- (W_i) is its configured weight.
- (N) is the number of included indicators.

This equation describes the general scoring structure. The exact implementation, score floors, rounding, rule interactions, and hazard attribution must be taken from the specific versioned source code being evaluated.

Concepts represented in the research

Planetary stationarity (Stambhana)

Apparent planetary motion near a configured speed threshold is represented as a computational indicator. The astronomical definition, time sampling, threshold, and treatment of different planets must be specified for each evaluated engine version.

Elemental sign categories (Tatva)

Traditional sign-element classifications are represented as categorical inputs. Their scientific relationship, if any, to physical natural-hazard processes remains a hypothesis requiring testing.

Boundary transitions (Gandanta)

Configured longitude intervals around selected sign boundaries can be evaluated algorithmically. Their definitions and thresholds must be fixed before an evaluation is conducted.

Asterism groupings and angular configurations

Selected traditional asterism categories and planetary angular relationships can be encoded as explicit rules. The implementation must document which rules are active and how each contributes to the composite score.

These concepts are described as computational inputs, not as established physical causes of earthquakes or extreme weather.

3. Illustrative Risk Tiers

The following four-tier scale has been used in JRIF documentation:

JRI score| Illustrative tier| Interpretation within the framework
0.0–3.9| Normal| Background monitoring category
4.0–5.9| Advisory| Elevated score category
6.0–7.9| Watch| Higher score category
8.0–10.0| Critical Alert| Highest score category

These labels are internal research classifications. They are not calibrated probabilities, official hazard-warning levels, or evidence that an event is likely to occur.

The operational thresholds must be confirmed against the exact engine version before reproducing any historical or prospective result. Different versions or scripts may use different tier definitions.

4. Hazard Categories and Geographic Interpretation

JRIF documentation has explored mapping selected rule combinations to broad categories such as hydrological, seismic, and atmospheric risk.

Such mappings are interpretive hypotheses. A computational label does not establish a causal mechanism, quantify physical hazard, or demonstrate geographic predictive skill.

Earlier documentation also described a South Asian regional sectoring approach based on the traditional Kurma Chakra and proposed broader astronomical geographic projections. These concepts require a separately documented and independently verified implementation before any corresponding geographic output can be considered reproducible.

No geographic location should be treated as being at elevated physical risk solely because JRIF assigns it a score or category.

5. Historical Evaluation Status

5.1 Global seismic backtest

An earlier JRIF publication reported a historical alert-window capture figure of 56.0% (74 of 132 events).

Subsequent technical auditing has not reproduced the 132-event sample, the 74-event match count, or the original event-selection and alert-matching procedure from the available backtest artifacts. The figure is therefore withdrawn as a verified performance claim pending recovery of the underlying evidence and independent reproduction of the calculation.

This correction does not establish how the original figure was produced or attribute its origin to any particular person, software system, or AI assistant.

An audited event-only dataset contains 253 earthquake records. In the audited point-in-time scoring pipeline, 33 of these records met the JRI threshold of 7.0 or greater at earthquake origin time. This is a descriptive result for that dataset and scoring procedure, not a measure of prospective predictive skill.

An event-only dataset cannot, by itself, establish the proportion of time spent in an alert state, false-alarm burden, warning lead time, or improvement over a suitable baseline.

5.2 Historical case studies

Earlier versions of JRIF documentation included numerical scores and astronomical interpretations for selected historical disasters, including the 1999 Odisha cyclone, the 2001 Bhuj earthquake, the 2013 Kedarnath disaster, and the 2018 Kerala floods.

Those numerical scores and interpretations are not presented here as validated results. Independent reproduction would require the relevant event definitions, timestamps, astronomical inputs, exact engine version, scoring outputs, and documented selection methodology.

Current status: JRIF's historical predictive performance remains unvalidated.

6. Prospective Research Programme (2026–2028)

Earlier JRIF documentation recorded the following dates as prospective research windows. They are retained here as historical research hypotheses, not as verified forecasts or warnings.

Previously documented window| Previously recorded peak JRI| Status
11–12 November 2026| 8.0| Unvalidated hypothesis
29 March–7 April 2027| 9.0| Unvalidated hypothesis
27 December 2027| 9.0| Unvalidated hypothesis
14 January 2028| 8.5| Unvalidated hypothesis
16 September 2028| 8.5| Unvalidated hypothesis

The dates and scores above reproduce earlier project documentation; their astronomical calculations and geographic interpretations have not been independently verified by this table.

They must not be interpreted as predictions that earthquakes, floods, cyclones, or other hazardous events will occur on those dates. They should not be used to make emergency decisions, direct evacuations, or advise the public to expect a disaster.

Any prospective evaluation must document the frozen engine version, input data, time zone, event definitions, scoring thresholds, evaluation horizon, baseline, and analysis procedure before examining the outcomes.

The original registration and its timestamp should be preserved. Any later change to a hypothesis or method must be documented rather than silently substituted for the original.

7. Reproducibility and Validation Requirements

JRIF's future evaluation programme should address the following requirements.

Software reproducibility

- Identify the exact source-code version or commit used.
- Record dependencies and ephemeris configuration.
- Test deterministic outputs at fixed timestamps.
- Record runtime errors, fallback modes, and missing-data conditions.
- Ensure that a failed astronomical calculation cannot silently become a valid risk score.

Astronomical verification

- Compare computed positions and relevant angular quantities against a documented reference.
- State the time scale, coordinate conventions, ayanamsha, and ephemeris backend.
- Quantify discrepancies and define acceptance criteria before evaluating performance.

Predictive evaluation

- Use a documented and reproducible event catalog.
- Define event selection and declustering rules before examining results.
- Specify whether alerts must precede events and by how much.
- Evaluate continuous background exposure, false alarms, event capture, lead time, and suitable baselines.
- Account for overlapping evaluation windows and temporal dependence.
- Report uncertainty and negative or inconclusive findings.

Software tests establish software behaviour under specified conditions. Astronomical tests establish agreement with specified astronomical references. Neither alone establishes natural-hazard predictive skill.

8. Safety and Intended Use

JRIF is an experimental research project. It has not been established as a reliable operational natural-hazard prediction or warning system.

Do not use JRIF scores to replace official warnings, emergency instructions, seismic monitoring, weather forecasts, or professional risk assessments. Decisions affecting life, property, infrastructure, and public safety must rely on authoritative information and established procedures.

The project should not imply that a numerical score represents a calibrated probability of a disaster unless a separate, valid calibration study demonstrates that interpretation.

9. Open Research and Citation

JRIF's original research record is archived on Zenodo:

- DOI: "10.5281/zenodo.22119016" (https://doi.org/10.5281/zenodo.22119016)
- Author: Prasad Vijay Chittal (PRAVICHIT)
- ORCID: "0009-0007-3554-6942" (https://orcid.org/0009-0007-3554-6942)

The original deposited record should be consulted for the version and content associated with that DOI. This repository README describes the current research position and does not imply that the original archived document has been retroactively altered.

Suggested citation

@article{chittal2026jrif,
  title = {Jyotish Risk Intelligence Framework (JRIF): A Computational Astrometeorological Risk Model and Forward Hazard Index},
  author = {Chittal, Prasad Vijay},
  year = {2026},
  doi = {10.5281/zenodo.22119016},
  note = {ORCID: 0009-0007-3554-6942}
}

For research inquiries, reproducibility discussions, and technical review, consult the author's ORCID profile.

---

Current Research Status

JRIF remains an exploratory computational framework. Its scoring rules can be tested for implementation consistency, and its astronomical calculations can be compared with reference data. Its ability to provide useful advance information about natural hazards remains an open empirical question.

The project prioritizes reproducibility, explicit uncertainty, transparent correction of unsupported claims, and prospective evaluation over claims of demonstrated predictive success.
