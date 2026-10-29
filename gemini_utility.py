import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Automatically reads GEMINI_API_KEY from environment/.env
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def load_gemini_pro_model():
    """Initializes and returns a multi-turn chat session."""
    return client.chats.create(model="gemini-3.8-flash")