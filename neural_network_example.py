import neural_network
import random


def get_accuracy(test_data):
    num_right = 0
    for example in test_data:
        x = example[:-1]
        y_ = example[-1]

        neural_network.set_input_layer(input_layer, x)
        y = output_neuron.predict()

        neural_network.clear_pre_vals(all_neurons)

        pred = int(y > .5)

        if y_ == pred:
            num_right += 1

    return num_right / float(len(test_data))

data = []
data_size = 10000
for i in range(data_size):
    x1 = (random.random() * 20) - 10
    x2 = (random.random() * 20) - 10
    y_ = int((x1 * x2) > 0)
    data.append([x1, x2, y_])

train_percent = .9
train_amount = int(len(data) * train_percent)
train_data = data[:train_amount]
test_data = data[train_amount:]

input_layer = [neural_network.ConstNode() for i in range(len(train_data[0])-1)]

layer, all_neurons = neural_network.create_fully_connected(input_layer, [3, 2], .1)

output_neuron = neural_network.Neuron(layer, .1)
output_sigmoid = neural_network.SigmoidNode(output_neuron)

all_neurons.append(output_neuron)

start = 0
print_num = 100000

for i in range(1000000):
    example = train_data[start]

    x = example[:-1]
    y_ = example[-1]

    neural_network.set_input_layer(input_layer, x)
    y = output_sigmoid.predict()
    error = y - y_

    output_sigmoid.get_all_gradient()
    output_sigmoid.update_w_all(error)

    neural_network.clear_pre_vals(all_neurons)

    if i % print_num == 0:
        print("error", y - y_, "x", x, "y_", y_, "y:", y)
        print(get_accuracy(test_data))

    start += 1
    if start >= len(train_data):
        start = 0

print(get_accuracy(test_data))
