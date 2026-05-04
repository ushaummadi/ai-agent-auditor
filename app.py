import streamlit as st
from orchestrator import run_pipeline

st.set_page_config(page_title="AI Agent Auditor", layout="wide")

# ---- STYLE ----
st.markdown("""
<style>
.big-card {
    padding: 20px;
    border-radius: 15px;
    background-color: #0f172a;
    color: white;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
}
.center-text {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<h1 class='center-text'>🤖 AI Agent Auditor</h1>
<p class='center-text' style='font-size:18px;'>
Measure which AI agent actually performs best — not just guess
</p>
<hr>
""", unsafe_allow_html=True)

# ---- INPUT SECTION ----
st.markdown("### 🧠 What task do you want AI agents to perform?")

task = st.text_area(
    "",
    placeholder="e.g. Write a persuasive product description for a magnesium supplement"
)

# ---- QUICK EXAMPLES ----
st.markdown("#### ⚡ Try an example:")

col1, col2 = st.columns(2)

with col1:
    if st.button("📦 Product Description"):
        task = "Write a persuasive product description for a magnesium supplement"

with col2:
    if st.button("📢 LinkedIn Post"):
        task = "Write a LinkedIn post announcing a new AI product launch"

# ---- RUN BUTTON ----
run = st.button("🚀 Compare AI Agents", use_container_width=True)
st.caption("⚡ Runs multiple AI models and evaluates them automatically")
# ---- EXECUTION ----
if run and task:

    with st.spinner("Running AI agents..."):
        result = run_pipeline(task)

    gemini_out = result["outputs"]["gemini"]
    groq_out = result["outputs"]["groq"]
    scores = result["scores"]

    # ---- OUTPUTS ----
    st.success("✅ Analysis complete — here’s how each AI performed")
    st.markdown("## 🧾 Agent Outputs")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            f"<div class='big-card'><h4>✨ Gemini</h4><p>{gemini_out}</p></div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"<div class='big-card'><h4>⚡ LLaMA3 (Groq)</h4><p>{groq_out}</p></div>",
            unsafe_allow_html=True
        )

    # ---- SCORES ----
    st.markdown("## 📊 Performance Comparison")

    c1, c2 = st.columns(2)
    g1 = scores.get("gemini", 5)
    g2 = scores.get("groq", 5)
    c1.metric("🧠 Analytical Agent Score", scores["gemini"])
    c2.metric("🎨 Creative Agent Score", scores["groq"])

    # ---- WINNER ----
    # ---- WINNER ----
    st.markdown("## 🏆 Best Agent")

    winner = scores.get("winner", "")
    winner = winner.lower().strip()

# fallback logic if winner is missing or invalid
    if winner not in ["gemini", "groq"]:
        if scores["gemini"] > scores["groq"]:
            winner = "gemini"
        elif scores["groq"] > scores["gemini"]:
            winner = "groq"

    if winner == "gemini":
        st.success("✨ Gemini performs best for this task")
    elif winner == "groq":
        st.success("⚡ LLaMA3 performs best for this task")
    else:
        st.warning("⚠️ Could not determine a clear winner")
    st.info(scores["reason"])

    # ---- PERFORMANCE BAR ----
    st.markdown("### 🔥 Performance Score")

    try:
        g1 = float(scores.get("gemini", 0))
        g2 = float(scores.get("groq", 0))

        best_score = max(g1, g2) / 10

    # clamp value between 0 and 1
        best_score = max(0.0, min(1.0, best_score))

    except:
        best_score = 0.5  # fallback safe value

    st.progress(best_score)

    # ---- RAW OUTPUT (PRO FEATURE) ----
    with st.expander("📄 View Raw Outputs"):
        st.subheader("Gemini")
        st.write(gemini_out)

        st.subheader("LLaMA3 (Groq)")
        st.write(groq_out)

# ---- FOOTER ----
st.markdown("""
<hr>
<p class='center-text'>
AI Agent Evaluation System • Built for comparing and managing AI agents
</p>
""", unsafe_allow_html=True)
