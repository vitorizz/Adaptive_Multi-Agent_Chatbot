from agents.general_agent import GeneralAgent
from agents.admissions_agent import AdmissionsAgent
from agents.ai_agent import AIAgent
from memory.vector_memory import VectorMemory
import requests

memory = VectorMemory()
last_user_query = ""
last_bot_response = ""

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
    global last_user_query, last_bot_response
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

    response = agent.generate_response(query, context)
    memory.add_interaction(query, response)

    last_user_query = query
    last_bot_response = response

    return response