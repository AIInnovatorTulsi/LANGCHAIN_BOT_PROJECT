# LANGCHAIN_BOT_PROJECT

An intelligent multi-agent AI system built using LangChain, LangGraph, and vector databases.
This project simulates autonomous bots that generate content, select relevant personas, and respond intelligently to user interactions.

# Features

* Bot Routing System
  Uses vector similarity search to match user input with the most relevant bot persona

* Vector Database (Chroma)
  Stores bot personalities using embeddings for semantic search

* Autonomous Content Engine (LangGraph)
  Automatically generates posts based on trending topics

* AI Reply System (Groq / Fallback)
  Generates smart, context-aware replies
  Includes fallback mechanism if API fails

* Prompt Injection Defense
  Prevents malicious user inputs from manipulating the bot

# How to Run
Step 1: Setup Database
python phase1.py

Step 2: Generate Content
python phase2.py

Step 3: Generate AI Reply
python phase3.py

# How It Works
1. Bot personas are stored in a vector database
2. User input is matched with the most relevant bot
3. LangGraph generates autonomous content
4. LLM generates intelligent replies
5. Fallback ensures reliability without API

# Example Output
{
"bot_id": "BotA",
"topic": "Latest AI news",
"post_content": "OpenAI releases powerful new model - Tech is the future!"
}

# Tech Stack
* Python
* LangChain
* LangGraph
* ChromaDB
* HuggingFace Embeddings
* Groq API
