# AI Instructions for Aircraft Checklist Maintenance

## Overview
This document defines standards and best practices for maintaining aircraft checklist files (`.aircraft` XML files). These standards ensure consistency, clarity, and proper aviation terminology throughout all checklists.

## Core Principles

### 1. Brevity First
- **Prefer concise wording** over verbose descriptions
- Example: Use "Seats and Belts" instead of "Seats and Seat Belts"
- Keep checklist items brief and actionable

### 2. Consistency is Critical
- **Standardized terminology** must be used throughout all checklists
- **Capitalization** must be consistent for the same items
- **Spelling** must be correct (aviation terminology is precise)

### 3. Understandable Wording
- Use clear, unambiguous language
- Avoid jargon unless it's standard aviation terminology
- Write as if for a GA pilot who needs to act quickly and accurately

## Terminology Standards

### General Principles
- **Switch names** should be consistently capitalized (typically uppercase for critical systems)
- **Valve names** should include "Valve" when referring to fuel or other critical valves
- **Equipment** (singular, not "Equipments")
- Use **standard aviation terminology** appropriate to the aircraft type

### Fuel System
- **FUEL SELECTOR Valve** (always uppercase, always includes "Valve")
- **FUEL SHUTOFF Valve** (always uppercase, always includes "Valve")
- **FUEL PUMP** or **FUEL PUMP Switch** (context-dependent, but consistent within checklist)
- Note: Terminology may vary by aircraft type (e.g., "FUEL SELECTOR" vs "FUEL SELECTOR Valve")

### Electrical Systems
- **AVIONICS Switch** (singular "Switch", uppercase "AVIONICS")
- **Electrical Equipment** (singular, not "Equipments")
- **Master Switch** (consistent capitalization; may include additional descriptors like "ALT and BATT" if applicable)
- Note: Specific configurations (e.g., "BUS 1 and 2") should match the aircraft's actual system

### Ignition Systems
- **MAGNETOS Switch** (always uppercase "MAGNETOS" for piston aircraft)
- Note: Electronic ignition systems may use different terminology

### Flight Controls
- **Flaps** (standard term)
- **Flight Controls** (standard capitalization)

### Safety Equipment
- **Seat Belts** (when referring to the belts themselves)
- **Seats and Belts** (when checking both together - brevity preferred)
- **Seat Backs** (capitalized, not "seat backs")

### Lights
- **STROBE Light** (not "STROBE light")
- **LANDING Light** (not "LAND Light")
- **BEACON Light Switch**
- **NAV Light Switch**

### Instruments & Systems
- **Annunciators** (correct spelling - not "Announciators")
- **Standby Altimeter** (not "Standby" alone)
- **Altimeter Setting** or **BARO** (use appropriate term for the aircraft's instrumentation)
- **Flight Instruments** (standard capitalization)
- Note: Glass cockpit terminology (e.g., "PFD BARO") should only be used if the aircraft has such systems

### Ground Equipment
- **Chocks** (correct spelling - not "Chokes")
- **Tow Bar** (standard capitalization)

## Capitalization Rules

### Always Uppercase
- Critical switch names: **MAGNETOS Switch**, **AVIONICS Switch**, **FUEL SELECTOR Valve**
- Critical systems: **FUEL SHUTOFF Valve**, **FUEL PUMP**
- Abbreviations: **STBY BATT**, **PFD**, **BARO**, **XPDR**, **ELT**
- Note: Not all aircraft will have all these systems; use appropriate terminology for the aircraft type

### Title Case (Standard Capitalization)
- Control names: **Throttle Control**, **Mixture Control**, **Propeller Control**
- System names: **Flight Controls**, **Flight Instruments**, **Flaps**
- Equipment: **Parking Brake**, **Seat Belts**, **Cabin Doors**

### Context-Dependent
- **Light** vs **Lights** - match the actual item (single light vs multiple)
- Switch vs Switches - use singular unless referring to multiple distinct switches

## Common Errors to Avoid

### Spelling
- ❌ "Announciators" → ✅ "Annunciators"
- ❌ "Chokes" → ✅ "Chocks"
- ❌ "Equipments" → ✅ "Equipment"

### Capitalization
- ❌ "Magnetos Switch" → ✅ "MAGNETOS Switch" (for piston aircraft)
- ❌ "Avionics Switch" → ✅ "AVIONICS Switch"
- ❌ "Fuel Selector" → ✅ "FUEL SELECTOR Valve" (when valve is part of the name)
- ❌ "STROBE light" → ✅ "STROBE Light"
- ❌ "LAND Light" → ✅ "LANDING Light"

### Terminology
- ❌ "FUEL SELECTOR" (without Valve) → ✅ "FUEL SELECTOR Valve" (when valve is part of the name)
- ❌ "Seats and Seat Belts" → ✅ "Seats and Belts" (brevity)
- ❌ "AVIONICS Switches" → ✅ "AVIONICS Switch" (singular, unless multiple distinct switches)
- ❌ "Equipments" → ✅ "Equipment" (always singular)

## Section Naming

### Clear, Concise Section Names
- ✅ "Before Start"
- ✅ "Before Takeoff"
- ✅ "Before TAXI"
- ✅ "RUN UP" or "Run Up" (be consistent within checklist)
- ✅ "If Engine Cold" or conditional sections as needed
- Use clear, action-oriented names that pilots can quickly identify

## Checklist Structure and Flow

### Digital Display Context
- All items within a single checklist are displayed on the same digital screen
- Sections are used to organize items into logical groups
- Sections represent sequential stages in a procedural flow

### Section Organization
- **Sections group related items** that belong to the same phase of a procedure
- Each section represents the **next stage in the operational flow**
- Sections should follow a logical sequence from initial checks through completion
- Example: In a "Start" checklist, sections might flow from "Cockpit Setup" → "Engine Start Setup" → "Start Engine" → "Before Taxi" → "RUN UP" → "Before Takeoff"

### Flow Principles
- Sections should reflect the **natural progression** of the procedure
- Group items that are performed together or in close sequence
- Use sections to break complex procedures into manageable phases
- Maintain **chronological order** within the checklist flow
- Conditional sections (e.g., "If Engine Cold") should be placed at the appropriate point in the sequence

### Aviation Terminology
- Use standard aviation terms when describing sections: **flow**, **procedure**, **sequence**, **phase**
- Section names should reflect the operational phase (e.g., "Cockpit Setup", "Engine Start", "Before Takeoff")
- Align section organization with standard aircraft operating procedures

## Checklist Review Checklist

When reviewing or editing checklists, verify:

1. **Spelling**: All aviation terms spelled correctly
2. **Capitalization**: Consistent throughout (especially switches and valves)
3. **Terminology**: Standard terms used consistently
4. **Brevity**: No unnecessary words
5. **Clarity**: Each item is unambiguous
6. **Consistency**: Same items named the same way across all checklists

## Examples of Good Checklist Items

```
<CheckItem Challenge="FUEL SELECTOR Valve" Response="BOTH" />
<CheckItem Challenge="AVIONICS Switch" Response="OFF" />
<CheckItem Challenge="MAGNETOS Switch" Response="START" />
<CheckItem Challenge="Seats and Belts" Response="CHECK SECURE" />
<CheckItem Challenge="Flaps" Response="UP" />
<CheckItem Challenge="STROBE Light" Response="ON" />
<CheckItem Challenge="Annunciators" Response="CHECK (no annunciators shown)" />
<CheckItem Challenge="Flight Controls" Response="FREE and CORRECT" />
```

Note: Specific system configurations (e.g., "BUS 1 and 2") should only be included if they match the aircraft's actual systems.

## Examples of Items to Fix

```
❌ <CheckItem Challenge="FUEL Selector" Response="BOTH" />
✅ <CheckItem Challenge="FUEL SELECTOR Valve" Response="BOTH" />

❌ <CheckItem Challenge="Magnetos Switch" Response="OFF" />
✅ <CheckItem Challenge="MAGNETOS Switch" Response="OFF" />

❌ <CheckItem Challenge="Announciators" Response="CHECK" />
✅ <CheckItem Challenge="Annunciators" Response="CHECK" />

❌ <CheckItem Challenge="FLAPS" Response="SET 0-10°" />
✅ <CheckItem Challenge="Flaps" Response="SET 0-10°" />

❌ <CheckItem Challenge="Equipments" Response="OFF" />
✅ <CheckItem Challenge="Electrical Equipment" Response="OFF" />
```

## Notes for AI Assistants

- When editing checklists, **always check for consistency** across the entire file
- Use `grep` to find all instances of a term before changing it
- When in doubt, **prefer brevity** while maintaining clarity
- **Aviation terminology is precise** - verify spelling and capitalization
- Consider the **pilot's perspective** - items should be quick to read and unambiguous
- **Standardize first, then optimize** - consistency is more important than perfection
- **Aircraft-specific systems**: Use terminology that matches the actual aircraft type
  - Piston aircraft may have "MAGNETOS Switch"
  - Turbine aircraft may have different ignition terminology
  - Glass cockpit aircraft may use "PFD" terminology
  - Steam gauge aircraft may use different instrument terminology
- **When in doubt**: Match the terminology used in the aircraft's official documentation (POH/AFM)
- **Always execute the validation script** (`validate.py`) after modifying any `.aircraft` XML files to ensure they conform to the schema

