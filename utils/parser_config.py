import argparse


def create_parser():
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
        '-lp',
        '--list-all-progress',
        action='store_true',
        help='List all in progress tasks')
    group.add_argument(
        '-lt',
        '--list-all-todo',
        action='store_true',
        help='List all tasks that are marked as todo')
    
    return parser
