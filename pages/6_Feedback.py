import streamlit as st

st.set_page_config(page_title="Feedback", layout="wide")

st.title("Feedback to Improve the Website")

st.write("We appreciate your feedback and want to continuously improve our app. Please share your thoughts, suggestions, or issues with us.")

# Feedback form
name = st.text_input("Name (optional)")
email = st.text_input("Email address (optional)")
feedback = st.text_area("Your feedback")

if st.button("Submit Feedback"):
    if feedback:
        # Here you can add the code to save the feedback or send it via email
        st.success("Thank you for your feedback!")
    else:
        st.error("Please enter your feedback before submitting.")

import streamlit as st

# (Your previous code)

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
