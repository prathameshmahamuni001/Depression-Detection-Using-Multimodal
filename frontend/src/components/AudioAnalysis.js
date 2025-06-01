import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { analyzeAudio } from "../services/api";
import "./AudioAnalysis.css"; // External CSS for styles

const AudioAnalysis = () => {
    const [audioFile, setAudioFile] = useState(null);
    const [previewURL, setPreviewURL] = useState(null);
    const [analysisResult, setAnalysisResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setAudioFile(file);
            setPreviewURL(URL.createObjectURL(file)); // Show selected audio
        }
    };

    const handleUpload = async () => {
        if (!audioFile) {
            alert("Please select an audio file first.");
            return;
        }

        setLoading(true);
        const formData = new FormData();
        formData.append("audio", audioFile);

        try {
            const response = await analyzeAudio(formData);
            setAnalysisResult(response);
            setTimeout(() => navigate("/video-analysis"), 3000); // Auto-navigate after 3 sec
        } catch (error) {
            alert("Error analyzing audio");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="audio-analysis-container">
            <div className="overlay"></div>
            <div className="content">
                <h2 className="title">Audio-Based Depression Analysis</h2>
                <p className="subtitle">
                    Upload a short audio clip, and our AI will analyze your voice tone.
                </p>

                <input type="file" accept="audio/*" onChange={handleFileChange} className="file-input" />

                {previewURL && (
                    <div className="preview-container">
                        <audio controls className="audio-player">
                            <source src={previewURL} type="audio/mpeg" />
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                )}

                <button className="analyze-button" onClick={handleUpload} disabled={loading}>
                    {loading ? "Analyzing..." : "Upload & Analyze"}
                </button>

                {analysisResult && (
                    <div className="result">
                        {/* <h3>Analysis Result</h3>
                        <p><strong>Detected Emotion:</strong> {analysisResult.emotion}</p>
                        <p><strong>Depression Score:</strong> {analysisResult.depression_score}</p>
                        <p className="redirect-message">⏳ Redirecting to Video Analysis in 3 seconds...</p> */}
                    </div>
                )}
            </div>
        </div>
    );
};

export default AudioAnalysis;
