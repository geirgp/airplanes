# SkyDemon Checklist Changes — LN-DAG (Cessna 172M)

**Purpose:** This document lists differences between the club's **SkyDemon checklists** (authoritative) and the **original reference** checklist, so reviewers can confirm that every change is intentional and justified.

**Reference:** `reference/checklist_ln-dag_april-2020.md` (OCR from April 2020 PDF)  
**SkyDemon source:** `Cessna 172M (LN-DAG).aircraft`  
**Instrumentation:** Garmin G5 (PFD/HSI) — aircraft has been upgraded from steam gauges.

---

## Summary

| Category | Description |
|----------|-------------|
| **Planned improvements** | Consolidation into sectioned checklists, standardized terminology and capitalization per `AI_INSTRUCTIONS.md` and `CHECKLIST_MIGRATION_GUIDE.md`. |
| **G5 instrumentation** | Items added, removed, or reworded to match G5 (no vacuum system, electronic attitude/heading, magnetometer). |

All deviations below fall into one of these two categories.

---

## 1. Planned improvements (migration guide & terminology)

### 1.1 Structure and consolidation

- **Single "Start" checklist**  
  The reference had separate blocks: *GROUND — START*, *GROUND — TAXI / RUN UP*, and *GROUND — TAKE-OFF*. These are merged into one SkyDemon checklist **Start** with sections in order: *Before Start* → *Start Engine* → *Before Taxi* → *RUN UP* → *Before Takeoff*. Same procedural sequence, fewer checklist switches. *(CHECKLIST_MIGRATION_GUIDE: fewer broader checklists with sections.)*

- **Preflight**  
  The long exterior list is grouped into sections: *Cabin*, *Empennage*, *Right Wing*, *Nose*, *Left Wing*, *Final*. Order of items preserved within each section.

- **Approach / landing**  
  *AIRBORNE — APPROACH*, *PRE-LANDING*, and *DOWNWIND* are merged into one checklist **APPROACH TO LANDING** with sections: *Approach (before traffic pattern)*, *Pre-Landing*, *Downwind*.

- **Emergencies**  
  Reference had several emergency blocks. SkyDemon groups them into: **Engine Failure In Flight**, **Engine Failures** (runway, after takeoff, in flight prop rotating/not rotating, emergency landing), **Fires**, **Other Emergencies**, **G5 Failures**.

### 1.2 Terminology and capitalization (AI_INSTRUCTIONS.md)

- **Gust lock** → **Control Lock** (preflight and shutdown).
- **Trim** → **Elevator Trim Control** (Before Start, RUN UP context).
- **Fuel selector** → **FUEL SELECTOR Valve** (all phases).
- **Avionics** → **AVIONICS Switch**; **Beacon** → **BEACON Light Switch**; **Magnetos** → **MAGNETOS Switch**.
- **Carburetor heat** → **CARB HEAT** (brevity and consistency).
- **Master switch** → **Master Switch** with qualifiers as needed (e.g. *BAT only*, *ALT*, *BOTH*).
- **Navigation lights** → **NAV Light Switch** / **NAV and STROBE Lights** where appropriate.
- **Landing lights** → **LANDING Light** (singular where it refers to the switch/light).
- **Radios** → **Radios (ATIS-GND-TWR)** where the intent is to set those frequencies.
- **Departure briefing** with sub-bullets → single item **Departure Briefing — REVIEWED**.
- **Documents — Filled** → **Documents — FILLED** (consistent verb form).
- **All Switches** → **All Switches OFF** (explicit response).
- **Flaps — Carefully up** → **Flaps — RETRACT CAREFULLY** (action-oriented).

### 1.3 Emergency memory items

- **Engine failure in flight**  
  **SELECT FIELD** response standardised to **CHECK SURFACE WIND** so the memory item explicitly includes wind check.

---

## 2. G5 instrumentation changes

### 2.1 Preflight — Nose section

- **Added:** **GMU 11 Magnetometer — CHECK (security of attachment)**  
  G5 uses an external magnetometer (GMU 11); security of attachment is a necessary preflight check.

### 2.2 Start Engine section

- **Added:** **G5 Displays (PFD and HSI) — CHECK (verify powered on, ALIGNING displayed)**  
  Confirms G5 is powered and in alignment mode before start.

- **Added:** **G5 Battery Status — CHECK (verify GREEN indicator)**  
  Ensures G5 internal backup battery is healthy.

- **Added:** **G5 AHRS Alignment — CHECK (ALIGNING cleared, no red X flags)**  
  Done after engine start/ALT on; confirms AHRS is aligned and usable.

- **Removed:** **Gyros — Set**  
  Replaced by G5 heading and attitude; no manual gyro setting.

### 2.3 RUN UP

- **Removed:** **Suction (4.6–5.4 green) — Checked**  
  No vacuum system with G5; suction gauge not applicable.

- **Retained:** Oil pressure/temperature, ammeter, magnetos, carb heat, throttle idle/1000 RPM. Wording normalized (e.g. **Oil Pressure / Temperature**, **Ammeter**, **MAGNETOS Switch**, **CARB HEAT**).

### 2.4 Before Takeoff

- **Replaced:** **Gyros (comp. Set to RWY HDG) — Set**  
  **With:** **G5 HSI Heading — VERIFY (agrees with runway HDG and compass)**  
  Reflects electronic HSI; pilot verifies heading against runway and compass.

### 2.5 New checklist: G5 Failures

- **G5 PFD Failure** — Use G5 HSI (reverts to attitude); use magnetic compass for heading.
- **ALIGNING KEEP WINGS LEVEL** — G5 attitude invalid until aligned; keep wings level; use standby/magnetic compass as needed.
- **NO BATT displayed on G5** — Do not conduct IMC; note G5 internal battery duration (e.g. up to 4 hours if aircraft power lost).

These sections are specific to G5 and have no direct equivalent in the steam-gauge reference.

---

## 3. Quick reference for reviewers

- **Consolidation and section names** → Align with `CHECKLIST_MIGRATION_GUIDE.md` (fewer checklists, clear sections, same procedural order).
- **Terminology/capitalization** → Align with `AI_INSTRUCTIONS.md` (e.g. FUEL SELECTOR Valve, AVIONICS Switch, Control Lock, CARB HEAT).
- **Removed suction / gyros** → Due to G5 (no vacuum; no traditional gyros).
- **New or reworded items** mentioning G5, G5 HSI, G5 AHRS, GMU 11, or G5 battery → All due to G5 instrumentation.
- **New "G5 Failures" checklist** → G5-specific emergency procedures.

If you see a change not listed here, it may be a normalisation (spelling, punctuation, or wording) that does not alter intent. When in doubt, compare the SkyDemon checklist line to the reference and to this document.
