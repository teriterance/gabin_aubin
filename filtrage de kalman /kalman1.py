import numpy as np
import matplotlib.pyplot as plt 
import math
from mpl_toolkits.mplot3d import axes3d

def pi_de_x(x, y):
    x = np.array([[x],[y]])
    xbar = np.array([[1],[2]])
    cov = np.array([[1,0],[0,1]])
    u = np.exp( (-0.5 * (x-xbar).T).dot(np.linalg.inv(cov).dot((x-xbar))))
    v = 1/np.sqrt(np.power(2*np.pi, 0.5)*np.linalg.det(cov))
    return u*v

def pi_de_x_mat(x,y):
    a = len(x)
    u = x.copy()
    for i in range(a):
        for j in range(a):
            u[i][j] = pi_de_x(x[i][j], y[i][j])
    return u

def pi_de_x_mat_2(x,y):
    a = len(x)
    u = x.copy()
    v  = np.array([[np.cos(np.pi/6), -np.sin(np.pi/6)], [np.sin(np.pi/6), np.cos(np.pi/6)]])
    v = v.dot(np.array([[1,0],[0,1]]))
    delt = np.array([[2], [5]])
    for i in range(a):
        for j in range(a):
            tmp = v.dot(np.array([[x[i][j]], [y[i][j]]]))+ delt
            u[i][j] = pi_de_x(tmp[0][0], tmp[1][0])
    return u

def question1():
    x = np.linspace(-10,10, 100)
    y = np.linspace(-10,10, 100)
    X,Y = np.meshgrid(x,y)
    Z = pi_de_x_mat(X,Y)
    figure = plt.figure()
    axis = figure.add_subplot(111, projection = '3d')
    axis.plot_wireframe(X, Y, Z)
    plt.show()

def question2():
    x = np.linspace(-10,10, 100)
    y = np.linspace(-10,10, 100)
    X,Y = np.meshgrid(x,y)
    Z = pi_de_x_mat_2(X,Y)
    figure = plt.figure()
    axis = figure.add_subplot(111, projection = '3d')
    axis.plot_wireframe(X, Y, Z)
    plt.show()

if __name__ == "__main__":
    question1()
    question2()