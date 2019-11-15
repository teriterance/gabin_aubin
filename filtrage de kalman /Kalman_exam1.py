from roblib import *
import numpy as np

def question1():
    ##on de finit notre fonction comme x= randmon(1000, 1) et y  = -x d'ou on a la matrice de covariance [[1 0][0 1]]
    N = 600
    X = randn(2, N)
    gama_x = np.array([[5, 2], [2, 5]])
    
    xbar = np.array([[-3], [5]])
    x = sqrtm(gama_x).dot(X) + xbar
    c = []
    ax= init_figure(-100,100,-100,100)
    draw_ellipse(xbar, gama_x, 0.7, ax, np.random.rand(3))
    dt = 0.5
    for k in range(1,7):
        x = x + dt*evolution(x, (k/2)**2)
        xbar[0] = np.mean(x[:,0])
        xbar[1] = np.mean(x[:,1])
        gama_x = np.cov(x)
        c.append(x)
        draw_ellipse(xbar, gama_x, 0.7, ax, np.random.rand(3))
    plt.show()
    plt.re

def evolution(x_k, u):
    B =  np.array([[1], [2]])
    A = np.array([[0,-1], [1,0]])
    d = A.dot(x_k) + B*u
    return d

def question_2_1():
    pass

if __name__ == "__main__":
    question1()