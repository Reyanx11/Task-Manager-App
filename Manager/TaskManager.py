import json
from datetime import datetime
import uuid

# Task class for individual task
class Task:
    def __init__(self,title,):
        self.id = str(uuid.uuid4())
        self.title = title
        self.completed=False
        self.created_at=datetime.now()   # captures time when task is created

    def mark_completed(self):
        self.completed =True  # mark task as completed
        print(f"{self.title} marked as completed")

    def mark_incomplete(self):
        self.completed=False  # mark task as incomplete
        print(f"{self.title} marked as incomplete")

# to toggle task (complete)
    def toggle(self):
        if self.completed:
            self.mark_incomplete()
        else:
            self.mark_completed()

    # convert task to dictionary for JSON saving
    def to_dict(self):
        return {
            "id" :self.id,
            "title" : self.title,
            "completed": self.completed,
            "created_at" : self.created_at.isoformat()
        }
    
    # recreate task from dictionary (loaded from JSON)
    @classmethod
    def from_dict(cls,data):
        task =cls(data['title'])
        task.id = data.get('id', str(uuid.uuid4()))  # fallback if 'id' is missing
        task.completed = data['completed']
        task.created_at =datetime.fromisoformat(data['created_at'])
        return task

    def __str__(self):
        status = "✓" if self.completed else "○"  # tick mark if completed
        date_str =self.created_at.strftime("%Y-%m-%d %H:%M")
        return(f"[{status}] {self.title} (created: {date_str})")

# TaskManager class to handle list of tasks
class TaskManger:
    def __init__(self,filename="tasks.json"):
        self.tasks =[]     # List to store all task objects
        self.filename = filename
        self.load_task()    # Load tasks at startup

# Add a new task
    def add_task(self,title):
        new_task = Task(title)
        print("Adding task:", new_task.title)
        self.tasks.append(new_task)  # add to list
        self.save_task()             # save updated list
        print(f"\nTask added: '{new_task}'")

    def toggle_task_by_id(self,task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.toggle()
                self.save_task()
                break

    def delete_task_by_id(self,task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_task()

# display task
    def display_task(self):
        if not self.tasks:
            print("\n Tasks not found")
        else:
            print("\n-----Your Tasks----")
            for idx,task in enumerate(self.tasks):
                print(f"{idx}. {task}")

# Mark a specific task complete
    def mark_task_completed(self, task_id):
        if 0 <= task_id <len(self.tasks):
            self.tasks[task_id-1].mark_completed()  # adjust for 0-based index
            self.save_task()
        else:
            print(f"Invalid task id {task_id}")
    
# delete a specific task
    def delete_task(self,task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks.pop(task_id-1)  # remove from list
            self.save_task()
        else:
            print(f"Invalid task id {task_id}")

# Save tasks to JSON file
    def save_task(self):
        try:
            tasks_data=[task.to_dict() for task in self.tasks]
            with open("tasks.json","w") as f:
                json.dump(tasks_data, f, indent=2)
            print(f"\n tasks saved to {self.filename}")
        except Exception as e:
            print(f"error saving task: {e}")

# Load tasks from JSON file
    def load_task(self):
        try:
            with open(self.filename,'r') as f:
                task_data =json.load(f)
            self.tasks = [Task.from_dict(task) for task in task_data]
            print(f"Loaded {len(self.tasks)} tasks from {self.filename}")
        except FileNotFoundError:
            print(f"No existing task file found. Starting fresh.")
        except Exception as e:
            print(f"Error loading tasks: {e}")

# returns a total number of task
    def get_task_count(self):
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        return total, completed

# Main menu logic
def main():
    while True:
        manager = TaskManger()
        print("\n---TASK MANAGER---")
        print("\n 1. Add task"
              "\n 2. Display tasks"
              "\n 3. Mark as completed"
              "\n 4. Delete task"
              "\n 5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input")
    

        if choice == 1:
            title=input("Enter a task to add:")
            manager.add_task(title)

        elif choice == 2:
            manager.display_task()

        elif choice == 3:
            manager.display_task()
            try:
                index = int(input("Enter index: "))
            except ValueError:
                print("Invalid input")

            manager.mark_task_completed(index)
        
        elif choice == 4:
            manager.display_task()
            try:
                index = int(input("Enter index: "))
            except ValueError:
                print("Invalid input")

            manager.delete_task(index)
        
        elif choice ==5:
            break

# Entry point
if __name__ =="__main__":
    main()
