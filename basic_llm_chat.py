import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)

print("ChatGPT is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = llm.invoke(user_input)
    print("ChatGPT:", response.content)

