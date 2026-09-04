# Introduction to LangChain

A hands-on course of Jupyter notebooks for learning [LangChain](https://www.langchain.com/) — a framework for building applications powered by large language models (LLMs). Each module builds on the last, moving from a single model call to a full tool-using, memory-enabled agent.

## Repository Structure

```
Introduction-to-LangChain/
├── README.md
├── requirements.txt
├── .env.example
└── module_1/
    ├── 1_1_foundational_models.ipynb
    ├── 1_1_prompting.ipynb
    ├── 1_2_tools.ipynb
    ├── 1_2_web_search.ipynb
    ├── 1_3_memory.ipynb
    ├── 1_4_multimodal_messages.ipynb
    ├── 1_5_personal_chef.ipynb
    └── 1_5_personal_chef.py
```

## Prerequisites

- Python 3.12+
- An OpenAI API key (used via `init_chat_model` / `create_agent` with `gpt-5-nano`)
- A [Tavily](https://tavily.com/) API key (used for the web search tool in 1.2 and 1.5)

## Setup

```bash
git clone https://github.com/<your-username>/Introduction-to-LangChain.git
cd Introduction-to-LangChain
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # then fill in your API keys
```

Launch Jupyter and work through `module_1/` in order:

```bash
jupyter notebook module_1/
```

## Module 1: LangChain Foundations

| # | Notebook | What it covers |
|---|----------|-----------------|
| 1.1 | `1_1_foundational_models.ipynb` | Initialising and invoking a chat model with `init_chat_model`; customising model parameters; comparing model providers; initialising and invoking an **agent** with `create_agent`; streaming an agent's output token by token |
| 1.1 | `1_1_prompting.ipynb` | Basic prompting with `create_agent`; steering behavior with a `system_prompt`; few-shot examples inside the system prompt; structured (formatted) prompts; structured **output** using a Pydantic `response_format` schema |
| 1.2 | `1_2_tools.ipynb` | Defining tools with the `@tool` decorator (including custom names/descriptions); invoking a tool directly; attaching tools to an agent so it can call them to answer questions |
| 1.2 | `1_2_web_search.ipynb` | Contrasting an agent with no external knowledge against one with a `web_search` tool (via the Tavily API), so it can answer questions about current events |
| 1.3 | `1_3_memory.ipynb` | Showing that an agent has no memory of prior turns by default, then adding persistent conversation memory with `InMemorySaver` as a `checkpointer` and a `thread_id` config |
| 1.4 | `1_4_multimodal_messages.ipynb` | Sending multimodal `HumanMessage` content: plain text, an uploaded image (base64-encoded), and recorded audio, to models that support each modality |
| 1.5 | `1_5_personal_chef.ipynb` / `.py` | Capstone: a "personal chef" agent that combines a system prompt, the web search tool, and memory to suggest recipes from a user's leftover ingredients and hold a multi-turn conversation about them |

## Key LangChain Concepts Introduced

- **Chat models** — `init_chat_model` for provider-agnostic model initialisation
- **Agents** — `create_agent` as the primary building block for LLM apps
- **Messages** — `HumanMessage`, multimodal content blocks (text/image/audio)
- **Prompting** — system prompts, few-shot examples, structured prompts and structured output (Pydantic)
- **Tools** — the `@tool` decorator, custom tool naming/descriptions, tool calling
- **Web search** — integrating the Tavily API as a tool for up-to-date answers
- **Memory** — `InMemorySaver` checkpointers and thread-based conversation state
- **Streaming** — consuming an agent's response as a stream of tokens

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [Tavily](https://tavily.com/)

## License

This project is licensed under the MIT License — feel free to use it for learning and experimentation.
