import sqlite3
import datetime
#TODO: Need to see if the habitpi.db exists - if so, back it up.  If a backup exists, remove the backup, and 
# back up the current habitpi.db

conn = sqlite3.connect('habitpi.db',
                        detect_types = sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

# Create a table for habits to be tracked.  
# Table stores:
# The number of the habit (should be 1-4)
# the date of the habit 
# and the number of continuous days (which will be incremented as long as there is an entry for yesterday
conn.execute('''CREATE TABLE HABITS
        (HABIT INT NOT NULL,
        HABIT_DATE timestamp NOT NULL,
        CONT_DAYS INT NOT NULL);''')
        

# Table for tracking weight - simple enough, just the date and the weight.
conn.execute('''CREATE TABLE WEIGHT
        (ID INT PRIMARY KEY NOT NULL,
        WDATE TIMESTAMP NOT NULL,
        WEIGHT REAL NOT NULL);''')

#TODO: Need to catch errors and flash codes on the LED's based on status.

