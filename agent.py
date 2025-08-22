import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams

load_dotenv()

# Simple agent instructions
AGENT_INSTRUCTIONS = "Use the tools to answer the user's questions."

# Vertex AI model configuration
ADK_MODEL = os.environ.get("ADK_MODEL", "gemini-2.0-flash")

# dbt MCP Configuration
DBT_MCP_URL = os.environ.get("DBT_MCP_URL")

# Validate required environment variables
required_vars = ["DBT_MCP_URL", "DBT_TOKEN", "DBT_USER_ID", "DBT_PROD_ENV_ID"]
missing_vars = [var for var in required_vars if not os.environ.get(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Use Vertex AI model
model = ADK_MODEL

# Initialize dbt MCP toolset with remote server connection
dbt_mcp_toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=DBT_MCP_URL,
        headers={
            "x-dbt-user-id": os.environ.get("DBT_USER_ID"),
            "x-dbt-prod-environment-id": os.environ.get("DBT_PROD_ENV_ID"),
            "x-dbt-dev-environment-id": os.environ.get("DBT_DEV_ENV_ID"),
            "x-dbt-account-id": os.environ.get("DBT_ACCOUNT_ID"),
            "Authorization": f"token {os.environ.get('DBT_TOKEN')}",
        },
    )
)

# Initialize the agent
root_agent = Agent(
    name=os.environ.get("AGENT_NAME", "dbt_simple_agent"),
    model=model,
    description="Simple dbt analytics agent using MCP remote server for querying business metrics and data.",
    instruction=AGENT_INSTRUCTIONS,
    tools=[dbt_mcp_toolset],
)
