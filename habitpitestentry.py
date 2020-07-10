# This will add a sample entry for testing/development it is not intended for production

import sqlite3
conn = sqlite3.connect('habitpi.db')

conn.execute("INSERT INTO HABIT1(ID,HABIT1,CONT_DAYS) \
        VALUES (1,datetime('now','localtime,),1)");

conn.execute("INSERT INTO HABIT1(ID,HABIT1,CONT_DAYS) \
        VALUES (2,datetime('now','+1 day','localtime',2)");
conn.commit()

