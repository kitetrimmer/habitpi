# HabitPi

This is a  project that I am starting to track habits using a Raspberry Pi.  

## Vision
The project will implement a box.  The box will have a 16 digit display, 4 LED's, and a 4 digit seven segment display.  It will be used for tracking habits and weight.  If a habit has not been completed for the day, the LED for that habit will either be on or off (user configurable).  When that habit is completed for the day, it will display the number of consecutive days that the habit has been completed. (sort of like this factory has gone XXX days without an accident.)  It will be possible to key a weight in once per day, and today's weight can be displayed, along with the change in weight since yesterday (possibly configurable number of days if watching daily is too much).

## Components in the repo:
**dbtools.py**: this is a tool that is used for testing and configuring the sqlite database that is used to store data.  It can be used to reset the database, add test data, drop and add tables, etc.
**habitpi.py**: this will be the main code base for the project.  It is what will run to keep track of everything going on.
**habitpi\_display.py**: This is a test program for the output of the data to the LED's.  You can test just the habit LED's, just a single number or character, the 4 segment multiplexing, or the habits an mutiplexing.
**habitpi.conf**: This is a configuration file that stores configuration for the software.
## Components yet to develop:
**keypad**: Need to generate code to read input from the 16 key pad.

## Next steps (as of July 28,2020):
* finish the electronics on the breadboard (including soldering the leads to the keypad)
* Develop the keypad driver
* Start stitching things together in the habitpi.db
* Start developing the UI - what buttons do what, etc.
* Move the electronics off of the breadboard and onto protoboard(s)
* Design/choose a case for the project

## This project is being built to the tune of:
* Hawaiian Folk Radio (google music)
* Essential House Radio (google music)
