# prompts.py

TASK_PROMPT = """
You are a helpful AI assistant.

Task:
{task}

Provide a clear, high-quality, and useful response.
"""
EVALUATION_PROMPT = """
You are a strict, unbiased AI evaluator.

IMPORTANT RULES:
- Do NOT favor longer answers
- Judge ONLY based on relevance to the task
- Be fair and critical

Task:
{task}

Responses:
Agent1: {gemini}
Agent2: {groq}

Score each (0–10) based on:
- Relevance
- Clarity
- Helpfulness

Return ONLY valid JSON:

{{
  "gemini": 8,
  "groq": 7,
  "winner": "gemini",
  "reason": "Gemini is clearer"
}}
"""
