# contains database management tools for testing the applications

import sqlite3
import datetime
import os
import time
import shutil

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def add_weight_data():

    # This will add sample records for testing/development.  It is not intended for production.
    # It will add 2 records to the weight table, with today's date and tomorrow's date.

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

def add_habit_data():
    
    # This will add a sample entry for testing/development it is not intended for production
    # It will add 2 records - both for habit 1, with todays's date/time and tomorrow's date/time
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

def confirm(tname):
    print(f"OK to drop {tname}?")
    sel = input("Press Y to confirm")
    if sel == "Y" or sel == "y":
        return True
    else:
        return False

def drop_habit_table():
    if confirm("habits") == True:
        print("Dropping Habits table")
        conn = sqlite3.connect()
        cursor = conn.cursor()
        cursor.execute("""DROP TABLE HABITS""")
        conn.close()
        print("Habits table dropped")

def drop_weight_table():
    if confirm("weight") == True:
        print("Dropping Weight table")
        conn = sqlite3.connect()
        cursor = conn.cursor()
        cursor.execute("""DROP TABLE WEIGHT""")
        conn.close()
        print("Weight table dropped")

def drop_table_menu():
    print("Choose table to drop")
    print("1. HABITS")
    print("2. WEIGHT")
    print("3. BOTH")
    print("Any other selection to abort")
    sel = input("Selection: ")

    if sel == 1:
        drop_habit_table()
    elif sel == 2:
        drop_weight_table()
    elif sel == 3:
        drop_habit_table()
        drop_habit_table()
    else:
        print("Aborting....")
def delete_habitpidb():
    # This is a function to delete the habitpi.db file
    confirm = input(color.RED + "Are you sure you want to delete habitpi.db?"+color.END)
    if confirm == 'Y' or confirm == "y":
        os.remove("habitpi.db")   
        print("habitpi.db has been removed")
        return
    else:
        return

def create_habitdb():

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
            (WDATE TIMESTAMP NOT NULL,
            WEIGHT REAL NOT NULL);''')

    #TODO: Need to catch errors and flash codes on the LED's based on status.

def reinitialize():
    # function to delete the habitpi database and rebuild it
    delete_habitpidb()
    create_habitdb()    

def create_habit_table():
    # This is a function that will create the habit table if it doesn't exist
    
    # create the connection to the database
    conn = sqlite3.connect('habitpi.db',
                        detect_types = sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    
    # create a cursor, and then a query to see if the tablename exists in the database
    c = conn.cursor()    
    c.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='HABITS'""")

    d = c.fetchone()
    #if the count is not 1, then table does not exist
    if d[0]==1: 
        print(color.RED+'The HABITS table already exists!'+color.END)
        input('Press ENTER to continue')
        return
    else:
    # Create a table for habits to be tracked.  
    # Table stores:
    # The number of the habit (should be 1-4)
    # the date of the habit 
    # and the number of continuous days (which will be incremented as long as there is an entry for yesterday
        conn.execute('''CREATE TABLE IF NOT EXISTS HABITS
            (HABIT INT NOT NULL,
            HABIT_DATE timestamp NOT NULL,
            CONT_DAYS INT NOT NULL);''')
        print('Created the HABITS table')
        input('Press ENTER to continue')
        return

def create_weight_table():
    # This is a function that will create the weight table if it doesn't exist
    
    # create the connection to the database
    conn = sqlite3.connect('habitpi.db',
                        detect_types = sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    
    # create a cursor, and then a query to see if the tablename exists in the database
    c = conn.cursor()    
    c.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='WEIGHT'""")

    d = c.fetchone()
    #if the count is not 1, then table does not exist
    if d[0]==1: 
        print(color.RED+'The WEIGHT table already exists!'+color.END)
        input('Press ENTER to continue')
        return
    else:
    # Create a table for habits to be tracked.  
    # Table stores:
    # date of the record
    # the weight at that date
        conn.execute('''CREATE TABLE IF NOT EXISTS WEIGHT
                (WDATE TIMESTAMP NOT NULL,
                WEIGHT REAL NOT NULL);''')
        print('Created the WEIGHT table')
        input('Press ENTER to continue')
        return

def add_table_menu():
    #This will add individual tables if they've been dropped
    
    print("---------------------")
    print("Choose which table to add")
    print("1. Habits")
    print("2. Weight")
    print("3. Both")
    sel = int(input("Choose one: "))

    if sel == 1:
        create_habit_table()
    elif sel == 2:
        create_weight_table()
    elif sel == 3:
        create_habit_table()
        create_weight_table()
    else:
        return

def backupdb():
    # This function will backup the habitpi.db
    
    filename = "habitpidbbak.db"
    print("")
    # Get a filename to back up to, using filename variable as default
    fn=input(f"Please provide the filename to backup to [{filename}] :")
    # if the user provided a filename, use it, otherwise use the default.
    if fn != "":
        filename = fn
    # check to see if the filename exists.  If it does, ask if the user wants to overwrite
    # and then overwrite if appropriate.
    if os.path.isfile(filename):
        print(color.RED+"Filename already exists"+color.END)
        delfile = input("Would you like to overwrite it?")
        if delfile == "Y" or delfile == "y":
            shutil.copy("habitpi.db",filename)
            print(color.GREEN)
            print(f"habitpi.db backed up to {filename}")
            print(color.END)
            input("Press Enter to continue")
            return
        else:
    # if the user doesn't want to overwrite, then start over and ask for another file name
            backupdb()
    # if the filename doesn't already exist, copy the file over.
    else:
        shutil.copy("habitpi.db",filename)
        print(color.GREEN)
        print(f"habitpi.db backed up to {filename}")
        print(color.END)
        input("Press Enter to continue")
        return

def db_menu():
    try:
        exit = False

        while exit == False:
            os.system("clear")
            print("Testing Database Tools")
            print("----------------------")
            print("")
            print("1. Backup Habitpi database")
            print("2. Reinitialize Habitpi database")
            print("3. Add Habit test data")
            print("4. Add Weight test data")
            print("5. Add both Habit and Weight test data")
            print("6. Drop tables from Habitpi database")
            print("7. Add table to Habitpi database")
            print("8. Delete habitpi.db")
            print("9. Exit")
            print("")
            sel = int(input("Pick an item: "))

            if not(1 <= sel <= 9):
                raise ValueError

            if sel == 1:
                backupdb()
            elif sel == 2:
                reinitialize()
            elif sel == 3:
                add_habit_data()
            elif sel == 4:
                add_weight_data()
            elif sel == 5:
                add_habit_data()
                add_weight_data()
            elif sel == 6:
                drop_table_menu()
            elif sel == 7:
                add_table_menu()
            elif sel == 8:
                delete_habitpidb()
            elif sel == 9:
                exit = True
        return
    except TypeError:
        print("Value must be an integer")
        db_menu()
    except ValueError:
        print("")
        print(color.RED + "Value must be from 1 to 8" + color.END)
        print("")
        db_menu()

if __name__ == "__main__":
    db_menu()
