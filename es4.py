from sys import argv
file = open(argv[1], "r")

# reading from file
taskList = file.read().split("\n")
file.close()

# initialisation
task2D = {}
i = 0

# setting preferences
for task in taskList:
    flag = True

    while(flag):
        print("\nTask " + str(i) + ": " + task + ". Is it urgent? (y/n): ", end="")
        answer = input()
        if answer == "y" :
            task2D[task] = True
            flag = False

        elif answer == "n" :
            task2D[task] = False
            flag = False

        else:
            print("Wrong answer. Please write y or n.")
    i = i + 1

print("\n\n2D Tasks dictionary: ", end="")
print(task2D)

# creating a new dictionary
urgent2D={}

for (task, urgent) in task2D.items():
    if urgent == True :
        urgent2D[task] = True

print("\n\n2D Urgent Tasks dictionary: ", end="")
print(urgent2D)




