from datetime import datetime

from googleapiclient.discovery import build

from src.utils import load_credentials, CREATE_EVENT_FIELDS, display_events, DEFAULT_CALENDAR, DEFAULT_TIMEZONE 


class Calendar:
    def __init__(self):
        self.creds = load_credentials()
        self.service = build('calendar', 'v3', credentials=self.creds)

    def list_next_events(self, n_events=20, calendar_id='primary'):
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


    # 10/10/2020t20:50
    def create_event(self,args):
        # parse datetimes
        data = {
            "description" : args.d,
            "summary": args.b,
            "start" : args.s,
            "end" : args.e,
            "calendar" : args.c,
        }
        print(data)
