import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def test_surface_with_tri_bottom():
    x = np.arange(-3, 3, 0.3)
    y = np.arange(-3, 3, 0.3)
    xx, yy = np.meshgrid(x, y)
    xf, yf = xx.flatten(), yy.flatten()
    zf = np.cos(xf) * np.cos(yf)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_trisurf(xf, yf, zf, cmap=cm.jet)

    ax.tricontourf(xf, yf, zf, zdir='z', offset=-1.5, cmap=cm.jet, alpha=0.5)

    ax.set_zlim(-1.5, 1)    # 
    ax.view_init(30, -45)   
    
    plt.show()

if __name__ == "__main__":
    test_surface_with_tri_bottom()