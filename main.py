import time
from utils.add_task import add_task
from utils.delete_task import delete_task
from utils.update_task import update_task
from utils.mark_task import mark_progress_task, mark_done_task
from utils.list import list_all
from utils.parser_config import create_parser

class NewParser():
    def task_args(self):
        while True:
            text = input('$ ').lower().split()

            if not text:
                continue

            try:
                if text[0] == 'exit' or 'stop' == text[0] :
                    print('Exiting task tracker!')
                    time.sleep(0.2)
                    break

                if text[0] != 'taskctl':
                    print('Command not recognized or missing: taskctl')
                    continue

                args = create_parser().parse_args(text)

                if any ([args.update == 0, args.delete == 0, args.mark_done == 0, args.mark_progress == 0]):
                    print("Type a valid id number")
                    continue

                self.execute_action(args)

            except SystemExit:
                pass
            except IndexError:
                pass

    def execute_action(self, args):
        action = {
            "add": lambda: add_task(' '.join(args.add)) if args.add else None,
            "delete": lambda: delete_task(args.delete) if args.delete else None,
            "update": lambda: update_task(args.update) if args.update else None,
            "mark_progress": lambda: mark_progress_task(args.mark_progress) if args.mark_progress else None,
            "mark_done": lambda: mark_done_task(args.mark_done) if args.mark_done else None,
            "list": lambda: list_all() if args.list_all else None
        }

        for action, func in action.items():
            if func:
                func()


"""
- criar arquivos para cada função: list-done, list-todo, list-progress;
- quando listar, pesquisar uma maneira de ficar mais organizado
- ULTIMA coisa planejada a se fazer: tratar saída da função de listar, de adição ou de update no terminal, 
   mostrando as tasks de forma organizada.
- MUDAR DE BRANCH!!!!!
"""

def main():

    result = NewParser()
    result.task_args()

if __name__ == '__main__':
    main()