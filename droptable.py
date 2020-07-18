#This program will allow a user to select a table to drop
#It is intended for use during testing

import sqlite3

def confirm(tname):
    print(f"OK to drop {tname}?")
    sel = input("Press Y to confirm")
    if sel == "Y" or sel == "y":
        return True
    else:
        return False

def drop_habit_table():
    if confirm("habits") = True:
        print("Dropping Habits table")
        conn = sqlite3.connect()
        cursor = conn.cursor()
        cursor.execute("""DROP TABLE HABITS""")
        conn.close()
        print("Habits table dropped")

def drop_weight_table():
    if confirm("weight") = True:
        print("Dropping Weight table")
        conn = sqlite3.connect()
        cursor = conn.cursor()
        cursor.execute("""DROP TABLE WEIGHT""")
        conn.close()
        print("Weight table dropped")

if __name__ == "__main__":
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

