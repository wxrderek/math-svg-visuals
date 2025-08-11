# svg_shapes/circle.py

class Circle:

    def __init__(self, cx: float, cy: float, r: float, fill: str='#000000', 
        stroke: str=None, stroke_width: float=1.0, 
        class_: str=None
    ):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.class_ = class_

    def to_svg(self) -> str:
        '''Returns svg circle element as a string'''
        attrs = [
            f'cx="{self.cx}"',
            f'cy="{self.cy}"',
            f'r="{self.r}"',
            f'fill="{self.fill}"'
        ]

        if self.stroke:
            attrs.append(f'stroke="{self.stroke}"')
            attrs.append(f'stroke-width="{self.stroke_width}"')

        if self.class_:
            attrs.append(f'class="{self.class_}"')

        return f'<circle {" ".join(attrs)} />'