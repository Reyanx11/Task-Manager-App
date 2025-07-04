from datetime import datetime

class Task:
    def __init__(self,title,):
        self.title = title
        self.completed=False
        self.created_at=datetime.now()

    def mark_completed(self):
        self.completed =True
        print(f"{self.title} marked as completed")

    def mark_incomplete(self):
        self.completed=False
        print(f"{self.title} marked as incomplete")

    def toggle(self):
        if self.completed:
            self.mark_incomplete()
        else:
            self.mark_completed()

    def __str__(self):
        status = "✓" if self.completed else "○"
        date_str =self.created_at.strftime("%Y-%m-%d %H:%M")

        return(f"[{status}] {self.title} (created: {date_str})")

if __name__ == "__main__":

    task1 =Task("abc")     
    print("created class")
    print(task1)   

    task1.mark_completed()
    print("After marking complete:")
    print(task1)

    task1.toggle()
    print("After toggling:")
    print(task1)