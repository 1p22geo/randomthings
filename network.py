from node import Node
import matplotlib.pyplot as plt
import numpy as np
from random import randint, choice

class Network:
    def __init__(self):
        self.layers = [[], [], [], [], [], []]
        self.layers[0] = [Node()]
        self.layers[1] = [Node([0.2]), Node([0.01], -0.1), Node([0.03], -0.93), Node([0.03], -0.93)]
        self.layers[2] = [Node([-0.02, 0.05, 0.03, 0.03]), Node([0.03, 0.8, 0.03, 0.03], -0.93), Node([0.03, 0.8, 0.03, 0.03], -0.93), Node([0.03, 0.8, 0.03, 0.03], -0.93)]
        self.layers[3] = [Node([0.95, 0.12, 0.03, 0.03],-0.4), Node([0.01, 0.05, 0.03, 0.03]), Node([0.01, 0.05, 0.03, 0.03])]
        self.layers[4] = [Node([0.95, 0.12, 0.03],-0.4), Node([0.01, 0.05, 0.03]), Node([0.01, 0.05, 0.03]), Node([0.01, 0.05, 0.03])]#TODO: Make those numbers random
        self.layers[5] = [Node([0.95, 0.12, 0.03, 0.03],-0.4), Node([0.01, 0.05, 0.03, 0.03])]

    def copy(self):
        a = Network()
        a.layers = self.layers

    def evaluate(self, values):
        for n in range(len(values)):
            self.layers[0][n].manual(values[n])
        for node in self.layers[1]:
            node.evaluate(self.layers[0])
        for node in self.layers[2]:
            node.evaluate(self.layers[1])
        for node in self.layers[3]:
            node.evaluate(self.layers[2])
        for node in self.layers[4]:
            node.evaluate(self.layers[3])
        for node in self.layers[5]:
            node.evaluate(self.layers[4])

        x = []
        for node in self.layers[5]:
            x.append(node.x)
        
        return x

    def randomize(self):
        layer = choice(self.layers)
        node = choice(layer)
        e = randint(-1, len(node.w)-1)
        if e == -1:
            node.b += choice([0,-0.2, 0.2, -0.05, 0.05])
        else:
            print(e)
            node.w[e] += choice([0, 0.1, -0.1, 0.3, -0.3])



net = Network()

for n in range(10000):
    net.randomize()

np.random.seed(19680801)

SAMPLE_SIZE = 50

fig, ax = plt.subplots(2)
dots = np.linspace(-10, 10, SAMPLE_SIZE)

evaled = net.evaluate([dots])
a, b = [], []
for pair in evaled:
    a.append(pair[0])
    b.append(pair[0])

ax[0].plot(dots, evaled[0])
ax[1].plot(dots, evaled[1])

plt.show()