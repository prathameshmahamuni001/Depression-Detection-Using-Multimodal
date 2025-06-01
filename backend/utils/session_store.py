# backend/utils/session_store.py

# Centralized session data store
session_data = {
    "image_score": 0,
    "audio_score": 0,
    "video_score": 0,
    "text_score": 0,
    "mcq_score": 0,
    "openended_score": 0
}

# Optional: reset session between users/runs
def reset_session():
    for key in session_data:
        session_data[key] = 0
