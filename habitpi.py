# This is the master file for habitpi python code

import sqlite3
import datetime

def update_habit(num):
    import datetime
    """ Updates the given habit in the habitpi database

    This function will add the current date and the continuous days to a given habit.  Valid numbers are between 0 and 3."""
    print("num is an int? ",isinstance(num,int))    
    conn = sqlite3.connect('habitpi.db')

    # Build the SQL Script for yesterday
    # TODO: change the query to select the datetime, but use a "WHERE date(HABIT_DATE) = ? /  *yesterday*"
    # TODO: create a yesterday(date) function to return yesterday's date.
    # TODO: create a tomorrow(date) function to return tomorrow's date.  (not sure why I need this, but why not!

    yesterday = conn.cursor()
    yesterday.execute("SELECT HABIT,date(HABIT_DATE),CONT_DAYS FROM HABITS WHERE HABIT = ?;",(num,))
    #yesterday.fetchall()
    for row in yesterday:
        print (row)
        print (row[1])
        print (row[2])
        print (type(row[2]))

update_habit(1)
