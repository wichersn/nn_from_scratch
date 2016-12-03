import math

class Neuron:
    def __init__(self, input_neurons, learning_rate):
        self.weights = []
        self.learning_rate = learning_rate
        self.input_neurons = input_neurons

        for i in range(len(self.input_neurons) + 1):
            self.weights.append(0)

        self.pre_predict = None

    @staticmethod
    def sigmoid(x):
        return 1/(1 + math.exp(-x))

    def predict(self):
        if not self.pre_predict:
            x = self.get_input_values()

            if len(x) != len(self.weights):
                return

            y = 0
            for i in range(len(self.weights)):
                y += x[i] * self.weights[i]

            self.pre_predict = Neuron.sigmoid(y)

        return self.pre_predict

    def get_input_values(self):
        x = []
        for neuron in self.input_neurons:
            x.append(neuron.predict())
        x = x + [1]
        return x

    def update_w(self, error, gradients):
        gradient = self.calc_gradient(error, gradients)
        x = self.get_input_values()

        for i in range(len(self.weights)):
            update = -gradient * x[i] * self.learning_rate
            self.weights[i] += update

    def calc_gradient(self, error, pre_gradients):
        y = self.predict()
        ave_pre_gradient = sum(pre_gradients) / float(len(pre_gradients))
        return error * (y * (1- y)) * ave_pre_gradient

    def get_gradient_w(self, error, pre_gradients, index):
        return self.calc_gradient(error, pre_gradients) * self.weights[index]

    def clear_pre_predict(self):
        self.pre_predict = None


class ConstNode:
    def __init__(self):
        self.value = 0

    def predict(self):
        return self.value

    def clear_pre_predict(self):
        pass


def set_input_layer(input_layer, values):
    for i in range(len(input_layer)):
        input_layer[i].value = values[i]

