from data import tasks
def update_file():
    file = open("todo_list/data.py", "w")
    file.write(f"tasks = {tasks}")
    file.close()
def add():
    new_task = input("Add new task: ")
    tasks.append(new_task)
    update_file()
    print(f'Task: "{new_task}" has been added successfully.')
def delete():
    for i in range(len(tasks)):
        print(i+1,".",tasks[i])
    inp = int(input("which task do you want to delete ?"))
    if inp-1 <= len(tasks) and inp-1 >= 0:
        del tasks[inp-1]
        update_file()
        print("Task successfully deleted ")
    
def edit():
    for i in range(len(tasks)):
        print(i+1,".",tasks[i])
    inp = int(input("which task do you want to edit ?"))
    if inp-1 <= len(tasks) and inp-1 >= 0:
        tasks[inp-1] = input("Enter task:")
        update_file()
        print(f"Task: \"{tasks[inp-1]}\" has been successfully edited ")
def show():
    print("All tasks: ")
    for i in range(len(tasks)):
        print(i+1,".",tasks[i])

while True:
    choice = int(input(("(1) Add task\n(2) Delete task\n(3) Edit task\n(4) Show tasks\n(5) exit")))
    if choice == 1:
        add()
    elif choice == 2:
        delete()
    elif choice == 3:
        edit()
    elif choice == 4:
        show()
    elif choice == 5:
        exit()
    else:
        print("Invalid Input")