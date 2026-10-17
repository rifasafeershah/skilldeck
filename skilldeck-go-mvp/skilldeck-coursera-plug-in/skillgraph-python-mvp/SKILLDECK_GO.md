# SkillDeck GO

Pokémon GO-inspired collectible credential dashboard for Coursera and Kaggle, built on the existing FastAPI MVP.

## Run on Windows PowerShell

```powershell
cd path\to\skilldeck-coursera-plug-in\skillgraph-python-mvp
py -m pip install -r requirements.txt
py -m uvicorn app.main:app --reload
```

Visit http://127.0.0.1:8000

## Features

- Collect Coursera and Kaggle credentials using manually entered course name, link, date, and comma-separated skills.
- Display collectible credential cards, provider filters, XP, levels, skill inventory, and career quests.
- Use imported skills from both providers in the existing role-fit engine.
- Existing Coursera data remains in its original SQLite table; Kaggle imports are stored in a separate table.
- Both providers use self-reported completion, **not** verified credentials. Kaggle and Coursera account history are **not** automatically fetched.
- XP: 100 per certificate plus 15 per listed skill. Level: 1 + floor(XP / 500). This is a game mechanic, not a proficiency measure.

## API

- `GET /api/collection`
- `POST /api/coursera/import`
- `POST /api/kaggle/import`
- `POST /api/analyze`

## Notes

This is a local, single-user prototype. Add authentication and user-level data isolation before deploying publicly. The original demo learning items are no longer preloaded into the interface; additional learning items are temporary in-browser session entries. Do not treat an entered credential link as verified completion.
