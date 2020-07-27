import RPi.GPIO as GPIO
import time
import configparser
import ast

def send_one():
    GPIO.output(DATA,GPIO.HIGH)
    GPIO.output(CLOCK,GPIO.HIGH)
    time.sleep(.001)
    GPIO.output(CLOCK,GPIO.LOW)

def send_zero():
    GPIO.output(DATA,GPIO.LOW)
    GPIO.output(CLOCK,GPIO.HIGH)
    time.sleep(.001)
    GPIO.output(CLOCK,GPIO.LOW)

def latch():
    GPIO.output(LATCH,GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(LATCH,GPIO.LOW)

def generate_numlist(digit):
    # G F E D C B A DP (1 to turn off)
    num_dict = {'0':'[1,0,0,0,0,0,0,1)',
                '1':'[1,1,1,1,0,0,1,1]',
                '2':'[0,1,0,0,1,0,0,1]',
                '3':'[0,1,1,0,0,0,0,1]',
                '4':'[0,0,1,1,0,0,1,1]',
                '5':'[0,1,0,0,1,0,0,0]',
                '6':'[0,1,0,0,0,0,0,1]',
                '7':'[0,0,0,1,1,0,1,1]',
                '8':'[0,0,0,0,0,0,0,1]',
                '9':'[0,0,0,0,1,0,0,1]',
                '0':'[0,0,0,0,0,0,1,1]'
                }
    #TODO: Add alpha characters
    digit_list = num_dict[str(digit)]
    #TODO: Need to catch invalid values, and think about converting only numbers to strings.
    return digit_list

def habitLEDmenu():
    habit_list = [0,0,0,0]
    digit_list = [0,0,0,0]
    number_list = [0,0,0,0,0,0,0,0]
    for habit in range(0,4):
        sel = ''
        sel = input(f"Light up LED {habit}?")
        if sel == 'y' or sel == 'Y':
            habit_list[habit] = 1
        else:
            habit_list[habit] = 0
    print(habit_list)
    print("output list = ",habit_list+digit_list+number_list)
    print("")
    final_list = habit_list + digit_list + number_list    
    return final_list

def digitmenu():
    try:
        whole_list  = []
        habit_list = [0,0,0,0]
        digit_list = [1,0,0,0]
        sel = int(input("Pick a number from 0-9 to display on the first digit: "))
        if 0<=sel<=9:
            number_str = generate_numlist(sel)
            number_list= ast.literal_eval(number_str)  #I might be able to return a list from generate_numlist - might have to check that.
        else:
            raise ValueError
        
        print('numberlist = ',number_list)
        print('List to send:')
        whole_list = habit_list + digit_list + number_list
        print(str(whole_list))
        
    except ValueError:
        print("Must be from 0 to 9 inclusive")
        digitmenu()
#    except TypeError:
#        print("Must be a number")


def foursegmentmenu():
    pass


def mainmenu():
    try:
        sel = 0
        while sel != 5:
            print('habitpi display test menu')
            print('Version 0.1')
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
                    disp_list = habitLEDmenu()
                elif sel == 2:
                    digitmenu()
                elif sel == 3:
                    foursegmentmenu()
                elif sel == 4:
                    habitledmenu()
                    foursegmentmenu()
            else:
                raise ValueError

            print("display list = ",disp_list)
            print("type = ",type(disp_list))
    except ValueError:
        print("Selection must be between 1 and 5")
        mainmenu()
#    except TypeError:
#        print("Selection must be a number")
#        mainmenu()

if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('habitpi.conf')

    try:
        # get the list from mainment()
        mainmenu() 
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        CLOCK = config['Pinouts'].getint('Clock')
        DATA = config['Pinouts'].getint('Data')
        LATCH = config['Pinouts'].getint('Latch')

        GPIO.setup(DATA,GPIO.OUT)
        GPIO.setup(CLOCK,GPIO.OUT)
        GPIO.setup(LATCH,GPIO.OUT)

# Migrate this code to a display function that gets a list 
    #    for var in led_dict[choice]:
    #        if var == 1:
    #            send_one()
    #        elif var == 0:
    #            send_zero()
    #        else:
    #            raise ValueError
    #    latch()
