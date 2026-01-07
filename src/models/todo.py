"""Todo model - Domain entity for todo items"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Todo:
    """Represents a single task item in the todo list.

    Attributes:
        id: Unique identifier (auto-generated, sequential)
        title: Task description (non-empty string)
        description: Additional details (optional)
        status: Current state - "pending" or "completed"
    """
    id: int
    title: str
    description: str
    status: str  # "pending" | "completed"
