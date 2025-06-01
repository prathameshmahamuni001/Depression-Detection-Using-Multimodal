# config.py

OPENROUTER_API_KEY = "<YOUR_OPENROUTER_API_KEY>"  # Replace with actual key
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "deepseek/deepseek-r1-zero:free"

OPENROUTER_HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>",  # Replace with your site URL
    "X-Title": "<YOUR_SITE_NAME>",  # Replace with your site name
}
