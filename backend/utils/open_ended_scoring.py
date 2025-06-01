import openai

def analyze_open_ended_responses(response_text):
    prompt = f"""
    You are a mental health expert. Analyze the following response for depression indicators:
    "{response_text}"
    Give a score from 0 to 100 where 0 means no depression and 100 means severe depression.
    Just return the number, nothing else.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}],
            max_tokens=10
        )
        return int(response["choices"][0]["message"]["content"].strip())
    except:
        return 50  # Default fallback score
