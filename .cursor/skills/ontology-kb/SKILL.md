---
name: ontology-kb
description: Answers questions from this project's ontology knowledge base. Use when the user asks about classes, properties, individuals, IRIs, labels, relations, definitions, or meaning according to the ontology.
---

# Ontology knowledge base

Domain answers come from `knowledge/`, not general training knowledge.

## Workflow

1. Run `python scripts/search_kb.py "QUERY"` with the user's terms, synonyms, and likely local names.
2. Open matching `path` files under `knowledge/md/` (prefer markdown animal/vocab pages over Turtle unless you need OWL syntax).
3. Answer using exact IRIs/labels from the corpus. Cite `file` (path) and term `id`.
4. If search returns nothing relevant, say the term is not in the knowledge base. Do not invent classes, properties, or individuals.
5. If `broader` or `rdfs:subClassOf` / `rdfs:subPropertyOf` is present in the source, treat it as an **asserted** link. Do not claim a full inferred closure unless the source states it.
6. Treat **anti-bids** (`pets:AntiBid`, `knowledge/md/vocab/antibids.md`) as stop/don't-start/protest — never as invitations for more of the same contact.

## Answer shape

- Lead with the term's `id` and `label`.
- Quote or paraphrase the asserted definition.
- List asserted relations (domain, range, subclass) found in the source file.
- End with citations: `` `path` `` + term id.

## Missing terms

Say: not in `knowledge/`. Offer the closest search hits if they are clearly related. Do not add new ontology content unless the user asks to edit the knowledge base.
