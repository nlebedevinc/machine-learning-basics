import numpy


def nonlin(x, deriv=False):
    return x * (1 - x) if deriv else 1 / (1 + numpy.exp(-x))


def norm_random(shape_0, shape_1):
    return 2 * numpy.random.random((shape_0, shape_1)) - 1


# my variant
letters = ['С', 'Г', 'А']
codes = ["1111111"
         "1000001"
         "1000000"
         "1000000"
         "1000000"
         "1000000"
         "1000001"
         "1111111",

         "0111111"
         "0100001"
         "0100000"
         "0100000"
         "0100000"
         "0100000"
         "0100000"
         "0100000",

         "0001000"
         "0010100"
         "0010100"
         "0100010"
         "0111110"
         "0100010"
         "1000001"
         "1000001"
         ]
x = []
for code in codes:
    x.append([int(i) for i in code])
x = numpy.array(x)
y = numpy.eye(x.shape[0])

# array of counts of neurons for each hidden layer
# length of this array determines count of hidden layers in the neuronet
# works correctly if not empty
neurons = [10]
synapses = [norm_random(x.shape[1], neurons[0])]
for i in range(len(neurons) - 1):
    synapses.append(norm_random(neurons[i], neurons[i + 1]))
synapses.append(norm_random(neurons[-1], x.shape[0]))

epochs = 10000
# training
for i in range(epochs):
    layers_outputs = []
    layers_outputs.append(x)
    for s in synapses:
        layers_outputs.append(nonlin(numpy.dot(layers_outputs[-1], s)))

    layers_deltas = []
    error = y - layers_outputs[-1]
    # layers_deltas.append(error * nonlin(layers_outputs[-1], deriv=True))
    for j, s in enumerate(synapses[-1::-1]):
        layers_deltas.append(error * nonlin(layers_outputs[-j - 1], deriv=True))
        error = numpy.dot(layers_deltas[-1], s.T)
    for j, s in enumerate(synapses):
        s += numpy.dot(layers_outputs[j].T, layers_deltas[-j - 1])

l_prev = []
for string in [
         "1111111"
         "1000001"
         "1111000"
         "1000000"
         "1111000"
         "1000000"
         "1000001"
         "1111111",

         "0111111"
         "0101001"
         "0101000"
         "0100000"
         "0100100"
         "0100000"
         "0101000"
         "0100000",

         "0001000"
         "0010100"
         "0010100"
         "0100110"
         "0111110"
         "0100010"
         "1000001"
         "1000001"
         ]:
    l_prev.append([int(i) for i in string])
for s in synapses:
    l_next = nonlin(numpy.dot(l_prev, s))
    l_prev = numpy.copy(l_next)
print("Letter C - probability:", layers_outputs[2][0])
for i in range(0, len(layers_outputs[0][0] - 7), 7):
    print(layers_outputs[0][0][i:i+7])
print("Letter Г - probability:", layers_outputs[2][1])
for i in range(0, len(layers_outputs[0][0] - 7), 7):
    print(layers_outputs[0][1][i:i+7])
print("Letter А - probability:", layers_outputs[2][2])
for i in range(0, len(layers_outputs[0][0] - 7), 7):
    print(layers_outputs[0][2][i:i+7])