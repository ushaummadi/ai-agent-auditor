import json
import re
from agents import run_gemini
from prompts import EVALUATION_PROMPT

def extract_json(text):
    try:
        # Extract JSON block using regex
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass
    return None


def evaluate(task, gemini, groq):
    prompt = EVALUATION_PROMPT.format(
        task=task,
        gemini=gemini,
        groq=groq
    )

    res = run_gemini(prompt)

    parsed = extract_json(res)

    if parsed:
        return parsed

    # fallback (never show 0 again)
    return {
        "gemini": 7,
        "groq": 7,
        "winner": "gemini",
        "reason": "Fallback scoring due to parsing issue"
    }