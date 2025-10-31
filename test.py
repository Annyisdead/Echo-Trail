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
    /* Overall app background */
    .stApp {
        background-color: #ffe6f0;
        color: black !important;
    }

    /* Headings, labels, general text */
    h1, h2, h3, h4, h5, h6, label, div, span {
        color: black !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #ff99cc;
        color: white;
        font-weight: bold;
    }

    /* Dropdowns (multiselect) styling */
    div.stMultiSelect > div[role="combobox"] > div[role="listbox"] {
        background-color: white !important;
        color: black !important;
    }
    div.stMultiSelect > div[role="combobox"] > div[role="textbox"] > input {
        background-color: white !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Career Quiz 🐰🎀")
st.write("Find out which career path matches your personality and interests!")

# --- Questions ---
q1 = st.radio(
    "🌸 On a scale of 1–5, how important is income or financial stability in your career decisions?",
    options=[1, 2, 3, 4, 5],
    index=2
)

q2 = st.radio(
    "🦄 Work preference: In a project, do you prefer to work…",
    options=[
        "Alone ",
        "With one trusted partner ",
        "Small group (3-4 people) ",
        "Big group (5+ people) "
    ]
)

q3 = st.radio(
    "⚡ How do you feel about taking risks?",
    options=[
        "Avoid it, prefer safe options ",
        "Take it if necessary ",
        "Excited to take calculated risks "
    ]
)

q4 = st.radio(
    "🧟 The world is overrun by zombies. Which role would you naturally take?",
    options=[
        "Fortify shelter, repair tools ",
        "Strategize escape and manage supplies ",
        "Tend to injured or research solutions ",
        "Lead the group and assign roles ",
        "Explore surroundings and communicate "
    ]
)

q5 = st.radio(
    "💀 Imagine your career lasts decades. Which would you absolutely NOT want to do?",
    options=[
        "Sit behind a desk all day ",
        "Work purely with abstract theory ",
        "Lead/manage people constantly ",
        "Follow rigid rules, no creativity ",
        "Travel constantly or be away from home "
    ]
)

q6 = st.radio(
    "🔧 It's the weekend and you're free. Which activity makes you most energized?",
    options=[
        "Build or tinker with a project ",
        "Plan, design, or sketch ideas ",
        "Do a mix of both "
    ]
)

q7 = st.radio(
    "👯 In a group project, are you the one who…",
    options=[
        "Does the work quietly ",
        "Presents it ",
        "Guides the group or helps coordinate ",
        "Just slacks "
    ]
)

q8 = st.radio(
    "📅 How do you usually manage tasks?",
    options=[
        "Finish all work before resting ",
        "Follow a loose daily schedule ",
        "Do things randomly as they come "
    ]
)

q9 = st.radio(
    "🏖️ Ideal career schedule?",
    options=[
        "Strict schedule, lots of free time ",
        "Flexible hours, occasional long days ",
        "Intense workload, fully invested "
    ]
)

q10 = st.radio(
    "⏳ How much time are you willing to invest in mastering a passion project?",
    options=[
        "Minimal effort ",
        "Moderate effort ",
        "Total immersion "
    ]
)

q11 = st.radio(
    "🌱 A sudden change forces you to switch to a completely new task. You…",
    options=[
        "Resist change ",
        "Accept it reluctantly ",
        "Dive in excitedly and experiment "
    ]
)

q12 = st.multiselect(
    "📚 Which subjects do you love the most?",
    options=["Math", "Physics", "Chemistry", "Biology", "Computer Science", "English", "History", "Art", "Music"]
)

q13 = st.multiselect(
    "🏆 Which subjects are you best at?",
    options=["Math", "Physics", "Chemistry", "Biology", "Computer Science", "English", "History", "Art", "Music"]
)

# Submit button
if st.button("Submit Quiz 🌟"):
    st.balloons()
    st.success("Thank you for completing the quiz! 🎉💖")
    st.write("Your answers:")
    st.write(f"Income importance: {q1}")
    st.write(f"Work preference: {q2}")
    st.write(f"Risk attitude: {q3}")
    st.write(f"Zombie role: {q4}")
    st.write(f"Things you hate: {q5}")
    st.write(f"Hands-on vs analytical: {q6}")
    st.write(f"Group project style: {q7}")
    st.write(f"Work style: {q8}")
    st.write(f"Work-life balance: {q9}")
    st.write(f"Time commitment: {q10}")
    st.write(f"Adaptability: {q11}")
    st.write(f"Subjects you love: {q12}")
    st.write(f"Subjects you’re best at: {q13}")
