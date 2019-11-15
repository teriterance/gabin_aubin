from roblib import *
import numpy as np
import scipy as sc

def question1():
    ##on de finit notre fonction comme x= randmon(1000, 1) et y  = -x d'ou on a la matrice de covariance [[1 0][0 1]]
    N = 1000
    X = randn(2, N)
    gama_x = np.array([[4, 3], [3, 3]])
    xbar = np.array([[1], [2]])
    x = sqrtm(gama_x).dot(X) + xbar
    #plot(x[0,:], x[1,:], '+')
    return x, xbar, gama_x

def question2():
    x, xbar, gama_x = question1()
    ax= init_figure(-20,20,-20,20)
    plot(x[0,:], x[1,:], '+')
    draw_ellipse(xbar, gama_x, 0.9, ax, np.random.rand(3))
    draw_ellipse(xbar, gama_x, 0.99, ax, np.random.rand(3))
    draw_ellipse(xbar, gama_x, 0.999, ax, np.random.rand(3))
    show()

def question3():
    #on regarde juste le rapport entre le nombre de points dans l'elipse de confience et le nombre de points hors de l'elipse de confiance 
    pass

def question4():
    pass

if __name__ == "__main__":
    question2()