from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",        # folder name
    glob="*.pdf",        # load all PDFs inside
    loader_cls=PyPDFLoader
)

docs = loader.load()     # or lazy_load()

for document in docs:
    print(document.metadata)
