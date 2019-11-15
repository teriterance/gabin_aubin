import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from mpl_toolkits.mplot3d import axes3d
from roblib import *

def elipse(w_bar, gama, nu):
    a = np.linspace(0, np.pi, 100)
    b = np.linspace(0, np.pi, 100)
    c = np.vstack((a,b))
    w = w_bar +np.sqrt(-np.log(1-nu))*np.power(gama, 0.5).dot(c)
    return w[0]+complex(0,1)*w[1]


def question1():
    A1 = np.array([[1, 0], [0, 3]])
    A2 = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)], [np.sin(np.pi/4), np.cos(np.pi/4)]])
    gama1 = np.array([[1,0],[0, 1]])
    gama2 = 3*gama1
    gama3 = A1.dot(gama2.dot(A1.T))+gama1
    gama4 = A2.dot(gama3.dot(A2.T))
    gama5 = gama4 + gama3
    gama6 = A2.dot(gama5.dot(A2.T))
    wbar = np.array([[0],[0]])
    ax= init_figure(-20,20,-20,20)
    draw_ellipse(np.array([[0],[0]]),gama1,0.9,ax,np.random.rand(3))
    draw_ellipse(np.array([[0],[0]]),gama2,0.9,ax,np.random.rand(3))
    draw_ellipse(np.array([[0],[0]]),gama3,0.9,ax,np.random.rand(3))
    draw_ellipse(np.array([[0],[0]]),gama4,0.9,ax,np.random.rand(3))
    draw_ellipse(np.array([[0],[0]]),gama5,0.9,ax,np.random.rand(3))
    draw_ellipse(np.array([[0],[0]]),gama6,0.9,ax,np.random.rand(3))
    plt.show()

if __name__ == "__main__":
    question1()