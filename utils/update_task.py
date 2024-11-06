import datetime
from utils.json_handler import json_dump, json_load

def update_task(task_id):

    task_dict = json_load()

    if not [task for task in task_dict['tasks'] if task["Id"] == task_id]:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")

    else:
        task_update = input('$ Task: ')

        for task in task_dict['tasks']: 
            if task['Id'] == task_id:
                task["Task"] = task_update
                task["Updated at"] = str(datetime.date.today())

        json_dump(task_dict)
        print(f'Your task has been updated successfully from {task["Task"]} to {task_update}')
