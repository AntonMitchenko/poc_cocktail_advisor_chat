import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Chat Interface", layout="centered")

# Title
st.title("Chat Interface with Streamlit")

# Session State for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form for user questions
with st.form("chat_form"):
    user_input = st.text_input("Enter your question:", placeholder="Type something...")
    submit_button = st.form_submit_button("Send")

# Placeholder for chat conversation
chat_placeholder = st.container()

# Logic to process user input and append to chat history
if submit_button and user_input.strip():
    # Append user question to chat history
    st.session_state.chat_history.append({"sender": "User", "message": user_input, "timestamp": datetime.now()})

    # Generate a mock response (replace this with your model's logic)
    response = f"This is a response to: '{user_input}'"

    # Append the model's response to chat history
    st.session_state.chat_history.append({"sender": "Model", "message": response, "timestamp": datetime.now()})

# Display chat history in the chat placeholder
with chat_placeholder:
    for chat in st.session_state.chat_history:
        if chat["sender"] == "User":
            st.markdown(f"**You:** {chat['message']}")
        else:
            st.markdown(f"**Model:** {chat['message']}")
