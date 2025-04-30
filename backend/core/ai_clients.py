# backend/core/ai_client.py

import os
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

async def ask_ai(prompt: str) -> str:
    payload = {
        "model": "mistral-7b-8k",
        "messages": [
            {"role": "system", "content": "You are a helpful and fair judge of which thing beats another."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error parsing response: {e}"
    else:
        return f"Error from Groq API: {response.status_code}, {response.text}"

# backend/core/ai_client.py

async def query_groq(guess_word: str, seed_word: str) -> str:
    prompt = f"Does '{guess_word}' beat '{seed_word}'? Reply only with 'YES' or 'NO'."
    return await ask_ai(prompt)

async def query_mistral(guess_word: str, seed_word: str) -> str:
    prompt = f"Does '{guess_word}' beat '{seed_word}'? Reply only with 'YES' or 'NO'."
    return await ask_ai(prompt)


