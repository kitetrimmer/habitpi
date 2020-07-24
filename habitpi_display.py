import RPi.GPIO as GPIO
import time
import configparser
config = configparser.ConfigParser()
config.read('habitpi.conf')


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

CLOCK = config['Pinouts'].getint('Clock')
DATA = config['Pinouts'].getint('Data')
LATCH = config['Pinouts'].getint('Latch')

#TODO: rewire the board so that the pins are right, and then start in...
#TODO: first thing to do, I think is to make everything light up
