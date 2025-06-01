import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Global dictionary to store scores
from utils.session_store import session_data



# Load the trained image model
image_model = load_model('models/model_filter_collab.keras')

# Emotion to depression score mapping
emotion_to_depression = {
    'Angry': 6,
    'Disgust': 7,
    'Fear': 8,
    'Happy': 1,
    'Sad': 9,
    'Surprise': 3,
    'Neutral': 5,
    'joy' : 2
}

# Emotion dictionary
emotion_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

def predict_depression_from_image(img_path):
    """Predicts depression score from an image."""
    try:
        # Load and preprocess the image
        img = image.load_img(img_path, color_mode='grayscale', target_size=(48, 48))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255  # Normalize pixel values

        # Make prediction
        predictions = image_model.predict(img_array)
        max_index = int(np.argmax(predictions))
        predicted_emotion = emotion_dict[max_index]

        # Convert emotion to depression score
        depression_score = emotion_to_depression[predicted_emotion]

        # Store the score in session_data
        session_data["image_score"] = depression_score
  # Change "image_score" to the correct modality


        return {
            "emotion": predicted_emotion,
            "depression_score": depression_score
        }
    except Exception as e:
        return {"error": str(e)}
