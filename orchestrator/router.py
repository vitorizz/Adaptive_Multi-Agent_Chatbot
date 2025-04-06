from agents.general_agent import GeneralAgent
from agents.admissions_agent import AdmissionsAgent
from agents.ai_agent import AIAgent
from memory.vector_memory import VectorMemory
import requests

memory = VectorMemory()

def classify_intent(query: str) -> str:
    prompt = f"""You are an intent classification model. Determine the user's intent based on their query.

Query: "{query}"

Possible intents: [admissions, ai, general]

Respond with only one word: admissions, ai, or general.
"""

    try:
        response = requests.post("http://127.0.0.1:11434/api/generate", json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })

        data = response.json()
        if "response" in data:
            return data["response"].strip().lower()
        else:
            print(f"[IntentClassifier] Unexpected response format: {data}")
            return "general"
    except Exception as e:
        print(f"[IntentClassifier] Error calling Ollama: {e}")
        return "general"

# def classify_followup_intent(query: str) -> str:
#     prompt = f"""You are a conversational intent classifier. Given a user message, classify it into one of the following intents:

# Options: [correction, memory_check, standard_query]

# User message: "{query}"

# Intent:"""

#     try:
#         response = requests.post("http://127.0.0.1:11434/api/generate", json={
#             "model": "mistral",
#             "prompt": prompt,
#             "stream": False
#         })

#         data = response.json()
#         if "response" in data:
#             return data["response"].strip().lower()
#         else:
#             print(f"[FollowupClassifier] Unexpected response format: {data}")
#             return "standard_query"
#     except Exception as e:
#         print(f"[FollowupClassifier] Error calling Ollama: {e}")
#         return "standard_query"

def route_query(query: str) -> str:
    lower = query.strip().lower()
    context = "" if lower in ["hello", "hi", "hey"] else memory.get_context(query)

    # This part does not really work well and messes up the chatbot 

    # followup_intent = classify_followup_intent(query)

    # if followup_intent == "memory_check":
    #     return f"You last mentioned: \"{last_user_query}\""

    # if followup_intent == "correction":
    #     return "Oops! Sorry about that. Could you clarify what you meant or correct me?"

    intent = classify_intent(query)

    if intent == "admissions":
        agent = AdmissionsAgent()
    elif intent == "ai":
        agent = AIAgent()
    else:
        agent = GeneralAgent()

    full_response = agent.generate_response(query, context)

    # Try to extract just the response text
    try:
        # Convert to dict if it's an object with attributes
        if not isinstance(full_response, dict) and hasattr(full_response, "__dict__"):
            response_dict = vars(full_response)
        else:
            response_dict = full_response
            
        # Navigate through the response structure
        if isinstance(response_dict, dict) and "response" in response_dict:
            inner = response_dict["response"]
            if isinstance(inner, dict) and "response" in inner:
                response_text = inner["response"]
            elif hasattr(inner, "response"):
                response_text = inner.response
            else:
                response_text = str(inner)
        else:
            response_text = str(full_response)
            
    except Exception as e:
        print(f"Error extracting response: {e}")
        response_text = str(full_response)

    # print("This is what we adding in memory:" + str(response_text))
    memory.add_interaction(query, response_text)

    return response_text