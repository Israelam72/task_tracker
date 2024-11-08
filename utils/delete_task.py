from utils.json_handler import json_dump, json_load
from utils.list import make_list

def delete_task(task_id):
    task_dict = json_load()

    task_to_delete = [task for task in task_dict['tasks'] if task["Id"] == task_id]

    if not task_to_delete:
        print(f"The task with the given id: {task_id}, doesn't exist, try again.")
    else:
        print("The following task is about to be deleted:")
        make_list(task_to_delete[0])
        certain = input("Are you sure you want to delete this task? [Y/n]: ").lower()
        while True:
            if certain not in ["yes", "y", "no", "n"]:
                print('Type "yes", "y", "no" or "n"')
                break
            elif certain == "yes" or certain == "y":
                task_dict['tasks'].remove(task_to_delete[0])

                json_dump(task_dict)

                if not task_dict['tasks']:
                    print(f"The last task was deleted!")
                else:
                    print(f"The task with the given id: {task_id}, has been deleted.")
                    
                break
            else:
                print("Task NOT deleted")
                break
    
    