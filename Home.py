import streamlit as st

# Page configuration
st.set_page_config(page_title="Mental Health Support App", layout="wide")

# Title of the app
st.title("Welcome to the Mental Health Support App")

st.write("""
## About This App

This app offers various questionnaires and resources to support your mental health. It does not replace professional medical advice.

Please use the navigation menu on the left to explore the different sections of the app.

**Features:**

- General mental health questionnaire
- Depression assessment (PHQ-9)
- Anxiety assessment (GAD-7)
- Stress assessment (PSS)
- Information on current mental health trends with interactive graphs
- Ability to upload your patient history and receive personalized insights
- Feedback form to improve the website
""")

import streamlit as st

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
