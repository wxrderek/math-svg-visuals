from utils import write_svg, build_svg_doc
from features.random_circles import random_circles, random_circles_on_grid, random_walk_circles

# set viewbox width and height
VIEWBOX_WIDTH, VIEWBOX_HEIGHT = 1000, 1000

def main():

    # test for random circles on grid
    grid_circles = random_circles_on_grid(grid_size=100, view_width=VIEWBOX_WIDTH, view_height=VIEWBOX_HEIGHT)
    svg_grid_circles = build_svg_doc(grid_circles)
    write_svg(svg_grid_circles, filename='random_circles_grid.svg')

    # test for random walk circles
    rw_circles = random_walk_circles(step_size=15, n=10000, view_width=VIEWBOX_WIDTH, view_height=VIEWBOX_HEIGHT)
    svg_rw_circles = build_svg_doc(rw_circles)
    write_svg(svg_rw_circles, filename='random_walk_circles.svg')

if __name__ == '__main__':
    main()