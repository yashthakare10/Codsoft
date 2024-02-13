import os

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Quit")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(tasks, start=1):
                print("{}. {}".format(index, task.strip()))

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write("{}\n".format(task))
    print("Task added successfully.")

def mark_task_as_done():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = "{} - Done\n".format(tasks[task_number - 1].strip())
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1).strip()
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task '{}' deleted.".format(deleted_task))
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_as_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
