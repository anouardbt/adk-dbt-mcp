# Simple dbt MCP Agent

A simplified dbt analytics agent that connects to a dbt MCP remote server for querying business metrics and dbt project metadaa using Google's ADK.


## Quick Setup

1. **Copy environment variables:**
   ```bash
   cp env.example .env
   ```

2. **Configure your environment in `.env`** (see `env.example` for all options)

3. **Copy the agent to your agents directory and run adk agent:**
   ```bash
   adk web [AGENT DIR]
   ```

## Documentation

For detailed information about:

- **dbt MCP setup and configuration:** https://github.com/dbt-labs/dbt-mcp/
- **ADK (Agent Development Kit):** https://google.github.io/adk-docs/

## Example Usage

- "What metrics are available?"
- "Show revenue by region for this year"
- "What's the avaible models to build XYZ"
- "What are the models that not healthy"
