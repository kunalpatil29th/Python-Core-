# todo_cli.py

"""
Project: CLI To-Do List
A simple command-line application to manage tasks.
"""

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def show_tasks():
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

add_task("Learn Python")
add_task("Build a project")
show_tasks()
