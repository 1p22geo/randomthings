import numpy as np

input_value = np.array([[0,0],[0,1],[1,1],[1,0]])
input_value.shape
output = np.array([0,1,1,0])
output = output.reshape(4,1)
weights = np.array([[0.1], [0.2]])
bias = 0.3
def sigmoid(x):
    return 1/(1+np.exp(-x))

def der(x):
    return sigmoid(x)*(1-sigmoid(x))

for epochs in range(100000):
    input_arr = input_value

    weighted_sum = np.dot(input_arr, weights) + bias
    first_output = sigmoid(weighted_sum)

    error = first_output - output
    total_error = np.square(np.subtract(first_output, output)).mean()

    first_der = error
    second_der = der(first_output)
    derivative = first_der * second_der

    t_input = input_value.T
    final_derivative = np.dot(t_input, derivative)


    weights = weights - 0.05 * final_derivative

    for i in derivative:
        bias = bias - 0.05 * i

print(weights)
print(bias)

pred = np.array([1,0])
result = np.dot(pred, weights) +bias
res = sigmoid(result)
print(res)