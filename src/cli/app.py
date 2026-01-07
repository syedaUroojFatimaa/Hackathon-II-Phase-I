"""CLI app - Main application loop and command routing"""
from src.services.todo_service import TodoService
from src.cli import renderer, parser


class TodoApp:
    """Main CLI application for managing todos.

    Handles user interaction, command routing, and error handling.
    """

    def __init__(self, service: TodoService):
        """Initialize the app with a TodoService instance.

        Args:
            service: The TodoService to use for todo operations
        """
        self.service = service
        self.running = True

    def run(self):
        """Start the main application loop."""
        print("\nWelcome to Todo App!")

        while self.running:
            renderer.display_menu()
            choice = parser.get_user_input("\nEnter choice (1-9): ")

            if choice == "1":
                self.handle_add()
            elif choice == "2":
                self.handle_view_all()
            elif choice == "3":
                self.handle_view_by_id()
            elif choice == "4":
                self.handle_update()
            elif choice == "5":
                self.handle_delete()
            elif choice == "6":
                self.handle_mark_complete()
            elif choice == "7":
                self.handle_mark_incomplete()
            elif choice == "8":
                self.handle_filter()
            elif choice == "9":
                self.handle_exit()
            else:
                renderer.display_error("Invalid choice. Please enter a number between 1 and 9.")

    def handle_add(self):
        """Handle the 'Add Todo' command."""
        print("\n--- Add Todo ---")
        title = parser.get_user_input("Enter title: ")
        description = parser.get_user_input("Enter description (optional): ")

        try:
            todo = self.service.add_todo(title, description)
            renderer.display_success(f"Todo created with ID: {todo.id}")
        except ValueError as e:
            renderer.display_error(str(e))

    def handle_view_all(self):
        """Handle the 'View All Todos' command."""
        print("\n--- All Todos ---")
        todos = self.service.get_all_todos()
        renderer.display_todos(todos)

    def handle_view_by_id(self):
        """Handle the 'View Todo by ID' command."""
        print("\n--- View Todo by ID ---")
        id_str = parser.get_user_input("Enter todo ID: ")

        todo_id = parser.validate_id(id_str)
        if todo_id is None:
            renderer.display_error("Invalid ID. Please enter a positive number.")
            return

        todo = self.service.get_todo(todo_id)
        if todo is None:
            renderer.display_error(f"Todo with ID {todo_id} not found.")
        else:
            renderer.display_todo(todo)

    def handle_update(self):
        """Handle the 'Update Todo' command."""
        print("\n--- Update Todo ---")
        id_str = parser.get_user_input("Enter todo ID: ")

        todo_id = parser.validate_id(id_str)
        if todo_id is None:
            renderer.display_error("Invalid ID. Please enter a positive number.")
            return

        # Check if todo exists
        existing = self.service.get_todo(todo_id)
        if existing is None:
            renderer.display_error(f"Todo with ID {todo_id} not found.")
            return

        # Show current values
        print(f"\nCurrent title: {existing.title}")
        print(f"Current description: {existing.description if existing.description else '(none)'}")

        # Get new values
        new_title = parser.get_user_input("\nEnter new title (or press Enter to keep current): ")
        new_description = parser.get_user_input("Enter new description (or press Enter to keep current): ")

        # Use None if user pressed Enter (to keep existing values)
        title_to_use = new_title if new_title else None
        desc_to_use = new_description if new_description else None

        try:
            updated = self.service.update_todo(todo_id, title_to_use, desc_to_use)
            if updated:
                renderer.display_success(f"Todo {todo_id} updated successfully.")
            else:
                renderer.display_error(f"Todo with ID {todo_id} not found.")
        except ValueError as e:
            renderer.display_error(str(e))

    def handle_delete(self):
        """Handle the 'Delete Todo' command."""
        print("\n--- Delete Todo ---")
        id_str = parser.get_user_input("Enter todo ID: ")

        todo_id = parser.validate_id(id_str)
        if todo_id is None:
            renderer.display_error("Invalid ID. Please enter a positive number.")
            return

        success = self.service.delete_todo(todo_id)
        if success:
            renderer.display_success(f"Todo {todo_id} deleted successfully.")
        else:
            renderer.display_error(f"Todo with ID {todo_id} not found.")

    def handle_mark_complete(self):
        """Handle the 'Mark Complete' command."""
        print("\n--- Mark Todo Complete ---")
        id_str = parser.get_user_input("Enter todo ID: ")

        todo_id = parser.validate_id(id_str)
        if todo_id is None:
            renderer.display_error("Invalid ID. Please enter a positive number.")
            return

        todo = self.service.mark_complete(todo_id)
        if todo:
            renderer.display_success(f"Todo {todo_id} marked as completed.")
        else:
            renderer.display_error(f"Todo with ID {todo_id} not found.")

    def handle_mark_incomplete(self):
        """Handle the 'Mark Incomplete' command."""
        print("\n--- Mark Todo Incomplete ---")
        id_str = parser.get_user_input("Enter todo ID: ")

        todo_id = parser.validate_id(id_str)
        if todo_id is None:
            renderer.display_error("Invalid ID. Please enter a positive number.")
            return

        todo = self.service.mark_incomplete(todo_id)
        if todo:
            renderer.display_success(f"Todo {todo_id} marked as pending.")
        else:
            renderer.display_error(f"Todo with ID {todo_id} not found.")

    def handle_filter(self):
        """Handle the 'Filter by Status' command."""
        print("\n--- Filter Todos by Status ---")
        status = parser.get_user_input("Enter status (pending/completed): ").lower()

        try:
            todos = self.service.filter_by_status(status)
            print(f"\n--- {status.capitalize()} Todos ---")
            renderer.display_todos(todos)
        except ValueError as e:
            renderer.display_error(str(e))

    def handle_exit(self):
        """Handle the 'Exit' command."""
        print("\nGoodbye! All data will be lost (in-memory only).")
        self.running = False
