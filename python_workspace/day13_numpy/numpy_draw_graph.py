import matplotlib.pyplot as plt
import numpy as np

if False:
    x = np.linspace(-5, 5, 50)
    sin = np.sin(x)
    plt.plot(x, sin, label='sin(x)')
    plt.legend()
    plt.show()
elif True:
    x = np.linspace(-5, 5, 50)
    arcsin = np.arcsin(x)
    plt.plot(x, arcsin, label='arcsin(x)')
    plt.legend()
    plt.show()
