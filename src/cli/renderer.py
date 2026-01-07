"""CLI renderer - Output formatting and display functions"""
from src.models.todo import Todo


def display_menu():
    """Display the main menu with all available options."""
    print("\n" + "=" * 40)
    print("         Todo App - Phase I")
    print("=" * 40)
    print("1. Add Todo")
    print("2. View All Todos")
    print("3. View Todo by ID")
    print("4. Update Todo")
    print("5. Delete Todo")
    print("6. Mark Complete")
    print("7. Mark Incomplete")
    print("8. Filter by Status")
    print("9. Exit")
    print("=" * 40)


def display_todo(todo: Todo):
    """Display a single todo with all its details.

    Args:
        todo: The todo to display
    """
    print(f"\nID: {todo.id}")
    print(f"Title: {todo.title}")
    print(f"Description: {todo.description if todo.description else '(none)'}")
    print(f"Status: {todo.status}")
    print("-" * 40)


def display_todos(todos: list[Todo]):
    """Display a list of todos.

    Args:
        todos: List of todos to display
    """
    if not todos:
        print("\nNo todos found.")
        return

    print(f"\nFound {len(todos)} todo(s):")
    for todo in todos:
        display_todo(todo)


def display_error(message: str):
    """Display an error message.

    Args:
        message: The error message to display
    """
    print(f"\n[ERROR] {message}")


def display_success(message: str):
    """Display a success message.

    Args:
        message: The success message to display
    """
    print(f"\n[SUCCESS] {message}")
