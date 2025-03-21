# import requests

# OLLAMA_API_URL = "http://127.0.0.1:11434/api/chat"

# def query_ollama(model_name: str, prompt: str) -> str:
#     """
#     Send a prompt to the Ollama model and return the generated response. 
#     """
#     payload = {
#         "model": model_name, 
#         "prompt": prompt
#     }

#     response = requests.post(OLLAMA_API_URL, json=payload, stream=False)
#     if response.status_code == 200:
#         data = response.json()
#         return data.get("response", "No response")
#     else:
#         raise Exception(f"Ollama API call failed with status code {response.status_code}: {response.text}")

import ollama

client = ollama.Client()

def query_ollama(model: str, prompt: str) -> str:

    model = model
    prompt = prompt
    response = client.generate(model=model, prompt=prompt)

    return response



