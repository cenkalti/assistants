import os

from framework import LLMAssistant, MCPToolkit

VAULT = os.environ["OBSIDIAN_VAULT"]


obsidian = LLMAssistant(
    name="Obsidian",
    system_prompt="""
    You are Obsidian assistant who has access to the Obsidian vault of the user.
    When searching for notes, use singular words.
    """,
    toolkit=MCPToolkit.from_node_package(
        "mcp-obsidian",
        args=["/vault"],
        mounts=[(VAULT, "/vault")],
    ),
)
