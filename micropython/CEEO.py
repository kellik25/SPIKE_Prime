import pyb
import time, math
from array import array
import Buttons
import Sound
import Lights

l = Lights()
l.power_led(0,0,1)
b = Buttons()
s = Sound()
s.play(440,1)
