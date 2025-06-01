import axios from "axios";

// 🎯 Backend API Base URL (Ensure it's correct)
const API_BASE_URL = "http://127.0.0.1:5000";

// 🎯 Create Axios Instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: { "Content-Type": "application/json" },
});

// ───────────────────────────────────────────────────────────
// ✅ IMAGE ANALYSIS API
// ───────────────────────────────────────────────────────────
export const analyzeImage = async (formData) => {
  try {
    const response = await api.post("/analyze_image", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return response.data;
  } catch (error) {
    console.error("❌ Error analyzing image:", error);
    return { error: "Failed to analyze image" };
  }
};

// ───────────────────────────────────────────────────────────
// ✅ AUDIO ANALYSIS API
// ───────────────────────────────────────────────────────────
export const analyzeAudio = async (formData) => {
  try {
    const response = await api.post("/analyze_audio", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return response.data;
  } catch (error) {
    console.error("❌ Error analyzing audio:", error);
    return { error: "Failed to analyze audio" };
  }
};

// ───────────────────────────────────────────────────────────
// ✅ VIDEO ANALYSIS API
// ───────────────────────────────────────────────────────────
export const analyzeVideo = async (videoFile) => {
  try {
    const formData = new FormData();
    formData.append("video", videoFile);

    const response = await api.post("/analyze_video", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    return response.data;
  } catch (error) {
    console.error("❌ Error analyzing video:", error);
    return { error: "Failed to analyze video" };
  }
};

// ───────────────────────────────────────────────────────────
// ✅ TEXT ANALYSIS API (Uses OpenRouter AI API for DeepSeek R1 Zero)
// ───────────────────────────────────────────────────────────
export const analyzeText = async (text) => {
  try {
    console.log("🔄 Sending Request to Backend...");
    const response = await api.post("/analyze_text", { text });

    console.log("📩 API Response Data:", response.data);
    return response.data;
  } catch (error) {
    console.error("❌ API Error in analyzeText:", error);
    return { error: "Failed to analyze text" };
  }
};

// ───────────────────────────────────────────────────────────
// ✅ SUBMIT QUESTIONNAIRE (MCQ + Open-ended responses)
// ───────────────────────────────────────────────────────────
export const submitQuestionnaire = async (data) => {
  try {
    const response = await api.post("/submit_questionnaire", data);
    return response.data;
  } catch (error) {
    console.error("❌ Error submitting questionnaire:", error);
    return { error: "Failed to submit questionnaire" };
  }
};

// ───────────────────────────────────────────────────────────
// ✅ FINAL DEPRESSION SCORE API
// ───────────────────────────────────────────────────────────
export const getFinalScore = async () => {
  try {
    // Retrieve scores from local storage
    const image_score = localStorage.getItem("image_score") || 50;
    const audio_score = localStorage.getItem("audio_score") || 50;
    const video_score = localStorage.getItem("video_score") || 50;
    const text_score = localStorage.getItem("text_score") || 50;
    const questionnaire_score = localStorage.getItem("questionnaire_score") || 50;

    const requestData = {
      image_score: Number(image_score),
      audio_score: Number(audio_score),
      video_score: Number(video_score),
      text_score: Number(text_score),
      questionnaire_score: Number(questionnaire_score),
    };

    console.log("📩 Sending final scoring data:", requestData);

    const response = await api.post("/final_score", requestData);
    return response.data;
  } catch (error) {
    console.error("❌ Error fetching final score:", error);
    return { error: "Failed to fetch final score" };
  }
};

export default api;
