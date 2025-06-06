import os

from framework import LLMAssistant, MCPToolkit

EXA_API_KEY = os.environ["EXA_API_KEY"]

exa = LLMAssistant(
    name="Exa",
    toolkit=MCPToolkit.from_config(
        command="npm",
        args=["exec", "-y", "exa-mcp-server"],
        env={"EXA_API_KEY": EXA_API_KEY},
    ),
)
