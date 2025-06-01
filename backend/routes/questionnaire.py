from flask import Blueprint, request, jsonify
from utils.mcq_scoring import calculate_mcq_score
from services.openended_analysis import analyze_open_ended_responses
# Global dictionary to store scores
from utils.session_store import session_data


questionnaire_bp = Blueprint("questionnaire", __name__)

@questionnaire_bp.route("/submit_questionnaire", methods=["POST"])
def submit_questionnaire():
    data = request.json
    mcq_answers = data.get("mcq_answers", [])
    open_ended_responses = data.get("open_ended_responses", [])

    # MCQ Score Calculation (assuming it's out of 100)
    mcq_score = calculate_mcq_score(mcq_answers)

    # Open-Ended Score Calculation
    open_ended_score = sum(analyze_open_ended_responses(resp) for resp in open_ended_responses) / len(open_ended_responses)

    # Final Combined Score (Weightage Example: 70% MCQ, 30% Open-ended)
    final_score = (0.7 * mcq_score) + ( 0.3  * open_ended_score)


    # Store the score in session_data
    session_data["mcq_score"] = mcq_score  # Change "image_score" to the correct modality
    session_data["open_ended_score"] = open_ended_score  # Change "image_score" to the correct modality

    return jsonify({
        "mcq_score": mcq_score,
        "open_ended_score": open_ended_score,
        "final_questionnaire_score": round(final_score, 2)
    })
