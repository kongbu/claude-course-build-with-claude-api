# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python MCP (Model Context Protocol) server that exposes document-related tools for AI assistants. Tools are Python functions registered with FastMCP and accessed through the MCP protocol.

## Commands

```bash
# Setup (requires Python 3.10+)
uv venv
source .venv/bin/activate
uv pip install -e .

# Run the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_document.py

# Run a specific test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

**Entry Point**: `main.py` creates a `FastMCP` server instance and registers tools.

**Tool Registration**: Tools are registered in `main.py` using:
```python
mcp.tool()(my_function)
```

**Tool Implementations**: Located in `tools/` directory. Each tool is a Python function.

## Defining MCP Tools

Tools must follow this pattern:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does")
) -> ReturnType:
    """One-line summary of what this tool does.

    Detailed explanation of the tool's functionality.

    When to use:
    - Use case 1
    - Use case 2

    When NOT to use:
    - Anti-pattern 1

    Examples:
        >>> my_tool("input", 42)
        "expected output"
    """
    # Implementation
```

Key requirements:
- Use Pydantic `Field` for all parameter descriptions
- Docstrings must include: one-line summary, detailed explanation, when to use/not use, examples
- Register in `main.py` with `mcp.tool()(function_name)`

## Code Style

- Always apply appropriate types to function arguments

## Test Structure

Tests use pytest with fixture files in `tests/fixtures/`. Test files follow the pattern `test_<module>.py` with test classes named `Test<ClassName>`.
