from typing import Optional
from .base_agent import BaseAgent
from llm.ollama_client import query_ollama
from external.wikipedia_api import search_wikipedia

class AIAgent(BaseAgent):
    def generate_response(self, query: str, context: Optional[str] = None) -> str:
        wiki_text = search_wikipedia(query)
        base = f"🤖 Hey there! Here's a clear explanation of your AI question:\n\n**{query}**"
        extras = []

        if context:
            print("context:" + context)  # Debugging
            extras.append(f"Previously, we discussed:\n{context}")

        if wiki_text:
            print("wiki text:" + wiki_text)  # Debugging
            extras.append(f"Here’s some background from Wikipedia that might help:\n{wiki_text}")

        follow_up = "\n\nWould you like to learn more about a related concept?"

        prompt = "\n\n".join([base] + extras + [follow_up])

        return query_ollama("ai_model", prompt)