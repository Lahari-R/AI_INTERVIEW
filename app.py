import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Placement Practice",layout = "centered")
st.title("AI_INTERVIEW_ASSISTANT")
st.caption("practice and prepare for interview")
try:
  client = Groq(api_key = ["Groq_API_KEY"])
  except(Keyerror,FileNotFound):
    st.error("API Key is missimg.Add it in Advanced settings")
    st.stop()
