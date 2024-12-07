from flask import Flask, render_template, request, redirect, url_for, session
import tensorflow as tf
import numpy as np

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'

# Load models
text_model = tf.keras.models.load_model('models/text_model.keras')
image_model = tf.keras.models.load_model('models/image_model.keras')
audio_model = tf.keras.models.load_model('models/audio_model.h5')
video_model = tf.keras.models.load_model('models/video_model.keras')

# Ensemble prediction storage
@app.route('/')
def home():
    session.clear()  # Clear previous session data
    return render_template('index.html')

@app.route('/text_input', methods=['GET', 'POST'])
def text_input():
    if request.method == 'POST':
        text = request.form['text']
        # Assume predict_text is a function returning the emotion
        emotion = predict_text(text)
        session['text_emotion'] = emotion
        return redirect(url_for('image_input'))
    return render_template('text_input.html')

@app.route('/image_input', methods=['GET', 'POST'])
def image_input():
    if request.method == 'POST':
        image = request.files['image']
        # Assume predict_image is a function returning the emotion
        emotion = predict_image(image)
        session['image_emotion'] = emotion
        return redirect(url_for('audio_input'))
    return render_template('image_input.html')

@app.route('/audio_input', methods=['GET', 'POST'])
def audio_input():
    if request.method == 'POST':
        audio = request.files['audio']
        # Assume predict_audio is a function returning the emotion
        emotion = predict_audio(audio)
        session['audio_emotion'] = emotion
        return redirect(url_for('video_input'))
    return render_template('audio_input.html')

@app.route('/video_input', methods=['GET', 'POST'])
def video_input():
    if request.method == 'POST':
        video = request.files['video']
        # Assume predict_video is a function returning the emotion
        emotion = predict_video(video)
        session['video_emotion'] = emotion
        return redirect(url_for('result'))
    return render_template('video_input.html')

@app.route('/result')
def result():
    # Aggregate emotions for the ensemble result
    emotions = [session.get('text_emotion'), session.get('image_emotion'),
                session.get('audio_emotion'), session.get('video_emotion')]
    final_emotion = majority_voting(emotions)
    return render_template('result.html', final_emotion=final_emotion)

# Functions for each model (stub functions)
def predict_text(text):
    return "Happy"  # Replace with model prediction logic

def predict_image(image):
    return "Sad"  # Replace with model prediction logic

def predict_audio(audio):
    return "Angry"  # Replace with model prediction logic

def predict_video(video):
    return "Neutral"  # Replace with model prediction logic

def majority_voting(emotions):
    from collections import Counter
    count = Counter(emotions)
    return count.most_common(1)[0][0]  # Returns most common emotion

if __name__ == '__main__':
    app.run(debug=True)
