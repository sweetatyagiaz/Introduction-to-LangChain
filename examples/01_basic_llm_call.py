"""
01 - Basic LLM Call
Demonstrates the simplest possible way to call an LLM using LangChain.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    response = llm.invoke("What is LangChain in one sentence?")
    print(response.content)


if __name__ == "__main__":
    main()
