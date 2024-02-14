import pyb
import time
from array import array

class Lights():
    '''
    This class controls the light functions of the spike prime hub
    '''
    def __init__(self):
        self.pixel_lut = [9,11,6,1,14,10,19,8,0,26,23,18,3,2,24,21,20,15,13,25,22,7,17,12,38,27,28,29,39,40,41,42,43,44,45,46,47]
        self.fullBrightness = 256*256-1
        self.display = bytearray(96)
        self.sclk = pyb.Pin(pyb.Pin.board.TLC_SCLK, pyb.Pin.AF_PP, alt=pyb.Pin.AF5_SPI1, pull= pyb.Pin.PULL_NONE)
        self.sout = pyb.Pin(pyb.Pin.board.TLC_SOUT, pyb.Pin.AF_PP, alt=pyb.Pin.AF5_SPI1, pull= pyb.Pin.PULL_NONE)
        self.sin = pyb.Pin(pyb.Pin.board.TLC_SIN,   pyb.Pin.AF_PP, alt=pyb.Pin.AF5_SPI1, pull= pyb.Pin.PULL_NONE)
        self.tlcLat = pyb.Pin(pyb.Pin.board.TLC_LAT, pyb.Pin.OUT, pull= pyb.Pin.PULL_NONE)
        self.gsclk = pyb.Pin(pyb.Pin('B15'),pyb.Pin.ALT, alt=pyb.Pin.AF9_TIM12, pull = pyb.Pin.PULL_NONE)
        
        self.spi = pyb.SPI(1, pyb.SPI.CONTROLLER,baudrate = 25000000, polarity=0, phase=0, bits=8, firstbit=pyb.SPI.MSB)
        self.display_on()
        self.power_led(0,0,1)

    #can't get this one to seem to work on its own but understand its concept
    def set(self, led, value = 256*256-1):
        '''
        set(led, value=256*256-1)
        This function sets the LED at the specified index to a particular color
        
        Args:
            led (integer) = index for the LED
            value (integer) = 16-bit value respresenting a color
        '''
        self.display[led * 2] = value&0xFF
        self.display[led * 2 + 1] = (value >> 8)&0xFF
        
    def pixel_set(self, led, value = 256*256-1):
        '''
        pixel_set(led, value = 256*256-1)
        This function should be used over set() as it checks that the desired LED index is in range before setting it
        
        Args:
            led (integer) = index for the LED
            value (integer) = 16-bit value representating a color
        
        Returns:
            -1 if index is not in range otherwise no return
        '''
        if led not in range(len(self.pixel_lut)): return -1
        self.set(self.pixel_lut[led],value)
        
    
    def timer_init(self):
        '''
        timer_init()
        This function powers the LED display
        '''
        tim = pyb.Timer(12, freq=25000000)
        ch = tim.channel(2, pyb.Timer.PWM, pin=self.gsclk)  #machine.Pin('B15'))
        ch.pulse_width_percent(90)

    def display_update(self):
        '''
        display_update()
        This function modifies the LED display to show the current LED configuration
        '''
        self.spi.write(b'\x00')
        for i in range(96):
            self.spi.write(bytes(self.display[95 - i:96 - i]))
        self.tlcLat.on()
        time.sleep_us(1)
        self.tlcLat.off()
        
    def latch_ctrl(self, dc, mc, bc, fc):
        '''
        latch_ctrl(dc, mc, bc, fc)
        This function configures different aspects of the LED properties
        
        Args:
            dc (integer) = dot correction
            mc (integer) = max current
            bc (integer) = brightness control
            fc (integer) = function control
        
        Notes:
            dc and fc are uint8
            mc and bc are uint32
        '''
        payload= bytearray()
        payload.append(1)                    # bit 768
        payload.append(0x96)                 # bits 760-767
        for i in range(48):
            payload.append(0)
        payload.append(fc >> 2)              # bits 368-375
        payload.append(fc << 6 | bc >> 15)   # bits 360-367
        payload.append(bc >> 7)              # bits 352-359
        payload.append(bc << 1 | mc >> 8)    # bits 344-351
        payload.append(mc)                   # bits 336-343  default is zero
        for i in range(42):
            payload.append(dc&0xFF)          # max dot correction value - bright as possible
        self.spi.write(payload)
        self.tlcLat.on()
        time.sleep_us(1)
        self.tlcLat.off()
    
    #check to see what the purpose of this is and what is the major difference between it and timer on
    def display_on(self):
        '''
        display_on()
        This function initialize power and properties of the LED configuration
        '''
        self.tlcLat.off()
        for i in range(2):
            self.latch_ctrl(0xff, 0, 0x1fffff, 0x11)
        self.timer_init()
        
    #check to see what purpose of this function is and why it is needed separately than display_on
    def start(self):
        '''
        start()
        This function turns the ble and power leds on
        '''
        self.pixel_set(25)
        self.pixel_set(26)
        self.pixel_set(27)
        self.display_update()
        
    def matrix_led(self, x, y, b = 1):
        '''
        matrix_led(x, y, b)
        This function controls which led is used in the matrix
        
        Args:
            x (integer) = left and right on the matrix
            y (integer) = up and down on the matrix
            b (integer) = brightness
        '''
        self.pixel_set(y*5+x, self.fullBrightness*b)
        self.display_update()
        
    def ble_led(self, r=0, g=1, b=0):
        '''
        ble_led(r, g, b)
        This function sets the color of the ble led on the hub
        
        Args:
            r (bool) = red
            g (bool) = green 
            b (bool) = blue
            
        Note:
            Bools written as integer values of 0 and 1
        '''
        self.pixel_set(25, self.fullBrightness*r)
        self.pixel_set(26, self.fullBrightness*g)
        self.pixel_set(27, self.fullBrightness*b)
        self.display_update()
        
    def power_led(self, r=0, g=0, b=1):
        '''
        power_led(r, g, b)
        This function sets the color of the power led on the hub
        
        Args:
            r (bool) = red
            g (bool) = green 
            b (bool) = blue
            
        Note:
            Bools written as integer values of 0 and 1
        '''
        #left and right leds
        self.pixel_set(28, self.fullBrightness*r)
        self.pixel_set(29, self.fullBrightness*g)
        self.pixel_set(30, self.fullBrightness*b)
        self.pixel_set(31, self.fullBrightness*r)
        self.pixel_set(32, self.fullBrightness*g)
        self.pixel_set(33, self.fullBrightness*b)
        self.display_update()

    def battery_led(self, r=1, g=0, b=0):
        '''
        battery_led(r, g, b)
        This functions ets the color of the battery led on the hub
        
        Args:
            r (bool) = red
            g (bool) = green 
            b (bool) = blue
            
        Note:
            Bools written as integer values of 0 and 1
        
        '''
        self.pixel_set(34, self.fullBrightness*r)
        self.pixel_set(35, self.fullBrightness*g)
        self.pixel_set(36, self.fullBrightness*b)
        self.display_update()
        
    #this is testing only comment out later 
    def full_test(self):
        for i in range(48):
            for b in range(0,self.fullBrightness,128):
                self.pixel_set(i,b)
                self.display_update()
                time.sleep(0.001)
            time.sleep(0.1)
            if i: self.pixel_set(i-1,0)
