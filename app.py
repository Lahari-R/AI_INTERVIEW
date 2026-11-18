
import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="AI_Interview_Assistant",
    page_icon="🎃",
    layout="centered"
)

# Application title
st.title("AI Interview Assistant")
st.caption("Practice and prepare for your placement here!")

# API Key configuration
try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)

except KeyError:
    st.error("API Key is missing. Add it to your Streamlit secrets.")
    st.stop()

# Job role selection
role = st.selectbox(
    "Job Title",
    [
        "Machine Learning Engineer",
        "Senior Software Engineer",
        "DevOps Engineer",
        "Data Analyst",
        "Prompt Engineer",
        "Other"
    ]
)

# Custom job title
if role == "Other":
    role = st.text_input("Enter your Job Title", placeholder="Enter your job title")

# Display selected role
if role:
    st.success(f"Selected Job Role: {role}")
