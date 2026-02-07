def compute_scores(skills):
    scores = {}
    for skill in skills:
        scores[skill] = scores.get(skill, 0) + 25

    for skill in scores:
        scores[skill] = min(scores[skill], 100)

    return scores
