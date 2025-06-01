import React, { useState } from "react";
import { analyzeVideo } from "../services/api";
import { useNavigate } from "react-router-dom";
import "./VideoAnalysis.css"; // External CSS

const VideoAnalysis = () => {
    const [videoFile, setVideoFile] = useState(null);
    const [previewURL, setPreviewURL] = useState(null);
    const [emotion, setEmotion] = useState("");
    const [depressionScore, setDepressionScore] = useState(null);
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleVideoChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setVideoFile(file);
            setPreviewURL(URL.createObjectURL(file)); // Live video preview
        }
    };

    const handleAnalyzeVideo = async () => {
        setError("");
        if (!videoFile) {
            setError("❌ Please upload a video file.");
            return;
        }

        setLoading(true);
        try {
            console.log("🚀 Sending Video to API...");
            const response = await analyzeVideo(videoFile);
            console.log("✅ API Response Received:", response);

            if (response && response.emotion && response.depression_score !== undefined) {
                setEmotion(response.emotion);
                setDepressionScore(response.depression_score);

                setTimeout(() => {
                    navigate("/questionnaire"); // Auto navigate after 3 sec
                }, 3000);
            } else {
                setError("❌ Invalid response from server. Please try again.");
            }
        } catch (err) {
            console.error("❌ Error in Video Analysis:", err);
            setError("Error analyzing video. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="video-analysis-container">
            <div className="overlay"></div>
            <div className="content">
                <h2 className="title">Video-Based Depression Analysis 🎥</h2>
                <p className="subtitle">
                    Upload a short video clip, and our AI will analyze facial expressions.
                </p>

                <input type="file" accept="video/*" onChange={handleVideoChange} className="file-input" />

                {previewURL && (
                    <div className="video-preview">
                        <video controls className="video-player">
                            <source src={previewURL} type="video/mp4" />
                            Your browser does not support the video tag.
                        </video>
                    </div>
                )}

                <button className="analyze-button" onClick={handleAnalyzeVideo} disabled={loading}>
                    {loading ? "Analyzing..." : "Upload & Analyze"}
                </button>

                {error && <p className="error">{error}</p>}

                {emotion && (
                    <div className="result">
                        {/* <h3>Analysis Result</h3>
                        <p><strong>Detected Emotion:</strong> {emotion}</p>
                        <p><strong>Depression Score:</strong> {depressionScore}</p>
                        <p className="redirect-message">⏳ Redirecting to Questionnaire in 3 seconds...</p> */}
                    </div>
                )}
            </div>
        </div>
    );
};

export default VideoAnalysis;
