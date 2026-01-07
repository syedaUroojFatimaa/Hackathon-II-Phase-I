"""Main entry point for Todo App - Phase I Console Application"""
import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services.todo_service import TodoService
from src.cli.app import TodoApp


def main():
    """Initialize and run the Todo App."""
    # Create service instance
    service = TodoService()

    # Create and run CLI app
    app = TodoApp(service)
    app.run()


if __name__ == "__main__":
    main()
