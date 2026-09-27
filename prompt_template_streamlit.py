from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

template = PromptTemplate(
    template="Write {num} lines on {topic}",
    input_variables=["num", "topic"]
)

num_lines = st.selectbox(
    "How many lines do you want?",
    (5, 10, 15, 20)
)

topic = st.selectbox(
    "Write content on",
    ("Cat", "Dog", "Elephant", "Donkey")
)

if st.button("Submit"):
    user_input = template.invoke({
        "num": num_lines,
        "topic": topic
    })

    result = model.invoke(user_input)
    st.write(result.content)
