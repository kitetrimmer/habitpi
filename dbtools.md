# HabitPi Database Tools
version 0.1

## Background on application
This application was developed to support the HabitPi project during development.  It is used to create the habitpi.db file, and allow test data to be added, tables to be dropped, etc.

## Main Menu

### 1. Backup Habitpi database
This option will allow the habitpi.db file to be copied to another filename of the user's choice in the same directory.  The application will check to see if that file already exists, and if so, it will prompt the user to overwrite.  This is useful so that when working with the other tools, you can revert to the original database.  **IT IS RECOMMENDED THAT THIS BE RUN PRIOR TO ANY OTHER ACTIVITIES IN THE TOOL!**

### 2. Reinitialize Habitpi database
This option will drop and recreate both the habit and the weight tables.

### 3. Add Test Data
This option will bring up a submenu to allow the user to select the tables to add test data to:
	1. Habits
	2. Weight
	3. Both

When adding test data to the habits table, the program will add 2 records to the Habit table:

|Habit        |Habit Date         |Consecutive Days|
|-------------|-------------------|----------------|
| 1           | Today's Date/Time | 1              |
| 1           | Today + 1 day     | 2              |

When adding test data to the weight table, the program will add 2 records to the Weight table:

|Weight Date        | Weight    |
|-------------------|-----------|
| Today's Date/Time | 100.0     |
| Today + 1 day     | 98.0      |

### 4. Drop tables from Habitpi database

This option will bring up a submenu to allow you to choose which tables in the habitpi database to drop.  Options are:
	1. Habits
	2. Weight
	3. Both (drops both the Habits table and the Weight table)

### 5. Add table to Habitpi database

This option will bring up a submenu to allow you to choose to add a table or tables.  The options are:
	1. Habits
	2. Weight
	3. Both
_If the tables already exist in the database, the tables will not be overwritten._

### 6. Delete habitpi.db

**This option will completely remove the habitpi.db file.**  
If this option is selected, the program will end.  The next time the dbtools run, the habitpi.db will be created if it does not exist.  This could happen if the user copied the backup database back to habitpi.db.

###7. Show data in database
This option will show all of the data in the database, for both the habits table and the weight table.  If the table does not exist for any reason, it will display that.  This is useful for examining what data is in the database while working on other parts of the program.

### 8. Exit

This option will exit from the application.
