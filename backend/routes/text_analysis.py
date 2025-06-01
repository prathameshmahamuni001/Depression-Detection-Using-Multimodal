import pickle
import re
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Global dictionary to store scores
from utils.session_store import session_data



# Load the tokenizer and label encoder
with open('models/tokenizers/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

with open('models/tokenizers/label_encoder.pickle', 'rb') as handle:
    label_encoder = pickle.load(handle)

# Load the trained text emotion model
text_model = load_model('models/Emotion_Recognition_Model.keras')

# Define depression scores for emotions (adjust weights if needed)
depression_scores = {
        "happy": 2,
        "neutral": 4,
        "sadness": 7,
        "anger": 5,
        "fearful": 8,
        "disgust": 7,
        "surprised": 2,
        "joy": 2
}

# Clean text
def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

# Predict emotion and return depression score
def predict_emotion_text(text):
    try:
        print("\n🔹 Raw Input Text:", text)  # Debugging

        text = clean_text(text)
        print("✅ Cleaned Text:", text)  # Debugging

        sequence = tokenizer.texts_to_sequences([text])
        print("📏 Tokenized Sequence:", sequence)  # Debugging

        padded_sequence = pad_sequences(sequence, maxlen=50, truncating='pre')
        print("📏 Padded Sequence:", padded_sequence)  # Debugging

        prediction = text_model.predict(padded_sequence)
        print("📊 Model Prediction:", prediction)  # Debugging

        emotion_index = np.argmax(prediction, axis=1)[0]
        print("🔢 Predicted Emotion Index:", emotion_index)  # Debugging

        emotion = label_encoder.classes_[emotion_index]
        print("😊 Final Predicted Emotion:", emotion)  # Debugging

        # Get depression score based on emotion
        depression_score = depression_scores.get(emotion, 50)
        print("📉 Calculated Depression Score:", depression_score)

        # Store the score in session_data
        session_data["text_score"] = depression_score  # Change "image_score" to the correct modality

        return {"emotion": emotion, "depression_score": depression_score}

    except Exception as e:
        print("❌ Error in predict_emotion_text:", str(e))  # Debugging
        return {"error": "Error processing text"}

