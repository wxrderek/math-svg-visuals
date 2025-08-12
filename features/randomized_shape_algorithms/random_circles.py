import numpy as np
import random

from svg_shapes.circle import Circle
from utils import random_hex_code, random_hex_grey, set_bg

def random_circles(n: int, view_width: int=1000, view_height: int=1000) -> str:
    '''Draws n random circles at random locations with random radii'''
    content = []
    content.append(set_bg('#2B2B2B', view_width, view_height))
    for i in range(n):

        # random location, radius, fill, opacity
        cx = random.randint(view_width//10, view_width-view_width//10)
        cy = random.randint(view_height//10, view_height-view_height//10)
        r = random.randint(view_width//25, view_width//7)
        rand_fill = random_hex_code((15, 50, 220), (100, 255, 255))
        rand_opacity = random.randint(5, 10)/10.0

        # outline shape
        random_circle_outline = Circle(cx, cy, r+view_width//75, fill='#2B2B2B', fill_opacity=0.5).to_svg()
        content.append(random_circle_outline)

        # fill shape
        random_circle = Circle(cx, cy, r, fill=rand_fill, fill_opacity=rand_opacity).to_svg()
        content.append(random_circle)

    return "\n".join(content)


def random_circles_on_grid(grid_size: int, view_width: int=1000, view_height: int=1000) -> str:
    '''Draws circles of random radii on grid coordinates'''
    content = []
    content.append(set_bg('#2B2B2B', view_width, view_height))
    # iterate through grid
    for x in range(grid_size, view_width-grid_size+1, grid_size):
        for y in range(grid_size, view_height-grid_size+1, grid_size):
            # random radius, fill
            r = random.randint(grid_size//5, grid_size//2)
            rand_fill = random_hex_grey(150, 255)

            circle = Circle(x, y, r, fill=rand_fill).to_svg()
            content.append(circle)
    
    return "\n".join(content)