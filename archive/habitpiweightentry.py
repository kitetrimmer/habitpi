# This will add sample records for testing/development.  It is not intended for production.
# It will add 2 records to the weight table, with today's date and tomorrow's date.

import sqlite3
import datetime

conn = sqlite3.connect('habitpi.db',detect_types = sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()
today = datetime.datetime.now()

#build a tuple of what to insert for the first row, and insert into the database
weight_tuple=(today,100.0)
insert_query="""INSERT INTO WEIGHT(WDATE,WEIGHT) VALUES (?,?)"""
cursor.execute(insert_query,weight_tuple)

#build a tuple of what to insert for the second row, and insert into the database
t = today + datetime.timedelta(days=1)
weight_tuple2 = (t,98.0)
cursor.execute(insert_query,weight_tuple2)

#commit the changes and close the database
conn.commit()
conn.close()


