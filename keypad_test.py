# This is the driver for the habitpi keypad, and code to test it.

# Copyright (C) 2020 Jason A Bright

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# import dependencies
import RPi.GPIO as GPIO
import time
import configparser

def poll_keypad():
    # This function will return the key that has been pressed

    # dictionary of buttons based on "coordinates"
    button = {(0,0):'1',
              (0,1):'2',
              (0,2):'3',
              (0,3):'A',
              (1,0):'4',
              (1,1):'5',
              (1,2):'6',
              (1,3):'B',
              (2,0):'7',
              (2,1):'8',
              (2,2):'9',
              (2,3):'C',
              (3,0):'*',
              (3,1):'0',
              (3,2):'#',
              (3,3):'D',
              (4,4):' '}

    # Set up the config parser, and read in the config file
    config = configparser.ConfigParser()
    config.read('habitpi.conf')

    # set up the GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    COL1 = config['KeypadPinouts'].getint('Column1')
    COL2 = config['KeypadPinouts'].getint('Column2')
    COL3 = config['KeypadPinouts'].getint('Column3')
    COL4 = config['KeypadPinouts'].getint('Column4')
    ROW1 = config['KeypadPinouts'].getint('Row1')   
    ROW2 = config['KeypadPinouts'].getint('Row2')
    ROW3 = config['KeypadPinouts'].getint('Row3')
    ROW4 = config['KeypadPinouts'].getint('Row4')

    GPIO.setup(COL1,GPIO.OUT)
    GPIO.setup(COL2,GPIO.OUT)
    GPIO.setup(COL3,GPIO.OUT)
    GPIO.setup(COL4,GPIO.OUT)
    GPIO.setup(ROW1,GPIO.IN)
    GPIO.setup(ROW2,GPIO.IN)
    GPIO.setup(ROW3,GPIO.IN)
    GPIO.setup(ROW4,GPIO.IN)

    # create lists so that we can iterate through them
    cols=[COL1,COL2,COL3,COL4]
    rows=[ROW1,ROW2,ROW3,ROW4]

    # some default values - 4,4 will never be returned from the keypad
    # so that is assigned ' ' in the dictionary, and pressed is assigned to that
    coord = (4,4)
    pressed = ' '

   # This is the meat of the driver.
   # 1. keep going until a button is pressed
   # 2. iterate through the columns, setting each one to high, and then...
   # 3. iterate through the rows, looking for a returned voltage
   # 4. When a returned voltage is found, we know the coordinates of the button
   #    that was pressed, so we can look that up to return the dictionary
   # (Note, I think that I have the rows an columns switched, but it works!)

    while pressed == ' ':
        for col in range(0,len(cols)):
            GPIO.output(cols[col],GPIO.HIGH)
            for row in range(0,len(rows)):
                if GPIO.input(rows[row]):
                    coord = (col,row)
            GPIO.output(cols[col],GPIO.LOW)
            pressed = button[coord]
            time.sleep(.05)
    return pressed

if __name__ == '__main__':
    pressed_button = None
    print("Keypad Test v0.1")
    print("Copyright (C) 2020 Jason Bright")
    print("This program comes with ABSOLUTELY NO WARRANTY")
    print("For details, see the license.md file")
    print("This is free software, and you are welcome to redistribute it under certain conditions")
    print("--------------------------------------------------------------------------------------")
    print("")
    print("Press D on the keypad to end")
    
    while pressed_button != 'D':
        pressed_button = poll_keypad()
        print ("Returned button = ",pressed_button)

