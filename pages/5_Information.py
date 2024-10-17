import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Information", layout="wide")

st.title("Information on Current Mental Health Trends")

# Display statistics with Plotly graphs
st.subheader("Global Mental Health Statistics")

# Example data for statistics
data = {
    'Condition': ['Depression', 'Anxiety Disorders', 'Bipolar Disorder', 'Schizophrenia'],
    'People Affected (Millions)': [264, 284, 45, 20]
}
df = pd.DataFrame(data)

# Bar chart with Plotly
fig = px.bar(df, x='Condition', y='People Affected (Millions)', title='Global Mental Health Statistics')
st.plotly_chart(fig)

# Additional statistics and graphs
st.subheader("Impact of the COVID-19 Pandemic")
covid_data = {
    'Year': [2019, 2020, 2021],
    'Increase in Anxiety (%)': [0, 25, 30],
    'Increase in Depression (%)': [0, 20, 28]
}
covid_df = pd.DataFrame(covid_data)
fig2 = px.line(covid_df, x='Year', y=['Increase in Anxiety (%)', 'Increase in Depression (%)'],
               title='Rise in Mental Health Issues During COVID-19')
st.plotly_chart(fig2)

st.subheader("Importance of Seeking Help")
st.write("""
- Early intervention can significantly improve outcomes.
- Access to mental health services remains a challenge in many regions.
- Reducing the stigma around mental health is crucial to encourage people to seek help.
""")

st.subheader("Resources")
st.write("""
- [World Health Organization (WHO) Mental Health](https://www.who.int/health-topics/mental-health)
- [German Society for Psychiatry, Psychotherapy, Psychosomatics and Neurology (DGPPN)](https://www.dgppn.de)
- [Federal Center for Health Education (BZgA)](https://www.bzga.de)
""")

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
