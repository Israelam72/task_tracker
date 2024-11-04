import time
from utils.add_task import add_task
from utils.delete_task import delete_task
from utils.update_task import update_task
from utils.parser_config import create_parser

class NewParser():
    def task_args(self):
        while True:
            text = input('$ ').lower().split()
            if text[0] == 'exit' or 'stop' == text[0]:
                print('Exiting task tracker!')
                time.sleep(0.2)
                break
            elif text[0] != 'taskctl':
                print('Command not recognized or missing: taskctl')
            else:
                try:
                    args = create_parser().parse_args(text)
                    action = {
                        "add": add_task(' '.join(args.add)) if args.add else None,
                        "delete": delete_task(args.delete) if args.delete else None,
                        "update": update_task(args.update) if args.update else None,
                    }

                    for action, func in action.items():
                        if func:
                            func()

                    
                except SystemExit:
                    pass
"""
- criar arquivos para cada função: update, list, mark in progress, mark done;
- quando criar o update, pensar da mesma forma que foi criada o delete
- MUDAR DE BRANCH!!!!!
"""

def main():

    result = NewParser()
    result.task_args()

if __name__ == '__main__':
    main()