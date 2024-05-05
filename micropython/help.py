from Sound import Sound
from Buttons import Buttons
from Lights import Lights

functions = {
    "Sound": Sound.__doc__,
    "play": Sound.play.__doc__,
    "Lights": Lights.__doc__,
    "set": Lights.set.__doc__,
    "pixel_set": Lights.pixel_set.__doc__,
    "timer_init": Lights.timer_init.__doc__,
    "display_update": Lights.display_update.__doc__,
    "latch_ctrl": Lights.latch_ctrl.__doc__,
    "display_on": Lights.display_on.__doc__,
    "start": Lights.start.__doc__,
    "matrix_led": Lights.matrix_led.__doc__,
    "ble_led": Lights.ble_led.__doc__,
    "power_led": Lights.power_led.__doc__,
    "battery_led": Lights.battery_led.__doc__,
    "Buttons": Buttons.__doc__,
    "search": Buttons.search.__doc__,
    "read": Buttons.read.__doc__}
    
def help(name):
    if name in functions:
        print(functions[name])
    else:
        print("function not found")
