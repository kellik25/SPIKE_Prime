import pyb

class Buttons():
    """
    Buttons class for handling button inputs on a Spike Prime hub using MicroPython.

    Attributes:
        btns (pyb.ADC): Analog-to-digital converter for the button sensor.
        center (pyb.ADC): Analog-to-digital converter for the center button.
        lut (dict): Lookup table mapping ADC values to button states.

    Methods:
        __init__(self): Initializes the Buttons class by setting up ADCs and the lookup table.
        search(self, measured): Finds the closest match in the lookup table for a given ADC value.
        read(self): Reads the ADC values for the buttons, determines their states, and returns the result.

    Example:
        buttons = Buttons()
        button_states = buttons.read()
        print(button_states)
    """
    
    def __init__(self):
        """
        Initializes the Buttons class.

        Sets up analog-to-digital converters (ADCs) for button and center inputs,
        and initializes the lookup table for mapping ADC values to button states.
        """
        self.btns = pyb.ADC(pyb.Pin('A1'))
        self.center = pyb.ADC(pyb.Pin('C4'))
        self.lut = {4093: [0, 0, 0, 0], 3654: [0, 0, 0, 1], 3155: [0, 0, 1, 0],
                    2885: [0, 0, 1, 1], 2645: [1, 0, 0, 0], 2454: [1, 0, 0, 1],
                    2218: [1, 0, 1, 0], 2084: [1, 0, 1, 1], 1800: [0, 0, 0, 0]}

    def search(self, measured):
        """
        Finds the closest match in the lookup table for a given measured ADC value.

        Args:
            measured (int): The ADC value to be matched.

        Returns:
            list: Button state corresponding to the closest match in the lookup table.
        """
        min_dist = 100000000
        for num, btns in self.lut.items():
            dist = (num - measured) ** 2
            if dist < min_dist:
                min_dist = dist
                btn = btns
        return btn

    def read(self):
        """
        Reads the ADC values for the buttons, determines their states, and returns the result.

        Returns:
            list: Button states represented as [L, C, R, BLE], where L, C, R are button states
                  and BLE indicates the charge state of the center button.
        """
        b = self.btns.read()  # >>4
        c = self.center.read()  # >>4
        a = self.search(b)   # [L, C, R, BLE]
        a[1] = self.search(c)[2]  # [PORTADC, C, ChargeOK] that gets merged...
        return a
