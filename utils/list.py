from utils.json_handler import json_load

task_dict = json_load()

def make_list(task):

    show_list = f"| Task: {task['Task']} | Id: {task['Id']} | Status: {task['Status']} | Created at: {task['Created at']} | Updated at: {task['Updated at']} |"
    print(len(show_list)*"-")
    print(show_list)
    print(len(show_list)*"-")

def list_all():
    
    for task in task_dict['tasks']:
        make_list(task)

def list_done():
    task_dict = json_load()

    for task in task_dict['tasks']:
        if task['Status'] == "done":
            make_list(task)

def list_todo():
    task_dict = json_load()

    for task in task_dict['tasks']:
        if task['Status'] == "todo":
            make_list(task)

def list_progress():
    task_dict = json_load()

    for task in task_dict['tasks']:
        if task['Status'] == "progress":
            make_list(task)
