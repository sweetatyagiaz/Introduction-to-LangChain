"""
02 - Prompt Templates
Shows how to use PromptTemplate to build reusable, parameterized prompts.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

def main():
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

    template = PromptTemplate.from_template(
        "Explain {topic} to a {audience} in no more than 3 sentences."
    )

    prompt = template.format(topic="vector embeddings", audience="high school student")
    response = llm.invoke(prompt)
    print(response.content)


if __name__ == "__main__":
    main()
