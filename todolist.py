todo_list = []

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added successfuly !")

    elif choice == '2':
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")

    elif choice == '4':
        print("TaTa!!")
        break

    else:
        print("Invalid choice!")