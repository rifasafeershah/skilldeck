# SkillDeck

SkillDeck converts **completed course certificates** into:
- Skill confidence scores
- Role compatibility percentages

## API Docs
http://localhost:8000/docs

## Demo Flow
1. POST /seed_user
2. POST /add_course
3. GET /skilldeck/{user_id}
4. POST /role_match
