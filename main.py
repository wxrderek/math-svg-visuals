from utils import write_svg, build_svg_doc
from random_circles import random_circles

# set viewbox width and height
VIEWBOX_WIDTH, VIEWBOX_HEIGHT = 1000, 1000

def main():
    text = random_circles(20, VIEWBOX_WIDTH, VIEWBOX_HEIGHT)
    svg_doc = build_svg_doc(text)
    write_svg(svg_doc, filename='test.svg')

if __name__ == '__main__':
    main()