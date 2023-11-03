'''
TESTING THE STANDARD UNICORN HAT (8, 8)
'''

from time import sleep
from random import randint

try:
    import unicornhathd as u
    print("unicorn hat hd detected")
except ImportError:
    from unicornhatsimulator import unicornhat as u

while True:
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    u.set_pixel(x, y, r, g, b)
    u.show()
    sleep(0.01)
