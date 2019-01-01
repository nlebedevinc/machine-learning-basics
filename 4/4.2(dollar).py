import numpy


# activation function
def nonlin(x, deriv=False):
    return x * (1 - x) if deriv else 1 / (1 + numpy.exp(-x))


# there is a file "dollar.txt" in the working directory, containing time data
with open("dollar.txt", 'r') as txt:
    data = [float(i) for i in txt.readlines()]
p = 4
x = data[:-p]
for i in range(1, p):
    x = numpy.vstack([x, data[i:-p + i]])
y = numpy.array([data[-p:]])

# normalizing
x_norm = (x - numpy.min(x)) / (numpy.max(x) - numpy.min(x))
y_norm = (y - numpy.min(y)) / (numpy.max(y) - numpy.min(y))


synapse0 = 2 * numpy.random.random((9, 18)) - 1
synapse1 = 2 * numpy.random.random((18, 1)) - 1

epochs = 250
batch = 500

for i in range(epochs):
    for j in range(0, x.shape[0], batch):
        l0 = x_norm
        l1 = nonlin(numpy.dot(l0, synapse0))
        l2 = nonlin(numpy.dot(l1, synapse1))

        l2_error = y_norm.T - l2

        l2_delta = l2_error * nonlin(l2, deriv=True)
        l1_error = numpy.dot(l2_delta, synapse1.T)
        l1_delta = l1_error * nonlin(l1, deriv=True)
        synapse1 += numpy.dot(l1.T, l2_delta)
        synapse0 += numpy.dot(l0.T, l1_delta)
    if (i % (epochs // 5)) == 0:
        print("Epoch %d: error=" % i + str(numpy.mean(numpy.abs(l2_error))))

l0 = data[p:]
l0_norm = (l0 - numpy.min(x)) / (numpy.max(x) - numpy.min(x))
l1 = nonlin(numpy.dot(l0_norm, synapse0))
l2_norm = nonlin(numpy.dot(l1, synapse1))
l2 = l2_norm * (numpy.max(y) - numpy.min(y)) + numpy.min(y)

print(l2)