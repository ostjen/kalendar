from datetime import datetime
import argparse

def valid_date(date):
    try:
        return datetime.strptime(date,"%d/%m/%Y-%H:%M")
    
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(date)
        raise argparse.ArgumentTypeError(msg)





