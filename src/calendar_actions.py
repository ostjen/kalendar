from datetime import datetime

from googleapiclient.discovery import build

from src.utils import load_credentials, display_events, CREATE_EVENT_FIELDS


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
        display_events(events)
        return events

    def create_event(self, **kwargs):
        # sanitize body
        event_body = {key: value for key, value in kwargs.items() if key in CREATE_EVENT_FIELDS}
        print(event_body)
        event = self.service.events().insert(calendarId='primary', body=event_body).execute()


# TODO timezone awareness
if __name__ == '__main__':
    cal = Calendar()
    now = datetime.now().isoformat('T')
    cal.create_event(summary='summary',
                     description='description',
                     start={
                         'dateTime': now,
                         'timeZone': 'America/Sao_Paulo',
                     },
                     end={
                         'dateTime': now,
                         'timeZone': 'America/Sao_Paulo',
                     })
