import streamlit as st
from openai import OpenAI
import pandas as pd
import PyPDF2
import os

def get_openai_api_key():
    # First, try to import from config.py
    try:
        from pages.config import OPENAI_API_KEY
        return OPENAI_API_KEY
    except ImportError:
        pass

    # Finally, try to get from environment variables
    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key:
        return api_key

    # If all methods fail, show an error
    st.error("OpenAI API key not found. Please set the 'OPENAI_API_KEY' in 'config.py', Streamlit secrets, or as an environment variable.")
    return None

# Get the API key
openai_api_key = get_openai_api_key()
if openai_api_key is None:
    st.stop()


# Initialize OpenAI client with API key
client = OpenAI(api_key=openai_api_key)  # Replace with your actual API key

st.set_page_config(page_title="General Questionnaire", layout="wide")

st.title("General Mental Health Questionnaire")

# Privacy notice for file upload
st.warning("**Note:** Please ensure that you have removed all personal data before uploading a file. By uploading, you agree that the content will be processed by the app.")

# File upload for patient history
uploaded_file = st.file_uploader("Optional: Upload your patient history (only .txt, .csv, and .pdf files)", type=["txt", "csv", "pdf"])

file_content = None
if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        # Handle text file
        file_content = uploaded_file.read().decode('utf-8')
        st.success("Text file uploaded successfully!")
    elif uploaded_file.type == "application/pdf":
        # Handle PDF file
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            file_content = ""
            for page in pdf_reader.pages:
                file_content += page.extract_text()
            st.success("PDF file uploaded successfully!")
        except Exception as e:
            st.error("Error reading PDF file.")
            file_content = None
    elif uploaded_file.type == "text/csv":
        # Handle CSV file
        try:
            df = pd.read_csv(uploaded_file)
            file_content = df.to_string()
            st.success("CSV file uploaded successfully!")
        except Exception as e:
            st.error("Error reading CSV file.")
            file_content = None
    else:
        st.error("Unsupported file type.")
        file_content = None

# 1. Personal Information
st.header("Personal Information")
age = st.number_input("Age", min_value=1, max_value=120, value=25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=0)
occupation = st.text_input("Occupation/Field of Study", value="Student")

# 2. Symptoms and Feelings
st.header("Symptoms and Feelings")
mood = st.multiselect(
    "Which of these moods do you frequently experience?",
    ["Sadness", "Feeling down", "Mood swings", "Irritability"],
    default=["Feeling down", "Irritability"]
)
anxiety = st.multiselect(
    "Do you experience anxiety or worries?",
    ["Often anxious", "Panic attacks", "Excessive worries"],
    default=["Often anxious"]
)
sleep = st.selectbox(
    "How would you describe your sleep patterns?",
    ["Difficulty falling asleep", "Trouble staying asleep", "Sleeping too much", "Sleeping too little", "Normal"],
    index=4
)
energy = st.selectbox(
    "How is your energy level?",
    ["Often tired", "Lacking energy", "Normal", "Energetic"],
    index=2
)
appetite = st.selectbox(
    "Have you noticed changes in appetite?",
    ["Increase", "Decrease", "No change"],
    index=2
)
concentration = st.selectbox(
    "Do you have difficulties with concentration?",
    ["Yes", "No"],
    index=1
)
thoughts = st.multiselect(
    "Do you experience any of the following thought patterns?",
    ["Racing thoughts", "None of these"],
    default=["None of these"]
)
behavior_changes = st.multiselect(
    "Have you noticed changes in your behavior?",
    ["Social withdrawal", "Changed behavior", "No changes"],
    default=["No changes"]
)

# 3. Duration and Frequency
st.header("Duration and Frequency")
symptom_duration = st.text_input("Since when have you been experiencing these symptoms?", value="A few weeks")
symptom_frequency = st.selectbox(
    "How often do these symptoms occur?",
    ["Daily", "Several times a week", "Weekly", "Monthly", "Rarely"],
    index=1
)

# 4. Stress Factors and Life Events
st.header("Stress Factors and Life Events")
life_changes = st.text_area("Have you recently experienced significant changes in your life?", value="Started a new job")
stress_levels = st.select_slider(
    "What is your current stress level?",
    options=["Low", "Medium", "High", "Very high"],
    value="Medium"
)

# 5. Medical History
st.header("Medical History")
medical_conditions = st.text_area("Do you have any diagnosed medical conditions?", value="None")
medications = st.text_area("Are you currently taking any medications?", value="None")
family_history = st.selectbox(
    "Is there a family history of mental illness?",
    ["Yes", "No", "Don't know"],
    index=1
)

# 6. Lifestyle and Habits
st.header("Lifestyle and Habits")
exercise = st.selectbox(
    "Do you exercise regularly?",
    ["Yes", "No"],
    index=0
)
substance_use = st.multiselect(
    "Do you consume alcohol or drugs?",
    ["Alcohol", "Drugs", "Neither"],
    default=["Neither"]
)
diet = st.selectbox(
    "How would you rate your diet?",
    ["Healthy", "Balanced", "Unhealthy"],
    index=1
)
social_support = st.selectbox(
    "Do you have a supportive social network?",
    ["Yes", "No"],
    index=0
)

# 7. Coping Strategies
st.header("Coping Strategies")
coping_strategies = st.text_area("How do you usually cope with stress or difficult emotions?", value="Talking to friends")
relaxation_techniques = st.selectbox(
    "Do you practice relaxation techniques or mindfulness?",
    ["Yes", "No"],
    index=0
)

# 8. Goals and Expectations
st.header("Goals and Expectations")
goals = st.text_area("What do you hope to achieve or improve?", value="Reduce stress levels")

# Submit Button
if st.button("Get Tips"):
    # Summarize user input
    user_input = f"""
    Age: {age}
    Gender: {gender}
    Occupation/Field of Study: {occupation}
    Mood: {', '.join(mood)}
    Anxiety and Worries: {', '.join(anxiety)}
    Sleep Patterns: {sleep}
    Energy Level: {energy}
    Appetite Changes: {appetite}
    Concentration Difficulties: {concentration}
    Thought Patterns: {', '.join(thoughts)}
    Behavioral Changes: {', '.join(behavior_changes)}
    Symptom Duration: {symptom_duration}
    Symptom Frequency: {symptom_frequency}
    Life Changes: {life_changes}
    Stress Level: {stress_levels}
    Medical Conditions: {medical_conditions}
    Medications: {medications}
    Family History: {family_history}
    Exercise: {exercise}
    Substance Use: {', '.join(substance_use)}
    Diet: {diet}
    Social Support: {social_support}
    Coping Strategies: {coping_strategies}
    Relaxation Techniques: {relaxation_techniques}
    Goals: {goals}
    """

    # If a file was uploaded, add its content
    if file_content:
        user_input += f"\nAdditional information from the uploaded file:\n{file_content}"

    # Request to GPT-4o API
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant providing general wellness tips based on user input. Do not provide medical diagnoses or specific medical advice. Encourage seeking professional help if needed. You should Response with 3 things: 1. What mental health sickness the user might have. 2. What could be the cause of the mental health sickness. 3. What the user can do to improve their mental health. If they have depression, anxiety or stress, refer to the assessment tools in the app."},
            {"role": "user", "content": user_input}
        ]
    )

    # Extract response
    tips = completion.choices[0].message.content

    # Display results
    st.header("Your Personalized Tips")
    st.write(tips)

    # Note about professional help
    st.info("**Note:** These tips are for informational purposes only and do not replace professional medical advice. Please consult a qualified professional if you need support.")

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
