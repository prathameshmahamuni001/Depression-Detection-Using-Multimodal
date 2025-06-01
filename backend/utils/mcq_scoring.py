def calculate_mcq_score(mcq_responses):
    """
    Calculates MCQ-based depression score.
    - Each answer ('A', 'B', 'C', 'D') is mapped to a score (0-3).
    - The total score is scaled to fit a 50-point range.
    """
    scoring = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    
    # Convert MCQ responses into a total raw score
    total_score = sum(scoring.get(answer, 0) for answer in mcq_responses)

    # Normalize score to fit in the 50-point range
    max_possible_score = len(mcq_responses) * 3  # Max score if all answers were 'D'
    normalized_score = (total_score / max_possible_score) * 50

    return round(normalized_score, 2)  # Ensure consistent decimal formatting
