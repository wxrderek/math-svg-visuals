import numpy as np
import random

from svg_shapes.circle import Circle
from svg_shapes.rect import Rectangle
from utils import set_bg

def random_walk_circles(step_size: int, n: int, view_width: int=1000, view_height: int=1000) -> str:
    '''Draws circles based on 2D random walk along axis directions for n steps, starting from center'''
    content = []
    content.append(set_bg('#2B2B2B', view_width, view_height))
    
    # first circle
    x, y = view_width//2, view_height//2
    first_circle = Circle(x, y, r=step_size//4, fill='#FFFFFF').to_svg()
    content.append(first_circle)

    # random walk
    for i in range(n):
        step_prob = random.randint(0, 1)
        step_dir = random.randint(0, 1)

        # prevent from walking out of grid
        if x-step_size//4 < 0: step_prob, step_dir = 1, 0
        elif x+step_size//4 > view_width: step_prob, step_dir = 0, 0
        if y-step_size//4 < 0: step_prob, step_dir = 1, 1
        elif y+step_size//4 > view_height: step_prob, step_dir = 0, 1

        if step_prob==1:
            if step_dir==0: x += step_size
            else: y += step_size
        else:
            if step_dir==0: x -= step_size
            else: y -= step_size
        
        # generate circle
        circle = Circle(x, y, r=step_size//4, fill='#FFFFFF').to_svg()
        content.append(circle)

    return "\n".join(content)


def random_walk_line(step_size: int, step_up_prob: float=0.2, view_width: int=1000, view_height: int=1000) -> str:
    '''Draws lines corresponding to random walks in x direction'''
    content = []
    content.append(set_bg('#2B2B2B', view_width, view_height))

    # initial position
    x0, y0 = view_width//2, view_height-step_size
    x = x0

    # random walk
    for y in range(y0, 0, -step_size):
        
        step_prob = np.random.choice([0, 1], size=1, replace=True, p=[step_up_prob, 1-step_up_prob])[0]
        while step_prob==1:
            step_dir = random.randint(0, 1)

            # prevent from walking out of grid
            if x-step_size < 0: step_dir = 1
            elif x+step_size > view_width: step_dir = 0

            if step_dir==0: x -= step_size
            else: x += step_size
            step_prob = np.random.choice([0, 1], size=1, replace=True, p=[step_up_prob, 1-step_up_prob])[0]

            # generate rectangle
            rectangle = Rectangle(x, y, step_size, step_size//10, fill='#FFFFFF').to_svg()
            content.append(rectangle)
    
    return "\n".join(content)