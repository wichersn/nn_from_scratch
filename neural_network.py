import math

class Node:
    def get_average_out_gradient(self):
        ave_out_gradient = 1
        if len(self.output_nodes) > 0:
            out_gradients = [self.output_nodes[i].get_gradient_w(i) for i in range(len(self.output_nodes))]
            ave_out_gradient = sum(out_gradients) / float(len(out_gradients))

        return ave_out_gradient

    def clear_pre_vals(self):
        pass

    def update_w(self, error):
        pass

    def get_all_gradient(self):
        for i in range(len(self.input_nodes)):
            self.get_gradient_w(i)
            self.input_nodes[i].get_all_gradient()

    def update_w_all(self, error):
        self.update_w(error)

        for input_node in self.input_nodes:
            input_node.update_w_all(error)

class Neuron(Node):
    def __init__(self, input_nodes, learning_rate):
        self.weights = []
        self.learning_rate = learning_rate
        self.input_nodes = input_nodes
        self.output_nodes = []
        self.pre_gradient = []

        for i in range(len(self.input_nodes)):
            self.weights.append(0)
            self.input_nodes[i].output_nodes.append(self)
            self.pre_gradient.append(None)

        self.weights.append(0)

        self.pre_predict = None

    def predict(self):
        if not self.pre_predict:
            x = self.get_input_values()

            if len(x) != len(self.weights):
                return

            y = 0
            for i in range(len(self.weights)):
                y += x[i] * self.weights[i]

            self.pre_predict = y

        return self.pre_predict

    def get_input_values(self):
        x = []
        for node in self.input_nodes:
            x.append(node.predict())
        x = x + [1]
        return x

    def update_w(self, error):
        gradient = self.get_average_out_gradient()
        x = self.get_input_values()

        for i in range(len(self.weights)):
            update = -gradient * error * x[i] * self.learning_rate
            self.weights[i] += update

    def get_gradient_w(self, index):
        if self.pre_gradient[index] == None:
            self.pre_gradient[index] = self.get_average_out_gradient() * self.weights[index]

        return self.pre_gradient[index]

    def clear_pre_vals(self):
        self.pre_predict = None
        self.pre_gradient = [None for i in range(len(self.input_nodes))]


class SigmoidNode(Node):
    def __init__(self, input_node):
        self.input_nodes = [input_node]
        self.output_nodes = []
        input_node.output_nodes.append(self)

    @staticmethod
    def sigmoid(x):
        return 1/(1 + math.exp(-x))

    def predict(self):
        return SigmoidNode.sigmoid(self.input_nodes[0].predict())

    def get_gradient_w(self, i):
        y = self.predict()

        return self.get_average_out_gradient() * (y * (1- y))


class ConstNode(Node):
    def __init__(self):
        self.value = 0
        self.output_nodes = []
        self.input_nodes = []

    def predict(self):
        return self.value


def clear_pre_vals(nodes):
    for node in nodes:
        node.clear_pre_vals()

def set_input_layer(input_layer, values):
    for i in range(len(input_layer)):
        input_layer[i].value = values[i]

def optimzer(root_node, y_):
    nodes = [root_node]
    
    while len(nodes) > 0:
        for node in nodes:
            new_nodes.extend()

