# nn_from_scratch
Implements a simple neural network without using neural network libraries.

I tried to derive the math for gradient descent and backprop myself. I got stuck a few times and got unstuck by watching Geoffrey Hinton’s course here: https://www.youtube.com/watch?v=cbeTc-Urqak&list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9

This repo contains neural network implementations at different levels of complexity. Gradient descent is used for optimization.

The simplest is a linear neuron implemented in simple_linear_neuron.py, with a usage example in simple_linear_neuron_example.py. This neuron can only create a single layer neural network.

Next, there is a logistic neuron implemented in simple_logistic_neuron.py an example in simple_logistic_neuron_example.py. This is the same as the linear neuron only with a sigmoid activation added on top. This is used on a simple Kaggle competition in simple_logistic_kaggle_example.py This neuron can also only be used in a single layer network.

Neural_network.py implements a neuron with backprop and sigmoid activations which can be used in a multilayer neural network. It is used in neural_network_example.py to solve a similar problem to http://playground.tensorflow.org/#activation=sigmoid&batchSize=10&dataset=xor&regDataset=reg-plane&learningRate=0.1&regularizationRate=0&noise=0&networkShape=3,2&seed=0.32502&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false with a similar network.
My network is mainly hit or miss on this problem, it either gets over 90% accuracy, or it does as well as guessing. I think this is due to gradient descent getting stuck at a local minimum due to the random initialization of weights.
