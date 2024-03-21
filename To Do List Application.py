# Define an empty list to store tasks
tasks = []

# Function to display the current to-do list
def show_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")
    else:
        print("There are no tasks in your list.")

# Function to add a new task
def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print("Task added successfully!")

# Function to mark a task as complete
def complete_task():
    if tasks:
        show_tasks()
        try:
            task_index = int(input("Enter the number of the task to mark complete: ")) - 1
            if "[Completed]" in tasks[task_index]:
                print("You have already completed this task.")
            else:
                tasks[task_index] += " [Completed]"
                print(f"Task '{tasks[task_index].replace(' [Completed]', '')}' marked as complete!")
        except (IndexError, ValueError):
            print("Invalid task number!")
    else:
        print("There are no tasks to complete.")

# Function to remove a task
def remove_task():
    show_tasks()
    if tasks:
        try:
            task_index = int(input("Enter the number of the task to remove: ")) - 1
            tasks.pop(task_index)
            print("Task removed successfully!")
        except (IndexError, ValueError):
            print("Invalid task number!")
    else:
        print("There are no tasks to remove.")

# Main loop to manage the to-do list
while True:
    print("\nTo-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Complete")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting To-Do List App...")
        break
    else:
        print("Invalid choice. Please try again.")
