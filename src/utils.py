import os
import pickle
from pprint import pprint

from config.settings import DISPLAY_FIELDS

CREATE_EVENT_FIELDS = ['summary', 'location', 'description', 'start', 'end', 'reccurence', 'attendees', 'reminders']

def load_credentials():
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            return pickle.load(token)
    else:
        return None


def display_events(events):
    for event in events:
        # parse timestamps into human readable format
        event['start'] = event['start']['dateTime'][:10] + ' -> ' + event['start']['dateTime'][11:16]
        event['end'] = event['end']['dateTime'][:10] + ' -> ' + event['end']['dateTime'][11:16]
        event_display = {key:value for key,value in event.items() if key in DISPLAY_FIELDS}
        pprint(event_display,indent=2)
        print('\n')
