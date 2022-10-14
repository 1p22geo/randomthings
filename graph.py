import matplotlib.pyplot as plt
import numpy as np
from things import Complex as Comp
np.random.seed(19680801)

SAMPLE_SIZE = 10

fig, ax = plt.subplots(2)
dots = np.linspace(0, 1, SAMPLE_SIZE)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()
x1, y1 = x, y
x2, y2 = x, y
x3, y3 = x, y

a = Comp(2,3)
b = Comp(4,-2)

for n in range(SAMPLE_SIZE**2):
    print(n)
    f = Comp(x[n], y[n])

    q = f.mul(b)

    r = q.add(a)
    x[n] = r.a
    y[n] = r.b

a1 = Comp(2,3)
b1 = Comp(4,-2)

for n in range(SAMPLE_SIZE**2):
    print(n)
    f = Comp(x1[n], y1[n])

    """     q = f.mul(b1)
    r = q.add(a1) """

    x1[n] = r.a
    y1[n] = r.b
    
""" print(y)
print(x) """
ax[0].scatter(x, y)
ax[1].scatter(x1, y1)
plt.show()