from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

def test_lmshow():
    digits = load_digits()
    plt.imshow(digits.images[1], cmap='jet', interpolation='bilinear')
    plt.show()

if __name__ == "__main__":
    test_lmshow()