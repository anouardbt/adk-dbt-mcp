# Simple dbt MCP Agent

A simplified dbt analytics agent that connects to a dbt MCP remote server for querying business metrics and data using Google Vertex AI.

## Quick Setup

1. **Copy environment variables:**
   ```bash
   cp env.example .env
   ```

2. **Configure your environment in `.env`** (see `env.example` for all options)

3. **Run the agent:**
   ```bash
   adk web dbt_simple.agent:root_agent
   ```

## Documentation

For detailed information about:

- **dbt MCP setup and configuration:** https://github.com/dbt-labs/dbt-mcp/
- **ADK (Agent Development Kit):** https://google.github.io/adk-docs/

## Example Usage

- "What metrics are available?"
- "Show revenue by region for this year"
- "Execute SQL: SELECT * FROM customers LIMIT 10"
