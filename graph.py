import matplotlib.pyplot as plt
import numpy as np
import things
np.random.seed(19680801)

fig, ax = plt.subplots()
dots = np.linspace(0.3, 1.2, 10)
X, Y = np.meshgrid(dots, dots)
x, y = X.ravel(), Y.ravel()

for x0 in range(len(x)):
    for y0 in range(len(y)):
        pass
    
print(y)
print(x)
ax.scatter(x, y)
plt.show()