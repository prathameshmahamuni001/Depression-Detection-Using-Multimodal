import React from "react";

const MCQQuestion = ({ question, onAnswer }) => {
  return (
    <div>
      <p>{question.question}</p>
      {question.options.map((opt, index) => (
        <label key={index}>
          <input
            type="radio"
            name={question.id}
            value={opt}
            onChange={(e) => onAnswer(question.id, e.target.value)}
          />
          {opt}
        </label>
      ))}
    </div>
  );
};

export default MCQQuestion;
