# Build With Claude API

Code and notebooks from the [Build with Claude API](https://www.anthropic.com) course, covering the Anthropic Python SDK from basic API calls through advanced features like RAG, tool use, and MCP servers.

## Contents

### 1. Access Claude with API

Fundamentals of the Anthropic Python SDK: making API calls, multi-turn conversations, system prompts, temperature control, streaming responses, and controlling output with message prefilling and stop sequences.

### 2. Prompt Evaluation

A framework for systematically evaluating prompt quality. Includes dataset generation, model-based grading, syntax validation (JSON/Python/Regex), and combined scoring to measure prompt effectiveness.

### 3. Prompt Engineering

Iterative prompt optimization with A/B testing. Demonstrates how to refine prompts step-by-step using a `PromptEvaluator` class, generate test cases, and produce HTML/JSON evaluation reports with scoring rubrics.

### 4. Tool Use with Claude

Extending Claude with external tools: defining tool schemas, executing tool calls, batch tool invocation, forcing structured data extraction, streaming with tools, the text editor tool for file operations, and web search integration.

### 5. Retrieval Augmented Generation

End-to-end RAG pipeline covering document chunking strategies (fixed-size, sentence-based, section-based), embeddings with VoyageAI, vector database search, BM25 keyword search, hybrid retrieval, reranking, and contextual retrieval.

### 6. Features of Claude

Advanced Claude capabilities: extended thinking with budget tokens, multi-modal image and PDF analysis, prompt caching for cost optimization, and the file API with code execution for data analysis and visualization.

### 7. Model Context Protocol

Reserved for MCP (Model Context Protocol) content.

### 8. Claude Code

A hands-on MCP server project built with FastMCP. Exposes document conversion tools (PDF/DOCX to markdown) and math tools through the MCP protocol, with full test coverage and a development guide (`CLAUDE.md`).

## Prerequisites

- Python 3.10+
- An Anthropic API key (set as `ANTHROPIC_API_KEY` environment variable)
- [uv](https://github.com/astral-sh/uv) (for the MCP server in section 8)
- A VoyageAI API key (for embeddings in section 5)

## Getting Started

```bash
# Clone the repo
git clone https://github.com/kongbu/claude-course-build-with-claude-api.git
cd claude-course-build-with-claude-api

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install anthropic python-dotenv

# Set your API key
export ANTHROPIC_API_KEY="your-key-here"
```

Then open any notebook (e.g. `1_access_claude_with_API/001_requests.ipynb`) in Jupyter to get started.

# Additional topics to investigate

- Agent orchestration
- Agent evaluation and instrumentation
- Agentic RAG
- RAG evaluation
- Tool evaluation
