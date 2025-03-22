
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

class VectorMemory:
    def __init__(self, embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.embedder = HuggingFaceEmbeddings(model_name=embedding_model_name)
        self.store = FAISS.from_documents([], self.embedder)

    def add_interaction(self, query: str, response: str):
        text = f"User: {query}\nBot: {response}"
        doc = Document(page_content=text)
        self.store.add_documents([doc])

    def get_context(self, query: str, k: int = 5) -> str:
        # similarity search on last query placeholder — use entire history if no query
        results = self.store.similarity_search(query, k=k)
        return "\n".join(doc.page_content for doc in results)