'''
Modified version of the unicorn-hat-sim package
from Mark Pitman (https://pypi.org/project/unicorn-hat-sim/)
which was a modified version from Jannis Hermanns (https://github.com/jayniz/unicorn-hat-sim)

The clear function wasn't working as expected and set_all wasn't implemented.
That snowballed into a pretty extensive adjustment / rewrite.
I'm not a python programmer and there might be a better way. ~ Matt Brash

Origin (0, 0) is top-left for PHAT and HAT, bottom-left for HATHD
'''

# Version 1.0.4

import sys
import colorsys

try:
    import pygame
    import pygame.gfxdraw
except ImportError:
    print("To simulate a unicorn HAT on your computer, please pip install pygame")

VERSION = "1.0.4"

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
    """Class representing a Pimoroni Unicorn HAT of various size"""
    def __init__(self, width, height, flip=False):
        # Compat with old library
        self.AUTO = None
        self.PHAT = None

        # Set some defaults
        self._flip = flip
        self._pixels = [(0, 0, 0)] * width * height
        self._pixel_size = 20
        self.width = width
        self.height = height
        self._window_width = self.width * self._pixel_size
        self._window_height = self.height * self._pixel_size
        self._screen = None
        self._on = False
        self.rotation(0)
        self.clear()

    @property
    def colors(self):
        """List the available colour strings (non-standard)"""
        k = list(COLORS.keys())
        k.sort()
        return k

    def power_on(self):
        """Initialize pygame, show the window, etc"""
        pygame.init()
        pygame.display.set_caption("Simulator v" + VERSION)
        print("Unicorn HAT simulator v" + VERSION)
        self._screen = pygame.display.set_mode(
            [self._window_width, self._window_height])
        self._on = True

    def set_pixel_size(self, pixel_size):
        """Set the pixel size and resize the window (no error checking)"""
        self._pixel_size = pixel_size
        self._window_width = self.width * self._pixel_size
        self._window_height = self.height * self._pixel_size
        self.show()

    def set_pixel(self, x, y, r, g=None, b=None):
        """Set the value of a pixel in the buffer based on RGB"""
        if not self._on:
            self.power_on()
        i = (y * self.width) + x
        if isinstance(r, tuple):
            r, g, b = r

        elif isinstance(r, str):
            try:
                r, g, b = COLORS[r.lower()]

            except KeyError as e:
                raise ValueError('Invalid color!') from e

        try:
            self._pixels[i] = [int(r), int(g), int(b)]
        except IndexError:
            print("Index out of bounds", x, "on", self.width, "and", y, "on", self.height)

    def set_pixel_hsv(self, x, y, h, s=1.0, v=1.0):
        """Set a single pixel in the buffer based on Hue, Saturation, Vibrance"""
        r, g, b = [int(n*255) for n in colorsys.hsv_to_rgb(h, s, v)]
        self.set_pixel(x, y, r, g, b)

    def set_all(self, r, g, b):
        """Set all pixels the given RGB (in the buffer)"""
        if not self._on:
            self.power_on()
        self._pixels = [(r, g, b)] * self.width * self.height

    def get_pixel(self, x, y):
        """Get the colour of a given pixel as a tuple"""
        return tuple(self._pixels[(y * self.width) + x])

    def get_pixels(self):
        """Get all of the pixels (return the buffer)"""
        # The actual HAT stores the pixels differently (in a 3D array)
        # Maybe I'll modify this in the future to match, but for now
        # we'll fake it. ~ M. Brash
        ret = []
        for y in range(0, self.width):
            ret.append([])
            for x in range(0, self.height):
                ret[y].append(self._pixels[(x * self.width) + y])

        return ret

    def show(self):
        """Update the HAT based on the data in the buffer"""
        if not self._on:
            self.power_on()

        self._screen.fill((0, 0, 0))

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:
                print("Exiting...")
                sys.exit()

        for x in range(self.width):
            for y in range(self.height):
                self.__draw_gfxcircle(x, y)

        pygame.display.update()

    def __draw_gfxcircle(self, x, y):
        """Draw a single LED"""
        p = self._pixel_size
        w_x = int(x * p + self._pixel_size / 2)
        w_y = int(y * p + self._pixel_size / 2)
        r = int(self._pixel_size / 4)
        color = self._pixels[self.__index(x, y)]
        #pygame.gfxdraw.aacircle(self._screen, w_x, w_y, r, (color[0],color[1],color[2],100))
        pygame.gfxdraw.filled_circle(self._screen, w_x, w_y, r, (color[0],color[1],color[2],140))
        pygame.gfxdraw.filled_circle(self._screen, w_x, w_y, int(r*.7), color)

    def get_shape(self):
        """Get the dimensions of the screen (HAT)"""
        return (self.width, self.height)

    def brightness(self, *args):
        """Set the brightness of the HAT (currently not used)"""
        pass

    def rotation(self, r):
        """Set the rotation of the HAT"""
        # Round to the nearest 90 degrees if height == width
        if self.width == self.height:
            self._rotation = round(r/90) * 90 % 360
        else:
            self._rotation = round(r/180) * 180 % 360

    def clear(self):
        """Clear the buffer (but not the screen)"""
        self._pixels = [(0, 0, 0)] * self.width * self.height

    def get_rotation(self):
        """Get the rotation setting for the HAT"""
        return self._rotation

    def set_layout(self, *args):
        """Not used, here for compatibility"""
        pass

    def off(self):
        """Turn off the HAT (clear and show)"""
        self.clear()
        self.show()

    def __index(self, x, y):
        """Return the index of a pixel within the buffer"""
        # Offset to match device rotation (counter clockwise)
        rot = self.get_rotation()

        if rot == 0:
            xx = x
            yy = self.height - 1 - y if self._flip else y
        elif rot == 90:
            xx = self.height - 1 - y
            yy = self.width - 1 - x if self._flip else x
        elif rot == 180:
            xx = self.width - 1 - x
            yy = y if self._flip else self.height - 1 - y
        elif rot == 270:
            xx = y if self._flip else y
            yy = x if self._flip else self.width - 1 - x

        return (yy * self.width) + xx

# Expose the three types of HATs. None are rotated by default,
# origin is top-left with y-values increasing as you go down the
# screen. This is intentional and should match the physical device.

# SD hat
unicornhat = UnicornHatSim(8, 8)

# Unicornhat HD (origin is the bottom-left)
unicornhathd = UnicornHatSim(16, 16, True)

# PHAT
unicornphat = UnicornHatSim(8, 4)
