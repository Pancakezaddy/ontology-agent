#!/usr/bin/env python3
"""Ask a local Cursor agent that is scoped to this ontology repo."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from cursor_sdk import Agent, AgentOptions, CursorAgentError, LocalAgentOptions

INSTRUCTION = (
    "Follow AGENTS.md and the ontology-kb skill. "
    "Search with `python scripts/search_kb.py QUERY` before answering. "
    "Cite term ids and file paths. Do not invent ontology terms.\n\n"
)


def repo_root() -> Path:
    here = Path(__file__).resolve().parent
    for candidate in (here.parent, *here.parent.parents):
        if (candidate / "knowledge").is_dir() and (candidate / "AGENTS.md").is_file():
            return candidate
    return here.parent


def agent_options(root: Path) -> AgentOptions:
    api_key = os.environ.get("CURSOR_API_KEY", "").strip()
    if not api_key:
        print(
            "Set CURSOR_API_KEY (Cursor Dashboard → Integrations).",
            file=sys.stderr,
        )
        sys.exit(1)
    return AgentOptions(
        api_key=api_key,
        model="composer-2.5",
        local=LocalAgentOptions(
            cwd=str(root),
            setting_sources=["project"],
        ),
    )


def exit_for_result(result) -> None:
    if result.status == "error":
        print(f"run failed: {getattr(result, 'id', '')}", file=sys.stderr)
        sys.exit(2)
    if result.status == "cancelled":
        sys.exit(130)
    text = result.result or ""
    if text:
        print(text)


def stream_run(run) -> None:
    run_id = getattr(run, "id", None) or getattr(run, "run_id", None)
    if run_id:
        print(f"run_id={run_id}", file=sys.stderr)
    for message in run.messages():
        if message.type == "assistant":
            content = getattr(message, "message", None)
            blocks = getattr(content, "content", None) if content is not None else None
            if not blocks:
                continue
            for block in blocks:
                if getattr(block, "type", None) == "text":
                    print(block.text, end="", flush=True)
    print()
    result = run.wait()
    exit_for_result(result)


def one_shot(question: str, options: AgentOptions) -> None:
    try:
        result = Agent.prompt(INSTRUCTION + question, options)
    except CursorAgentError as err:
        print(
            f"startup failed: {err.message}, retryable={err.is_retryable}",
            file=sys.stderr,
        )
        sys.exit(1)
    exit_for_result(result)


def interactive(options: AgentOptions) -> None:
    try:
        with Agent.create(
            model=options.model,
            api_key=options.api_key,
            local=options.local,
        ) as agent:
            print(f"agent_id={agent.agent_id}", file=sys.stderr)
            first = True
            while True:
                try:
                    line = input("ask> ").strip()
                except EOFError:
                    print()
                    return
                if not line or line in {":q", "quit", "exit"}:
                    return
                prompt = INSTRUCTION + line if first else line
                first = False
                try:
                    run = agent.send(prompt)
                    stream_run(run)
                except CursorAgentError as err:
                    print(
                        f"startup failed: {err.message}, retryable={err.is_retryable}",
                        file=sys.stderr,
                    )
                    sys.exit(1)
    except CursorAgentError as err:
        print(
            f"startup failed: {err.message}, retryable={err.is_retryable}",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Query the ontology knowledge base via a local Cursor agent.",
    )
    parser.add_argument("question", nargs="*", help="One-shot question")
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Multi-turn session (shared conversation state)",
    )
    args = parser.parse_args()
    options = agent_options(repo_root())
    if args.interactive:
        interactive(options)
        return
    if not args.question:
        parser.error("pass a question, or use -i for interactive mode")
    one_shot(" ".join(args.question), options)


if __name__ == "__main__":
    main()
