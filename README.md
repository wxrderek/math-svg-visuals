# math-svg-visuals

Playing with SVG file generators wrapped in Python functions. 

End goal is to create SVG generators for mathematical visualizations/diagrams. 

### Potential Features
- Multiple random algorithms (sampling, random walks) to generate graphics based on standard geometric shapes (circles, rectangles)

- Feature to generate a path defined by some (Lipschitz) smooth vector-valued function by fitting Bezier curve segments to sampled points from function image

- Algorithms to build datasets for standard 3D shapes (cones, cylinders, smooth surfaces) which marked level curves to be displayed in desired perspectives via projection onto 2D planes

- Feature to generate a random graph with nodes sampled according to some 2D distribution and edges of different styles (between $\epsilon$-close nodes) to hopefully match some desired symbol

- Feature that samples 3D data from given 2D distribution of customized shape and constructs simplicial complexes (Cech, Vietoris-Rips) to hopefully match some desired symbol; see https://sauln.github.io/blog/nerve-playground/

- Feature that builds the 2D visual representation of a discrete-discrete or continuous-discrete optimal transport plan (based on Wasserstein metric) between distributions to hopefully match some desired symbol; see https://indico.cern.ch/event/845380/attachments/1915103/3241592/Dvurechensky_lectures.pdf