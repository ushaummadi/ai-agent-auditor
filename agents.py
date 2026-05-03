import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# --- Agent 1 (Analytical) ---
def run_gemini(prompt):
    try:
        res = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{
                "role": "user",
                "content": f"Write a detailed, structured, factual response:\n{prompt}"
            }]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Agent 1 Error: {str(e)}"


# --- Agent 2 (Creative) ---
def run_groq(prompt):
    try:
        res = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{
                "role": "user",
                "content": f"Write a short,detailed, creative, engaging response:\n{prompt}"
            }]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Agent 2 Error: {str(e)}"