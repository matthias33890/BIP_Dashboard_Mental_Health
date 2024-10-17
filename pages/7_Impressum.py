import streamlit as st

st.set_page_config(page_title="Legal Notice", layout="wide")

st.title("Legal Notice")

st.write("""
**Your Name**

Your Address

Your Email Address

Your Phone Number

Responsible for content according to § 55 Abs. 2 RStV: Your Name

**Disclaimer:** This is a sample legal notice. Please consult a lawyer to ensure compliance with all relevant laws and regulations.
""")

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
