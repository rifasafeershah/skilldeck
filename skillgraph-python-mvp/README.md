# SkillGraph Python MVP

A small FastAPI MVP that converts courses/certifications into Skill Scores, Role Fit Scores, gap analysis, and recommendations.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000

## MVP features
- Add completed courses/certifications
- Auto-detect skills from course titles/descriptions
- Generate Skill Scores
- Calculate Role Fit Score by target role
- Show missing skills and recommended next actions

## GitHub upload
```bash
git init
git add .
git commit -m "Initial SkillGraph Python MVP"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/skillgraph-python-mvp.git
git push -u origin main
```
