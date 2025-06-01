import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Chart } from "react-google-charts";
import axios from "axios";
import "./FinalOutput.css"; // ✅ Updated CSS

const FinalOutput = () => {
  const [finalScore, setFinalScore] = useState(null);
  const [severity, setSeverity] = useState("");
  const [advice, setAdvice] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchFinalScore = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5000/final_score");
        setFinalScore(response.data.final_score);
        setSeverity(response.data.severity);
        setAdvice(response.data.advice);
      } catch (error) {
        console.error("❌ Error fetching final score:", error);
      }
    };

    fetchFinalScore();
  }, []);

  const restartAnalysis = () => {
    navigate("/"); // 🔄 Restart Analysis
  };

  return (
    <div className="final-output-container">
      <div className="final-output-box">
        <h1 className="title">🧠 Depression Analysis Result</h1>

        {finalScore !== null ? (
          <div className="results">
            <h2 className="score">
              📊 Your Final Depression Score:{" "}
              <span className={`severity ${severity.toLowerCase()}`}>{finalScore}</span>
            </h2>
            <h3 className="severity-level">
              🩺 Severity Level: <span className={`severity ${severity.toLowerCase()}`}>{severity}</span>
            </h3>
            <p className="advice">📢 <b>Advice:</b> {advice}</p>

            {/* 📊 Fixed Chart (Centered) */}
            <div className="chart-container">
              <Chart
                width={"450px"}  // ✅ Adjusted for better centering
                height={"300px"}
                chartType="ColumnChart"
                loader={<div>Loading Chart...</div>}
                data={[
                  ["Category", "Score", { role: "style" }],
                  ["Final Score", finalScore, "#3498db"],
                ]}
                options={{
                  title: "Final Depression Score",
                  hAxis: { title: "Analysis", minValue: 0, maxValue: 100 },
                  vAxis: { title: "Score", minValue: 0, maxValue: 100 },
                  legend: "none",
                }}
              />
            </div>

            {/* 🔄 Restart Button */}
            <button onClick={restartAnalysis} className="restart-btn">🔄 Restart Analysis</button>
          </div>
        ) : (
          <p className="loading">Loading results...</p>
        )}
      </div>
    </div>
  );
};

export default FinalOutput;
