import numpy as np
import matplotlib.pyplot as plt
import scipy 
from mpl_toolkits.mplot3d import Axes3D

def grad_3_1(X, Y):
    return Y, X

def print_grad_2D(grad_f, start_x = -1, end_x = 1, start_y = -1, end_y = 1, nbx = 10, nby = 10):
    """ This function is made to print the gradien of given function f """
    X, Y = np.meshgrid(np.linspace(start_x, end_x, nbx), np.linspace(start_y, end_y, nby))
    Gx, Gy = grad_f(X, Y)
    plt.quiver(X, Y, Gx, Gy)
    plt.show()

def print_contour_line( start_x = -1, end_x = 1, start_y = -1, end_y = 1, nbx = 10, nby = 10):
    X, Y = np.meshgrid(np.linspace(start_x, end_x, nbx), np.linspace(start_y, end_y, nby))
    Z = X*Y
    fig  = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z)
    plt.show()

def exercice_3_1():
    #Soit f(x,y) = x*y on veut determiner 1
    #le gradient de f au point x0, y0
    #on a grad(f) =  y*x_^ + x *
    # afichage du champ de vecteur 
    print_contour_line( -5, 5, -5, 5, 100, 100)
    


def exercice_3_2():
    p_vrai = [np.sqrt(2), -1, 1]
    t = np.array([i for i in range(-3,7)])
    yv = p_vrai[0]*t**2 + p_vrai[1]*t + p_vrai[2]
    y = np.round(yv)

    ##calcul de l'estimation
    M = np.vander(t, 3)
    print(M)
    p_est = np.linalg.lstsq(M, y)
    print(p_est)
if __name__ == "__main__":
    exercice_3_2()