import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Load the trained image model
image_model = load_model('models/model_filter_collab.keras')

# Dictionary of emotions
emotion_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

# Predict emotion from image
def predict_emotion_image(img_path):
    img = image.load_img(img_path, color_mode='grayscale', target_size=(48, 48))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = 255
    predictions = image_model.predict(img_array)
    max_index = int(np.argmax(predictions))
    predicted_emotion = emotion_dict[max_index]
    return predicted_emotion
