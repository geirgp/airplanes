# SkyDemon Checklist Changes — LN-MTX (Cessna 172P)

**Purpose:** This document lists differences between the club's **SkyDemon checklists** (authoritative) and the **original reference** checklist, so reviewers can confirm that every change is intentional and justified.

**Reference:** `reference/checklist_ln-mtx_202x.md` (OCR from undated revision PDF)  
**SkyDemon source:** `Cessna 172P (LN-MTX).aircraft`  
**Instrumentation:** Steam gauges (no G5/GI275). No instrumentation upgrade for this aircraft.  
**Related:** Wording harmonized with LN-DAG where club checklists share the same lineage; see `SkyDemon_changes_LN-DAG.md`.

---

## Summary

| Category | Description |
|----------|-------------|
| **Planned improvements** | Consolidation into sectioned checklists, standardized terminology and capitalization per `AI_INSTRUCTIONS.md` and `CHECKLIST_MIGRATION_GUIDE.md`. |
| **Instrumentation** | None. LN-MTX retains vacuum system and traditional gyros; RUN UP still includes Suction and Gyros. |

All deviations are planned improvements; there are no changes due to upgraded instrumentation.

---

## 1. Planned improvements (migration guide & terminology)

### 1.1 Structure and consolidation

- **Single "Start" checklist**  
  The reference had separate blocks: *GROUND — START*, *GROUND — TAXI / RUN UP*, and *GROUND — TAKE-OFF*. These are merged into one SkyDemon checklist **Start** with sections: *Before Start* → *Start Engine* → *Before Taxi* → *RUN UP* → *Before Takeoff*. Same procedural sequence, fewer checklist switches. *(CHECKLIST_MIGRATION_GUIDE.)*

- **Preflight**  
  Exterior list grouped into sections: *Cabin*, *Empennage*, *Right Wing*, *Nose*, *Left Wing*, *Final*. Item order preserved within each section.

- **Approach / landing**  
  *AIRBORNE — APPROACH*, *PRE-LANDING*, and *DOWNWIND* merged into **APPROACH TO LANDING** with sections: *Approach (before traffic pattern)*, *Pre-Landing*, *Downwind*.

- **Emergencies**  
  Grouped into: **Engine Failure In Flight**, **Engine Failures** (runway, after takeoff, in flight prop rotating/not rotating, emergency landing), **Fires**, **Other Emergencies**. No G5/GI275, so no avionics-failure checklist.

### 1.2 Terminology and capitalization (AI_INSTRUCTIONS.md)

- **Gust lock** → **Gust Lock** (preflight and shutdown; matches reference PDF and LN-DAG).
- **Trim** → **Elevator Trim Control**.
- **Fuel selector** → **FUEL SELECTOR Valve**.
- **Avionics** → **AVIONICS Switch**; **Beacon** → **BEACON Light Switch**; **Magnetos** → **MAGNETOS Switch**.
- **Carburetor heat** → **CARB HEAT**.
- **Master switch** → **Master Switch** (with **BATT only**, **Master Switch ALT**, **BOTH** as appropriate).
- **Navigation lights** → **NAV Light Switch** / **NAV and STROBE Lights**.
- **Landing lights** → **LANDING Light** where referring to the switch/light.
- **Radios** → **Radios (ATIS-GND-TWR)**.
- **Gyros (comp. Set to RWY HDG)** → **Gyros (compass set to RWY HDG) — SET** (retained; aircraft has steam gyros).
- **Departure briefing** with sub-bullets → **Departure Briefing — REVIEWED**.
- **Documents — Filled** → **Documents — FILLED**.
- **Flaps — Carefully up** → **Flaps — RETRACT CAREFULLY**.
- **Primer** → **Primer (hot - cold)** with response **2-6, LOCKED**.
- **Area** (RUN UP) → **Area Free**.
- **Brakes** (engine failure on runway) → **APPLY TO STOP**.
- **Mixture** (SHUT DOWN) → **FULL LEAN** (restores reference PDF wording; IDLE CUTOFF retained in emergency checklists only).

### 1.3 RUN UP and Before Takeoff (unchanged intent)

- **Suction (4.6–5.4 green)** — **Retained.** Aircraft has vacuum system; item worded as **Suction — CHECK (4.6-5.4 green)**.
- **Gyros** — **Retained** in Before Takeoff as **Gyros (compass set to RWY HDG) — SET**.
- **AVIONICS Switch** — Single **AVIONICS Switch — ON** after start (no BUS 1/2 split; aircraft has conventional avionics).

### 1.4 Emergency memory items

- **Engine failure in flight:** **SELECT FIELD** response standardised to **CHECK SURFACE WIND**.

---

## 2. Alignment with LN-DAG

LN-MTX checklists were harmonized with LN-DAG (Cessna 172M) where the aircraft share the same club checklist lineage, with these intentional differences:

| Kept on MTX only | Omitted from MTX (DAG has G5) |
|------------------|-------------------------------|
| **Suction** in RUN UP | GMU 11 Magnetometer (preflight) |
| **Gyros** in Start Engine and Before Takeoff | G5 Displays, Battery, AHRS, HSI checks |
| **AVIONICS Switch — ON** after start (conventional avionics bus) | **G5 Failures** emergency checklist |

Wording aligned to match DAG: Gust Lock, Primer (hot - cold), Master Switch (BATT only) / Master Switch ALT, Area Free, Departure Briefing, FULL LEAN shutdown, Brakes APPLY TO STOP.

---

## 3. What did not change (no instrumentation upgrade)

- No G5 or GI275; no PFD/HSI/BARO or standby display items.
- No magnetometer (GMU 11) check.
- No "G5 Failures" or "AHRS/ADC failure" checklist.
- Suction and gyro checks remain in RUN UP and Before Takeoff.
- Ammeter and magnetos check limits unchanged (e.g. max 125 drop +/- 50).

---

## 4. Quick reference for reviewers

- **Consolidation** → Matches `CHECKLIST_MIGRATION_GUIDE.md`.
- **Terminology** → Matches `AI_INSTRUCTIONS.md`.
- **Suction and Gyros** → Kept; aircraft still has vacuum and steam gyros.
- **Alignment with LN-DAG** → Same club checklist structure and wording except vacuum/gyro items and no G5 content. Changelog entries for shared terminology match `SkyDemon_changes_LN-DAG.md`.

Any change not listed here should be a wording or formatting normalisation that does not alter procedural intent.
