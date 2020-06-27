# sevensegment function documentation

## What is this?
The sevensegment function will display a value on a sevensegment display.  It takes 3 arguments:

*ch:* This is the character that will be displayed.
*d:* This is the duration that the character should be displayed
*pinouts* This is a tuple that describes how the seven segment display is connected to the Pi.  See below for how this should be configured.

## Values that can be displayed:
The following values can be displayed by this function:

   1,2,3,4,5,6,7,8,9,0,A,C,E,F,H,J,L,P,U

Any other values will throw an error.

## pinout configuration

The seven segment display is configured as follows:


    ---a---
    |     |
    f     b 
    |     |
    ---g---
    |     |
    e     c
    |     |
    ---d---   dp

For the numbers to come out right, the tuple should list the GPIO pinouts in the following order:

g,f,a,b,e,d,c,dp

For instance, if the segment is wired as follows, the tuple would be (6,13,19,26,21,20,16,12)

Segment | GPIO Pin
--------|---------
g | 6
f | 13
a | 19
b | 26
e | 21
d | 20
c | 16
dp| 12

## Pinouts

The display I am using has the following pinouts:

    g  f  cc  a  b
    |  |  |   |  |
    |  |  |   |  |
    +------------+
    |            |
    |  ---a---   |
    |  |     |   |
    |  f     b   |
    |  |     |   |
    |  ---g---   |
    |  |     |   |
    |  e     c   |
    |  |     |   |
    |  ---d--- dp|
    |            |
    +------------+
    |  |  |   |  |
    |  |  |   |  |
    e  d  cc  c dp    
