from argparse import ArgumentDefaultsHelpFormatter
from .task import Task
from datetime import date
from tabulate import tabulate
from argparse import Namespace

class TaskController :
    def __init__(self, filename):
        self.filename = filename

    def add_task(self, args):
        # 1) start_date
        if not args.start_date :
            now = date.today().isoformat()
            args.start_date = now

        # 2) task
        task = Task(args.title, args.description, args.start_date, args.end_date, args.done)

        # 3) open file and save info
        with open(self.filename, 'a') as file :
            file.write(str(task)+ '\n')

# to print these date in a the CLI :
# https://pypi.org/project/tabulate/
# install : pip install tabulate
    def list_tasks(self) :
        unfinished_task = []
        with open(self.filename, 'r') as file :
            for line in file :
                title, description, start_date, end_date, done = line.split(", ")
                end_date = None if end_date == 'None' else end_date
                done = False if done.strip('\n') == 'False' else True
                if done :
                    continue
                unfinished_task.append({'title' : title, 'description' : description, 'start_date': start_date, 'end_date':end_date})
            
            return unfinished_task

    def list_all_tasks(self) :
        all_tasks = []
        with open(self.filename, 'r') as file :
            for line in file :
                title, description, start_date, end_date, done = line.split(", ")
                end_date = None if end_date == 'None' else end_date
                done = False if done.strip('\n') == 'False' else True
                all_tasks.append({'title' : title, 'description' : description, 'start_date': start_date, 'end_date':end_date, 'done':done})
            
            return all_tasks

    def due_date(self, start, end) :
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
        delta_date = end_date - start_date
        return f'{delta_date.days} days left.'

    def print_table(self, tasks):
        formatted_tasks = []
        for number, task in enumerate(tasks, 1):
            if task['start_date'] and task['end_date'] :
                due_date = self.due_date(task['start_date'], task['end_date'])
            else :
                due_date = 'Open'
            formatted_tasks.append({'no.':number, **task, 'due_date':due_date})
        print(tabulate(formatted_tasks, headers = 'keys'))

    def display(self, args) :
        all_task = self.list_all_tasks()
        unchecked_tasks = self.list_tasks()
        if not all_task :
            print("There are no tasks. To add a task use add <task>")
            return
        
        if args.all:
            self.print_table(all_task)
        else :
            if unchecked_tasks:
                self.print_table(unchecked_tasks)
            else :
                print('All tasks are checked!')

    def check_task(self, args) :
        index = args.task
        tasks = self.list_all_tasks()
        if index <= 0 or index > len(tasks) :
            print(f'Task number ({index}) does not exist!')
            return
        
        tasks[index-1]['done'] = True
        with open(self.filename,'w') as file :
            for task in tasks :
                self.add_task(Namespace(**task))

    def remove(self, args) :
        tasks = self.list_all_tasks()
        if args.task :
            index = args.task
        else :
            index = len(tasks) - 1

        if index <= 0 or index > len(tasks) :
            print(f'Task number ({index}) does not exist!')
            return
        
        tasks.pop(index - 1)
        with open(self.filename,'w') as file :
            for task in tasks :
                self.add_task(Namespace(**task))

    def reset(self, *args) :
        with open(self.filename,'w') as file :
            file.write('')
            print('You have deleted all tasks')

        

    
