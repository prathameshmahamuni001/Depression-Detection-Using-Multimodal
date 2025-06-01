import React from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css"; // External CSS for styling

const Home = () => {
  const navigate = useNavigate();

  const handleStartAnalysis = () => {
    navigate("/text-analysis"); // Redirect to image analysis first
  };

  return (
    <div className="home-container">
      <div className="overlay"></div>
      <div className="content">
        <h1 className="title">Multimodal Depression Detection</h1>
        <p className="description">
          A scientific approach to assessing mental health using AI-powered analysis.  
          Upload images, audio, video, and answer a few questions to get a detailed assessment.
        </p>
        <button className="start-button" onClick={handleStartAnalysis}>
          Start Analysis
        </button>
      </div>
    </div>
  );
};

export default Home;
