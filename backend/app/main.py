from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import Base, engine, get_db
from .models import User, Course, SkillScore
from .extract import extract_skills
from .scoring import compute_scores

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SkillDeck API")

@app.post("/seed_user")
def seed_user(db: Session = Depends(get_db)):
    user = User(name="Rifa")
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"user_id": user.id}

@app.post("/add_course")
def add_course(user_id: int, title: str, db: Session = Depends(get_db)):
    course = Course(user_id=user_id, title=title)
    db.add(course)
    db.commit()

    skills = extract_skills(title)
    scores = compute_scores(skills)

    for skill, score in scores.items():
        db.add(SkillScore(user_id=user_id, skill=skill, score=score))

    db.commit()
    return {"skills_added": skills}

@app.get("/skilldeck/{user_id}")
def get_skilldeck(user_id: int, db: Session = Depends(get_db)):
    rows = db.query(SkillScore).filter(SkillScore.user_id == user_id).all()
    return [{"skill": r.skill, "score": r.score} for r in rows]

@app.post("/role_match")
def role_match(user_id: int, role: str, db: Session = Depends(get_db)):
    role_skills = {
        "Product Manager": ["Product Management", "Agile", "AI Ethics"],
        "Data Analyst": ["SQL", "Data Visualization", "Machine Learning"]
    }

    user_skills = db.query(SkillScore).filter(SkillScore.user_id == user_id).all()
    user_map = {s.skill: s.score for s in user_skills}

    total = 0
    for s in role_skills.get(role, []):
        total += user_map.get(s, 0)

    confidence = round((total / (len(role_skills[role]) * 100)) * 100, 2)
    return {"role": role, "confidence_percent": confidence}
