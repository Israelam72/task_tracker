import os
import datetime
from utils.json_handler import json_dump, json_load, path
from utils.list import make_list


def add_task(task):
        if not os.path.exists(path) or not json_load()['tasks']:
            first_task = {
                "tasks": [
                    {
                        "Task": task,
                        "Id": 1,
                        "Status": "todo",
                        "Created at": str(datetime.date.today()),
                        "Updated at": str(datetime.date.today())
                    }
                    
                ]
            }

            json_dump(first_task)
            print("Your first task has been created!")

        else:
            task_dict = json_load()

            new_task = {
                "Task": task,
                "Id": task_dict['tasks'][-1]["Id"] + 1,
                "Status": "todo",
                "Created at": str(datetime.date.today()),
                "Updated at": str(datetime.date.today())
            }
                
            task_dict["tasks"].append(new_task)

            json_dump(task_dict)
            print("A new task has been added!")
            make_list(new_task)    