import numpy as np
import librosa
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from flask import jsonify

# Global dictionary to store scores
from utils.session_store import session_data


# Load the trained audio model
audio_model = load_model("models/audio_emotion_lstm_model.h5")

# Emotion labels
emotion_labels = ["angry", "disgust", "fear", "happy", "neutral", "ps", "sad"]
label_encoder = LabelEncoder()
label_encoder.fit(emotion_labels)

# Map emotions to depression scores (custom mapping)
emotion_to_score = {
    "angry": 6,
    "disgust": 7,
    "fear": 8,
    "happy": 2,
    "neutral": 4,
    "ps": 5,  # Placeholder emotion
    "sad": 9,
}

# Extract MFCC features
def extract_mfcc(filename, duration=3, offset=0.5):
    try:
        y, sr = librosa.load(filename, duration=duration, offset=offset)
        mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
        return mfcc
    except Exception as e:
        print(f"Error extracting MFCC: {str(e)}")
        return None

# ✅ Updated: Accept `audio_file` as an argument
def analyze_audio(audio_file):
    mfcc_features = extract_mfcc(audio_file)
    
    if mfcc_features is None:
        return jsonify({"error": "Error extracting features"}), 400

    mfcc_features = np.expand_dims(mfcc_features, axis=0)
    mfcc_features = np.expand_dims(mfcc_features, axis=2)

    predictions = audio_model.predict(mfcc_features)
    predicted_index = np.argmax(predictions, axis=1)
    predicted_emotion = label_encoder.inverse_transform(predicted_index)[0]

    depression_score = emotion_to_score.get(predicted_emotion, 4)  # Default score if unknown emotion

    # ✅ Store the depression score in `session_data`
    session_data["audio_score"] = depression_score

    return jsonify({
        "emotion": predicted_emotion,
        "depression_score": depression_score
    })
