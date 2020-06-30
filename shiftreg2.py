# This program will light up an LED based on the number that is input
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def clear_register(pinout):
    
    DATA = pinout[0]
    SHIFT = pinout[1]
    LATCH = pinout[2]
    GPIO.setup(DATA,GPIO.OUT)
    GPIO.setup(SHIFT,GPIO.OUT)
    GPIO.setup(LATCH,GPIO.OUT)
    for i in range(0,8):
        GPIO.output(DATA,GPIO.LOW)
        GPIO.output(SHIFT,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SHIFT,GPIO.LOW)
    GPIO.output(LATCH,GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(LATCH,GPIO.LOW)

# update the register
def update_register(n,pinout):

    DATA = pinout[0]
    SHIFT = pinout[1]
    LATCH = pinout[2]
    GPIO.setup(DATA,GPIO.OUT)
    GPIO.setup(SHIFT,GPIO.OUT)
    GPIO.setup(LATCH,GPIO.OUT)

    num = {
            '0' : (0,0,0,0,0,0,0,0),
            '1' : (0,0,0,0,0,0,0,1),
            '2' : (0,0,0,0,0,0,1,0),
            '3' : (0,0,0,0,0,1,0,0),
            '4' : (0,0,0,0,1,0,0,0),
            '5' : (0,0,0,1,0,0,0,0),
            '6' : (0,0,1,0,0,0,0,0),
            '7' : (0,1,0,0,0,0,0,0),
            '8' : (1,0,0,0,0,0,0,0)
          }
    for c in range(0,8):
        if num[n][c] == 0:
            GPIO.output(DATA,GPIO.LOW)
            GPIO.output(SHIFT,GPIO.HIGH)
            time.sleep (0.001)
            GPIO.output(SHIFT,GPIO.LOW)
        else:
            GPIO.output(DATA,GPIO.HIGH)
            GPIO.output(SHIFT,GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(SHIFT,GPIO.LOW)

# release the data to the leds
def send_to_leds(pinout):

   DATA = pinout[0]
   SHIFT = pinout[1]
   LATCH = pinout[2]
   GPIO.setup(DATA,GPIO.OUT)
   GPIO.setup(SHIFT,GPIO.OUT)
   GPIO.setup(LATCH,GPIO.OUT)
   
   GPIO.output(LATCH,GPIO.HIGH)
   time.sleep(0.001)
   GPIO.output(LATCH,GPIO.LOW)

# validate the pinouts
def validate_pinouts(pinout,config):
    # check to make sure it's a tuple
    if not isinstance(pinout, dict):
        return "Not a Tuple"
    # make sure that all the pins are valid
    for a in range(0,len(pinout)):
        if not(1<=pinout<=26):
            return "pinout ",a," is invalid"
    # for a shift register there should only be 3 values
    if config=="shiftregister" and len(pinout)!=3:
        return "Need to have 3 pinouts for a shift register"

    return True

if __name__ == "__main__":
    #(17,27,23)
    pinout = (17,50,23)
    try:
       p = validate_pinouts(pinout,"shiftregister")
       if not p:
           print(p)
           raise Exception
       clear_register(pinout)
       while True:
           n = input("Number from 0 to 8 to light up ")
           update_register(n,pinout)
           send_to_leds(pinout)
           time.sleep(5)
           clear_register(pinout)
    except KeyError:
        print("That's all folks!")
    finally:
        GPIO.cleanup()
        
