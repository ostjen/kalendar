import sys
from calendar_manager import CalendarManager
from setup import setup


def execute_from_command_line(argv):
    if argv[1] == 'setup':
        setup()
    else:
        manager = CalendarManager(argv)
        manager.execute()


if __name__ == '__main__':
    execute_from_command_line(sys.argv)
