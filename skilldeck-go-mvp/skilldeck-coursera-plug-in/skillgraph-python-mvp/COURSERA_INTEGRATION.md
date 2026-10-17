# Coursera integration (MVP)

This branch supports manual imports of Coursera accomplishment URLs. It does **not** call a private Coursera API, verify completion, or access a learner account. Imported records are marked `self_reported`.

## Start

```bash
cd skillgraph-python-mvp
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 and use the Coursera import form.

## API

- `POST /api/coursera/import`: `{ "title": "Foundations of Cybersecurity", "url": "https://www.coursera.org/account/accomplishments/verify/EXAMPLE", "skills": ["security"] }`
- `GET /api/coursera/certificates`: list imported records.
- `POST /api/analyze`: includes imported certificate skills in existing skill and role-fit scores.

## Important limitations

- All imported records are stored in one local SQLite database. Do not deploy publicly without authentication and user isolation.
- The course-title mapping is a small curated demonstration, not live Coursera metadata. Unknown courses require manual skills.
- Existing role-fit scoring is heuristic and not a measure of job readiness.
- An automatic completion sync requires a separately approved Coursera organization integration.
