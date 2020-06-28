# Notes and Plans for Habit Pi
-----------------------
These are things that I remember and don't want to forget on this project.  They're in no particular order to start, and I may organize as I go.

X Look at SQLite to see if it might work later
	This looks promising - fairly easy to use.  Need to diagram exactly what I'm thinking about.
- learning about arrays of dictionaries in python
- send data from pi to desktop securely
- learn about multisegment displays
- continue to learn about git
- need to have a way for the pi to update
- dim displays
- LED's to indicate whether the goal was done today or not?
- Figure out pinouts - do I need to learn shift registers?
- Synch to desktop to back up data, and for data analysis.


## To-Do's
-[X] document the displays for the user
-[X] document the inputs for the user
-[ ] write a function to diplay numbers on a 4x7 segment display
-[ ] write a function for handling numpad inputs
-[x] order breadboards and parts
-[ ] wire up interfaces on breadboard
-[ ] write functions to pass data off to server
-[ ] bill of materials
-[ ] order rgb LED
-[ ] solder board, rather than breadboard

## Displays
- 4 status lights to indicate whether a habit has been done each day.  (Lit up if it has)
- 4 x 7 segment display to indicate numeric information:
	- subsequent days for each habit (maybe first # = habit number, then space, then days complete)
	- current weight
	- change in weight from yesterday
	- time
- status light
	- green = on, network connection
	- blue = needs restart (for updates)
	- red = on, no network connection

## Inputs
- 16 key pad for entry
	- indicate habit for day by pressing letter.
	- undo by pressing # and then the letter.
	- record weight by pressing * then weight - decimal will always be after the 3rd digit
	- restart / update by pressing *#*# - confirm after that?
	- dim display?

## Things to record
- Habits
	- complete or not?
	- Time completed
	- weight
	- time of weight recording


