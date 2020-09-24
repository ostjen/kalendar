from datetime import datetime
import argparse
from config.settings import DEFAULT_TIME_FORMAT 

def valid_date(date):
    try:
        return datetime.strptime(date,DEFAULT_TIME_FORMAT)
    
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(date)
        raise argparse.ArgumentTypeError(msg)





