import os
import pickle

CREATE_EVENT_FIELDS = ['summary','location','description','start','end','reccurence','attendees','reminders']

def load_credentials():
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            return pickle.load(token)
    else:
        return None

