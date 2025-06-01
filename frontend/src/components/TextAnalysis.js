import React, { useState, useEffect } from "react";
import { analyzeText } from "../services/api";
import { useNavigate } from "react-router-dom";
import "./TextAnalysis.css"; // External CSS for styling

const TextAnalysis = () => {
    const [text, setText] = useState("");
    const [emotion, setEmotion] = useState("");
    const [depressionScore, setDepressionScore] = useState(null);
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleAnalyzeText = async () => {
        setError(""); // Clear previous errors
        if (!text.trim()) {
            setError("Please enter some text for analysis.");
            return;
        }

        setLoading(true); // Show loading state

        try {
            console.log("🚀 Sending Text to API:", text);
            const response = await analyzeText(text);
            console.log("✅ API Response Received:", response);

            if (response && response.emotion && response.depression_score !== undefined) {
                setEmotion(response.emotion);
                setDepressionScore(response.depression_score);
            } else {
                setError("❌ Invalid response from server. Please try again.");
            }
        } catch (err) {
            console.error("❌ Error in Text Analysis:", err);
            setError("Error analyzing text. Please try again.");
        } finally {
            setLoading(false); // Hide loading state
        }
    };

    // Automatically navigate to Video Analysis after 2 seconds
    useEffect(() => {
        if (depressionScore !== null) {
            const timer = setTimeout(() => {
                navigate("/image-analysis");
            }, 3000);
            return () => clearTimeout(timer); // Cleanup timeout
        }
    }, [depressionScore, navigate]);

    return (
        <div className="text-analysis-container">
            <div className="overlay"></div>
            <div className="content">
                <h2 className="title">Text-Based Depression Analysis</h2>
                <p className="subtitle">
                    Enter a short passage about your feelings, and our AI will analyze its emotional tone.
                </p>
                
                <textarea
                    className="text-input"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    placeholder="Describe your emotions here..."
                />
                
                <button className="analyze-button" onClick={handleAnalyzeText} disabled={loading}>
                    {loading ? "Analyzing..." : "Analyze"}
                </button>

                {error && <p className="error-message">{error}</p>}

                {emotion && (
                    <div className="result">
                        {/* <h3>Analysis Result</h3>
                        <p><strong>Detected Emotion:</strong> {emotion}</p>
                        <p><strong>Depression Score:</strong> {depressionScore}</p>
                        <p className="redirect-message">⏳ Redirecting to Video Analysis in 3 seconds...</p> */}
                    </div>
                )}
            </div>
        </div>
    );
};

export default TextAnalysis;
