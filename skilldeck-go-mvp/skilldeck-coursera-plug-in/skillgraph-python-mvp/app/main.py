from __future__ import annotations

import json
from pathlib import Path
from typing import List, Literal
from urllib.parse import urlparse
import sqlite3
from fastapi import HTTPException
from pydantic import Field

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.scoring import build_skill_scores, calculate_role_fit

BASE_DIR = Path(__file__).resolve().parent.parent
ROLES_PATH = BASE_DIR / "data" / "roles.json"
STATIC_DIR = BASE_DIR / "static"
DB_PATH = BASE_DIR / "data" / "certificates.sqlite3"

app = FastAPI(title="SkillGraph MVP", version="1.0.0")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


with db_connection() as db:
    db.execute("""CREATE TABLE IF NOT EXISTS certificates (
        id INTEGER PRIMARY KEY, url TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL, completed_at TEXT,
        skills_json TEXT NOT NULL, verification TEXT NOT NULL
    )""")


COURSE_SKILLS = {
    "foundations of cybersecurity": ["security", "risk management"],
    "google data analytics": ["analytics", "sql", "data visualization"],
    "introduction to statistics": ["statistics"],
    "agile meets design thinking": ["agile", "user research", "product strategy"],
    "product strategy": ["product strategy", "roadmapping"],
    "introduction to sql": ["sql"],
}


class CourseraCertificate(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    url: str = Field(min_length=10, max_length=1000)
    completed_at: str | None = None
    skills: List[str] = Field(default_factory=list)


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
    for cert in collection_rows():
        items.append({"title": cert["title"], "source": "certification",
                      "description": " ".join(cert["skills"]),
                      "explicit_skills": cert["skills"]})
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


@app.post("/api/coursera/import")
def import_coursera_certificate(payload: CourseraCertificate):
    parsed = urlparse(payload.url)
    if (parsed.scheme != "https" or
        (parsed.hostname or "").lower() not in {"coursera.org", "www.coursera.org"} or
        not (parsed.path.startswith("/account/accomplishments/") or parsed.path.startswith("/accomplishments/"))):
        raise HTTPException(400, "Provide a Coursera accomplishments HTTPS link")

    mapped = []
    for course_title, skills in COURSE_SKILLS.items():
        if course_title in payload.title.casefold():
            mapped.extend(skills)
    # Preserve every learner-entered skill, not just predefined keywords.
    # Also support comma-separated strings sent directly to the API.
    raw_skills = [*mapped]
    for entry in payload.skills:
        raw_skills.extend(entry.split(","))
    skills = sorted({skill.strip() for skill in raw_skills if skill.strip()}, key=str.casefold)
    with db_connection() as db:
        db.execute("""INSERT INTO certificates
            (url, title, completed_at, skills_json, verification)
            VALUES (?, ?, ?, ?, 'self_reported')
            ON CONFLICT(url) DO UPDATE SET
            title=excluded.title, completed_at=excluded.completed_at,
            skills_json=excluded.skills_json""",
            (payload.url, payload.title, payload.completed_at, json.dumps(skills)))
    return {"status": "imported", "verification": "self_reported", "skills": skills}


@app.get("/api/coursera/certificates")
def list_coursera_certificates():
    with db_connection() as db:
        rows = db.execute("SELECT * FROM certificates ORDER BY id DESC").fetchall()
    return [{**dict(row), "skills": json.loads(row["skills_json"])} for row in rows]


class KaggleCertificate(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    url: str = Field(min_length=10, max_length=1000)
    completed_at: str | None = None
    skills: List[str] = Field(default_factory=list)


with db_connection() as db:
    db.execute("""CREATE TABLE IF NOT EXISTS kaggle_certificates (
        id INTEGER PRIMARY KEY, url TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL, completed_at TEXT,
        skills_json TEXT NOT NULL, verification TEXT NOT NULL
    )""")


def collection_rows():
    with db_connection() as db:
        coursera = db.execute("SELECT * FROM certificates ORDER BY id DESC").fetchall()
        kaggle = db.execute("SELECT * FROM kaggle_certificates ORDER BY id DESC").fetchall()
    results = []
    for provider, rows in (("coursera", coursera), ("kaggle", kaggle)):
        for row in rows:
            results.append({"id": f"{provider}-{row['id']}", "provider": provider,
                "title": row["title"], "url": row["url"],
                "completed_at": row["completed_at"],
                "skills": json.loads(row["skills_json"]),
                "verification": row["verification"]})
    return results


@app.get("/api/collection")
def get_collection():
    items = collection_rows()
    unique_skills = sorted({skill for item in items for skill in item["skills"]}, key=str.casefold)
    xp = sum(100 + 15 * len(item["skills"]) for item in items)
    return {"certificates": items, "total": len(items), "skills": unique_skills,
            "xp": xp, "level": 1 + xp // 500,
            "providers": {p: sum(item["provider"] == p for item in items)
                          for p in ("coursera", "kaggle")}}


@app.post("/api/kaggle/import")
def import_kaggle_certificate(payload: KaggleCertificate):
    parsed = urlparse(payload.url)
    hostname = (parsed.hostname or "").lower()
    if parsed.scheme != "https" or hostname not in {"kaggle.com", "www.kaggle.com"}:
        raise HTTPException(400, "Provide a Kaggle HTTPS certificate or course URL")
    raw = [s.strip() for entry in payload.skills for s in entry.split(",")]
    skills = sorted({s for s in raw if s}, key=str.casefold)
    with db_connection() as db:
        db.execute("""INSERT INTO kaggle_certificates
            (url, title, completed_at, skills_json, verification)
            VALUES (?, ?, ?, ?, 'self_reported')
            ON CONFLICT(url) DO UPDATE SET title=excluded.title,
            completed_at=excluded.completed_at, skills_json=excluded.skills_json""",
            (payload.url, payload.title, payload.completed_at, json.dumps(skills)))
    return {"status": "imported", "verification": "self_reported", "skills": skills}
