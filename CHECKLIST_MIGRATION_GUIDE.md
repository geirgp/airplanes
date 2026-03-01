# Checklist Consolidation Migration Guide

Use this process when converting many small legacy checklists into fewer sectioned checklists.

## Migration Checklist (Step-by-Step)

1. Define target consolidated checklist names by operational objective (e.g., `Start`, `Taxi`, `Landing`).
2. Map each legacy checklist to a destination checklist and section name.
3. Order sections in strict procedural sequence (first action to last action).
4. Move items without changing procedural intent; keep original action order inside each section.
5. Create dedicated conditional sections only where needed (e.g., `If Engine Cold`).
6. Remove accidental duplicates created during merge; keep intentional re-checks only.
7. Normalize terminology, spelling, and capitalization using `AI_INSTRUCTIONS.md` standards.
8. Check readability on one-screen digital flow: section names should be quickly scannable.
9. Validate that each consolidated checklist can be executed without jumping between checklists.
10. Run `validate.py` and resolve all schema/structure issues before finalizing.

## Notes

- This guide supports the checklist structure principles defined in `AI_INSTRUCTIONS.md`.
- Prefer consolidation first, then split only where scanability or workflow clearly suffers.
