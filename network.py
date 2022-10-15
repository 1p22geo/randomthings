from node import Node
import matplotlib.pyplot as plt
import numpy as np

class Network:
    def __init__(self):
        self.layer0 = [Node()]
        self.layer1 = [Node([0.5]), Node([0.5])]
        self.layer2 = [Node([0.5, 0.5]), Node([0.5, 0.5])]
        self.layer3 = [Node([0.5]), Node([0.5])]

    def evaluate(self, values):
        for n in range(len(values)):
            self.layer0[n].manual(values[n])
        for node in self.layer1:
            node.evaluate(self.layer0)
        for node in self.layer2:
            node.evaluate(self.layer1)
        for node in self.layer3:
            node.evaluate(self.layer2)

        x = []
        for node in self.layer3:
            x.append(node.x)
        
        return x