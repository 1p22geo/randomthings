from node import Node
import matplotlib.pyplot as plt
import numpy as np
import copy
from random import randint, choice, random, sample

class Network:
    def __init__(self):
        self.layers = [[]]
        self.layers[0] = [Node()]
        self.layers.append([Node([random()]), Node([random()]), Node([random()]), Node([random()])])
        self.layers.append([Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]),Node([random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]),Node([random(), random(), random(), random(), random()])])
        """ self.layers.append([Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]),Node([random(), random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]),Node([random(), random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]),Node([random(), random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]),Node([random(), random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]),Node([random(), random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]),Node([random(), random(), random(), random(), random()])])
        """
        self.layers.append([Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()]), Node([random(), random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()])])
        """ self.layers.append([Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()])])
         """
        self.layers.append([Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()])])
        self.layers.append([Node([random(), random(), random()]), Node([random(), random(), random()]), Node([random(), random(), random()]), Node([random(), random(), random()])])
        self.layers.append([Node([random(), random(), random(), random()]), Node([random(), random(), random(), random()])])

    def copy(self):

        return copy.deepcopy(self)


    def evaluate(self, values):
        for n in range(len(values)):
            self.layers[0][n].manual(values[n])
        for n in range(len(self.layers)-1):
            for node in self.layers[n+1]:
                node.evaluate(self.layers[n])

        x = []
        for node in self.layers[-1]:
            x.append(node.x)
        
        return x

    def randomize(self):
        layer = choice(self.layers)
        node = choice(layer)
        e = randint(-1, len(node.w)-1)
        if e == -1:
            node.b += choice([0,-0.2, 0.2, -0.5, 0.5, 1, -1])
        else:
            node.w[e] += choice([0, 0.1, -0.1, 0.3, -0.3, 0.5, -0.5, 1, -1])

np.random.seed(19680801)

SAMPLE_SIZE = 1000

fig, ax = plt.subplots(2, 2)
best = Network()
nets = [best]
for p in range(100):
    

    bnets = copy.deepcopy(nets)
    for g in bnets:
        for m in range(50):
            a =best.copy()
            a.randomize()
            nets.append(a)

    #dots = sample(list(np.linspace(-50, 50, 1000)), SAMPLE_SIZE)
    #dots = np.array(dots)
    dots = np.linspace(-10, 10, SAMPLE_SIZE)
    result_a = 10000*dots**2
    result_b = 20000*dots+3

    diffs = {}

    for net in nets:

        evaled = net.evaluate([dots])
        diff = 0

        for n in range(SAMPLE_SIZE):
            diff += abs(evaled[0][n]-result_a[n])
            diff += abs(evaled[1][n]-result_b[n])
        diffs[diff] = net
        print(diff)

    min = 10000
    index = -1

    v = list(diffs.keys())
    v.sort()
    nets = []
    for o in range(5):
        nets.append(diffs[v[o]])

    """ for n in range(len(diffs)):
        if diffs[n] < min:
            min = diffs[n]
            index = n """

    #best = nets[index]

dots = np.linspace(-10, 10, SAMPLE_SIZE)
result_a = 1000*dots**2
result_b = 2000*dots+3

evaled = best.evaluate([dots])

ax[0][0].plot(dots, evaled[0])
ax[1][0].plot(dots, evaled[1])
ax[0][1].plot(dots, result_a)
ax[1][1].plot(dots, result_b)


plt.show()