import numpy as np
import random

from svg_shapes.circle import Circle
from utils import random_hex_code

def random_circles(n: int, view_width: int=1000, view_height: int=1000) -> str:
    '''Draws n random circles at random locations with random radii'''
    content = []
    for i in range(n):
        cx = random.randint(view_width//10, view_width-view_width//10)
        cy = random.randint(view_width//10, view_width-view_width//10)
        r = random.randint(view_width//25, view_width//7)
        rand_fill = random_hex_code((15, 50, 220), (100, 255, 255))
        rand_opacity = random.randint(5, 10)/10.0

        # outline shape
        random_circle_outline = Circle(cx, cy, r+view_width//75, fill='#000000', fill_opacity=0.5).to_svg()
        content.append(random_circle_outline)

        # fill shape
        random_circle = Circle(cx, cy, r, fill=rand_fill, fill_opacity=rand_opacity).to_svg()
        content.append(random_circle)

    return "\n".join(content)