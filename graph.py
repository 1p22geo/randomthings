import matplotlib.pyplot as plt
import numpy as np
from things import Complex as Comp
np.random.seed(19680801)

SAMPLE_SIZE = 9

fig, ax = plt.subplots(2, 2)
dots = np.linspace(-1, 1, SAMPLE_SIZE)
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
    

a1 = Comp(int(input("Real part of a  ")),int(input("Imaginary part of a  ")))
b1 = Comp(int(input("Real part of b  ")),int(input("Imaginary part of b  ")))
c1 = Comp(int(input("Real part of c  ")),int(input("Imaginary part of c  ")))
d1 = Comp(int(input("Real part of d  ")),int(input("Imaginary part of d  ")))

""" a1 = Comp(0,0)
b1 = Comp(1,0)
c1 = Comp(0,0)
d1 = Comp(0,0) """

for n in range(SAMPLE_SIZE**2):
    f = Comp(float(x1[n]), float(y1[n]))
    """ print(f)
    print(f.power(2)) """

    q = f.mul(b1)
    r = a1
    p = f.power(2).mul(c1)
    p1 = f.power(3).mul(d1)
    out = q.add(r).add(p).add(p1)

    """ print(out) """
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
v = int(input("Which vertice to paint? "))
elems_to_yellow = [37, 38, 39, 41, 42, 43, 36, 44]
elems_to_purple = [40, v]
elems_to_blue = [49, 58, 67, 76, 31, 22, 13, 4]
z = np.linspace(10, 10, SAMPLE_SIZE**2)
print(len(z))
for n in range(len(z)):
    if n in elems_to_yellow:
        z[n] = 20

for n in range(len(z)):
    if n in elems_to_purple:
        z[n] = 50

for n in range(len(z)):
    if n in elems_to_blue:
        z[n] = 30
print(z)

ax[0][0].scatter(x, y, s=z, c=z)
ax[1][0].scatter(x1, y1, s=z, c=z)
ax[0][1].triplot(x, y)
ax[1][1].triplot(x1,y1)
plt.show()