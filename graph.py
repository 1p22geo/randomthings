import matplotlib.pyplot as plt
import numpy as np
from things import Complex as Comp
np.random.seed(19680801)

SAMPLE_SIZE = 10

fig, ax = plt.subplots(2,2)
dots = np.linspace(0, 1, SAMPLE_SIZE)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
x1 = x.copy()
y1 = y.copy()
x2 = x.copy()
y2 = y.copy()
x3 = x.copy()
y3 = y.copy()

a = Comp(2,3)
b = Comp(4,-2)

for n in range(SAMPLE_SIZE**2):
    print(n)
    f = Comp(x[n], y[n])

    """ q = f.mul(b)

    r = q.add(a) """
    x[n] = f.a
    y[n] = f.b
    

a1 = Comp(2,3)
b1 = Comp(4,-2)

for n in range(SAMPLE_SIZE**2):
    print(n)
    f = Comp(x1[n], y1[n])

    q = f.mul(b1)
    r = q.add(a1)

    x1[n] = q.a
    y1[n] = q.b


a2 = Comp(4,-3)
b2 = Comp(5,-1)

for n in range(SAMPLE_SIZE**2):
    print(n)
    f = Comp(x2[n], y2[n])

    q = f.mul(b2)
    r = q.add(a2)

    x2[n] = q.a
    y2[n] = q.b


a3 = Comp(0,0)
b3 = Comp(1,1)

for n in range(SAMPLE_SIZE**2):
    print(n)
    f = Comp(x3[n], y3[n])

    q = f.mul(b3)
    r = q.add(a3)

    x3[n] = q.a
    y3[n] = q.b
    
""" print(y)
print(x) """
ax[0][0].scatter(x, y)
ax[1][0].scatter(x1, y1)
ax[0][1].scatter(x2, y2)
ax[1][1].scatter(x3, y3)
plt.show()