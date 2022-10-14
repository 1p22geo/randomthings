class Node:
    def __init__(self, weighths=[], offset=0):
        self.x = 0
        self.w = weighths
        self.b = offset

    def evaluate(self, nodes):
        if not len(nodes) == len(self.w):
            return -1
        sum = 0
        for n in range(len(nodes)):
            sum += nodes[n].x + self.w[n]
        self.x = max(0, sum)

    def manual(self, x):
        self.x = x