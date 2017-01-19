import random
import simple_linear_neuron

train_data = []
train_size = 20
for i in range(train_size):
    x1 = random.randint(0, 10)
    x2 = random.randint(0, 10)
    x3 = random.randint(0, 10)
    y_ = x1 * 2 + x2 * -1 + x3 * -3 + 1
    train_data.append([x1, x2, x3, y_])

neuron = simple_linear_neuron.LinearNeuron(len(train_data[0]) - 1, .001)

for epoch in range(1000):
    for example in train_data:
        x = example[:-1]
        y_ = example[-1]

        y = neuron.predict(x)
        neuron.update_w(x, y_)

    print("error", y - y_, "x", x, "y_", y_, "y:", y, "w", neuron.weights)
