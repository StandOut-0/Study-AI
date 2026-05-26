import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

def test_triangulation():
    x = np.linspace(-5, 5, 20)
    y = np.linspace(-5, 5, 20)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2 

    X_flat = X.flatten()
    Y_flat = Y.flatten()
    Z_flat = Z.flatten()

    tri = Triangulation(X_flat, Y_flat)

    plt.figure(figsize=(8, 6))
    plt.tripcolor(tri, Z_flat, cmap='viridis', edgecolors='k', lw=0.5)
    
    plt.title("Triangulation (tripcolor)")
    plt.colorbar(label='Height (Z)')
    plt.show()

if __name__ == "__main__":
    test_triangulation()