# SkyDemon Checklist Changes — LN-FTD (Cessna 172S)

**Purpose:** This document lists differences between the club's **SkyDemon checklists** (authoritative) and the **original reference** checklist, so reviewers can confirm that every change is intentional and justified.

**Reference:** `reference/checklist_ln-ftd_aug-2020.md` (OCR from Aug 2020 PDF — G1000 aircraft)  
**SkyDemon source:** `Cessna 172S (LN-FTD).aircraft`  
**Instrumentation:** G1000 with **Garmin GI275** standby instruments (upgrade from original G1000-only / conventional standby configuration).

---

## Summary

| Category | Description |
|----------|-------------|
| **Planned improvements** | Consolidation, standardized terminology and capitalization per `AI_INSTRUCTIONS.md` and `CHECKLIST_MIGRATION_GUIDE.md`; typo fixes (Chocks, Equipments). |
| **GI275 instrumentation** | Standby and backup references updated for GI275 (standby display, backup battery, AHRS/ADC, BARO); new GI275-specific failure and miscompare procedures. |

All deviations are either planned improvements or due to GI275 standby instrumentation.

---

## 1. Planned improvements (migration guide & terminology)

### 1.1 Structure and consolidation

- **Start checklist**  
  Reference had *BEFORE STARTING ENGINE*, *STARTING ENGINE*, *TAXI*, *RUN UP*, *BEFORE, AND WHEN LINE UP*. SkyDemon uses one **Start** checklist with sections: *Cockpit Setup* → *Engine Start Setup* → *If Engine Cold* → *Start Engine* → *Before Taxi* → *RUN UP* → *Before Takeoff*. Same flow, fewer checklist switches.

- **Approach / landing**  
  *DESCENT*, *APPROACH*, *PRE LANDING*, *DOWNWIND*, *GO AROUND* merged into **APPROACH TO LANDING** with sections *Descent*, *Approach (before traffic pattern)*, *Downwind*. **GO AROUND** remains a separate checklist.

- **Shutdown**  
  *AFTER LANDING* and *SHUT DOWN* retained as separate checklists; **Securing Airplane (POH)** added to capture POH securing steps (parking brake, throttle, electrical, mixture, magnetos, master, STBY BATT, control lock, fuel selector).

- **Emergencies**  
  POH-style grouping: **Engine Failures (POH)**, **Forced landings (POH)** (including ditching and precautionary landing), **Fires (POH)**, **Electrical System Malfunctions**, **Air Data and AHRS Failures**, **Display Cooling Advisory**, **High Carbon Monoxide**. **Landing (POH)** and **Securing Airplane (POH)** added for normal/short-field/balked landing and securing.

### 1.2 Terminology and typo fixes (AI_INSTRUCTIONS.md)

- **Tow bar / Chokes** → **Tow Bar / Chocks** (correct spelling; reference had "Chokes").
- **Electrical Equipments** → **Electrical Equipment** (singular).
- **Avionic Switch** / **AVIONIC Switches** → **AVIONICS Switch (BUS 1 and BUS 2)** (consistent naming).
- **LAND Light** → **LANDING Light** (standard term).
- **Pilot and Passengers seat backs** → **Pilot and Passenger Seat Backs** (capitalization).
- **Seats and seat belts** → **Seats and Belts** (brevity where used).
- **Fuel Selector** / **Fuel selector** → **FUEL SELECTOR Valve** where appropriate.
- **G1000 ALT SEL** retained; **Standby Altimeter** → **GI275 Altimeter** or **GI275 Standby** where the standby is the GI275 (see §2).

### 1.3 Content alignment with POH

- **Departure briefing** — Reference: "DEPARTURE Briefing" with sub-bullets. SkyDemon: **Engine Failure Briefing — EXPRESS PROCEDURE** and **Outbound Routing Briefing — DEFINE** (same intent, clearer triggers).
- **Downwind** — Added **Landing Briefing — DONE**, **FINAL / RUNWAY — CHECK**; **Autopilot — OFF** in pre-landing flow.
- **After landing** — Reference had "Carburetor heat — Off" in AFTER LANDING; G1000/172S often omits carb heat in this list; SkyDemon keeps **Flaps — UP**, lights, radio, landing time. **CARB HEAT** is in approach/downwind as needed.
- **Fires (POH)** — SkyDemon expands fire procedures to match POH (during start, engine fire in flight, electrical fire in flight, cabin fire, wing fire) with correct sequence and follow-ups (e.g. circuit breakers, restore power if safe).
- **Landing (POH)** — Normal landing, short field, balked landing, after landing; aligns with POH speeds and flap use.
- **Forced landings (POH)** — Emergency landing without engine power, precautionary landing with engine power, ditching; seat backs, belts, doors, mixture/fuel/magnetos/master, touchdown and brakes per POH.

---

## 2. GI275 instrumentation changes

The reference checklist was written for G1000 with conventional standby instruments (and LOW VACUUM annunciator). LN-FTD now uses **Garmin GI275** as standby/backup. The following changes reflect that.

### 2.1 Preflight — 1 CABIN

- **Replaced:** **LOW VACUUM Annunciator — CHECK (verify annunciator is shown)**  
  **With:** **GI275 Standby Display — CHECK (verify ON, no red X, no Service Required)**  
  No vacuum system for standby; GI275 is the standby attitude/altitude/airspeed source.

- **Added:** **GI275 Backup Battery — CHECK (Menu > System > Battery: verify GREEN icon)**  
  Ensures GI275 backup battery is charged (no equivalent in reference).

- **Reference had:** "AVIONICS Switch (BUS 2)" and "Aft Avionic Fan" with "AVIONICS Switch (BUS 2)" — wording aligned; BUS 1/BUS 2 flow unchanged.

### 2.2 Start — Engine Start Setup / Start Engine

- **STBY BATT** — SkyDemon adds optional IFR test (hold 20 s, verify green light). ARM and annunciator check retained.
- **Replaced:** **G1000 PFD alignment / STBY instruments**  
  **With:** **GI275 AHRS — CHECK (AHRS ALIGN cleared, no flags)** after Master ALT on and avionics on.  
  Reflects GI275 as the standby AHRS; alignment must complete before use.

### 2.3 RUN UP

- **Altimeters** — Reference: "PFD (BARO) — SET" and "STBY Instruments — SET". SkyDemon: **Altimeter PFD (BARO) — SET**, **GI275 Altimeter (BARO) — SET** (explicit GI275 BARO set).
- **Replaced:** **VAC Indicator — CHECK**  
  **With:** **GI275 Standby — CHECK (no flags, agrees with PFD)**  
  No vacuum gauge; standby is GI275, cross-checked with PFD.

- **G1000 ALT SEL** — Retained (aircraft still has G1000).

### 2.4 CLIMB

- **Replaced:** **Altimeters — PFD (BARO) / Standby Altimeter — SET**  
  **With:** **PFD BARO — SET**, **GI275 Altimeter — SET**.  
- **Added:** **LANDING Light — OFF** (optional climb cleanup).

### 2.5 APPROACH TO LANDING — Descent / Approach / Downwind

- **Descent:** **PFD BARO** and **GI275 Altimeter** — SET (replaces generic "Standby Altimeter").
- **Approach:** ATIS, heading, landing lights, arrival briefing; altimeter set covered in Descent.
- **Downwind:** Engine instruments, mixture, fuel selector, autopilot off, seats/belts, doors, brake pressure, flaps, landing briefing, final/runway check. Order and content aligned with single-pilot flow; **Autopilot — OFF** explicit.

### 2.6 SHUT DOWN / Securing Airplane

- **Electrical Equipment** (singular); **AVIONICS Switch BUS 1 and 2 — OFF**; **STBY BATT — OFF**; **FUEL SELECTOR Valve — LEFT OR RIGHT** (or LEFT or RIGHT) per POH securing. **Tachometer Time — LOGGED**; **Cleaning — DONE** where used.

### 2.7 Air Data and AHRS Failures (GI275-specific)

Reference had **AIR DATA SYSTEM FAILURE** and **AHRS FAILURE** with "Standby Airspeed", "Standby Altimeter", "Standby Attitude Indicator", "Non-stabilized Magnetic Compass". SkyDemon:

- **RED X — PFD Airspeed / Altitude / Attitude (AHRS) / HSI** — Retained; standby is now **GI275** or **Standby ASI/Altimeter** as applicable.
- **Added: GI275 AHRS Failure (Red X on attitude)** — Use G1000 PFD for attitude; if PFD also failed, use magnetic compass and standby ASI/altimeter.
- **Added: GI275 ADC Failure (Red X on airspeed/altitude)** — Use G1000 PFD for airspeed/altitude; cross-check standby.
- **Added: GI275 ATTITUDE/ALT/IAS Miscompare (Amber)** — Cross-check all sources; seek/maintain VFR; land ASAP if unresolvable.
- **Added: GI275 on Backup Battery** — Check battery status (GREEN 60+ min, YELLOW 15–59 min, RED less than 15 min); note nav/ADS-B load-shed; seek VFR and land ASAP if needed.

These reflect GI275 as a second ADAHRS with its own failure and backup-battery modes.

### 2.8 Engine failure and fire procedures

- **Engine Failure In Flight** — FUEL PUMP, MAGNETOS, MIXTURE, FUEL SHUTOFF, FUEL SELECTOR, RADIO, TRANSPONDER per POH; wording aligned with reference and POH.
- **Engine failure during takeoff roll / immediately after takeoff** — Throttle idle, brakes, flaps; if insufficient runway: mixture IDLE CUTOFF, MAGNETOS OFF, STBY BATT OFF, MASTER OFF; cabin door unlatch. Matches POH and reference intent.
- **Engine failure during flight (restart)** — Fuel shutoff on, fuel selector both, fuel pump on, mixture rich, magnetos both/start, then fuel pump off. **Airspeed** given as 68 KIAS (best glide) in SkyDemon vs 70 in some references; 68 KIAS is consistent with POH best glide for 172S.
- **Fires (POH)** — During start (crank or evacuate), engine fire in flight, electrical fire in flight, cabin fire, wing fire; steps and follow-up (circuit breakers, restore power, land ASAP) aligned with POH and reference.

---

## 3. Quick reference for reviewers

- **Consolidation and section names** → `CHECKLIST_MIGRATION_GUIDE.md`.
- **Terminology / typos** → `AI_INSTRUCTIONS.md` (Chocks, LANDING Light, Equipment, FUEL SELECTOR Valve, Seat Backs, etc.).
- **LOW VACUUM / VAC / Standby** → Replaced or supplemented by **GI275** (standby display, backup battery, BARO, AHRS, ADC).
- **New failure/miscompare/backup-battery items** → All GI275-specific (Air Data and AHRS Failures, GI275 on Backup Battery).
- **POH-only sections** (Landing (POH), Securing Airplane (POH), Forced landings (POH) with ditching/precautionary) → Intentional expansion to match POH; no change to aircraft type.

If you see a change not listed here, it may be wording or structure normalisation. When in doubt, compare the SkyDemon line to the reference and to this document.
