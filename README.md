# LangChain 学习笔记

从零开始学习 LangChain 的完整学习路径，涵盖从基础模型调用到构建 AI Agent 的全过程。

---

## 学习路线

```
模型调用 → 提示词工程 → Chain 链 → Memory 记忆 → Tools 工具 → Agents 智能体 → RAG 检索增强生成 → 实战项目
```

---

## 目录说明

| 章节 | 主题 | 内容概要 |
|------|------|----------|
| **chapter02** | Model IO | 模型调用、PromptTemplate、ChatPromptTemplate、FewShotPrompt、输出解析器 |
| **chapter03** | Chains | LCEL 语法理解、传统 Chain 用法、基于 LCEL 构建链 |
| **chapter04** | Memory | ConversationBufferMemory、ConversationSummaryMemory 等记忆模块 |
| **chapter05** | Tools | 自定义工具定义、大模型分析并调用工具 |
| **chapter06** | Agents | Agent 工具调用、MCP 协议（Server/Client 实现） |
| **chapter07** | RAG | 文档加载、文本拆分、Embedding、Chroma 向量数据库、检索器、智能对话助手综合案例 |
| **chapter08** | 旅行助手智能体 | 基于 ReAct 模式的实战项目，集成天气、景点、交通、美食、预算、路线规划等工具 |

---

## 快速开始

### 环境准备

```bash
# 克隆项目
git clone <repo-url>
cd AiProject

# 创建并激活虚拟环境
python -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install langchain langchain-openai openai tavily-python requests python-dotenv mcp langchain-tavily chromadb
```

### 配置 API 密钥

在 `chapter02-model IO/` 目录下创建 `.env` 文件：

```bash
OPENAI_API_KEY2=your_api_key_here
OPENAI_BASE_URL2=https://api.your-provider.com/v1
TAVILY_API_KEY=your_tavily_api_key
GAODE_API_KEY=your_gaode_key_here
```

---

## 重点章节

### chapter02 - 模型 IO

学习 LangChain 的核心抽象：如何调用大模型、如何构造提示词、如何解析输出。

- `01/02` 模型调用（ChatOpenAI 基础用法）
- `03` PromptTemplate — 变量化提示词
- `04` ChatPromptTemplate — 多角色对话模板
- `05` FewShotPromptTemplate — 少量示例提示词
- `06` 从文件加载 Prompt（JSON/YAML）
- `07` 输出解析器（StrOutputParser、JsonOutputParser 等）
- `08` 调用本地大模型

### chapter03 - Chain 链

掌握 LCEL（LangChain Expression Language）的管道语法：

```python
chain = prompt | model | parser
result = chain.invoke({"input": "..."})
```

### chapter06 - Agents & MCP

- 通过 Notebook 学习 Agent 的工具调用机制
- MCP（Model Context Protocol）实践：用 FastMCP 编写 Server，用 `mcp` SDK 编写 Client

### chapter07 - RAG

完整的 RAG 流程实践：

```
文档加载 → 文本拆分 → 向量嵌入 → 存入 Chroma → 检索 → 生成回答
```

### chapter08 - 旅行助手智能体（实战项目）

一个完整的 ReAct Agent 实战项目，不依赖 LangChain AgentExecutor，手动实现推理-行动循环。

**功能：** 天气查询、景点推荐、交通指南、美食推荐、预算估算、景点地图、路线规划

**运行：**

```bash
cd "chapter08-Hello-Agents"
python travel_assistant_agent.py --interactive   # 交互式多轮对话
python travel_assistant_agent.py                 # 单轮模式
```

---

## 技术栈

- **Python** 3.14
- **LangChain** — LLM 应用开发框架
- **OpenAI SDK** — 兼容 OpenAI 接口的大模型调用
- **Tavily** — 搜索引擎 API
- **Chroma** — 向量数据库
- **MCP** — Model Context Protocol（工具协议）
- **Jupyter Notebook** — 学习和实验环境

---

## 学习资源

- [LangChain 官方文档](https://python.langchain.com/)
- [LangChain 中文教程](https://github.com/langchain-ai/langchain)
- [Tavily Search API](https://docs.tavily.com/)
- [MCP 协议规范](https://modelcontextprotocol.io/)
- [OpenAI API 文档](https://platform.openai.com/docs/api-reference/)