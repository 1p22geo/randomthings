from random import choice, randint
import numpy as np
def GraientDescent(best, SAMPLE_SIZE, f = choice([1, -1])):
    print("=========================")
    
    dots = np.linspace(-10, 10, 1000)
    #dots = np.array(dots)
    result_a = -np.exp(dots)
    #result_b = -(2*dots**3+3*dots**2-10*dots)

    evaled = best.evaluate([dots])
    diff = 0
    
    #diff = np.sum((evaled[0]-result_a)**2)/SAMPLE_SIZE

    for n in range(SAMPLE_SIZE):
        diff += abs(evaled[0][n]-result_a[n])**2
        #diff += abs(evaled[1][n]-result_b[n])**2
    diff /= SAMPLE_SIZE
    print(diff)
    layer = choice(best.layers)
    if layer == best.layers[0]:
        return 0
    node = choice(layer)
    e = randint(-1,len(node.w)-1)
    if e == -1:
        node.b += 0.05*f
    else:
        node.w[e] += 0.05*f
    
    new_evaled = best.evaluate([dots])
    new_diff = 0
    
    for n in range(SAMPLE_SIZE):
        new_diff += abs(new_evaled[0][n]-result_a[n])**2
        #new_diff += abs(new_evaled[1][n]-result_b[n])**2
    new_diff /= SAMPLE_SIZE
    print(new_diff)
    if new_diff >= diff or diff-new_diff <0.00005:
        
        if e == -1:
            node.b -= 0.1*f
        else:
            node.w[e] -= 0.1*f
        new_evaled = best.evaluate([dots])
        new_diff = 0
        
        for n in range(SAMPLE_SIZE):
            new_diff += abs(new_evaled[0][n]-result_a[n])**2
            #new_diff += abs(new_evaled[1][n]-result_b[n])**2
        new_diff /= SAMPLE_SIZE
        print(new_diff)
        if new_diff >= diff or diff-new_diff <0.00005:
            if e == -1:
                node.b += 0.05*f
            else:
                node.w[e] += 0.05*f
            print(3)
            return 0
        else:
            f = -f
    diffs = [10000000]
    while True:
        if e == -1:
            node.b += 0.05*f
        else:
            node.w[e] += 0.05*f

        new_evaled = best.evaluate([dots])
        new_diff = 0
        print(node.w[e])
        for n in range(SAMPLE_SIZE):
            new_diff += abs(new_evaled[0][n]-result_a[n])**2
            #new_diff += abs(new_evaled[1][n]-result_b[n])**2
        new_diff /= SAMPLE_SIZE
        diffs.append(new_diff)
        print("A ", new_diff)
        if int(new_diff) >= int(diffs[-2]) or diffs[-2]-new_diff<0.00002:
            
            if e == -1:
                node.b += 0.05*f
            else:
                node.w[e] += 0.05*f
            print(" -> ", new_diff)
            return 1