def Add_Task():             #The following function is used to add a task to the file Task.txt
    Task = input("Enter the Task: ")
    with open("Task.txt", "a") as file:
        file.write(Task + "\n")
    print("Task Added Successfully")

def View_Task():            #The following function is used to view the tasks in the file Task.txt
    with open("Task.txt", "r") as file:
        Tasks = file.readlines()
        if len(Tasks) == 0:
            print("No Tasks Available")
        else:
            for i in range(len(Tasks)):
                print(f"{i+1}. {Tasks[i]}")

def Delete_Task():          #The following function is used to delete a task from the file Task.txt
    View_Task()
    with open("Task.txt", "r") as file:
        Tasks = file.readlines()
    if len(Tasks) == 0:
        print("No Tasks Available")
    else:
        Task_No = int(input("Enter the Task Number to Delete: "))
        if Task_No > len(Tasks):
            print("Invalid Task Number")
        else:
            Tasks.pop(Task_No-1)
            with open("Task.txt", "w") as file:
                for Task in Tasks:
                    file.write(Task)
            print("Task Deleted Successfully")


if __name__=="__main__":
    print("To Do List")
    while True:
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Exit")
        Choice = int(input("Enter your choice: "))
        if Choice == 1:
            Add_Task()
        elif Choice == 2:
            View_Task()
        elif Choice == 3:
            Delete_Task()
        elif Choice == 4:
            break
        else:
            print("Invalid Choice")
    print("Thank You")
