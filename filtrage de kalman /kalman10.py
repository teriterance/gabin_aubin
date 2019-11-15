from roblib import *

def question1():
    A = array([[1,0],[0,1]])
    x = array([[0],[0]])
    C = array([[2, 3]])
    u = 0
    y = 8
    C1=array([[3,2]])
    C2=array([[1,-1]])

    Gx = 1000*array([[1,0],[0,1]])
    Galpha = array([[0, 0], [0,0]])
    x, Gx = kalman(x,Gx,u,y,Galpha,1,A,C)
    ax=init_figure(-5,5,-5,5)
    #draw_ellipse(x, Gx, 0.9, ax, np.random.rand(3))
    print("les valeurs de x et Gx sont ")
    print(x,Gx)
    y = 7
    x, Gx = kalman(x,Gx,u,y,Galpha,4,A,C1)
    draw_ellipse(x, Gx, 0.9, ax, np.random.rand(3))
    print("les valeurs de x et Gx sont ")
    print(x,Gx)
    y = 0

    x, Gx = kalman(x,Gx,u,y,Galpha,4,A,C2)
    draw_ellipse(x, Gx, 0.9, ax, np.random.rand(3))
    print("les valeurs de x et Gx sont ")
    print(x,Gx)
    plt.show()

if __name__ == "__main__":
    question1()