import streamlit as st
from gemini_utility import load_gemini_pro_model

st.set_page_config(
    page_title="AI ChatBot Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI ChatBot Agent")

# Maintain session state
if "chat_session" not in st.session_state:
    st.session_state.chat_session = load_gemini_pro_model()

# Render previous chat history
for message in st.session_state.chat_session.get_history():
    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Input prompt
user_prompt = st.chat_input("Ask anything...")
if user_prompt:
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_session.send_message(user_prompt)
            st.markdown(response.text)