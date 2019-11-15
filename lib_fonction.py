import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import scipy.linalg


def print_grad_2D(grad_f, start_x = -1, end_x = 1, start_y = -1, end_y = 1, nbx = 10, nby = 10):
    """ This function is made to print the gradien of given function f """
    X, Y = np.meshgrid(np.linspace(start_x, end_x, nbx), np.linspace(start_y, end_y, nby))
    Gx, Gy = grad_f(X, Y)
    plt.quiver(X, Y, Gx, Gy)
    plt.show()

def print_contour_line(f, start_x = -1, end_x = 1, start_y = -1, end_y = 1, nbx = 10, nby = 10):
    X, Y = np.meshgrid(np.linspace(start_x, end_x, nbx), np.linspace(start_y, end_y, nby))
    Z = X*Y
    plt.contour(X, Y, Z)
    plt.plot()