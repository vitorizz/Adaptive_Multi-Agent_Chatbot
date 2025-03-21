from agents.general_agent import GeneralAgent
from agents.admissions_agent import AdmissionsAgent
from agents.ai_agent import AIAgent

def route_query(query: str) -> str:
    """
    For now just going to route the query to the appropriate agent based on a simple keyword matching. 
    """
    if any(keyword in query.lower() for keyword in ["admission", "apply", "program", "Concordia"]):
        agent = AdmissionsAgent()
    elif any(keyword in query.lower() for keyword in ["AI", "artificial intelligence", "neural network", "deep learning"]):
        agent = AIAgent()
    else:
        agent = GeneralAgent()

    #Later I'll pass along the context as well
    
    return agent.generate_response(query)
