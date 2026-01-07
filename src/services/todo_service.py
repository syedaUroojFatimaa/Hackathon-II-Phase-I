"""TodoService - Business logic and in-memory storage for todos"""
from src.models.todo import Todo


class TodoService:
    """Manages todo lifecycle (CRUD operations), enforces business rules, maintains in-memory storage.

    State:
        _todos: In-memory storage of all todos (dict[int, Todo])
        _next_id: Counter for sequential ID generation
    """

    def __init__(self):
        """Initialize TodoService with empty storage and ID counter starting at 1."""
        self._todos: dict[int, Todo] = {}
        self._next_id: int = 1

    def add_todo(self, title: str, description: str = "") -> Todo:
        """Create a new todo with auto-generated ID and default status 'pending'.

        Args:
            title: Task description (required, must be non-empty after stripping)
            description: Additional details (optional, defaults to empty string)

        Returns:
            The newly created Todo with assigned ID

        Raises:
            ValueError: If title is empty or whitespace-only
        """
        # Strip whitespace and validate
        title = title.strip()
        if not title:
            raise ValueError("Title cannot be empty")

        # Create todo with next ID
        todo = Todo(
            id=self._next_id,
            title=title,
            description=description,
            status="pending"
        )

        # Store and increment ID
        self._todos[self._next_id] = todo
        self._next_id += 1

        return todo

    def get_todo(self, id: int) -> Todo | None:
        """Retrieve a single todo by its ID.

        Args:
            id: The unique identifier of the todo

        Returns:
            Todo if found, None otherwise
        """
        return self._todos.get(id)

    def get_all_todos(self) -> list[Todo]:
        """Retrieve all todos in the system.

        Returns:
            List of all todos (empty list if no todos exist)
        """
        return list(self._todos.values())

    def update_todo(self, id: int, title: str | None = None, description: str | None = None) -> Todo | None:
        """Update the title and/or description of an existing todo.

        Args:
            id: The unique identifier of the todo to update
            title: New title (or None to keep existing)
            description: New description (or None to keep existing)

        Returns:
            Updated Todo if ID exists, None otherwise

        Raises:
            ValueError: If new title is provided but is empty or whitespace-only
        """
        # Look up existing todo
        existing = self._todos.get(id)
        if existing is None:
            return None

        # Validate new title if provided
        if title is not None:
            title = title.strip()
            if not title:
                raise ValueError("Title cannot be empty")
        else:
            title = existing.title

        # Use new description if provided, otherwise keep existing
        if description is None:
            description = existing.description

        # Create new Todo with updated values
        updated = Todo(
            id=existing.id,
            title=title,
            description=description,
            status=existing.status
        )

        # Replace in storage
        self._todos[id] = updated
        return updated

    def delete_todo(self, id: int) -> bool:
        """Remove a todo from the system.

        Args:
            id: The unique identifier of the todo to delete

        Returns:
            True if todo was found and deleted, False otherwise
        """
        if id in self._todos:
            del self._todos[id]
            return True
        return False

    def mark_complete(self, id: int) -> Todo | None:
        """Mark a todo as completed.

        Args:
            id: The unique identifier of the todo to mark complete

        Returns:
            Updated Todo with status="completed" if ID exists, None otherwise
        """
        existing = self._todos.get(id)
        if existing is None:
            return None

        # Create new Todo with status="completed"
        completed = Todo(
            id=existing.id,
            title=existing.title,
            description=existing.description,
            status="completed"
        )

        # Replace in storage
        self._todos[id] = completed
        return completed

    def mark_incomplete(self, id: int) -> Todo | None:
        """Mark a todo as pending (undo completion).

        Args:
            id: The unique identifier of the todo to mark incomplete

        Returns:
            Updated Todo with status="pending" if ID exists, None otherwise
        """
        existing = self._todos.get(id)
        if existing is None:
            return None

        # Create new Todo with status="pending"
        pending = Todo(
            id=existing.id,
            title=existing.title,
            description=existing.description,
            status="pending"
        )

        # Replace in storage
        self._todos[id] = pending
        return pending

    def filter_by_status(self, status: str) -> list[Todo]:
        """Retrieve all todos with a specific status.

        Args:
            status: The status to filter by ("pending" or "completed")

        Returns:
            List of todos matching the status (empty list if none match)

        Raises:
            ValueError: If status is not "pending" or "completed"
        """
        if status not in ("pending", "completed"):
            raise ValueError("Status must be 'pending' or 'completed'")

        return [todo for todo in self._todos.values() if todo.status == status]
