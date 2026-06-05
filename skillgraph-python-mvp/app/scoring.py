from __future__ import annotations

from typing import Dict, List

SKILL_KEYWORDS: Dict[str, List[str]] = {
    "python": ["python", "pandas", "fastapi", "machine learning", "ml"],
    "sql": ["sql", "database", "query", "snowflake"],
    "data visualization": ["visualization", "tableau", "power bi", "charts", "dashboard"],
    "statistics": ["statistics", "regression", "probability", "experiment"],
    "analytics": ["analytics", "kpi", "metrics", "analysis", "data"],
    "product strategy": ["product strategy", "product", "market", "vision"],
    "roadmapping": ["roadmap", "prioritization", "planning", "backlog"],
    "user research": ["user research", "customer discovery", "interview", "persona"],
    "agile": ["agile", "scrum", "sprint", "jira"],
    "security": ["security", "cybersecurity", "infosec", "threat", "vulnerability"],
    "risk management": ["risk", "third-party", "vendor", "assessment"],
    "iam": ["iam", "identity", "access", "sailpoint", "rbac"],
    "compliance": ["compliance", "hipaa", "nist", "soc 2", "policy"],
    "incident response": ["incident", "response", "triage", "investigation"]
}


def detect_skills(text: str) -> List[str]:
    text = text.lower()
    matches = []
    for skill, keywords in SKILL_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            matches.append(skill)
    return matches


def build_skill_scores(items: List[dict]) -> Dict[str, int]:
    scores: Dict[str, int] = {}

    for item in items:
        title = item.get("title", "")
        description = item.get("description", "")
        source = item.get("source", "course")
        text = f"{title} {description} {source}"
        detected = detect_skills(text)

        for skill in detected:
            base_points = 25
            if source.lower() in ["certification", "certificate"]:
                base_points += 10
            scores[skill] = min(100, scores.get(skill, 0) + base_points)

    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))


def calculate_role_fit(skill_scores: Dict[str, int], role_requirements: Dict[str, int]) -> dict:
    total_weight = sum(role_requirements.values())
    earned = 0
    gaps = []

    for skill, weight in role_requirements.items():
        user_score = skill_scores.get(skill, 0)
        earned += min(user_score, 100) / 100 * weight
        if user_score < 60:
            gaps.append({
                "skill": skill,
                "current_score": user_score,
                "recommended_action": f"Complete a project or course focused on {skill}."
            })

    fit_score = round((earned / total_weight) * 100) if total_weight else 0
    return {"fit_score": fit_score, "gaps": gaps}
