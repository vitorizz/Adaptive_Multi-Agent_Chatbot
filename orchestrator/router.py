from agents.general_agent import GeneralAgent
from agents.admissions_agent import AdmissionsAgent
from agents.ai_agent import AIAgent
from memory.vector_memory import VectorMemory
# from memory.context_manager import ContextManager

# context_manager = ContextManager()
memory = VectorMemory()

def route_query(query: str) -> str:
    """
    For now just going to route the query to the appropriate agent based on a simple keyword matching. 
    """

    lower = query.strip().lower()
    context = "" if lower in ["hello", "hi", "hey"] else memory.get_context(query)

    if any(keyword in query.lower() for keyword in ["admission", "apply", "program", "Concordia"]):
        agent = AdmissionsAgent()
    elif any(keyword in query.lower() for keyword in ["AI", "artificial intelligence", "neural network", "deep learning"]):
        agent = AIAgent()
    else:
        agent = GeneralAgent()

    response = agent.generate_response(query, context)
    memory.add_interaction(query, response)

    return response