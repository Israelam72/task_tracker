import argparse
import time

parser = argparse.ArgumentParser(prog='taskctl', description='Creates tasks')
parser.add_argument('taskctl', help='Digite o comprimento e largura')
parser.add_argument('-l','--largura')
parser.add_argument('-c', '--comprimento')

class NewParser():
    def task_args(self):
        while True:
            text = input('$ ').lower()

            if text in ['exit', 'stop']:
                print('Exiting task tracker!')
                time.sleep(0.5)
                break
            elif not text.startswith('taskctl'):
                print('Command not recognized or missing: taskctl')
            else:
                try:
                    args = parser.parse_args(text.split())
                    print(f'Largura = {args.largura}, comprimento = {args.comprimento}')
                except SystemExit:
                    pass


def main():

    result = NewParser()
    result.task_args()

if __name__ == '__main__':
    main()