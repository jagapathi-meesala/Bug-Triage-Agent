from core.registry import execute_tool

class PortableAdapter:
    """Framework-neutral invocation boundary."""
    def invoke(self, tool_name: str, arguments: dict) -> dict:
        return execute_tool(tool_name, arguments)
