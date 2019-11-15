from roblib import *

def question1():
    A0 = array([[0.5, 0],[0,1]])
    A1 = array([[1,-1],[1,1]])
    A2 = array([[1, -1],[1,1]])

    u0 = array([[8],[16]])
    u1 = array([[-6],[-18]])
    u2 = array([[32],[-8]])

    C= array([[1,1]])

    y0 = 7
    y1 = 30
    y2 = -6
    
    Galpha = array([[1,0],[0,1]])
    Gbeta = 1

    x0 = array([[0],[0]])
    gama0 = 100*eye(2)

    ax=init_figure(-200,200,-200,200)

    x, Gx =kalman(x0, gama0, u0, y0, Galpha, Gbeta, A0, C)
    draw_ellipse(x, Gx, 0.9, ax, np.random.rand(3))

    x, Gx =kalman(x, Gx, u1, y1, Galpha, Gbeta, A1, C)
    draw_ellipse(x, Gx, 0.9, ax, np.random.rand(3))
    
    x, Gx =kalman(x, Gx, u2, y2, Galpha, Gbeta, A2, C)
    draw_ellipse(x, Gx, 0.9, ax, np.random.rand(3))

    plt.show()


if __name__ == "__main__":
    b=randn(3)

    A0=np.array([[0.5, 0],
                [0, 1]])
    A1=np.array([[1, -1],
                [1, 1]])
    A2=A1
    u0=np.array([[8],
                [16]])
    u1=np.array([[-6],
                [-18]])
    u2=np.array([[32],
                [-8]])
    C0=np.array([[1, 1]])
    C1=C0
    C2=C0
    y0=7
    y1=30
    y2=-6
    Γalpha=eye(2)
    Γbeta=1

    X0=zeros((2,1))
    Γ0=100*eye(2)

    #Affichage
    ax=init_figure(-40,40,-40,40)
    draw_ellipse(X0, Γ0, 0.9, ax, np.random.rand(3))
    Xhat1, Γhat1 = kalman(X0,Γ0,u0,y0,Γalpha,b[0],A0,C0)
    draw_ellipse(Xhat1, Γhat1, 0.9, ax, np.random.rand(3))
    Xhat2, Γhat2 = kalman(Xhat1,Γhat1,u1,y1,Γalpha,b[1],A1,C1)
    draw_ellipse(Xhat2, Γhat2, 0.9, ax, np.random.rand(3))
    Xhat3, Γhat3 = kalman(Xhat2, Γhat2,u2,y2,Γalpha,b[2],A2,C2)
    draw_ellipse(Xhat3, Γhat3, 0.9, ax, np.random.rand(3))
    plt.title("Ellipses de confiance à 90%")
    plt.show()