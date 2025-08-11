import numpy as np
import random

from svg_shapes.circle import Circle

def random_circles(n: int, view_width: int=1000, view_height: int=1000) -> str:
    
    content = []
    for i in range(n):
        cx = random.randint(view_width//10, view_width-view_width//10)
        cy = random.randint(view_width//10, view_width-view_width//10)
        r = random.randint(view_width//20, view_width//5)
        random_circle = Circle(cx, cy, r, fill="#A4E9ED", stroke='#000000', stroke_width=10).to_svg()

        content.append(random_circle)

    return "\n".join(content)