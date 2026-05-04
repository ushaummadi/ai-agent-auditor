import os
import requests
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ---------- BETTER TOPIC EXTRACTION ----------
def extract_topic(prompt):
    """
    Extract meaningful keywords from user prompt
    """
    stopwords = {
        "write", "create", "generate", "make", "tell", "explain",
        "what", "is", "a", "an", "the", "for", "about", "of", "to"
    }

    words = prompt.lower().split()
    keywords = [w for w in words if w not in stopwords]

    # Take first 2–3 meaningful words
    topic = "_".join(keywords[:3])

    return topic if topic else "Artificial_intelligence"


# ---------- WIKIPEDIA API ----------
def fetch_context(prompt):
    try:
        topic = extract_topic(prompt)

        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
        res = requests.get(url)

        if res.status_code != 200:
            return ""

        data = res.json()
        return data.get("extract", "")

    except Exception:
        return ""


# ---------- AGENT 1 (ANALYTICAL) ----------
def run_gemini(prompt):
    try:
        context = fetch_context(prompt)

        if not context:
            context = "No external data available."

        res = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{
                "role": "user",
                "content": f"""
Use the following context if relevant:
{context}

Give a structured, detailed, high-quality answer.

Task:
{prompt}
"""
            }]
        )

        return res.choices[0].message.content

    except Exception as e:
        return f"Agent 1 Error: {str(e)}"


# ---------- AGENT 2 (CREATIVE) ----------
def run_groq(prompt):
    try:
        context = fetch_context(prompt)

        if not context:
            context = "No external data available."

        res = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{
                "role": "user",
                "content": f"""
Use the following context if relevant:
{context}

Give a short, creative,structured, detailed, engaging response.

Task:
{prompt}
"""
            }]
        )

        return res.choices[0].message.content

    except Exception as e:
        return f"Agent 2 Error: {str(e)}"
