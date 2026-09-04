# Introduction to LangChain

A hands-on course of Jupyter notebooks for learning [LangChain](https://www.langchain.com/) — a framework for building applications powered by large language models (LLMs). Module 1 covers the foundations (models, prompting, tools, memory, multimodal input). Module 2 builds on that with MCP, runtime context, custom state, multi-agent systems, and bonus RAG/SQL agents.

## Repository Structure

```
Introduction-to-LangChain/
├── README.md
├── requirements.txt
├── .env.example
├── module_1/
│   ├── 1_1_foundational_models.ipynb
│   ├── 1_1_prompting.ipynb
│   ├── 1_2_tools.ipynb
│   ├── 1_2_web_search.ipynb
│   ├── 1_3_memory.ipynb
│   ├── 1_4_multimodal_messages.ipynb
│   ├── 1_5_personal_chef.ipynb
│   └── 1_5_personal_chef.py
└── module_2/
    ├── 2_1_mcp.ipynb
    ├── 2_1_travel_agent.ipynb
    ├── 2_2_runtime_context.ipynb
    ├── 2_2_state.ipynb
    ├── 2_3_multi_agent.ipynb
    ├── 2_4_wedding_planners.ipynb
    ├── bonus_rag.ipynb
    └── bonus_sql.ipynb
```

## Prerequisites

- Python 3.12+
- An OpenAI API key (used via `init_chat_model` / `create_agent` with `gpt-5-nano`)
- A [Tavily](https://tavily.com/) API key (web search tool in Module 1 and the wedding planner lab)
- `uv` installed if you want to run the online MCP time-server example in `2_1_mcp.ipynb`

## Setup

```bash
git clone https://github.com/<your-username>/Introduction-to-LangChain.git
cd Introduction-to-LangChain
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # then fill in your API keys
```

Launch Jupyter and work through the modules in order:

```bash
jupyter notebook module_1/
jupyter notebook module_2/
```

## Module 1: LangChain Foundations

| # | Notebook | What it covers |
|---|----------|-----------------|
| 1.1 | [1_1_foundational_models.ipynb](notebooks/module-1/1.1_foundational_models.ipynb) | Initialising and invoking a chat model with `init_chat_model`; customising model parameters; comparing model providers; initialising and invoking an **agent** with `create_agent`; streaming an agent's output token by token |
| 1.1 | [1_1_prompting.ipynb](notebooks/module-1/1.1_prompting.ipynb) | Basic prompting with `create_agent`; steering behavior with a `system_prompt`; few-shot examples inside the system prompt; structured (formatted) prompts; structured **output** using a Pydantic `response_format` schema |
| 1.2 | [1_2_tools.ipynb](notebooks/module-1/1.2_tools.ipynb) | Defining tools with the `@tool` decorator (including custom names/descriptions); invoking a tool directly; attaching tools to an agent so it can call them to answer questions |
| 1.2 | [1_2_web_search.ipynb](notebooks/module-1/1.2_web_search.ipynb) | Contrasting an agent with no external knowledge against one with a `web_search` tool (via the Tavily API), so it can answer questions about current events |
| 1.3 | [1_3_memory.ipynb](notebooks/module-1/1.3_memory.ipynb) | Showing that an agent has no memory of prior turns by default, then adding persistent conversation memory with `InMemorySaver` as a `checkpointer` and a `thread_id` config |
| 1.4 | [1_4_multimodal_messages.ipynb](notebooks/module-1/1.4_multimodal_messages.ipynb) | Sending multimodal `HumanMessage` content: plain text, an uploaded image (base64-encoded), and recorded audio, to models that support each modality |
| 1.5 | [1_5_personal_chef.ipynb](notebooks/module-1/1.5_personal_chef.ipynb) / [.py](notebooks/module-1/1.5_personal_chef.py) | Capstone: a "personal chef" agent that combines a system prompt, the web search tool, and memory to suggest recipes from a user's leftover ingredients and hold a multi-turn conversation about them |

**Key concepts:** chat models, agents, messages, prompting, structured output, tools, web search, memory, streaming.

## Module 2: Agentic Systems

| # | Notebook | What it covers |
|---|----------|-----------------|
| 2.1 | [2_1_mcp.ipynb](module_2/2_1_mcp.ipynb) | Connecting an agent to the Model Context Protocol (MCP) via `MultiServerMCPClient`: launching a **local** stdio MCP server and pulling its tools/resources/prompts, then connecting to an **online** MCP server (a time server run with `uv`) |
| 2.1 | [2_1_travel_agent.ipynb](module_2/2_1_travel_agent.ipynb) | Building a travel agent by connecting to a remote MCP server over `streamable_http` (Kiwi's flight-search MCP), combined with a `system_prompt` and `InMemorySaver` memory |
| 2.2 | [2_2_runtime_context.ipynb](module_2/2_2_runtime_context.ipynb) | Passing static runtime context into an agent via a `context_schema` dataclass, and reading that context from inside a tool using `ToolRuntime` |
| 2.2 | [2_2_state.ipynb](module_2/2_2_state.ipynb) | Defining a `CustomState` (extending `AgentState`) so tools can **write to** state via `Command` updates and **read from** state via `ToolRuntime.state`, persisted per `thread_id` |
| 2.3 | [2_3_multi_agent.ipynb](module_2/2_3_multi_agent.ipynb) | Composing multiple agents: creating specialised subagents (square root / square), wrapping each as a tool, and having a main coordinator agent decide which subagent to call |
| 2.4 | [2_4_wedding_planners.ipynb](module_2/2_4_wedding_planners.ipynb) | Capstone: a multi-agent **wedding planner** that coordinates subagents (flights via the Kiwi MCP server with retry/error-handling interceptors, venue search, and playlist curation via web search) behind a main coordinator agent, with production concerns like retryable MCP error handling and search-count limits |
| bonus | [bonus_rag.ipynb](module_2/bonus_rag.ipynb) | Retrieval-augmented generation: loading a PDF with `PyPDFLoader`, chunking with `RecursiveCharacterTextSplitter`, embedding with `OpenAIEmbeddings`, storing/querying an `InMemoryVectorStore`, and wrapping similarity search as a tool for an agent to search an employee handbook |
| bonus | [bonus_sql.ipynb](module_2/bonus_sql.ipynb) | Giving an agent access to a SQL database via `SQLDatabase` and a custom `sql_query` tool, letting it write and run its own queries against a SQLite database (Chinook) to answer natural-language questions |

**Key concepts:** MCP (Model Context Protocol) clients/servers, remote tool servers, runtime context, custom agent state (read/write), multi-agent composition (subagents-as-tools), retry/error-handling for external tools, RAG (retrieval-augmented generation), SQL agents.

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
- [Tavily](https://tavily.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## License

This project is licensed under the MIT License — feel free to use it for learning and experimentation.
