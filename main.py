from utils import write_svg, build_svg_doc
from features.random_circles import random_circles, random_circles_on_grid, random_walk_circles
from svg_shapes.path import Path

# set viewbox width and height
VIEWBOX_WIDTH, VIEWBOX_HEIGHT = 1000, 1000

def main():

    # test for random circles on grid
    grid_circles = random_circles_on_grid(grid_size=100, view_width=VIEWBOX_WIDTH, view_height=VIEWBOX_HEIGHT)
    svg_grid_circles = build_svg_doc(grid_circles, width=VIEWBOX_WIDTH, height=VIEWBOX_HEIGHT)
    write_svg(svg_grid_circles, filename='random_circles_grid.svg')

    # test for random walk circles
    rw_circles = random_walk_circles(step_size=15, n=10000, view_width=VIEWBOX_WIDTH, view_height=VIEWBOX_HEIGHT)
    svg_rw_circles = build_svg_doc(rw_circles, width=VIEWBOX_WIDTH, height=VIEWBOX_HEIGHT)
    write_svg(svg_rw_circles, filename='random_walk_circles.svg')

    # test Path class
    path_test = Path(500, 500, fill='none', stroke='#0077cc', stroke_width=10)
    path_test.add_cubic_bezier(700, 300, 900, 700, 100, 900)
    path_test.add_cubic_bezier(100, 700, 300, 300, 900, 100)
    path_test.add_cubic_bezier(700, 300, 900, 700, 100, 900)
    path_test.add_cubic_bezier(100, 700, 300, 300, 500, 500)
    svg_path_test = build_svg_doc(path_test.to_svg(), width=VIEWBOX_WIDTH, height=VIEWBOX_HEIGHT)
    write_svg(svg_path_test, filename='path_test.svg')

if __name__ == '__main__':
    main()