tasks = []

def addtask():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Your task has been recorded!")

def listtasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def markcompleted():
    listtasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            print(f"Marked task '{tasks[task_number]}' as completed.")
            tasks.pop(task_number)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid choice.")
        print("Please enter a valid task number.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")

while True:
    print("*************Welcome to To-Do List***************")
    
    print("\n1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter the choice (1/2/3/4/5): ")

    if choice == "1":
        addtask()
    elif choice == "2":
        listtasks()
    elif choice == "3":
        markcompleted()
    elif choice == '4':
        listtasks()
        task_index = int(input("Enter the task index to delete: "))
        delete_task(task_index)
    elif choice == "5":
        print("Sayonara!")
        break
    else:
        print("Invalid choice.")
        print("Please kindly select a valid option.")
