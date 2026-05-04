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
- Short answers can score HIGH if better
- Penalize unnecessary length

Task:
{task}

Responses:
Agent1: {gemini}
Agent2: {groq}

Score each (0–10) based on:
1. Relevance to task
2. Clarity
3. Helpfulness
4. Creativity (if applicable)

Return ONLY JSON:

{
  "gemini": <score>,
  "groq": <score>,
  "winner": "<gemini or groq or tie>",
  "reason": "<short explanation>"
}
"""
