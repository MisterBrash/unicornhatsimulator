"""Rotation test"""

from time import sleep

# Change the import to unicornphat, unicornhat, or unicornhathd
# Remember - HD has origin in bottom-left, others top-left
from unicornhatsimulator import unicornhathd as u

u.rotation(0)
u.set_pixel(0, 0, 255, 0, 255)
u.set_pixel(0, 1,255, 255, 0)
u.set_pixel(1, 0, 0, 255, 0)
u.set_pixel(1, 1, 0, 0, 255)
u.set_pixel(7, 4, 255, 255, 255)
u.set_pixel(6, 4,255, 255, 0)
u.set_pixel(7, 3, 0, 255, 0)
u.set_pixel(6, 3, 0, 0, 255)
u.show()

while True:
    for r in range(0, 4):
        u.rotation(r*90)
        print(r*90)
        u.show()
        sleep(1)
