import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { analyzeImage } from "../services/api";
import "./ImageAnalysis.css"; // External CSS for styles

const ImageAnalysis = () => {
    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(null);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setImage(file);
            setPreview(URL.createObjectURL(file)); // Display selected image
        }
    };

    const handleUpload = async () => {
        if (!image) {
            alert("Please select an image first.");
            return;
        }
        setLoading(true); // Show loading state

        const formData = new FormData();
        formData.append("file", image);

        try {
            const response = await analyzeImage(formData);
            setResult(response);
            setTimeout(() => navigate("/audio-analysis"), 3000); // Auto-navigate after 3 sec
        } catch (error) {
            alert("Error analyzing image");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="image-analysis-container">
            <div className="overlay"></div>
            <div className="content">
                <h2 className="title">Image-Based Depression Analysis</h2>
                <p className="subtitle">
                    Upload a facial image, and our AI will analyze emotional expressions.
                </p>

                <input type="file" accept="image/*" onChange={handleFileChange} className="file-input" />

                {preview && (
                    <div className="preview-container">
                        <img src={preview} alt="Selected Preview" className="preview-image" />
                    </div>
                )}

                <button className="analyze-button" onClick={handleUpload} disabled={loading}>
                    {loading ? "Analyzing..." : "Analyze"}
                </button>

                {result && (
                    <div className="result">
                        {/* <h3>Analysis Result</h3>
                        <p><strong>Detected Emotion:</strong> {result.emotion}</p>
                        <p><strong>Depression Score:</strong> {result.depression_score}</p>
                        <p className="redirect-message">⏳ Redirecting to Audio Analysis in 3 seconds...</p> */}
                    </div>
                )}
            </div>
        </div>
    );
};

export default ImageAnalysis;
