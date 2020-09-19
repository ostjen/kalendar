from src.validators import valid_date
from src.calendar_actions import Calendar
from src.utils import display_events,DEFAULT_CALENDAR
from argparse import ArgumentParser

class CalendarManager:
    def __init__(self, argument):
        self.argument = argument

    def execute(self):
        calendar = Calendar()
        # the only positional arg
        action = self.argument[1]
        
        if action == 'list':
            events = calendar.list_next_events()
            display_events(events)

        elif action == 'find':
            search_event = self.argument[2]
            events = calendar.find_event(search_event)
            display_events(events)
        
        elif action == 'create':
            create_parser = ArgumentParser(description = 'create event')
            create_parser.add_argument('-d',help = 'description')
            create_parser.add_argument('-b',help = 'brief/summary')
            create_parser.add_argument('-s',help = 'start time',type=valid_date,required=True)
            create_parser.add_argument('-e',help = 'end time',type=valid_date,required=True)
            create_parser.add_argument('-c',default=DEFAULT_CALENDAR,help = 'calendar(default = primary')
            args = create_parser.parse_known_args()[0]
            calendar.create_event(args)
