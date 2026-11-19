
import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="AI Assistant Interview",
    layout="centered"
)

st.title("AI Interview Assistant")
st.caption("Launched By Lahari R")

# Groq API connection
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

except (KeyError, FileNotFoundError):
    st.error("API Key is missing. Add it in Streamlit secrets.")
    st.stop()

# Job role selection
role = st.selectbox(
    "Job Title",
    [
        "Machine Learning Engineer",
        "Senior Software Engineer",
        "DevOps Engineer",
        "Data Analyst",
        "Other"
    ]
)

if role == "Other":
    custom_role = st.text_input("Enter your Job Title")

    if custom_role.strip():
        role = custom_role

# Model selection
gen_model = st.selectbox(
    "Model",
    ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
)

# Difficulty selection
level = st.selectbox(
    "Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

# Activity selection
mode = st.radio(
    "Activity",
    [
        "Generate Questions",
        "Generate Code Questions",
        "Evaluate Answers",
        "Improve Answers"
    ]
)

# Input based on selected activity
if mode == "Generate Questions":

    count = st.slider(
        "Number of Questions", 1, 10, 5
    )

elif mode == "Generate Code Questions":

    topic = st.selectbox(
        "Topics",
        ["SQL", "AIML", "Python", "DSA", "Java", "C/C++"]
    )

    count = st.slider(
        "Number of Questions", 1, 10, 5
    )

else:

    questions = st.text_area(
        "Enter Interview Questions here"
    )

    answer = st.text_area(
        "Enter your answer",
        height=160
    )

# Generate AI response
if st.button("Generate AI Response", type="primary"):

    # Validate inputs
    if mode in ["Evaluate Answers", "Improve Answers"]:

        if not questions.strip() or not answer.strip():
            st.warning("Please enter a valid Question and Answer.")
            st.stop()

    # Create task based on activity
    if mode == "Generate Questions":

        task = (
            f"Generate {count} frequently asked interview questions "
            f"for the job role {role}. Include 3 theoretical and "
            "2 scenario-based questions where possible. "
            "Do not give answers. Give hints."
        )

    elif mode == "Generate Code Questions":

        task = (
            f"Generate {count} frequently asked coding questions "
            f"on the topic {topic} for the job role {role}. "
            "Give hints to solve them. Be accurate."
        )

    elif mode == "Evaluate Answers":

        task = (
            f"Question: {questions}\n"
            f"My Answer: {answer}\n"
            "Evaluate this answer based on concept, relevance, "
            "communication, and length of answer. "
            "Give each rating out of 5 in a list. "
            "Also provide suggestions for improvement."
        )

    elif mode == "Improve Answers":

        task = (
            f"Question: {questions}\n"
            f"My Answer: {answer}\n"
            "Improve the answer based on choice of words, "
            "technical accuracy, and conceptual clarity. "
            "Provide the improved answer."
        )

    # Background information
    background = (
        f"Job role: {role}\n"
        f"Difficulty level: {level}\n"
    )

    # Groq API call
    with st.spinner("Generating your answer..."):

        try:

            response = client.chat.completions.create(

                model=gen_model,

                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Act as a Senior Interview expert "
                            "for both HR and Technical interviews."
                        )
                    },
                    {
                        "role": "user",
                        "content": background + task
                    }
                ],

                temperature=0.7,
                max_tokens=1800
            )

            # Display AI response
            output = response.choices[0].message.content

            st.subheader("AI Response")
            st.markdown(output)

            # Download response
            st.download_button(
                "Download Response",
                output,
                file_name="Interview_Response.txt",
                mime="text/plain"
            )

        except Exception as e:

            st.error("API connection was unsuccessful.")
            st.error(f"Error details: {e}")

# Footer
st.caption(
    "Powered by Streamlit and GitHub. Using Groq LLM API."
)
