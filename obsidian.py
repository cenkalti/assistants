import os
from typing import Optional

from framework import LLMAssistant, MCPToolkit

VAULT = os.environ["OBSIDIAN_VAULT"]
NPM_CACHE_DIR = os.environ["NPM_CACHE_DIR"]


def docker_command(
    image: str,
    *,
    name: Optional[str] = None,
    args: list[str] = [],
    env: list[tuple[str, str]] = [],
    entrypoint: Optional[str] = None,
    mounts: list[tuple[str, str]] = [],
    volumes: list[tuple[str, str]] = [],
):
    cmd = ["docker", "run", "-i", "--rm"]
    if name:
        cmd.extend(["--name", f"akson-{name}"])
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
    kwargs["args"] = ["exec", package] + kwargs["args"]
    kwargs["mounts"] = kwargs.get("mounts", []) + [(NPM_CACHE_DIR, "/root/.npm")]
    return docker_command("node:24", name=package, entrypoint="/usr/local/bin/npm", **kwargs)


cmd = node_package(
    "mcp-obsidian",
    args=["/vault"],
    mounts=[(VAULT, "/vault")],
)


obsidian = LLMAssistant(
    name="Obsidian",
    system_prompt="""
    You are Obsidian assistant who has access to the Obsidian vault of the user.
    When searching for notes, use singular words.
    """,
    toolkit=MCPToolkit.from_config(command=cmd[0], args=cmd[1:]),
)
