'''
Modified version of the unicorn-hat-sim package
from Mark Pitman (https://pypi.org/project/unicorn-hat-sim/)
which was a modified version from Jannis Hermanns (https://github.com/jayniz/unicorn-hat-sim)

The clear function wasn't working as expected and set_all wasn't implemented.
I've updated it below, however I'm not a python programmer
and there might be a better way. ~ Matt Brash
In the future I want to add other functions to resize the pixels, etc
'''

# Version 1.0.4

import sys
import colorsys
import pygame.gfxdraw

try:
    import pygame
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

class UnicornHatSim(object):
    def __init__(self, width, height, rotation_offset=0):
        # Compat with old library
        self.AUTO = None
        self.PHAT = None

        # Set some defaults
        self.rotation_offset = rotation_offset
        self.rotation(0)
        self.pixels = [(0, 0, 0)] * width * height
        self.pixel_size = 15
        self.width = width
        self.height = height
        self.window_width = width * self.pixel_size
        self.window_height = height * self.pixel_size

        # Init pygame and off we go
        pygame.init()   
        pygame.display.set_caption("Unicorn HAT simulator")
        self.screen = pygame.display.set_mode(
            [self.window_width, self.window_height])
        self.clear()

    # Set the pixel size and resize the window (no error checking)
    def set_pixel_size(self, pixel_size):
        self.pixel_size = pixel_size
        self.window_width = self.width * self.pixel_size
        self.window_height = self.height * self.pixel_size
        self.screen = pygame.display.set_mode(
            [self.window_width, self.window_height])
        self.show()

    def set_pixel(self, x, y, r, g=None, b=None):
        i = (x * self.width) + y
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
        self.pixels = [(r, g, b)] * self.width * self.height

    # Get the colour of a given pixel as a tuple
    def get_pixel(self, x, y):
        i = (x * self.width) + y
        return tuple(self.pixels[i])
  
    # Get all of the pixels (return the buffer)
    def get_pixels(self):
        return self.pixels

    def draw(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:
                print("Exiting...")
                sys.exit()

        for x in range(self.width):
            for y in range(self.height):
                self.draw_led(x, y)

    def show(self):
        self.screen.fill((0, 0, 0))
        self.draw()
        pygame.display.flip()

    def draw_led(self, x, y):
        self.draw_gfxcircle(x, y)

    def draw_gfxcircle(self, x, y):
        p = self.pixel_size
        w_x = int(x * p + self.pixel_size / 2)
        w_y = int((self.height - 1 - y) * p + self.pixel_size / 2)
        r = int(self.pixel_size / 4)
        color = self.pixels[self.index(x, y)]
        pygame.gfxdraw.aacircle(self.screen, w_x, w_y, r, color)
        pygame.gfxdraw.filled_circle(self.screen, w_x, w_y, r, color)

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
        return (xx * self.width) + yy


# SD hats works as expected
unicornhat = UnicornHatSim(8, 8)
unicornphat = UnicornHatSim(8, 4)

# Unicornhat HD seems to be the other way around (not that there's anything wrong with that), so we rotate it 180°
unicornhathd = UnicornHatSim(16, 16, 180)
