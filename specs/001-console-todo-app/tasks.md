---

description: "Task list for In-Memory Python Console Todo App implementation"
---

# Tasks: In-Memory Python Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/todo_service.md

**Tests**: Manual testing only for Phase I (automated tests in Phase II)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below follow single project structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project directory structure (src/, src/models/, src/services/, src/cli/, tests/manual/)
- [ ] T002 Initialize pyproject.toml with Python 3.13+ and UV configuration
- [ ] T003 [P] Create __init__.py in src/
- [ ] T004 [P] Create __init__.py in src/models/
- [ ] T005 [P] Create __init__.py in src/services/
- [ ] T006 [P] Create __init__.py in src/cli/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 Create Todo model dataclass in src/models/todo.py (frozen=True, fields: id, title, description, status)
- [ ] T008 Create TodoService class skeleton in src/services/todo_service.py (init with _todos dict and _next_id counter)
- [ ] T009 Create CLI app skeleton in src/cli/app.py (main loop structure, menu display)
- [ ] T010 [P] Create renderer module in src/cli/renderer.py (display_menu, display_todo, display_todos functions)
- [ ] T011 [P] Create parser module in src/cli/parser.py (validate_id, get_user_input functions)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Todo Management (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todos and view all existing todos

**Independent Test**: Launch app, add 2-3 todos with different titles, view list to confirm all appear with unique IDs

### Implementation for User Story 1

- [ ] T012 [US1] Implement add_todo method in src/services/todo_service.py (validate title, generate ID, create Todo, store in dict)
- [ ] T013 [US1] Implement get_all_todos method in src/services/todo_service.py (return list of all todos from dict)
- [ ] T014 [US1] Implement get_todo method in src/services/todo_service.py (lookup by ID, return Todo or None)
- [ ] T015 [US1] Implement menu display in src/cli/app.py (show 9 options: Add, View All, View by ID, Update, Delete, Mark Complete, Mark Incomplete, Filter, Exit)
- [ ] T016 [US1] Implement add command handler in src/cli/app.py (prompt for title and description, call service.add_todo, display confirmation)
- [ ] T017 [US1] Implement view all command handler in src/cli/app.py (call service.get_all_todos, use renderer to display)
- [ ] T018 [US1] Implement view by ID command handler in src/cli/app.py (prompt for ID, call service.get_todo, display result or error)
- [ ] T019 [US1] Implement display_todo function in src/cli/renderer.py (format single todo with ID, title, description, status)
- [ ] T020 [US1] Implement display_todos function in src/cli/renderer.py (format list of todos, handle empty list)
- [ ] T021 [US1] Implement display_error function in src/cli/renderer.py (format error messages)
- [ ] T022 [US1] Create main.py entry point in src/main.py (instantiate TodoService and CLI app, start main loop)
- [ ] T023 [US1] Implement exit command handler in src/cli/app.py (clean exit with goodbye message)
- [ ] T024 [US1] Add error handling for ValueError in add command (catch and display user-friendly message)
- [ ] T025 [US1] Add error handling for empty list in view all command (display "No todos found" message)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently (MVP complete!)

---

## Phase 4: User Story 2 - Delete Todos (Priority: P2)

**Goal**: Enable users to remove todos they no longer need

**Independent Test**: Add 3 todos, delete the middle one by ID, verify list shows only 2 remaining todos

### Implementation for User Story 2

- [ ] T026 [US2] Implement delete_todo method in src/services/todo_service.py (check if ID exists, remove from dict, return True/False)
- [ ] T027 [US2] Implement delete command handler in src/cli/app.py (prompt for ID, validate numeric, call service.delete_todo, display confirmation or error)
- [ ] T028 [US2] Add error handling for non-existent ID in delete command (display "Todo not found" message)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Todo Details (Priority: P3)

**Goal**: Enable users to modify title or description of existing todos

**Independent Test**: Add a todo with title "Buy milk", update it to "Buy organic milk", verify change is reflected

### Implementation for User Story 3

- [ ] T029 [US3] Implement update_todo method in src/services/todo_service.py (lookup todo, validate new title if provided, create new Todo with updates, replace in dict)
- [ ] T030 [US3] Implement update command handler in src/cli/app.py (prompt for ID, prompt for new title/description with option to keep current, call service.update_todo, display confirmation)
- [ ] T031 [US3] Add error handling for ValueError in update command (catch empty title validation, display user-friendly message)
- [ ] T032 [US3] Add error handling for non-existent ID in update command (display "Todo not found" message)

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Mark Complete/Incomplete (Priority: P4)

**Goal**: Enable users to mark todos as complete or incomplete to track progress

**Independent Test**: Add 3 todos, mark 2 as complete, verify status is correctly displayed when viewing list

### Implementation for User Story 4

- [ ] T033 [P] [US4] Implement mark_complete method in src/services/todo_service.py (lookup todo, create new Todo with status="completed", replace in dict)
- [ ] T034 [P] [US4] Implement mark_incomplete method in src/services/todo_service.py (lookup todo, create new Todo with status="pending", replace in dict)
- [ ] T035 [US4] Implement mark complete command handler in src/cli/app.py (prompt for ID, call service.mark_complete, display confirmation or error)
- [ ] T036 [US4] Implement mark incomplete command handler in src/cli/app.py (prompt for ID, call service.mark_incomplete, display confirmation or error)
- [ ] T037 [US4] Add error handling for non-existent ID in mark complete/incomplete commands (display "Todo not found" message)

**Checkpoint**: At this point, User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Filter by Status (Priority: P5)

**Goal**: Enable users to view only pending or only completed todos

**Independent Test**: Add 5 todos, mark 2 as complete, filter by "pending", verify only 3 pending items appear

### Implementation for User Story 5

- [ ] T038 [US5] Implement filter_by_status method in src/services/todo_service.py (validate status is "pending" or "completed", filter todos, return list)
- [ ] T039 [US5] Implement filter command handler in src/cli/app.py (prompt for status, validate input, call service.filter_by_status, display filtered results)
- [ ] T040 [US5] Add error handling for invalid status in filter command (display "Status must be 'pending' or 'completed'" message)
- [ ] T041 [US5] Add error handling for empty filter results (display "No todos found with status: {status}" message)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T042 [P] Create README.md in repository root (project overview, setup instructions, usage examples)
- [ ] T043 [P] Create manual test scenarios in tests/manual/test_scenarios.md (acceptance scenarios from spec.md)
- [ ] T044 Add input validation for menu choice in src/cli/app.py (validate 1-9, display "Invalid choice" for other input)
- [ ] T045 Add input validation for numeric IDs in src/cli/parser.py (validate_id function, handle non-numeric input)
- [ ] T046 Improve error messages across all CLI commands (ensure all errors are user-friendly, no stack traces)
- [ ] T047 Add empty input handling for title/description prompts (strip whitespace, handle Enter key for optional fields)
- [ ] T048 Test with 50+ todos to verify performance (ensure no noticeable degradation per SC-007)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories (independently testable)
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories (independently testable)
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories (independently testable)
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories (independently testable)

### Within Each User Story

- Foundational tasks (Phase 2) before any user story tasks
- Service methods before CLI handlers that use them
- Renderer functions before CLI handlers that use them
- Core implementation before error handling
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T003-T006)
- Foundational tasks marked [P] can run in parallel (T010-T011)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Within User Story 4: mark_complete and mark_incomplete methods can be implemented in parallel (T033-T034)
- Polish tasks marked [P] can run in parallel (T042-T043)

---

## Parallel Example: User Story 1

```bash
# After Foundational phase is complete, these can run in parallel:
# (Note: In practice, service methods should complete before CLI handlers)

# Service layer (can run in parallel):
Task T012: Implement add_todo in src/services/todo_service.py
Task T013: Implement get_all_todos in src/services/todo_service.py
Task T014: Implement get_todo in src/services/todo_service.py

# CLI layer (after service methods complete):
Task T016: Implement add command handler
Task T017: Implement view all command handler
Task T018: Implement view by ID command handler
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T006)
2. Complete Phase 2: Foundational (T007-T011) - CRITICAL - blocks all stories
3. Complete Phase 3: User Story 1 (T012-T025)
4. **STOP and VALIDATE**: Test User Story 1 independently
   - Launch app
   - Add 3 todos with different titles
   - View all todos
   - View specific todo by ID
   - Verify empty list message
   - Verify error handling for empty title
   - Exit cleanly
5. MVP is now complete and usable!

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (T012-T025) → Test independently → MVP deployed!
3. Add User Story 2 (T026-T028) → Test independently → Delete functionality added
4. Add User Story 3 (T029-T032) → Test independently → Update functionality added
5. Add User Story 4 (T033-T037) → Test independently → Status tracking added
6. Add User Story 5 (T038-T041) → Test independently → Filtering added
7. Add Polish (T042-T048) → Final refinements
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T011)
2. Once Foundational is done:
   - Developer A: User Story 1 (T012-T025)
   - Developer B: User Story 2 (T026-T028) + User Story 3 (T029-T032)
   - Developer C: User Story 4 (T033-T037) + User Story 5 (T038-T041)
3. Stories complete and integrate independently
4. Team completes Polish together (T042-T048)

---

## Task Count Summary

- **Phase 1 (Setup)**: 6 tasks
- **Phase 2 (Foundational)**: 5 tasks
- **Phase 3 (User Story 1 - MVP)**: 14 tasks
- **Phase 4 (User Story 2)**: 3 tasks
- **Phase 5 (User Story 3)**: 4 tasks
- **Phase 6 (User Story 4)**: 5 tasks
- **Phase 7 (User Story 5)**: 4 tasks
- **Phase 8 (Polish)**: 7 tasks

**Total**: 48 tasks

**Parallel Opportunities**: 8 tasks can run in parallel (marked with [P])

**MVP Scope**: Phases 1-3 (25 tasks) deliver a fully functional todo app with add and view capabilities

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- No automated tests in Phase I (manual testing only per constitution)
- Commit after each phase or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Validation Checklist

✅ All tasks follow format: `- [ ] [TaskID] [P?] [Story?] Description with file path`
✅ Tasks organized by user story (5 user stories mapped)
✅ Each user story has independent test criteria
✅ Foundational phase blocks all user stories (correct dependency)
✅ User stories can be implemented in parallel after Foundational
✅ File paths included in all implementation tasks
✅ MVP scope clearly identified (User Story 1)
✅ Parallel opportunities marked with [P]
✅ No tests generated (manual testing only for Phase I)
✅ Total task count: 48 tasks
