# video_emotion.py

import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, Response  # Add this line

# Initialize Flask app
app = Flask(__name__)

# Define emotion labels
emotion_dict = {
    0: "Angry",
    1: "Disgusted",
    2: "Fearful",
    3: "Happy",
    4: "Neutral",
    5: "Sad",
    6: "Surprised"
}

# Load the trained video emotion model
video_model = tf.keras.models.load_model('models/video_emotion_model.keras')

# Load face detector
face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

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
            face = face.astype('float32') / 255
            face = np.expand_dims(face, axis=0)
            face = np.expand_dims(face, axis=-1)

            # Predict emotion
            emotion_prediction = video_model.predict(face)
            max_index = np.argmax(emotion_prediction[0])
            emotion = emotion_dict[max_index]
            emotions.append(emotion)

    cap.release()
    return max(set(emotions), key=emotions.count)  # Return the most frequent emotion

@app.route('/video_feed/<path:video_path>')
def video_feed(video_path):
    return Response(generate_frames(video_path),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
