from .base_agent import BaseAgent
from llm.ollama_client import query_ollama
from typing import Optional

class GeneralAgent(BaseAgent):
    def generate_response(self, query: str, context: Optional[str] = None) -> str:
        if context:
            prompt = f"{context}\nPlease answer the following question in a concise manner:\n{query}"
        else:
            prompt = f"Please answer the following question in a concise manner:\n{query}"
        return query_ollama("general_model", prompt)