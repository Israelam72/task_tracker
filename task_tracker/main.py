import argparse
import time

parser = argparse.ArgumentParser(prog='taskctl', description='Creates tasks')
parser.add_argument('-l','--largura')
parser.add_argument('-c', '--comprimento')

def main():
    while True:
        text = input('$ ').lower()
        if text != 'exit':
            args = parser.parse_args(text.split())
            print(args.comprimento)
        else:
            print("Exiting the Task Tracker")
            time.sleep(1)
            break

if __name__ == '__main__':
    main()