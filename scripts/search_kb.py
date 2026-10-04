#!/usr/bin/env python3
"""Search the ontology knowledge base and print ranked JSON matches."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SKIP_NAMES = {"README.md", "catalog.md"}
TEXT_SUFFIXES = {".ttl", ".owl", ".rdf", ".jsonld", ".json", ".md", ".txt", ".jsonl"}


def repo_root() -> Path:
    here = Path(__file__).resolve().parent
    for candidate in (here.parent, *here.parent.parents):
        if (candidate / "knowledge").is_dir():
            return candidate
    return here.parent


def tokenize(query: str) -> list[str]:
    parts = [part for part in query.lower().replace("#", " ").replace(":", " ").split() if part]
    long_parts = [part for part in parts if len(part) >= 3]
    return long_parts or parts


def score_text(query: str, *fields: str) -> int:
    q = query.strip().lower()
    if not q:
        return 0
    blob = " ".join(f or "" for f in fields).lower()
    score = 0
    if q in blob:
        score += 50
    for token in tokenize(query):
        if token in blob:
            score += 10
    for field in fields:
        value = (field or "").lower()
        if value == q:
            score += 40
        elif value.endswith("#" + q) or value.endswith(":" + q):
            score += 30
    return score


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                item = json.loads(text)
            except json.JSONDecodeError as exc:
                print(f"skip {path}:{line_no}: {exc}", file=sys.stderr)
                continue
            if isinstance(item, dict):
                rows.append(item)
    return rows


def snippet_from_row(row: dict) -> str:
    definition = (row.get("definition") or "").strip()
    if definition:
        return definition
    return (row.get("label") or row.get("id") or "").strip()


def search_jsonl(path: Path, query: str) -> list[dict]:
    hits: list[dict] = []
    for row in load_jsonl(path):
        ident = str(row.get("id") or "")
        label = str(row.get("label") or "")
        definition = str(row.get("definition") or "")
        term_type = str(row.get("type") or "")
        file_path = str(row.get("file") or str(path.as_posix()))
        score = score_text(query, ident, label, definition, term_type)
        if score <= 0:
            continue
        hits.append(
            {
                "id": ident or None,
                "label": label or None,
                "type": term_type or None,
                "broader": row.get("broader"),
                "snippet": snippet_from_row(row),
                "path": file_path,
                "score": score,
            }
        )
    return hits


def search_files(knowledge: Path, query: str) -> list[dict]:
    hits: list[dict] = []
    for path in knowledge.rglob("*"):
        if not path.is_file() or path.name in SKIP_NAMES:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if path.name == "terms.jsonl":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        rel = path.as_posix()
        try:
            rel = str(path.relative_to(knowledge.parent).as_posix())
        except ValueError:
            pass
        score = 0
        snippet = ""
        q = query.strip().lower()
        for line in text.splitlines():
            line_score = score_text(query, line)
            if line_score > score:
                score = line_score
                snippet = line.strip()
        if q and q in text.lower() and score == 0:
            score = 5
            snippet = next(
                (line.strip() for line in text.splitlines() if q in line.lower()),
                path.name,
            )
        if score <= 0:
            continue
        hits.append(
            {
                "id": None,
                "label": path.stem,
                "type": None,
                "broader": None,
                "snippet": snippet,
                "path": rel,
                "score": score,
            }
        )
    return hits


def merge_hits(hits: list[dict], limit: int) -> list[dict]:
    ranked = sorted(hits, key=lambda item: (-item["score"], item.get("path") or "", item.get("id") or ""))
    return ranked[:limit]


def search(query: str, limit: int = 8) -> list[dict]:
    """Return ranked KB hits for query (empty list if none)."""
    query = (query or "").strip()
    if not query:
        return []
    root = repo_root()
    knowledge = root / "knowledge"
    jsonl = knowledge / "terms.jsonl"
    if jsonl.is_file():
        hits = search_jsonl(jsonl, query)
    else:
        hits = search_files(knowledge, query)
    return merge_hits(hits, limit)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the ontology knowledge base.")
    parser.add_argument("query", help="Label, IRI fragment, or phrase to find")
    parser.add_argument("--limit", type=int, default=8, help="Maximum matches to print")
    args = parser.parse_args()
    query = args.query.strip()
    if not query:
        print("[]")
        return 0

    root = repo_root()
    knowledge = root / "knowledge"
    if not knowledge.is_dir():
        print(f"knowledge directory not found at {knowledge}", file=sys.stderr)
        return 1

    hits = search(args.query, args.limit)
    print(json.dumps(hits, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
