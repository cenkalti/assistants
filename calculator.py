from enum import StrEnum

from framework import FunctionToolkit, LLMAssistant
from pydantic import BaseModel

system_prompt = """
    You are an assistant that has access to a calculator.
    Use your tools to calculate the result of the given expression.
"""


type Number = int | float


class Operation(StrEnum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


def calculate(a: Number, op: Operation, b: Number) -> Number:
    """
    Calculate the result of the given operation.

    Args:
      a (Number): The first number
      op (Operation): The operation to perform
      b (Number): The second number

    Returns:
      Number: The result of the operation
    """
    match op:
        case Operation.ADD:
            return a + b
        case Operation.SUBTRACT:
            return a - b
        case Operation.MULTIPLY:
            return a * b
        case Operation.DIVIDE:
            return a / b
        case _:
            raise ValueError(f"Unknown operation: {op}")


class Result(BaseModel):
    answer: int


calculator = LLMAssistant(
    name="Calculator",
    system_prompt=system_prompt,
    toolkit=FunctionToolkit([calculate]),
    output_type=Result,
)
