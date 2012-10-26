from distutils.core import setup
from distutils.cmd import Command
from subprocess import Popen


class VirtualenvCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        process = Popen(["virtualenv", "--distribute", "env/"])
        process.communicate()


class RequirementsCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        process = Popen(["env/bin/pip", "install", "-r", "requirements.txt"])
        process.communicate()


class RunServerCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        process = Popen(["env/bin/python", "manage.py", "runserver", "0.0.0.0:8000"])
        process.communicate()


setup(
    cmdclass={
        'run': RunServerCommand,
        'env': VirtualenvCommand,
        'requirements': RequirementsCommand
    },
)
