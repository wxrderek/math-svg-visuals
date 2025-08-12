import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D projection
import numpy as np

def plot_2d_points(points, title='2D Plot', color='b', marker='.', linestyle='-', show=True):
    '''Plots 2D points from a (N, 2) numpy array'''
    x = points[:, 0]
    y = points[:, 1]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, color=color, marker=marker, linestyle=linestyle)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis("equal")  # keeps aspect ratio
    plt.grid(True)
    plt.tight_layout()

    if show:
        plt.show()


def plot_3d_points(points, title='', color='b', marker='.', show=True, 
    plot_scatter=True, show_grid=True, show_axis=True):
    '''Plots 3D points from a (N, 3) or (M, N, 3) numpy array'''
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection='3d')

    # reshape surface
    if points.ndim == 3 and not plot_scatter:
        x = points[:, :, 0]
        y = points[:, :, 1]
        z = points[:, :, 2]
        ax.plot_surface(x, y, z, color=color, edgecolor='k', alpha=0.8)
    else:
        if points.ndim == 3: points = points.reshape(-1, 3)
        x, y, z = points[:, 0], points[:, 1], points[:, 2]
        ax.scatter(x, y, z, c=color, marker=marker)
    
    # Set equal axis scaling
    all_xyz = np.concatenate([x.flatten(), y.flatten(), z.flatten()])
    min_val = np.min(all_xyz)
    max_val = np.max(all_xyz)
    mid = (min_val + max_val) / 2
    radius = (max_val - min_val) / 2

    ax.set_xlim(mid - radius, mid + radius)
    ax.set_ylim(mid - radius, mid + radius)
    ax.set_zlim(mid - radius, mid + radius)

    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    if not show_axis: ax.set_axis_off()
    ax.grid(show_grid)
    plt.tight_layout()

    if show:
        plt.show()
