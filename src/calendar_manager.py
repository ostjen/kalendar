from src.calendar_actions import Calendar


class CalendarManager:
    def __init__(self, argument):
        self.argument = argument

    def execute(self):
       calendar = Calendar()
       if self.argument[1] == 'list':
           calendar.list_next_events()

