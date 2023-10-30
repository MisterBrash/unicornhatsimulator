'''Testing the simulator'''

from time import sleep
from unicornhatsimulator import unicornhathd as u


sleep(1)
print("Window Loading... Setting up pixel(s)")
u.set_pixel(3, 4, "silver")
u.show()
print(u.get_pixel(3, 4))
sleep(1)
u.set_pixel_size(35)

print("Pausing 5 seconds before closing")
sleep(5)
