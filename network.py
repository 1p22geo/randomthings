from node import Node
import matplotlib.pyplot as plt
import numpy as np
import copy
import gradient2 as graient
from random import randint, choice, random, sample, uniform

class Network:
    def __init__(self):
        self.layers = [[]]
        self.layers[0] = [Node()]
        self.layers.append([Node([uniform(2, -2)]), Node([uniform(2, -2)]), Node([uniform(2, -2)]), Node([uniform(2, -2)])])
        self.layers.append([Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)])])
        #self.layers.append([Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)])])
        #self.layers.append([Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)])])
        #self.layers.append([Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)])])
        #self.layers.append([Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)])])
        #self.layers.append([Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)]), Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)])])
        
        self.layers.append([Node([uniform(2, -2), uniform(2, -2), uniform(2, -2), uniform(2, -2)])])

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
            node.b += choice([0,-0.2, 0.2, -0.05, 0.05, 1, -1])
        else:
            node.w[e] += choice([0, 0.1, -0.1, 0.3, -0.3, 0.7, -0.7])

np.random.seed(19680801)

SAMPLE_SIZE = 500

fig, ax = plt.subplots(2, 2)
best = Network()
changes = 0
count = 0
changeList = [0]
while True:
    count +=1
    a = graient.GraientDescent(best, SAMPLE_SIZE)
    if a :
        changeList.append(count)

    if count-changeList[-1] >= 10000:
        break

    """ nets = [best]


    for m in range(200):
        a =best.copy()
        a.randomize()
        nets.append(a)

    dots = np.linspace(-10, 10, 1000)
    #dots = np.array(dots)
    result_a = dots**3+2*dots**2-10*dots
    result_b = 2*dots**3+3*dots**2-10*dots

    diffs = []

    for net in nets:

        evaled = net.evaluate([dots])
        diff = 0

        for n in range(SAMPLE_SIZE):
            diff += abs(evaled[0][n]-result_a[n])
            diff += abs(evaled[1][n]-result_b[n])
        diffs.append(diff)
        print(diff)
    print("----------------------\n\n")

    index = np.argmin(diffs)

    best = nets[index] """

dots = np.linspace(-10, 10, SAMPLE_SIZE)
result_a = -np.exp(dots)
#result_b = 2*dots**3+3*dots**2-10*dots

evaled = best.evaluate([dots])

ax[0][0].plot(dots, evaled[0])
#ax[1][0].plot(dots, evaled[1])
ax[0][1].plot(dots, result_a)
#ax[1][1].plot(dots, result_b)


plt.show()