import random
import simple_logistic_neuron

def get_accuracy(test_data):
    num_right = 0
    for example in test_data:
        x = example[:-1]
        y_ = example[-1]

        y = neuron.predict(x)
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

neuron = simple_logistic_neuron.LogisticNeuron(len(train_data[0]) - 1, .1)

start = 0
print_num = 1000
for i in range(10000):
    example = train_data[start]

    x = example[:-1]
    y_ = example[-1]

    y = neuron.predict(x)
    neuron.update_w(x, y_)

    if i % print_num == 0:
        print("error", y - y_, "x", x, "y_", y_, "y:", y, "w", neuron.weights)
        print(get_accuracy(test_data))

    start += 1
    if start >= len(train_data):
        start = 0

print(get_accuracy(test_data))
