from __future__ import annotations

import json
from pathlib import Path
from typing import List

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.scoring import build_skill_scores, calculate_role_fit

BASE_DIR = Path(__file__).resolve().parent.parent
ROLES_PATH = BASE_DIR / "data" / "roles.json"
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="SkillGraph MVP", version="1.0.0")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class LearningItem(BaseModel):
    title: str
    source: str = "course"
    description: str = ""


class SkillGraphRequest(BaseModel):
    target_role: str
    learning_items: List[LearningItem]


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/roles")
def get_roles():
    with open(ROLES_PATH, "r", encoding="utf-8") as f:
        roles = json.load(f)
    return {"roles": list(roles.keys()), "role_requirements": roles}


@app.post("/api/analyze")
def analyze_profile(payload: SkillGraphRequest):
    with open(ROLES_PATH, "r", encoding="utf-8") as f:
        roles = json.load(f)

    items = [item.model_dump() for item in payload.learning_items]
    skill_scores = build_skill_scores(items)

    target_role = payload.target_role
    role_requirements = roles.get(target_role)
    if not role_requirements:
        return {"error": f"Unknown role: {target_role}"}

    role_result = calculate_role_fit(skill_scores, role_requirements)

    all_role_matches = []
    for role, requirements in roles.items():
        result = calculate_role_fit(skill_scores, requirements)
        all_role_matches.append({"role": role, "fit_score": result["fit_score"]})

    all_role_matches.sort(key=lambda x: x["fit_score"], reverse=True)

    return {
        "skill_scores": skill_scores,
        "target_role": target_role,
        "role_fit_score": role_result["fit_score"],
        "skill_gaps": role_result["gaps"],
        "role_matches": all_role_matches
    }
