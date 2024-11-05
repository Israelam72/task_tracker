from utils.json_handler import json_dump, json_load

def mark_progress_task(task_id):

    task_dict = json_load()

    if not [task for task in task_dict['tasks'] if task["id"] == task_id]:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")

    else:
        for task in task_dict['tasks']: 
            if task['id'] == task_id:
                task["status"] = "progress"

        json_dump(task_dict)
        print(f'Your task has been marked successfully from {task["status"]} to "progress"')

def mark_done_task(task_id):

    task_dict = json_load()

    if not [task for task in task_dict['tasks'] if task["id"] == task_id]:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")

    else:
        for task in task_dict['tasks']: 
            if task['id'] == task_id:
                task["status"] = "done"

        json_dump(task_dict)
        print(f'Your task has been marked successfully from {task["status"]} to "done"')
