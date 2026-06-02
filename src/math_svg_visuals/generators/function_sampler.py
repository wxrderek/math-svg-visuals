import numpy as np

def sample_path(f, t_range, dt: float):
    '''Samples from path in Rn representing the image of an R -> Rn function f'''
    times = np.arange(t_range[0], t_range[1] + dt, dt)
    points = np.array([f(t) for t in times])
    return points

def sample_surface(f, u_range, v_range, du: float, dv: float):
    '''Samples from surface in R^n representing the image of an R2 -> Rn function f'''
    u_vals = np.arange(u_range[0], u_range[1] + du, du)
    v_vals = np.arange(v_range[0], v_range[1] + dv, dv)

    surface = np.array([[f(u, v) for v in v_vals] for u in u_vals])
    return surface