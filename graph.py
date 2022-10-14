import matplotlib.pyplot as plt
import numpy as np
from things import Complex as Comp
np.random.seed(19680801)

SAMPLE_SIZE = 10

fig, ax = plt.subplots()
dots = np.linspace(0, 1, SAMPLE_SIZE)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()

a = Comp(2,3)
b = Comp(4,-2)

for n in range(SAMPLE_SIZE**2):
    print(n)
    f = Comp(x[n], y[n])

    q = f.mul(b)

    r = q.add(a)
    x[n] = r.a
    y[n] = r.b
    
""" print(y)
print(x) """
ax.scatter(x, y)
plt.show()