# This will add a sample entry for testing/development it is not intended for production

import sqlite3
import datetime
conn = sqlite3.connect('habitpi.db')
cursor = conn.cursor()
today = datetime.datetime.now()

data_tuple1 = (1,today,1)
insert_with_param = """INSERT INTO HABITS(HABIT, HABIT_DATE,CONT_DAYS) VALUES (?,?,?);"""
cursor.execute(insert_with_param,data_tuple1)
        
t = today + datetime.timedelta(days=1)
data_tuple2 = (1,t,2)
cursor.execute(insert_with_param,data_tuple2)
        
conn.commit()
conn.close()

