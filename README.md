# Todo App - Phase I: In-Memory Python Console Application

A simple, deterministic command-line todo application built with Python 3.13+. This is Phase I of a multi-phase evolution toward a full-stack, AI-powered, cloud-native system.

## Features

- ✅ **Add Todos**: Create new tasks with title and optional description
- ✅ **View Todos**: Display all todos or view a specific todo by ID
- ✅ **Update Todos**: Modify title or description of existing todos
- ✅ **Delete Todos**: Remove todos you no longer need
- ✅ **Mark Complete/Incomplete**: Track progress by marking todos as complete or pending
- ✅ **Filter by Status**: View only pending or completed todos
- ✅ **In-Memory Storage**: All data stored in memory (no persistence between sessions)
- ✅ **Deterministic**: Fully predictable behavior with sequential ID generation

## Requirements

- **Python 3.13+** installed on your system
- **UV** package manager (recommended) or pip

## Installation

### Option 1: Using UV (Recommended)

1. **Install UV** (if not already installed):
   ```bash
   pip install uv
   ```

2. **Navigate to project directory**:
   ```bash
   cd TODO-APP
   ```

3. **Run the application**:
   ```bash
   uv run src/main.py
   ```

### Option 2: Using Python directly

1. **Navigate to project directory**:
   ```bash
   cd TODO-APP
   ```

2. **Run the application**:
   ```bash
   python src/main.py
   ```

   Or on some systems:
   ```bash
   python3 src/main.py
   ```

## Usage

When you launch the application, you'll see an interactive menu:

```
========================================
         Todo App - Phase I
========================================
1. Add Todo
2. View All Todos
3. View Todo by ID
4. Update Todo
5. Delete Todo
6. Mark Complete
7. Mark Incomplete
8. Filter by Status
9. Exit
========================================
```

### Quick Start Example

```bash
$ uv run src/main.py

Welcome to Todo App!

========================================
         Todo App - Phase I
========================================
1. Add Todo
2. View All Todos
...
9. Exit
========================================

Enter choice (1-9): 1

--- Add Todo ---
Enter title: Buy groceries
Enter description (optional): Milk, eggs, bread

✅ Todo created with ID: 1

Enter choice (1-9): 1

--- Add Todo ---
Enter title: Call mom
Enter description (optional):

✅ Todo created with ID: 2

Enter choice (1-9): 2

--- All Todos ---

Found 2 todo(s):

ID: 1
Title: Buy groceries
Description: Milk, eggs, bread
Status: pending
----------------------------------------

ID: 2
Title: Call mom
Description: (none)
Status: pending
----------------------------------------

Enter choice (1-9): 6

--- Mark Todo Complete ---
Enter todo ID: 2

✅ Todo 2 marked as completed.

Enter choice (1-9): 8

--- Filter Todos by Status ---
Enter status (pending/completed): pending

--- Pending Todos ---

Found 1 todo(s):

ID: 1
Title: Buy groceries
Description: Milk, eggs, bread
Status: pending
----------------------------------------

Enter choice (1-9): 9

Goodbye! All data will be lost (in-memory only).
```

## Architecture

The application follows a clean layered architecture:

```
CLI Layer (src/cli/)
    ↓
Application Layer (src/services/)
    ↓
Domain Layer (src/models/)
    ↓
Storage Layer (in-memory dict)
```

### Project Structure

```
TODO-APP/
├── src/
│   ├── models/
│   │   └── todo.py          # Todo entity (dataclass)
│   ├── services/
│   │   └── todo_service.py  # Business logic and storage
│   ├── cli/
│   │   ├── app.py           # Main CLI loop and command routing
│   │   ├── parser.py        # Input validation
│   │   └── renderer.py      # Output formatting
│   └── main.py              # Application entry point
├── tests/
│   └── manual/
│       └── test_scenarios.md # Manual test scenarios
├── specs/
│   └── 001-console-todo-app/ # Design documents
├── pyproject.toml           # Project configuration
└── README.md                # This file
```

## Key Design Decisions

- **Dataclass for Todo**: Immutable, type-safe entity with frozen=True
- **Dict Storage**: O(1) lookups by ID, sufficient for 1000+ todos
- **Interactive REPL**: Better UX than single-command execution
- **Sequential IDs**: Simple, predictable, human-readable (starts at 1)
- **No External Dependencies**: Python standard library only

## Limitations (Phase I)

### No Persistence
- **What it means**: All todos are lost when you exit the app
- **Workaround**: Keep the app running during your work session
- **Future**: Phase II will add database persistence

### No Multi-User Support
- **What it means**: Only one person can use the app at a time
- **Workaround**: Each user runs their own instance
- **Future**: Phase II will add user accounts

### No Undo
- **What it means**: Deletions are permanent (for the session)
- **Workaround**: Be careful when deleting
- **Future**: Phase III may add undo functionality

### No Due Dates or Priorities
- **What it means**: All todos are treated equally
- **Workaround**: Use title prefixes like "[URGENT]" or "[Today]"
- **Future**: Phase II will add due dates and priorities

## Testing

Phase I uses manual testing. See `tests/manual/test_scenarios.md` for acceptance test scenarios.

To test the application:

1. Launch the app: `uv run src/main.py`
2. Follow the test scenarios in `tests/manual/test_scenarios.md`
3. Verify all acceptance criteria are met

## Error Handling

The application provides user-friendly error messages for common issues:

- **"Title cannot be empty"**: You tried to add/update a todo with no title
- **"Todo not found"**: You referenced an ID that doesn't exist
- **"Invalid choice"**: You entered something other than 1-9
- **"Invalid ID"**: You entered a non-numeric or negative ID
- **"Status must be 'pending' or 'completed'"**: Invalid status for filtering

## Performance

- **Startup**: Instant (<1 second)
- **Operations**: Instant (<100ms)
- **Capacity**: Handles 1000+ todos without slowdown

## Development

### Constitution Compliance

This implementation follows the project constitution:
- ✅ **Spec-First Development**: All features derived from spec.md
- ✅ **Phase Isolation**: Phase I only - no web, no database, no AI
- ✅ **Traceability**: All features map to functional requirements
- ✅ **Deterministic**: Fully predictable behavior
- ✅ **Technology Stack Discipline**: Python 3.13+ only
- ✅ **Separation of Concerns**: Clear layer boundaries

### Design Documents

All design documents are in `specs/001-console-todo-app/`:
- `spec.md` - Feature specification with user stories
- `plan.md` - Implementation plan with architecture
- `data-model.md` - Entity definitions and validation rules
- `contracts/todo_service.md` - TodoService interface contract
- `tasks.md` - Implementation task breakdown
- `quickstart.md` - Detailed usage guide

## Next Steps (Future Phases)

### Phase II - Full-Stack Web Application
- Persistent storage (PostgreSQL via Neon)
- Web interface (Next.js frontend)
- RESTful API (FastAPI backend)
- User authentication
- Due dates and priorities

### Phase III - AI-Powered Todo Chatbot
- Natural language interaction
- OpenAI ChatKit integration
- Agents SDK for task automation
- MCP SDK for tool integration

### Phase IV - Local Kubernetes Deployment
- Docker containerization
- Minikube orchestration
- Helm charts
- kubectl-ai tooling

### Phase V - Advanced Cloud Deployment
- DigitalOcean DOKS
- Kafka event streaming
- Dapr application runtime
- Infrastructure as code

## Contributing

This is a learning project demonstrating spec-driven development. Contributions should:
1. Start with a spec update
2. Follow the constitution principles
3. Maintain phase isolation
4. Include manual test scenarios

## License

This project is for educational purposes.

## Support

For issues or questions:
- Check the quickstart guide: `specs/001-console-todo-app/quickstart.md`
- Review the specification: `specs/001-console-todo-app/spec.md`
- Check error messages (they're designed to be helpful)

---

**Phase I Status**: ✅ Complete and ready for use!

**Try it now**: `uv run src/main.py`
# Hackathon-II-Phase-I
