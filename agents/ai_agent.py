from typing import Optional
from .base_agent import BaseAgent
from llm.ollama_client import query_ollama
from external.wikipedia_api import search_wikipedia

class AIAgent(BaseAgent):
    def generate_response(self, query: str, context: Optional[str] = None) -> str:
        wiki_text = search_wikipedia(query)
        prompt_lines = [
            "You are an AI assistant. The following background information is provided solely for context. Use it to better understand the query but do not include it in your final answer."
        ]

        if context:
            print("context:" + context)  # Debugging
            prompt_lines.append(f"Context:\n{context}")

        if wiki_text:
            print("wiki text:" + wiki_text)  # Debugging
            prompt_lines.append(f"Wikipedia Background:\n{wiki_text}")

        prompt_lines.append(f"Query:\n{query}")
        prompt = "\n\n".join(prompt_lines)

        return query_ollama("ai_model", prompt)