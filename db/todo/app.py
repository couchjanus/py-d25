"""Main File to Run the programe"""
import sys
from to_do_list import ToDoList
from datetime import date

class App:
    """Display a menu and respond to choices when
    run """

    def __init__(self):
        self.toDoList = ToDoList()
        self.choices = {
            "1": self.show_tasks,
            "2": self.search_tasks,
            "3": self.add_task,
            "4": self.update_task,
            "5": self.delete_task,
            "6": self.quit,
        }

    def display_menu(self):
        print(
            """
            To Do List menu
            ===============
            1. Show all Tasks 
            2. Search Tasks
            3. Add Tasks
            4. Update task
            5. Delete Task
            6. Quit
            """
        )

    def run(self):
        """Display the menu and repond to the choices"""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_tasks(self):
        tasks = self.toDoList.all_tasks()
        for row in tasks:
            print(row)

    def search_tasks(self):
        q = input("Search tasks: ")
        task = self.toDoList.search(q)
        print(task)

    def add_task(self):
        task_name = input("Enter a task details: ")
        task_deadline = input("Enter a task deadline: ") or date.today().strftime("%Y-%m-%d")
        self.toDoList.new_task(task_name, task_deadline)
        print("Your task has been added:")

    def update_task(self):
        task_id = input("Enter a task id: ")
        task_status = input("Enter new status: ")
        
        self.toDoList.update_task(task_id, task_status)
        print("Your task has been updated")

    def delete_task(self):
        id = input("Enter a task id:")
        self.toDoList.delete_task(id)
        print("Your task has been deleted")

    def quit(self):
        print("Thank you for using To-Do-List today")
        sys.exit(0)

if __name__ == "__main__":
    App().run()
