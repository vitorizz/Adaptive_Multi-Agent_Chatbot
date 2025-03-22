import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent="Adaptive_Multi-Agent_Chatbot/1.0 (https://github.com/vitorizz)",
    language="en"
)

def search_wikipedia(query: str) -> str:
    page = wiki.page(query)
    if page.exists():
        # Return the first 2–3 sentences for brevity
        return " ".join(page.summary.split(". ")[:2]) + "."
    return None