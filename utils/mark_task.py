import datetime
from utils.json_handler import json_dump, json_load

def mark_progress_task(task_id):

    task_dict = json_load()

    if not [task for task in task_dict['tasks'] if task["Id"] == task_id]:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")

    else:
        for task in task_dict['tasks']: 
            if task['Id'] == task_id:
                task["Status"] = "progress"
                task["Updated at"] = str(datetime.date.today())

        json_dump(task_dict)
        print(f'Your task has been marked successfully from {task["Status"]} to "progress"')

def mark_done_task(task_id):

    task_dict = json_load()

    if not [task for task in task_dict['tasks'] if task["Id"] == task_id]:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")

    else:
        for task in task_dict['tasks']: 
            if task['Id'] == task_id:
                task["Status"] = "done"
                task["Updated at"] = str(datetime.date.today())

        json_dump(task_dict)
        print(f'Your task has been marked successfully from {task["Status"]} to "done"')
