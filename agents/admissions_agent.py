from typing import Optional
from .base_agent import BaseAgent
from llm.ollama_client import query_ollama

class AdmissionsAgent(BaseAgent):
    def generate_response(self, query: str, context: Optional[str] = None) -> str:
        prompt = f"Provide detailed information about Concordia University's Computer Science admissions for:\n{query}"
        return query_ollama("admissions_model", prompt)