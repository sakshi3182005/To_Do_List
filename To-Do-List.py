tasks = [] #initializing an empty list to store task

def add_task(task): #Function to add a task to the list
    tasks.append(task)
    print("Task Added!!!")

def view_tasks(): #Function to view all task
    if not tasks:
        print("No task in the list")
    else:
        print("Tasks:")
        for index , task in enumerate(tasks,start=1): #enumerate is a built-in python function used for iteration
            print(f"{index}.{task}")

def remove_task(index): #Function to remove a task by its index
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index-1) #here we subtract 1 from index cuz python starts numbering from 0 and pop will itself update and re-arrange the order
        print(f"Removed Task :{removed_task}")
    else:
        print("Invalid Task Index!!!")

while True : #while True is to create an infinite loop until the user explicitly quits
    print("Options")
    print("Enter 'add' to add a new task")
    print("Enter 'view' to view tasks")
    print("Enter 'remove' to remove a task")
    print("Enter 'quit' to exit")
    user_input = input(":")
    if user_input =="quit":
        break
    elif user_input =="add":
        task= input("Enter a task :")
        add_task(task)
    elif user_input =="view":
        view_tasks()
    elif user_input =="remove":
        index = int(input("Enter the task index to remove :"))
        remove_task(index)
    else:
        print("Invalid Input , Please Try Again")

