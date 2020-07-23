# This is the master file for habitpi python code

# update_habit
# TODO: test incremental update functions
# TODO: error trapping for update_habit
# TODO:      - did a number get passed
# TODO:      - could we get a connection to the db

# Other functions
# TODO: create test data generator for weight
# TODO: create updater for weight
# TODO: create reader for weight
# TODO: start creating displays
# TODO: config file - how does incremental updates get treated (1x/day, total number of times, last 24 hours?)


import sqlite3
import datetime
import sys

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
    """ Updates the given habit in the habitpi databasei

    This function will add the current date and the continuous days to a given habit.  Valid numbers are between 0 and 3."""
    try: 
        if not(isinstance(num,int)):
            raise TypeError 
        if not(0<=num<=3):
            raise ValueError 
        conn = sqlite3.connect('habitpi.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        check = conn.cursor()
       
        # this section checks to see if we had a record recorded yesterday.

        query_param = (num,) + find_midnights()
        check.execute("""SELECT HABIT,HABIT_DATE,CONT_DAYS 
                              FROM HABITS 
                              WHERE HABIT = ? AND HABIT_DATE BETWEEN ? and ? ;""",query_param)
        # If we don' find a record for yesterday, then we need to reset the number of days
        nullcheck = check.fetchone() 
        if nullcheck == None:
            curr_count = 1
        else:
            curr_count = nullcheck[2]+1   
        
        #Now that we know what the current count should be, we can write out our record.
        entry_tuple = (num, datetime.datetime.now(),curr_count)
        entry = conn.cursor()
        entry_query="""INSERT INTO HABITS(HABIT, HABIT_DATE,CONT_DAYS) VALUES (?,?,?);"""
        entry.execute(entry_query,entry_tuple)
        
        #TODO: need to call the display refreshing routines (that aren't written yet)
        conn.commit()
    except TypeError:
            print(f"Habit number passed was {type(num)} - expected an integer")
    except ValueError:
            print(f"Habit number must be between 0 and 3 inclusive.  {num} was passed.")
    except sqlite3.Error as er:
        print(f"SQLite error {' '.join(er.args)}")
        print(f"Exception class is {er.__class__}")

    finally:
        conn.close()

def show_all_habits():
    # This will show all the records in the habitpi.db.  
    # It is currently going to be used for testing, but may be useful elsewhere.

    # import dependencies
    import sqlite3
    import datetime

    # establish a connection, and define a cursor.
    conn = sqlite3.connect('habitpi.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = conn.cursor()
    
    # loop through each of the habits 0-3
    for habit in range (0,4):
         print('habit = ',habit)
         query = """SELECT * FROM HABITS WHERE HABIT = ?"""
         cursor.execute(query,(habit,))
         test = cursor.fetchone()
         # test is a single row row from the cursor given a certain habit
         # if it is empty, print "no records"
         if test == None:
            print("no records")
         else:
         # if test is not empty, then run the query again to get all the records, and display them.    
             print("HABIT   HABIT_DATE            CONT_DAYS")
             cursor.execute(query,(habit,))
             data = cursor.fetchall()
             for rows in data:
                 print(f'{rows[0]}       {rows[1].strftime("%Y-%m-%d %H:%M:%S")}   {rows[2]}')

def show_weight():
    # This is a function to show all of the weight data

    conn = sqlite3.connect('habitpi.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM WEIGHT;""")
    recs = cursor.fetchall()
    if recs == None:
        print(color.RED + "No Weight Records" + color.END)
    else:
        print("Date                 Weight      Weight Change")
        for a in range (0,len(recs)):
            if a == 0:
                print(recs[a][0].strftime("%Y-%m-%d"),"         ",recs[a][1],"      N/A")
            else:
                print(recs[a][0].strftime("%Y-%m-%d"),"         ",recs[a][1],"     ",round((recs[a][1]-recs[a-1][1]),1))

def write_weight_to_db(weight):
    #This function will write the weight information to the database

    conn = sqlite3.connect('habitpi.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = conn.cursor()
    #build a tuple of the current datetime and the weight passed, pass this into the query, commit, and close the connection    
    wt_tuple = (datetime.datetime.now(),weight)
    query = """INSERT INTO WEIGHT (WDATE,WEIGHT) VALUES (?,?)"""
    cursor.execute(query,wt_tuple)
    conn.commit()
    conn.close()

def update_weight():
    # This is the function to update weight

    # Establish a connection to the database
    conn=sqlite3.connect('habitpi.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

    # Check to see if there's been an update today
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM WEIGHT WHERE date(WDATE)=date('now')""")
    cdata = cursor.fetchone()
    print("cdata = ",cdata)
    # If there is no record for data, simply ask for the weight and record it
    if cdata == None:
        weight = float(input(f"Input weight for {datetime.date.today()}: "))
        write_weight_to_db(weight)    
    # If there is data, ask whether to overwrite, and if so, ask for the weight,
    # delete the record from today, and write the new record.
    else:
        print(f"There is already a weight of {cdata[1]} recorded for today")
        sel = input("Would you like to overwrite this weight? ")
        if sel == "Y" or sel == "y":
            weight = float(input(f"Input weight for {datetime.date.now()}: "))
            query = ("""DELETE FROM WEIGHT WHERE date(WDATE)=date('now')""")
            cursor.execute(query)
            cursor.commit()
            write_weight_to_db(weight)
    # close the connection
    conn.close() 


def habitpi_menu():
    try:
        sel = 0
        while sel != 4:
            
            print("HabitPi Main Menu")
            print("version 0.1")
            print("-----------------")
            print("1. Habits")
            print("2. Weight")
            print("3. Show Data")
            print("4. Exit")
            print("")
            sel = int(input("Select One: "))
            
            if 1<=sel<=4:
                if sel==1:
                    show_all_habits()
                    hnum =int(input('Which habit? '))
                    update_habit(hnum)
                    show_all_habits()
                elif sel==2:
                    update_weight()
                    show_weight()
                elif sel==3:
                    show_all_habits()
                    show_weight()
            else:
                raise ValueError

    except ValueError:
        print(color.RED + "Selection must be a number between 1 and 4" + color.END)
        habitpi_menu()

if __name__ == "__main__":
    habitpi_menu()
