import openai
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

# Global dictionary to store scores
from utils.session_store import session_data


# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Sentiment Analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_open_ended_responses(response_text):
    """
    Analyzes open-ended responses for depression indicators.
    - If OpenAI API is available, it uses GPT.
    - If not, it falls back to sentiment analysis.
    - Returns a depression score between **0 to 50**.
    """

    prompt = f"""
    You are a mental health expert. Analyze the following response for depression indicators:
    "{response_text}"
    Give a score from 0 to 50 where 0 means no depression and 50 means severe depression.
    Just return the number, nothing else.
    """

    try:
        if OPENAI_API_KEY:
            openai.api_key = OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a mental health expert."},
                    {"role": "user", "content": prompt}
                ]
            )
            score = int(response["choices"][0]["message"]["content"].strip())

            # Ensure score is in the range 0-50
            score = max(0, min(score, 50))
            session_data["open_ended_score"] = score
            return score

        else:
            raise Exception("OpenAI API Key Missing")

    except Exception as e:
        print(f"Error: ")
        print("Using Sentiment Analysis")

        # **Backup Sentiment Analysis**
        sentiment_score = sia.polarity_scores(response_text)["compound"]

        # Convert sentiment score (-1 to +1) into depression score (0 to 50)
        depression_score = ((1 - sentiment_score) / 2) * 100 
        openended_depression = round(depression_score, 2)*10

        # Store in session data
        session_data["open_ended_score"] = openended_depression

        return openended_depression
