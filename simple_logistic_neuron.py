import math


class LogisticNeuron:
    def __init__(self, num_weights, learning_rate):
        self.weights = []
        self.learning_rate = learning_rate

        num_weights += 1
        for i in range(num_weights):
            self.weights.append(0)

    @staticmethod
    def sigmoid(x):
        return 1/(1 + math.exp(-x))

    def predict(self, x):
        x = x +[1]
        if len(x) != len(self.weights):
            return

        y = 0
        for i in range(len(self.weights)):
            y += x[i] * self.weights[i]

        return LogisticNeuron.sigmoid(y)

    def update_w(self, x, y_):
        y = self.predict(x)
        if y == None:
            return

        x = x + [1]

        error = y - y_

        for i in range(len(self.weights)):
            update = -error * self.learning_rate * x[i] * (y * (1- y))
            self.weights[i] += update
