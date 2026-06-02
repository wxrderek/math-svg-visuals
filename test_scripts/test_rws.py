from math_svg_visuals.utils import write_svg, build_svg_doc
from math_svg_visuals.features.randomized_shape_algorithms.random_walks import random_walk_line, random_walk_circles

# set viewbox width and height
VIEWBOX_WIDTH, VIEWBOX_HEIGHT = 1000, 1000

if __name__ == '__main__':

    # test for random walk circles
    rw_circles = random_walk_circles(step_size=15, n=10000, view_width=VIEWBOX_WIDTH, view_height=VIEWBOX_HEIGHT)
    svg_rw_circles = build_svg_doc(rw_circles, width=VIEWBOX_WIDTH, height=VIEWBOX_HEIGHT)
    write_svg(svg_rw_circles, filename='rw_circles.svg', dirname='test_svgs')

    # test for random walk line
    rw_line_test = random_walk_line(30, step_up_prob=0.05, view_width=VIEWBOX_WIDTH, view_height=VIEWBOX_HEIGHT)
    svg_rw_line = build_svg_doc(rw_line_test, width=VIEWBOX_WIDTH, height=VIEWBOX_HEIGHT)
    write_svg(svg_rw_line, filename='rw_line_test.svg', dirname='test_svgs')