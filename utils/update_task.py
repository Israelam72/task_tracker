import datetime
from utils.json_handler import json_dump, json_load
from utils.list import make_list

def update_task(task_id):

    task_dict = json_load()

    if not [task for task in task_dict['tasks'] if task["Id"] == task_id]:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")

    else:
        task_update = input('$ Task: ')

        for task in task_dict['tasks']: 
            if task['Id'] == task_id:
                prev_task = task['Task']
                task["Task"] = task_update
                task["Updated at"] = str(datetime.date.today())
                break

        json_dump(task_dict)
        print(f'Your task has been updated successfully from {prev_task} to {task_update}')
        make_list(task)
