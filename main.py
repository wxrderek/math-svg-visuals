import numpy as np

from utils import write_svg, build_svg_doc

from data_generators.function_sampler import sample_path, sample_surface
from data_generators.plotting import plot_2d_points, plot_3d_points

from features.randomized_shape_algorithms.random_circles import random_circles, random_circles_on_grid
from features.randomized_shape_algorithms.random_walks import random_walk_line, random_walk_circles

from svg_shapes.circle import Circle
from svg_shapes.path import Path
from svg_shapes.rect import Rectangle

# set viewbox width and height
VIEWBOX_WIDTH, VIEWBOX_HEIGHT = 1000, 1000

def main():

    '''
    # test for random walk circles
    rw_circles = random_walk_circles(step_size=15, n=10000, view_width=VIEWBOX_WIDTH, view_height=VIEWBOX_HEIGHT)
    svg_rw_circles = build_svg_doc(rw_circles, width=VIEWBOX_WIDTH, height=VIEWBOX_HEIGHT)
    write_svg(svg_rw_circles, filename='rw_circles.svg')

    # test for random walk line
    rw_line_test = random_walk_line(30, step_up_prob=0.05, view_width=VIEWBOX_WIDTH, view_height=VIEWBOX_HEIGHT)
    svg_rw_line = build_svg_doc(rw_line_test, width=VIEWBOX_WIDTH, height=VIEWBOX_HEIGHT)
    write_svg(svg_rw_line, filename='rw_line_test.svg')
    '''

    # testing samplers
    from data_generators.testing import test_sphere, test_torus, test_sine_wave, test_saddle
    test_saddle(plot_scatter=False)


if __name__ == '__main__':
    main()