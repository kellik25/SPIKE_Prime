import pyb
import time, math
from array import array

#might not even need the class cause then when import it would be "from Buttons import Buttons" versus without the class just doing "import
# Buttons"
class Buttons():
    '''fred = Buttons()
       fred.read()'''
    def __init__(self):
        self.btns = pyb.ADC(pyb.Pin('A1'))
        self.center = pyb.ADC(pyb.Pin('C4'))
        self.lut = {4093: [0,0,0,0], 3654:[0,0,0,1], 3155:[0,0,1,0], 2885:[0,0,1,1], 2645:[1,0,0,0], 2454:[1,0,0,1],2218:[1,0,1,0], 2084:[1,0,1,1], 1800: [0,0,0,0] }
        
    def search(self, measured):
        min = 100000000
        for num,btns in self.lut.items():
            dist = (num-measured)**2
            if dist < min: 
                min = dist
                btn = btns
        return btn
    
    def read(self):
            b = self.btns.read()#>>4
            c = self.center.read()#>>4
            a = self.search(b)   #[L,C, R, BLE]
            a[1] = self.search(c)[2] #[PORTADC, C, ChargeOK] that gets merged...
            return a
