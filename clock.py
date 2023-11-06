"""Digital clock display 12h format"""
from time import sleep
import datetime
try:
    import unicornhathd as u
    print("unicorn hat hd detected")
except ImportError:
    from unicornhatsimulator import unicornhathd as u

u.rotation(270)
u.clear()
u.brightness(0.8)
MICROSECOND = 1000000

small_nums = [[[True,True,True],[True,False,True],[True, False, True],[True,False,True],[True,True,True]],
        [[False, False, True],[False, False, True],[False, False, True],[False, False, True],[False, False, True]],
        [[True, True, True],[False, False,True],[True, True, True],[True, False, False],[True, True, True]],
        [[True, True, True],[False, False,True],[True, True, True],[False, False, True],[True, True, True]],
        [[True, False, True],[True, False,True],[True, True, True],[False, False, True],[False, False, True]],
        [[True, True, True],[True, False,False],[True, True, True],[False, False, True],[True, True, True]],
        [[True, True, True],[True, False,False],[True, True, True],[True, False, True],[True, True, True]],
        [[True, True, True],[False, False,True],[False, False, True],[False, False, True],[False, False, True]],
        [[True,True,True],[True,False,True],[True, True, True],[True,False,True],[True,True,True]],
        [[True, True, True],[True, False,True],[True, True, True],[False, False, True],[False, False, True]]]

# Draw the given number starting at top, left
def draw_num(top, left, digit, verbose = False):
    for y in range(5):
        if verbose: print(nums[digit][y][0], nums[digit][y][1], nums[digit][y][2])
        for x in range(3):
            if small_nums[digit][y][x]: u.set_pixel(top+y, left+x, 255, 220, 220)

# Display a given number at given top/left
def display(num, top = 0, left = 0):
    if len(num) == 1:
        num = "0" + num
    for x in num:
        if (x != " "):
            draw_num(top, left, int(x))
        left = left + 4

def dots(val):
    r = int(150 * (val % MICROSECOND)/MICROSECOND)
    g = int(100 * (val % MICROSECOND)/MICROSECOND)

    u.set_pixel(3, 7, r, g, g)
    u.set_pixel(5, 7, r, g, g)


while (True):
    u.clear()
    now = datetime.datetime.now()

    ''' draw each time string in their specific locations
    draw_time_string(now.month, 4, 0, 4, magenta)
    draw_time_string(now.day, 5, 0, 3, brown if now.day & 16 else blue)
    draw_time_string(now.hour, 6, 0, 2, red)
    draw_time_string(now.minute, 6, 0, 1, yellow)
    draw_time_string(now.second, 6, 0, 0, green)'''
    hour = ""

    if (now.hour > 12):
        hour = str(now.hour - 12)
    else:
        hour = str(now.hour)

    if (len(hour) == 1):
        hour = " " + hour
    display(hour, 2, 0)
    display(str(now.minute), 2, 8)
    if now.second % 2 == 0:
        dots(now.microsecond)
    else:
        dots(MICROSECOND - now.microsecond)
    u.show()

    sleep(0.05)
