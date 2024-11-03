import os
import datetime
from utils.json_handler import json_dump, json_load

path = './data.json'


def add_task(task):
        if not os.path.exists(path) or not json_load()['tasks']:
            first_task = {
                "tasks": [
                    {
                        "task": task,
                        "id": 1,
                        "status": "todo",
                        "createdAt": str(datetime.date.today()),
                        "updatedAt": str(datetime.date.today())
                    }
                    
                ]
            }

            json_dump(first_task)
            print("Your first task has been created!")

        else:
            task_dict = json_load()

            new_task = {
                "task": task,
                "id": task_dict['tasks'][-1]["id"] + 1,
                "status": "todo",
                "createdAt": str(datetime.date.today()),
                "updatedAt": str(datetime.date.today())
            }
                
            task_dict["tasks"].append(new_task)

            json_dump(task_dict)
            print("A new task has been added!")    