import RPi.GPIO as GPIO
import time
import configparser
import ast

def send_one():
    GPIO.output(DATA,GPIO.HIGH)
    GPIO.output(CLOCK,GPIO.HIGH)
    #time.sleep(.001)
    GPIO.output(CLOCK,GPIO.LOW)

def send_zero():
    GPIO.output(DATA,GPIO.LOW)
    GPIO.output(CLOCK,GPIO.HIGH)
    #time.sleep(.001)
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
    try:
        while True:
            if 0<=num<=9999:
                disp_string = str(num)
                disp_string = disp_string.rjust(4, ' ')
                for a in range(0,len(disp_string)):
                    if a == 0:
                        digit_list = [1,0,0,0]
                        number_str = generate_numlist(disp_string[a])
                        number_list=ast.literal_eval(number_str)
                    elif a == 1:
                        digit_list = [0,1,0,0]
                        number_str = generate_numlist(disp_string[a])
                        number_list=ast.literal_eval(number_str)
                    elif a == 2:
                        digit_list = [0,0,1,0]
                        number_str = generate_numlist(disp_string[a])
                        number_list=ast.literal_eval(number_str)
                    elif a == 3:
                        digit_list = [0,0,0,1]
                        number_str = generate_numlist(disp_string[a])
                        number_list=ast.literal_eval(number_str)
                    else:
                        print("too many digits")
                    disp_list = habit_list + digit_list + number_list
                    display(disp_list)
                    time.sleep(.0005)
    except:
        display([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        return

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
                    num = int(input("What number to display (0 to 9999)"))
                    habit_list = [0,0,0,0]    
                    foursegmentdisplay(num,habit_list)
                elif sel == 4:
                    habit_list = habitLEDmenu()
                    num = int(input("What number to display (0 to 9999)"))
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
    # get the list from mainment()
    config = configparser.ConfigParser()
    config.read('habitpi.conf')

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    CLOCK = config['Pinouts'].getint('Clock')
    DATA = config['Pinouts'].getint('Data')
    LATCH = config['Pinouts'].getint('Latch')

    GPIO.setup(DATA,GPIO.OUT)
    GPIO.setup(CLOCK,GPIO.OUT)
    GPIO.setup(LATCH,GPIO.OUT)
    mainmenu() 
        
