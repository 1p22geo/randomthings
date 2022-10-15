import matplotlib.pyplot as plt
import numpy as np
from things import Complex as Comp
np.random.seed(19680801)

SAMPLE_SIZE = 10

fig, ax = plt.subplots(2)
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
    f = Comp(x[n], y[n])

    """ q = f.mul(b)

    r = q.add(a) """
    x[n] = f.a
    y[n] = f.b
    

a1 = Comp(int(input("give value  ")),int(input("give value  ")))
b1 = Comp(int(input("give value  ")),int(input("give value  ")))
c1 = Comp(int(input("give value  ")),int(input("give value  ")))

for n in range(SAMPLE_SIZE**2):
    f = Comp(float(x1[n]), float(y1[n]))
    print(f)
    print(f.power(2))

    q = f.mul(b1)
    r = a1
    p = f.power(2).mul(c1)
    out = q.add(r).add(p)

    print(out)
    x1[n] = out.a
    y1[n] = out.b


""" a2 = Comp(4,-3)
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
    f = Comp(x3[n], y3[n])

    q = f.mul(b3)
    r = q.add(a3)

    x3[n] = q.a
    y3[n] = q.b """
    
""" print(y)
print(x) """
ax[0].scatter(x, y)
ax[1].scatter(x1, y1)
plt.show()