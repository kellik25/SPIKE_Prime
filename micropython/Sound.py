import pyb
import time, math
from array import array

class Sound():
    '''
    This class controls the sound functions of the spike prime controller
    '''
    # don't think i need to create help modules for inits but can if needed
    def __init__(self):
        # create a buffer containing a sine-wave, using half-word samples
        self.buf = array('H', 2048 + int(2047 * math.sin(2 * math.pi * i / 128)) for i in range(128))
        self.tim = pyb.Timer(6, freq=440*len(self.buf))
        self.dac = pyb.DAC(1, bits=12)
        
    def play(self, freq, duration):
        '''
        This function plays a sound at the frequency inputted for the inputted number of seconds
        :param freq: integer
        :param duration: integer
        '''
        self.tim.freq(freq*len(self.buf))
        self.dac.write_timed(self.buf, self.tim, mode=pyb.DAC.CIRCULAR)
        #what is this pin number?
        fred = pyb.Pin('C10', pyb.Pin.OUT)
        fred.on()
        time.sleep(duration)
        fred.off()
        
#help module not displaying docstrings which can sometimes happen in micropython
        #check to see that micropython is up to date - which it seems to be 
        #or use .__doc__ attribute instead of help to see the docstrings
        #this would be something like: "print(Sound.Sound.play.__doc__)"
        #could also create class that is just functions of helper functions that are full with string explanations
            #downside is that I would need to update this every time a new function is made which could get annoying
