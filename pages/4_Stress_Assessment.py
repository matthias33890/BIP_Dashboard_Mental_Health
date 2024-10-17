import streamlit as st

st.set_page_config(page_title="Stress Assessment", layout="wide")

st.title("Stress Assessment (PSS)")
st.write("This test is based on the Perceived Stress Scale (PSS).")

# PSS Questions
pss_questions = [
    "How often have you felt that you were experiencing unexpected events in the last month?",
    "How often have you felt that you could not control the important things in your life in the last month?",
    "How often have you felt nervous and stressed in the last month?",
    "How often have you felt confident about your ability to handle your personal problems in the last month?",
    "How often have you felt that things were going well for you in the last month?",
    "How often have you felt that you were on top of things in the last month?",
    "How often have you been upset because of things that were outside of your control in the last month?",
    "How often have you felt that difficulties were piling up so high that you could not overcome them in the last month?"
]

pss_responses = []

options = ["Never", "Almost never", "Sometimes", "Fairly often", "Very often"]
scores = {"Never": 0, "Almost never": 1, "Sometimes": 2, "Fairly often": 3, "Very often": 4}

for i, question in enumerate(pss_questions):
    response = st.radio(f"{i+1}. {question}", options, key=f"pss_{i}")
    pss_responses.append(scores[response])

# Calculate total score
total_score = sum(pss_responses)

# Interpretation of the score
if st.button("Show Results"):
    st.subheader("Your Stress Assessment Result")
    st.write(f"Your total score is: **{total_score}** out of 32.")

    # General interpretation
    if total_score <= 13:
        level = "Low stress level"
    elif 14 <= total_score <= 26:
        level = "Moderate stress level"
    else:
        level = "High stress level"

    st.write(f"This suggests a **{level}**.")

    # General tips and encouragement to seek professional help
    st.write("It might be helpful to develop stress management strategies or seek professional support.")
    st.info("**Note:** This test is a screening tool and not a diagnosis. For a full evaluation, please consult a qualified professional.")

# Support services in the sidebar
st.sidebar.header("Support Services")
st.sidebar.write("""
- **Telephone Counseling Germany**
  - Phone: 0800 111 0 111 or 0800 111 0 222
  - Website: [telefonseelsorge.de](https://www.telefonseelsorge.de)

- **Federal Center for Health Education (BZgA)**
  - Website: [bzga.de](https://www.bzga.de)

- **Number Against Sorrow (for children and adolescents)**
  - Phone: 116111
  - Website: [nummergegenkummer.de](https://www.nummergegenkummer.de)

- **Helpline "Violence Against Women"**
  - Phone: 08000 116 016
  - Website: [hilfetelefon.de](https://www.hilfetelefon.de)
""")
