import numpy as np

class Node:
    def __init__(self, weighths=[], offset=0.1):
        self.x = 0
        self.w = weighths
        self.b = offset

    def evaluate(self, nodes):
        if not len(nodes) == len(self.w):
            raise ArithmeticError
        sum = 0
        for n in range(len(nodes)):
            sum += nodes[n].x * self.w[n]
        sum -= self.b
        self.x = np.tanh(sum) 

    def manual(self, x):
        self.x = x