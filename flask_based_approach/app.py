from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename
from text_emotion import predict_emotion_text
from image_emotion import predict_emotion_image
from audio_emotion import predict_emotion_audio
from video_emotion import predict_emotion_video

app = Flask(__name__)

# Ensure directories exist for uploads
UPLOAD_FOLDER = 'static/uploads/'
IMAGE_FOLDER = os.path.join(UPLOAD_FOLDER, 'images/')
AUDIO_FOLDER = os.path.join(UPLOAD_FOLDER, 'audio/')
VIDEO_FOLDER = os.path.join(UPLOAD_FOLDER, 'videos/')

app.config['IMAGE_UPLOADS'] = IMAGE_FOLDER
app.config['AUDIO_UPLOADS'] = AUDIO_FOLDER
app.config['VIDEO_UPLOADS'] = VIDEO_FOLDER

# Index route
@app.route('/')
def index():
    return render_template('index.html')

# Route for text emotion prediction
@app.route('/predict_text', methods=['POST'])
def predict_text():
    user_input = request.form['text_input']
    emotion = predict_emotion_text(user_input)
    return render_template('index.html', text_emotion=emotion)

# Route for image emotion prediction
@app.route('/predict_image', methods=['POST'])
def predict_image():
    if 'image' in request.files:
        image_file = request.files['image']
        if image_file.filename != '':
            filename = secure_filename(image_file.filename)
            filepath = os.path.join(app.config['IMAGE_UPLOADS'], filename)
            image_file.save(filepath)
            emotion = predict_emotion_image(filepath)
            return render_template('index.html', image_emotion=emotion)
    return render_template('index.html', image_emotion="No image provided")

# Route for audio emotion prediction
@app.route('/predict_audio', methods=['POST'])
def predict_audio():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        if audio_file.filename != '':
            filename = secure_filename(audio_file.filename)
            filepath = os.path.join(app.config['AUDIO_UPLOADS'], filename)
            audio_file.save(filepath)
            emotion = predict_emotion_audio(filepath)
            return render_template('index.html', audio_emotion=emotion)
    return render_template('index.html', audio_emotion="No audio provided")

# Route for video emotion prediction
@app.route('/predict_video', methods=['POST'])
def predict_video():
    if 'video' in request.files:
        video_file = request.files['video']
        if video_file.filename != '':
            filename = secure_filename(video_file.filename)
            filepath = os.path.join(app.config['VIDEO_UPLOADS'], filename)
            video_file.save(filepath)
            emotion = predict_emotion_video(filepath)
            return render_template('index.html', video_emotion=emotion)
    return render_template('index.html', video_emotion="No video provided")

if __name__ == '__main__':
    app.run(debug=True)
