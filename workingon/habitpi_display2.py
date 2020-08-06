# habitpi_display.py: an application to test the displays for the habitpi project
# Copyright (C) 2020 Jason A. Bright


# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Contact Jason Bright at <jay><ay><bee><dot>kitetrimmer@gmail.com

# Some basic concepts:
# There are 2 595 shift registers that drive a 4 digit 7 segment display, and 4 led's.
# These 2 bytes are broken down as follows:
# first 4 bits: Habit List - which of the habit LED's should be lit up 
# next 4 bits: Digit List - which digit should be lit up (used in multiplexing)
# last 8 bits: Number List - which individual elements should be lit up to make the number

import RPi.GPIO as GPIO
import time
import configparser
import ast
from os import system

def setup_GPIO():
    import RPi.GPIO as GPIO
    import configparser
    
    config = configparser.ConfigParser()
    config.read('habitpi.conf')

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    CLOCK = config['LEDPinouts'].getint('Clock')
    DATA = config['LEDPinouts'].getint('Data')
    LATCH = config['LEDPinouts'].getint('Latch')

    GPIO.setup(DATA,GPIO.OUT)
    GPIO.setup(CLOCK,GPIO.OUT)
    GPIO.setup(LATCH,GPIO.OUT)

def send_one():
# this will send a 1 to the 595 chips.
    setup_GPIO()
    GPIO.output(DATA,GPIO.HIGH)
    GPIO.output(CLOCK,GPIO.HIGH)
    GPIO.output(CLOCK,GPIO.LOW)

def send_zero():
# sends a 0 to the 595 chips
    setup_GPIO()
    GPIO.output(DATA,GPIO.LOW)
    GPIO.output(CLOCK,GPIO.HIGH)
    #time.sleep(.001)
    GPIO.output(CLOCK,GPIO.LOW)

def latch():
    #latches the 595 chips to send data out to the LED's
    setup_GPIO()
    GPIO.output(LATCH,GPIO.HIGH)
    GPIO.output(LATCH,GPIO.LOW)

def generate_numlist(digit):
    # Looks up a digit to return the list for the number list
    
    # G F E D C B A DP (1 to turn off)
    num_dict = {'0':'[1,0,0,0,0,0,0,1)',
                '1':'[1,1,1,1,0,0,1,1]',
                '2':'[0,1,0,0,1,0,0,1]',
                '3':'[0,1,1,0,0,0,0,1]',
                '4':'[0,0,1,1,0,0,1,1]',
                '5':'[0,0,1,0,0,1,0,1]',
                '6':'[0,0,0,0,0,1,0,1]',
                '7':'[1,1,1,1,0,0,0,1]',
                '8':'[0,0,0,0,0,0,0,1]',
                '9':'[0,0,1,0,0,0,0,1]',
                '0':'[1,0,0,0,0,0,0,1]',
                ' ':'[1,1,1,1,1,1,1,1]'
                }
    #TODO: Add alpha characters
    digit_list = num_dict[digit]
    #TODO: Need to catch invalid values, and think about converting only numbers to strings.
    return digit_list

def habitLEDmenu():
    # Creates the habit list by asking the user whether to light up LED's
    setup_GPIO()

    habit_list = [0,0,0,0]
    for habit in range(0,4):
        sel = ''
        sel = input(f"Light up LED {habit}?")
        if sel == 'y' or sel == 'Y':
            habit_list[habit] = 1
        else:
            habit_list[habit] = 0
    return habit_list

def digitmenu():
    # a menu so that the user can select a digit to try for the first digit

    setup_GPIO()
    try:
        whole_list  = []
        habit_list = [0,0,0,0]
        digit_list = [1,0,0,0]
        sel = int(input("Pick a number from 0-9 to display on the first digit: "))
        if 0<=sel<=9:
            number_str = generate_numlist(str(sel))
            number_list= ast.literal_eval(number_str)  #I might be able to return a list from generate_numlist - might have to check that.
        else:
            raise ValueError
        
        whole_list = habit_list + digit_list + number_list
        print(str(whole_list))
        return whole_list

    except ValueError:
        print("Must be from 0 to 9 inclusive")
        digitmenu()
#    except TypeError:
#        print("Must be a number")

def display(disp_list):
    # takes a list and sends it to the 595 chips
    
    for var in disp_list:
            if var == 1:
                send_one()
            elif var == 0:
                send_zero()
            else:
                raise ValueError
    latch()
    return

def foursegmentdisplay(num,habit_list):
    # takes a number from the main menu, and a habit_list to build out a display
    # for the 4 segment display
    try:
        setup_GPIO()
        while True:
            if 0<=num<=9999:
                # Turn the number into something that is usable

                # turn the number into a string
                disp_string = str(num)
                # eliminate any decimal points
                show_string = disp_string.replace('.','')

                # pad with spaces so that a 1 digit number only shows on the rightmost display
                show_string= show_string.rjust(4, ' ')
                # build a list that shows where the decimal places are.
                dp_list = []
                dp_count = 0
                for a in range(0,len(disp_string)):
                    if disp_string[a] == '.':
                        dp_count += 1
                        dp_list.append(a-dp_count)

                # at this point we have a string with number to display, padded 
                # with spaces - show_string
                # and a list of digits that will need a decimal point - dp_list

                for a in range(0,len(show_string)):
                    if a == 0:
                        digit_list = [1,0,0,0]
                        number_str = generate_numlist(show_string[a])
                        number_list=ast.literal_eval(number_str)
                        if a in dp_list:
                            number_list[7] = 0
                    elif a == 1:
                        digit_list = [0,1,0,0]
                        number_str = generate_numlist(show_string[a])
                        number_list=ast.literal_eval(number_str)
                        if a in dp_list:
                            number_list[7] = 0
                    elif a == 2:
                        digit_list = [0,0,1,0]
                        number_str = generate_numlist(show_string[a])
                        number_list=ast.literal_eval(number_str)
                        if a in dp_list:
                            number_list[7] = 0
                    elif a == 3:
                        digit_list = [0,0,0,1]
                        number_str = generate_numlist(show_string[a])
                        number_list=ast.literal_eval(number_str)
                        if a in dp_list:
                            number_list[7] = 0
                    
                    else:
                        print("too many digits")
                    disp_list = habit_list + digit_list + number_list
                    display(disp_list)
                    time.sleep(.0005)
    except:
        display([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        return

def check_num(string):
    # checks to see if the number to display is valid, and if it has a decimal
    # keeps a float number, otherwise, sends an integer
    
    try:
        # try to see if the number is convertible to a float.  If it isn't, 
        # a ValueError will be thrown.  May as well keep this to use later.
        num=float(string)
        # check to see if the original string has a decimal point, and if not, 
        # return an integer of the string.
        if string.find('.') == -1:
            num = int(string)
        return num
    except ValueError:
        print("Expecting a number!")
        return

def mainmenu():
    # This is the main menu

    try:
        sel = 0
        while sel != 5:
            #system('clear')
            print("-------------------------")
            print('habitpi display test menu')
            print('Version 0.1')
            print('Copyright (C) 2020 Jason A Bright')
            print('This program comes with ABSOLUTELY NO WARRANTY')
            print('This is free software, and you are welcome to redistribute it')
            print('For details see the license.md file')
            print('-------------------------')
            print('1. Test Habit LEDs')
            print('2. Test Individual 7 seg display (1st digit)')
            print('3. Test 4 segment display')
            print('4. Test full display')
            print('5. Exit')
            print("")
            sel = int(input('Select an option '))

            if 0 <= sel <=5:
                if sel == 1:
                    habit_list = habitLEDmenu()
                    digit_list = [0,0,0,0]
                    number_list = [0,0,0,0,0,0,0,0]
                    disp_list = habit_list+digit_list+number_list
                    display(disp_list)
                elif sel == 2:
                    habit_list = [0,0,0,0]
                    digit_list = [1,0,0,0]
                    number_list = digitmenu()
                    disp_list = habit_list+digit_list+number_list
                    display(disp_list)
                elif sel == 3:
                    num = input("What number to display (0 to 9999)")
                    num = check_num(num)
                    habit_list = [0,0,0,0]    
                    foursegmentdisplay(num,habit_list)
                elif sel == 4:
                    habit_list = habitLEDmenu()
                    num = input("What number to display (0 to 9999)")
                    num = check_num(num)
                    foursegmentdisplay(num,habit_list)
            else:
                raise ValueError

    except ValueError:
        print("Selection must be between 1 and 5")
        mainmenu()
#    except TypeError:
#        print("Selection must be a number")
#        mainmenu()

if __name__ == '__main__':
    mainmenu() 
       
