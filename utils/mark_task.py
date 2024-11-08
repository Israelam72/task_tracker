import datetime
from utils.json_handler import json_dump, json_load
from utils.list import make_list

def mark_progress_task(task_id):

    task_dict = json_load()

    if not [task for task in task_dict['tasks'] if task["Id"] == task_id]:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")

    else:
        for task in task_dict['tasks']: 
            if task['Id'] == task_id:
                prev_status = task["Status"]
                task["Status"] = "in progress"
                task["Updated at"] = str(datetime.date.today())
                new_status = task
                break

        json_dump(task_dict)
        print(f'Your task has been marked successfully from {prev_status} to "in progress"')
        make_list(new_status) 

def mark_done_task(task_id):

    task_dict = json_load()

    if not [task for task in task_dict['tasks'] if task["Id"] == task_id]:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")

    else:
        for task in task_dict['tasks']: 
            if task['Id'] == task_id:
                prev_status = task["Status"]
                task["Status"] = "done"
                task["Updated at"] = str(datetime.date.today())
                new_status = task
                break

        json_dump(task_dict)
        print(f'Your task has been marked successfully from {prev_status} to "done"')
        make_list(new_status) 

