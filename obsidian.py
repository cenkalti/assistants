import os
from typing import Optional

from framework import LLMAssistant, MCPToolkit

VAULT = os.environ["OBSIDIAN_VAULT"]


def docker_command(
    image: str,
    *,
    args: list[str] = [],
    env: list[tuple[str, str]] = [],
    entrypoint: Optional[str] = None,
    mounts: list[tuple[str, str]] = [],
    volumes: list[tuple[str, str]] = [],
):
    cmd = ["docker", "run", "-i", "--rm"]
    if entrypoint:
        cmd.extend(["--entrypoint", entrypoint])
    for mount in mounts:
        cmd.extend(["--mount", f"type=bind,source={mount[0]},target={mount[1]}"])
    for volume in volumes:
        cmd.extend(["-v", f"{volume[0]}:{volume[1]}"])
    for env_var in env:
        cmd.extend(["-e", f"{env_var[0]}={env_var[1]}"])
    cmd.append(image)
    cmd.extend(args)
    return cmd


def node_package(package: str, **kwargs):
    kwargs["image"] = "node:24"
    kwargs["entrypoint"] = "/usr/local/bin/npm"
    kwargs["args"] = ["exec", package] + kwargs["args"]
    return docker_command(**kwargs)


cmd = node_package(
    "mcp-obsidian",
    args=["/vault"],
    mounts=[(VAULT, "/vault")],
)


obsidian = LLMAssistant(
    name="Obsidian",
    system_prompt="You are Obsidian assistant.",
    toolkit=MCPToolkit.from_config(command=cmd[0], args=cmd[1:]),
)
