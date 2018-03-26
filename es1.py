tasks = []

while True:
    print("\nInsert the number corresponding to the action you want to perform:")
    print("1. insert a new task;")
    print("2. remove a task;")
    print("3. show all the tasks;")
    print("4. close the program.\n")

    print("Your choice: ", end="")

    choice=int(input())

    if choice == 1:
        print("Write a new task: ", end="")
        task=input()
        tasks.append(task)
        print("New task added.")

    elif choice == 2:
        print("Remove a new task: ", end="")
        task=input()
        if task not in tasks:
            print("The task you want to delete is not present ")
        else:
            tasks.remove(task)
            print("The task has been correctly removed")

    elif choice == 3:
        print(sorted(tasks, key=lambda v: v.upper()))

    elif choice == 4:
        print("Program closed.")
        exit(0)

    else:
        print("Your choice is not corrected")