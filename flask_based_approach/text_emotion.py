import pickle
import re
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Load the tokenizer and label encoder
with open('tokenizers/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

with open('tokenizers/label_encoder.pickle', 'rb') as handle:
    label_encoder = pickle.load(handle)

# Load the trained text emotion model
text_model = load_model('models/Emotion_Recognition_Model.keras')

# Clean text
def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

# Predict emotion from text
def predict_emotion_text(text):
    text = clean_text(text)
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=50, truncating='pre')
    prediction = text_model.predict(padded_sequence)
    emotion_index = np.argmax(prediction, axis=1)[0]
    emotion = label_encoder.classes_[emotion_index]
    return emotion
