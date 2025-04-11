
tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")
    
    elif choice == "2":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    
    elif choice == "3":
        if not tasks:
            print("Nothing to remove — your list is empty!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            remove_index = int(input("Enter the number of the task to remove: "))
            if 1 <= remove_index <= len(tasks):
                removed = tasks.pop(remove_index - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
    
    elif choice == "4":
        print("Goodbye! ✅")
        break

    else:
        print("Please enter a valid option (1-4).")


