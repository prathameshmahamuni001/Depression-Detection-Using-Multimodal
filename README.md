# 🧠 Multimodal Depression Detection System

An AI-powered system designed to assess signs of depression by analyzing multiple human inputs: facial expressions, speech tone, text sentiment, and questionnaire responses. This project uses an ensemble approach to ensure a holistic and more reliable mental health evaluation.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Project Demo](#project-demo)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [How It Works](#how-it-works)
- [Setup & Installation](#setup--installation)
- [Features](#features)
- [Results & Visualizations](#results--visualizations)
- [Limitations](#limitations)
- [Future Scope](#future-scope)
- [License](#license)

---

## ✅ About the Project

Depression can manifest in many ways — through tone of voice, expressions, written words, or even self-reflection. This system aims to assist early detection by combining:

- 📷 Facial emotion analysis
- 🔉 Speech tone detection
- ✍️ Text-based sentiment analysis
- 🧾 Questionnaire scoring

Each input is analyzed using its own pre-trained model, and the results are fused for a final depression score and classification.

---

## 🎥 Project Demo

> *Insert YouTube/video demo link here if available*

---

## 🛠 Tech Stack

| Domain         | Technologies Used                    |
|----------------|--------------------------------------|
| Frontend       | Tkinter (GUI for input & output)     |
| Audio Analysis | Librosa, TensorFlow/Keras            |
| Image/Video    | OpenCV, CNN-based Emotion Model      |
| Text Analysis  | DeepSeek API, Transformers (NLP)     |
| Fusion Logic   | Weighted Late Fusion (Ensemble)      |
| Visualization  | Matplotlib, Seaborn                  |
| Deployment     | Local Python-based system (GUI)      |

---

## 🧩 System Architecture


     [Image]     [Audio]     [Video]     [Text]     [Questionnaire]
        ↓           ↓           ↓           ↓              ↓
 Image Model  Audio Model  Video Model  Text Model    Scoring Logic
        ↓           ↓           ↓           ↓              ↓
       └───────────── Weighted Fusion (Late Fusion) ─────────────┘
                              ↓
                      Final Depression Score
                              ↓
                      Depression Level Output



---

## ⚙️ How It Works

1. **User Inputs**:
   - Uploads image, audio, video, enters text, and answers questions.
2. **Modality-specific Models**:
   - Each input is passed through a specialized AI model that outputs a depression score (1–10).
3. **Score Fusion**:
   - Scores are combined using weighted average:
     - Image: 10%
     - Audio: 10%
     - Video: 20%
     - Text: 25%
     - Questionnaire: 35%
4. **Final Output**:
   - A score from 1–10 + depression level (Normal, Mild, Moderate, Severe)
   - Visualized using a bar graph

---

## 📦 Setup & Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/multimodal-depression-detector.git
cd multimodal-depression-detector

pip install -r requirements.txt

python app.py


Use the GUI

Upload your inputs

Click "Predict"

View your results and depression level

🌟 Features
Analyze multiple modalities: image, audio, video, text, and questionnaire

Real-time scoring and visualization

User-friendly GUI built with Tkinter

Late fusion strategy for accurate ensemble predictions

Clear classification: Low, Mild, Moderate, Severe

📊 Results & Visualizations
The system provides:

Individual modality scores

Final weighted score

Bar chart comparison

Classification level based on final score

⚠️ Limitations
Requires clear and valid input files for each modality

Pre-trained models may not generalize to all demographics

Subjective questionnaire scoring may influence overall output

🔮 Future Scope
Deploy on web using Flask/Streamlit

Use real-time webcam/audio for dynamic detection

Add multilingual text support

Enhance accuracy with larger, diverse datasets



 
