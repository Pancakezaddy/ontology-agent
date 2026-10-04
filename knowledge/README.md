# Knowledge base

This folder is the source of truth for domain meaning. Agents must search here before answering.

## Layout

| Path | Role |
| --- | --- |
| [`md/`](md/INDEX.md) | Canonical markdown ontology (animals + vocab) |
| `catalog.md` | Short index |
| `ontologies/household-pets.ttl` | Same facts as OWL/Turtle |
| `terms.jsonl` | Search index; `file` points at markdown pages |

## Adding or updating terms

1. Edit the matching page under `md/animals/` or `md/vocab/`.
2. Mirror the fact in `ontologies/household-pets.ttl`.
3. Add or refresh the row in `terms.jsonl`.
4. Confirm with `python scripts/search_kb.py "your term"`.

Do not invent classes or properties missing from these files.

## `terms.jsonl` schema

One JSON object per line: `id`, `label`, `type`, `definition`, `broader`, `file`.
