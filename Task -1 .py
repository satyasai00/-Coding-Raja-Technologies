#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import os
from datetime import datetime, timedelta

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

# Function to display tasks
def display_tasks(tasks):
    clear_screen()
    if not tasks:
        print("No tasks found.")
    else:
        print("Task List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

# Function to add a new task
def add_task(tasks):
    clear_screen()
    title = input("What task would you like to add? ")
    priority = input("How would you prioritize it (high/medium/low)? ").lower()
    due_date_str = input("Any specific due date (YYYY-MM-DD)? ")
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None

    new_task = {
        "title": title,
        "priority": priority,
        "due_date": due_date_str if due_date else "Not set",
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Great! Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    clear_screen()
    display_tasks(tasks)
    task_index = int(input("Which task would you like to remove? Enter the task number: ")) - 1

    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"The task '{removed_task['title']}' has been removed successfully.")
    else:
        print("Invalid task number. Please try again.")

# Function to mark a task as completed
def mark_completed(tasks):
    clear_screen()
    display_tasks(tasks)
    task_index = int(input("Which task have you completed? Enter the task number: ")) - 1

    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Congratulations! Task '{tasks[task_index]['title']}' marked as completed.")
    else:
        print("Invalid task number. Please try again.")

# Function to clear the console screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nWelcome to the To-Do List:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("What would you like to do? Enter the number (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


