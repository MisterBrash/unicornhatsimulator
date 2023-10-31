# Unicorn HAT (HD) simulator
Unicorn HAT (HD) simulator - Originally by Jannis Hermanns &lt;jannis@gmail.com>, modified by Mark Pitman &lt;mark.pitman@gmail.com> and adjusted by me (Matt Brash &lt;matt@brash.ca>)

Simulates a Unicorn HAT HD (and should work for the 8x8 HAT and the 8x4 PHAT as well) using pygame.
The version you see here includes the following edits:
- Added `set_all(r, g, b)` to set the entire buffer to one colour
- Modified the `clear()` function to act like the real HAT (clears the buffer, not the screen)
- Added `get_pixel(x, y)` to return a tuple of the r, g, b values of a pixel
- Added `get_pixels()` which returns the entire buffer as an array of arrays of arrays ([y][x][r, g, b])
- Modified `set_pixel()` to accept a colour string, for example `set_pixel(x, y, "red")` see [set_pixel.md](set_pixel.md)
- Added the non-standard `set_pixel_size(value)` which is only for the simulator to increase or decrease the dot size

## Usage

If you want your code to run on your computer as well as your Pi, you could do something like this:

1. `pip install unicornhatsimulator` (or `pip2` or `pip3` depending on your setup)
2. Adjust your `import unicornhathd` statement as follows:

```python
'''
Note: The alias "as unicorn" can be whatever you want (or nothing at all).
For example: as u
'''
try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicornhatsimulator import unicornhathd as unicorn
```

You can choose from `import unicornhathd` (16x16), `import unicornhat` (8x8) and `import unicornphat` (8x4). 

## Demo

(Note that this gif has a low framerate, the simulator runs nice and smooth in real life)

![Demo](https://cl.ly/2s070z1k0L3J/Screen%20Recording%202017-06-26%20at%2011.12%20PM.gif)

## TODO

- [ ] find a python person to show me how this would be done properly. For example - leaving the window open at the end.
- [ ] fix/check rotation
- [ ] add a proper LED glow effect so it looks more like a real unicorn HAT
- [x] publish via pip ([now online at pypi](https://pypi.org/project/unicornhatsimulator/))
- [x] add `get_pixel(x, y)` and `get_pixels`
- [x] add non-standard `set_pixel_size(p)` to increase or decrease dot sizes

---

#### Disclaimer

I am _not_ a `pygame` programmer. I'm barely a `python` programmer. I found the original code for the simulator and tried to modify it to match the current state of the [Pimoroni UnicornhatHD](https://github.com/pimoroni/unicorn-hat-hd) library. This was in order to have my students be able to work on their projects in [Replit](https://replit.com) when they don't have access to their physical raspberry pi's from class.

Feel free to leave suggestions (issues, bugs) but do not expect a timely response.


~ M. Brash

