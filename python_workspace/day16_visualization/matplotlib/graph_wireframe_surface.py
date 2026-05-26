import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation # 1. 이 줄을 꼭 추가해야 해요!

def test_triangulation():
    x = np.arange(-5, 5, 0.25)
    y = np.arange(-5, 5, 0.25)
    xx, yy = np.meshgrid(x, y)
    rr = np.sqrt(xx**2 + yy**2)
    zz = np.sin(rr)

    tri = Triangulation(xx.flatten(), yy.flatten())
    
    plt.tripcolor(tri, zz.flatten(), cmap='viridis')
    plt.show()

if __name__ == "__main__":
    test_triangulation()