import time
from utils.add_task import add_task
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
                        "add": add_task(' '.join(args.add) if args.add else None)
                    }

                    for action, func in action.items():
                        if func:
                            func()

                    
                except SystemExit:
                    pass

# criar arquivos para cara função: update, delete, list...
#MUDAR DE BRANCH!!!!!

def main():

    result = NewParser()
    result.task_args()

if __name__ == '__main__':
    main()