from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, priority='Low'):
        self.title = title
        self.description = description
        self.due_date = self.parse_due_date(due_date)
        self.priority = priority
        self.is_completed = False

    def parse_due_date(self, due_date):
        try:
            return datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            print(f"Invalid date format: {due_date}. Expected YYYY-MM-DD.")
            return None

    def complete(self):
        self.is_completed = True

    def update(self, title=None, description=None, due_date=None, priority=None):
        if title is not None: self.title = title
        if description is not None: self.description = description
        if due_date is not None: self.due_date = self.parse_due_date(due_date)
        if priority is not None: self.priority = priority

    def __repr__(self):
        status = 'Completed' if self.is_completed else 'Pending'
        due_date_str = self.due_date.strftime('%Y-%m-%d') if self.due_date else 'N/A'
        return f"{self.title} [{self.priority}] - {status}\nDue: {due_date_str}\n{self.description}\n"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority='Low'):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print(f"Added task: {title}")

    def list_tasks(self):
        if not self.tasks:
            return "No tasks available."
        return "\n".join(str(task) for task in self.tasks)

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                print(f"Task '{title}' is now completed.")
                return
        print(f"Task '{title}' not found.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Removed task: {title}")
                return
        print(f"Task '{title}' not found.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks have been cleared.")

def run_app():
    todo_list = ToDoList()
    
    menu = (
        "\nTo-Do List Manager\n"
        "1. Add Task\n"
        "2. List All Tasks\n"
        "3. Complete Task\n"
        "4. Remove Task\n"
        "5. Clear All Tasks\n"
        "6. Exit\n"
    )
    
    while True:
        print(menu)
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task Title: ")
            description = input("Task Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (Low, Medium, High): ")
            todo_list.add_task(title, description, due_date, priority)
        elif choice == '2':
            print(todo_list.list_tasks())
        elif choice == '3':
            title = input("Task Title to Complete: ")
            todo_list.mark_task_completed(title)
        elif choice == '4':
            title = input("Task Title to Remove: ")
            todo_list.remove_task(title)
        elif choice == '5':
            todo_list.clear_tasks()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    run_app()