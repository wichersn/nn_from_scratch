import random

class Neuron:
    def __init__(self, num_weights, learning_rate):
        self.weights = []
        self.learning_rate = learning_rate

        num_weights += 1
        for i in range(num_weights):
            self.weights.append(0)

    def predict(self, x):
        x = x +[1]
        if len(x) != len(self.weights):
            return

        y = 0
        for i in range(len(self.weights)):
            y += x[i] * self.weights[i]
        return y

    def update_w(self, x, y_):
        y = self.predict(x)
        if y == None:
            return

        x = x + [1]

        error = y - y_

        for i in range(len(self.weights)):
            update = -error * self.learning_rate * x[i]
            self.weights[i] += update


train_data = []
train_size = 20
for i in range(train_size):
    x1 = random.randint(0, 10)
    x2 = random.randint(0, 10)
    x3 = random.randint(0, 10)
    y_ = x1 * 2 + x2 * -1 + x3 * -3 + 1
    train_data.append([x1, x2, x3, y_])

neuron = Neuron(len(train_data[0])-1, .001)

for epoch in range(100):
    for example in train_data:
        x = example[:-1]
        y_ = example[-1]

        y = neuron.predict(x)
        neuron.update_w(x, y_)

        print("error", y - y_, "x", x, "y_", y_, "y:", y, "w", neuron.weights)