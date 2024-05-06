import pyb

class Buttons():
    '''
    To use the Buttons module add the following import statement to your project:
    
    from Buttons import Buttons
    
    All functions in the module should be called inside the button module as a prefix like so:
    
    Buttons.read()
    '''
    
    def __init__(self):
        self.btns = pyb.ADC(pyb.Pin('A1'))
        self.center = pyb.ADC(pyb.Pin('C4'))
        
        self.lut = {4093: [0,0,0,0], 3654:[0,0,0,1], 3155:[0,0,1,0], 2885:[0,0,1,1], 2645:[1,0,0,0], 2454:[1,0,0,1],2218:[1,0,1,0], 2084:[1,0,1,1], 1800: [0,0,0,0] }
        
    def search(self, measured):
        '''
        search(measured)
        This function finds and returns the button states that matches the inputted measurement
        
        Args:
            measured(integer) = button value state to match
            
        Returns:
            btn (list) = list of booleans representaing button states[left, center, right, bluetooth]
            
        Note:
            Boolean values written as 1s and 0s
        '''
        min = 100000000
        for num,btns in self.lut.items():
            dist = (num-measured)**2
            if dist < min: 
                min = dist
                btn = btns
        return btn
    
    def read(self):
        '''
        read()
        This function returns the current state of the buttons
            
        Returns:
            a (list) = list of booleans representating button states [left, center, right, bluetooth]
            
        Note:
            Boolean values written as 1s and 0s
        '''
        b = self.btns.read()#>>4
        c = self.center.read()#>>4
        a = self.search(b)   #[L,C, R, BLE]
        a[1] = self.search(c)[2] #[PORTADC, C, ChargeOK] that gets merged...
        return a
