# Task Manager in Python 📃

This is a simple yet effective **Task Manager** built using **Python's `os` module**. It allows users to manage tasks with features like adding, viewing, marking, and deleting tasks.

## Features
✅ Add new tasks with unique IDs  
✅ View tasks with their status (Incomplete/Completed)  
✅ Mark tasks as complete  
✅ Delete tasks while retaining the original task IDs  
✅ Save tasks to a file for persistence

---

## How to Run
### Prerequisites
Ensure you have **Python 3.12.1** or later installed.

### Steps to Run
1. **Clone the Repository**  
   ```bash
   git clone <your_repo_link>
   ```

2. **Navigate to the Folder**  
   ```bash
   cd task-manager
   ```

3. **Run the Code**  
   ```bash
   python task_manager.py
   ```

---

## Usage Instructions
Upon running the code, you will see the following menu:
```
Task Manager Menu :
1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Save
6. Exit
```

### Commands Overview
- **Add Task:** Adds a new task with an automatically assigned ID.  
- **View Tasks:** Displays all tasks with their respective statuses.  
- **Mark Task as Complete:** Marks the selected task as "completed."  
- **Delete Task:** Deletes a task but keeps the original task IDs intact.  
- **Save:** Saves all tasks to `manager.txt`.  
- **Exit:** Closes the application without saving new changes.

---

## Code Structure
### `load_task()`
- Loads saved tasks from `manager.txt` (if available).

### `save_task()`
- Writes current task data back into `manager.txt` for persistence.

### `add_task()`
- Adds a new task with the status set as "incomplete."

### `view_tasks()`
- Displays all tasks with their respective IDs and statuses.

### `mark_task()`
- Marks a selected task as "completed."

### `delete_task()`
- Deletes the chosen task and retains the original IDs.

### `main()`
- Provides the main menu to access all features.

---

## Future Enhancements
- Implement ID rearrangement after task deletion.  
- Add deadlines and priority levels for tasks.  
- Develop a GUI interface using `tkinter` or `PyQt`.  
- Enable sorting and filtering options for better task management.  

---

## Sample Task File (`manager.txt`)
```
1 | Finish Python Project | incomplete
2 | Study for Exams | completed
3 | Workout Session | incomplete
```

---

## Author
**Manikesh**  
[GitHub Profile](https://github.com/your-profile)

If you find this project useful, consider giving it a star! ⭐

