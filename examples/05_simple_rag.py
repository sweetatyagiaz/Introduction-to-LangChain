"""
05 - Simple Retrieval-Augmented Generation (RAG)
Demonstrates embedding a small set of documents, storing them in a vector
store, retrieving relevant chunks for a query, and passing them to an LLM.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

DOCUMENTS = [
    "LangChain is a framework for developing applications powered by language models.",
    "A chain in LangChain connects a sequence of calls, such as a prompt and an LLM.",
    "LangChain supports integration with vector stores like FAISS, Pinecone, and Chroma.",
    "Agents in LangChain let an LLM decide which tools to call to complete a task.",
]

def main():
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore = FAISS.from_texts(DOCUMENTS, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

    prompt = PromptTemplate.from_template(
        "Answer the question using only the context below.\n\n"
        "Context:\n{context}\n\nQuestion: {question}"
    )

    def format_docs(docs):
        return "\n".join(d.page_content for d in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    question = "What is a chain in LangChain?"
    print(chain.invoke(question))


if __name__ == "__main__":
    main()
