# AGENTS.md

## Repository purpose

- This is an OpenCode kit for thesis guidance, not an application codebase: there are no package manifests, build scripts, test suites, or CI workflows in the repo.
- `opencode.json` sets `asesor-tesis-ds` as the default agent; run `opencode` from the repository root to load repo-local agents.

## High-value sources

- `.opencode/agent/asesor-tesis-ds.md` is the source of truth for constructing a Maestría en Ingeniería de Software thesis under Design Science.
- `.opencode/agent/traductor-alsie.md` is used only after the Design Science work is complete; it translates `tesis_ds/` into the ALSIE IFI structure.
- `referencias/ds_ch00_prefacio.md` through `referencias/ds_ch15_referencias.md` are the local Design Science book chapters the asesor must consult by stage.
- `instituciones/alsie/guia_ifi_contenido.md` and `instituciones/alsie/indicadores_revision_ifi.md` are the normative ALSIE sources for the translator.
- `plantillas/` contains optional Markdown skeletons for generated thesis work; do not treat them as completed thesis content.

## Workflow constraints to preserve

- All deliverables produced by the agents must be Markdown (`.md`); do not generate `.docx`, `.pdf`, `.tex`, or `.odt` as final outputs.
- Thesis work goes in `tesis_ds/`; ALSIE translation output goes in `entrega_alsie/`. In an individual thesis fork, these outputs may be versioned for tutor review.
- Do not run `traductor-alsie` before `tesis_ds/00_estado.md` shows E0–E10 closed; translating earlier creates provisional or empty ALSIE sections.
- The asesor must maintain `tesis_ds/matriz_coherencia.md` as the chain: problem → object → field → objective → question → artifact → evaluation → criteria → evidence → contribution.
- References and citations in thesis artifacts must follow APA 7; unverifiable sources must be marked `[por verificar]`, not invented.

## Editing this repo

- Keep agent instructions in Spanish académico de Bolivia with formal `usted`, matching the existing `.opencode/agent/*.md` files.
- Preserve the separation of concerns: `asesor-tesis-ds` builds the Design Science investigation; `traductor-alsie` maps a completed investigation to ALSIE.
- If adding a new institution, add `instituciones/<institucion>/`, add `.opencode/agent/traductor-<institucion>.md`, and update `README.md`.
- ALSIE Markdown can be regenerated from original Word files with the `pandoc` commands documented in `instituciones/alsie/README.md`; the original `.docx` files are not versioned.

## Verification

- There is no automated validation pipeline. For changes here, verify by reading the affected Markdown/config files and checking that `README.md`, `opencode.json`, and `.opencode/agent/*.md` remain consistent.
