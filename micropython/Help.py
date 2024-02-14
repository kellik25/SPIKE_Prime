from Sound import Sound

def help(name):
    if name == "play":
        print(Sound.play.__doc__) #easier but cannot get docstring to print which should not be happening
    elif name == "search":
        print('''
        search(measured)
        This function finds and retuns the button state that matches the inputted measurement
        
        Args:
            measured(integer) = button value state to match
            
        Returns:
            btn (list) = list of booleans representaing button states[left, center, right, bluetooth]
            
        Note:
            Boolean values written as 1s and 0s
        ''')
    elif name == "read":
        print('''
        read()
        This function returns the current state of the buttons
            
        Returns:
            a (list) = list of booleans representating button states [left, center, right, bluetooth]
            
        Note:
            Boolean values written as 1s and 0s
        ''')
    elif name == "set":
        print('''
        set(led, value=256*256-1)
        This function sets the LED at the specified index to a particular color
        
        Args:
            led (integer) = index for the LED
            value (integer) = 16-bit value respresenting a color
        ''')
    elif name == "pixel_set":
        print('''
        pixel_set(led, value = 256*256-1)
        This function should be used over set() as it checks that the desired LED index is in range before setting it
        
        Args:
            led (integer) = index for the LED
            value (integer) = 16-bit value representating a color
        
        Returns:
            -1 if index is not in range otherwise no return
        ''')
    elif name == "timer_init":
        print('''
        timer_init()
        This function powers the LED display
        ''')
    elif name == "display_update":
        print('''
        display_update()
        This function modifies the LED display to show the current LED configuration
        ''')
    elif name == "latch_ctrl":
        print('''
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
        ''')
    elif name == "display_on":
        print('''
        display_on()
        This function initialize power and properties of the LED configuration
        ''')
    elif name == "start":
        print('''
        start()
        This function turns the ble and power leds on
        ''')
    elif name == "matrix_led":
        print('''
        matrix_led(x, y, b)
        This function controls which led is used in the matrix
        
        Args:
            x (integer) = left and right on the matrix
            y (integer) = up and down on the matrix
            b (integer) = brightness
        ''')
    elif name == "ble_led":
        print('''
        ble_led(r, g, b)
        This function sets the color of the ble led on the hub
        
        Args:
            r (bool) = red
            g (bool) = green 
            b (bool) = blue
            
        Note:
            Bools written as integer values of 0 and 1
        ''')
    elif name == "power_led":
        print('''
        power_led(r, g, b)
        This function sets the color of the power led on the hub
        
        Args:
            r (bool) = red
            g (bool) = green 
            b (bool) = blue
            
        Note:
            Bools written as integer values of 0 and 1
        ''')
    elif name == "battery_led":
        print('''
        battery_led(r, g, b)
        This functions ets the color of the battery led on the hub
        
        Args:
            r (bool) = red
            g (bool) = green 
            b (bool) = blue
            
        Note:
            Bools written as integer values of 0 and 1
        
        ''')
    else:
        print('''
        function unknown
        ''')
    
