tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Task added: {title}")

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✖"
        print(f"{i}. {t['title']} [{status}]")

def complete_task(index):
    try:
        tasks[index - 1]["done"] = True
        print("Task marked as completed!")
    except:
        print("Invalid task number.")

if __name__ == "__main__":
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Complete Task\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            num = int(input("Enter task number: "))
            complete_task(num)
        else:
            break
