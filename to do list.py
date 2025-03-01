#to do list
tasks = []

def add_task(description):
    task = {
        'description': description,
        'completed': False
    }
    tasks.append(task)

def view_tasks():
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{idx}. {task['description']} - {status}")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
    else:
        print("Give Proper Input:")

def complete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
    else:
        print("Invalid task number")

if __name__ == "__main__":
    while True:
        print("\nWelcome to To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Complete Task")
        print("5. Exit")
        
        response = input("Enter Your Preference: ")
        
        if response == '1':
            description = input("Enter Description of task: ")
            add_task(description)
        elif response == '2':
            view_tasks()
        elif response == '3':
            task_number = int(input("Enter your task number: "))
            remove_task(task_number)
        elif response == '4':
            task_number = int(input("Enter task number to update status: "))
            complete_task(task_number)
        elif response == '5':
            break
        else:
            print("Give Valid Input\n")
