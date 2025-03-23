Adaptive Multi-Agent Chatbot
============================

This project is for COMP 474 -- Intelligent Systems at Concordia University. It implements an adaptive multi-agent chatbot system that leverages Ollama for LLM-based responses, LangChain for memory and prompt engineering, and FAISS for vector memory storage. The chatbot dynamically routes queries to specialized agents---General, Admissions, and AI---while maintaining context across multi-turn conversations and integrating external knowledge (e.g., from Wikipedia).

Table of Contents
-----------------

-   Features

-   Project Structure

-   Installation

-   Running the Application

-   Usage

-   Authors

Features
--------

-   **Multi-Agent Architecture:**

    -   **General Agent:** Handles generic questions.

    -   **Admissions Agent:** Provides detailed Concordia University Computer Science admissions information.

    -   **AI Agent:** Answers questions related to AI, machine learning, and deep learning.

-   **Context Management and Retrieval-Augmented Generation (RAG):**

    -   Uses LangChain and FAISS to store and retrieve conversation history via vector embeddings.

    -   Supports multi-turn conversations by prepending relevant past interactions to the current query.

-   **External Knowledge Integration:**

    -   Integrates with Wikipedia to fetch up-to-date information when available.

-   **FastAPI-based API:**

    -   Provides REST endpoints for user queries.

    -   Easily deployable locally or on cloud platforms.
 
 
Project Structure
-----------------

- **adaptive_multi-agent_chatbot/**
  - **agents/**
    - `__init__.py`
    - `base_agent.py` – Abstract base class for agents
    - `general_agent.py` – General questions agent
    - `admissions_agent.py` – Admissions-specific agent
    - `ai_agent.py` – AI-related queries agent
  - **api/**
    - `__init__.py`
    - `main.py` – FastAPI server entry point
  - **external/**
    - `__init__.py`
    - `wikipedia_api.py` – Wikipedia integration for external knowledge
  - **memory/**
    - `__init__.py`
    - `vector_memory.py` – FAISS vector memory using LangChain and FAISS
  - **orchestrator/**
    - `__init__.py`
    - `router.py` – Routes queries to the appropriate agent
  - **llm/**
    - `__init__.py`
    - `ollama_client.py` – Integrates with the Ollama API for LLM responses
  - **tests/**
    - `__init__.py`
    - `test_agents.py` – Unit tests for agents and modules
  - `requirements.txt` – Python dependencies
  - `README.md` – This file
 
Installation
------------

1.  **Clone the repository:**

    `git clone https://github.com/vitorizz/Adaptive_Multi-Agent_Chatbot.git
    cd adaptive_chatbot`

2.  **Create a Python virtual environment:**

    `python -m venv venv`

3.  **Activate the virtual environment:**

    -   **Windows:**

        `venv\Scripts\activate`

    -   **macOS/Linux:** (Project has not been tested on MacOS)

        `source venv/bin/activate`

4.  **Install the required dependencies:**

    `pip install -r requirements.txt`

    **Note:** The `requirements.txt` includes packages such as:

    -   `fastapi`

    -   `uvicorn`

    -   `requests`

    -   `langchain`

    -   `faiss-cpu`

    -   `sentence-transformers`

    -   `wikipedia-api`

Running the Application
-----------------------

1.  **Start the FastAPI server:**

    `uvicorn api.main:app --reload`

2.  **Access the API:**

    The server runs by default on <http://127.0.0.1:8000>.

3.  **API Endpoints:**

**GET /query**

*Example using Postman:*

1\. Open Postman and create a new GET request.

2\. Set the URL to:

http://127.0.0.1:8000/query?query=What is Concordia's CS admission process?

3\. Click "Send" to execute the request.

This endpoint routes the query to the appropriate agent (based on keywords) and returns a JSON response:

```json

{ "query": "your query here", "response": "agent's response here" }
```


Usage
-----

-   **Multi-turn Conversations:**\
    The chatbot retains context using a vector memory system. Follow-up questions automatically incorporate the most relevant past interactions.

-   **Domain-Specific Routing:**\
    The router inspects the query and selects one of the three agents:

    -   Queries with keywords like "admission," "apply," or "Concordia" are handled by the Admissions Agent.

    -   Queries with keywords like "AI," "machine learning," or "neural" are handled by the AI Agent.

    -   All other queries are handled by the General Agent.

-   **External Knowledge:**\
    If available, the chatbot augments its responses with Wikipedia summaries.



Authors
-------
Vito Rizzuto 40246408
Miro
Kate
