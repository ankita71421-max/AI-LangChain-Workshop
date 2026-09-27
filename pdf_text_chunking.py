from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Load PDF
loader = PyPDFLoader("SS1.pdf")
docs = loader.load()

# Split into chunks
splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=" "   # spelling fixed
)

result = splitter.split_documents(docs)

# Print the second chunk’s text
print(result[1].page_content)

# Print metadata (like page number)
print(result[1].metadata)

# Optional: loop through chunks
for i, doc in enumerate(result[:5]):  # first 5 chunks
    print(f"Chunk {i+1}:")
    print(doc.page_content)
    print("Metadata:", doc.metadata)
    print("-" * 40)



