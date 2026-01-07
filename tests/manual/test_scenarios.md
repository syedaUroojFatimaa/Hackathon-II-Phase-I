# Manual Test Scenarios - Phase I Console Todo App

**Purpose**: Validate all acceptance criteria from spec.md through manual testing

**Date**: 2026-01-06

**Prerequisites**: Application running via `uv run src/main.py`

---

## Test Scenario 1: Basic Todo Management (User Story 1 - MVP)

**Goal**: Verify users can add and view todos

### Test Case 1.1: Add Todo with Title and Description

**Steps**:
1. Launch app: `uv run src/main.py`
2. Select option 1 (Add Todo)
3. Enter title: "Buy groceries"
4. Enter description: "Milk, eggs, bread"

**Expected Result**:
- ✅ System confirms: "Todo created with ID: 1"
- ✅ ID is assigned (should be 1 for first todo)

**Acceptance Criteria**: FR-001, FR-002, FR-011

---

### Test Case 1.2: View All Todos

**Steps**:
1. Add 3 todos with different titles
2. Select option 2 (View All Todos)

**Expected Result**:
- ✅ System displays all 3 todos
- ✅ Each todo shows: ID, title, description, status
- ✅ All todos have status "pending"

**Acceptance Criteria**: FR-004, FR-013

---

### Test Case 1.3: View Empty List

**Steps**:
1. Launch fresh app (no todos added)
2. Select option 2 (View All Todos)

**Expected Result**:
- ✅ System displays: "No todos found."

**Acceptance Criteria**: FR-004

---

### Test Case 1.4: View Todo by ID

**Steps**:
1. Add a todo (should get ID 1)
2. Select option 3 (View Todo by ID)
3. Enter ID: 1

**Expected Result**:
- ✅ System displays the todo with all details

**Acceptance Criteria**: FR-004

---

### Test Case 1.5: Add Todo with Empty Title

**Steps**:
1. Select option 1 (Add Todo)
2. Enter title: "" (empty string)
3. Enter description: "Test"

**Expected Result**:
- ❌ System displays error: "Title cannot be empty"
- ✅ Todo is NOT created

**Acceptance Criteria**: FR-009, FR-010

---

## Test Scenario 2: Delete Todos (User Story 2)

**Goal**: Verify users can delete todos

### Test Case 2.1: Delete Existing Todo

**Steps**:
1. Add 3 todos (IDs 1, 2, 3)
2. Select option 5 (Delete Todo)
3. Enter ID: 2

**Expected Result**:
- ✅ System confirms: "Todo 2 deleted successfully."
- ✅ View all shows only todos 1 and 3

**Acceptance Criteria**: FR-005

---

### Test Case 2.2: Delete Non-Existent Todo

**Steps**:
1. Add 1 todo (ID 1)
2. Select option 5 (Delete Todo)
3. Enter ID: 999

**Expected Result**:
- ❌ System displays error: "Todo with ID 999 not found."
- ✅ Existing todo remains unchanged

**Acceptance Criteria**: FR-010

---

### Test Case 2.3: Delete Last Todo

**Steps**:
1. Add 1 todo (ID 1)
2. Delete todo ID 1
3. View all todos

**Expected Result**:
- ✅ System displays: "No todos found."

**Acceptance Criteria**: FR-005

---

## Test Scenario 3: Update Todo Details (User Story 3)

**Goal**: Verify users can update todo title and description

### Test Case 3.1: Update Title Only

**Steps**:
1. Add todo with title "Old title" and description "Old desc"
2. Select option 4 (Update Todo)
3. Enter ID: 1
4. Enter new title: "New title"
5. Press Enter for description (keep current)

**Expected Result**:
- ✅ System confirms: "Todo 1 updated successfully."
- ✅ View shows title changed to "New title"
- ✅ Description remains "Old desc"

**Acceptance Criteria**: FR-006

---

### Test Case 3.2: Update Description Only

**Steps**:
1. Add todo with title "Title" and description "Old desc"
2. Select option 4 (Update Todo)
3. Enter ID: 1
4. Press Enter for title (keep current)
5. Enter new description: "New desc"

**Expected Result**:
- ✅ System confirms: "Todo 1 updated successfully."
- ✅ Title remains "Title"
- ✅ Description changed to "New desc"

**Acceptance Criteria**: FR-006

---

### Test Case 3.3: Update Non-Existent Todo

**Steps**:
1. Add 1 todo (ID 1)
2. Select option 4 (Update Todo)
3. Enter ID: 999

**Expected Result**:
- ❌ System displays error: "Todo with ID 999 not found."

**Acceptance Criteria**: FR-010

---

### Test Case 3.4: Update with Empty Title

**Steps**:
1. Add todo with title "Title"
2. Select option 4 (Update Todo)
3. Enter ID: 1
4. Enter new title: "" (empty string)

**Expected Result**:
- ❌ System displays error: "Title cannot be empty"
- ✅ Todo remains unchanged

**Acceptance Criteria**: FR-009, FR-010

---

## Test Scenario 4: Mark Complete/Incomplete (User Story 4)

**Goal**: Verify users can track todo status

### Test Case 4.1: Mark Todo Complete

**Steps**:
1. Add todo (ID 1, status should be "pending")
2. Select option 6 (Mark Complete)
3. Enter ID: 1
4. View all todos

**Expected Result**:
- ✅ System confirms: "Todo 1 marked as completed."
- ✅ View shows status "completed"

**Acceptance Criteria**: FR-007

---

### Test Case 4.2: Mark Todo Incomplete

**Steps**:
1. Add todo and mark it complete (ID 1, status "completed")
2. Select option 7 (Mark Incomplete)
3. Enter ID: 1
4. View all todos

**Expected Result**:
- ✅ System confirms: "Todo 1 marked as pending."
- ✅ View shows status "pending"

**Acceptance Criteria**: FR-007

---

### Test Case 4.3: Mark Non-Existent Todo

**Steps**:
1. Select option 6 (Mark Complete)
2. Enter ID: 999

**Expected Result**:
- ❌ System displays error: "Todo with ID 999 not found."

**Acceptance Criteria**: FR-010

---

### Test Case 4.4: View Mixed Statuses

**Steps**:
1. Add 5 todos
2. Mark todos 1, 3, 5 as complete
3. View all todos

**Expected Result**:
- ✅ Todos 1, 3, 5 show status "completed"
- ✅ Todos 2, 4 show status "pending"

**Acceptance Criteria**: FR-004, FR-013

---

## Test Scenario 5: Filter by Status (User Story 5)

**Goal**: Verify users can filter todos by status

### Test Case 5.1: Filter by Pending

**Steps**:
1. Add 5 todos
2. Mark 2 todos as complete
3. Select option 8 (Filter by Status)
4. Enter status: "pending"

**Expected Result**:
- ✅ System displays only 3 pending todos
- ✅ Completed todos are not shown

**Acceptance Criteria**: FR-008

---

### Test Case 5.2: Filter by Completed

**Steps**:
1. Add 5 todos
2. Mark 2 todos as complete
3. Select option 8 (Filter by Status)
4. Enter status: "completed"

**Expected Result**:
- ✅ System displays only 2 completed todos
- ✅ Pending todos are not shown

**Acceptance Criteria**: FR-008

---

### Test Case 5.3: Filter with No Matches

**Steps**:
1. Add 3 todos (all pending)
2. Select option 8 (Filter by Status)
3. Enter status: "completed"

**Expected Result**:
- ✅ System displays: "No todos found."

**Acceptance Criteria**: FR-008

---

### Test Case 5.4: Filter with Invalid Status

**Steps**:
1. Select option 8 (Filter by Status)
2. Enter status: "invalid"

**Expected Result**:
- ❌ System displays error: "Status must be 'pending' or 'completed'"

**Acceptance Criteria**: FR-010

---

## Test Scenario 6: Edge Cases

**Goal**: Verify system handles edge cases correctly

### Test Case 6.1: Invalid Menu Choice

**Steps**:
1. Enter choice: "abc"

**Expected Result**:
- ❌ System displays error: "Invalid choice. Please enter a number between 1 and 9."

**Acceptance Criteria**: FR-010

---

### Test Case 6.2: Invalid ID Format

**Steps**:
1. Select option 3 (View Todo by ID)
2. Enter ID: "abc"

**Expected Result**:
- ❌ System displays error: "Invalid ID. Please enter a positive number."

**Acceptance Criteria**: FR-010

---

### Test Case 6.3: Negative ID

**Steps**:
1. Select option 3 (View Todo by ID)
2. Enter ID: "-1"

**Expected Result**:
- ❌ System displays error: "Invalid ID. Please enter a positive number."

**Acceptance Criteria**: FR-010

---

### Test Case 6.4: Long Description (1000+ characters)

**Steps**:
1. Select option 1 (Add Todo)
2. Enter title: "Test"
3. Enter description: (paste 1000+ character string)

**Expected Result**:
- ✅ System accepts and stores the long description
- ✅ View displays the full description

**Acceptance Criteria**: FR-001

---

### Test Case 6.5: Duplicate Titles

**Steps**:
1. Add todo with title "Duplicate"
2. Add another todo with title "Duplicate"

**Expected Result**:
- ✅ Both todos are created with different IDs
- ✅ System allows duplicate titles

**Acceptance Criteria**: FR-001, FR-002

---

## Test Scenario 7: Performance

**Goal**: Verify system handles 50+ todos without degradation

### Test Case 7.1: Add 50 Todos

**Steps**:
1. Add 50 todos with different titles
2. View all todos
3. Filter by status
4. Update a todo
5. Delete a todo

**Expected Result**:
- ✅ All operations complete in <100ms
- ✅ No noticeable slowdown
- ✅ No errors or crashes

**Acceptance Criteria**: SC-007

---

## Test Scenario 8: Application Lifecycle

**Goal**: Verify application starts and exits cleanly

### Test Case 8.1: Clean Startup

**Steps**:
1. Launch app: `uv run src/main.py`

**Expected Result**:
- ✅ App starts without errors
- ✅ Menu displays correctly
- ✅ No warnings or stack traces

**Acceptance Criteria**: SC-009

---

### Test Case 8.2: Clean Exit

**Steps**:
1. Launch app
2. Select option 9 (Exit)

**Expected Result**:
- ✅ System displays: "Goodbye! All data will be lost (in-memory only)."
- ✅ App exits cleanly
- ✅ No errors or warnings

**Acceptance Criteria**: FR-015, SC-009

---

### Test Case 8.3: Data Loss on Exit

**Steps**:
1. Launch app
2. Add 3 todos
3. Exit app (option 9)
4. Launch app again
5. View all todos

**Expected Result**:
- ✅ System displays: "No todos found."
- ✅ All previous data is lost (in-memory only)

**Acceptance Criteria**: FR-014

---

## Test Summary Checklist

After completing all test scenarios, verify:

- [ ] All 15 functional requirements (FR-001 through FR-015) are met
- [ ] All 10 success criteria (SC-001 through SC-010) are met
- [ ] All 5 user stories are independently testable
- [ ] Error messages are user-friendly (no stack traces)
- [ ] Application is deterministic (same input → same output)
- [ ] Performance is acceptable (50+ todos, <100ms operations)
- [ ] Application starts and exits cleanly

---

## Notes

- All tests should be performed in a single session (in-memory only)
- If any test fails, document the failure and investigate
- Phase I uses manual testing only (automated tests in Phase II)
- Each user story should be testable independently
