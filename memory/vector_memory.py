from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore

class VectorMemory:
    def __init__(self, embedding_model_name="sentence-transformers/all-MiniLM-L6-v2"):
        # Initialize the embedding model.
        self.embedder = HuggingFaceEmbeddings(model_name=embedding_model_name)
        
        # Create a dummy embedding to determine the dimensionality.
        dummy_embedding = self.embedder.embed_query("dummy")
        d = len(dummy_embedding)
        
        # Create an empty FAISS index with the proper dimensionality.
        index = faiss.IndexFlatL2(d)
        
        # Use an InMemoryDocstore instead of an empty dictionary.
        self.store = FAISS(
            embedding_function=self.embedder,
            index=index,
            docstore=InMemoryDocstore({}),
            index_to_docstore_id={}
        )


    def add_interaction(self, query: str, response: str):
        text = f"User: {query}\nBot: {response}"
        doc = Document(page_content=text)
        self.store.add_documents([doc])

    def get_context(self, query: str, k: int = 5) -> str:
        docs = self.store.similarity_search(query, k=k)
        return "\n".join(doc.page_content for doc in docs)