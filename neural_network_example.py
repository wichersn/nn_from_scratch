import neural_network
import random


def get_accuracy(test_data):
    num_right = 0
    for example in test_data:
        x = example[:-1]
        y_ = example[-1]

        neural_network.set_input_layer(input_layer, x)
        y = neuron2.predict()

        neural_network.clear_pre_vals([neuron1, neuron2])

        pred = int(y > .5)

        if y_ == pred:
            num_right += 1

    return num_right / float(len(test_data))

data = []
train_size = 500
for i in range(train_size):
    x1 = random.randint(0, 10)
    x2 = random.randint(0, 10)
    x3 = random.randint(-5, 5)
    y_ = int((x1*-1 + x2*3 + x3 * -9 - 5) > 0)
    data.append([x1, x2, x3, y_])

train_percent = .6
train_amount = int(len(data) * train_percent)
train_data = data[:train_amount]
test_data = data[train_amount:]

input_layer = [neural_network.ConstNode() for i in range(len(train_data[0])-1)]

neuron1 = neural_network.Neuron(input_layer, .1)
sigmoid1 = neural_network.SigmoidNode(neuron1)
neuron2 = neural_network.Neuron([sigmoid1], .1)
sigmoid2 = neural_network.SigmoidNode(neuron2)

start = 0
print_num = 10000

neuron2.weights = [1,0]
for i in range(100000):
    example = train_data[start]

    x = example[:-1]
    y_ = example[-1]

    neural_network.set_input_layer(input_layer, x)
    y = neuron2.predict()
    error = y - y_

    neuron2.get_all_gradient()
    neuron2.update_w_all(error)

    neural_network.clear_pre_vals([neuron1, neuron2])

    if i % print_num == 0:
        print("error", y - y_, "x", x, "y_", y_, "y:", y, "w", neuron1.weights, neuron2.weights)
        print(get_accuracy(test_data))

    start += 1
    if start >= len(train_data):
        start = 0

print(get_accuracy(test_data))
