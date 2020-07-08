import sqlite3

#TODO: Need to see if the habitpi.db exists - if so, back it up.  If a backup exists, remove the backup, and 
# back up the current habitpi.db

conn = sqlite3.connect('habitpi.db')

# Create a table for each habit to be tracked.  Simple table just the date of the habit (stored as HABITn)
# and the number of continuous days (which will be incremented as long as there is an entry for yesterday
conn.execute('''CREATE TABLE HABIT1
        (ID INT PRIMARY KEY NOT NULL,
        HABIT1 INT NOT NULL,
        CONT_DAYS INT NOT NULL);''')
        
conn.execute('''CREATE TABLE HABIT2
        (ID INT PRIMARY KEY NOT NULL,
        HABIT2 INT NOT NULL,
        CONT_DAYS INT NOT NULL);''')

conn.execute('''CREATE TABLE HABIT3
        (ID INT PRIMARY KEY NOT NULL,
        HABIT3 INT NOT NULL,
        CONT_DAYS INT NOT NULL);''')

conn.execute('''CREATE TABLE HABIT4
        (ID INT PRIMARY KEY NOT NULL,
        HABIT4 INT NOT NULL,
        CONT_DAYS INT NOT NULL);''')

# Table for tracking weight - simple enough, just the date and the weight.
conn.execute('''CREATE TABLE WEIGHT
        (ID INT PRIMARY KEY NOT NULL,
        WDATE DATE NOT NULL,
        WEIGHT REAL NOT NULL);''')

#TODO: Need to catch errors and flash codes on the LED's based on status.

