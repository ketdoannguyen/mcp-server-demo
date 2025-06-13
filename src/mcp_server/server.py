import logging
import os
from typing import Any, Dict

import uvicorn
from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)

# Initialize FastMCP server
logger.info("🚀 Initializing FastMCP server...")
mcp_server = FastMCP("Demo")


@mcp_server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    result = a + b
    logger.info(f"Adding {a} + {b} = {result}")
    return result


@mcp_server.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    result = a * b
    logger.info(f"Multiplying {a} * {b} = {result}")
    return result


@mcp_server.tool()
async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city.

    Args:
        city: Name of the city

    Returns:
        Weather information string
    """
    logger.info(f"Fetched weather for {city}")
    return f"Mock weather data for {city}: 25°C, Sunny"


@mcp_server.tool()
async def get_system_info() -> Dict[str, Any]:
    """Get basic system information.

    Returns:
        Dictionary containing system information
    """
    import platform

    info = {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }

    logger.info("Retrieved system information")
    return info


@mcp_server.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting.

    Args:
        name: Name of the person to greet

    Returns:
        Personalized greeting message
    """
    greeting = f"Hello, {name}! Welcome to the MCP server."
    logger.info(f"Generated greeting for {name}")
    return greeting


@mcp_server.resource("config://app")
def get_config() -> str:
    """Get static configuration data.

    Returns:
        Application configuration string
    """
    config = """
    App Configuration:
    - Name: MCP Demo Server
    - Version: 1.0.0
    - Environment: Development
    - Features: Tools, Resources, Prompts
    """
    logger.info("Retrieved app configuration")
    return config.strip()


@mcp_server.prompt()
def review_code(code: str) -> str:
    """Generate a code review prompt.

    Args:
        code: Code to be reviewed

    Returns:
        Formatted code review prompt
    """
    prompt = f"""Please review this code for:
- Code quality and best practices
- Potential bugs or issues
- Performance considerations
- Documentation and readability

Code to review:

```python
{code}
```

Please provide detailed feedback and suggestions for improvement."""

    logger.info("Generated code review prompt")
    return prompt


def get_server_config() -> tuple[str, int]:
    """Get server configuration from environment variables.

    Returns:
        Tuple of (host, port)
    """
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    return host, port


def main() -> None:
    """Main function to start the MCP server."""
    logger.info("🔧 Starting MCP server...")

    try:
        host, port = get_server_config()

        logger.info(f"✅ Server will be available at http://{host}:{port}/sse")
        logger.info("🔗 MCP clients can connect to the SSE endpoint")

        # Start the server
        uvicorn.run(mcp_server.sse_app(), host=host, port=port)

    except KeyboardInterrupt:
        logger.info("\n👋 Server shutting down...")
    except Exception as e:
        logger.error(f"❌ Server error: {e}")
        raise


if __name__ == "__main__":
    main()
