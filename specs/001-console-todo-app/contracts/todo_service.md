# TodoService Contract

**Feature**: 001-console-todo-app
**Date**: 2026-01-06
**Type**: Internal API Contract

## Purpose

Define the interface contract for the TodoService class, which provides all business logic and data management operations for the todo application. This contract serves as the boundary between the CLI layer and the application/storage layers.

## Service Interface

### Class: TodoService

**Responsibility**: Manage todo lifecycle (CRUD operations), enforce business rules, maintain in-memory storage.

**State**:
- `_todos: dict[int, Todo]` - In-memory storage of all todos
- `_next_id: int` - Counter for sequential ID generation

---

## Methods

### add_todo

**Signature**:
```python
def add_todo(self, title: str, description: str = "") -> Todo
```

**Purpose**: Create a new todo with auto-generated ID and default status "pending".

**Parameters**:
- `title` (str, required): Task description, must be non-empty after stripping whitespace
- `description` (str, optional): Additional details, defaults to empty string

**Returns**: `Todo` - The newly created todo with assigned ID

**Raises**:
- `ValueError` - If title is empty or whitespace-only

**Behavior**:
1. Strip whitespace from title
2. Validate title is non-empty
3. Generate next sequential ID
4. Create Todo instance with status="pending"
5. Store in `_todos` dict
6. Increment `_next_id`
7. Return created Todo

**Example**:
```python
service = TodoService()
todo = service.add_todo("Buy groceries", "Milk, eggs, bread")
# Returns: Todo(id=1, title="Buy groceries", description="Milk, eggs, bread", status="pending")
```

---

### get_todo

**Signature**:
```python
def get_todo(self, id: int) -> Todo | None
```

**Purpose**: Retrieve a single todo by its ID.

**Parameters**:
- `id` (int, required): The unique identifier of the todo

**Returns**:
- `Todo` - If todo with given ID exists
- `None` - If todo with given ID does not exist

**Raises**: None

**Behavior**:
1. Look up todo in `_todos` dict by ID
2. Return todo if found, None otherwise

**Example**:
```python
todo = service.get_todo(1)
# Returns: Todo(id=1, ...) or None
```

---

### get_all_todos

**Signature**:
```python
def get_all_todos(self) -> list[Todo]
```

**Purpose**: Retrieve all todos in the system.

**Parameters**: None

**Returns**: `list[Todo]` - List of all todos, empty list if no todos exist

**Raises**: None

**Behavior**:
1. Extract all values from `_todos` dict
2. Convert to list
3. Return list (order not guaranteed)

**Example**:
```python
todos = service.get_all_todos()
# Returns: [Todo(id=1, ...), Todo(id=2, ...), ...]
```

---

### update_todo

**Signature**:
```python
def update_todo(self, id: int, title: str | None = None, description: str | None = None) -> Todo | None
```

**Purpose**: Update the title and/or description of an existing todo.

**Parameters**:
- `id` (int, required): The unique identifier of the todo to update
- `title` (str | None, optional): New title, or None to keep existing
- `description` (str | None, optional): New description, or None to keep existing

**Returns**:
- `Todo` - The updated todo if ID exists and update succeeds
- `None` - If todo with given ID does not exist

**Raises**:
- `ValueError` - If new title is provided but is empty or whitespace-only

**Behavior**:
1. Look up existing todo by ID
2. Return None if not found
3. If title provided, validate non-empty after stripping
4. Create new Todo with updated values (keep status unchanged)
5. Replace old todo in `_todos` dict
6. Return updated Todo

**Example**:
```python
updated = service.update_todo(1, title="Buy organic groceries")
# Returns: Todo(id=1, title="Buy organic groceries", description="Milk, eggs, bread", status="pending")
```

---

### delete_todo

**Signature**:
```python
def delete_todo(self, id: int) -> bool
```

**Purpose**: Remove a todo from the system.

**Parameters**:
- `id` (int, required): The unique identifier of the todo to delete

**Returns**:
- `True` - If todo was found and deleted
- `False` - If todo with given ID does not exist

**Raises**: None

**Behavior**:
1. Check if todo exists in `_todos` dict
2. If exists, remove from dict and return True
3. If not exists, return False

**Example**:
```python
success = service.delete_todo(1)
# Returns: True if deleted, False if not found
```

---

### mark_complete

**Signature**:
```python
def mark_complete(self, id: int) -> Todo | None
```

**Purpose**: Mark a todo as completed.

**Parameters**:
- `id` (int, required): The unique identifier of the todo to mark complete

**Returns**:
- `Todo` - The updated todo with status="completed" if ID exists
- `None` - If todo with given ID does not exist

**Raises**: None

**Behavior**:
1. Look up existing todo by ID
2. Return None if not found
3. Create new Todo with status="completed" (keep other fields unchanged)
4. Replace old todo in `_todos` dict
5. Return updated Todo

**Idempotency**: Calling this on an already completed todo is safe (no error, returns todo with status="completed")

**Example**:
```python
completed = service.mark_complete(1)
# Returns: Todo(id=1, title="Buy groceries", description="...", status="completed")
```

---

### mark_incomplete

**Signature**:
```python
def mark_incomplete(self, id: int) -> Todo | None
```

**Purpose**: Mark a todo as pending (undo completion).

**Parameters**:
- `id` (int, required): The unique identifier of the todo to mark incomplete

**Returns**:
- `Todo` - The updated todo with status="pending" if ID exists
- `None` - If todo with given ID does not exist

**Raises**: None

**Behavior**:
1. Look up existing todo by ID
2. Return None if not found
3. Create new Todo with status="pending" (keep other fields unchanged)
4. Replace old todo in `_todos` dict
5. Return updated Todo

**Idempotency**: Calling this on an already pending todo is safe (no error, returns todo with status="pending")

**Example**:
```python
pending = service.mark_incomplete(1)
# Returns: Todo(id=1, title="Buy groceries", description="...", status="pending")
```

---

### filter_by_status

**Signature**:
```python
def filter_by_status(self, status: str) -> list[Todo]
```

**Purpose**: Retrieve all todos with a specific status.

**Parameters**:
- `status` (str, required): The status to filter by ("pending" or "completed")

**Returns**: `list[Todo]` - List of todos matching the status, empty list if none match

**Raises**:
- `ValueError` - If status is not "pending" or "completed"

**Behavior**:
1. Validate status is "pending" or "completed"
2. Filter all todos by status
3. Return filtered list

**Example**:
```python
pending_todos = service.filter_by_status("pending")
# Returns: [Todo(id=1, status="pending"), Todo(id=3, status="pending"), ...]
```

---

## Error Handling

### Validation Errors

**When**: Business rule violations (empty title, invalid status)
**How**: Raise `ValueError` with descriptive message
**Handled By**: CLI layer catches and displays user-friendly message

### Not Found Errors

**When**: Operation on non-existent ID
**How**: Return `None` or `False` (not an exception)
**Handled By**: CLI layer checks return value and displays appropriate message

### No Errors For

- Idempotent operations (mark complete when already complete)
- Empty list results (no todos, no matches)
- Valid operations on empty state

---

## Invariants

**TodoService guarantees**:
1. IDs are always unique within a session
2. IDs are always sequential starting from 1
3. IDs are never reused (even after deletion)
4. All todos have valid status ("pending" or "completed")
5. All todos have non-empty titles
6. Storage is always consistent (no partial updates)
7. Operations are deterministic (same input → same output)

---

## Usage Example

```python
from services.todo_service import TodoService

# Initialize service
service = TodoService()

# Add todos
todo1 = service.add_todo("Buy groceries", "Milk, eggs, bread")
todo2 = service.add_todo("Call mom")

# View all
all_todos = service.get_all_todos()
print(f"Total todos: {len(all_todos)}")

# Update
updated = service.update_todo(1, title="Buy organic groceries")

# Mark complete
completed = service.mark_complete(1)

# Filter
pending = service.filter_by_status("pending")
print(f"Pending todos: {len(pending)}")

# Delete
success = service.delete_todo(2)
```

---

## Testing Considerations

**Unit Tests** (Phase II):
- Test each method with valid inputs
- Test validation errors (empty title, invalid status)
- Test not-found cases (non-existent IDs)
- Test idempotency (mark complete twice)
- Test edge cases (empty list, single todo, 1000 todos)

**Manual Tests** (Phase I):
- Follow acceptance scenarios from spec.md
- Verify error messages are user-friendly
- Verify data consistency across operations

---

## References

- Data Model: `specs/001-console-todo-app/data-model.md`
- Feature Specification: `specs/001-console-todo-app/spec.md`
- Implementation Plan: `specs/001-console-todo-app/plan.md`
