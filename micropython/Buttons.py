import pyb

#figure out formating inside docstrings better too
#double check that right on what each function does in this class

#think the name of the classes need to change because its confusing to do Sound.Sound, Button.Button, etc.; for using from Sound import Sound
class Buttons():
    '''
    This class controls the button functions of the spike prime hub
    '''
    def __init__(self):
        self.btns = pyb.ADC(pyb.Pin('A1'))
        #is the bluetooth button contained in this one?
        self.center = pyb.ADC(pyb.Pin('C4'))
        #why is center seperated?
        self.lut = {4093: [0,0,0,0], 3654:[0,0,0,1], 3155:[0,0,1,0], 2885:[0,0,1,1], 2645:[1,0,0,0], 2454:[1,0,0,1],2218:[1,0,1,0], 2084:[1,0,1,1], 1800: [0,0,0,0] }
        
    def search(self, measured):
        '''
        This function finds and retuns the button state that matches the inputted measurement
        The state is returned as a list of the buttons: [left, center, right, bluetooth]
        :param measured: integer
        :return btn: list of integers
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
            This function returns the current state of the buttons as 1s and 0s in a list
            [left, center, right, bluetooth]
            '''
            b = self.btns.read()#>>4
            #center button is not registering when pushed
            c = self.center.read()#>>4
            a = self.search(b)   #[L,C, R, BLE]
            a[1] = self.search(c)[2] #[PORTADC, C, ChargeOK] that gets merged...
            return a
