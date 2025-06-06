from framework import LLMAssistant, MCPToolkit

pizza_orderer = LLMAssistant(
    name="Pizza Orderer",
    system_prompt="You are an AI assistant that can order pizza over the phone.",
    toolkit=MCPToolkit.from_config(
        command="uv",
        args=["run", "python", "mcp-servers/bland.py"],
    ),
)
