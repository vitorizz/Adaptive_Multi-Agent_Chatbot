from typing import Optional
from .base_agent import BaseAgent
from llm.ollama_client import query_ollama

class AIAgent(BaseAgent):
    def generate_response(self, query: str, context: Optional[str] = None) -> str:
        if context:
            prompt = f"{context}\nExplain the following AI concept or query clearly:\n{query}"
        else:
            prompt = f"Explain the following AI concept or query clearly:\n{query}"
        return query_ollama("ai_model", prompt)