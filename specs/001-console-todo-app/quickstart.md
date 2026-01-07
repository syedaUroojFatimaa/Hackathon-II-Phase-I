# Quickstart: In-Memory Python Console Todo App

**Feature**: 001-console-todo-app
**Date**: 2026-01-06
**Phase**: Phase I - Console Application

## Prerequisites

- **Python 3.13+** installed on your system
- **UV** package manager (recommended) or pip
- Terminal/Console access

## Installation

### Option 1: Using UV (Recommended)

1. **Install UV** (if not already installed):
   ```bash
   pip install uv
   ```

2. **Clone/Navigate to project**:
   ```bash
   cd TODO-APP
   ```

3. **Run the application**:
   ```bash
   uv run src/main.py
   ```

   UV will automatically:
   - Create a virtual environment
   - Install dependencies (none for Phase I)
   - Run the application

### Option 2: Using Python directly

1. **Navigate to project**:
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

## First Run

When you launch the application, you'll see an interactive menu:

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

## Basic Usage

### Adding Your First Todo

1. Select option `1` (Add Todo)
2. Enter a title when prompted: `Buy groceries`
3. Enter a description (optional): `Milk, eggs, bread`
4. The app confirms: `Todo created with ID: 1`

### Viewing All Todos

1. Select option `2` (View All Todos)
2. The app displays all todos with their details:
   ```
   ID: 1
   Title: Buy groceries
   Description: Milk, eggs, bread
   Status: pending
   ---
   ```

### Updating a Todo

1. Select option `4` (Update Todo)
2. Enter the ID of the todo to update: `1`
3. Enter new title (or press Enter to keep current): `Buy organic groceries`
4. Enter new description (or press Enter to keep current): `Organic milk, free-range eggs, whole grain bread`
5. The app confirms the update

### Marking a Todo Complete

1. Select option `6` (Mark Complete)
2. Enter the ID of the todo: `1`
3. The app confirms: `Todo 1 marked as completed`

### Filtering Todos

1. Select option `8` (Filter by Status)
2. Enter status to filter by: `pending` or `completed`
3. The app displays only todos matching that status

### Deleting a Todo

1. Select option `5` (Delete Todo)
2. Enter the ID of the todo to delete: `1`
3. The app confirms: `Todo 1 deleted`

### Exiting the Application

1. Select option `9` (Exit)
2. The app closes gracefully
3. **Note**: All data is lost when you exit (in-memory only)

## Common Workflows

### Daily Task Management

```
1. Launch app
2. Add todos for the day (option 1)
3. View all todos (option 2)
4. Mark completed tasks (option 6)
5. Filter to see remaining work (option 8 → "pending")
6. Exit when done (option 9)
```

### Quick Todo Check

```
1. Launch app
2. View all todos (option 2)
3. Exit (option 9)
```

### Cleaning Up Completed Tasks

```
1. Launch app
2. Filter by completed (option 8 → "completed")
3. Note IDs of completed todos
4. Delete each completed todo (option 5)
5. Exit (option 9)
```

## Tips & Tricks

### Efficient Navigation
- Menu options are numbered 1-9 for quick selection
- Just type the number and press Enter

### Empty Descriptions
- Descriptions are optional
- Press Enter without typing to leave description empty

### Viewing Specific Todos
- Use option 3 (View Todo by ID) to see details of a single todo
- Faster than viewing all todos when you know the ID

### Status Management
- Use option 7 (Mark Incomplete) to undo completion
- Useful if you accidentally marked something complete

### Filtering
- Filter by "pending" to see what's left to do
- Filter by "completed" to review what you've accomplished

## Error Messages

### "Title cannot be empty"
- **Cause**: You tried to add or update a todo with no title
- **Solution**: Provide a non-empty title

### "Todo not found"
- **Cause**: You referenced an ID that doesn't exist
- **Solution**: Use option 2 to view all todos and their IDs

### "Invalid choice"
- **Cause**: You entered something other than 1-9
- **Solution**: Enter a number between 1 and 9

### "Invalid status"
- **Cause**: You entered something other than "pending" or "completed" when filtering
- **Solution**: Enter exactly "pending" or "completed" (case-sensitive)

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

## Troubleshooting

### "Python not found"
- **Solution**: Install Python 3.13+ from python.org
- **Verify**: Run `python --version` or `python3 --version`

### "UV not found"
- **Solution**: Install UV with `pip install uv`
- **Alternative**: Use Python directly (Option 2 above)

### "Module not found" errors
- **Cause**: Running from wrong directory
- **Solution**: Make sure you're in the TODO-APP root directory
- **Verify**: Run `ls src/main.py` (should exist)

### Application crashes
- **Cause**: Unexpected input or bug
- **Solution**: Restart the application
- **Report**: Note what you did before the crash for bug reporting

## Performance

### Expected Performance
- **Startup**: Instant (<1 second)
- **Operations**: Instant (<100ms)
- **Capacity**: Handles 1000+ todos without slowdown

### If Performance Degrades
- **Unlikely in Phase I**: Dict-based storage is very fast
- **If it happens**: Restart the application (clears memory)

## Data Location

### Phase I: In-Memory Only
- **Storage**: RAM only (no files created)
- **Location**: N/A (nothing written to disk)
- **Backup**: Not possible (data is ephemeral)

### Phase II: Database
- **Storage**: PostgreSQL database (Neon)
- **Location**: Cloud-hosted
- **Backup**: Automatic database backups

## Next Steps

### After Mastering Phase I
1. Provide feedback on usability
2. Request features for Phase II
3. Test edge cases and report bugs

### Phase II Preview
- Persistent storage (database)
- Web interface (Next.js frontend)
- RESTful API (FastAPI backend)
- User authentication
- Due dates and priorities

## Support

### Getting Help
- Check error messages (they're designed to be helpful)
- Review this quickstart guide
- Check the feature specification: `specs/001-console-todo-app/spec.md`

### Reporting Issues
- Note the exact steps to reproduce
- Include the error message (if any)
- Describe expected vs actual behavior

## Examples

### Example Session

```
$ uv run src/main.py

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

Enter choice: 1
Enter title: Buy groceries
Enter description (optional): Milk, eggs, bread
Todo created with ID: 1

Enter choice: 1
Enter title: Call mom
Enter description (optional):
Todo created with ID: 2

Enter choice: 2
ID: 1
Title: Buy groceries
Description: Milk, eggs, bread
Status: pending
---
ID: 2
Title: Call mom
Description:
Status: pending
---

Enter choice: 6
Enter todo ID: 2
Todo 2 marked as completed

Enter choice: 8
Enter status (pending/completed): pending
ID: 1
Title: Buy groceries
Description: Milk, eggs, bread
Status: pending
---

Enter choice: 9
Goodbye!
```

## Summary

**Phase I Console Todo App** is a simple, fast, in-memory task manager perfect for:
- Learning the application workflow
- Managing tasks during a single work session
- Testing and providing feedback for future phases

**Remember**: Data is not saved between sessions. Phase II will add persistence.

---

**Ready to start?** Run `uv run src/main.py` and begin managing your todos!
