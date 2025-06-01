import cv2
import numpy as np
import tensorflow as tf
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os

# Global dictionary to store scores
from utils.session_store import session_data



# Define Blueprint
video_bp = Blueprint("video_analysis", __name__)

# Define emotion labels
emotion_dict = {
    0: "Angry",
    1: "Disgusted",
    2: "Fearful",
    3: "Happy",
    4: "Neutral",
    5: "Sad",
    6: "Surprised",
    7: "joy"
}

# Depression score mapping (for demo)
depression_score_map = {
        "Happy": 2,
        "Neutral": 4,
        "Sad": 7,
        "Angry": 5,
        "Fearful": 8,
        "Disgust": 7,
        "Surprised": 2,
        "Joy":2
}

# Load trained video emotion model
video_model = tf.keras.models.load_model("models/video_emotion_model.keras")

# Load face detector
face_detector = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

def predict_emotion_video(video_path):
    cap = cv2.VideoCapture(video_path)
    emotions = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            face = gray_frame[y:y+h, x:x+w]
            face = cv2.resize(face, (48, 48))
            face = face.astype("float32") / 255
            face = np.expand_dims(face, axis=0)
            face = np.expand_dims(face, axis=-1)

            # Predict emotion
            emotion_prediction = video_model.predict(face)
            max_index = np.argmax(emotion_prediction[0])
            emotion = emotion_dict[max_index]
            emotions.append(emotion)

    cap.release()

    if emotions:
        most_common_emotion = max(set(emotions), key=emotions.count)
        depression_score = depression_score_map.get(most_common_emotion, 4)
    else:
        most_common_emotion = "Unknown"
        depression_score = 4

    # Store the score in session_data
    session_data["video_score"] = depression_score # Change "image_score" to the correct modality

    return most_common_emotion, depression_score

@video_bp.route("/analyze_video", methods=["POST"])
def analyze_video():
    if "video" not in request.files:
        return jsonify({"error": "No video file provided"}), 400

    video_file = request.files["video"]
    filename = secure_filename(video_file.filename)
    filepath = os.path.join("uploads", filename)
    video_file.save(filepath)

    emotion, depression_score = predict_emotion_video(filepath)

    # Clean up
    os.remove(filepath)

    return jsonify({
        "emotion": emotion,
        "depression_score": depression_score
    })
