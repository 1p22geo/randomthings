from random import choice, randint
import numpy as np
mu = 0.0005
def GraientDescent(best, SAMPLE_SIZE):
    print("=========================")
    f = choice([1, -1])
    dots = np.linspace(-10, 10, 1000)
    #dots = np.array(dots)
    result_a = (3*dots**2-10*dots)*(0.001)

    #evaled = best.evaluate([dots])
    
    diff = 0
    
    for n in range(SAMPLE_SIZE):
        evaled = best.evaluate([dots[n]])
        diff += abs(evaled[0]-result_a[n])**2
    diff /= SAMPLE_SIZE
    print(diff)
    layer = choice(best.layers[1:])
    node = choice(layer)
    e = randint(-1,len(node.w)-1)
    if e == -1:
        node.b += mu*f
    else:
        node.w[e] += mu*f
    
    #new_evaled = best.evaluate([dots])
    new_diff = 0
    
    for n in range(SAMPLE_SIZE):
        evaled = best.evaluate([dots[n]])
        new_diff += abs(evaled[0]-result_a[n])**2
    new_diff /= SAMPLE_SIZE
    print(new_diff)
    if new_diff >= diff:
        print(3)
        if e == -1:
            node.b -= mu*f
        else:
            node.w[e] -= mu*f
        return best
    else:
        diffs = [10000000]
        while True:
            if e == -1:
                node.b += mu*f
            else:
                node.w[e] += mu*f
    
            #new_evaled = best.evaluate([dots])
            new_diff = 0
            print(node.w[e])
            for n in range(SAMPLE_SIZE):
                evaled = best.evaluate([dots[n]])
                new_diff += abs(evaled[0]-result_a[n])**2
            new_diff /= SAMPLE_SIZE
            diffs.append(new_diff)
            print("A ", new_diff)
            if e == -1:
                node.b += mu*f
            else:
                node.w[e] += mu*f
            print(" -> ", new_diff)
            return best