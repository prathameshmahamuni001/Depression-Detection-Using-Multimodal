from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from routes.image_analysis import predict_depression_from_image
from routes.audio_analysis import analyze_audio 
from routes.text_analysis import predict_emotion_text
from routes.questionnaire import questionnaire_bp
from routes.video_analysis import video_bp


from services.openended_analysis import analyze_open_ended_responses
from utils.mcq_scoring import calculate_mcq_score  # Ensure this function exists



app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    """Handles image upload & returns depression score."""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Get depression score
    result = predict_depression_from_image(file_path)

    return jsonify(result)


# Route for text analysis
@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json()
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"error": "No text provided"}), 400

        result = predict_emotion_text(text)

        # Ensure response contains both emotion & depression_score
        if "emotion" in result and "depression_score" in result:
            return jsonify(result)
        else:
            return jsonify({"error": "Invalid response format"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Register blueprints
app.register_blueprint(video_bp)

UPLOAD_FOLDER_AUDIO = "uploads/audio"
os.makedirs(UPLOAD_FOLDER_AUDIO, exist_ok=True)

@app.route("/analyze_audio", methods=["POST"])
def analyze_audio_route():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    file_path = "uploads/" + audio_file.filename
    audio_file.save(file_path)  # Save file temporarily

    return analyze_audio(file_path)  # ✅ Pass the correct argument







@app.route("/submit_questionnaire", methods=["POST"])
def submit_questionnaire():
    try:
        data = request.json  # Get request data

        # Extract MCQ & Open-ended responses
        mcq_responses = data.get("mcq_responses", [])
        open_ended_responses = data.get("open_ended_responses", [])

        # Calculate MCQ score
        mcq_score = calculate_mcq_score(mcq_responses)  # Make sure this function exists

        # Analyze Open-ended responses using ChatGPT
        open_ended_score = 0
        for response in open_ended_responses:
            score = analyze_open_ended_responses(response)
            if score is not None:
                open_ended_score += score

        # Normalize Open-Ended Score (Scale from 0-100 to 0-10)
        open_ended_score = open_ended_score / (10 * max(len(open_ended_responses), 1))

        # Final Score Calculation
        final_score = (mcq_score * 1) + (open_ended_score * 0.5)

        return jsonify({
            "mcq_score": mcq_score,
            "open_ended_score": open_ended_score,
            "final_score": final_score
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

from utils.final_scoring import calculate_final_score


@app.route("/final_score", methods=["GET"])
def get_final_score():
    result = calculate_final_score()
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)