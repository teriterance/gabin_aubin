import numpy as np
import matplotlib.pyplot as pyplot


P = 0.1*np.random.rand(100,2)
print(P)
A = np.linspace(0, 4, 10)
B = np.linspace(2, 5, 10)
x1 = np.array([2,3,4,5,6,7,8,9,10])
y = np.array([28,204,88,472,938,1274,2202,3036,4499])
A_r = []
B_r = []
for p in P: 
#   scatter(p[0], p[1],color='black')
    for b in B:
        for a in A:
            x = np.power(x1, b)
            X = np.vstack([x*(1+p[0]), np.ones(len(x))]).T
            ym = np.linalg.lstsq(X, y+(p[1]))
            ym = ym[0][0]*x + ym[0][1]
            if np.max(np.abs(y-ym)) < 200:
                A_r.append(a)
                B_r.append(b)
print(A_r)
print(B_r)

x2 = np.log(x1)
A2 = np.log(A)
B2 = np.log(B)
y2 = np.log(y)

x = np.power(x2, b)
X = np.vstack([x, np.ones(len(x))]).T
ym = np.linalg.lstsq(X, y2)

a = np.exp(ym[0][1])
print(a)