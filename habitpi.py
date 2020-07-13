# This is the master file for habitpi python code

import sqlite3
import datetime

def find_midnights():
    # This function returns a tuple of datetimes.
    # first value is midnight yesterday and second is midnight today
    # this is going to be used to see if something happened yesterday in the query
    today = datetime.datetime.now()
    mid_today = today.replace(hour=0,minute=0,second=0,microsecond=0)
    t = today.day
    y = t -1
    mid_yesterday = mid_today.replace(day=y)
    return(mid_yesterday,mid_today)

def update_habit(num):
    import datetime
    """ Updates the given habit in the habitpi databasei

    This function will add the current date and the continuous days to a given habit.  Valid numbers are between 0 and 3."""
    #TODO: turn this "num is an int?" into an actual test for debugging
    print("num is an int? ",isinstance(num,int))    

    conn = sqlite3.connect('habitpi.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    habit_data = conn.cursor()
    #TODO: add the tuple from find_midnights to num, and use it in the query below
    habit_data.execute("SELECT HABIT,HABIT_DATE,CONT_DAYS FROM HABITS WHERE HABIT = ? AND HABIT_DATE BETWEEN ? and ? ;",(num,))
    for row in habit_data:
        print(row)
        print("-----------")
        print(row[0])
        print(row[1].date())
        print(type(row[1].date()))
        print(row[2])

update_habit(1)
