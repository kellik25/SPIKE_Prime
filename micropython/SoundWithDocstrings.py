import pyb
import time, math
from array import array

class Sound():
    '''
    This class controls the sound functions of the spike prime hub
    '''
    # don't think i need to create help modules for inits but can if needed
    def __init__(self):
        # create a buffer containing a sine-wave, using half-word samples
        self.buf = array('H', 2048 + int(2047 * math.sin(2 * math.pi * i / 128)) for i in range(128))
        self.tim = pyb.Timer(6, freq=440*len(self.buf))
        self.dac = pyb.DAC(1, bits=12)
        
    def play(self, freq, duration):
        '''
        play(freq, duration)
        This function plays a sound
        
        Args:
            freq (integer) = pitch (frequency) of the sound
            duration (integer) = time for sound to play
        '''
        self.tim.freq(freq*len(self.buf))
        self.dac.write_timed(self.buf, self.tim, mode=pyb.DAC.CIRCULAR)
        #what is this pin number?
        fred = pyb.Pin('C10', pyb.Pin.OUT)
        fred.on()
        time.sleep(duration)
        fred.off()
