from utils.json_handler import json_dump, json_load

def update_task(task_id):

    task_dict = json_load()

    if not [task for task in task_dict['tasks'] if task["id"] == task_id]:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")

    else:
        task_update = input('$ Task: ')

        for task in task_dict['tasks']: 
            if task['id'] == task_id:
                task["task"] = task_update

        json_dump(task_dict)
        print(f'Your task has been updated successfully from {task["task"]} to {task_update}')
