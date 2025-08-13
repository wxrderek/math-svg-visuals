# math-svg-visuals

Playing with SVG file generators wrapped in Python functions. 

End goal is to create SVG generators for mathematical visualizations/diagrams. 

### Potential Features
- Multiple random algorithms (sampling, random walks) to generate graphics based on standard geometric shapes (circles, rectangles)

- Feature to generate a path defined by some (Lipschitz) smooth vector-valued function by fitting Bezier curve segments to sampled points from function image

- Features to build datasets for standard 3D shapes (cones, cylinders, smooth surfaces) to plot in with matplotlib from a desired orientation
    - Option to display level curves (argument in plot_surface)
    - Note that the SVGs exported form matplotlib tend do be built from small shapes made from straight paths, not Bezier curves
    - Several matplotlib artifacts may be to be removed after exporting; need for a post-export pipeline to ensure usability of output

- Feature to generate a random graph with nodes sampled according to some 2D distribution and edges of different styles (between $\epsilon$-close nodes) to hopefully match some desired symbol

- Feature that samples 3D data from given 2D distribution of customized shape and constructs simplicial complexes (Cech, Vietoris-Rips) to hopefully match some desired symbol; see https://sauln.github.io/blog/nerve-playground/

- Feature that builds the 2D visual representation of a discrete-discrete optimal transport plan (based on Wasserstein metric) between distributions to hopefully match some desired symbol; see https://indico.cern.ch/event/845380/attachments/1915103/3241592/Dvurechensky_lectures.pdf
    - Mathematically, optimal transport plan matrices between 1D probability distributions are constrained to c-cyclically monotone supports, meaning desired symbols cannot be arbitrary: https://math.univ-lyon1.fr/~santambrogio/SupportcCM.pdf
    - Alternatively, given a desired matrix that satisfies the probabilistic constraints, it uniquely determines the distributions from/to which it maps; an arbitrary symbol is guaranteed to be a possible transport plan, just not an optimal transport plan

- Feature to simulate Conway's game of life on a small 2D grid and use the output after a set number of iterations to flexibly build an SVG representation of the grid
    - Function to set the initial state of the grid to some desired arrangement
    - Mechanism which leaves an "afterimage" of living squares up to the next iteration; each arrangement is stored for 2 iterations