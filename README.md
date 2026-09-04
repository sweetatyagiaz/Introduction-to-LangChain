# Introduction to LangChain

A hands-on course of Jupyter notebooks for learning [LangChain](https://www.langchain.com/) — a framework for building applications powered by large language models (LLMs). Module 1 covers the foundations (models, prompting, tools, memory, multimodal input). Module 2 builds on that with MCP, runtime context, custom state, multi-agent systems, and bonus RAG/SQL agents.

## Repository Structure

```
Introduction-to-LangChain/
├── README.md
├── requirements.txt
├── .env.example
├── module_1/
│   ├── Lesson 1: Foundation Models
│       ├── 1_1_foundational_models.ipynb
│       ├── 1_1_prompting.ipynb
│   ├── Lesson 2: Tools
│       ├── 1_2_tools.ipynb
│       ├── 1_2_web_search.ipynb
│   ├── Lesson 3: Short-Term Memory     (1_3_memory.ipynb)
│   ├── Lesson 4: MultiModal Messages   (1_4_multimodal_messages.ipynb)
│   ├── Lesson 5: Personal Chef
│       ├── 1_5_personal_chef.ipynb
│       └── 1_5_personal_chef.py
├── module_2/
│   ├── Lesson 1: MCP
│       ├── 2_1_mcp.ipynb
│       ├── 2_1_travel_agent.ipynb
│   ├── Lesson 2: Context and State
│       ├── 2_2_runtime_context.ipynb
│       ├── 2_2_state.ipynb
│   ├── Lesson 3: Multi-Agent Systems (2_3_multi_agent.ipynb)
│   ├── Lesson 4: Wedding Planner (2_4_wedding_planners.ipynb)
│   ├── Bonus: RAG & SQL Query (bonus_rag.ipynb, bonus_sql.ipynb)
└── module_3/
    ├── Lession 1: What is Middleware? (3.2_managing_messages.ipynb)
    ├── Lesson 3: Human In The Loop (3.3_hitl.ipynb)
    ├── Lesson 4: Dynamic Agents
        ├── 3_4_dynamic_models.ipynb
        ├── 3_4_dynamic_prompts.ipynb
        ├── 3_4_dynamic_tools.ipynb
    ├── Lesson 5: Email Assistant
        ├── 3_5_email_agent.ipynb
        ├── 3_5_email_agent.py
        └── Front End App Reference: agent-chat-ui
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
| 2.1 | [2_1_mcp.ipynb](notebooks/module-2/2.1_mcp.ipynb) | Connecting an agent to the Model Context Protocol (MCP) via `MultiServerMCPClient`: launching a **local** stdio MCP server and pulling its tools/resources/prompts, then connecting to an **online** MCP server (a time server run with `uv`) |
| 2.1 | [2_1_travel_agent.ipynb](notebooks/module-2/2.1_travel_agent.ipynb) | Building a travel agent by connecting to a remote MCP server over `streamable_http` (Kiwi's flight-search MCP), combined with a `system_prompt` and `InMemorySaver` memory |
| 2.2 | [2_2_runtime_context.ipynb](notebooks/module-2/2.2_runtime_context.ipynb) | Passing static runtime context into an agent via a `context_schema` dataclass, and reading that context from inside a tool using `ToolRuntime` |
| 2.2 | [2_2_state.ipynb](notebooks/module-2/2.2_state.ipynb) | Defining a `CustomState` (extending `AgentState`) so tools can **write to** state via `Command` updates and **read from** state via `ToolRuntime.state`, persisted per `thread_id` |
| 2.3 | [2_3_multi_agent.ipynb](notebooks/module-2/2.3_multi_agent.ipynb) | Composing multiple agents: creating specialised subagents (square root / square), wrapping each as a tool, and having a main coordinator agent decide which subagent to call |
| 2.4 | [2_4_wedding_planners.ipynb](notebooks/module-2/2.4_wedding_planners.ipynb) | Capstone: a multi-agent **wedding planner** that coordinates subagents (flights via the Kiwi MCP server with retry/error-handling interceptors, venue search, and playlist curation via web search) behind a main coordinator agent, with production concerns like retryable MCP error handling and search-count limits |
| bonus | [bonus_rag.ipynb](notebooks/module-2/bonus_rag.ipynb) | Retrieval-augmented generation: loading a PDF with `PyPDFLoader`, chunking with `RecursiveCharacterTextSplitter`, embedding with `OpenAIEmbeddings`, storing/querying an `InMemoryVectorStore`, and wrapping similarity search as a tool for an agent to search an employee handbook |
| bonus | [bonus_sql.ipynb](notebooks/module-2/bonus_sql.ipynb) | Giving an agent access to a SQL database via `SQLDatabase` and a custom `sql_query` tool, letting it write and run its own queries against a SQLite database (Chinook) to answer natural-language questions |

**Key concepts:** MCP (Model Context Protocol) clients/servers, remote tool servers, runtime context, custom agent state (read/write), multi-agent composition (subagents-as-tools), retry/error-handling for external tools, RAG (retrieval-augmented generation), SQL agents.

## Module 3: Middleware & Agent Control

| # | Notebook | What it covers |
|---|----------|-----------------|
| 3.2 | [3_2_managing_messages.ipynb](notebooks/module-3/3.2_managing_messages.ipynb) | Managing long conversation histories: auto-summarizing older messages with `SummarizationMiddleware` (token-based trigger, keeping the most recent message), and a custom `@before_agent` middleware that trims/deletes messages (e.g. removing `ToolMessage`s) from state via `RemoveMessage` |
| 3.3 | [3_3_hitl.ipynb](notebooks/module-3/3.3_hitl.ipynb) | Human-in-the-loop (HITL) tool approval with `HumanInTheLoopMiddleware`: marking some tools as auto-run and others as requiring approval, inspecting the resulting `__interrupt__`, and resuming the paused run by **approving**, **rejecting** (with a message), or **editing** the tool call before it executes |
| 3.4 | [3_4_dynamic_models.ipynb](notebooks/module-3/3.4_dynamic_models.ipynb) | Dynamically swapping which model handles a request with `@wrap_model_call`: picking a larger model for long conversations and a smaller/cheaper one for short ones, based on message count in state |
| 3.4 | [3_4_dynamic_prompts.ipynb](notebooks/module-3/3.4_dynamic_prompts.ipynb) | Generating the system prompt dynamically per-request with `@dynamic_prompt`, driven by runtime context (e.g. responding only in the user's requested language) |
| 3.4 | [3_4_dynamic_tools.ipynb](notebooks/module-3/3.4_dynamic_tools.ipynb) | Restricting which tools are available to the model per-request with `@wrap_model_call`, based on runtime context (e.g. giving "internal" users access to a SQL tool but "external" users only web search) |
| 3.5 | [3_5_email_agent.ipynb](module_3/3_5_email_agent.ipynb) / [.py](module_3/3_5_email_agent.py) | Capstone: an email agent that combines everything from Module 3 — an `authenticate` tool that writes to custom state, dynamic tools/prompt middleware that only unlock the inbox once authenticated, and `HumanInTheLoopMiddleware` requiring approval before any email is actually sent |

**Key concepts:** middleware (`SummarizationMiddleware`, `@before_agent`, `@wrap_model_call`, `@dynamic_prompt`), conversation trimming/summarization, human-in-the-loop approval (approve/reject/edit), dynamic model selection, dynamic prompts, dynamic tool access control, state-gated authentication flows.

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
- [Tavily](https://tavily.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## License

This project is licensed under the MIT License — feel free to use it for learning and experimentation.
