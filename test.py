'''Testing the simulator'''

from time import sleep
from random import randint
from unicornhatsimulator import unicornhathd as u

u.set_pixel_size(35)
sleep(1)
print("Window Loading... ")
u.set_pixel(3, 4, "silver")

for i in range(1, 5000):
    u.set_pixel(randint(0, 15), randint(0, 15), randint(0, 255), randint(0, 255), randint(0, 255))
    u.show()

v = u.get_pixels()
print(v)

print("Pausing 3 seconds before closing")
sleep(3)
