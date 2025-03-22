from .base_agent import BaseAgent
from llm.ollama_client import query_ollama
from typing import Optional
from external.wikipedia_api import search_wikipedia

class GeneralAgent(BaseAgent):
    def generate_response(self, query: str, context: Optional[str] = None) -> str:
        wiki_text = search_wikipedia(query)
        base = f"Please answer the following question concisely:\n{query}"
        extras = []

        if context:
            print("context:" + context) # Debugging
            extras.append(context)
        if wiki_text:
            print("wiki text:" + wiki_text) # Debugging
            extras.append(f"You can refer to this info:\n{wiki_text}")
        prompt = "\n".join([base] + extras)

        return query_ollama("general_model", prompt)