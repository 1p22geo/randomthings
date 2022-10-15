from node import Node
import matplotlib.pyplot as plt
import numpy as np
import copy
from random import randint, choice, random, sample, uniform

class Network:
    def __init__(self):
        self.layers = [[]]
        self.layers[0] = [Node()]
        self.layers.append([Node([uniform(0,0.5)]), Node([uniform(0,0.5)]), Node([uniform(0,0.5)]), Node([uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]),Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]),Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]),Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]),Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]),Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]),Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]),Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]),Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
       
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])
        self.layers.append([Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)]), Node([uniform(0,0.5), uniform(0,0.5), uniform(0,0.5), uniform(0,0.5)])])

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
            pass
            node.b += choice([0,-0.2, 0.2, -0.5, 0.5, 1, -1])
        else:
            node.w[e] += choice([0, 0.1, -0.1, 0.03, -0.03, 0.05, -0.05])

np.random.seed(19680801)

SAMPLE_SIZE = 1000

fig, ax = plt.subplots(2, 2)
best = Network()
nets = [best]
for p in range(20):
    

    bnets = copy.deepcopy(nets)
    for g in bnets:
        for m in range(200):
            a =best.copy()
            a.randomize()
            nets.append(a)

    #dots = sample(list(np.linspace(-50, 50, 1000)), SAMPLE_SIZE)
    #dots = np.array(dots)
    dots = np.linspace(-10, 10, SAMPLE_SIZE)
    result_a = np.log10(abs(dots))
    result_b = np.exp(dots)
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
    best = diffs[v[0]]
    for o in range(3):
        nets.append(diffs[v[o]])

    """ for n in range(len(diffs)):
        if diffs[n] < min:
            min = diffs[n]
            index = n """

    #best = nets[index]

dots = np.linspace(-10, 10, SAMPLE_SIZE)
result_a = np.log10(abs(dots))
result_b = np.exp(dots)

evaled = best.evaluate([dots])

ax[0][0].plot(dots, evaled[0])
ax[1][0].plot(dots, evaled[1])
ax[0][1].plot(dots, result_a)
ax[1][1].plot(dots, result_b)


plt.show()