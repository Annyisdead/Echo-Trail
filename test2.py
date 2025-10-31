import streamlit as st

# Page config
st.set_page_config(
    page_title="Career Quiz 🌸",
    page_icon="🦄",
    layout="centered",
)

# Baby pink background, black text everywhere except dropdowns
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6f0;
        color: black !important;
    }

    h1, h2, h3, h4, h5, h6, label, div, span {
        color: black !important;
    }

    .stButton>button {
        background-color: #ff99cc;
        color: white;
        font-weight: bold;
    }

    /* Dropdown styling */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
    }

    div[data-baseweb="select"] div[role="listbox"] {
        background-color: white !important;
        color: black !important;
    }

    div[data-baseweb="select"] div[role="option"] {
        background-color: white !important;
        color: black !important;
    }

    div[data-baseweb="select"] div[role="option"]:hover {
        background-color: #ffb6d9 !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Career Quiz 🐰🎀")
st.write("Find out which career path matches your personality and interests!")

# Questions
q1 = st.radio("🌸 Importance of income?", [1,2,3,4,5], index=2)
q2 = st.radio("🦄 Work preference?", ["Alone","One partner","Small group","Big group"])
q3 = st.radio("⚡ Risk attitude?", ["Avoid","If needed","Calculated risks"])
q4 = st.radio("🧟 Zombie role?", ["Fix shelter","Strategize","Heal/Research","Lead","Explore"])
q5 = st.radio("💀 Career nightmare?", ["Desk work","Pure theory","Managing people","No creativity","Constant travel"])
q6 = st.radio("🔧 Free weekend vibe?", ["Build","Plan/Sketch","Both"])
q7 = st.radio("👯 Group role?", ["Quiet worker","Presenter","Coordinator/Leader","Slacker"])
q8 = st.radio("📅 Task style?", ["Finish first","Loose routine","Random"])
q9 = st.radio("🏖️ Schedule?", ["Structured","Flexible","Intense grind"])
q10 = st.radio("⏳ Time investment?", ["Minimal","Moderate","Total dedication"])
q11 = st.radio("🌱 Adaptability?", ["Resist","Slowly accept","Excited"])
q12 = st.multiselect("📚 Favorite subjects?", ["Math","Physics","Chemistry","Biology","Computer Science","English","History","Art","Music"])
q13 = st.multiselect("🏆 Best subjects?", ["Math","Physics","Chemistry","Biology","Computer Science","English","History","Art","Music"])

# Scoring
score = 0

# Tech inclination
if q2 == "Alone": score += 1
if q3 == "Calculated risks": score += 2
if q6 == "Build": score += 2
if "Computer Science" in q12 or "Math" in q12: score += 2
if "Computer Science" in q13 or "Math" in q13: score += 2

# Creative inclination
creative_subjects = {"Art","Music","English","History"}
if any(s in creative_subjects for s in q12): score += 2
if any(s in creative_subjects for s in q13): score += 2
if q6 == "Plan/Sketch": score += 2

# Leadership
if q7 == "Coordinator/Leader": score += 2
if q4 == "Lead": score += 2

# Map score to career
if score >= 10:
    career = "🧠 Software Engineer / Tech Innovator"
elif score >= 6:
    career = "🎨 Creative Field (Design, Writing, Media)"
else:
    career = "🤝 Business & Management / PR / Strategy"

# Submit button
if st.button("Submit Quiz 🌟"):
    st.balloons()
    st.success(f"✨ Your Ideal Career Path: **{career}** ✨")

