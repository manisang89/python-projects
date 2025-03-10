import os

file_name="manager.txt"
def load_task():
    tasks={}

    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            for line in file:
                tasks_id,task_title,status=line.strip().split("|")
                tasks[int(tasks_id)]={"task_title":task_title,"status":status}

    return tasks


def save_task(tasks):
    with open(file_name,"w") as file:
        for task_id,task in tasks.items():
            file.write(f"{task_id} | {task['task_title']} | {task['status']}\n")


def add_task(tasks):
    title=input("Enter task title : ")
    task_id=max(tasks.keys(),default=0)+1
    tasks[task_id]={"task_title":title,"status":"incomplete"}
    print(f"{title} is added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id,task in tasks.items():
            print(f"{task_id} | {task['task_title']} - {task['status']}")
    
def mark_task(task):
    tasks_id=int(input("Enter task id to mark as complete : "))
    if tasks_id in task:
        task[tasks_id]["status"]="completed"
    else:
        print("Invalid task id.")


def delete_task(tasks):
    tasks_id=int(input("Enter task id to delete : "))
    if tasks_id in tasks:
        print(f"{ tasks.pop(tasks_id)} is deleted")
    else:
        print("Invalid task id.")
    

def main():
    tasks=load_task()
    while True:
        print("\nTask Manager Menu : ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save")
        print("6. Exit")
        choice=input("Enter your choice : ")
        if choice=="1":
            add_task(tasks)
        elif choice=="2":
            view_tasks(tasks)
        elif choice=="3":
            mark_task(tasks)
        elif choice=="4":
            delete_task(tasks)
        elif choice=="5":
            save_task(tasks)
        elif choice=="6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    
if __name__=="__main__":
    main()