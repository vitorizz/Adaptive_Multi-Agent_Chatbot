from fastapi import FastAPI, HTTPException
from orchestrator.router import route_query

app = FastAPI(title="Adaptive Multi-agent Chatbot API")

@app.get("/query")
def get_response(query: str):
    try: 
        response = route_query(query)
        return {"query": query, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))