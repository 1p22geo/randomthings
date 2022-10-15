from node import Node
import matplotlib.pyplot as plt
import numpy as np
import copy
from random import randint, choice, random, sample

class Network:
    def __init__(self):
        self.layers = [[], [], [], [], [], []]
        self.layers[0] = [Node()]
        self.layers[1] = [Node([random()]), Node([random()]), Node([random()]), Node([random()])]
        self.layers[2] = [Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()])]
        self.layers[3] = [Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()])]
        self.layers[4] = [Node([random(), random(), random()]), Node([random(), random(), random()]), Node([random(), random(), random()]), Node([random(), random(), random()])]#TODO: Make those numbers random
        self.layers[5] = [Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()])]

    def copy(self):

        return copy.deepcopy(self)


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
            node.w[e] += choice([0, 0.1, -0.1, 0.3, -0.3])



nets = [Network()]
best = nets[0]


np.random.seed(19680801)

SAMPLE_SIZE = 50

fig, ax = plt.subplots(2, 2)
dots = np.linspace(-10, 10, SAMPLE_SIZE)
result_a = np.sin(dots)
result_b = np.cos(dots)

evaled = nets[0].evaluate([dots])
diff = 0

for n in range(SAMPLE_SIZE):
    diff += abs(evaled[0][n]-result_a[n])
    diff += abs(evaled[1][n]-result_b[n])

print(diff)

ax[0][0].plot(dots, evaled[0])
ax[1][0].plot(dots, evaled[1])
ax[0][1].plot(dots, result_a)
ax[1][1].plot(dots, result_b)


plt.show()