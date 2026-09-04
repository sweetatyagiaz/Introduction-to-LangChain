# Introduction to LangChain

A beginner-friendly guide and set of runnable examples for getting started with [LangChain](https://www.langchain.com/) — a framework for building applications powered by large language models (LLMs).

## What is LangChain?

LangChain provides building blocks for creating LLM-powered applications: prompt templates, chains, memory, tools/agents, and integrations with vector stores and external APIs. This repo walks through the core concepts step by step, from a simple LLM call to a basic retrieval-augmented (RAG) pipeline.

## Repository Structure

```
Introduction-to-LangChain/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .env.example            # Template for API keys
├── examples/               # Standalone Python scripts
│   ├── 01_basic_llm_call.py
│   ├── 02_prompt_templates.py
│   ├── 03_chains.py
│   ├── 04_memory.py
│   └── 05_simple_rag.py
└── notebooks/               # Jupyter notebooks for interactive exploration
    └── getting_started.ipynb
```

## Prerequisites

- Python 3.9+
- An API key from an LLM provider (e.g. OpenAI, Anthropic)

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Introduction-to-LangChain.git
   cd Introduction-to-LangChain
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your API key:
   ```bash
   cp .env.example .env
   ```

## Topics Covered

| # | Topic | File |
|---|-------|------|
| 1 | Making a basic LLM call | `examples/01_basic_llm_call.py` |
| 2 | Prompt templates | `examples/02_prompt_templates.py` |
| 3 | Chains (combining steps) | `examples/03_chains.py` |
| 4 | Conversation memory | `examples/04_memory.py` |
| 5 | Simple retrieval-augmented generation (RAG) | `examples/05_simple_rag.py` |

## Running an Example

```bash
python examples/01_basic_llm_call.py
```

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)

## License

This project is licensed under the MIT License — feel free to use it for learning and experimentation.
