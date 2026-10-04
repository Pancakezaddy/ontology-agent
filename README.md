# Ontology Agent

Cursor chat and a Python CLI both answer from `knowledge/`. They search first, cite term ids, and do not invent classes or properties.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export CURSOR_API_KEY="cursor_..."   # Cursor Dashboard → Integrations
```

`search_kb.py` needs only the standard library. The chatbot needs FastAPI (`requirements.txt`). `scripts/ask.py` needs `cursor-sdk` (`pip install -r requirements-cli.txt`) and `CURSOR_API_KEY`.

## Cursor chat

Open this repo in Cursor and ask about terms, types, or relations. The `ontology-kb` skill and `AGENTS.md` tell the agent to run:

```bash
python scripts/search_kb.py "Vader"
```

then read the matching files under `knowledge/`.

## CLI

One-shot (local agent, project settings only):

```bash
python scripts/ask.py "Who is Vader in this ontology?"
```

Follow-ups in one session:

```bash
python scripts/ask.py -i
```

## Knowledge base

| Path | Role |
| --- | --- |
| `knowledge/md/` | Readable ontology (animals, bids, anti-bids) |
| `knowledge/catalog.md` | Namespaces and file index |
| `knowledge/terms.jsonl` | Search index (one term per line) |
| `knowledge/README.md` | How to add terms |

The corpus is markdown under `knowledge/md/` plus Turtle `knowledge/ontologies/household-pets.ttl`.

## Chatbot

Local UI that retrieves from the ontology (anti-bids included). Without `OPENAI_API_KEY` it lists retrieved terms; with the key it composes a grounded answer.

```bash
pip install -r requirements.txt
cd /path/to/repo
uvicorn chatbot.app:app --host 127.0.0.1 --port 8765
```

Open http://127.0.0.1:8765

Optional: `export OPENAI_API_KEY=...` and `OPENAI_MODEL=gpt-4o-mini`.
