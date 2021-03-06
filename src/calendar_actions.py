from datetime import datetime

from googleapiclient.discovery import build

from config.settings import DEFAULT_TIMEZONE, LIST_EVENTS_LIMIT, DEFAULT_CALENDAR
from src.utils import load_credentials, CREATE_EVENT_FIELDS, display_events 



class Calendar:
    def __init__(self):
        self.creds = load_credentials()
        self.service = build('calendar', 'v3', credentials=self.creds)

    def list_next_events(self, n_events=LIST_EVENTS_LIMIT, calendar_id=DEFAULT_CALENDAR):
        now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = self.service.events().list(calendarId=calendar_id, timeMin=now,
                                                   maxResults=n_events, singleEvents=True,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])
        return events


    def find_event(self, search_event):
        events = self.list_next_events()
        filtered_events = []
        for event in events:
            if event['summary'] == search_event:
                filtered_events.append(event)

        return filtered_events


    def create_event(self,args):
        data = {
            "summary": args.n,
            "description" : args.d,
            "start" : {
                'dateTime': args.s.isoformat(),
                'timeZone': DEFAULT_TIMEZONE
            },
             "end" : {
                'dateTime': args.e.isoformat(),
                'timeZone': DEFAULT_TIMEZONE
            }
        }
        event = self.service.events().insert(calendarId= args.c, body=data).execute()
        print('created event {{}}'.format(data['summary']))
