import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return x**2 + y**2

def test_contour():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    # plt.contour(X, Y, Z)
    plt.contourf(X, Y, Z)
    plt.show()

if __name__ == "__main__":
    test_contour()