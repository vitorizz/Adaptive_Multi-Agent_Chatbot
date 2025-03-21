from typing import Optional
from .base_agent import BaseAgent
from llm.ollama_client import query_ollama

class AdmissionsAgent(BaseAgent):
    def generate_response(self, query: str, context: Optional[str] = None) -> str:
        # Prepend conversation history if available
        if context:
            prompt = f"{context}\nProvide detailed information about Concordia University's Computer Science admissions for:\n{query}"
        else:
            prompt = f"Provide detailed information about Concordia University's Computer Science admissions for:\n{query}"

        return query_ollama("admissions_model", prompt)
