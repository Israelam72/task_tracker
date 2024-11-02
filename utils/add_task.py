import os
import json
import datetime

path = './data.json'


def add_task(task):
        if not os.path.exists(path):
            first_task = {
                "tasks": [
                    {
                        "task": f"{task}",
                        "id": 1,
                        "status": "todo",
                        "createdAt": str(datetime.date.today()),
                        "updatedAt": str(datetime.date.today())
                    }
                    
                ]
            }

            with open(path, "w") as file:
                json.dump(first_task, file, indent=2)

        else:
            with open(path, "r") as file:
                task_dict = json.load(file)

                new_task = {
                    "task": f"{task}",
                        "id": len(task_dict["tasks"]) + 1,
                        "status": "todo",
                        "createdAt": str(datetime.date.today()),
                        "updatedAt": str(datetime.date.today())
                }
                
                task_dict["tasks"].append(new_task)
                
                with open(path, "w") as file:
                    json.dump(task_dict, file, indent=2)