from langchain_community.document_loaders import PyPDFLoader

# Load the PDF
loader = PyPDFLoader("SS.pdf")
docs = loader.load()

print(len(docs))       # Number of pages loaded
print(docs[0].page_content)  # Content of the first page