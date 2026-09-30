from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class ToolContract:
    name: str
    purpose: str
    input_schema: dict[str, Any]
    output_schema: dict[str, Any]
    validator: Callable[[dict[str, Any]], None]
    executor: Callable[[dict[str, Any]], dict[str, Any]]

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        self.validator(payload)
        return self.executor(payload)
