import streamlit as st
from transformers import Conversation, pipeline

conversation_pipeline = pipeline("conversational")

# Initialize the conversation pipeline
pipe = conversation_pipeline("microsoft/DialoGPT-medium")

def generate_activity_plan(days):
    if days == 1:
        messages = [
            {"role": "user", "content": "I want to spend 1 day in Shaki, Azerbaijan."},
            {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
        ]
    elif days == 3:
        messages = [
            {"role": "user", "content": "I want to spend 3 days in Shaki, Azerbaijan."},
            {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
        ]
    elif days == 7:
        messages = [
            {"role": "user", "content": "I want to spend a week in Shaki, Azerbaijan."},
            {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
        ]
    else:
        return "Sorry, I can only generate activity plans for 1, 3, or 7 days."

    # Generate conversation
    conv = Conversation(messages=messages)
    conv = pipe(conv)

    # Extract the response
    response = conv.generated_responses[-1]["generated_text"]
    return response

# Define the application title and layout
st.title("Shaki Activity Planner")
st.write("This application helps you plan your activities in Shaki, Azerbaijan.")

# Create a form to collect user input
with st.form("user_input"):
    # Get the number of days the user wants to spend in Shaki
    days = st.selectbox("How many days do you want to spend in Shaki?", [1, 3, 7])

    # Submit button
    submitted = st.form_submit_button("Generate Activity Plan")

# Generate the activity plan based on user input
if submitted:
    activity_plan = generate_activity_plan(days)
    st.write(activity_plan)
