import streamlit as st
from pipeline.chain import run_chain
import requests
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Startup Grant Eligibility Agent",
    layout="wide"
)

# ---------------- GLOBAL STYLES ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f8fbff, #eef2ff);
    font-family: 'Segoe UI', sans-serif;
}

/* NAVBAR */
.navbar {
    padding: 25px 60px;
}

.nav-title {
    font-size: 24px;
    font-weight: 700;
    color: #2563eb;
}

/* HERO SECTION */
.hero-container {
    padding: 30px 60px 10px 60px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    color: #1f2937;
}

.hero-sub {
    font-size: 18px;
    color: #4b5563;
    margin-top: 15px;
    max-width: 600px;
}

/* Force heading visibility */
h1, h2, h3, h4, h5, h6 {
    color: #1f2937 !important;
}

p {
    color: #4b5563 !important;
}

/* Improve label visibility */
label {
    font-weight: 600 !important;
    color: #1f2937 !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #4f46e5);
    color: white;
    padding: 14px 36px;
    border-radius: 40px;
    font-weight: 600;
    font-size: 16px;
    border: none;
    margin-top: 10px;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1d4ed8, #4338ca);
}

/* Result card */
.result-card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    margin-top: 30px;
    border-left: 6px solid #2563eb;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown("""
<div class="navbar">
    <div class="nav-title">🚀 Startup Grant Eligibility Agent</div>
</div>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">
            AI-Powered Startup Grant <br> Eligibility Engine
        </div>
        <div class="hero-sub">
            Instantly check eligibility for government grants,
            identify qualification gaps, and understand documentation risks —
            with clear, AI-driven decisions.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=300
    )

# ---------------- FORM SECTION ----------------

st.markdown("""
<h2 style='margin-top:30px;'>
📋 Startup Profile Information
</h2>
<p>
Provide accurate details to receive a precise eligibility assessment.
</p>
""", unsafe_allow_html=True)

sector = st.selectbox("Industry Sector", ["AI", "FinTech", "AgriTech", "Healthcare"])
stage = st.selectbox("Startup Stage", ["Idea", "Prototype", "MVP"])
revenue = st.number_input("Annual Revenue (₹)", min_value=0.0)
dpiit = st.radio("DPIIT Recognition Status", ["Yes", "No"])
state = st.text_input("Registered State (e.g., Delhi, Karnataka)")

analyze = st.button("🔍 Analyze Eligibility")


# ---------------- OUTPUT SECTION ----------------
if analyze:

    profile = {
        "sector": sector,
        "stage": stage,
        "revenue": revenue,
        "dpiit": dpiit,
        "state": state
    }

    with st.spinner("Analyzing eligibility..."):
        result = run_chain(profile)

    # ---------- Clean Result Formatting ----------
    clean_result = result.replace("\n", "<br>")

    # ---------- Result Card ----------
    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.markdown("""
    <h3 style="color:#1f2937; font-weight:700;">
    🧠 AI Decision
    </h3>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="color:#1f2937; font-size:16px; line-height:1.7;">
    {clean_result}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Trigger n8n ONLY ONCE ----------
    try:
        response = requests.post(
            "https://dhru25.app.n8n.cloud/webhook-test/startup-alert",
            json={
                "profile": profile,
                "ai_result": result
            }
        )
        if response.status_code == 200:
            st.success("✅ Automation Triggered Successfully")
        else:
            st.warning("⚠️ Workflow triggered but response not 200")
    except Exception as e:
        st.error("❌ n8n not running")