from utils.json_handler import json_dump, json_load

def delete_task(task_id):
    task_dict = json_load()
    print(task_id)
    if task_id == 0:
        print("Type a valid id number")

    task_to_delete = [task for task in task_dict['tasks'] if task["Id"] == task_id]

    if not task_to_delete:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")
    else:
        task_dict['tasks'].remove(task_to_delete[0])
    
    json_dump(task_dict)

    if not task_dict['tasks']:
        print(f"The last task was deleted!")
    else:
        print(f"The task with the given id: {task_id}, has been deleted.")