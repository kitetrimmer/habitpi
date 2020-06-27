# This is a function to display a character on a seven segment display
# for documentation, see the sevensegment.md

def sevensegment(ch,d,pinout):
    #ch is the character to display
    #d is the duration in seconds
    #pinout is the pinout for the display

    from gpiozero import LEDBoard
    from time import sleep
    import traceback

    num = {
            '1': (3,6),
            '2': (2,3,0,4,5),
            '3': (2,3,0,6,5),
            '4': (1,0,3,6),
            '5': (2,1,0,6,5),
            '6': (2,1,4,5,6,0),
            '7': (2,3,6),
            '8': (0,1,2,3,4,5,6),
            '9': (2,3,1,0,6),
            '0': (2,1,4,5,6,3),
            'A': (4,1,2,3,0,6),
            'C': (2,1,4,5),
            'E': (2,1,0,4,5),
            'F': (2,1,0,4),
            'H': (1,4,0,3,6),
            'J': (3,6,5,4),
            'L': (1,4,5),
            'P': (2,3,0,1,4),
            'U': (1,4,5,6,3)
            }

       # Validate the inputs - ch needs to be in the num dictionary, and d needs to be an integer

    try:
        if ch not in num:
            raise ValueError ("Can't display that value on seven segment display)")
        if not type(d) is int:
            raise TypeError ("Expecting an integer for duration")
        if not type(pinout) is tuple:
            raise TypeError ("Need a tuple for pinouts") 
        if len(pinout) != 8:
            raise IndexError ("Need list of 8 pinouts")
        for a in range(0,len(pinout)):
                if not (1<=pinout[a]<=26):
                    raise ValueError ("GPIO pinouts must be from 1 to 26")
    except ValueError as error:
        traceback.print_exc()
    except TypeError as error:
        traceback.print_exc()
    except IndexError as error:
        traceback.print_exc()
    else:
        leds = LEDBoard(*pinout)

        for a in range(0,len(num[ch])):
            leds[num[ch][a]].on()
        sleep(d)
        leds.off()

