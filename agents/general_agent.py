from .base_agent import BaseAgent
from llm.ollama_client import query_ollama
from typing import Optional
from external.wikipedia_api import search_wikipedia

class GeneralAgent(BaseAgent):
    def is_salutation(self, query: str) -> bool:
        salutations = {
            "hello", "hi", "hey", "greetings", 
            "goodbye", "bye", "good morning", 
            "good afternoon", "good evening"
        }
        return query.strip().lower() in salutations

    def generate_response(self, query: str, context: Optional[str] = None) -> str:
        # Check if the query is a salutation
        if self.is_salutation(query):
            prompt = (f"User salutation: '{query}'. Respond with an appropriate, friendly greeting or farewell "
                      "without additional explanation.")
            return query_ollama("general_model", prompt)
        
        wiki_text = search_wikipedia(query)
        prompt_lines = [
            "You are an expert answering questions. The background information provided below is solely for context and must not be included in your final answer."
        ]
        if context:
            print(f"Previously, we discussed:\n{context}")  # Debugging
            prompt_lines.append(f"Context:\n{context}")
        if wiki_text:
            print("wiki text:" + wiki_text)  # Debugging
            prompt_lines.append(f"Wikipedia Background:\n{wiki_text}")
        
        prompt_lines.append(f"Query:\n{query}")
        prompt = "\n\n".join(prompt_lines)

        return query_ollama("general_model", prompt)
