'''
Modified version of the unicorn-hat-sim package
from Mark Pitman (https://pypi.org/project/unicorn-hat-sim/)
which was a modified version from Jannis Hermanns (https://github.com/jayniz/unicorn-hat-sim)

The clear function wasn't working as expected and set_all wasn't implemented.
I've updated it below, however I'm not a python programmer
and there might be a better way. ~ Matt Brash

Origin (0, 0) is top-left for all three types of HATs. As far as I know, this is the
way Pimoroni designed them and it matches computer screens and game canvas, etc.
'''

# Version 1.0.4

import sys
import colorsys

try:
    import pygame
    import pygame.gfxdraw
except ImportError:
    print("To simulate a unicorn HAT on your computer, please pip install pygame")

COLORS = {
    'red': (255, 0, 0),
    'lime': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'magenta': (255, 0, 255),
    'cyan': (0, 255, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray': (127, 127, 127),
    'grey': (127, 127, 127),
    'silver': (192, 192, 192),
    'maroon': (128, 0, 0),
    'olive': (128, 128, 0),
    'green': (0, 128, 0),
    'teal': (0, 128, 128),
    'navy': (0, 0, 128),
    'orange': (255, 165, 0),
    'gold': (255, 215, 0),
    'purple': (128, 0, 128),
    'indigo': (75, 0, 130)
}

class UnicornHatSim:
    def __init__(self, width, height, rotation_offset=0):
        # Compat with old library
        self.AUTO = None
        self.PHAT = None

        # Set some defaults
        self.rotation_offset = rotation_offset
        self.rotation(0)
        self.pixels = [(0, 0, 0)] * width * height
        self.pixel_size = 20
        self.width = width
        self.height = height
        self.window_width = self.width * self.pixel_size
        self.window_height = self.height * self.pixel_size
        self.on = False
        self.clear()

    @property
    def COLORS(self):
        k = list(COLORS.keys())
        k.sort()
        return k
    
    def power_on(self):
        # Init pygame and off we go
        pygame.init()   
        pygame.display.set_caption("Unicorn HAT simulator")
        self.screen = pygame.display.set_mode(
            [self.window_width, self.window_height])
        self.on = True

    # Set the pixel size and resize the window (no error checking)
    def set_pixel_size(self, pixel_size):
        self.pixel_size = pixel_size
        self.window_width = self.width * self.pixel_size
        self.window_height = self.height * self.pixel_size
        #self.screen = pygame.display.set_mode(
            #[self.window_width, self.window_height])
        self.show()

    def set_pixel(self, x, y, r, g=None, b=None):
        if not self.on: self.power_on()
        i = (y * self.width) + x
        if type(r) is tuple:
            r, g, b = r

        elif type(r) is str:
            try:
                r, g, b = COLORS[r.lower()]

            except KeyError:
                raise ValueError('Invalid color!')

        self.pixels[i] = [int(r), int(g), int(b)]

    # Turn all pixels the given colour
    def set_all(self, r, g, b):
        if not self.on: self.power_on()
        self.pixels = [(r, g, b)] * self.width * self.height

    # Get the colour of a given pixel as a tuple
    def get_pixel(self, x, y):
        i = (y * self.width) + x
        return tuple(self.pixels[i])
  
    # Get all of the pixels (return the buffer)
    def get_pixels(self):
        # The actual HAT stores the pixels differently (in a 3D array)
        # Maybe I'll modify this in the future to match, but for now
        # we'll fake it. ~ M. Brash
        ret = []
        for y in range(0, self.width):
            ret.append([])
            for x in range(0, self.height):
                ret[y].append(self.pixels[(x * self.width) + y])

        return ret

    def draw(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:
                print("Exiting...")
                sys.exit()

        for x in range(self.width):
            for y in range(self.height):
                self.draw_led(x, y)

    def show(self):
        if not self.on: self.power_on()
        self.screen.fill((0, 0, 0))
        self.draw()
        pygame.display.update()

    def draw_led(self, x, y):
        self.draw_gfxcircle(x, y)

    def draw_gfxcircle(self, x, y):
        p = self.pixel_size
        w_x = int(x * p + self.pixel_size / 2)
        w_y = int(y * p + self.pixel_size / 2)
        r = int(self.pixel_size / 4)
        color = self.pixels[self.index(x, y)]
        #pygame.gfxdraw.aacircle(self.screen, w_x, w_y, r+1, (color[0],color[1],color[2],100))
        pygame.gfxdraw.filled_circle(self.screen, w_x, w_y, r, (color[0],color[1],color[2],140))
        pygame.gfxdraw.filled_circle(self.screen, w_x, w_y, int(r*.7), color)

    def get_shape(self):
        return (self.width, self.height)

    def brightness(self, *args):
        pass

    def rotation(self, r):
        self._rotation = int(round(r/90.0)) % 3

    # Clear the buffers
    def clear(self):
        self.pixels = [(0, 0, 0)] * self.width * self.height
        

    def get_rotation(self):
        return self._rotation * 90

    def set_layout(self, *args):
        pass

    def set_pixel_hsv(self, x, y, h, s=1.0, v=1.0):
        r, g, b = [int(n*255) for n in colorsys.hsv_to_rgb(h, s, v)]
        self.set_pixel(x, y, r, g, b)

    def off(self):
        print("Closing window")
        pygame.quit()

    def index(self, x, y):
        # Offset to match device rotation
        rot = (self.get_rotation() + self.rotation_offset) % 360

        if rot == 0:
            xx = x
            yy = y
        elif rot == 90:
            xx = self.height - 1 - y
            yy = x
        elif rot == 180:
            xx = self.width - 1 - x
            yy = self.height - 1 - y
        elif rot == 270:
            xx = y
            yy = self.width - 1 - x
        return (yy * self.width) + xx


'''
Expose the three types of HATs. None are rotated by default,
origin is top-left with y-values increasing as you go down the
screen. This is intentional and should match the physical device.
'''

# SD hat
unicornhat = UnicornHatSim(8, 8)

# Unicornhat HD
unicornhathd = UnicornHatSim(16, 16)

# PHAT
unicornphat = UnicornHatSim(8, 4)
