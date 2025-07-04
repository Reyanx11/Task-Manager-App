from datetime import datetime


# Task class for individual task
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
        self.created_at = datetime.now()   #captures time when task is created

    def mark_completed(self):
        self.completed = True
        print(f"{self.title} marked as completed")

    def mark_incomplete(self):
        self.completed = False
        print(f"{self.title} marked as incomplete")

# to toggle task (complete)

    def toggle(self):
        if self.completed:
            self.mark_incomplete()
        else:
            self.mark_completed()

    def __str__(self):
        status = "✓" if self.completed else "○"
        date_str = self.created_at.strftime("%Y-%m-%d %H:%M")
        return f"[{status}] {self.title} (created: {date_str})"


#TaskManager class to handle list of tasks
class TaskManger:
    def __init__(self):
        self.tasks = []     # List to store all task objects

# Add a new task
    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        print(f"\nTask added: '{new_task}'")

# display task
    def display_task(self):
        if not self.tasks:
            print("\nNo tasks found.")
        else:
            print("\n----- Your Tasks -----")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

# Mark a specific task complete
    def mark_task_completed(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            self.tasks[task_id - 1].mark_completed()
        else:
            print(f"Invalid task ID: {task_id}")

# delete a specific task
    def delete_task(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            deleted = self.tasks.pop(task_id - 1)
            print(f"Deleted task: {deleted.title}")
        else:
            print(f"Invalid task ID: {task_id}")

# returns a total number of task
    def get_task_count(self):
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        return total, completed

if __name__ == "__main__":
    manager = TaskManger()

# Test runs
    manager.add_task("dsa")
    manager.add_task("project")
    manager.add_task("wasting time")

    manager.display_task()

    manager.mark_task_completed(2)

    manager.display_task()

    total, completed = manager.get_task_count()
    print(f"Total tasks: {total}, Completed: {completed}")
