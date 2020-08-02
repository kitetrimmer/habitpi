# This is a program to test the keypad
import RPi.GPIO as GPIO
import time
import configparser

def catch_key():
    key = ''
#    try:
    while key == '':        
        for a in range(0,3):
            if a == 0:
                GPIO.output(COL1,GPIO.HIGH)
                if GPIO.input(ROW1):
                    key = '1'
                elif GPIO.input(ROW2):
                    key = '4'
                elif GPIO.input(ROW3):
                    key = '7'
                elif GPIO.input(ROW4):
                    key = '*'
                    
            if a == 1:
                GPIO.output(COL2,GPIO.HIGH)
                if GPIO.input(ROW1):
                    key = '2'
                elif GPIO.input(ROW2):
                    key = '5'
                elif GPIO.input(ROW3):
                    key = '8'
                elif GPIO.input(ROW4):
                    key = '0'
            if a == 2:
                GPIO.output(COL3,GPIO.HIGH)
                if GPIO.input(ROW1):
                    key = '3'
                elif GPIO.input(ROW2):
                    key = '6'
                elif GPIO.input(ROW3):
                    key = '9'
                elif GPIO.input(ROW4):
                    key = '#'
            
            if a == 3:
                GPIO.output(COL4,GPIO.HIGH)
                if GPIO.input(ROW1):
                    key = 'A'
                elif GPIO.input(ROW2):
                    key = 'B'
                elif GPIO.input(ROW3):
                    key = 'C'
                elif GPIO.input(ROW4):
                    key = 'D'
    print(" Key Pressed = ",key)
    time.sleep(1)
    catch_key()
    
#    except:
#        print("error")




if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('habitpi.conf')

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
    catch_key()
