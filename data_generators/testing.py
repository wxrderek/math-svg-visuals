import numpy as np
from data_generators.function_sampler import sample_path, sample_surface
from data_generators.plotting import plot_2d_points, plot_3d_points


# ==================== testing R3 surfaces ====================

def test_sphere(plot_scatter=True):
    def sphere(u, v):
        x = np.cos(u) * np.sin(v)
        y = np.sin(u) * np.sin(v)
        z = np.cos(v)
        return [x, y, z]
    samples = sample_surface(sphere, u_range=(0, 2*np.pi), v_range=(0, np.pi), du=0.05, dv=0.1)
    plot_3d_points(samples, plot_scatter=plot_scatter)


def test_torus(plot_scatter=True):
    def torus(u, v, R=1.0, r=0.3):
        x = (R + r * np.cos(v)) * np.cos(u)
        y = (R + r * np.cos(v)) * np.sin(u)
        z = r * np.sin(v)
        return [x, y, z]
    samples = sample_surface(lambda u, v: torus(u, v), u_range=(0, 2*np.pi), v_range=(0, 2*np.pi), du=0.1, dv=0.1)
    plot_3d_points(samples, plot_scatter=plot_scatter)


def test_sine_wave(plot_scatter=True):
    def sine_wave(u, v):
        x = u
        y = v
        z = np.sin(u) * np.cos(v)
        return [x, y, z]
    samples = sample_surface(sine_wave, u_range=(-2*np.pi, 2*np.pi), v_range=(-2*np.pi, 2*np.pi), du=0.2, dv=0.2)
    plot_3d_points(samples, plot_scatter=plot_scatter)


def test_saddle(plot_scatter=True):
    def saddle(u, v):
        x = u
        y = v
        z = u**2 - v**2
        return [x, y, z]
    samples = sample_surface(saddle, u_range=(-3, 3), v_range=(-3, 3), du=0.1, dv=0.1)
    plot_3d_points(samples, plot_scatter=plot_scatter)
        
    