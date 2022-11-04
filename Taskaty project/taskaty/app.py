# is going to be the access to the project
from argparse import ArgumentParser
from operator import add # This unit will allow the py to work on the command line
from .taskcontroller import TaskController

# print (__name__) : __main__
# but when this file is imported the output will be the name of the file not __main__
# so if the file has been run by python you will get __main__
# if the file is imported you will get the file name
# for more explanation : https://www.youtube.com/watch?v=sugvnHA7ElY

def main():
    controller = TaskController('task.txt')




    # parser = ArgumentParser()
    # args = parser.parse_args()
    # run in command line by # python app.py
    # you will see that you have only one argument possible >> -h
    # python app.py -h
    # usage: app.py [-h]
    # options:
    # -h, --help  show this help message and exit
    # to add describtion :
    parser = ArgumentParser(description="Simple CLI task manager")
    # parser.add_argument('add')
    # args = parser.parse_args()
    # print(args)
    # so now you will have an argument with key = add and value = Hello for example
    # Namespace(add='Hellp')
    # print(args.add)
    # Hello

    # if the application is doing more than one action so it is better to make them in sub commands (subparsers)
    subparsers = parser.add_subparsers()
    
    add_task = subparsers.add_parser('add', help="Add the given task")
    add_task.add_argument('title', help="Title of the task", type=str)
    add_task.add_argument('-d', '--description', help="Short description of the task", type= str, default=None )
    add_task.add_argument('-s', '--start_date', help="Date to begin the task", type= str, default=None )
    add_task.add_argument('-e', '--end_date', help="Date to end the task", type= str, default=None )
    add_task.add_argument('--done', help="Check whether the task is done or not", default=False )
    add_task.set_defaults(func= controller.add_task)

    list_tasks = subparsers.add_parser('list', help='List unfinished tasks')
    list_tasks.add_argument('-a', '--all', help='List all tasks', action='store_true') # once a is there all status will be True to show the tasks
    list_tasks.set_defaults(func= controller.display)

    check_task = subparsers.add_parser('check', help='Check the given task')
    check_task.add_argument('-t', '--task', help='Number of the tasks to be done. If not specified, last task will be removed.', type=int)
    check_task.set_defaults(func= controller.check_task)


    remove = subparsers.add_parser('remove', help='Remove a task')
    remove.add_argument('-t','--task', help='The task to be removed (Number)',type=int)
    remove.set_defaults(func= controller.remove)


    reset = subparsers.add_parser('reset', help='Remove all tasks')
    reset.set_defaults(func= controller.reset)

    
    args = parser.parse_args()
    args.func(args)

    # python app.py -h
    # usage: app.py [-h] {add,list,check,remove,reset} ...

    # Simple CLI task manager

    # positional arguments:
    # {add,list,check,remove,reset}
    #     add                 Add the given task
    #     list                List unfinished tasks
    #     check               Check the given task
    #     remove              Remove a task
    #     reset               Remove all tasks

    # options:
    # -h, --help            show this help message and exit

    # python app.py list -h
    # usage: app.py list [-h] [-a]

    # options:
    # -h, --help  show this help message and exit
    # -a, --all   List all tasks

    # they all must be identified above the args = parser.parse_args()

if __name__ == '__main__':
    main()