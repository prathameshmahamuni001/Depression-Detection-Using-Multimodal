import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Questionnaire.css";  // ✅ Import CSS for styling

const Questionnaire = () => {
    const [answers, setAnswers] = useState({
        mcq1: "", mcq2: "", mcq3: "", mcq4: "", mcq5: "",
        mcq6: "", mcq7: "", mcq8: "", mcq9: "", mcq10: "",
        mcq11: "", mcq12: "", mcq13: "", mcq14: "", mcq15: "",
        openEnded1: "", openEnded2: "", openEnded3: "", openEnded4: "",
        openEnded5: "", openEnded6: "", openEnded7: ""
    });

    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setAnswers((prev) => ({
            ...prev,
            [name]: value,
        }));
    };

    const handleSubmit = async () => {
        setLoading(true);
        setError("");
        try {
            const response = await fetch("http://127.0.0.1:5000/submit_questionnaire", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    mcq_responses: Object.values(answers).slice(0, 15),
                    open_ended_responses: Object.values(answers).slice(15)
                }),
            });

            const data = await response.json();
            setResults(data);

            setTimeout(() => {
                navigate("/final-output");
            }, 3000);

        } catch (error) {
            console.error("Error submitting questionnaire:", error);
            setError("Failed to submit. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="questionnaire-container">
            <div className="questionnaire-box">
                <h1 className="questionnaire-title">Depression Questionnaire</h1>

                {/* MCQ Questions */}
                {[
                    "Do you feel sad often?",
                    "Do you have trouble sleeping?",
                    "Do you feel fatigued or low on energy?",
                    "Have you lost interest in activities you once enjoyed?",
                    "Do you find it hard to concentrate or make decisions?",
                    "Do you often feel hopeless about the future?",
                    "Have you noticed changes in your appetite?",
                    "Do you frequently experience feelings of guilt or worthlessness?",
                    "Do you feel more irritable or frustrated than usual?",
                    "Do you avoid social interactions and prefer to be alone?",
                    "Have you experienced sudden mood swings?",
                    "Do you feel anxious or restless without any specific reason?",
                    "Have you had thoughts of self-harm or suicide?",
                    "Do you struggle to complete daily tasks or maintain hygiene?",
                    "Have you been feeling emotionally numb or disconnected from reality?",
                ].map((question, index) => (
                    <div key={index} className="question-card">
                        <label>{question}</label>
                        <select name={`mcq${index + 1}`} onChange={handleChange}>
                            <option value="">Select</option>
                            <option value="A">Rarely</option>
                            <option value="B">Sometimes</option>
                            <option value="C">Often</option>
                            <option value="D">Almost Always</option>
                        </select>
                    </div>
                ))}

                {/* Open-Ended Questions */}
                {[
                    "Can you describe how you have been feeling emotionally in the past week?",
                    "What are some thoughts that frequently occupy your mind these days?",
                    "Have there been any recent life changes or events that have affected your mood?",
                    "How would you describe your motivation to complete daily tasks?",
                    "Do you feel supported by friends or family when you are struggling emotionally?",
                    "What activities or situations make you feel the most stressed or overwhelmed?",
                    "If you could change one thing about your emotional well-being, what would it be?",
                ].map((question, index) => (
                    <div key={index} className="question-card">
                        <label>{question}</label>
                        <input type="text" name={`openEnded${index + 1}`} onChange={handleChange} />
                    </div>
                ))}

                <button onClick={handleSubmit} className="submit-button" disabled={loading}>
                    {loading ? "Submitting..." : "Submit"}
                </button>

                {/* Show Error Message if any */}
                {error && <p className="error-message">{error}</p>}

                {/* Show Results on the Same Page */}
                {results && (
                    <div className="results-box">
                        {/* <h2>Final Results:</h2>
                        <p><strong>MCQ Score:</strong> {results.mcq_score}</p>
                        <p><strong>Open-Ended Score:</strong> {results.open_ended_score}</p>
                        <p><strong>Final Depression Score:</strong> {results.final_score}</p>
                        <p className="redirect-message">Redirecting to Final Output Page...</p> */}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Questionnaire;
