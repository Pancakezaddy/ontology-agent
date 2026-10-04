"""Grounded answers from the household ontology markdown."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from search_kb import repo_root, search  # noqa: E402

SYSTEM = """You answer only from the ontology CONTEXT below.
Distinguish affection bids from anti-bids (do not start, stop, or protest).
Cite term IRIs (https://example.org/ontology/pets#...) and markdown paths.
If the corpus does not contain the fact, say so. Do not invent animals, bids, or anti-bids.
"""


def _read_hit_files(hits: list[dict], max_chars: int = 14000) -> str:
    root = repo_root()
    chunks: list[str] = []
    seen: set[str] = set()
    total = 0
    for hit in hits:
        rel = hit.get("path") or ""
        if not rel or rel in seen:
            continue
        seen.add(rel)
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        piece = f"### {rel}\n{text}\n"
        if total + len(piece) > max_chars:
            piece = piece[: max(0, max_chars - total)]
        chunks.append(piece)
        total += len(piece)
        if total >= max_chars:
            break
    return "\n".join(chunks)


def retrieve(question: str, limit: int = 10) -> tuple[list[dict], str]:
    hits = search(question, limit=limit)
    extra: list[dict] = []
    q = question.lower()
    if any(w in q for w in ("stop", "don't", "dont", "anti", "consent", "shy", "crowd", "uninvited")):
        extra = search("anti-bid", limit=4)
    seen = {h.get("id") for h in hits}
    merged = hits + [h for h in extra if h.get("id") not in seen]
    context = _read_hit_files(merged)
    return merged, context


def _openai_chat(question: str, context: str) -> str | None:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        return None
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    body = {
        "model": model,
        "temperature": 0,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": f"CONTEXT:\n{context or '(no files retrieved)'}\n\nQUESTION: {question}",
            },
        ],
    }
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        return payload["choices"][0]["message"]["content"]
    except (urllib.error.URLError, KeyError, IndexError, json.JSONDecodeError):
        return None


def extractive_answer(hits: list[dict]) -> str:
    if not hits:
        return (
            "Not in the knowledge base. I can only answer from the household ontology "
            "(named pets, bids, and anti-bids)."
        )
    lines = ["From the ontology (no LLM key set — showing retrieved terms):", ""]
    for hit in hits:
        label = hit.get("label") or ""
        ident = hit.get("id") or ""
        snippet = hit.get("snippet") or ""
        path = hit.get("path") or ""
        lines.append(f"- **{label}** `{ident}`")
        if snippet:
            lines.append(f"  {snippet}")
        if path:
            lines.append(f"  _{path}_")
        lines.append("")
    lines.append("Set OPENAI_API_KEY for a composed answer grounded in these files.")
    return "\n".join(lines).strip()


def answer_question(question: str) -> dict:
    hits, context = retrieve(question)
    generated = _openai_chat(question, context) if context or hits else None
    text = generated or extractive_answer(hits)
    return {
        "answer": text,
        "hits": [
            {
                "id": h.get("id"),
                "label": h.get("label"),
                "path": h.get("path"),
                "snippet": h.get("snippet"),
            }
            for h in hits
        ],
        "grounded": bool(generated),
    }
