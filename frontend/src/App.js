import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import ImageAnalysis from "./components/ImageAnalysis";
import AudioAnalysis from "./components/AudioAnalysis";
import VideoAnalysis from "./components/VideoAnalysis";
import TextAnalysis from "./components/TextAnalysis";
import Questionnaire from "./components/Questionnaire";
import FinalOutput from "./components/FinalOutput";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/image-analysis" element={<ImageAnalysis />} />
        <Route path="/audio-analysis" element={<AudioAnalysis />} />
        <Route path="/video-analysis" element={<VideoAnalysis />} />
        <Route path="/text-analysis" element={<TextAnalysis />} />
        <Route path="/questionnaire" element={<Questionnaire />} />
        <Route path="/final-output" element={<FinalOutput />} />
      </Routes>
    </Router>
  );
}

export default App;
