# svg_shapes/rect.py

class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float,
        fill: str='#000000', fill_opacity: float=1.0, 
        stroke: str=None, stroke_width: float=1.0,
        class_: str=None
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill
        self.fill_opacity = fill_opacity
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.class_ = class_

    def to_svg(self) -> str:
        '''Returns svg rectangle element as a string'''
        attrs = [
            f'x="{self.x}"',
            f'y="{self.y}"',
            f'width="{self.width}"',
            f'height="{self.height}"',
            f'fill="{self.fill}"',
            f'fill-opacity="{self.fill_opacity}"'
        ]

        if self.stroke:
            attrs.append(f'stroke="{self.stroke}"')
            attrs.append(f'stroke-width="{self.stroke_width}"')

        if self.class_:
            attrs.append(f'class="{self.class_}"')

        return f'<rect {" ".join(attrs)} />'