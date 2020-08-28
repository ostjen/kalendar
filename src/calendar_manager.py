from src.calendar_actions import Calendar
from src.utils import display_events


class CalendarManager:
    def __init__(self, argument):
        self.argument = argument

    def execute(self):
        calendar = Calendar()
        action = self.argument[1]

        if action == 'list':
            events = calendar.list_next_events()
            display_events(events)

        elif action == 'find':
            search_event = self.argument[2]
            events = calendar.list_next_events()
            for event in events:
                if event['summary'] == search_event:
                    display_events([event])
