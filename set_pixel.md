# Set_Pixel

As of the time of writing this, the full install of the [Pimoroni Unicorn-HAT-HD library](https://github.com/pimoroni/unicorn-hat-hd/tree/master) doesn't seem to include the updated `set_pixel()` function which accepts colour strings. Interestingly the source code _does_ include it. I'm not sure why the [source on Github](https://github.com/pimoroni/unicorn-hat-hd/blob/master/library/unicornhathd/__init__.py) does not match the [library on PyPi](https://pypi.org/project/unicornhathd/), but there you have it.

The `set_pixel()` function typically takes 5 integers - location and colour: `set_pixel(x, y, r, g, b)`

However, the updated version allows for a `string` description of the colour instead of `r, g, b`: `set_pixel(x, y, colour)`

**Example**:
```python
unicornhathd.set_pixel(4, 5, "red")
unicornhathd.set_pixel(7, 14, "teal")
```

The available colour strings are below:

```python
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
```


