from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
project_id = os.getenv("OPENAI_PROJECT")


# Initialize model
model = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini",
    organization=project_id
)


# Define prompt template
prompt = PromptTemplate(
    template="Answer the following question:\n{question}\n"
             "from the following text:\n{text}",
    input_variables=["question", "text"]
)

parser = StrOutputParser()


# Load webpage
url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421"

loader = WebBaseLoader(url)
docs = loader.load()


# Build chain
chain = prompt | model | parser


# Run chain
result = chain.invoke({
    "question": "What is the product we are talking about?",
    "text": docs[0].page_content
})

print(result)

