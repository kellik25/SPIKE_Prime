from Buttons import Buttons
from Sound import Sound
import Lights
import Help

l = Lights.Lights()
#l.display_on() what does this do does not output anything
#l.display_update()
#l.start()
#l.timer_init()
#l.power_led(0,0,0)
#l.ble_led(0,0,0)
#l.battery_led(0,0,0)
#l.matrix_led(2,1)

#l.full_test()
#l.power_led(0,0,1)

b = Buttons()
measured_value = 3000
print(b.search(measured_value))
print(b.read())

#find way to get rid of the Help.help so that it is just help
Help.help("read")

#s = Sound.Sound()
s = Sound()
s.play(500,2)
