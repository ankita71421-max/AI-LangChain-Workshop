import os
from dotenv import load_dotenv

load_dotenv()

print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv

load_dotenv()

print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv

load_dotenv()

print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)

st.title("ChatGPT with History")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**ChatGPT:** {msg['content']}")

# Input box
user_input = st.text_input("Enter your prompt:")

if st.button("Submit") and user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response
    response = llm.invoke(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response.content})

    # Rerun to show updated history
    st.rerun()


