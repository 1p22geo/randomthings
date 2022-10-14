import matplotlib.pyplot as plt
import numpy as np
from things import Complex as Comp
np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0, 1, 5)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()

a = Comp(2,3)
b = Comp(4,-2)

for x0 in range(len(x)):
    for y0 in range(len(y)):
        f = Comp(x[x0], y[y0])
        q = f.mul(b)
        r = q.add(a)
        x[x0] = r.a
        y[y0] = r.b
    
print(y)
print(x)
ax.scatter(x, y)
plt.show()