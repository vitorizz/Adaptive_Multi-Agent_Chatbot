from typing import Optional

class BaseAgent:
    def generate_response(self, query: str, context: Optional[str] = None) -> str:
        """
        Generate a response based on the query and optional context. 
        This method should be overridden by subclasses. 
        """
        raise NotImplementedError("Subclasses must implement this method")