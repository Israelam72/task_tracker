from utils.json_handler import json_load

def list_all():
    task_dict = json_load()

    for task in task_dict['tasks']:
        show_list = f"| Task: {task['Task']} | Id: {task['Id']} | Status: {task['Status']} | Created at: {task['Created at']} | Updated at: {task['Updated at']} |"
        print(len(show_list)*"-")
        print(show_list)
        print(len(show_list)*"-")
