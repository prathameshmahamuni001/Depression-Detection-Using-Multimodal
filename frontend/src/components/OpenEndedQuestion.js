import React, { useState } from "react";
import { analyzeText } from "../services/api";

const OpenEndedQuestion = () => {
    const [question, setQuestion] = useState("How do you feel today?");
    const [answer, setAnswer] = useState("");
    const [score, setScore] = useState(null);

    const handleSubmit = async () => {
        const result = await analyzeText(question, answer);
        if (result) {
            setScore(result.score);
        }
    };

    return (
        <div>
            <h2>{question}</h2>
            <textarea
                value={answer}
                onChange={(e) => setAnswer(e.target.value)}
                placeholder="Type your answer here..."
            />
            <button onClick={handleSubmit}>Analyze</button>
            {score !== null && <p>Depression Score: {score}</p>}
        </div>
    );
};

export default OpenEndedQuestion;
