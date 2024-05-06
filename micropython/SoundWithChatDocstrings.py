import pyb
import time
import math
from array import array

class Sound:
    """
    A class to generate sound using the Spike Prime Hub.

    Attributes:
        buf (array.array): Buffer containing a sine-wave for sound generation.
        tim (pyb.Timer): Timer object for controlling frequency.
        dac (pyb.DAC): DAC (Digital to Analog Converter) object for sound output.
    """

    def __init__(self):
        """
        Initializes the Sound object with a sine-wave buffer and necessary peripherals.
        
        Example:
            >>> sound = Sound()
        """
        # create a buffer containing a sine-wave, using half-word samples
        self.buf = array('H', [2048 + int(2047 * math.sin(2 * math.pi * i / 128)) for i in range(128)])
        self.tim = pyb.Timer(6, freq=440 * len(self.buf))
        self.dac = pyb.DAC(1, bits=12)

    def play(self, freq, duration):
        """
        Plays a sound with the specified frequency and duration.

        Args:
            freq (int): The frequency of the sound in Hertz.
            duration (float): The duration of the sound in seconds.
        
        Example:
            >>> sound.play(500, 2)
        """
        # Set the frequency of the timer to match the desired frequency
        self.tim.freq(freq * len(self.buf))
        # Write the sine-wave buffer to the DAC and play it
        self.dac.write_timed(self.buf, self.tim, mode=pyb.DAC.CIRCULAR)

        # Turn on an LED to indicate sound playback
        led_pin = pyb.Pin('C10', pyb.Pin.OUT)
        led_pin.on()

        # Wait for the specified duration
        time.sleep(duration)

        # Turn off the LED after the sound finishes
        led_pin.off()
