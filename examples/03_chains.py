"""
03 - Chains
Demonstrates chaining a prompt template, an LLM, and an output parser together
using LangChain Expression Language (LCEL).
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def main():
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    prompt = PromptTemplate.from_template("Give me 3 project ideas for learning {subject}.")
    parser = StrOutputParser()

    # Chain: prompt -> llm -> parser
    chain = prompt | llm | parser

    result = chain.invoke({"subject": "LangChain"})
    print(result)


if __name__ == "__main__":
    main()
