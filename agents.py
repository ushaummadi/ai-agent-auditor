import os
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
# --- Wikipedia API ---
def fetch_context(query):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        res = requests.get(url)
        data = res.json()
        return data.get("extract", "")
    except:
        return ""
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
                "content": f"Write a short,detailed, creative, engaging answer:\n{prompt}"
            }]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Agent 2 Error: {str(e)}"
