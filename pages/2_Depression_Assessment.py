import streamlit as st

st.set_page_config(page_title="Depression Assessment", layout="wide")

st.title("Depression Assessment")
st.write("This test is based on the PHQ-9 questionnaire.")

# PHQ-9 Questions
phq9_questions = [
    "Little interest or pleasure in doing things?",
    "Feeling down, depressed, or hopeless?",
    "Trouble falling or staying asleep, or sleeping too much?",
    "Feeling tired or having little energy?",
    "Poor appetite or overeating?",
    "Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
    "Trouble concentrating on things, such as reading the newspaper or watching television?",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you've been moving around a lot more than usual?",
    "Thoughts that you would be better off dead or thoughts of hurting yourself in some way?"
]

phq9_responses = []

options = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
scores = {"Not at all": 0, "Several days": 1, "More than half the days": 2, "Nearly every day": 3}

for i, question in enumerate(phq9_questions):
    response = st.radio(f"{i+1}. {question}", options, key=f"phq9_{i}")
    phq9_responses.append(scores[response])

# Calculate total score
total_score = sum(phq9_responses)

# Interpretation of the score
if st.button("Show Results"):
    st.subheader("Your Depression Assessment Result")
    st.write(f"Your total score is: **{total_score}** out of 27.")

    # General interpretation
    if total_score <= 4:
        level = "Minimal or no depression"
    elif 5 <= total_score <= 9:
        level = "Mild depression"
    elif 10 <= total_score <= 14:
        level = "Moderate depression"
    elif 15 <= total_score <= 19:
        level = "Moderately severe depression"
    else:
        level = "Severe depression"

    st.write(f"This suggests: **{level}**.")

    # General tips and encouragement to seek professional help
    st.write("Please consider consulting a mental health professional for a comprehensive evaluation and support.")
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
