# Research: In-Memory Python Console Todo App

**Feature**: 001-console-todo-app
**Date**: 2026-01-06
**Phase**: Phase 0 - Architecture Research

## Purpose

Document architectural decisions, technology choices, and design patterns for the Phase I console todo application. All decisions must align with Phase I constitution constraints: in-memory only, console-based, deterministic, no external dependencies.

## Research Questions

### Q1: How should we represent the Todo entity?

**Options Evaluated**:
1. Plain Python dict
2. NamedTuple
3. Dataclass
4. Pydantic model

**Decision**: Python dataclass with `frozen=True`

**Rationale**:
- Built-in to Python 3.7+ (no external dependencies)
- Type-safe with type hints
- Immutable when frozen (prevents accidental mutations)
- Clean syntax with automatic `__init__`, `__repr__`, `__eq__`
- Better IDE support than plain dicts
- No runtime overhead compared to NamedTuple

**Alternatives Rejected**:
- Plain dict: No type safety, easy to make mistakes with key names
- NamedTuple: Less flexible for future extensions, no default values
- Pydantic: External dependency (violates Phase I constraints)

**Code Pattern**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Todo:
    id: int
    title: str
    description: str
    status: str  # "pending" | "completed"
```

---

### Q2: What data structure should we use for in-memory storage?

**Options Evaluated**:
1. List of todos
2. Dict with ID as key
3. SQLite in-memory database

**Decision**: Dict with ID as key (`dict[int, Todo]`)

**Rationale**:
- O(1) lookups by ID (vs O(n) for list)
- Simple and built-in (no dependencies)
- Sufficient for 1000 todos (spec requirement)
- Easy to implement all CRUD operations
- Memory efficient for Phase I scale

**Alternatives Rejected**:
- List: O(n) lookups would require linear search for every get/update/delete operation
- SQLite in-memory: Overkill for Phase I, adds complexity, not needed until Phase II

**Performance Analysis**:
- Dict lookup: O(1) - constant time regardless of size
- List lookup: O(n) - scales linearly with number of todos
- For 1000 todos: dict ~1μs, list ~500μs average (assuming mid-list lookup)

---

### Q3: How should we structure the CLI interface?

**Options Evaluated**:
1. Argument-based CLI (e.g., `todo add "Buy milk"`)
2. Interactive REPL with menu
3. TUI (Text User Interface) with curses/rich

**Decision**: Interactive REPL with numbered menu

**Rationale**:
- Matches spec assumption: "interactive console program"
- Better UX for multiple operations in one session
- No need to remember command syntax
- Easier to discover features
- No external dependencies (vs TUI libraries)

**Alternatives Rejected**:
- Argument-based: Less interactive, requires remembering commands, not aligned with spec
- TUI library: External dependency (violates Phase I), overkill for simple operations

**Menu Structure**:
```
=== Todo App ===
1. Add Todo
2. View All Todos
3. View Todo by ID
4. Update Todo
5. Delete Todo
6. Mark Complete
7. Mark Incomplete
8. Filter by Status
9. Exit

Enter choice:
```

---

### Q4: How should we generate unique IDs?

**Options Evaluated**:
1. Sequential integers starting from 1
2. UUIDs
3. Random integers
4. Timestamp-based IDs

**Decision**: Sequential integers starting from 1

**Rationale**:
- Simple and predictable (deterministic - Phase I requirement)
- Human-readable (easy to reference in CLI)
- Matches spec assumption: "Todo IDs will be sequential integers starting from 1"
- No external dependencies
- Sufficient uniqueness for single-session, single-user application

**Alternatives Rejected**:
- UUIDs: Overkill, not human-readable, harder to type in CLI
- Random integers: Non-deterministic (violates Phase I constraints)
- Timestamp-based: Non-deterministic, potential collisions if operations are fast

**Implementation Pattern**:
```python
class TodoService:
    def __init__(self):
        self._todos: dict[int, Todo] = {}
        self._next_id: int = 1

    def add_todo(self, title: str, description: str) -> Todo:
        todo = Todo(id=self._next_id, title=title, description=description, status="pending")
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo
```

---

### Q5: How should we handle errors and validation?

**Options Evaluated**:
1. Exceptions with try/except
2. Return None/False for errors
3. Result type (Ok/Err pattern)

**Decision**: Hybrid approach - exceptions for validation, None/False for not-found cases

**Rationale**:
- Exceptions for validation errors (empty title) - clear error messages
- None/False for not-found cases (ID doesn't exist) - simpler control flow
- Pythonic and idiomatic
- No external dependencies

**Validation Strategy**:
- CLI layer: Validate input format (e.g., ID is numeric)
- Service layer: Validate business rules (e.g., title non-empty)
- Display user-friendly error messages (no stack traces)

**Error Handling Pattern**:
```python
# Validation error - raise exception
def add_todo(self, title: str, description: str) -> Todo:
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")
    # ... create todo

# Not found - return None
def get_todo(self, id: int) -> Todo | None:
    return self._todos.get(id)
```

---

## Architecture Pattern

**Selected Pattern**: Layered Architecture (4 layers)

**Layers**:
1. **CLI Layer**: User interaction (input/output)
2. **Application Layer**: Business logic and orchestration
3. **Domain Layer**: Entity definitions
4. **Storage Layer**: In-memory data management

**Rationale**:
- Clear separation of concerns (Constitution Principle VI)
- Easy to test each layer independently (Phase II)
- Supports future evolution (Phase II will add persistence layer)
- Simple enough for Phase I scope
- No framework dependencies

**Layer Communication**:
- CLI → Application (calls service methods)
- Application → Domain (creates/manipulates entities)
- Application → Storage (manages dict)
- No circular dependencies

---

## Best Practices Applied

### Python 3.13+ Features
- Type hints for all function signatures
- Union types with `|` operator (e.g., `Todo | None`)
- Dataclasses for entity definitions
- F-strings for output formatting

### Code Organization
- One class per file
- Clear module structure (models/, services/, cli/)
- Minimal coupling between layers
- No global state (except within TodoService instance)

### Determinism
- No random number generation
- No external API calls
- No file I/O
- No timestamps (except for display purposes)
- Sequential ID generation

### Error Handling
- Validate early (fail fast)
- User-friendly error messages
- No crashes on invalid input
- Graceful degradation

---

## Technology Stack Summary

**Language**: Python 3.13+
**Dependencies**: None (Python standard library only)
**Storage**: In-memory dict
**CLI**: Built-in input()/print()
**Testing**: Manual (Phase I), pytest (Phase II)

**Justification**: All choices align with Phase I constitution constraints and require zero external dependencies.

---

## Open Questions

None - all architectural decisions resolved.

---

## References

- Python dataclasses documentation: https://docs.python.org/3/library/dataclasses.html
- Python dict performance: O(1) average case for get/set operations
- Phase I Constitution: `.specify/memory/constitution.md`
- Feature Specification: `specs/001-console-todo-app/spec.md`
