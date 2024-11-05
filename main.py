import time
from utils.add_task import add_task
from utils.delete_task import delete_task
from utils.update_task import update_task
from utils.mark_task import mark_progress_task, mark_done_task
from utils.parser_config import create_parser

class NewParser():
    def task_args(self):
        while True:
            text = input('$ ').lower().split()
            try:
                if text[0] != 'taskctl':
                    print('Command not recognized or missing: taskctl')
                elif text[0] == 'exit' or 'stop' == text[0] :
                    print('Exiting task tracker!')
                    time.sleep(0.2)
                    break
                else:
                    try:
                        args = create_parser().parse_args(text)
                        action = {
                            "add": add_task(' '.join(args.add)) if args.add else None,
                            "delete": delete_task(args.delete) if args.delete else None,
                            "update": update_task(args.update) if args.update else None,
                            "mark_progress": mark_progress_task(args.mark_progress) if args.mark_progress else None,
                            "mark_done": mark_done_task(args.mark_done) if args.mark_done else None,
                        }

                        for action, func in action.items():
                            if func:
                                func()

                        
                    except SystemExit:
                        pass
            except IndexError:
                pass

"""
- consertar bug que se o argumento for 0 ele reseta para o modo taskctl
- criar arquivos para cada função: list, list-done, list-todo, list-progress;
- quando criar o update, pensar da mesma forma que foi criada o delete
- ULTIMA coisa planejada a se fazer: tratar saída da função de listar, de adição ou de update no terminal, 
   mostrando as tasks de forma organizada.
- MUDAR DE BRANCH!!!!!
"""

def main():

    result = NewParser()
    result.task_args()

if __name__ == '__main__':
    main()