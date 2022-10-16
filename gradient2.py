from random import choice, randint
import numpy as np
def GraientDescent(best, SAMPLE_SIZE, y_hat, y, x):
    db = (np.sum(y_hat-y)*2)/len(y)
    dw = (np.dot((y_hat-y), x)*2)/len(y)