# svg_shapes/path.py

class Path:
    def __init__(self, start_x: float, start_y: float,
        fill: str="none", fill_opacity: float=1.0,
        stroke: str="#000000", stroke_width: float=1.0,
        class_: str=None
    ):
        '''Create svg path element with specific start point only'''
        self.start = (start_x, start_y)
        self.fill = fill
        self.fill_opacity = fill_opacity
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.class_ = class_

        # initialize 'd' attribute at specified start point
        self.d = f"M {start_x} {start_y}"


    def add_cubic_bezier(self, c1x: float, c1y: float, c2x: float, c2y: float, x: float, y: float):
        '''Append a cubic Bezier segment to the path'''
        self.d += f" C {c1x} {c1y}, {c2x} {c2y}, {x} {y}"


    def to_svg(self) -> str:
        '''Returns svg path element as a string'''
        attrs = [
            f'd="{self.d}"',
            f'fill="{self.fill}"',
            f'fill-opacity="{self.fill_opacity}"',
            f'stroke="{self.stroke}"',
            f'stroke-width="{self.stroke_width}"'
        ]

        if self.class_:
            attrs.append(f'class="{self.class_}"')

        return f'<path {" ".join(attrs)} />'