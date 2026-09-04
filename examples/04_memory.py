"""
04 - Conversation Memory
Shows how to maintain conversation history across multiple turns.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

def main():
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

    history = []

    turns = [
        "My name is Alex and I'm learning LangChain.",
        "What's my name?",
    ]

    for user_input in turns:
        history.append(HumanMessage(content=user_input))
        response = llm.invoke(history)
        history.append(AIMessage(content=response.content))
        print(f"User: {user_input}")
        print(f"AI: {response.content}\n")


if __name__ == "__main__":
    main()
