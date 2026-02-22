def findPerfectMatch(candidates, user_skills, user_needs):
    scores = []
    for candidate in candidates:
        score = 0

        # Score based on skill match
        skill_match = len(set(user_skills) & set(candidate['skills']))
        score += skill_match * 10  # Weighted score for each matching skill

        # Reverse need bonus
        reverse_need_bonus = len(set(user_needs) & set(candidate['needs']))
        score += reverse_need_bonus * 5  # Weighted score for each reversed need match

        # Online status bonus
        if candidate['online']:
            score += 20  # Bonus for being online

        # Rating score
        score += candidate['rating'] * 2  # Rating contributes to the score

        scores.append((candidate, score))

    # Sort candidates by score in descending order
    scores.sort(key=lambda x: x[1], reverse=True)
    
    return [candidate for candidate, score in scores]  # Return sorted candidates based on score