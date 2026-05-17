# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LangChain + AI Agent learning project organized into chapters (chapter02 through chapter08), progressing from basic model I/O to building a full ReAct travel assistant agent.

## Project Structure

- **chapter02-model IO/** — LLM calling, prompt templates (PromptTemplate, ChatPromptTemplate), output parsers. Contains `.env` with API keys.
- **chapter03-chains/** — LangChain chains: LCEL syntax and traditional Chain usage.
- **chapter04-memory/** — Conversation memory modules (ConversationBufferMemory, etc.).
- **chapter05-tools/** — Custom tool definitions and LLM tool-calling.
- **chapter06-agents/** — Agent tool invocation (notebook), MCP server/client implementations.
- **chapter07-RAG/** — RAG pipeline: document loaders, splitters, embeddings, vector stores (Chroma), retrievers, and a conversational QA assistant.
- **chapter08-Hello-Agents/** — Main project: a ReAct-pattern travel assistant agent with weather, attractions, transport, restaurant, budget, and route planning tools.

## Development Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies (no requirements.txt — key packages)
pip install langchain langchain-openai openai tavily-python requests python-dotenv mcp langchain-tavily

# Run the travel assistant agent (chapter08)
cd "chapter08-Hello-Agents"
python travel_assistant_agent.py --interactive   # interactive multi-turn mode
python travel_assistant_agent.py                 # single-turn mode

# Run MCP server (chapter06)
python chapter06-agents/03-MCP_server.py

# Run notebooks
jupyter notebook chapter07-RAG/01-文档加载器的使用.ipynb
```

## Environment Variables

The `.env` file lives in `chapter02-model IO/`. Scripts load it via `dotenv.load_dotenv(dotenv_path='../chapter02-model IO/.env')`.

Required keys:
- `OPENAI_API_KEY2` / `OPENAI_BASE_URL2` — OpenAI-compatible LLM endpoint (uses deepseek-v4-flash)
- `TAVILY_API_KEY` — Tavily search API
- `GAODE_API_KEY` — Gaode (Amap) maps API for geocoding and route planning

## Architecture: Travel Assistant Agent (chapter08)

The core agent (`travel_assistant_agent.py`) implements a manual ReAct loop:

1. **System prompt** defines available tools and output format (Thought/Action/Finish)
2. **Tool functions**: `get_weather`, `get_attraction`, `get_transport`, `get_restaurant`, `estimate_budget`, `show_map`, `get_route`
3. **LLM client** (`OpenAICompatibleClient`) wraps any OpenAI-compatible API
4. **ReAct loop**: parse Thought → Action from LLM output, execute tool, append Observation, repeat
5. **Conversation management** (`TravelAssistant` class): maintains OpenAI messages format context with history truncation

The agent does NOT use LangChain's built-in AgentExecutor — it implements its own parsing and tool dispatch with regex.

## Key Technical Details

- Python 3.14 with venv at `.venv/`
- Notebooks use Chinese filenames and comments (learning materials)
- MCP server uses FastMCP with stdio transport
- Vector stores in RAG chapter use Chroma (persisted in `chapter07-RAG/asset/`)
- The `asset/load/` directory contains sample documents and Python function examples for the RAG chapter