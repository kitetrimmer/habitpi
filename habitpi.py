# This is the master file for habitpi python code

def update_habit(num):
    """ Updates the given habit in the habitpi database

    This function will add the current date and the continuous days to a given habit.  Valid numbers are between 0 and 3."""
    
    # import sqlite, and create a connection to the habitpi database
    import sqlite3
    conn = sqlite3.connect('habitpi.db')
    
    # Build the SQL Script for yesterday
    yesterday = conn.execute("SELECT * FROM HABIT"+str(num)+";")
    for row in yesterday:
        print (row[1])
        ydate = row[1]
        print (row[2])
        ydays = row[2]

    print ("Yesterday's Date = ",ydate)
    print ("Yesterday's continuous days = ",ydays)

    #script = "UPDATE TABLE HABIT",num," SET HABIT",num," = datetime('now')"
    # HABIT1, CONT_DAYS

update_habit(1)
