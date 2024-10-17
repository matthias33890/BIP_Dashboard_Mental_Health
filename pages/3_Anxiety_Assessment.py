import streamlit as st

st.set_page_config(page_title="Anxiety Assessment", layout="wide")

st.title("Anxiety Assessment (GAD-7)")
st.write("This test is based on the GAD-7 questionnaire.")

# GAD-7 Questions
gad7_questions = [
    "Feeling nervous, anxious, or on edge?",
    "Not being able to stop or control worrying?",
    "Worrying too much about different things?",
    "Trouble relaxing?",
    "Being so restless that it's hard to sit still?",
    "Becoming easily annoyed or irritable?",
    "Feeling afraid as if something awful might happen?"
]

gad7_responses = []

options = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
scores = {"Not at all": 0, "Several days": 1, "More than half the days": 2, "Nearly every day": 3}

for i, question in enumerate(gad7_questions):
    response = st.radio(f"{i+1}. {question}", options, key=f"gad7_{i}")
    gad7_responses.append(scores[response])

# Calculate total score
total_score = sum(gad7_responses)

# Interpretation of the score
if st.button("Show Results"):
    st.subheader("Your Anxiety Assessment Result")
    st.write(f"Your total score is: **{total_score}** out of 21.")

    # General interpretation
    if total_score <= 4:
        level = "Minimal or no anxiety"
    elif 5 <= total_score <= 9:
        level = "Mild anxiety"
    elif 10 <= total_score <= 14:
        level = "Moderate anxiety"
    else:
        level = "Severe anxiety"

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
