import argparse
import json
import time
import os

path = './data.json'

parser = argparse.ArgumentParser(prog='taskctl', description='Manage your tasks!')
parser.add_argument('taskctl', help='Manage your tasks with this command')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    '-a',
    '--add',
     nargs='+',
     type=str,
     help='Add a task')
group.add_argument(
    '-u',
     '--update',
     type=int,
     help='Update a task')
group.add_argument(
    '-d',
     '--delete',
     type=int,
     help='Delete a task')
group.add_argument(
    '-mp',
     '--mark-progress',
     type=int,
     help='Mark a task as "in progress"')
group.add_argument(
    '-md',
     '--mark-done',
     type=int,
     help='Mark a task as "done"')
group.add_argument(
    '-l',
     '--list-all',
     action='store_true',
     help='List all tasks')
group.add_argument(
    '-ld',
     '--list-all-done',
     action='store_true',
     help='List all done tasks')
group.add_argument(
    '-ln',
     '--list-all-not',
     action='store_true',
     help='List all tasks that are not done')
group.add_argument(
    '-lp',
     '--list-all-progress',
     action='store_true',
     help='List all in progress tasks')

class NewParser():
    def task_args(self):
        while True:
            text = input('$ ').lower().split()
            if text[0] == 'exit' or 'stop' == text[0]:
                print('Exiting task tracker!')
                time.sleep(0.5)
                break
            elif text[0] != 'taskctl':
                print('Command not recognized or missing: taskctl')
            else:
                try:
                    args = parser.parse_args(text)
                    action = {
                        "add": lambda: self.add_task(' '.join(args.add) if args.add else None)
                    }

                    for action, func in action.items():
                        if func:
                            func()

                    
                except SystemExit:
                    pass

    def add_task(self, task):
        if os.path.exists(path):
            with open('data.json') as file:
                task_dict = json.load(file)
                print(task_dict)
        else:
            new_task = {
                "task": f"{task}"
            }
            object_json = json.dumps(new_task, indent=2)
            with open('data.json', "w") as file:
                file.write(object_json)
        

        
# Arrumar como é passado para JSON
# checar por que JSON esta sendo criado no lugar errado!!
# adicionar id na task
# criar json se não existe
#MUDAR DE BRANCH!!!!!

def main():

    result = NewParser()
    result.task_args()

if __name__ == '__main__':
    main()