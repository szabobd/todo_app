import sys

import os

print(sys.argv)


def print_usage():
    print('\n'
          'Command Line Todo application \n'
          '============================= \n'
          'Command line arguments: \n'
          '    -l  Lists all tasks \n'
          '    -a   Adds a new task \n'
          '    -r   Removes a task \n'
          '    -c   Completes a task \n'
          '    -u   Lists undone tasks \n'
          )


def print_count():
    try:
        list_undone_task()
        with open('tasks.txt', 'r') as in_file1, open('undone_tasks.txt', 'r') as in_file2:
            print('You have ' + str(len(list(in_file1))) + ' todos, from which ' + str(len(list(in_file2))) + ' are undone')

    except FileNotFoundError:
        print('You have no todos yet')


def list_task():
    try:
        with open('tasks.txt', 'r') as in_file:
            for position, line in enumerate(in_file):
                print(str(position + 1) + ' -' + str(line))

    except FileNotFoundError:
        print('You need to ask some tasks first')


def list_undone_task():
    with open('tasks.txt', 'r') as in_file:
        checker = []
        for position, line in enumerate(in_file):
            if list(line)[2] == ' ':
                checker.append(line)

    with open('undone_tasks.txt', 'w') as in_file:
        for line in checker:
            in_file.write(line)


def print_undone_task():
    with open('undone_tasks.txt', 'r') as in_file:
        for position, line in enumerate(in_file):
            print(str(position + 1) + ' -' + str(line))


def add_task():
    with open('tasks.txt', 'a') as in_file:
        in_file.write(' [ ] ' + sys.argv[2] + '\n')


def check_task():
    with open('tasks.txt', 'r') as in_file:
        updated_list = []
        content = in_file.readlines()
        for position, line in enumerate(content):
            if position + 1 == int(sys.argv[2]):
                list_of_characters = list(line)
                list_of_characters[2] = 'x'
                checked_line = ""
                updated_list.append(checked_line.join(list_of_characters))
            else:
                updated_list.append(line)

    with open('tasks.txt', 'w') as in_file:
        for line in updated_list:
            in_file.write(line)


def remove_task():
    try:
        with open('tasks.txt', 'r') as in_file:
            lines = in_file.readlines()
            in_file.close()

            del lines[int(sys.argv[2]) - 1]

        with open('tasks.txt', 'w+') as in_file:
            for line in lines:
                in_file.write(line)

    except IndexError:
        print('Unable to remove: index is out of bound')

    except ValueError:
        print('Unable to remove: index is not a number')


if len(sys.argv) == 1:
    print_usage()
    print_count()

elif sys.argv[1] == '-l':
    if os.stat('tasks.txt').st_size == 0:
        print('No todos for today :)')
    elif os.stat('tasks.txt').st_size != 0:
        list_task()

elif sys.argv[1] == '-u':
    try:
        if os.stat('tasks.txt').st_size != 0:
            list_undone_task()
            print_undone_task()
        elif os.stat('tasks.txt').st_size == 0:
            print('You did it, champ!')
    except FileNotFoundError:
        print('You need to add some tasks first')

elif sys.argv[1] == '-a':
    if len(sys.argv) == 2:
        print('Unable to add: no task provided')
    else:
        add_task()

elif sys.argv[1] == '-c':
    if len(sys.argv) == 2:
        print('Unable to check: no index provided')
    else:
        check_task()

elif sys.argv[1] == '-r':
    if len(sys.argv) == 2:
        print('Unable to remove: no index provided')
    remove_task()

elif sys.argv[1] != '-l' or 'u' or '-r' or '-a' or '-c':
    print('Invalid argument, please todo.py and see the available arguments!')
