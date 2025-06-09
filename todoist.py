import os

from framework import LLMAssistant, MCPToolkit

TODOIST_API_TOKEN = os.environ["TODOIST_API_TOKEN"]

todoist = LLMAssistant(
    name="Todoist",
    model="claude-sonnet-4-20250514",
    system_prompt=("You are Todoist assistant."),
    toolkit=MCPToolkit.from_docker_image("todoist-mcp", env=[("TODOIST_API_KEY", TODOIST_API_TOKEN)]),
)
