import time

# Get the current date in DD/MM/YYYY format
date = time.strftime("%d/%m/%Y")

# Initialize the task list
Tasks = []

def newTask():
    name = input("Enter the name of your task: ")
    description = input("Enter the description of your task: ")
    task_details = input("Enter the task details: ")

    # Add the task to the list
    Tasks.append({
        "name": name,
        "description": description,
        "date": date,
        "details": task_details,
    })
    print("\nTask created successfully!")

def editTask(index):
    if 0 <= index < len(Tasks):
        new_details = input("Enter the new task details: ")
        Tasks[index]["details"] = new_details
        Tasks[index]["date"] = date  # Update the date to reflect the edit
        print("\nTask edited successfully!")
    else:
        print("Invalid task number!")

def deleteTask(index):
    if 0 <= index < len(Tasks):
        Tasks.pop(index)
        print("\nTask deleted successfully!")
    else:
        print("Invalid task number!")

def displayTasks():
    if Tasks:
        print("\nYour tasks:")
        for i, task in enumerate(Tasks):
            print(f"{i}: {task['name']}")
    else:
        print("\nNo tasks available!")

# Main Program Loop
while True:
    user_choice = input("\nDo you want to create a new task? (Yes/No): ").strip().lower()

    if user_choice == "yes":
        newTask()
    else:
        displayTasks()
        if not Tasks:
            print("\nNo tasks to edit or delete. Exiting.")
            break

        try:
            queryT = int(input("\nEnter the number of the task you want to open: "))
            if 0 <= queryT < len(Tasks):
                print("\nSelected Task Details:")
                task = Tasks[queryT]
                print(
                    f"Name: {task['name']}\nDescription: {task['description']}\nDate: {task['date']}\nTask: {task['details']}"
                )

                action = input("\nDo you want to edit or delete this task? (edit/delete/none): ").strip().lower()
                if action == "edit":
                    editTask(queryT)
                elif action == "delete":
                    deleteTask(queryT)
                else:
                    print("\nNo changes made.")
            else:
                print("\nInvalid task number!")
        except ValueError:
            print("\nInvalid input! Please enter a number.")

    continue_program = input("\nDo you want to continue? (Yes/No): ").strip().lower()
    if continue_program != "yes":
        print("\nExiting the Task Manager. Goodbye!")
        break
