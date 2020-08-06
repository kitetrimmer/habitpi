# THIS IS NOT WORKING - IT IS A TEST, BUT I'M OBVIOUSLY NOT READY TO GO HERE YET!



# This is a test of multiprocessing.  I am going to ask the keypad for input, and display the results on the keypad

# Copyright (C) 2020 Jason A Bright

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

from multiprocessing import Process
import keypad_test
import habitpi_display
import configparser
import RPi.GPIO as GPIO

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
       

habit_list=[0,0,0,0]
num = 1
disp = Process(target=habitpi_display.foursegmentdisplay, args=(num,habit_list))
inp = Process(target=keypad_test.fourdigitinput)

inp.start
disp.start()

inp.join()
disp.join()
