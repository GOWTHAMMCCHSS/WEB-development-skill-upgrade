def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your to-do list.")

def remove_task(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task you want to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
