from importlib.metadata import entry_points
from setuptools import setup

setup (
    name = 'taskaty',
    version = '0.1.0',
    description = 'A simple command-line Task-app written in python',
    author = 'Osama Alsalafi',
    intsall_requires = ['tabulate'],
    entry_points = {
        'console_scripts' : [
            'taskaty=taskaty:main',
        ],
    },
)