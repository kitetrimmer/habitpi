# This will add a sample entry for testing/development it is not intended for production
# It will add 2 records - both for habit 1, with todays's date/time and tomorrow's date/time

import sqlite3
import datetime

#establish a connection to the habitpi.db, set up a cursor, and populate a date in the 'today' variable
conn = sqlite3.connect('habitpi.db',detect_types = sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()
today = datetime.datetime.now()

#build a tuple of what to insert for the first row, and insert it into the database
habit_tuple1 = (1,today,1)
insert_with_param = """INSERT INTO HABITS(HABIT, HABIT_DATE,CONT_DAYS) VALUES (?,?,?);"""
cursor.execute(insert_with_param,habit_tuple1)

#build a tuple of what to insert for the second row (basically add 1 day to the date, and set the consecutive
#days to 2, and then insert into the db
t = today + datetime.timedelta(days=1)
print("type t = ",type(t))
data_tuple2 = (1,t,2)
cursor.execute(insert_with_param,data_tuple2)

# commit the changes and close the connection
conn.commit()
conn.close()

