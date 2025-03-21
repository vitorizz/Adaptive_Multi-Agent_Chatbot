class ContextManager: # Making a simple in memory store for now, later we will use faiss
    def __init__(self):
        self.history = []

    def add_interaction(self, query: str, response: str):
        self.history.append({"query": query, "response": response})

    def get_context(self, limit: int = 5) -> str:
        entries = self.history[-limit:]
        return "\n".join(f"User: {e['query']}\nBot: {e['response']}" for e in entries)