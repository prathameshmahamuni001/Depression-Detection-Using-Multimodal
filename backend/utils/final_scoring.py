# Import session data from all analysis modules
from routes.image_analysis import session_data as image_data
from routes.audio_analysis import session_data as audio_data
from routes.video_analysis import session_data as video_data
from routes.text_analysis import session_data as text_data
from routes.questionnaire import session_data as questionnaire_data
from utils.session_store import session_data

# Function to determine severity level based on final score
def get_severity_and_advice(score):
    if score < 40:
        return "Minimal or No Depression", "You seem to be in a good mental state. Keep maintaining healthy habits!"
    elif 40 <= score < 50:
        return "Mild Depression", "Try engaging in positive activities and talking to close ones. Consider therapy if needed."
    elif 50 <= score < 60:
        return "Moderate Depression", "Consult a mental health professional. Adopt stress management techniques."
    else:
        return "Severe Depression", "Immediate consultation with a doctor is recommended. Professional support is crucial."

# Function to calculate the final depression score
def calculate_final_score():
    # Fetch stored scores from each module, defaulting to 0 if missing
    image_score = session_data.get("image_score", 0)
    audio_score = session_data.get("audio_score", 0)
    video_score = session_data.get("video_score", 0)
    text_score = session_data.get("text_score", 0)
    mcq_score = session_data.get("mcq_score", 0)
    openended_score = session_data.get("openended_score", 0)


    # Define weight distribution (Total = 100%)
    WEIGHTS = {
        "image": 5,
        "audio": 10,
        "video": 15,
        "text": 20,
        "mcq": 30,
        "openended": 10
    }

    # Corrected version (no /4)
    final_score = round((  
        (mcq_score / 40) * WEIGHTS["mcq"] +
        (openended_score / 10) * WEIGHTS["openended"] +
        (image_score / 10) * WEIGHTS["image"] +
        (audio_score / 10) * WEIGHTS["audio"] +
        (video_score / 10) * WEIGHTS["video"] +
        (text_score / 10) * WEIGHTS["text"]
    ), 2)


    # Round final score
    final_score = round(final_score*10, 2)

    # Get severity level & advice
    severity, advice = get_severity_and_advice(final_score)

    return {
        "final_score": final_score,
        "severity": severity,
        "advice": advice
    }
