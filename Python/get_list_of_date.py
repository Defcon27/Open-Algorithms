from datetime import datetime
from dateutil import parser
import datetime as dt
from dateutil.relativedelta import relativedelta

def get_first_date(date):
    date = parser.parse(date)
    
    date = datetime(date.year, date.month, 1)
    
    return date.strftime('%Y-%m-%d')

def get_end_date(date):
    datetimes = parser.parse(date)
    next_month = datetimes.replace(day=28) + dt.timedelta(days=4)  
    last_date = (next_month - dt.timedelta(days=next_month.day)).strftime('%Y-%m-%d')

    return last_date

def get_list_date(firstDate,endDate):
    """
    create list of Date
    """

    firstDate = datetime.strptime(firstDate, '%Y-%m-%d').date()
    endDate = datetime.strptime(endDate, '%Y-%m-%d').date()

    listOfDate = []
    
    while firstDate < endDate:
        print(firstDate)
        listOfDate.append(firstDate.strftime('%Y-%m-%d'))
        firstDate += relativedelta(days=1)
    else:
        listOfDate.append(firstDate.strftime('%Y-%m-%d'))
    
    return listOfDate 

# input your date
date = '2020-05-05'

firstDate = get_first_date(date)
endDate = get_end_date(date)

print(get_list_date(firstDate,endDate))