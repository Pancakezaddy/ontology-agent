# Ontology Agent

Answers about domain meaning (classes, properties, individuals, relations) come from `knowledge/`, not general training knowledge.

Before answering those questions:

1. Follow the `ontology-kb` skill.
2. Run `python scripts/search_kb.py "QUERY"`.
3. Read the matching markdown under `knowledge/md/` (then Turtle only if needed).
4. Cite term `id` and file path.
5. If the corpus has no match, say so. Do not invent terms.
6. Anti-bids mean do not start, stop, or protest — not a bid for more pets.
