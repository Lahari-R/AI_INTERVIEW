import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Placement Practice",
    layout="centered"
)

st.title("AI Placement Assistant")
st.caption("Practice and prepare for interview")

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

except (KeyError, FileNotFoundError):
    st.error("API Key is missing. Add it in Advanced Settings.")
    st.stop()

role = st.selectbox(
    "Job Title",
    [
        "Machine Learning Engineer",
        "Prompt Engineer",
        "Senior Software Engineer",
        "Artificial Intelligence Engineer",
        "Other"
    ]
)
