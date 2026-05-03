from agents import run_gemini, run_groq
from evaluator import evaluate
from prompts import TASK_PROMPT

def run_pipeline(task):
    prompt = TASK_PROMPT.format(task=task)

    gemini_output = run_gemini(prompt)
    groq_output = run_groq(prompt)

    scores = evaluate(task, gemini_output, groq_output)

    return {
        "outputs": {
            "gemini": gemini_output,
            "groq": groq_output
        },
        "scores": scores
    }