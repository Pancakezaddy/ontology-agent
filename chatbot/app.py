#!/usr/bin/env python3
"""Household ontology chatbot (FastAPI)."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .grounding import answer_question

STATIC = Path(__file__).resolve().parent / "static"

app = FastAPI(title="Household ontology chat")
app.mount("/static", StaticFiles(directory=STATIC), name="static")


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC / "index.html")


@app.post("/api/chat")
def chat(body: ChatRequest) -> dict:
    return answer_question(body.message.strip())
