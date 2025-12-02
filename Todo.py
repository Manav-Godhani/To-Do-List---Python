Tasks = ["Hello"]
# print("Add the task")
# task = input("Enter task :- ")
# Tasks.append(task)
# print(Tasks)

while True:
    print("===========================")
    print("⚙️-: Operations :- ⚙️")
    print("===========================")
    print("1️⃣  Add Task")
    print("2️⃣  View Tasks")
    print("3️⃣  Delete Task")
    print("4️⃣  Exit")
    print("===========================")
    Choice = int(input("Enter Your Operations :- "))

    if Choice == 1:
        task = input("Enter task to add :- ")
        Tasks.append(task)
        print("---------------------------")
        print("Task added successfully. ✅")
    elif Choice == 2:
        print("------------------")
        print("Total Tasks are : ", len(Tasks))
        print("------------------")
        num = 1
        for i in Tasks:
            print(num ,"=> ",i)
            num += 1
    elif Choice == 3:
        num=0
        for i in Tasks:
            print(num+1 , "- ", i)
            num += 1
        print("---------------------------")
        index = int(input("Enter task index"))
        Tasks.pop(index-1)
        print("---------------------------")
        print("Task deleted successfully. ❌")
    elif Choice == 4:
        print("Goodbye! 👋")
        break
    else:
        print("Invalid Choice") 


# This is a simple To-Do list application that allows users to add, view, and delete tasks.