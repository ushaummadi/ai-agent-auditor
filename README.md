# 🤖 AI Agent Auditor

Measure which AI agent actually performs best — not just guess.

---

## 🚀 Overview

AI Agent Auditor is a mini system that runs a given task across multiple AI agents and evaluates their performance automatically.

Instead of relying on intuition or hype, this tool helps users **objectively compare AI outputs** and identify the best-performing agent for a specific use case.

---

## 🎯 Problem

With so many AI models available, it’s hard to answer:

* Which AI is better for *my task*?
* Should I use a creative model or a structured one?
* Which output is actually more useful?

Most users guess.

👉 This project removes the guesswork.

---

## 💡 Solution

AI Agent Auditor:

* Runs the same task on multiple AI agents
* Compares outputs side-by-side
* Uses an AI evaluator (LLM-as-a-judge)
* Assigns scores and selects a winner

---

## 🧠 How It Works

1. User enters a task
2. Two AI agents generate responses:

   * 🧠 Analytical Agent → detailed, structured
   * 🎨 Creative Agent → short, engaging
3. An evaluator AI compares both outputs
4. Scores are assigned based on:

   * Clarity
   * Usefulness
   * Persuasiveness
5. A winner is selected with reasoning

---

## 🏗️ Architecture

```bash
User Input → Agents → Outputs → Evaluator → Scores + Winner → UI
```

---

## ✨ Features

* ⚡ Multi-agent execution
* 🤖 AI-powered evaluation (LLM-as-a-judge)
* 📊 Automatic scoring system
* 🏆 Winner detection with explanation
* 🎨 Clean Streamlit UI
* 🔄 Real-time comparison

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** — UI
* **Groq API** — LLM inference (fast & free tier)
* **Prompt Engineering**
* **dotenv** — environment variables

---

## 📁 Project Structure

```bash
ai-agent-auditor/
│
├── app.py                # Streamlit UI
├── orchestrator.py       # Pipeline controller
├── agents.py             # AI agents
├── evaluator.py          # Scoring logic
├── prompts.py            # Prompt templates
│
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── utils/
    └── parser.py         # JSON parsing helper
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/ai-agent-auditor
cd ai-agent-auditor

pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Environment Variables

Create a `.env` file:

```bash
GROQ_API_KEY=your_api_key
```

---

## 📸 Example Use Case

**Input:**

```
Write a catchy Instagram caption for a fitness product
```

**Output:**

* Two AI-generated responses
* Scores for each agent
* Winner with explanation

---

## 🧠 Key Concept: LLM-as-a-Judge

This project uses an evaluation technique where an AI model compares outputs from other AI models.

Used in:

* OpenAI Evals
* LangChain evaluation systems
* Production AI pipelines

---

## ⚠️ Limitations

* LLM evaluator may have bias (e.g., prefers structured answers)
* Scores are heuristic, not absolute
* Same model used with different prompts (can be extended)

---

## 🔮 Future Improvements

* Add more LLM providers (OpenAI, Claude, Gemini)
* Improve scoring with task-specific metrics
* Add human feedback loop
* Store historical evaluations
* Deploy as a SaaS tool

---

## 🙌 Author

**Usha Rani**
B.Tech Software Engineering (2026)

---

## ⭐ Final Note

This project demonstrates:

* Multi-agent AI systems
* Prompt engineering
* LLM evaluation design
* User-focused thinking

---
