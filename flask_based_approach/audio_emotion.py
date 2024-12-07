import numpy as np
import librosa
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# Load the trained audio model
audio_model = load_model('models/AudioModelLSTM.h5')

# Emotion labels
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'ps', 'sad']
label_encoder = LabelEncoder()
label_encoder.fit(emotion_labels)

# Extract MFCC from audio
def extract_mfcc(filename, duration=3, offset=0.5):
    y, sr = librosa.load(filename, duration=duration, offset=offset)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    return mfcc

# Predict emotion from audio
def predict_emotion_audio(audio_file):
    mfcc_features = extract_mfcc(audio_file)
    if mfcc_features is not None:
        mfcc_features = np.expand_dims(mfcc_features, axis=0)
        mfcc_features = np.expand_dims(mfcc_features, axis=2)
        predictions = audio_model.predict(mfcc_features)
        predicted_index = np.argmax(predictions, axis=1)
        predicted_emotion = label_encoder.inverse_transform(predicted_index)
        return predicted_emotion[0]
    else:
        return "Error extracting features"
